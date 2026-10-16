---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Compound Engineering Plugin memory comparison: project reasoning, packs, continuity, optimization and improvement state, with unresolved host and ancillary routes."
run-id: AAS-2026-10-13-compound-engineering-plugin-6ac79f4e7555-01
source-identity: https://github.com/EveryInc/compound-engineering-plugin
reviewed-boundary: "50532b00de523980010d97fe950965b35382a3b7"
memory-comparison:
  version: 2
  scope: >-
    Use-accumulated project solutions/patterns, writable or imported pack rules,
    CONCEPTS vocabulary, prior-session derivatives, continuity snapshots,
    optimization logs/digests, implementation receipts and recovery state,
    retained review/residual and evaluation evidence, and revised methodology.
    Includes unresolved retune, dogfood, ideation, live-polish, pending-feedback,
    sweep and additional glossary/solution consumer routes, plus opaque host
    compaction and injected auto-memory dependencies. Excludes unchanged shipped
    skills and distribution copies as memory, ordinary untransformed current-run
    context, arbitrary product code as a learning store, and external host/model
    implementation. Provider memory and trace provenance are unresolved, not
    inferred from the fact that a model uses weights.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Solutions/patterns and project glossary; live writable pack files"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-solutions, memory.md#mem-obj-concepts, memory.md#mem-obj-pack-rules]
              note: "The prescribed producers retain Markdown in project or pack directories."
            - value: repo
              basis: claimed
              records: [memory.md#mem-obj-solutions, memory.md#mem-obj-concepts, runtime.md#rt-rte-learning-admission]
              note: "Committed project learning and refresh changes also persist in Git; not every local write is committed."
          records: [memory.md#mem-obj-solutions, memory.md#mem-obj-concepts, memory.md#mem-obj-pack-rules, runtime.md#rt-rte-learning-admission]
          note: "These named objects have file retention and conditional Git retention; actual project contents are not supplied."
        - scope: "Git-sourced pack cache"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-rte-pack-resolution]
              note: "The inspected resolver returns an existing checkout or creates a local checkout containing readable rule files."
            - value: repo
              basis: wired
              records: [memory.md#mem-rte-pack-resolution]
              note: "The reusable cache is a Git checkout keyed by URL/ref, not a vector or semantic index."
          records: [memory.md#mem-rte-pack-resolution, memory.md#mem-obj-pack-rules]
          note: "Cache substrate is known even though third-party content and ref freshness are not."
        - scope: "Session skeleton/digest, managed handoff, optimization log/result markers and strategy digest"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-session-skeleton, memory.md#mem-obj-handoff, memory.md#mem-obj-experiment-log, memory.md#mem-obj-strategy-digest]
              note: "The workflows name scratch, temporary or gitignored local files; a managed handoff is not permanent storage."
          records: [memory.md#mem-obj-session-skeleton, memory.md#mem-obj-handoff, memory.md#mem-obj-experiment-log, memory.md#mem-obj-strategy-digest]
          note: "Classification covers named local representations, not every arbitrary user-selected handoff publication surface."
        - scope: "External implementation manifest, authorization/receipts and Git recovery objects"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit]
              note: "Private JSON and authorization/receipt files support executable transition checks."
            - value: repo
              basis: wired
              records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit]
              note: "Transport refs/objects and canonical-commit records retain integration and recovery history."
          records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit]
          note: "This is operational memory, not an assertion that all product commits are learned guidance."
        - scope: "Saved review and evaluation evidence; revised repository methodology"
          assessment: partial
          findings:
            - value: files
              basis: wired
              records: [epistemic.md#epi-obj-eval-artifacts, epistemic.md#epi-rte-eval-grading]
              note: "Grading implementation saves JSON/report artifacts."
            - value: files
              basis: claimed
              records: [epistemic.md#epi-obj-review-findings, workflow.md#wf-rte-review-admission]
              note: "Review run artifacts and reports are local files before residual delivery."
            - value: files
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring]
              note: "The repository authoring pathway retains editable revised skills and evaluation reports."
            - value: repo
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring]
              note: "Versioned method changes permit later publication and source reversion."
          records: [epistemic.md#epi-obj-eval-artifacts, epistemic.md#epi-rte-eval-grading, epistemic.md#epi-obj-review-findings, workflow.md#wf-rte-review-admission, runtime.md#rt-rte-skill-authoring]
          note: "PR-body/tracker destinations and arbitrary handoff destinations have no fully classified storage implementation in these records."
        - scope: "Opaque host memory/compaction archives and ancillary retune, dogfood, ideation, live-polish, pending-feedback and sweep state"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model, runtime.md#rt-rte-skill-authoring]
          note: "Reports name included dependencies and ancillary state but do not resolve all operative parts or provider retention. Complete substrate enumeration is prevented."
      records: [memory.md#mem-obj-solutions, memory.md#mem-rte-pack-resolution, memory.md#mem-obj-handoff, memory.md#mem-obj-experiment-log, runtime.md#rt-obj-run-manifest, epistemic.md#epi-obj-eval-artifacts, runtime.md#rt-rte-skill-authoring, memory.md#mem-rte-session-capture]
      note: "Principal file and Git surfaces are supported; external destinations and named unresolved dependencies prevent complete coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Learning, pattern, rule, glossary, handoff, session-digest and optimization-strategy prose at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-solutions, memory.md#mem-obj-pack-rules, memory.md#mem-obj-concepts, memory.md#mem-obj-session-skeleton, memory.md#mem-obj-handoff, memory.md#mem-obj-strategy-digest]
              note: "Reasoning, definitions, summaries and recommendations receive their effects through model interpretation."
          records: [memory.md#mem-obj-solutions, memory.md#mem-obj-pack-rules, memory.md#mem-obj-concepts, memory.md#mem-obj-session-skeleton, memory.md#mem-obj-handoff, memory.md#mem-obj-strategy-digest]
          note: "This unit covers the stated prose consumption path, not an implied symbolic interpretation of all YAML or metadata."
        - scope: "Controller identities, authorization fields, digests and receipts at fixed-rule transaction consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-bap-controller-state]
              note: "Exact IDs, argv, digests and snapshots permit or reject transitions under executable rules."
          records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-bap-controller-state]
          note: "Packet prose remains a separate model input; the JSON authorization fields are not natural-language authority."
        - scope: "Experiment hypotheses/reasons and metrics/status markers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-experiment-log, memory.md#mem-rte-experiment-digest]
              note: "The model interprets hypotheses and reasons while generating subsequent strategy."
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-experiment-log, memory.md#mem-rte-experiment-digest]
              note: "Identity/status/metric fields have a declared fixed-rule comparison and recovery consumer; decide script implementation is uninspected."
          records: [memory.md#mem-obj-experiment-log, memory.md#mem-rte-experiment-digest]
          note: "The two parts share a named log boundary but retain different consumers and no wired comparison claim."
        - scope: "Saved evaluation and review artifacts: transcript/judgment prose versus fixed-rule fields"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [epistemic.md#epi-obj-review-findings, epistemic.md#epi-obj-eval-artifacts]
              note: "Defect claims, evidence and rubric judgments are interpreted by reviewers/authors."
            - value: symbolic
              basis: wired
              records: [epistemic.md#epi-rte-review-findings, epistemic.md#epi-rte-eval-grading]
              note: "Structured confidence/status/grade predicates have fixed partitioning and grading consumers, without certifying prose truth."
          records: [epistemic.md#epi-obj-review-findings, epistemic.md#epi-obj-eval-artifacts, epistemic.md#epi-rte-review-findings, epistemic.md#epi-rte-eval-grading]
          note: "Named operative parts are split by consumption even where serialized together."
        - scope: "Revised method text at future author/host consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-bap-skill-instructions]
              note: "Editable instruction bodies can later be interpreted by models after distribution; no deployed revised version is observed."
          records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-bap-skill-instructions]
          note: "Only use-revised method bodies are included; unchanged loader metadata is not memory."
        - scope: "Opaque consumed host payloads and ancillary retained-state parts"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model, runtime.md#rt-rte-skill-authoring]
          note: "Rendered host summaries do not resolve their original payloads. Other state leaf semantics are unresolved; external weights do not classify these retained objects."
      records: [memory.md#mem-obj-solutions, runtime.md#rt-bap-controller-state, memory.md#mem-obj-experiment-log, epistemic.md#epi-rte-eval-grading, runtime.md#rt-rte-skill-authoring, memory.md#mem-rte-session-capture]
      note: "Text and symbolic consumption are supported locally; parametric memory and a complete inventory remain unestablished."
    lineage:
      assessment: partial
      units:
        - scope: "Model-assembled learning, glossary and writable path-pack updates"
          assessment: partial
          findings:
            - value: authored
              basis: claimed
              records: [runtime.md#rt-rte-learning-admission, memory.md#mem-obj-solutions, memory.md#mem-obj-concepts, memory.md#mem-obj-pack-rules]
              note: "The orchestrator writes reason-bearing guidance and vocabulary from current problem/tree evidence."
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-solutions]
              note: "Relevant archived session findings are selectively folded into learning sections."
          records: [runtime.md#rt-rte-learning-admission, memory.md#mem-rte-session-capture, memory.md#mem-obj-pack-rules]
          note: "Known later derivation does not establish initialization of every pre-existing learning, glossary or local pack rule."
        - scope: "Imported Git pack files"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-rte-pack-resolution, memory.md#mem-obj-pack-rules]
              note: "Resolver acquisition imports declared external files into the cache; import does not endorse their claims."
          records: [memory.md#mem-rte-pack-resolution, memory.md#mem-obj-pack-rules]
          note: "This covers the inspected acquisition path only; upstream original authorship remains unresolved separately."
        - scope: "Prior-session skeleton and historian digest"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
              note: "Inspected Pi extraction reduces archived session material using active-path/compaction filtering and text caps."
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
              note: "Historian synthesis extracts prose findings from selected scratch skeletons."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
          note: "Extracted lineage is supported without claiming lossless preservation or wiring every platform parser."
        - scope: "Continuity snapshot and experiment strategy digest"
          assessment: known
          findings:
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
              note: "Models distill selected conversation/workspace experience or logged experiment outcomes into later-consumed prose."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
          note: "Selection/redaction and compression are derivation paths, not evidence of improved capacity."
        - scope: "Transaction state and grading outputs derived by fixed code"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit, epistemic.md#epi-rte-eval-grading]
              note: "Programs construct authorization/receipt state and deterministic grade results from inputs and execution evidence; this is not model-authored guidance."
          records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit, epistemic.md#epi-rte-eval-grading]
          note: "The classification concerns generated control/results fields, not the original provenance of every transcript or packet."
        - scope: "Review claims, learnings dossier and revised method prose"
          assessment: known
          findings:
            - value: authored
              basis: claimed
              records: [epistemic.md#epi-obj-review-findings, epistemic.md#epi-obj-learnings-dossier]
              note: "Models formulate review claims and selected learning recommendations; semantic preservation is not demonstrated."
            - value: authored
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring]
              note: "Authors can revise method text using criticism and comparisons."
          records: [epistemic.md#epi-obj-review-findings, epistemic.md#epi-obj-learnings-dossier, runtime.md#rt-rte-skill-authoring]
          note: "Knowledge-to-dossier derivation is not automatically trace extraction; methodology authors may be human or agent."
        - scope: "Upstream initial content, opaque host summaries/memory and ancillary state derivations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-pack-rules, memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model, runtime.md#rt-rte-skill-authoring]
          note: "Inspection exposes derivative display and declared feedback routes but not all original input/provenance paths. No lineage value resolves those opaque parts."
      records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-pack-resolution, runtime.md#rt-obj-run-manifest, epistemic.md#epi-rte-eval-grading, runtime.md#rt-rte-skill-authoring]
      note: "Authored, imported, extracted and code-compiled paths coexist; unresolved initial and host provenance prevents a complete union."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Solutions/rules/glossary and distilled findings at planning and review consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-bap-project-evidence, memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-obj-concepts]
              note: "Retained reasoning and canonical terminology supply current decision evidence and advice; pack prescriptions are explicitly not workflow instructions."
            - value: ranking
              basis: claimed
              records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval]
              note: "Retained title/tags/applicability/body relevance influences which learning findings receive priority."
          records: [memory.md#mem-bap-project-evidence, memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-obj-concepts]
          note: "Model-interpreted evidence does not establish enforced policy or measured activation."
        - scope: "Prior-session evidence and experiment outcomes at their durable update consumers"
          assessment: known
          findings:
            - value: learning
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-experiment-digest]
              note: "Retained session experience feeds solution updates; retained experiment outcomes feed a strategy digest for later work."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-experiment-digest]
          note: "Learning authority names the update path, not improved future capacity."
        - scope: "Handoff snapshot and optimization strategy digest at later orientation/hypothesis invocations"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
              note: "Snapshots provide untrusted continuity context; digest provides next-batch advice/evidence. Neither grants action authority."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
          note: "These downstream effects remain separate from learning authority at their producers."
        - scope: "Experiment metrics/status and result markers at comparison and recovery consumers"
          assessment: known
          findings:
            - value: ranking
              basis: claimed
              records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log]
              note: "Recorded metrics influence relative eligibility/priority of tested product variants."
            - value: routing
              basis: claimed
              records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log]
              note: "Recorded statuses and result markers select recovery and next-batch input windows; they do not reconstruct missing approval or forecasts."
          records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log]
          note: "Declared comparison/recovery consumers are supported; uninspected decide code is not an enforced guarantee."
        - scope: "Controller authorization/receipt state at executable authorization and integration consumers"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [runtime.md#rt-bap-controller-state, runtime.md#rt-rte-external-unit]
              note: "Stored identity, authorization and digest fields define admissible dispatch/integration transitions."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-bap-controller-state, runtime.md#rt-rte-external-unit]
              note: "Mismatch and failing/mutating verification veto progression on the bundled transaction route."
            - value: routing
              basis: wired
              records: [runtime.md#rt-obj-run-manifest, runtime.md#rt-rte-external-unit]
              note: "Run/unit/attempt/job and fixed-recipient state bind the authorized workspace and external destination."
          records: [runtime.md#rt-bap-controller-state, runtime.md#rt-rte-external-unit, runtime.md#rt-obj-run-manifest]
          note: "These forces govern the inspected protocol, not arbitrary shell actions or a universal sandbox. Full resume alternatives remain outside this resolved unit."
        - scope: "Review/residual and grading artifacts at caller, human reviewer and methodology author"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [workflow.md#wf-rte-review-admission, epistemic.md#epi-rte-eval-grading, runtime.md#rt-rte-skill-authoring]
              note: "Persisted findings and evaluation results supply evidence for later fixes, decisions or method revision, without automatic acceptance."
          records: [workflow.md#wf-rte-review-admission, epistemic.md#epi-rte-eval-grading, runtime.md#rt-rte-skill-authoring]
          note: "Current-run helper confidence partitions are not generalized standing controls; method-update admission remains separate."
        - scope: "Use-revised methodology at future author and host-model consumers"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-bap-skill-instructions]
              note: "Changed method text can enter later model-facing guidance after publication/loading; no exercised feedback-to-deployment chain is supplied."
          records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-bap-skill-instructions]
          note: "Unchanged shipped skills are excluded from the memory inventory; revised retained instructions are included."
        - scope: "Opaque host memory, ancillary state, additional readers and full recovery alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-session-capture, runtime.md#rt-rte-external-unit, runtime.md#rt-cmp-host-model, runtime.md#rt-rte-skill-authoring]
          note: "Actual consumed parts and consequential effects are not fully recorded; no complete authority inventory follows."
      records: [memory.md#mem-bap-project-evidence, memory.md#mem-rte-session-capture, memory.md#mem-rte-experiment-digest, runtime.md#rt-bap-controller-state, workflow.md#wf-rte-review-admission, runtime.md#rt-rte-skill-authoring]
      note: "Knowledge, learning, ranking, routing, validation, enforcement and instruction have local warrants; opaque alternative consumers prevent completeness."
    write_agency:
      assessment: partial
      units:
        - scope: "Ordinary learning/glossary capture, session enrichment and model-admitted safe refresh actions"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-learning-admission, memory.md#mem-rte-session-capture, epistemic.md#epi-rte-refresh-curation]
              note: "Models admit content without a required human decision on each entry; silent glossary edits and non-interactive capture make the distinction explicit."
          records: [runtime.md#rt-rte-learning-admission, memory.md#mem-rte-session-capture, epistemic.md#epi-rte-refresh-curation]
          note: "Starting capture or choosing a destination does not make all resulting content admission manual."
        - scope: "Conditional human-approved refresh changes and discoverability instruction edits"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [epistemic.md#epi-rte-refresh-curation, epistemic.md#epi-rte-capture-grounding]
              note: "Ambiguous/interactive replacement or split decisions and consented instruction-file changes have explicit human approval mechanisms."
          records: [epistemic.md#epi-rte-refresh-curation, epistemic.md#epi-rte-capture-grounding]
          note: "Human control applies only to the named gated edits, not the whole store or every pack write."
        - scope: "Pack-cache admission and controller authorization/receipt writes"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-pack-resolution, runtime.md#rt-rte-external-unit, runtime.md#rt-obj-run-manifest]
              note: "Software admits reusable checkouts and transaction state after its own checks; generic caller identity is not per-content human approval."
          records: [memory.md#mem-rte-pack-resolution, runtime.md#rt-rte-external-unit, runtime.md#rt-obj-run-manifest]
          note: "Source configuration initiation remains separate from these software admission mechanisms."
        - scope: "Handoff content, experiment logs/digests and review residual composition"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, workflow.md#wf-rte-review-admission]
              note: "Models/software choose retained content within user-selected scope; user workflow initiation, spend approval and later action confirmation are separate decisions."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, workflow.md#wf-rte-review-admission]
          note: "No mandatory per-summary or per-measurement human content approval is described."
        - scope: "Saved grading results"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [epistemic.md#epi-rte-eval-grading]
              note: "The driver parses/saves grading output without a human decision approving each retained grade."
          records: [epistemic.md#epi-rte-eval-grading]
          note: "Saving evidence does not automatically admit a proposed revised skill."
        - scope: "Initial stores/config, contributor method-change admission, host state and ancillary write mechanisms"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-pack-rules, memory.md#mem-rte-pack-resolution, runtime.md#rt-rte-skill-authoring, runtime.md#rt-cmp-host-model]
          note: "Pre-existing control and the human/agent contributor or merge decision are unresolved. Ancillary and provider writers lack sufficient admission details."
      records: [runtime.md#rt-rte-learning-admission, epistemic.md#epi-rte-refresh-curation, memory.md#mem-rte-pack-resolution, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, epistemic.md#epi-rte-eval-grading, runtime.md#rt-rte-skill-authoring]
      note: "Automatic and conditional manual admission coexist; unknown initialization and method/provider admission prevent completeness."
    curation_operations:
      assessment: partial
      units:
        - scope: "High-overlap learning updates and refresh corpus transformations"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-learning-admission, epistemic.md#epi-rte-refresh-curation]
              note: "In-place updates and successor replacements revise retained guidance."
            - value: consolidate
              basis: claimed
              records: [epistemic.md#epi-rte-refresh-curation, runtime.md#rt-rte-learning-admission]
              note: "Refresh combines existing guidance while preserving unique content and repairs references."
            - value: dedup
              basis: claimed
              records: [epistemic.md#epi-rte-refresh-curation, runtime.md#rt-rte-learning-admission]
              note: "Overlap handling updates rather than multiplies learning; consolidation removes a subsumed document. Lightweight collision checks alone do not establish this operation."
            - value: invalidate
              basis: claimed
              records: [epistemic.md#epi-rte-refresh-curation]
              note: "Evidence-supported withdrawal/removal changes current reliance while Git retains history. Stale status alone is not automatic reader exclusion."
            - value: decay
              basis: claimed
              records: [epistemic.md#epi-rte-refresh-curation]
              note: "Gated deletion forgets content from the active corpus; it is not age-based expiry or deletion of Git history."
          records: [runtime.md#rt-rte-learning-admission, epistemic.md#epi-rte-refresh-curation]
          note: "These are prescribed transformations, not observed semantic outcomes or a wired all-mode validator."
        - scope: "Session reduction and historian extraction"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
              note: "Inspected Pi extraction selects/reduces retained archive messages into a lossy skeleton."
            - value: consolidate
              basis: claimed
              records: [memory.md#mem-rte-session-capture]
              note: "Historian synthesis selects existing failed approaches/decisions for incorporation into retained learning. Its name does not establish a novel claim."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
          note: "The wired extraction witness does not upgrade model synthesis or every platform parser."
        - scope: "Continuity snapshot, strategy digest and selected learning dossier"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, memory.md#mem-rte-learning-retrieval]
              note: "Models select/compress existing session, experiment or corpus material for a reduced later-consumed representation. Semantic fidelity remains unobserved."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, memory.md#mem-rte-learning-retrieval]
          note: "Lossiness or epistemic uncertainty does not itself turn consolidation into creation of a new claim."
        - scope: "Pattern generalization, revised methods, opaque host and ancillary transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-solutions, runtime.md#rt-rte-skill-authoring, memory.md#mem-rte-session-capture]
          note: "No recorded input/output pair establishes a novel pattern claim; retune/other leaf transformations and host compaction writers remain unresolved. Synthesis and promotion are not inferred from labels."
      records: [epistemic.md#epi-rte-refresh-curation, memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, memory.md#mem-rte-learning-retrieval, runtime.md#rt-rte-skill-authoring]
      note: "Supported reductions, revisions and withdrawal coexist with unresolved transformations. Pack acquisition/cache lookup and unchanged receipt I/O alone establish no curation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Planning/review requests for solutions, packs and canonical terminology, including researcher return"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-obj-concepts]
              note: "The task's foreground agent requests memory research or performs inline reads; returned selected findings fulfill that request."
          records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-obj-concepts]
          note: "Automatic relevance selection within a requested research return does not create an additional push operation."
        - scope: "Pack cache lookup"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-pack-resolution]
              note: "A resolver invocation requests declared roots; a trusted retained checkout supplies the requested material."
          records: [memory.md#mem-rte-pack-resolution]
          note: "A URL/ref identity on this requested lookup is not identifier-based push."
        - scope: "Archived-session enrichment, user-selected handoff and experiment resume/next-batch reads"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
              note: "Capture requests historical evidence, a user selects continuity source, and later optimization invocations read requested digest/log windows."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
          note: "Automatic probing and model ranking remain inside their requested workflows; no unsolicited delivery is established."
        - scope: "Same-plan receipt recovery, later residual/evaluation consultation and revised-method loading"
          assessment: partial
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-external-unit, workflow.md#wf-rte-review-admission]
              note: "Same-run/plan recovery requests existing receipts; residual records are supplied to a later reviewer through the requested delivery workflow."
            - value: pull
              basis: afforded
              records: [runtime.md#rt-rte-skill-authoring, epistemic.md#epi-rte-eval-grading]
              note: "Future authors can consult saved evidence and revised methods."
          records: [runtime.md#rt-rte-external-unit, workflow.md#wf-rte-review-admission, runtime.md#rt-rte-skill-authoring, epistemic.md#epi-rte-eval-grading]
          note: "Full recovery and publication/loading of changed methods are not fully traced. A possible host injection cannot be classified from static registration."
        - scope: "Host-injected memory/compaction and ancillary retune, dogfood, ideation, live-polish, feedback and sweep readers"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model, runtime.md#rt-rte-skill-authoring]
          note: "Available summaries and search matches do not establish request/selection/delivery ownership for every alternative. Push remains unresolved, not absent."
      records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-rte-pack-resolution, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, runtime.md#rt-rte-external-unit, runtime.md#rt-rte-skill-authoring]
      note: "Pull is supported on inspected/requested chains; unresolved host and ancillary paths prevent a pull-only system conclusion."
    read_back_signal:
      assessment: uninspected
      units:
        - scope: "Resolved pull operations: learning research, cache lookup, historical capture, handoff and experiment reads"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval, memory.md#mem-rte-pack-resolution, memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest]
          note: "Signals classify push selection, not lexical/relevance selectors or identifiers used to fulfill these explicit memory requests."
        - scope: "Resolved requested receipt and residual/evaluation consultation"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-external-unit, workflow.md#wf-rte-review-admission, epistemic.md#epi-rte-eval-grading]
          note: "Exact run IDs and artifact paths belong to requested return/recovery, not targeted unsolicited delivery."
        - scope: "Unresolved changed-method loading, host injection/compaction and ancillary delivery alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-skill-authoring, memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model]
          note: "No recorded complete push chain names trigger, selector input and delivered retained parts; stronger inapplicability or a positive signal would hide missing coverage."
      records: [memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-pack-resolution, runtime.md#rt-rte-external-unit, runtime.md#rt-rte-skill-authoring, memory.md#mem-rte-session-capture]
      note: "No positive push signal is established. Known pull units are locally inapplicable, but unresolved alternatives make the axis uninspected rather than absent or globally inapplicable."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic prior-session enrichment into durable solutions with later planning/review consumption"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-solutions, memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval]
              note: "Archived session experience automatically feeds model-admitted reason-bearing learning, retained for later agents."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-solutions, memory.md#mem-rte-learning-retrieval, memory.md#mem-rte-review-retrieval]
          note: "Wired extraction alone does not upgrade the end-to-end model update/consumer chain. No improved-capacity result is required or claimed."
        - scope: "Model-generated continuity handoff consumed by a subsequent orientation invocation"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-obj-handoff]
              note: "Selected prior conversation/workspace experience becomes a retained model-written continuation summary for another agent."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-obj-handoff]
          note: "User initiation/source choice is not per-content admission; temporary managed retention can still span later invocations. The snapshot need not generalize."
        - scope: "Automatic batch-outcome digest used by subsequent hypothesis generation"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-strategy-digest]
              note: "Persisted experiment outcomes feed a model-authored strategy artifact reread for next-batch behavior, including local cross-session resumes."
          records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-strategy-digest]
          note: "Human scope/spend approval does not approve each digest; no observed useful activation or causal improvement is supplied."
        - scope: "Repository method authoring/retuning, direct current-session capture, opaque host updates and ancillary summaries"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-rte-learning-admission, memory.md#mem-rte-session-capture, runtime.md#rt-cmp-host-model]
          note: "Feedback-responsive method edits exist as a pathway, but automatic content admission and the complete trace-to-later-consumer chain are unresolved on these alternatives. Current work is not automatically an archived trace."
        - scope: "Imported static pack rule acquisition alone"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-pack-resolution, memory.md#mem-obj-pack-rules]
          note: "This named acquisition consumes external rule files, not activity traces; upstream pack-learning provenance is separately unresolved, not a negative about its authors."
      records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, runtime.md#rt-rte-skill-authoring, runtime.md#rt-rte-learning-admission, memory.md#mem-rte-pack-resolution]
      note: "Three qualifying prescribed automatic trace-fed chains establish yes. No bounded absence record supports a local or system-wide no; unresolved alternative writers prevent completeness."
    trace_source:
      assessment: partial
      units:
        - scope: "Qualifying prior-session enrichment: recorded conversation and tool activity"
          assessment: partial
          findings:
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
              note: "Archived user/assistant session turns are selected, summarized and incorporated into permanent learning."
            - value: tool-traces
              basis: claimed
              records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
              note: "The retained extraction includes tool names/targets/status and error evidence used in failed-attempt/session findings."
          records: [memory.md#mem-rte-session-capture, memory.md#mem-obj-session-skeleton]
          note: "Host summaries, discarded branches and unaudited platform parsers leave mixed original provenance and full tool-payload coverage unresolved. Wrapping session messages in events does not establish event-stream sources."
        - scope: "Qualifying handoff summary: selected prior conversation"
          assessment: partial
          findings:
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-rte-handoff-resume, memory.md#mem-obj-handoff]
              note: "Selected conversational intent, progress, decisions and rejected alternatives are carried into the subsequent orientation."
          records: [memory.md#mem-rte-handoff-resume, memory.md#mem-obj-handoff]
          note: "Workspace evidence and arbitrary explicit external sources can also contribute, but recorded detail does not establish every original trace class."
        - scope: "Qualifying optimization digest: linked experiment proposals, execution feedback and outcomes"
          assessment: known
          findings:
            - value: tool-traces
              basis: claimed
              records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log]
              note: "Persisted measurement/execution feedback from experiment runs supplies digest evidence."
            - value: trajectories
              basis: claimed
              records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log, memory.md#mem-obj-strategy-digest]
              note: "Per-experiment hypotheses/actions, measured outcomes and keep/revert results form linked experience used to extract success/failure strategy."
          records: [memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log, memory.md#mem-obj-strategy-digest]
          note: "The recorded original input is experiment experience, not merely a YAML event label or static optimization spec. Actual measurements are not supplied."
        - scope: "Unresolved qualifying alternatives in method retuning, host and ancillary updates"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-skill-authoring, runtime.md#rt-cmp-host-model, memory.md#mem-rte-session-capture]
          note: "The reports name archives and feedback surfaces but leave automatic write/consumer chains and original mixed inputs unresolved; their source axis cannot become inapplicable."
        - scope: "Imported static pack acquisition without a qualifying trace-fed update"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-pack-resolution, memory.md#mem-obj-pack-rules]
          note: "The bounded acquisition path imports rules rather than trace-derived behavior updates; no system-wide trace-learning absence is implied."
      records: [memory.md#mem-rte-session-capture, memory.md#mem-rte-handoff-resume, memory.md#mem-rte-experiment-digest, memory.md#mem-obj-experiment-log, runtime.md#rt-rte-skill-authoring]
      note: "Session logs, tool traces and linked experiment trajectories have claimed local warrants. Opaque source mixtures and unresolved write routes prevent complete classification; event-streams is not inferred from timestamps."
---

# Compound Engineering Plugin memory profile

## Comparison rationale

The comparison covers accumulated operational state as well as project guidance. Private controller receipts matter because later recovery consumes them. Unchanged skill installation and resource registration are not themselves memory writes. Revised methodology is included only through the repository authoring pathway, where a changed retained method can guide a later author or host invocation. The principal inventory and its unresolved alternatives follow the memory report's coverage account, not a claim that the whole-system boundary was exhaustively audited.

The five reconciliation supersessions affect solutions, pack rules, glossary, pack resolution and planning delivery. Their canonical citations here are [MEM-OBJ-solutions](memory.md#mem-obj-solutions), [MEM-OBJ-pack-rules](memory.md#mem-obj-pack-rules), [MEM-OBJ-concepts](memory.md#mem-obj-concepts), [MEM-RTE-pack-resolution](memory.md#mem-rte-pack-resolution) and [MEM-RTE-learning-retrieval](memory.md#mem-rte-learning-retrieval). Capture grounding and refresh remain distinct parts of [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), not duplicate routes. No unresolved reconciliation conflict changes a value.

Evidence strength remains attached to the mechanism. The wired pack-cache function establishes file/Git acquisition, not rule quality or observed reuse. Wired controller validation establishes vetoes on the bundled transaction route, not a universal sandbox. The wired session extractor reduces archive material; the historian-to-learning-to-later-reader chain remains claimed. The mechanical script in [EPI-RTE-capture-grounding](epistemic.md#epi-rte-capture-grounding) cannot upgrade semantic admission or retained prose to wired truth checking. Full grounding is postwrite and adjudicated; Lightweight lacks that semantic pass.

Pack prescriptions have knowledge authority at their planning/review consumers, because they are explicitly treated as evidence rather than workflow instructions. Their metadata and relevance influence ranking even without a learned ranking policy. Controller fields instead supply validation, enforced veto and routing at fixed-rule consumers. Experiment experience supplies learning authority at the digest update; the digest supplies knowledge at later hypothesis generation. These paths do not demonstrate improved capacity.

Starting a workflow is separate from approving its retained content. Silent glossary edits, automatic session enrichment, model-written handoffs and batch digests are automatic admission mechanisms. Conditional refresh approvals and consent to discoverability instruction edits are manual mechanisms. Destination selection alone does not convert a pack or handoff content write to manual. Initial store/config control and methodology merge/admission remain unresolved.

Consolidation is supported by selection/compression of archived sessions, continuity and experimental experience, and by merging retained guidance. Faithfulness remains uncertain without turning every model summary into synthesis. No input/output instance establishes that a generalized pattern creates a claim absent from its inputs. Evidence-supported deletion withdraws active reliance and forgets live corpus content while Git retains history. Stale metadata does not establish automatic suppression at readers; age alone is not decay policy.

Read-back is operation-specific. The researcher receives a request for retained evidence and returns selected findings; this is pull, not a second push because software or a model performs selection. The same distinction holds for requested pack roots, history enrichment, explicit handoff selection and next-batch digest reads. Identifiers and lexical relevance on these paths do not support push-signal values. Host injection and changed-method loading remain unresolved, so the system is not classified as pull-only and the signal axis is not globally inapplicable.

Trace learning uses the profile's write-route meaning. [MEM-RTE-session-capture](memory.md#mem-rte-session-capture), [MEM-RTE-handoff-resume](memory.md#mem-rte-handoff-resume) and [MEM-RTE-experiment-digest](memory.md#mem-rte-experiment-digest) each describe automatic experience-to-retained-artifact-to-later-consumer chains. A continuation snapshot qualifies despite its temporary storage and lack of generalization. Optimization histories link hypotheses/changes and measured outcomes, supporting trajectories alongside tool feedback; a timestamp or serialization wrapper does not add event-streams. Host-compacted summaries retain uncertain original provenance. No bounded absence record supports trace-learning no, and the authoring/evaluation pathway alone does not establish an automatic live-skill update.

Unresolved retune, dogfood, ideation, live-polish, feedback and sweep state, additional glossary/solution consumers, full recovery internals and host memory writers remain included limitations. Their missing leaf semantics, admission ownership, selection chains and original inputs prevent stronger coverage assessments. Display summaries and available search matches do not classify opaque consumed payloads. There are no observed-run or causally supported findings in this profile.

Source-read log: none. Classification used only the supplied accepted members, reconciliation, types and record contract. No source files, incumbent profiles or reference profiles were read.
