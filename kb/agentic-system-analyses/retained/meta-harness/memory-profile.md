---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Meta-Harness memory comparison: classification state, reference search experience, KIRA
  continuations, pilot history and onboarding handoffs.'
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
source-identity: https://github.com/stanford-iris-lab/meta-harness
reviewed-boundary: 8123ccabe2b19fa1123090b2e5f1bacc20963ce8
memory-comparison:
  version: 2
  scope: Use-derived classification examples/checkpoints/logs/local completion replay; reference results/frontiers,
    separately assessed summary result and rationale parts, requested reports and retained candidate code;
    KIRA task-local continuation summaries/fallbacks and opaque inherited/provider alternatives; pilot
    source snapshots and evaluation history with separate model-feedback and final-score consumers; afforded
    domain-specification handoff. Includes unresolved generated-state and arbitrary initial-checkpoint
    control. Excludes external model weights, static datasets/seed prompts/skills/suite/verifier code
    as memory objects, ordinary untransformed conversation/tool accumulation, and unfrozen external run
    artifacts. Provider cache state is retained as an opaque included alternative, not equated with local
    response files.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Live FewShotMemory examples and epoch best_state
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-examples
          - memory.md#mem-obj-memory
          note: List and captured state reside in process memory.
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-obj-memory
        note: Live list and best-state capture are distinguished from disk transport.
      - scope: Classification checkpoints, logs, local response cache, reference histories, result files
          and candidate code
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-completion-cache
          - memory.md#mem-obj-frontier-val
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-summary-rationale
          - runtime.md#rt-bap-candidate-execution
          - epistemic.md#epi-obj-val-results
          note: Run-local files retain serialized state, traces, result/control fields, rationale and
            executable artifacts.
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-completion-cache
        - memory.md#mem-obj-frontier-val
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-summary-rationale
        - runtime.md#rt-bap-candidate-execution
        - epistemic.md#epi-obj-val-results
        note: These named local artifacts are files; JSON and Python describe encoding, not an additional
          substrate.
      - scope: Pilot history and source/result snapshots
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          note: EvaluationState retains result dictionaries in an immutable tuple.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          note: Source snapshots, full evaluation results and uploaded history are files.
        records:
        - memory.md#mem-obj-evaluation-history
        note: Tuple accumulation and persistent snapshots/report are separate operative parts.
      - scope: KIRA handoff chat and trajectory structures
        assessment: partial
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Summary text and references are appended to chat/trajectory structures.
        records:
        - runtime.md#rt-rte-kira-execution
        note: Local chat/trajectory retention is inspectable; broader Harbor persistence is external.
      - scope: Requested report and onboarding documents
        assessment: known
        findings:
        - value: files
          basis: afforded
          records:
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-domain-onboarding
          note: Shipped procedures request report/specification files.
        records:
        - memory.md#mem-obj-reports
        - runtime.md#rt-rte-domain-onboarding
        note: Classification reports and domain specification are afforded file artifacts, not observed
          instances.
      - scope: Included generated-candidate internal state and opaque provider/host retained parts
        assessment: not-determinable
        findings: []
        records: &id001
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        - memory.md#mem-obj-completion-cache
        note: Generated payload internals and provider-cache substrate/lifetime are unresolved; disk checkpoint
          transport does not determine every internal substrate.
      records:
      - memory.md#mem-obj-examples
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-completion-cache
      - memory.md#mem-obj-frontier-val
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-summary-rationale
      - runtime.md#rt-bap-candidate-execution
      - epistemic.md#epi-obj-val-results
      - memory.md#mem-obj-evaluation-history
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-domain-onboarding
      note: The inventory includes live state, local durable files, afforded documents and opaque alternatives.
        Positive local file storage does not enumerate provider or generated-candidate internals.
    representational_form:
      assessment: partial
      units:
      - scope: Few-shot question/answer demonstrations at solver
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-examples
          - memory.md#mem-rte-classification-memory
          note: Selected demonstrations become Q/A text.
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-rte-classification-memory
        note: Question/answer strings are consumed through model interpretation.
      - scope: Example keys/order, checkpoint control, trace fields, result metrics, frontier identities
          and resume counters
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-examples
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-frontier-val
          - memory.md#mem-obj-summary-results
          - epistemic.md#epi-obj-val-results
          note: Serialization/control and numerical selection remain symbolic even where associated text
            is natural language.
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-frontier-val
        - memory.md#mem-obj-summary-results
        - epistemic.md#epi-obj-val-results
        note: Fixed-rule consumers operate on localized keys, numbers and identities.
      - scope: Summary hypothesis/change text and symbolic design labels
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-summary-rationale
          note: Model-authored hypotheses/changes retain textual encoding.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-summary-rationale
          note: Axis/component labels remain localized design metadata.
        records:
        - memory.md#mem-obj-summary-rationale
        note: Copied rationale and labels are separately identifiable within the declared rationale part.
      - scope: Cache response text and usage/key metadata
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-completion-cache
          - memory.md#mem-rte-completion-replay
          note: Content is replayed as model response text.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-completion-cache
          note: Exact keys and token/cost fields use fixed rules.
        records:
        - memory.md#mem-obj-completion-cache
        - memory.md#mem-rte-completion-replay
        note: Payload text and accounting metadata have different consumers.
      - scope: Reference candidate implementations, pilot source snapshots and history control fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          - runtime.md#rt-bap-candidate-execution
          note: Python rules execute in all three search routes; pilot JSON fields determine history filtering/scoring.
        records:
        - memory.md#mem-obj-evaluation-history
        - runtime.md#rt-bap-candidate-execution
        note: Executable source and source hash/acceptance/reward/budget data are not the feedback prose.
      - scope: Classification log text previews and retained answer text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-classification-log
          - epistemic.md#epi-obj-predictions
          note: Input previews and answer strings retain model-interpreted text.
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-predictions
          - epistemic.md#epi-rte-answer-check
          note: Recorded answer strings also serve as localized inputs to fixed comparator rules.
        records:
        - memory.md#mem-obj-classification-log
        - epistemic.md#epi-obj-predictions
        note: Partial previews and model answer strings are textual; comparator consumption is a separate
          fixed-rule path.
      - scope: Pilot feedback reason/task explanations and KIRA handoff text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          - runtime.md#rt-rte-kira-execution
          note: Reason/verifier summaries and summary_prompt are delivered as text.
        records:
        - memory.md#mem-obj-evaluation-history
        - runtime.md#rt-rte-kira-execution
        note: Readable feedback and derived handoff are model-interpreted text; inherited opaque payload
          alternatives are not inferred from them.
      - scope: Requested reports and domain specification
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-domain-onboarding
          note: Reports and decisions/defaults/unknowns are intended for later model interpretation.
        records:
        - memory.md#mem-obj-reports
        - runtime.md#rt-rte-domain-onboarding
        note: Documents are specified as prose guidance.
      - scope: Included generated-candidate internal state and opaque provider/host retained parts
        assessment: not-determinable
        findings: []
        records: *id001
        note: No controlled form follows for arbitrary generated state or opaque provider payloads from
          their display summaries; model weights themselves are outside this use-derived memory boundary.
      records:
      - memory.md#mem-obj-examples
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-frontier-val
      - memory.md#mem-obj-summary-results
      - epistemic.md#epi-obj-val-results
      - memory.md#mem-obj-summary-rationale
      - memory.md#mem-obj-completion-cache
      - memory.md#mem-rte-completion-replay
      - memory.md#mem-obj-evaluation-history
      - runtime.md#rt-bap-candidate-execution
      - epistemic.md#epi-obj-predictions
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-domain-onboarding
      note: Mixed containers are split by operative text, fixed-rule fields and consumer. No parametric
        memory value is inferred merely from the presence of external models.
    lineage:
      assessment: partial
      units:
      - scope: Few-shot retained training associations
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-examples
          - memory.md#mem-rte-classification-memory
          note: Batch inputs and target labels supply retained demonstrations.
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-rte-classification-memory
        note: The list copies imported dataset input/ground-truth associations, not retained model reasons.
      - scope: Reference numerical summaries/frontiers and pilot aggregated history fields
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-frontier-val
          - memory.md#mem-obj-evaluation-history
          - epistemic.md#epi-rte-suite-scoring
          note: Software derives result/control projections, winners and aggregate history.
        records:
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-frontier-val
        - memory.md#mem-obj-evaluation-history
        - epistemic.md#epi-rte-suite-scoring
        note: Deterministic projection/aggregation differs from authorship of explanatory text.
      - scope: Retained manifest hypotheses/changes and candidate implementations
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-summary-rationale
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          - runtime.md#rt-bap-candidate-execution
          note: Models supply hypotheses and candidate source retained by the drivers.
        records:
        - memory.md#mem-obj-summary-rationale
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        - runtime.md#rt-bap-candidate-execution
        note: Software copying does not turn model-authored rationale into software-derived explanation.
      - scope: Classification logs and extracted completion payload
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-completion-cache
          - memory.md#mem-rte-completion-replay
          note: Logger records runtime results; cache extracts response content/usage.
        records:
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-completion-cache
        - memory.md#mem-rte-completion-replay
        note: Execution events and provider responses are retained projections, not trained weights.
      - scope: KIRA derived handoff
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Task-history-fed summary text is retained for a later call.
        records:
        - runtime.md#rt-rte-kira-execution
        note: Conversation/screens feed the handoff; exact inherited derivation and all input provenance
          remain opaque.
      - scope: Requested reports and domain specification
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-domain-onboarding
          note: Models are instructed to write analysis and the domain handoff.
        records:
        - memory.md#mem-obj-reports
        - runtime.md#rt-rte-domain-onboarding
        note: Authorship is afforded, not observed production.
      - scope: Initial caller-supplied checkpoints, generated state provenance and provider-cache payload
          lineage
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        note: A run-keyed checkpoint read establishes selection, not initial content provenance; inherited/provider
          internals are not pinned here.
      records:
      - memory.md#mem-obj-examples
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-frontier-val
      - memory.md#mem-obj-evaluation-history
      - epistemic.md#epi-rte-suite-scoring
      - memory.md#mem-obj-summary-rationale
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - runtime.md#rt-bap-candidate-execution
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-completion-cache
      - memory.md#mem-rte-completion-replay
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-domain-onboarding
      - memory.md#mem-obj-memory
      note: Known copying, compilation and authorship coexist with unresolved initialization and inherited
        derivation. Checkpoint alternatives preserve payload-specific lineage rather than a universal
        JSON provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected demonstrations at classification solver and replayed completion text at requesting
          candidate
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-examples
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-obj-completion-cache
          - memory.md#mem-rte-completion-replay
          note: Stored associations and replayed responses supply content for prediction.
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-completion-cache
        - memory.md#mem-rte-completion-replay
        note: These content paths supply answer context or a returned answer, not a human-approved rule.
      - scope: Reference histories, rationale, traces and requested reports at proposer/analysis reader
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-summary-rationale
          - memory.md#mem-obj-frontier-val
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          note: History supplies comparison evidence and design advice.
        - value: learning
          basis: afforded
          records:
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          note: Recorded experience is requested input to durable candidate-code revision; actual reliance
            is unobserved.
        records:
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-summary-rationale
        - memory.md#mem-obj-frontier-val
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-reports
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        note: Model file reads and interpretation are afforded by instructions, not automatic full-content
          injection.
      - scope: Summary iteration counters at resume and frontier identities/metrics at final selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-frontier-val
          note: Iteration selects the next round; frontier identities select later evaluation inputs.
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-frontier-val
          - epistemic.md#epi-rte-frontier-selection
          - epistemic.md#epi-rte-terminal-scoring
          note: Retained scores determine winner/Pareto priority.
        records:
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-frontier-val
        - epistemic.md#epi-rte-frontier-selection
        - epistemic.md#epi-rte-terminal-scoring
        note: Different retained fields select continuation versus relative candidate priority.
      - scope: Supervised batch experience at candidate update
        assessment: partial
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-obj-examples
          note: Labelled/evaluated batch experience updates durable demonstrations later consumed by prediction.
        records:
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-examples
        note: The update is wired; generated candidates may transform feedback differently and no improvement
          follows.
      - scope: Retained candidate code at task-harness execution
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-bap-candidate-execution
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          note: Candidate rules choose solver prompts, observations and tool/model operations.
        records:
        - runtime.md#rt-bap-candidate-execution
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        note: Inspected imports grant executable selection rules. Arbitrary generated replacements prevent
          exhaustive enumeration of their effects.
      - scope: KIRA handoff at later inference and pilot projected history at editing opportunity
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          - memory.md#mem-obj-evaluation-history
          note: Later model calls receive handoff or projected feedback.
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-pilot-search
          - memory.md#mem-obj-evaluation-history
          note: Pilot feedback feeds the model editing opportunity for durable candidate rules; exercised
            dependence is not established.
        records:
        - runtime.md#rt-rte-kira-execution
        - memory.md#mem-obj-evaluation-history
        - runtime.md#rt-rte-pilot-search
        note: Handoff text and readable feedback are advisory; pilot ordinary message accumulation is
          not itself a derived memory write.
      - scope: Pilot accepted flags and rewards at historical scorer
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          - epistemic.md#epi-rte-history-selection
          note: Acceptance/non-null flags and report arithmetic establish score eligibility.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          - epistemic.md#epi-rte-history-selection
          note: Ineligible entries are excluded and invalid arithmetic yields zero.
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-history
          - epistemic.md#epi-rte-history-selection
          note: Eligible reward values determine the historical maximum.
        records:
        - memory.md#mem-obj-evaluation-history
        - epistemic.md#epi-rte-history-selection
        note: History fields control eligibility and maximum historical reward, not final-source restoration.
      - scope: Domain specification at later implementation agent
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-rte-domain-onboarding
          note: A retained domain specification guides subsequent implementation without granting unconfirmed
            spend.
        records:
        - runtime.md#rt-rte-domain-onboarding
        note: The afforded handoff conveys operator decisions and explicitly bounded implementation direction.
      - scope: Opaque generated-state and inherited/provider consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        note: Their internal consumer rules and effects cannot be enumerated from transport or display
          fields.
      records:
      - memory.md#mem-obj-examples
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-completion-cache
      - memory.md#mem-rte-completion-replay
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-summary-rationale
      - memory.md#mem-obj-frontier-val
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - epistemic.md#epi-rte-frontier-selection
      - epistemic.md#epi-rte-terminal-scoring
      - runtime.md#rt-bap-candidate-execution
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-evaluation-history
      - runtime.md#rt-rte-pilot-search
      - epistemic.md#epi-rte-history-selection
      - runtime.md#rt-rte-domain-onboarding
      - memory.md#mem-obj-memory
      note: 'Authority is classified at each actual consumer: experience can feed updating while derived
        content supplies knowledge or routing. Static proposer skills and verifier code are excluded as
        use-derived objects, not misclassified as memory controls.'
    write_agency:
      assessment: partial
      units:
      - scope: Batch admission, best-epoch restore, checkpoint/log/cache writes, frontier/summary admission
          and pilot history
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-classification-log
          - memory.md#mem-rte-completion-replay
          - memory.md#mem-obj-frontier-val
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-summary-rationale
          - memory.md#mem-obj-evaluation-history
          note: Software/model mechanisms admit these retained contents without operator approval of each
            item.
        records:
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-classification-log
        - memory.md#mem-rte-completion-replay
        - memory.md#mem-obj-frontier-val
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-summary-rationale
        - memory.md#mem-obj-evaluation-history
        note: Starting the workflow is not per-content human approval.
      - scope: Candidate-code admission and KIRA handoff production
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          - runtime.md#rt-rte-pilot-search
          - runtime.md#rt-rte-kira-execution
          note: Model/software updates and admission operate after workflow launch.
        records:
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        - runtime.md#rt-rte-pilot-search
        - runtime.md#rt-rte-kira-execution
        note: Reference import gates, pilot source gate and inherited summarizer invocation do not ask
          a human to approve each retained change.
      - scope: Requested report authorship
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-obj-reports
          note: Model report admission has no specified per-content human gate.
        records:
        - memory.md#mem-obj-reports
        note: Procedure requests model-produced guidance; no report instance is supplied.
      - scope: Consequential operator decisions retained in domain specification
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-domain-onboarding
          note: The handoff procedure elicits human scope/criterion/budget decisions.
        records:
        - runtime.md#rt-rte-domain-onboarding
        note: This is content-level operator choice, not merely launch authorization.
      - scope: Direct set_state replacement and unspecified initial/generated/provider admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-examples
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        note: Generic caller identity does not establish manual versus automatic control of supplied checkpoint
          content; provider admission internals are opaque.
      records:
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-classification-log
      - memory.md#mem-rte-completion-replay
      - memory.md#mem-obj-frontier-val
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-summary-rationale
      - memory.md#mem-obj-evaluation-history
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - runtime.md#rt-rte-pilot-search
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-domain-onboarding
      - memory.md#mem-obj-examples
      note: Admission control is separate from authorship and physical copying. Known automatic transformations
        do not settle arbitrary checkpoint initialization.
    curation_operations:
      assessment: partial
      units:
      - scope: Reference result-history projection and frontier replacement
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-frontier-val
          note: Result aggregates and frontier entries reduce existing recorded outcomes into comparison
            state.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-frontier-val
          - epistemic.md#epi-rte-terminal-scoring
          note: A better result replaces an existing frontier entry.
        - value: promote
          basis: wired
          records:
          - memory.md#mem-obj-frontier-val
          - epistemic.md#epi-rte-frontier-selection
          note: Winner/Pareto selection raises candidates to retained frontier/final-evaluation eligibility.
        records:
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-frontier-val
        - epistemic.md#epi-rte-frontier-selection
        - epistemic.md#epi-rte-terminal-scoring
        note: These records cover projection of retained results and implemented winner updates.
      - scope: Best-epoch checkpoint replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - memory.md#mem-rte-classification-memory
          note: Software replaces current state with best_state after validation.
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-rte-classification-memory
        note: Restoring a prior captured state revises current retained candidate state; it does not establish
          semantic criticism.
      - scope: Fresh-start withdrawal of selected code and indexes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        note: Reset selectively deletes code, indexes and results while some other artifacts survive.
          The records do not establish retained history of the particular withdrawn contents, so they
          do not establish invalidate or another controlled curation value for this mechanism.
      - scope: KIRA fallback handoff
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: The fallback condenses task-state input into a smaller continuation context.
        records:
        - runtime.md#rt-rte-kira-execution
        note: The fallback retains original instruction and a bounded screen suffix alongside surviving
          messages; it does not prove complete history loss.
      - scope: Inherited summarizer transformation, generated-candidate maintenance and unproduced reports
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-kira-execution
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-reports
        note: The inherited transformation is opaque and reports are requested rather than inspected outputs;
          no synthesis, deduplication or fidelity conclusion follows from their names.
      records:
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-frontier-val
      - epistemic.md#epi-rte-frontier-selection
      - epistemic.md#epi-rte-terminal-scoring
      - memory.md#mem-obj-memory
      - memory.md#mem-rte-classification-memory
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-reports
      note: Operations classify implemented retained-content transformations. Simple append, acquisition,
        cache-key lookup and schema serialization alone add no curation value. Selective reset deletion
        does not establish history-preserving invalidation. Unknown branches prevent an exhaustive
        operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Run-keyed checkpoint load, cache replay and deterministic history/frontier reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-rte-completion-replay
          - memory.md#mem-obj-summary-results
          - memory.md#mem-obj-frontier-val
          - epistemic.md#epi-rte-history-selection
          note: Load/replay/resume/selection/scoring code reads requested state or history.
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-rte-completion-replay
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-frontier-val
        - epistemic.md#epi-rte-history-selection
        note: These consumers request retained material; fulfilling those reads is not another unsolicited
          push.
      - scope: Proposer/analysis history reads and onboarding document load
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          - memory.md#mem-obj-reports
          - runtime.md#rt-rte-domain-onboarding
          note: Models choose instructed file reads for histories, reports or domain handoff.
        records:
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        - memory.md#mem-obj-reports
        - runtime.md#rt-rte-domain-onboarding
        note: Instructions afford later requested file reads; completion and reliance remain unobserved.
      - scope: Demonstration selection and delivery to solver
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-obj-examples
          note: Per-input sampling/shuffling plus the character cap injects selected demonstrations.
        records:
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-examples
        note: The solver asks for a task prediction, not for those particular retained examples; candidate
          code selects them automatically.
      - scope: KIRA continuation handoff
        assessment: partial
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Context pressure triggers summary or fallback appended to a later model request.
        records:
        - runtime.md#rt-rte-kira-execution
        note: Visible proactive/overflow retry supplies handoff automatically; inherited selection/delivery
          alternatives remain opaque.
      - scope: Generated-candidate alternative read-back and provider-side reuse
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        note: The candidate interface and cache decoration do not enumerate actual alternate delivery
          operations.
      records:
      - memory.md#mem-obj-memory
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-rte-completion-replay
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-frontier-val
      - epistemic.md#epi-rte-history-selection
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-domain-onboarding
      - memory.md#mem-obj-examples
      - runtime.md#rt-rte-kira-execution
      note: Both requested retrieval and automatic context injection exist. Pilot ordinary tool-result
        accumulation is excluded as a new read-back mechanism; durable history scoring is included.
    read_back_signal:
      assessment: partial
      units:
      - scope: Few-shot automatic demonstration injection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-classification-memory
          - memory.md#mem-obj-examples
          note: Sampling/shuffling and budget filters are coarse; hashing the input is not identity matching
            to a stored question.
        records:
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-examples
        note: 'Trigger: prediction. Selector input: input-derived random seed, list availability, max_examples
          and character budget. Selected part: formatted examples.'
      - scope: KIRA fallback injection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Fixed suffix selection is coarse rather than semantic or identifier-targeted.
        records:
        - runtime.md#rt-rte-kira-execution
        note: 'Trigger: failed summary after context pressure. Selector input: original instruction and
          current screen. Selected part: instruction plus last 1000 screen characters alongside remaining
          chat.'
      - scope: Inherited KIRA summary selection and generated/provider pushes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-kira-execution
        - memory.md#mem-obj-memory
        note: The inherited selector inputs and generated alternative selectors are unknown; model-generated
          display text cannot establish inferred-judgment or embedding selection.
      - scope: Checkpoint/cache/history/document request fulfillment
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-rte-completion-replay
        - memory.md#mem-obj-summary-results
        - memory.md#mem-obj-frontier-val
        - runtime.md#rt-rte-domain-onboarding
        note: These named operations are pull reads, so the push-selector axis does not apply to them.
          The unresolved push alternatives remain included above.
      records:
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-examples
      - runtime.md#rt-rte-kira-execution
      - memory.md#mem-obj-memory
      - memory.md#mem-rte-completion-replay
      - memory.md#mem-obj-summary-results
      - memory.md#mem-obj-frontier-val
      - runtime.md#rt-rte-domain-onboarding
      note: Coarse selectors have positive witnesses, but opaque push alternatives prevent completeness.
        Cache digests and requested paths identify pull requests, not identifier-based push.
    trace_learning:
      assessment: partial
      units:
      - scope: KIRA summary and fallback continuation
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Automatic trace-fed handoff changes the context artifact used by a later model invocation,
            without needing measured improvement.
        records:
        - runtime.md#rt-rte-kira-execution
        note: Task traces automatically yield retained continuation text delivered to later inference;
          exact inherited input selection and rationale retention remain unresolved.
      - scope: Reference trajectory/history-to-candidate and requested report route
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - runtime.md#rt-rte-classification-search
          - runtime.md#rt-rte-terminal-search
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-reports
          - runtime.md#rt-bap-candidate-execution
          note: Later proposer/analysis work is instructed to use traces/results in retained behavior-shaping
            revisions.
        records:
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-reports
        - runtime.md#rt-bap-candidate-execution
        note: The shipped procedure requests experience-fed durable code/guidance; it does not prove compliance.
      - scope: Pilot evaluation-feedback-to-candidate edit route
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-pilot-search
          - memory.md#mem-obj-evaluation-history
          - runtime.md#rt-bap-candidate-execution
          note: The implemented feedback/edit/evaluate chain affords automatic durable behavior-artifact
            revision at the outer-plus-child boundary.
        records:
        - runtime.md#rt-rte-pilot-search
        - memory.md#mem-obj-evaluation-history
        - runtime.md#rt-bap-candidate-execution
        note: Feedback reaches a model able to edit persistent source subsequently evaluated by children.
          No actual evidence-responsive edit is observed.
      - scope: Supervised batch trace qualification, generic checkpoints and provider transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-examples
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-kira-execution
        note: Few-shot stores source input/target pairs and drops prediction/reason feedback; offline
          batches are static labels. These records do not justify a universal trace-fed classification
          for all training modes or generated candidates, nor a bounded system-wide no.
      records:
      - runtime.md#rt-rte-kira-execution
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-reports
      - runtime.md#rt-bap-candidate-execution
      - runtime.md#rt-rte-pilot-search
      - memory.md#mem-obj-evaluation-history
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-examples
      - memory.md#mem-obj-memory
      note: Positive automatic continuation and feedback-to-artifact routes coexist with unresolved training/generated/provider
        alternatives. Trace learning here does not assert learning benefit, accepted explanations or successful
        self-improvement.
    trace_source:
      assessment: partial
      units:
      - scope: KIRA handoff original trace inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Recorded task conversational history feeds continuation.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-kira-execution
          note: Terminal observations/screens from task execution feed summary/fallback.
        records:
        - runtime.md#rt-rte-kira-execution
        note: Conversation/screens are recorded task experience; the inherited exact selected mixture
          remains uninspected.
      - scope: Reference history-fed candidate/report route
        assessment: known
        findings:
        - value: tool-traces
          basis: afforded
          records:
          - runtime.md#rt-rte-classification-search
          - memory.md#mem-obj-classification-log
          - memory.md#mem-obj-reports
          note: Training execution predictions/evaluator feedback and timing/log records are requested
            evidence for revisions.
        - value: trajectories
          basis: afforded
          records:
          - runtime.md#rt-rte-terminal-search
          note: Successful and failed linked task trajectories are requested analysis inputs.
        records:
        - runtime.md#rt-rte-classification-search
        - runtime.md#rt-rte-terminal-search
        - memory.md#mem-obj-classification-log
        - memory.md#mem-obj-reports
        note: Classification logs and terminal trajectories are distinct recorded sources requested by
          the procedure.
      - scope: Pilot evaluation-feedback-to-code route
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-pilot-search
          - memory.md#mem-obj-evaluation-history
          note: Controller/task execution results feed the outer editor through tool feedback.
        records:
        - runtime.md#rt-rte-pilot-search
        - memory.md#mem-obj-evaluation-history
        note: Original source is evaluate_harness execution feedback, not a new event stream merely because
          it is serialized as a tool message.
      - scope: Additional inherited summary inputs and generated/training/provider trace routes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-kira-execution
        - memory.md#mem-rte-classification-memory
        - memory.md#mem-obj-memory
        note: Exact inherited mixture and whether arbitrary candidate writes consume additional qualifying
          trace sources are not recorded. Imported static training labels do not establish an event-stream
          or session-log source.
      records:
      - runtime.md#rt-rte-kira-execution
      - runtime.md#rt-rte-classification-search
      - runtime.md#rt-rte-terminal-search
      - memory.md#mem-obj-classification-log
      - memory.md#mem-obj-reports
      - runtime.md#rt-rte-pilot-search
      - memory.md#mem-obj-evaluation-history
      - memory.md#mem-rte-classification-memory
      - memory.md#mem-obj-memory
      note: Sources follow the original qualifying experience, not JSON/event labels. Unknown routes remain
        unresolved rather than inapplicable because another qualifying route is known.
---

# Meta-Harness memory profile

## Comparison rationale

The profile classifies accepted records, not a new source inspection. No source files were read for this mapping. Evidence is implementation or shipped procedure: no finding claims observed activation, measured benefit or causal support.

The example-list duplicate resolves to [MEM-OBJ-examples](memory.md#mem-obj-examples); the superseded epistemic declaration is not used as a separate witness. No other supersession changes a value. The valid evolution-summary container is represented through [MEM-OBJ-summary-results](memory.md#mem-obj-summary-results) and [MEM-OBJ-summary-rationale](memory.md#mem-obj-summary-rationale). Software-derived counters/results do not confer derived explanatory warrant on copied model hypotheses. The broader [EPI-OBJ-val-results](epistemic.md#epi-obj-val-results) adds numerical result-file coverage, not another rationale lineage.

Storage and form are separate. A file checkpoint does not make an opaque payload symbolic merely because its name ends in JSON. Few-shot Q/A strings supply knowledge through interpretation, while list fields, resume counters and scores have fixed-rule consumers. NoMemory and unknown generated state prevent treating successful reload as universal behavioral activation. [MEM-OBJ-memory](memory.md#mem-obj-memory) and [MEM-RTE-classification-memory](memory.md#mem-rte-classification-memory) retain those alternatives.

Pull and push are operations within chains, not labels on entire workflows. A requested checkpoint or digest replay is pull; automatic demonstration selection into the solver request is push. Its input hash seeds sampling, rather than matching a retained example identity. KIRA context pressure triggers automatic continuation delivery, but the inherited summarizer's precise selection remains unknown. The visible fallback retains a screen suffix and instruction alongside surviving messages, not necessarily an entirely replaced context. See [MEM-RTE-classification-memory](memory.md#mem-rte-classification-memory), [MEM-RTE-completion-replay](memory.md#mem-rte-completion-replay) and the memory annotation on [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution).

Trace learning is not an improvement verdict. KIRA's retained continuation qualifies even within one task. Reference experience-to-code/report use remains afforded procedure; pilot feedback-to-edit wiring is not observed evidence-responsive revision. Ordinary pilot tool-message accumulation is not separately counted as derived memory. Historical scoring uses retained eligibility/reward fields, not the final candidate bytes, and does not restore best code. See [RT-RTE-classification-search](runtime.md#rt-rte-classification-search), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) and [MEM-OBJ-evaluation-history](memory.md#mem-obj-evaluation-history).

Fresh-start deletion is not classified as invalidation. The memory annotations on [RT-RTE-classification-search](runtime.md#rt-rte-classification-search) and [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search) establish selective cleanup and residual artifacts, not retention of the history of the particular withdrawn contents. That missing relation prevents a controlled curation finding for reset; it does not erase the independently supported consolidation, evolution and promotion findings.

All ten axes remain partial because the accepted inventory contains generated-candidate alternatives, unspecified checkpoint initialization, opaque inherited/provider state or selection, or unproduced model guidance. Those are local coverage limits, not evidence of absent memory or negative learning. A strong local witness never upgrades a merely afforded branch. No unsupported global absence, complete-value union or empirical improvement follows.
