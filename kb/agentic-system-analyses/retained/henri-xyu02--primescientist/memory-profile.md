---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'PrimeScientist memory comparison: experiment trees, retained diagnostics and
  guidance, workspace reuse, and opaque session/insight origins.'
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
source-identity: https://github.com/henri-xyu02/PrimeScientist
reviewed-boundary: 29971beac6f4f4b41309b1326762e1b83ceece98
memory-comparison:
  version: 2
  scope: Accumulated experiment-tree plans, priors/reasons, packets/statistics, winning logs
    and diagnostic reductions, failure digests, baseline history and reusable workspaces;
    cross-task insight files and copies; reflector session access metadata and opaque resumed
    payload. Includes their automatic admission, transformation, withdrawal/reset and later
    driver/reflector/worker consumer routes, including native-skill loading uncertainty and
    arbitrary workspace data/model parts. Excludes shipped static task instructions/references,
    fixed reflector/search policy, transient scoring intermediates without a later consumer,
    the disabled temporary error-analysis helper, and external model weights/runtime internals
    except the included session/native-skill memory interfaces. No deployment, benefit or
    model-weight-learning assertion.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Tree plans, statistics, proposal artifacts, outcome packets, raw logs and reductions,
          baseline history, retained workspaces, insight copies and session access metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-obj-stats
          - runtime.md#rt-obj-sandbox
          - memory.md#mem-obj-prior
          - memory.md#mem-obj-diff
          - memory.md#mem-obj-changes
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - memory.md#mem-obj-reflector-session
          - memory.md#mem-obj-insights
          - runtime.md#rt-rte-search-execution
          - memory.md#mem-rte-log-brief
          note: Inspected writes, copies, reloads and later consumers establish filesystem
            retention.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-obj-stats
        - runtime.md#rt-obj-sandbox
        - memory.md#mem-obj-prior
        - memory.md#mem-obj-diff
        - memory.md#mem-obj-changes
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - memory.md#mem-obj-reflector-session
        - memory.md#mem-obj-insights
        - runtime.md#rt-rte-search-execution
        - memory.md#mem-rte-log-brief
        note: These operative retained objects and staging copies use the filesystem; JSON
          and Markdown are encodings, not different substrates.
      - scope: External reflector session payload selected through saved session ID
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-reflector-session
        - memory.md#mem-rte-session-resume
        note: The JSON access file is inspected, but neither client/provider payload storage
          nor retention internals are inspected. No substrate value is assigned to the payload.
      records:
      - runtime.md#rt-obj-skill
      - runtime.md#rt-obj-stats
      - runtime.md#rt-obj-sandbox
      - memory.md#mem-obj-prior
      - memory.md#mem-obj-diff
      - memory.md#mem-obj-changes
      - memory.md#mem-obj-packet
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - memory.md#mem-obj-reflector-session
      - memory.md#mem-obj-insights
      - runtime.md#rt-rte-search-execution
      - memory.md#mem-rte-log-brief
      - memory.md#mem-rte-session-resume
      note: The operative file inventory is recorded; external session storage remains opaque.
        Workspace file storage does not resolve the encodings inside it.
    representational_form:
      assessment: partial
      units:
      - scope: Plans, prior reason fields, changes, insight text, packet diagnostics, log
          excerpts, rejection digest and baseline history at model interpretation paths
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - memory.md#mem-obj-changes
          - memory.md#mem-obj-insights
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-bap-plan-worker
          note: File/context routes deliver textual guidance and diagnostic material.
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-prior
          - runtime.md#rt-rte-plan-admission
          note: Requested hypothesis/rationale fields are available for later reflector interpretation;
            actual authored content and consultation are unobserved.
        records:
        - runtime.md#rt-obj-skill
        - memory.md#mem-obj-prior
        - memory.md#mem-obj-changes
        - memory.md#mem-obj-insights
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-bap-plan-worker
        note: These parts reach models as language or textual diagnostic context, not as fixed-rule
          numerical state.
      - scope: Q/P/visits, prior estimate, packet control fields, session ID/counter and executable
          workspace code at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-prior
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-reflector-session
          - runtime.md#rt-obj-sandbox
          - runtime.md#rt-bap-score-selector
          note: Python interprets fields by fixed rules and runtimes execute retained code.
        records:
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-prior
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-reflector-session
        - runtime.md#rt-obj-sandbox
        - runtime.md#rt-bap-score-selector
        note: Numeric selection, identifier handling, replay and execution have localized
          symbolic units and fixed consumer rules.
      - scope: Requested diff.py execution producing a full child plan
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-diff
          - runtime.md#rt-rte-plan-admission
          note: Reflector prompt requests Python execution; inherited delivery alone does
            not establish rerun.
        records:
        - memory.md#mem-obj-diff
        - runtime.md#rt-rte-plan-admission
        note: The script has an executable symbolic path, but execution/provenance is only
          requested, not checked.
      - scope: Task-specific data/model files within arbitrary retained workspaces
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-sandbox
        note: The mixed directory may contain additional encodings; task-specific forms and
          consumers were not inspected. No parametric classification follows from a workspace
          name.
      - scope: Restored external reflector session content and host compaction products
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - memory.md#mem-obj-reflector-session
        note: The access identifier is not a readable payload summary. Payload form and actual
          restored window remain opaque.
      records:
      - runtime.md#rt-obj-skill
      - memory.md#mem-obj-prior
      - memory.md#mem-obj-changes
      - memory.md#mem-obj-insights
      - memory.md#mem-obj-packet
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-bap-plan-worker
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-reflector-session
      - runtime.md#rt-obj-sandbox
      - runtime.md#rt-bap-score-selector
      - memory.md#mem-obj-diff
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-rte-session-resume
      note: Text and fixed-rule fields are split at their consumers. Arbitrary workspace data/model
        files and the external session payload prevent complete coverage.
    lineage:
      assessment: partial
      units:
      - scope: Reflector-created root and successor plans and requested reason/change/script
          artifacts
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-rte-plan-admission
          note: The driver delegates root/successor plan writing to the reflector.
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-prior
          - memory.md#mem-obj-changes
          - memory.md#mem-obj-diff
          note: Prompts request explicit reason, delta and transformation artifacts without
            enforcing their production.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-rte-plan-admission
        - memory.md#mem-obj-prior
        - memory.md#mem-obj-changes
        - memory.md#mem-obj-diff
        note: Model authorship is a path classification, not evidence of semantic novelty
          or observed plan quality.
      - scope: Literal retained log excerpt
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-log-brief
          - memory.md#mem-rte-log-brief
          note: Fixed head/tail extraction retains selected log lines.
        records:
        - memory.md#mem-obj-log-brief
        - memory.md#mem-rte-log-brief
        note: The brief is selected from execution output, not newly inferred content.
      - scope: Numeric statistics, outcome bookkeeping, failure digest and baseline history
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-vanilla-retention
          note: Arithmetic aggregation and deterministic formatting compile retained outcomes
            into subsequent control/guidance.
        records:
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-vanilla-retention
        note: Fixed code derives structured/formatted outputs from outcomes and reasons; derivation
          does not resolve upstream truth.
      - scope: Session access metadata parsed from Codex stdout
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-reflector-session
          - memory.md#mem-rte-session-resume
          note: The wrapper parses returned session metadata and saves it for continuation/accounting.
        records:
        - memory.md#mem-obj-reflector-session
        - memory.md#mem-rte-session-resume
        note: This refers only to identifier/counter derivation, not the provenance of session
          contents.
      - scope: Cross-task insight copies
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-insights
          - memory.md#mem-rte-insight-delivery
          note: Pre-existing benchmark insight files are copied and supplied to later consumers.
        records:
        - memory.md#mem-obj-insights
        - memory.md#mem-rte-insight-delivery
        note: Copy/import lineage is known, but original authorship and experience-derived
          publication are unresolved.
      - scope: Pre-existing raw proposal directories admitted without a fresh author call
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-prior
        - runtime.md#rt-rte-plan-admission
        note: Bootstrap establishes admission, not whether initial files were human-authored,
          model-authored or derived.
      - scope: 'Inherited code and arbitrary workspace data/model files: original derivation'
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-obj-sandbox
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-vanilla-retention
          note: Delegated coding can produce retained executable changes subsequently reused.
        records:
        - runtime.md#rt-obj-sandbox
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-vanilla-retention
        note: Worker editing and retained copies establish a code-authoring path; initial
          data/model provenance and other internal derivations remain uninspected.
      - scope: External reflector session payload provenance and compaction
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        note: External continuation is requested; transcript origins and derived host memory
          are not inspected.
      records:
      - runtime.md#rt-obj-skill
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-obj-prior
      - memory.md#mem-obj-changes
      - memory.md#mem-obj-diff
      - memory.md#mem-obj-log-brief
      - memory.md#mem-rte-log-brief
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-packet
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-rte-vanilla-retention
      - memory.md#mem-obj-reflector-session
      - memory.md#mem-rte-session-resume
      - memory.md#mem-obj-insights
      - memory.md#mem-rte-insight-delivery
      - runtime.md#rt-obj-sandbox
      note: Known generation, derivation and import paths coexist with unknown initial proposal/insight
        provenance and opaque workspace/session content.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected node plans and change explanation at coding-worker guidance consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - memory.md#mem-obj-changes
          - runtime.md#rt-bap-plan-worker
          note: Plans and read-first change instructions guide the later worker.
        records:
        - runtime.md#rt-obj-skill
        - memory.md#mem-obj-changes
        - runtime.md#rt-bap-plan-worker
        note: Standing invocation guidance is delivered through native skills or inline instructions;
          it is not procedural enforcement.
      - scope: Diagnostic packets, brief, failure digest, prior reasons and insight text at
          reflector/worker reference consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-insights
          - memory.md#mem-rte-insight-delivery
          - runtime.md#rt-rte-plan-admission
          note: Diagnostic/reference material is prepared for later interpretation.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-prior
          - runtime.md#rt-rte-plan-admission
          note: Requested durable reasons can be consulted by a later reflector.
        records:
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-prior
        - memory.md#mem-obj-insights
        - memory.md#mem-rte-insight-delivery
        - runtime.md#rt-rte-plan-admission
        note: These parts supply evidence or advice; score truth and model compliance are
          not guaranteed.
      - scope: Baseline history at subsequent worker guidance consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-vanilla-retention
          note: Formatted prior experience supplies context.
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-vanilla-retention
          note: History-as-skill carries directions for the next attempt.
        records:
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-rte-vanilla-retention
        - runtime.md#rt-bap-plan-worker
        note: Prior scores/actions and short summaries supply context, with a request to avoid
          failures and improve.
      - scope: Retained outcome/diagnostic inputs at successor-plan and history update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-plan-admission
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-obj-stats
          note: Retained results feed successor guidance, history and numerical selection-state
            updates.
        records:
        - runtime.md#rt-rte-plan-admission
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-obj-stats
        note: Experience feeds durable behavior-shaping outputs; this authority does not assert
          improved capacity.
      - scope: Q/P and admitted prior estimate at BAVT weighting consumer
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-prior
          - runtime.md#rt-bap-score-selector
          note: Fixed code weights later branch selection using Q/P.
        records:
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-prior
        - runtime.md#rt-bap-score-selector
        note: Retained numbers influence relative sampling priority, not epistemic truth probability.
      - scope: Packet presence/replay fields and session ID/counter at driver/continuation
          consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-packet
          - memory.md#mem-obj-reflector-session
          - memory.md#mem-rte-session-resume
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-vanilla-retention
          note: Control state selects later operations, continuation and input history.
        records:
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-reflector-session
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-vanilla-retention
        note: Retained fields determine execute-versus-expand, replay, continuation identity
          and budget accounting.
      - scope: Retained branch visibility and score state at selection/inheritance/keep-revert
          consumers
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-bap-score-selector
          - runtime.md#rt-rte-vanilla-retention
          - memory.md#mem-obj-pruned-children
          note: Hidden branch state and score comparisons block normal reuse/selection of
            rejected alternatives.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-obj-sandbox
          - runtime.md#rt-rte-vanilla-retention
          note: Score and retained workspace availability select the next starting state.
        records:
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-obj-sandbox
        - runtime.md#rt-bap-score-selector
        - runtime.md#rt-rte-vanilla-retention
        - memory.md#mem-obj-pruned-children
        note: The driver excludes hidden branches and conditions seed reuse/replacement on
          recorded scores. This veto is on later search use, not on earlier worker actions.
      - scope: External session payload and task-specific workspace content at opaque downstream
          consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-obj-sandbox
        note: The continuation/copy path is visible, but payload effects and arbitrary data/model
          consumers are not. Executable content alone does not justify a blanket instruction
          or learning authority for the entire workspace.
      records:
      - runtime.md#rt-obj-skill
      - memory.md#mem-obj-changes
      - runtime.md#rt-bap-plan-worker
      - memory.md#mem-obj-packet
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-prior
      - memory.md#mem-obj-insights
      - memory.md#mem-rte-insight-delivery
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-rte-vanilla-retention
      - runtime.md#rt-obj-stats
      - runtime.md#rt-bap-score-selector
      - memory.md#mem-obj-reflector-session
      - memory.md#mem-rte-session-resume
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-obj-sandbox
      note: Authority follows each consumed part, not its filename. Model effects remain guidance/affordance
        rather than observed compliance; opaque payload and workspace consumers prevent an
        exhaustive authority inventory.
    write_agency:
      assessment: partial
      units:
      - scope: Reflector plan admission, packet/statistics/artifact retention, brief/digest/history
          production and session-metadata updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-plan-admission
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-packet
          - memory.md#mem-rte-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - memory.md#mem-obj-reflector-session
          - memory.md#mem-rte-session-resume
          - runtime.md#rt-rte-vanilla-retention
          note: Driver and model own content generation/admission; launching and setting options
            are not per-entry approval.
        records:
        - runtime.md#rt-rte-plan-admission
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-packet
        - memory.md#mem-rte-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - memory.md#mem-obj-reflector-session
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-rte-vanilla-retention
        note: Inspected routes admit without per-content human approval, including score-gated
          workspace replacement.
      - scope: Insight copying/loading after files exist
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-insight-delivery
          - memory.md#mem-obj-insights
          note: Code copies and loads files on presence/filter predicates without content
            approval.
        records:
        - memory.md#mem-rte-insight-delivery
        - memory.md#mem-obj-insights
        note: Known automatic copy is independent of unresolved initial content admission.
      - scope: Initial cross-task insights and pre-existing raw proposal content admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-insights
        - memory.md#mem-obj-prior
        - runtime.md#rt-rte-plan-admission
        note: Original controller/approval is unresolved. Unknown caller identity cannot establish
          manual or automatic initial admission.
      - scope: External session content writes and compaction; arbitrary workspace data/model
          admission
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-obj-sandbox
        note: Internal host and task-specific write mechanisms were not inspected; inspected
          metadata/copy operations do not classify them.
      records:
      - runtime.md#rt-rte-plan-admission
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-packet
      - memory.md#mem-rte-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - memory.md#mem-obj-reflector-session
      - memory.md#mem-rte-session-resume
      - runtime.md#rt-rte-vanilla-retention
      - memory.md#mem-rte-insight-delivery
      - memory.md#mem-obj-insights
      - memory.md#mem-obj-prior
      - runtime.md#rt-obj-sandbox
      note: Software/model admission is automatic despite an operator launching the workflow.
        Initial raw proposals/insights and host payload writes retain unknown control; mere
        filesystem editability establishes no manual route.
    curation_operations:
      assessment: partial
      units:
      - scope: Log brief, pruning digest and bounded baseline history production
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-log-brief
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-vanilla-retention
          note: Head/tail selection, short failure excerpts and ten-entry/400-character history
            compress retained material.
        records:
        - memory.md#mem-rte-log-brief
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-rte-vanilla-retention
        note: Fixed selection/formatting reduces retained experience, even while full logs/packets
          remain on disk.
      - scope: Running Q/visits updates and strict-improvement best-workspace replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-obj-stats
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-vanilla-retention
          - runtime.md#rt-obj-sandbox
          note: Scores revise existing aggregate state and the baseline replaces its best
            retained code.
        records:
        - runtime.md#rt-obj-stats
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-vanilla-retention
        - runtime.md#rt-obj-sandbox
        note: Existing durable entries are revised by explicit arithmetic or replacement.
          A new child plan is not itself evidence of semantic synthesis.
      - scope: Score-pruned branch withdrawal retaining packet/artifact history
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - memory.md#mem-obj-pruned-children
          - runtime.md#rt-bap-score-selector
          note: Directory hiding withdraws normal search reliance without deleting history.
        records:
        - runtime.md#rt-rte-search-execution
        - memory.md#mem-obj-pruned-children
        - runtime.md#rt-bap-score-selector
        note: Hidden branches lose current normal selection eligibility while their evidence
          survives.
      - scope: Operator-requested force-init deletion of run-specific retained state
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-plan-admission
          - memory.md#mem-rte-session-resume
          note: Force-init forgets specified retained run state through deletion.
        records:
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-plan-admission
        - memory.md#mem-rte-session-resume
        note: Coarse reset removes the existing root and associated ledgers/session/logs;
          local insights/instruction survive. This is not claim-by-claim evidential withdrawal.
      - scope: Model-mediated successor-plan transformations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-plan-admission
        - memory.md#mem-obj-diff
        - memory.md#mem-obj-prior
        note: Prompts request new hypotheses and changes, but no generated content resolves
          consolidation versus synthesis or semantic evolution. Requested diff provenance
          is not an enforced transformation.
      - scope: Insight production/maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-insights
        - memory.md#mem-rte-insight-delivery
        note: Copy overwrites do not establish substantive curation; experience extraction/publication
          and evidence-based withdrawal remain unresolved.
      - scope: External session compaction and task-specific workspace maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-obj-sandbox
        note: Host compaction and arbitrary data/model update semantics were not inspected.
      records:
      - memory.md#mem-rte-log-brief
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-rte-vanilla-retention
      - runtime.md#rt-obj-stats
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-obj-sandbox
      - runtime.md#rt-bap-score-selector
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-rte-session-resume
      - memory.md#mem-obj-diff
      - memory.md#mem-obj-prior
      - memory.md#mem-obj-insights
      - memory.md#mem-rte-insight-delivery
      note: Implemented reductions, updates and withdrawal/reset are classified locally. Model
        proposal semantics, insight maintenance and external host transformations are unresolved
        rather than inferred from route names.
    read_back_direction:
      assessment: partial
      units:
      - scope: Reflector/worker explicitly requested artifact reads and driver state reloads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-packet
          note: Driver reloads retained tree and packet state.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-plan-admission
          - memory.md#mem-rte-log-brief
          - memory.md#mem-obj-prior
          - runtime.md#rt-bap-plan-worker
          note: Reflector/worker can request retained filesystem artifacts; actual model file
            reads and native loading are unobserved.
        records:
        - runtime.md#rt-rte-plan-admission
        - memory.md#mem-rte-log-brief
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-packet
        - memory.md#mem-obj-prior
        - runtime.md#rt-bap-plan-worker
        note: A consumer reading a named file fulfills its request; file availability alone
          is not another automatic delivery.
      - scope: Automatic plan/history/insight and inherited-workspace supply to a new invocation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-bap-plan-worker
          - memory.md#mem-obj-history-shown
          - memory.md#mem-rte-insight-delivery
          - runtime.md#rt-obj-sandbox
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-rte-vanilla-retention
          note: Invocation staging supplies retained guidance, prior experience and selected
            code.
        records:
        - runtime.md#rt-bap-plan-worker
        - memory.md#mem-obj-history-shown
        - memory.md#mem-rte-insight-delivery
        - runtime.md#rt-obj-sandbox
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-rte-vanilla-retention
        note: Code prepares selected retained inputs without a material request from the new
          worker.
      - scope: External reflector session restoration and native-skill body insertion
        assessment: partial
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-session-resume
          - memory.md#mem-obj-reflector-session
          note: Wrapper requests continuation by saved session identity; this does not classify
            internal host delivery.
        records:
        - memory.md#mem-rte-session-resume
        - memory.md#mem-obj-reflector-session
        - runtime.md#rt-bap-plan-worker
        note: Wrapper requests the selected session, but host window selection/restoration
          and implicit skill insertion are uninspected.
      records:
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-rte-log-brief
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-packet
      - memory.md#mem-obj-prior
      - runtime.md#rt-bap-plan-worker
      - memory.md#mem-obj-history-shown
      - memory.md#mem-rte-insight-delivery
      - runtime.md#rt-obj-sandbox
      - runtime.md#rt-rte-vanilla-retention
      - memory.md#mem-rte-session-resume
      - memory.md#mem-obj-reflector-session
      note: Both requested filesystem reads and automatic subsequent-invocation supply are
        supported. External restoration and native-skill loading add unresolved operations;
        neither known direction covers them.
    read_back_signal:
      assessment: partial
      units:
      - scope: FIRE-Bench insight supply at worker invocation
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-insight-delivery
          - memory.md#mem-obj-insights
          note: Availability/nonempty filters select the broad insight inventory without semantic
            relevance or budget inference.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-insight-delivery
          - memory.md#mem-obj-insights
          note: Current task stem is matched to exclude its own insight and deliver the other-task
            files.
        records:
        - memory.md#mem-rte-insight-delivery
        - memory.md#mem-obj-insights
        note: Trigger is worker invocation; selector uses Markdown availability, nonempty
          size, sorting and current-task identity; selected parts are other-task insight text.
      - scope: Baseline history supply at next iteration
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-vanilla-retention
          note: Recency/count/length rules select the delivered history without inferred semantic
            relevance.
        records:
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-rte-vanilla-retention
        note: Trigger is the next attempt; selector takes the last ten records and truncates
          summaries to 400 characters, then stages the selected history.
      - scope: Selected node plan and parent/best workspace staging
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-bap-score-selector
          - runtime.md#rt-rte-vanilla-retention
          note: Fixed score/availability/ancestry rules determine eligible retained inputs.
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-search-execution
          - runtime.md#rt-obj-skill
          - runtime.md#rt-obj-sandbox
          - runtime.md#rt-bap-plan-worker
          note: Selected node/parent paths actually resolve which plan/workspace bytes are
            staged, rather than merely labeling a request.
        records:
        - runtime.md#rt-rte-search-execution
        - runtime.md#rt-obj-skill
        - runtime.md#rt-obj-sandbox
        - runtime.md#rt-bap-score-selector
        - runtime.md#rt-rte-vanilla-retention
        - runtime.md#rt-bap-plan-worker
        note: Trigger is driver-selected execution; ancestry/visibility and recorded score
          eligibility precede resolving the selected node/parent or best-workspace path into
          delivered retained parts. A catalog identifier alone would not suffice.
      - scope: Native-skill selection/body insertion and external resumed-session window selection
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-bap-plan-worker
        - memory.md#mem-rte-session-resume
        - memory.md#mem-obj-reflector-session
        note: Implicit invocation configuration and saved session ID do not reveal host selectors,
          selected payload parts or restored budget. No signal is assigned to opaque content.
      records:
      - memory.md#mem-rte-insight-delivery
      - memory.md#mem-obj-insights
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-rte-vanilla-retention
      - runtime.md#rt-rte-search-execution
      - runtime.md#rt-obj-skill
      - runtime.md#rt-obj-sandbox
      - runtime.md#rt-bap-score-selector
      - runtime.md#rt-bap-plan-worker
      - memory.md#mem-rte-session-resume
      - memory.md#mem-obj-reflector-session
      note: Signals are local to automatic input preparation. Coarse filters and actual node/task
        identity matching are separate from unknown native-skill and host session selectors;
        no semantic insight retrieval is inferred.
    trace_learning:
      assessment: partial
      units:
      - scope: Log-brief, failure-digest and baseline-history writes for later model consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-log-brief
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-rte-plan-admission
          - runtime.md#rt-rte-vanilla-retention
          note: Raw retained output/outcomes feed automatic durable reductions and later reflector/worker
            context.
        records:
        - memory.md#mem-rte-log-brief
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-rte-plan-admission
        - runtime.md#rt-rte-vanilla-retention
        note: Execution experience is automatically reduced into retained diagnostic/context
          guidance delivered to subsequent invocations.
      - scope: Outcome-fed Q/visits updates and reflector successor-plan admission
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-packet
          - runtime.md#rt-bap-score-selector
          - runtime.md#rt-rte-plan-admission
          - runtime.md#rt-bap-plan-worker
          note: Trace-fed writes produce behavior-shaping numerical state and successor guidance
            with later consumers.
        records:
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-packet
        - runtime.md#rt-bap-score-selector
        - runtime.md#rt-rte-plan-admission
        - runtime.md#rt-bap-plan-worker
        note: Evaluation feedback changes durable selection state and feeds the wired proposal-to-later-worker
          path; model evidence responsiveness is not observed.
      - scope: Cross-task insight publication from completed attempts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-insights
        - memory.md#mem-rte-insight-delivery
        note: Existing file delivery is wired but its original producer and admission are
          unresolved. Neither a closed learning loop nor a local no follows.
      - scope: External session-derived host memory and task-specific workspace data/model
          updates
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-obj-sandbox
        note: Automatic trace-to-durable-artifact transformations inside those parts were
          not inspected; copied code or session access metadata alone cannot decide them.
      records:
      - memory.md#mem-rte-log-brief
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-rte-plan-admission
      - runtime.md#rt-rte-vanilla-retention
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-packet
      - runtime.md#rt-bap-score-selector
      - runtime.md#rt-bap-plan-worker
      - memory.md#mem-obj-insights
      - memory.md#mem-rte-insight-delivery
      - memory.md#mem-rte-session-resume
      - runtime.md#rt-obj-sandbox
      note: Known automatic trace-fed reductions and control/guidance updates coexist with
        unresolved insight publication and opaque host/workspace updates. Yes means a durable
        later-consumed update path, not improved capacity or a weight change.
    trace_source:
      assessment: partial
      units:
      - scope: Execution-output/verification feedback within brief, failure digest, history,
          score-state and successor-guidance update chains
        assessment: partial
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-log-brief
          - memory.md#mem-obj-log-brief
          - memory.md#mem-obj-pruned-children
          - memory.md#mem-obj-history-shown
          - runtime.md#rt-obj-stats
          - memory.md#mem-obj-packet
          - runtime.md#rt-rte-plan-admission
          note: Execution logs, verifier tails and evaluation feedback supply the automatic
            later-consumed updates.
        records:
        - memory.md#mem-rte-log-brief
        - memory.md#mem-obj-log-brief
        - memory.md#mem-obj-pruned-children
        - memory.md#mem-obj-history-shown
        - runtime.md#rt-obj-stats
        - memory.md#mem-obj-packet
        - runtime.md#rt-rte-plan-admission
        note: Recorded tool/runtime/evaluation output is supported. Logs/narratives, prior
          reasons and inherited workspace observations may mix other material; records do
          not enumerate conversational turns or linked multi-step source content.
      - scope: Cross-task insight original update inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-insights
        - memory.md#mem-rte-insight-delivery
        note: Initial producer and whether a qualifying trace-fed write occurred are unresolved,
          so no trace source can be assigned.
      - scope: External session-derived host artifacts and task-specific workspace updates
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-resume
        - runtime.md#rt-obj-sandbox
        note: Source content and qualifying internal writes are not inspected. Session ID
          alone does not establish session-logs as a source.
      records:
      - memory.md#mem-rte-log-brief
      - memory.md#mem-obj-log-brief
      - memory.md#mem-obj-pruned-children
      - memory.md#mem-obj-history-shown
      - runtime.md#rt-obj-stats
      - memory.md#mem-obj-packet
      - runtime.md#rt-rte-plan-admission
      - memory.md#mem-obj-insights
      - memory.md#mem-rte-insight-delivery
      - memory.md#mem-rte-session-resume
      - runtime.md#rt-obj-sandbox
      note: Execution feedback is a supported source for qualifying routes. Mixed agent narrative/proposal
        inputs and opaque update origins prevent a complete source enumeration; serialization
        does not establish session logs, events or trajectories.
---

# PrimeScientist memory profile

## Comparison rationale

The comparison covers retained experience and its later consumers, not every
file or model used by the workflow. All positive bases are implementation,
requested behavior or affordance, not observed operation. File staging does
not establish native-skill loading, model compliance, scientific warrant or
improved future capacity. The symbolic Q/visits route and automatic diagnostic
reductions nevertheless meet the profile's trace-learning test: they update
retained behavior-shaping state with subsequent consumers. See
[RT-OBJ-stats](runtime.md#rt-obj-stats),
[RT-BAP-score-selector](runtime.md#rt-bap-score-selector),
[MEM-RTE-log-brief](memory.md#mem-rte-log-brief), and
[MEM-OBJ-history-shown](memory.md#mem-obj-history-shown).

The file substrate does not turn every operative part into language. Numeric
priors/statistics, identifiers and executable code have symbolic consumers;
reasons and diagnostic text have interpretation paths. Arbitrary workspace
model/data files remain uninspected rather than being classified as parametric
memory. Provider weights are outside the accumulated-memory boundary because
no recorded update route brings them inside it. Session payload remains
included and opaque, independent of the inspected JSON access metadata. See
[MEM-OBJ-prior](memory.md#mem-obj-prior),
[RT-OBJ-sandbox](runtime.md#rt-obj-sandbox), and
[MEM-RTE-session-resume](memory.md#mem-rte-session-resume).

Known copying of insight files establishes imported lineage and automatic
supply, not initial authorship, human approval, experience extraction or a
closed cross-task learning loop. The current-task name match and nonempty
file filter select delivered parts without inferred relevance. Initial insight
admission remains unresolved. Existing raw proposal directories have the same
initial-control limitation even though subsequent bootstrap is automatic. See
[MEM-OBJ-insights](memory.md#mem-obj-insights),
[MEM-RTE-insight-delivery](memory.md#mem-rte-insight-delivery), and
[RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).

Head/tail excerpts, short failure digests and bounded history consolidate
retained experience. No output claim proves synthesis by the reflector:
generated proposal semantics are unavailable. Score hiding instead establishes
withdrawal of normal branch reliance while retaining history. Strict score
improvement replaces baseline code; it is not acceptance of an explanatory
claim. Trace-source coverage retains unresolved narrative and proposal inputs
rather than assigning event streams or session logs from filenames. See
[MEM-OBJ-pruned-children](memory.md#mem-obj-pruned-children),
[RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention), and
[RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).

The reconciliation supersedes EPI-OBJ-prior, EPI-OBJ-log-brief and EPI-OBJ-packet
with their MEM declarations. All profile references use the canonical memory
records; the supersessions affect reason/form/lineage, diagnostic reduction and
packet-consumer classifications, not their producing route identities. The
failed-resume recovery disagreement is retained as a limitation: neither
unconditional clearing nor a guaranteed fresh next context is asserted here.
The visible resume request supports a route, not restoration fidelity. See
[MEM-OBJ-prior](memory.md#mem-obj-prior),
[MEM-OBJ-log-brief](memory.md#mem-obj-log-brief),
[MEM-OBJ-packet](memory.md#mem-obj-packet),
[RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), and
[MEM-RTE-session-resume](memory.md#mem-rte-session-resume).

FIRE-Bench packet consumers receive normalized scores but not reference-derived
false-positive/negative diagnoses. Retention is therefore not complete diagnostic
read-back or reliable pointer dereference after pruning. Replay can also lose
conclusion-only narrative while retaining scores/actions. These limits qualify
knowledge and trace-source coverage without erasing numeric control or the
positive history route. See
[EPI-RTE-score-attachment](epistemic.md#epi-rte-score-attachment),
[MEM-OBJ-packet](memory.md#mem-obj-packet), and
[MEM-OBJ-history-shown](memory.md#mem-obj-history-shown).

Source-read log: none. Classification used only the supplied accepted members
and reconciliation; no ambiguity required a frozen-source read. Every axis
remains partial because its inventory retains unresolved included parts. No
system-wide negative or complete-value enumeration is inferred from a known
branch.
