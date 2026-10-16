---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "JEPA-Anything memory profile: retained task-design products, numerical history and publication metadata at the frozen builder boundary."
run-id: "AAS-2026-10-15-jepa-anything-434b01ab7774-01"
source-identity: "https://github.com/Gen-Verse/JEPA-Anything"
reviewed-boundary: "c6e6c88f3ef75a4ce7acd660d6fa5779d995512c"
memory-comparison:
  version: 2
  scope: "Includes use-produced design/configuration/assumption and generated-package parts, retained diagnostics, Welford history, mutable projection/EMA module state and maintained checkpoint provenance. Includes their documented alternative writes and later consumers, retaining unresolved initial numerical provenance and future checkpoint-consumer limits. Excludes shipped static Skill/reference methodology, enclosing host/provider internals and session management, ordinary current-call rollout states, and unpublished checkpoint payloads that do not exist in the current entry. Optional report files remain in inventory without an invented later consumer."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Task design files, normalized configuration, generated programs, documentation and copied diagnostics/file list"
          assessment: "partial"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-design-config"
                - "runtime.md#rt-obj-scaffold-manifest"
                - "runtime.md#rt-rte-scaffold-admission"
                - "epistemic.md#epi-rte-design-diagnostics"
              note: "The loader reads JSON/YAML; rendering persists a directory and standalone diagnostics can be written to a file."
          records:
            - "runtime.md#rt-obj-design-config"
            - "runtime.md#rt-obj-scaffold-manifest"
            - "runtime.md#rt-rte-scaffold-admission"
            - "epistemic.md#epi-rte-design-diagnostics"
          note: "Filesystem persistence is wired. Missing separate diagnostic, executable-contract and file-list object declarations prevent complete part-level coverage."
        - scope: "OnlineVarianceTracker count, mean and M2"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Historical sufficient statistics reside in local tensor buffers."
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "Registered buffers retain history across monitor calls; a state_dict example does not establish disk save/reload."
        - scope: "Projection basis and EMA target-encoder parameters"
          assessment: "known"
          findings:
            - value: "model-weights"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
                - "memory.md#mem-cmp-target-encoder"
              note: "Learnable projection rows and target-encoder parameters are retained model state."
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
                - "memory.md#mem-cmp-target-encoder"
                - "runtime.md#rt-rte-core-projection"
              note: "Fixed projection rows and target-module buffers are retained in process; no numeric checkpoint writer is established."
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Local tensor/module storage is specified even though actual values and original training provenance are not."
        - scope: "Checkpoint publication/provenance metadata"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
              note: "The maintained publication manifest resides in the source repository."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
              note: "The verifier reads the retained JSON manifest."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
          note: "The current JSON entry is repository metadata, not binary checkpoint storage."
        - scope: "Optional recipe and verifier diagnostic reports"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structural-checks"
              note: "Caller-selected output files retain derived audit results."
          records:
            - "runtime.md#rt-rte-structural-checks"
          note: "Optional writes establish file persistence, not an automatic later reader."
      records:
        - "runtime.md#rt-obj-design-config"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "runtime.md#rt-rte-scaffold-admission"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
      note: "The recorded products and numerical state have classified storage. The package and diagnostic containers lack separately declared material parts; no uniform payload or consumer account is inferred from those containers."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Task summary and compiler assumptions retained inside copied configuration"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-compiler-assumptions"
              note: "The host is instructed to record task facts and reversible design choices in prose."
          records:
            - "memory.md#mem-obj-compiler-assumptions"
          note: "The requested text is preserved if supplied; no later semantic reload is established."
        - scope: "Configuration fields, generated executable contracts, diagnostics and file-list fields"
          assessment: "partial"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-design-config"
                - "epistemic.md#epi-obj-claims"
                - "epistemic.md#epi-rte-template-specialization"
              note: "Mappings and literal substitutions supply fixed-rule consumers."
          records:
            - "runtime.md#rt-obj-design-config"
            - "runtime.md#rt-obj-scaffold-manifest"
            - "epistemic.md#epi-obj-claims"
            - "epistemic.md#epi-rte-template-specialization"
          note: "Fixed-rule fields are established; separate generated-program, file-list and diagnostic object declarations are missing. Package prose is not treated as executable data."
        - scope: "Generated documentation and comments"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-scaffold-manifest"
              note: "Rendered documentation and comments remain natural-language material, not parametric state."
          records:
            - "runtime.md#rt-obj-scaffold-manifest"
          note: "The package record explicitly distinguishes prose from symbolic Python/configuration."
        - scope: "Count, mean and M2 at the Welford consumer"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Localized sufficient statistics have fixed merge and penalty rules."
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "Numeric encoding alone is not distributed-parametric form."
        - scope: "Learnable projection basis and EMA target-encoder parameter parts"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
                - "memory.md#mem-cmp-target-encoder"
              note: "Distributed numerical basis/encoder state is consumed by forward computation."
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
          note: "These numerical parameters differ from fixed-rule sample statistics."
        - scope: "Fixed projection basis"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
                - "runtime.md#rt-rte-core-projection"
              note: "Fixed numerical rows have localized linear-algebra consumers."
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "runtime.md#rt-rte-core-projection"
          note: "The fixed tensor supplies a specified linear analysis/synthesis map rather than a learned update route."
        - scope: "Target encoder module-dependent non-floating buffers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-cmp-target-encoder"
          note: "The supplied module may have non-floating buffers, but their content and consumption rules are not established."
        - scope: "Checkpoint metadata and structural reports"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
                - "runtime.md#rt-rte-structural-checks"
              note: "Hashes, availability, check results and evidence-envelope fields are fixed-rule data."
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
                - "runtime.md#rt-rte-structural-checks"
              note: "Provenance limits and allowed-interpretation text are prose parts."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
            - "runtime.md#rt-rte-structural-checks"
          note: "Neither report encoding nor metadata is a trained checkpoint."
      records:
        - "memory.md#mem-obj-compiler-assumptions"
        - "runtime.md#rt-obj-design-config"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "epistemic.md#epi-obj-claims"
        - "epistemic.md#epi-rte-template-specialization"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
      note: "Positive forms remain attached to operative paths. Missing package/report parts and module-dependent encoder buffers prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        - scope: "Host-authored design and assumptions"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "memory.md#mem-obj-compiler-assumptions"
              note: "The host proposes task-specific choices and records assumptions."
            - value: "imported"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
              note: "User/project facts are brought into the proposed contract."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "memory.md#mem-obj-compiler-assumptions"
          note: "This is a requested source-to-product path, not observed authorship or established semantic fidelity."
        - scope: "Rendered configuration/program parts and derived diagnostics"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-template-specialization"
                - "epistemic.md#epi-rte-design-diagnostics"
              note: "Literal template specialization and fixed diagnostic predicates derive product material."
          records:
            - "epistemic.md#epi-rte-template-specialization"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-obj-scaffold-manifest"
          note: "The transformations are inspected, but package/report subobjects remain undeclared separately."
        - scope: "Welford statistics: numerical derivation and original samples"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Fixed numerical merging produces retained sufficient statistics."
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "Zero initialization and Welford accumulation are known. Original sample content/origin is not recorded, so trace extraction or imported experience cannot be concluded."
        - scope: "Projection basis: caller initialization, optimization and QR"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
              note: "The constructor clones caller-provided basis state."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-core-projection"
              note: "Scheduled explicit QR retraction transforms current numerical rows."
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "runtime.md#rt-rte-core-projection"
          note: "Caller-supplied rows and explicit retraction are known; upstream optimization data and initial training provenance remain unresolved."
        - scope: "EMA target encoder: initialization and subsequent update"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-target-encoder"
              note: "Target state enters as a caller module or copied context module."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-target-encoder"
                - "runtime.md#rt-rte-core-projection"
              note: "EMA combines parameter/buffer state under fixed numerical rules."
          records:
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "A supplied module or context-encoder copy initializes the target; original training and optimizer inputs remain unknown."
        - scope: "Checkpoint manifest initial content and subsequent maintainer editing"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
              note: "Maintainer editing can supply publication and provenance metadata."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
          note: "Maintainers can edit metadata; their initial approval/provenance process is not implemented."
        - scope: "Retained recipe/verifier diagnostic outputs"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structural-checks"
              note: "Deterministic checks produce hashes, results and an evidence envelope."
          records:
            - "runtime.md#rt-rte-structural-checks"
          note: "This lineage covers diagnostics, not trained parameters or accepted scientific conclusions."
      records:
        - "runtime.md#rt-rte-task-compilation"
        - "memory.md#mem-obj-compiler-assumptions"
        - "epistemic.md#epi-rte-template-specialization"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
      note: "Known derivation paths do not resolve encoder training or factor-sample origin. Missing material-part declarations also prevent treating the generated package as a complete single lineage unit."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Generated usage-mode constants at callback dispatch"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-generated-contract"
                - "epistemic.md#epi-rte-template-specialization"
              note: "USAGE_MODE selects readout, analysis or repeated transition."
          records:
            - "runtime.md#rt-bap-generated-contract"
            - "epistemic.md#epi-rte-template-specialization"
          note: "The dispatcher consumes persisted constants, not the copied diagnostic report."
        - scope: "Generated contract criteria at invoked tests and audit helpers"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-generated-contract"
                - "epistemic.md#epi-obj-claims"
                - "epistemic.md#epi-rte-evidence-envelope"
                - "epistemic.md#epi-rte-measurement-checks"
              note: "Persisted planned comparisons and audit thresholds define conformity."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-generated-contract"
                - "epistemic.md#epi-rte-evidence-envelope"
                - "epistemic.md#epi-rte-measurement-checks"
              note: "Invoked branches reject mismatches by exceptions."
          records:
            - "runtime.md#rt-bap-generated-contract"
            - "epistemic.md#epi-obj-claims"
            - "epistemic.md#epi-rte-evidence-envelope"
            - "epistemic.md#epi-rte-measurement-checks"
          note: "Force is local to invoked checks; callback execution can bypass them."
        - scope: "Diagnostic feedback at host design repair"
          assessment: "partial"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "epistemic.md#epi-rte-design-diagnostics"
              note: "The host is instructed to use structured diagnostics as repair feedback."
            - value: "learning"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "epistemic.md#epi-rte-design-diagnostics"
                - "runtime.md#rt-bap-generated-contract"
              note: "Feedback is requested to revise a durable design/program subsequently consumed by generated calls; this does not assert improved capacity."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-obj-design-config"
          note: "A validity predicate gates CLI rendering, but no separate retained diagnostic-report object is declared. The gate uses a fresh report, not an old report file."
        - scope: "Welford historical statistics at activity-penalty computation"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Count/mean/M2 supply historical variance information to the penalty calculation."
            - value: "learning"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-streaming-monitor"
              note: "The returned differentiable history-dependent loss can feed an external optimizer; no optimizer is invoked here."
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "The next monitor call consumes historical numerical evidence. Actual external optimization remains unobserved."
        - scope: "Checkpoint metadata at integrity/publication consistency verifier"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
                - "runtime.md#rt-rte-structural-checks"
              note: "Manifest descriptors and hashes supply criteria for checking local publication artifacts."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
            - "runtime.md#rt-rte-structural-checks"
          note: "A failed check yields diagnostic failure/status, not revoked loading authority."
        - scope: "Copied assumptions, package file-list, archived reports and generated prose at later semantic consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-compiler-assumptions"
            - "runtime.md#rt-obj-scaffold-manifest"
            - "runtime.md#rt-rte-structural-checks"
          note: "Inspectability and optional persistence do not identify a later semantic consumer. Undeclared diagnostic/file-list parts cannot be assigned the executable constants authority."
        - scope: "Projection and target-encoder retained state at numerical forward calls"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Changed tensors influence later calculations, but records do not establish a controlled authority category for each opaque parameter/buffer part at an actual learning or decision consumer."
      records:
        - "runtime.md#rt-bap-generated-contract"
        - "epistemic.md#epi-rte-template-specialization"
        - "epistemic.md#epi-obj-claims"
        - "epistemic.md#epi-rte-evidence-envelope"
        - "epistemic.md#epi-rte-measurement-checks"
        - "runtime.md#rt-rte-task-compilation"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-obj-design-config"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
        - "memory.md#mem-obj-compiler-assumptions"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
      note: "Generated contracts have concrete fixed-rule consumers. Inspection-only prose/reports, unresolved initial model content and undeclared package/report parts prevent a uniform complete authority account."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Requested host proposal and diagnostic-driven design repair"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "memory.md#mem-obj-compiler-assumptions"
              note: "Model authorship and requested repair admit task-specific content computationally."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "memory.md#mem-obj-compiler-assumptions"
          note: "The host chooses fields/revisions without mandatory per-content human approval."
        - scope: "Explicit human configuration or generated-file editing"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-scaffold-admission"
                - "runtime.md#rt-obj-design-config"
              note: "A human can edit the configuration or generated Python directly."
          records:
            - "runtime.md#rt-rte-scaffold-admission"
            - "runtime.md#rt-obj-design-config"
          note: "This is a separate editing affordance, not inferred human approval of automatic rendering."
        - scope: "CLI/direct-render package admission and optional diagnostic/report writes"
          assessment: "partial"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scaffold-admission"
                - "epistemic.md#epi-rte-design-diagnostics"
                - "runtime.md#rt-rte-structural-checks"
              note: "Code admits output under validity/format/destination or report-write rules without a required human content decision."
          records:
            - "runtime.md#rt-rte-scaffold-admission"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-rte-structural-checks"
            - "runtime.md#rt-obj-scaffold-manifest"
          note: "Software gates and writes are known; separately declared report/program/file-list parts are missing. Direct rendering does not inherit the CLI validity gate."
        - scope: "Welford update and reset"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-streaming-monitor"
              note: "Shape/finite/overflow checks precede fixed-rule updates, and reset clears history."
          records:
            - "memory.md#mem-rte-streaming-monitor"
          note: "Caller flags select invocation; code decides numerical admissibility and replaces buffers."
        - scope: "Subsequent EMA and explicit projection retraction"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-target-encoder"
                - "runtime.md#rt-rte-core-projection"
              note: "Code validates update conditions and computes replacement tensors without a parameter-quality human approval step."
          records:
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "The numerical mutation mechanism is known independently of initial weights and external optimizer control."
        - scope: "Initial basis/encoder content and external optimization inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Caller-supplied state does not establish whether a human or software admitted the original content."
        - scope: "Checkpoint publication metadata editing and initial admission"
          assessment: "partial"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
              note: "Maintainers can edit publication metadata as an explicit content choice."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
          note: "Explicit maintainer editing is possible; the initial review/approval mechanism is not implemented."
      records:
        - "runtime.md#rt-rte-task-compilation"
        - "memory.md#mem-obj-compiler-assumptions"
        - "runtime.md#rt-rte-scaffold-admission"
        - "runtime.md#rt-obj-design-config"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-rte-structural-checks"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "memory.md#mem-rte-streaming-monitor"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
      note: "Known software admissions and explicit editing affordances coexist with unknown initialization control. Neither generic caller identity nor starting the workflow establishes manual admission."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Requested host revision of retained task design from diagnostics"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "runtime.md#rt-obj-design-config"
              note: "The host revises an existing proposed configuration after diagnostic criticism."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "runtime.md#rt-obj-design-config"
          note: "The source requests repeated repair; it supplies no exercised host trace."
        - scope: "Welford history update and reset"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Prior and new sample information is combined into reduced count/mean/M2 statistics, without retaining sample identities."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-online-variance-tracker"
                - "memory.md#mem-rte-streaming-monitor"
              note: "Each admitted batch revises existing sufficient statistics."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-streaming-monitor"
              note: "Reset forgets all accumulated history; this is explicit forgetting, not gradual age-based downweighting."
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "These operations concern numerical history rather than standing natural-language facts."
        - scope: "EMA target-state update and QR retraction"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-target-encoder"
                - "runtime.md#rt-rte-core-projection"
              note: "EMA revises existing target state; QR retraction revises current learnable rows."
          records:
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Transformation is established without improved model quality or retained historical reasons."
        - scope: "Initial/externally optimized numerical state"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Unknown initial training and external optimization data prevent enumerating their memory-curation operations."
        - scope: "Package generation, copied diagnostics/file list and checkpoint metadata maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-scaffold-manifest"
            - "epistemic.md#epi-rte-template-specialization"
            - "memory.md#mem-obj-checkpoint-manifest"
            - "epistemic.md#epi-rte-design-diagnostics"
          note: "Literal copying/rendering and integrity checks alone establish no controlled curation operation. Separate output-part declarations and metadata maintenance implementation are missing; no promotion is inferred from temporary-directory replacement."
      records:
        - "runtime.md#rt-rte-task-compilation"
        - "runtime.md#rt-obj-design-config"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "epistemic.md#epi-rte-template-specialization"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "epistemic.md#epi-rte-design-diagnostics"
      note: "Numerical and requested design revisions are classified at their own evidence layer. Opaque optimizer inputs, metadata maintenance and undeclared output parts prevent a complete operation inventory."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit config-path load, render and generated-module/test invocation"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scaffold-admission"
                - "runtime.md#rt-bap-generated-contract"
                - "epistemic.md#epi-rte-template-specialization"
              note: "Path load, import and explicit calls request retained product material."
          records:
            - "runtime.md#rt-rte-scaffold-admission"
            - "runtime.md#rt-bap-generated-contract"
            - "epistemic.md#epi-rte-template-specialization"
          note: "The caller requests the design/package consumer; no independent relevance selector supplies extra memory."
        - scope: "Caller-selected tracker, projection module and target encoder at subsequent numerical calls"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-streaming-monitor"
                - "runtime.md#rt-cmp-orthogonal-factor-projection"
                - "memory.md#mem-cmp-target-encoder"
                - "runtime.md#rt-rte-core-projection"
              note: "Requested monitor/forward calls consume their selected module buffers/parameters, without an unsolicited memory-delivery route."
          records:
            - "memory.md#mem-rte-streaming-monitor"
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "All retained numerical state of the selected module is used; callback return horizons are not accumulated memory."
        - scope: "Checkpoint manifest and local bytes at verifier invocation"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
                - "runtime.md#rt-rte-structural-checks"
              note: "Caller/default path and local artifact root select verification inputs."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
            - "runtime.md#rt-rte-structural-checks"
          note: "This is manifest/file verification, not deserialization or automatic installation."
        - scope: "Future checkpoint consumer described by verify-before-load guidance"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-checkpoint-manifest"
              note: "The guide describes consumers verifying staged checkpoint bytes before loading."
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
          note: "This is an afforded consumer role, not a wired weight loader; the current entry has no payload."
        - scope: "Copied assumptions, retained diagnostic reports and file-list at later host/semantic consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-compiler-assumptions"
            - "runtime.md#rt-obj-scaffold-manifest"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-rte-structural-checks"
          note: "No cross-session reload selector or automatic later report consumer is established. Missing part declarations prevent resolving the mixed containers into complete later-consumer units."
      records:
        - "runtime.md#rt-rte-scaffold-admission"
        - "runtime.md#rt-bap-generated-contract"
        - "epistemic.md#epi-rte-template-specialization"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
        - "memory.md#mem-obj-compiler-assumptions"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "epistemic.md#epi-rte-design-diagnostics"
      note: "Concrete requested routes are classified without converting internal return delivery into push. Unestablished semantic reload/report consumers and future checkpoint loading prevent complete coverage."
    read_back_signal:
      assessment: "not-determinable"
      units:
        - scope: "Inspected config/package, numerical-module and manifest verification requests"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-scaffold-admission"
            - "runtime.md#rt-bap-generated-contract"
            - "memory.md#mem-rte-streaming-monitor"
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "memory.md#mem-obj-checkpoint-manifest"
          note: "These are requested pull operations. A config path or module identity on a request is not identifier-based push."
        - scope: "Unestablished host semantic reload and retained-report/file-list consumer alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-compiler-assumptions"
            - "runtime.md#rt-obj-scaffold-manifest"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-rte-structural-checks"
          note: "No trigger, selector input and selected retained part are recorded for a push here. This uncertainty does not establish absent push or any controlled signal."
      records:
        - "runtime.md#rt-rte-scaffold-admission"
        - "runtime.md#rt-bap-generated-contract"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "memory.md#mem-obj-compiler-assumptions"
        - "runtime.md#rt-obj-scaffold-manifest"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-rte-structural-checks"
      note: "Inspected requested routes do not need a push selector, but unresolved later-consumer alternatives prevent a whole-boundary pull-only or absent-read-back conclusion."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Host consumes validation execution feedback, repairs design and emits later-consumed generated contracts"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "epistemic.md#epi-rte-design-diagnostics"
                - "runtime.md#rt-rte-scaffold-admission"
                - "runtime.md#rt-bap-generated-contract"
              note: "Tool diagnostic results feed automatic host repair; the revised configuration is retained/rendered into contracts consumed by later imports/calls."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-rte-scaffold-admission"
            - "runtime.md#rt-bap-generated-contract"
          note: "This is the declared host workflow, not implemented host orchestration. Trace learning here means feedback-fed durable artifact revision, independently of beneficial learning."
        - scope: "Welford historical-statistics route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "The fixed update and later loss consumer are wired, but original batch activity provenance and a durable save/reload route are not established. No qualifying trace-fed durable update or bounded negative can be concluded."
        - scope: "Projection/EMA state, initial encoders and external optimization"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "Original experience/optimizer inputs and durable checkpoint write routes are uninspected. Parameter mutability alone establishes neither qualifying trace learning nor its absence."
        - scope: "Checkpoint metadata and retained audit/package auxiliary outputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
            - "runtime.md#rt-rte-structural-checks"
            - "runtime.md#rt-obj-scaffold-manifest"
          note: "These records do not establish an automatic raw-trace-to-durable-behavior-shaping write and later consumer for every included part. The missing part declarations and future payload limit prevent a blanket negative."
      records:
        - "runtime.md#rt-rte-task-compilation"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-rte-scaffold-admission"
        - "runtime.md#rt-bap-generated-contract"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
        - "runtime.md#rt-obj-scaffold-manifest"
      note: "The requested diagnostic-repair chain supports a claimed positive, not observed learning or improved capacity. Numerical input provenance and checkpoint persistence are unresolved, so there is no system-wide negative."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Validation feedback consumed by host design repair"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-compilation"
                - "epistemic.md#epi-rte-design-diagnostics"
              note: "Validator code/path/message results feed the requested host revision of durable design artifacts."
          records:
            - "runtime.md#rt-rte-task-compilation"
            - "epistemic.md#epi-rte-design-diagnostics"
            - "runtime.md#rt-rte-scaffold-admission"
            - "runtime.md#rt-bap-generated-contract"
          note: "The input is tool execution feedback, not a recorded session conversation or environmental event stream."
        - scope: "Original factor samples used in Welford accumulation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-online-variance-tracker"
            - "memory.md#mem-rte-streaming-monitor"
          note: "Sample-origin identities are not retained or established. Numeric batches alone do not identify event streams, session logs, tool traces or trajectories."
        - scope: "Original encoder/basis training and external optimizer inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-orthogonal-factor-projection"
            - "memory.md#mem-cmp-target-encoder"
            - "runtime.md#rt-rte-core-projection"
          note: "A copied/EMA-updated module does not identify the content or origin of its training experience."
        - scope: "Other report/manifest/package auxiliary retention"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-checkpoint-manifest"
            - "runtime.md#rt-rte-structural-checks"
            - "runtime.md#rt-obj-scaffold-manifest"
          note: "No qualifying automatic trace-fed durable-write/later-consumer chain is established for these parts; source classification cannot be borrowed from the diagnostic repair route."
      records:
        - "runtime.md#rt-rte-task-compilation"
        - "epistemic.md#epi-rte-design-diagnostics"
        - "runtime.md#rt-rte-scaffold-admission"
        - "runtime.md#rt-bap-generated-contract"
        - "memory.md#mem-obj-online-variance-tracker"
        - "memory.md#mem-rte-streaming-monitor"
        - "runtime.md#rt-cmp-orthogonal-factor-projection"
        - "memory.md#mem-cmp-target-encoder"
        - "runtime.md#rt-rte-core-projection"
        - "memory.md#mem-obj-checkpoint-manifest"
        - "runtime.md#rt-rte-structural-checks"
        - "runtime.md#rt-obj-scaffold-manifest"
      note: "The claimed diagnostic-driven repair has an identifiable execution-feedback source. Other included numerical/update paths have unresolved origins, rather than an inapplicable source inferred from a local negative."
---

# JEPA-Anything memory profile

## Comparison rationale

The builder retains products and bounded numerical history, not a target-owned agent-session store. The profile keeps generated executable constants separate from copied assumptions, diagnostic feedback and file-list metadata. The first have fixed-rule consumers; inspectability of the others does not establish a later semantic consumer. See [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest), [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract) and [MEM-OBJ-compiler-assumptions](memory.md#mem-obj-compiler-assumptions).

The supplied reconciliation leaves missing-part conflicts for diagnostic feedback, generated executable contracts and the generated file-list manifest. This profile does not declare replacements or reopen verification. It cites existing containers and their recorded paths, preserves supported findings, and leaves affected inventory coverage partial. It neither grants a report the generated program's authority nor treats the whole package as a single fully assessed consumer object. Consequently no complete-value enumeration is claimed for those axes.

The supplied reconciliation supersedes the epistemic variance object and route with [MEM-OBJ-online-variance-tracker](memory.md#mem-obj-online-variance-tracker) and [MEM-RTE-streaming-monitor](memory.md#mem-rte-streaming-monitor). All profile references use these canonical declarations. Welford buffers are symbolic sufficient statistics under fixed consumer rules, not parametric encoder weights. The reset operation is forgetting; it does not establish gradual decay, history-preserving invalidation or per-sample deletion. EMA and QR revise existing numerical state. None of these operations establishes improved capacity. See also [MEM-CMP-target-encoder](memory.md#mem-cmp-target-encoder) and [RT-RTE-core-projection](runtime.md#rt-rte-core-projection).

The trace-learning positive is deliberately only claimed. The source-defined workflow asks the host to consume tool diagnostics, revise the design, retain it and render contracts that later calls consume. That meets the profile's trace-fed artifact-write meaning at the requested-workflow layer; it is not an assertion of observed training, autonomous orchestration, a revised Skill or compiler self-improvement. The numerical histories retain separate unknown provenance and durable-write limits. A diagnostic-repair positive does not classify those alternatives. See [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation), [EPI-RTE-design-diagnostics](epistemic.md#epi-rte-design-diagnostics), [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission) and [RT-BAP-generated-contract](runtime.md#rt-bap-generated-contract).

A requested path load, module call or manifest verification is pull. Internal delivery within that requested operation is not counted again as push. File paths and module identities do not establish identifier-based unsolicited selection. Since later semantic report/assumption consumers remain unresolved, the signal axis is not globally inapplicable. The unpublished checkpoint entry is metadata only; the verifier's future published-file branch is integrity checking, while verify-before-load is an afforded external consumer role. See [MEM-OBJ-checkpoint-manifest](memory.md#mem-obj-checkpoint-manifest), [MEM-RTE-streaming-monitor](memory.md#mem-rte-streaming-monitor) and [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).

No frozen-source files were read for this classification. All warrants come from the supplied records and annotations, with the supplied reconciliation resolving the two supersessions. No records, quotations, source identities or execution evidence were added.
