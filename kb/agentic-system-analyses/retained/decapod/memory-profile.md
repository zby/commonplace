---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Decapod memory profile: retained repository knowledge, context artifacts, governance and
  acceptance state, with opaque internalization and untraced alternatives.'
run-id: AAS-2026-10-14-decapod-c44705119841-01
source-identity: https://github.com/DecapodLabs/decapod
reviewed-boundary: 067b8f55071e13dd103779998168b4c9ffd31a79
memory-comparison:
  version: 2
  scope: Accumulated knowledge and promotion events; federation decisions and access edges; archive originals/replacement
    summaries; LCM originals/derived summaries; aptitude preferences/prompts/observations; trajectory/Jev
    governance history; feedback; persisted context capsules/bundles; internalization payload/manifests/leases;
    authored living specs; retained session/task/workspace custody and acceptance/evaluation state. Included
    untraced decide, worker lesson, health/reflex, scheduled/evaluator, RPC trace, full spec/governance
    and remote-driver alternatives remain unresolved. Excludes shipped static constitution/host instructions,
    ordinary transient controller state, installed executable updates and external host/model/provider
    internals.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Knowledge rows, promotion events, feedback rows and LCM summary table
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-entry
          - epistemic.md#epi-obj-promotion-event
          - memory.md#mem-obj-feedback-entry
          - memory.md#mem-obj-summary-entry
          note: Knowledge and feedback/summary declarations identify SQLite or decapod.db with database
            consumers.
        records:
        - memory.md#mem-obj-knowledge-entry
        - epistemic.md#epi-obj-promotion-event
        - memory.md#mem-obj-feedback-entry
        - memory.md#mem-obj-summary-entry
        note: Canonical objects retain the SQLite information supplied by reconciled epistemic declarations;
          summary text is distinct from original events.
      - scope: LCM original stream/index, aptitude preferences/prompts/observations, federation node and
          edge tables
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-obj-preference
          - memory.md#mem-obj-agent-prompt
          - memory.md#mem-obj-observation
          - memory.md#mem-obj-federation-node
          note: Retained rows, metadata namespaces and indexed tables provide relational database storage.
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-obj-preference
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-obj-observation
        - memory.md#mem-obj-federation-node
        note: Relational tables and transactional streams are recorded; do not infer every backend implementation
          from the shared database name.
      - scope: Federation node/source/supersedes access structure
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-federation-node
          - memory.md#mem-rte-decision-memory
          note: Nodes and node_edges retain source and supersedes relationships alongside their database
            substrate.
        records:
        - memory.md#mem-obj-federation-node
        - memory.md#mem-rte-decision-memory
        note: The inspected edge structure is known; complete traversal, search and rebuild remain in
          the alternative-surface gap.
      - scope: Archive originals and replacement file; internalization payload/manifest/mount/log; bundle/capsule;
          live trajectory/Jev sections; sessions and eval JSON
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-archive-entry
          - memory.md#mem-obj-internalization-manifest
          - memory.md#mem-obj-adapter-payload
          - memory.md#mem-obj-portable-context-bundle
          - memory.md#mem-obj-trajectory-artifact
          - memory.md#mem-obj-jev-ledger
          - runtime.md#rt-obj-agent-session
          - epistemic.md#epi-obj-eval-verdict
          - epistemic.md#epi-obj-eval-aggregate
          note: Filesystem copies, JSON artifacts and adapter bytes retain the respective parts.
        records:
        - memory.md#mem-obj-archive-entry
        - memory.md#mem-obj-internalization-manifest
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-obj-portable-context-bundle
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-obj-jev-ledger
        - runtime.md#rt-obj-agent-session
        - epistemic.md#epi-obj-eval-verdict
        - epistemic.md#epi-obj-eval-aggregate
        note: These operative files are known even where custom payload semantics are opaque.
      - scope: Committed governance history, authored living specs and accepted-base executor authority
        assessment: known
        findings:
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-trajectory-artifact
          - memory.md#mem-obj-jev-ledger
          - runtime.md#rt-rte-context-resolve
          - runtime.md#rt-obj-accepted-executor
          - runtime.md#rt-rte-validate-candidate
          note: Git preserves governance versions and authored specs; accepted Git objects back executor
            identity.
        records:
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-obj-jev-ledger
        - runtime.md#rt-rte-context-resolve
        - runtime.md#rt-obj-accepted-executor
        - runtime.md#rt-rte-validate-candidate
        note: Live files and immutable repository versions are distinct retained surfaces; transient controller
          memory is not accumulated memory.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: &id001
        - memory.md#mem-rte-decision-memory
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-governance-reload
        - runtime.md#rt-rte-context-resolve
        - runtime.md#rt-rte-validate-candidate
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-obj-knowledge-entry
      - epistemic.md#epi-obj-promotion-event
      - memory.md#mem-obj-feedback-entry
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-obj-preference
      - memory.md#mem-obj-agent-prompt
      - memory.md#mem-obj-observation
      - memory.md#mem-obj-federation-node
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-obj-archive-entry
      - memory.md#mem-obj-internalization-manifest
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-obj-portable-context-bundle
      - memory.md#mem-obj-trajectory-artifact
      - memory.md#mem-obj-jev-ledger
      - runtime.md#rt-obj-agent-session
      - epistemic.md#epi-obj-eval-verdict
      - epistemic.md#epi-obj-eval-aggregate
      - runtime.md#rt-rte-context-resolve
      - runtime.md#rt-obj-accepted-executor
      - runtime.md#rt-rte-validate-candidate
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-governance-reload
      note: Files, repository versions, database tables and federation graph access have positive witnesses.
        Untraced alternative stores prevent complete inventory; external host/provider parameters are
        excluded, not classified as this memory substrate.
    representational_form:
      assessment: partial
      units:
      - scope: Readable knowledge, archive original and caller summary, LCM originals and summaries, preferences/prompts/observations,
          decision prose, trajectory prose, bundle snippets, feedback and verdict explanations
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-entry
          - memory.md#mem-obj-archive-entry
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-obj-summary-entry
          - memory.md#mem-obj-preference
          - memory.md#mem-obj-agent-prompt
          - memory.md#mem-obj-observation
          - memory.md#mem-obj-federation-node
          - memory.md#mem-obj-trajectory-artifact
          - memory.md#mem-obj-portable-context-bundle
          - memory.md#mem-obj-feedback-entry
          - epistemic.md#epi-obj-eval-verdict
          note: Hosts interpret retained prose; verdict explanation is readable but is not the numerical
            aggregate justification.
        records:
        - memory.md#mem-obj-knowledge-entry
        - memory.md#mem-obj-archive-entry
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-obj-summary-entry
        - memory.md#mem-obj-preference
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-obj-observation
        - memory.md#mem-obj-federation-node
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-obj-portable-context-bundle
        - memory.md#mem-obj-feedback-entry
        - epistemic.md#epi-obj-eval-verdict
        note: Interpretive text is classified separately from fixed-rule metadata.
      - scope: IDs, provenance/status/TTL, original hashes, indexes, prompt priorities/usage, node edges,
          trajectory check/custody state, Jev numerical ledger, manifests/leases, bundle bindings, sessions
          and eval scores/criteria
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-entry
          - memory.md#mem-obj-archive-entry
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-obj-summary-entry
          - memory.md#mem-obj-preference
          - memory.md#mem-obj-agent-prompt
          - memory.md#mem-obj-observation
          - memory.md#mem-obj-federation-node
          - memory.md#mem-obj-trajectory-artifact
          - memory.md#mem-obj-jev-ledger
          - memory.md#mem-obj-internalization-manifest
          - memory.md#mem-obj-portable-context-bundle
          - runtime.md#rt-obj-agent-session
          - epistemic.md#epi-obj-eval-verdict
          - epistemic.md#epi-obj-eval-aggregate
          - epistemic.md#epi-obj-promotion-event
          note: Structured fields and numbers are consumed by explicit selection, integrity, lifecycle
            and validation rules.
        records:
        - memory.md#mem-obj-knowledge-entry
        - memory.md#mem-obj-archive-entry
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-obj-summary-entry
        - memory.md#mem-obj-preference
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-obj-observation
        - memory.md#mem-obj-federation-node
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-obj-jev-ledger
        - memory.md#mem-obj-internalization-manifest
        - memory.md#mem-obj-portable-context-bundle
        - runtime.md#rt-obj-agent-session
        - epistemic.md#epi-obj-eval-verdict
        - epistemic.md#epi-obj-eval-aggregate
        - epistemic.md#epi-obj-promotion-event
        note: Numerical probabilities, counts and scores have localized fixed consumers, not distributed
          parameters.
      - scope: Custom internalization adapter payload encoding
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        note: The custom executable and inference loader are opaque; hashing bytes and displaying metadata
          cannot decide symbolic versus parametric representation.
      - scope: Builtin noop adapter content
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        note: Empty output carries no content to classify; the symbolic manifest remains separately included.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-obj-knowledge-entry
      - memory.md#mem-obj-archive-entry
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-obj-preference
      - memory.md#mem-obj-agent-prompt
      - memory.md#mem-obj-observation
      - memory.md#mem-obj-federation-node
      - memory.md#mem-obj-trajectory-artifact
      - memory.md#mem-obj-portable-context-bundle
      - memory.md#mem-obj-feedback-entry
      - epistemic.md#epi-obj-eval-verdict
      - memory.md#mem-obj-jev-ledger
      - memory.md#mem-obj-internalization-manifest
      - runtime.md#rt-obj-agent-session
      - epistemic.md#epi-obj-eval-aggregate
      - epistemic.md#epi-obj-promotion-event
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-governance-reload
      - runtime.md#rt-rte-context-resolve
      - runtime.md#rt-rte-validate-candidate
      note: Natural-language and symbolic parts coexist. No parametric memory value is supported by an
        adapter filename or the separate external Jev model; custom encoding and untraced alternatives
        keep coverage partial.
    lineage:
      assessment: partial
      units:
      - scope: Caller-authored knowledge/feedback/preferences/prompts, decision prose/rationale, trajectory
          declarations and archive replacement summary
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-entry
          - memory.md#mem-obj-feedback-entry
          - memory.md#mem-obj-preference
          - memory.md#mem-obj-agent-prompt
          - memory.md#mem-obj-federation-node
          - memory.md#mem-obj-trajectory-artifact
          - memory.md#mem-rte-archive-context
          note: Callers supply text or rationale rather than code inferring it.
        records:
        - memory.md#mem-obj-knowledge-entry
        - memory.md#mem-obj-feedback-entry
        - memory.md#mem-obj-preference
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-obj-federation-node
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-rte-archive-context
        note: Authored describes content production, not authenticated human control; actual prompt initialization
          is unresolved.
      - scope: LCM verbatim file/stdin ingestion and archive copied original
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-obj-archive-entry
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-rte-archive-context
          note: Existing caller file/event content is copied into retained originals.
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-obj-archive-entry
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-rte-archive-context
        note: The acquisition path is known; source authenticity and original authorship are not thereby
          established.
      - scope: Imported external eval verdict success and explanation
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - epistemic.md#epi-obj-eval-verdict
          - epistemic.md#epi-rte-eval-judge-import
          note: Judge parses supplied JSON and retains its verdict fields.
        records:
        - epistemic.md#epi-obj-eval-verdict
        - epistemic.md#epi-rte-eval-judge-import
        note: Model attribution is copied metadata, not a model invocation.
      - scope: Handoff-derived text and LCM interaction/tool-event prefix
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-handoff-memory
          note: Successful handoff activity is formatted into durable knowledge and an observation.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Recorded interaction/tool content supplies automatic chronological extracts.
        records:
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-obj-summary-entry
        note: Known trace-derived branches coexist with LCM artifact/mixed inputs whose original provenance
          is not resolved.
      - scope: Compiled bundle/capsule, governance normalization, Jev ledger, eval aggregate and internalization
          metadata
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-bundle-transfer
          - memory.md#mem-obj-portable-context-bundle
          - memory.md#mem-rte-governance-reload
          - memory.md#mem-obj-jev-ledger
          - epistemic.md#epi-rte-eval-statistics
          - epistemic.md#epi-obj-eval-aggregate
          - memory.md#mem-obj-internalization-manifest
          - memory.md#mem-rte-internalization-lease
          note: Selection, hashing, normalization, redaction and numerical aggregation produce durable
            structures.
        records:
        - memory.md#mem-rte-bundle-transfer
        - memory.md#mem-obj-portable-context-bundle
        - memory.md#mem-rte-governance-reload
        - memory.md#mem-obj-jev-ledger
        - epistemic.md#epi-rte-eval-statistics
        - epistemic.md#epi-obj-eval-aggregate
        - memory.md#mem-obj-internalization-manifest
        - memory.md#mem-rte-internalization-lease
        note: Fixed code constructs these derived parts; this does not classify custom adapter semantics.
      - scope: Custom adapter derivation and actual prompt/spec initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-obj-agent-prompt
        - runtime.md#rt-rte-context-resolve
        note: A local source-to-executable route is known but payload derivation and initial text provenance
          are not; no complete authored/imported/parametric lineage follows.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-obj-knowledge-entry
      - memory.md#mem-obj-feedback-entry
      - memory.md#mem-obj-preference
      - memory.md#mem-obj-agent-prompt
      - memory.md#mem-obj-federation-node
      - memory.md#mem-obj-trajectory-artifact
      - memory.md#mem-rte-archive-context
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-obj-archive-entry
      - memory.md#mem-rte-lcm-summary
      - epistemic.md#epi-obj-eval-verdict
      - epistemic.md#epi-rte-eval-judge-import
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-rte-bundle-transfer
      - memory.md#mem-obj-portable-context-bundle
      - memory.md#mem-rte-governance-reload
      - memory.md#mem-obj-jev-ledger
      - epistemic.md#epi-rte-eval-statistics
      - epistemic.md#epi-obj-eval-aggregate
      - memory.md#mem-obj-internalization-manifest
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-obj-adapter-payload
      - runtime.md#rt-rte-context-resolve
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-aptitude-reminders
      - runtime.md#rt-rte-validate-candidate
      note: Known authored, imported, trace-extracted and compiled paths are retained independently. Initialization
        and opaque production gaps do not erase subsequent derivations.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Knowledge/decision/archive/LCM/feedback and observation content at requesting host; trajectory
          at assurance; bundle snippets and living specs at host
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-store
          - memory.md#mem-rte-decision-memory
          - memory.md#mem-rte-archive-context
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-rte-feedback-proposal
          - memory.md#mem-rte-aptitude-reminders
          - memory.md#mem-rte-governance-reload
          - memory.md#mem-rte-bundle-transfer
          - runtime.md#rt-rte-context-resolve
          note: Returned content supplies reference, evidence or context to the host; assurance receives
            retained trajectory context.
        records:
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-rte-decision-memory
        - memory.md#mem-rte-archive-context
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-governance-reload
        - memory.md#mem-rte-bundle-transfer
        - runtime.md#rt-rte-context-resolve
        note: Context/advice delivery establishes the implemented channel, not observed reliance or truth.
      - scope: Retained aptitude prompt and preference directions at host reminder consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-agent-prompt
          - memory.md#mem-obj-preference
          - memory.md#mem-rte-aptitude-reminders
          note: Prompt/remind returns standing prompt text and preference values as host guidance.
        records:
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-obj-preference
        - memory.md#mem-rte-aptitude-reminders
        note: Standing directions are distinct from their selection metadata; host compliance is unobserved.
      - scope: Prompt priority/usage; knowledge optional recency fields; federation update order
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-aptitude-reminders
          note: Prompt priority/usage controls order and tie breaks; rendered confidence alone is not
            assigned ranking.
        - value: ranking
          basis: afforded
          records:
          - epistemic.md#epi-rte-knowledge-select
          note: Retained creation age affects optional recency scoring in library search.
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-decision-memory
          note: Retained updated time controls decision listing priority.
        records:
        - memory.md#mem-rte-aptitude-reminders
        - epistemic.md#epi-rte-knowledge-select
        - memory.md#mem-rte-decision-memory
        note: Each ranking finding names the recorded ordering input; no outcome-driven learned ranker
          is inferred.
      - scope: Knowledge status, prompt active/context, session identity/expiry and workspace assignments;
          same-run governance ledger association
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-store
          - memory.md#mem-rte-aptitude-reminders
          note: Status and context/category metadata select eligible retained content.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-session-custody
          - runtime.md#rt-rte-workspace-ensure
          - memory.md#mem-rte-governance-reload
          note: Session/task/run identity selects custody, work scope and ledger append/reset behavior.
        records:
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-rte-aptitude-reminders
        - runtime.md#rt-rte-session-custody
        - runtime.md#rt-rte-workspace-ensure
        - memory.md#mem-rte-governance-reload
        note: Retained state chooses delivered scope or continuation. Consumers/effects are not generalized
          to all commands.
      - scope: Promotion event at procedural add; archive index/budget inputs; internalization manifest/lease
          at attach and validation; bundle bindings at import; eval requirement/aggregate at publisher;
          accepted executor and retained proof at readiness
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-obj-promotion-event
          - epistemic.md#epi-rte-promotion-record
          - memory.md#mem-rte-promotion-lifecycle
          - memory.md#mem-obj-internalization-manifest
          - memory.md#mem-rte-internalization-lease
          - memory.md#mem-rte-bundle-transfer
          - epistemic.md#epi-obj-eval-aggregate
          - epistemic.md#epi-rte-eval-promotion-gate
          - runtime.md#rt-obj-accepted-executor
          - runtime.md#rt-rte-validate-candidate
          note: Stored event fields, artifact/policy bindings and aggregate/executor requirements determine
            admissibility.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-obj-promotion-event
          - epistemic.md#epi-rte-promotion-record
          - memory.md#mem-rte-promotion-lifecycle
          - memory.md#mem-rte-archive-context
          - memory.md#mem-obj-internalization-manifest
          - memory.md#mem-rte-internalization-lease
          - memory.md#mem-rte-bundle-transfer
          - epistemic.md#epi-obj-eval-aggregate
          - epistemic.md#epi-rte-eval-promotion-gate
          - runtime.md#rt-obj-accepted-executor
          - runtime.md#rt-rte-validate-candidate
          note: Failed retained criteria or restore budget reject the covered admission/read/publication
            transition.
        records:
        - epistemic.md#epi-obj-promotion-event
        - epistemic.md#epi-rte-promotion-record
        - memory.md#mem-rte-promotion-lifecycle
        - memory.md#mem-rte-archive-context
        - memory.md#mem-obj-internalization-manifest
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-bundle-transfer
        - epistemic.md#epi-obj-eval-aggregate
        - epistemic.md#epi-rte-eval-promotion-gate
        - runtime.md#rt-obj-accepted-executor
        - runtime.md#rt-rte-validate-candidate
        note: These retained parts supply actual fixed criteria and executable vetoes. A hash read alone
          does not make adapter semantic content a criterion.
      - scope: LCM recorded interaction/tool originals at automatic summary update; handoff activity at
          durable knowledge derivation
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-rte-handoff-memory
          note: Recorded experience feeds automatic durable context artifacts with later summary/search
            consumers.
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-rte-handoff-memory
        note: Learning authority is local to experience-fed durable artifact production, independent of
          improvement or host adoption.
      - scope: Custom adapter at hypothetical inference consumer; full policy/spec authority and untraced
          coordination consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - runtime.md#rt-rte-context-resolve
        - runtime.md#rt-rte-workspace-ensure
        - runtime.md#rt-rte-validate-candidate
        note: Integrity/mount consumers are known above; parameter loading, full policy provenance and
          other effects remain uninspected.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-rte-knowledge-store
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-archive-context
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-governance-reload
      - memory.md#mem-rte-bundle-transfer
      - runtime.md#rt-rte-context-resolve
      - memory.md#mem-obj-agent-prompt
      - memory.md#mem-obj-preference
      - epistemic.md#epi-rte-knowledge-select
      - runtime.md#rt-rte-session-custody
      - runtime.md#rt-rte-workspace-ensure
      - epistemic.md#epi-obj-promotion-event
      - epistemic.md#epi-rte-promotion-record
      - memory.md#mem-rte-promotion-lifecycle
      - memory.md#mem-obj-internalization-manifest
      - memory.md#mem-rte-internalization-lease
      - epistemic.md#epi-obj-eval-aggregate
      - epistemic.md#epi-rte-eval-promotion-gate
      - runtime.md#rt-obj-accepted-executor
      - runtime.md#rt-rte-validate-candidate
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-obj-adapter-payload
      note: Knowledge, instruction, ranking, routing, validation, enforcement and learning each name retained
        parts and actual consumers. Excluded static constitution does not establish retained instruction;
        partial custom/alternative consumers prevent a system-complete authority account.
    write_agency:
      assessment: partial
      units:
      - scope: LCM derived summary admission after requested summarize
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Code transforms selected originals and admits summary without a human content decision.
        records:
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-obj-summary-entry
        note: Starting the operation is not per-content approval of the generated prefix.
      - scope: Successful handoff knowledge/observation admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-handoff-memory
          note: Status ok triggers retained formatted knowledge and observation without human per-content
            approval.
        records:
        - memory.md#mem-rte-handoff-memory
        note: Caller authors summary but software independently admits the derived content; writes are
          best effort.
      - scope: Jev ledger append, governance normalization, session reacquisition, generated readiness
          healing, bundle export and internalization manifest/noop writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-governance-reload
          - memory.md#mem-obj-jev-ledger
          - runtime.md#rt-rte-session-custody
          - runtime.md#rt-rte-validate-candidate
          - memory.md#mem-rte-bundle-transfer
          - memory.md#mem-rte-internalization-lease
          note: Software constructs and admits derived structures, receipts/projections or leases after
            workflow requests.
        records:
        - memory.md#mem-rte-governance-reload
        - memory.md#mem-obj-jev-ledger
        - runtime.md#rt-rte-session-custody
        - runtime.md#rt-rte-validate-candidate
        - memory.md#mem-rte-bundle-transfer
        - memory.md#mem-rte-internalization-lease
        note: Known software-produced structures are separated from caller semantic admissions and opaque
          custom output.
      - scope: Eval statistics aggregate admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-eval-statistics
          - epistemic.md#epi-obj-eval-aggregate
          note: Calculation automatically writes the derived numerical artifact.
        records:
        - epistemic.md#epi-rte-eval-statistics
        - epistemic.md#epi-obj-eval-aggregate
        note: The caller selects settings, not each generated aggregate value.
      - scope: Explicit knowledge/promotion/decision/preference/prompt/feedback/trajectory content and
          archive summary/replacement; LCM raw ingestion; external eval verdict and gate requirement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-rte-promotion-lifecycle
        - memory.md#mem-rte-decision-memory
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-obj-agent-prompt
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-governance-reload
        - memory.md#mem-rte-archive-context
        - memory.md#mem-rte-lcm-summary
        - epistemic.md#epi-rte-eval-judge-import
        - epistemic.md#epi-rte-eval-promotion-gate
        note: Generic callers, approver strings and workflow starts do not establish an explicit human
          decision. Software field validation alone does not resolve content control.
      - scope: Configured internalizer custom payload admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        note: Executable production is known, but its semantic admission mechanism and possible approval
          step are opaque.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-rte-governance-reload
      - memory.md#mem-obj-jev-ledger
      - runtime.md#rt-rte-session-custody
      - runtime.md#rt-rte-validate-candidate
      - memory.md#mem-rte-bundle-transfer
      - memory.md#mem-rte-internalization-lease
      - epistemic.md#epi-rte-eval-statistics
      - epistemic.md#epi-obj-eval-aggregate
      - memory.md#mem-rte-knowledge-store
      - memory.md#mem-rte-promotion-lifecycle
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-obj-agent-prompt
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-archive-context
      - epistemic.md#epi-rte-eval-judge-import
      - epistemic.md#epi-rte-eval-promotion-gate
      - memory.md#mem-obj-adapter-payload
      - runtime.md#rt-rte-context-resolve
      note: Several derived admissions are automatic. No manual value is supported solely by caller identity,
        human intent or approved_by text; explicit content admission and custom producer control remain
        unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: LCM chronological prefix over retained originals
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Selected retained originals are combined and reduced into a durable context extract; no
            new claim need be inferred.
        records:
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-obj-summary-entry
        note: Fixed formatting and prefix reduction constitute consolidation in this comparison vocabulary;
          semantic fidelity and operation success remain unobserved.
      - scope: Preference category/key replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-preference
          - memory.md#mem-rte-aptitude-reminders
          note: Upsert overwrites an existing category/key value.
        records:
        - memory.md#mem-obj-preference
        - memory.md#mem-rte-aptitude-reminders
        note: This revises an existing preference; aptitude consolidate command itself has no content
          mutation.
      - scope: Knowledge conflict overwrite and supersession; valid federation edit/supersession
        assessment: known
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-rte-promotion-lifecycle
          - memory.md#mem-rte-decision-memory
          note: Library overwrite/edit revises existing retained content.
        - value: invalidate
          basis: afforded
          records:
          - memory.md#mem-rte-promotion-lifecycle
          - memory.md#mem-rte-decision-memory
          note: Supersession keeps history/lineage while withdrawing active reliance.
        records:
        - memory.md#mem-rte-promotion-lifecycle
        - memory.md#mem-rte-decision-memory
        note: Inspected library transformations are afforded, not automatically scheduled or necessarily
          available through basic RPC writes.
      - scope: Knowledge expiry staling and recency downweighting
        assessment: known
        findings:
        - value: decay
          basis: afforded
          records:
          - memory.md#mem-rte-promotion-lifecycle
          - epistemic.md#epi-rte-knowledge-withdraw
          note: Invoked expiry maintenance marks expiring rows stale.
        - value: decay
          basis: afforded
          records:
          - epistemic.md#epi-rte-knowledge-select
          note: Optional recency scoring downweights older retained rows.
        - value: invalidate
          basis: afforded
          records:
          - memory.md#mem-rte-promotion-lifecycle
          - epistemic.md#epi-rte-knowledge-withdraw
          note: Stale status withdraws search eligibility while retaining rows.
        records:
        - memory.md#mem-rte-promotion-lifecycle
        - epistemic.md#epi-rte-knowledge-select
        - epistemic.md#epi-rte-knowledge-withdraw
        note: No shipped decay caller is established; persistent default entries do not expire via this
          selection.
      - scope: Archive caller summary, custom adapter transformation, feedback adoption and untraced consolidation/remediation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-archive-context
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-aptitude-reminders
        note: Software file copying does not establish summary authorship as an implemented consolidation;
          opaque payload production and unimplemented placeholder adoption cannot establish synthesize/promote/dedup.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-obj-preference
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-promotion-lifecycle
      - memory.md#mem-rte-decision-memory
      - epistemic.md#epi-rte-knowledge-select
      - epistemic.md#epi-rte-knowledge-withdraw
      - memory.md#mem-rte-archive-context
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-rte-governance-reload
      - runtime.md#rt-rte-context-resolve
      - runtime.md#rt-rte-validate-candidate
      note: Consolidation, evolution, invalidation and decay have local warrants. Promotion event recording
        does not itself raise a knowledge row tier; reference-list dedup and index rebuild are not deduplication
        of retained claims. Other curation remains unresolved, not absent.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested knowledge/decision search, archive restore, LCM summary/show, aptitude reminder/pending,
          feedback proposal, bundle import and current spec resolution
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-store
          - memory.md#mem-rte-decision-memory
          - memory.md#mem-rte-archive-context
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-rte-aptitude-reminders
          - memory.md#mem-rte-feedback-proposal
          - memory.md#mem-rte-bundle-transfer
          - runtime.md#rt-rte-context-resolve
          note: Calling host asks for retained material and receives selected content by value.
        records:
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-rte-decision-memory
        - memory.md#mem-rte-archive-context
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-bundle-transfer
        - runtime.md#rt-rte-context-resolve
        note: Request, internal selection and returned delivery form one pull chain, not an extra push.
      - scope: Requested assurance/trajectory and structural session, artifact, ledger, evaluation and
          readiness consumers
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-governance-reload
          - runtime.md#rt-rte-session-custody
          - memory.md#mem-rte-internalization-lease
          - epistemic.md#epi-rte-eval-statistics
          - epistemic.md#epi-rte-eval-promotion-gate
          - runtime.md#rt-rte-validate-candidate
          note: Later requested invocations load retained governance, custody, artifacts and criteria
            needed to return their result.
        records:
        - memory.md#mem-rte-governance-reload
        - runtime.md#rt-rte-session-custody
        - memory.md#mem-rte-internalization-lease
        - epistemic.md#epi-rte-eval-statistics
        - epistemic.md#epi-rte-eval-promotion-gate
        - runtime.md#rt-rte-validate-candidate
        note: Request-owned operations reload retained inputs as part of fulfillment; unsolicited model
          supply is not established.
      - scope: Custom inference loader, RPC trace consumers and scheduler/reflex/worker-lesson delivery
          alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-governance-reload
        note: Known metadata reload and automatic writes do not decide opaque inference supply or untraced
          later-consumer direction.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-rte-knowledge-store
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-archive-context
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-bundle-transfer
      - runtime.md#rt-rte-context-resolve
      - memory.md#mem-rte-governance-reload
      - runtime.md#rt-rte-session-custody
      - memory.md#mem-rte-internalization-lease
      - epistemic.md#epi-rte-eval-statistics
      - epistemic.md#epi-rte-eval-promotion-gate
      - runtime.md#rt-rte-validate-candidate
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-handoff-memory
      note: All classified read-back chains are pull. No positive push witness is recorded, but included
        alternative consumers remain uninspected, preventing a complete pull-only or absent-push assertion.
    read_back_signal:
      assessment: uninspected
      units:
      - scope: Fully inspected requested text and structural reload chains
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-rte-decision-memory
        - memory.md#mem-rte-archive-context
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-bundle-transfer
        - runtime.md#rt-rte-context-resolve
        - memory.md#mem-rte-governance-reload
        - runtime.md#rt-rte-session-custody
        - epistemic.md#epi-rte-eval-statistics
        - epistemic.md#epi-rte-eval-promotion-gate
        note: Signal classifies push selection only. Identifiers/lexical matching on requested pull returns
          are not push signals.
      - scope: Opaque inference and untraced automatic/scheduled later-consumer alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-governance-reload
        - runtime.md#rt-rte-validate-candidate
        note: No recorded push selector trigger/input/selected payload is available for these included
          alternatives; identifiers on manifests or requested files cannot fill the gap.
      records:
      - memory.md#mem-rte-knowledge-store
      - memory.md#mem-rte-decision-memory
      - memory.md#mem-rte-archive-context
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-bundle-transfer
      - runtime.md#rt-rte-context-resolve
      - memory.md#mem-rte-governance-reload
      - runtime.md#rt-rte-session-custody
      - epistemic.md#epi-rte-eval-statistics
      - epistemic.md#epi-rte-eval-promotion-gate
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-rte-handoff-memory
      - runtime.md#rt-rte-validate-candidate
      note: No controlled push-signal finding is established. Partial direction coverage prevents axis
        inapplicability; unresolved alternatives remain uninspected even though known pull units are inapplicable.
    trace_learning:
      assessment: partial
      units:
      - scope: LCM interaction/tool originals to automatic durable prefix to later requested summary consumer
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Recorded interaction/tool activity feeds an automatic retained summary later delivered
            as context.
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-obj-summary-entry
        note: This qualifies for trace-fed durable context writing despite deterministic formatting and
          no demonstrated improvement. Artifact/nontrace input alternatives remain unresolved.
      - scope: Successful task handoff activity to persistent formatted knowledge to later search/pending
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-handoff-memory
          - memory.md#mem-rte-knowledge-store
          - memory.md#mem-obj-observation
          note: Handoff experience is automatically retained as knowledge/observation with later search
            or pending delivery.
        records:
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-rte-knowledge-store
        - memory.md#mem-obj-observation
        note: Automatic best-effort admission and later consumer route establish wiring, not execution
          success or automatic recipient injection.
      - scope: Trace origin and behavioral update in caller trajectory, Jev history, feedback/pattern
          proposals, eval, custom adapters and worker/scheduled remediation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-trajectory-artifact
        - memory.md#mem-obj-jev-ledger
        - memory.md#mem-rte-governance-reload
        - memory.md#mem-rte-feedback-proposal
        - memory.md#mem-rte-aptitude-reminders
        - epistemic.md#epi-rte-eval-judge-import
        - epistemic.md#epi-rte-eval-statistics
        - epistemic.md#epi-rte-eval-promotion-gate
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-handoff-memory
        note: Curated declarations, raw retention and fixed statistics do not establish a complete qualifying
          automatic experience-to-behavior update. Custom/worker/remediation writes and future consumers
          are unresolved; no bounded absence record licenses no.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-rte-knowledge-store
      - memory.md#mem-obj-observation
      - memory.md#mem-obj-trajectory-artifact
      - memory.md#mem-obj-jev-ledger
      - memory.md#mem-rte-governance-reload
      - memory.md#mem-rte-feedback-proposal
      - memory.md#mem-rte-aptitude-reminders
      - epistemic.md#epi-rte-eval-judge-import
      - epistemic.md#epi-rte-eval-statistics
      - epistemic.md#epi-rte-eval-promotion-gate
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-rte-decision-memory
      - runtime.md#rt-rte-context-resolve
      - runtime.md#rt-rte-validate-candidate
      note: Two local automatic trace-fed context routes support yes. This comparison classification neither
        claims improved capacity nor contradicts unobserved learning/adoption in the reports. Other included
        routes cannot be assigned a blanket no.
    trace_source:
      assessment: partial
      units:
      - scope: LCM qualifying recorded interaction originals
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Recorded conversational interaction content can feed the durable summary.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-lcm-event
          - memory.md#mem-rte-lcm-summary
          - memory.md#mem-obj-summary-entry
          note: Recorded tool activity/content can feed the same automatic summary.
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-rte-lcm-summary
        - memory.md#mem-obj-summary-entry
        note: Interaction/tool content is recorded, but exact imported originals and mixed artifact provenance
          are not supplied; these are qualifying content branches, not authentication of every event.
      - scope: Task handoff qualifying activity and supplied summary
        assessment: partial
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-rte-handoff-memory
          note: Successful task handoff event and its from/to/task/summary fields feed formatted durable
            memory.
        records:
        - memory.md#mem-rte-handoff-memory
        note: The task handoff is a discrete coordination event. The summary may contain additional sources
          but its actual original content/provenance is not resolved.
      - scope: LCM artifact inputs and custom/worker/reflex/eval/governance alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-lcm-event
        - memory.md#mem-obj-adapter-payload
        - memory.md#mem-rte-internalization-lease
        - memory.md#mem-rte-handoff-memory
        - memory.md#mem-rte-aptitude-reminders
        - memory.md#mem-rte-governance-reload
        - epistemic.md#epi-rte-eval-judge-import
        - epistemic.md#epi-rte-eval-statistics
        note: Artifact labels do not establish trajectories/session origin. Custom executable inputs and
          untraced lesson/remediation consumers cannot be classified; no global inapplicability follows
          from known nonqualifying examples.
      - scope: Included decide producer and federation graph maintenance; worker lessons; health/reflex
          remediation; scheduled maintenance/evaluation; RPC trace consumers; spec/override initialization;
          full plans/claims/checkpoints and remote driver evidence
        assessment: uninspected
        findings: []
        records: *id001
        note: The accepted inventory names these available but untraced alternatives. Their retained parts,
          admission, transformations and later consumers lack complete recorded facts; no complete system
          value inventory follows. References identify the neighboring established mechanisms, not invented
          records for missing parts.
      records:
      - memory.md#mem-obj-lcm-event
      - memory.md#mem-rte-lcm-summary
      - memory.md#mem-obj-summary-entry
      - memory.md#mem-rte-handoff-memory
      - memory.md#mem-obj-adapter-payload
      - memory.md#mem-rte-internalization-lease
      - memory.md#mem-rte-aptitude-reminders
      - memory.md#mem-rte-governance-reload
      - epistemic.md#epi-rte-eval-judge-import
      - epistemic.md#epi-rte-eval-statistics
      - memory.md#mem-rte-decision-memory
      - runtime.md#rt-rte-context-resolve
      - runtime.md#rt-rte-validate-candidate
      note: Session-log, tool-trace and handoff event sources have local qualifying paths. Mixed inputs
        and opaque alternatives prevent complete enumeration; no trajectories value follows from a trajectory-named
        curated declaration alone.
---

# Decapod memory profile

## Comparison rationale

The inventory separates retained content from its access and admission metadata. It includes coordination and acceptance memory where later invocations consume it, but not the runtime's entire filesystem or external model weights. Static constitution delivery does not make shipped instructions accumulated memory. Live governance files and Git history are separate storage paths; the transient accepted-executor object is not an in-memory memory classification, although retained accepted-base Git authority is included ([RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor), [MEM-OBJ-trajectory-artifact](memory.md#mem-obj-trajectory-artifact)).

All positive findings are architectural, not observed operation or benefit. The inventory remains partial because the accepted reports explicitly retain untraced decide, federation graph, worker lesson, health/reflex, scheduled/evaluator, RPC-trace, spec initialization, full governance and remote-driver routes. The repeated unresolved unit keeps these included parts visible; its references identify adjacent accepted records, not nonexistent declarations for omitted mechanisms. No source fact outside those records establishes a value.

Reconciliation canonicalizes the duplicated knowledge, internalization manifest/payload, feedback and LCM-summary objects to memory declarations. It also canonicalizes internalization lifecycle and feedback proposal routes to memory declarations. These supersessions change citation destinations, not evidence strength or opaque-payload coverage. The epistemic promotion event, knowledge selection/withdrawal and evaluation parts remain distinct; LCM and knowledge routes that merely overlap remain separate. SQLite information from reconciled object declarations is preserved in the canonical object classification; the other recorded relational tables are classified as rdbms without claiming unacquired backend internals.

Requested returns remain pull even when fixed code chooses a prefix, ranks rows or performs budget checks. A requested archive ID, active prompt context, original hash or bundle path does not establish identifier-based push. Consequently read_back_signal has inapplicable local pull units but an uninspected axis: included alternative consumers prevent a completely assessed pull-only boundary ([MEM-RTE-archive-context](memory.md#mem-rte-archive-context), [MEM-RTE-aptitude-reminders](memory.md#mem-rte-aptitude-reminders), [MEM-RTE-internalization-lease](memory.md#mem-rte-internalization-lease)).

The LCM prefix qualifies as consolidation because code combines retained originals into a reduced representation of their existing content. The memory report's distinction from semantic summarization is retained: truncation may omit qualifications and unsafe slicing may fail. Neither defect implies synthesis. The qualifying interaction/tool branches also support trace_learning yes: automatic durable summary production and later requested context delivery suffice, without improvement evidence. Handoff has a separate trace-fed knowledge route, sourced from discrete coordination activity; its caller summary's additional provenance remains unresolved ([MEM-RTE-lcm-summary](memory.md#mem-rte-lcm-summary), [EPI-RTE-lcm-summary](epistemic.md#epi-rte-lcm-summary), [MEM-RTE-handoff-memory](memory.md#mem-rte-handoff-memory)). Learning authority at those update consumers and knowledge authority at later context consumers are separate findings.

The promotion event records an alleged approver and is later a procedural-admission criterion. It does not itself promote an existing knowledge row or authenticate human approval. Thus it supports validation/enforcement, not an automatic promote operation or manual agency. Library expiry/conflict/recency transformations retain afforded findings beside wired ordinary reads and promotion checks; no scheduled decay is asserted ([EPI-RTE-promotion-record](epistemic.md#epi-rte-promotion-record), [MEM-RTE-promotion-lifecycle](memory.md#mem-rte-promotion-lifecycle), [EPI-RTE-knowledge-withdraw](epistemic.md#epi-rte-knowledge-withdraw)).

Opaque custom adapter bytes retain known file storage but unknown representation, derivation and inference effect. The noop alternative has empty content, while manifest and lease fields are symbolic with actual integrity/admission consumers. Neither a behavior-changing label nor a metadata attach supplies a parametric finding, a training route or an inference-context push ([MEM-OBJ-adapter-payload](memory.md#mem-obj-adapter-payload), [MEM-RTE-internalization-lease](memory.md#mem-rte-internalization-lease)).

No new source reads were made. Classification used only supplied accepted reports, their annotations and reconciliation. No records, quotations or new evidence were added; no report verification was reopened.
