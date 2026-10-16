---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Agent Workflow Memory memory comparison: file-backed workflow updates, admission evidence,
  optional retrieval and episode notes at the frozen commit.'
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
source-identity: https://github.com/zorazrw/agent-workflow-memory
reviewed-boundary: 8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1
memory-comparison:
  version: 2
  scope: 'Included: accumulated/replaced Mind2Web and WebArena workflow files; their raw conversation/trajectory
    inputs, gate signals, retained reasons and annotation metrics; initial concrete exemplars/specifiers
    and website workflow contents insofar as they supply initialization or later selection; optional retrieval
    output files/vector access structures; optional in-process episode notes and their recorded later
    display route. Excluded: unchanged shipped induction/evaluation instructions as independent memory,
    ordinary untransformed action/observation history, task configuration and benchmark ranking data as
    general runtime storage, auxiliary basic agent without workflow memory, provider model weights/internals
    and BrowserGym internal persistence implementation. Initial content provenance, external production
    control and optional-note durability remain unresolved rather than excluded.'
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Mind2Web and WebArena workflow payloads, including shipped initial contents and replacement
          outputs
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          note: Workflow text persists at configured local file paths and is reloaded by acting consumers.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        note: Both consumers load plaintext; neither workflow syntax nor source-repository shipment makes
          the operative store a graph or a repository-backed memory mechanism.
      - scope: Concrete exemplars/specifiers, saved Mind2Web conversations/metrics, WebArena raw evidence
          and evaluator signals/reasons
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          - memory.md#mem-obj-conversation
          - epistemic.md#epi-obj-annotation-metrics
          - epistemic.md#epi-rte-annotation-score
          - memory.md#mem-obj-arena-traces
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - memory.md#mem-obj-autoeval-thoughts
          note: AWM reads or writes local retained files; externally produced logs, rewards and screenshots
            are file inputs.
        records:
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-obj-conversation
        - epistemic.md#epi-obj-annotation-metrics
        - epistemic.md#epi-rte-annotation-score
        - memory.md#mem-obj-arena-traces
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-obj-autoeval-thoughts
        note: The records identify JSON/text and screenshot files at the consumer boundary. Unknown content
          provenance and external file-production details do not change this visible substrate.
      - scope: Optional retrieval index and selected output file
        assessment: known
        findings:
        - value: vector
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Dense-vector FAISS indexing and optional local save are available in the standalone retrieval
            mechanism.
        - value: files
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Selection writes consumer-ready plaintext; optional index persistence is local disk storage.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: The index is an optional access structure, not proof of successful semantic workflow retrieval.
          The workflow branch saves a FAISS store but returns the wrong object; ablation constructs its
          store directly and does not persist it.
      - scope: Optional episode scratchpad
        assessment: known
        findings:
        - value: in-memory
          basis: afforded
          records:
          - memory.md#mem-rte-episode-memory
          note: Parsed model memory text is appended to the agent list and can enter a later enabled history
            prompt.
        records:
        - memory.md#mem-rte-episode-memory
        note: The included note list is in process only. Diagnostic return does not establish external
          persistence or cross-episode reload.
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-exemplar-content
      - memory.md#mem-obj-exemplar-specifier
      - memory.md#mem-obj-conversation
      - epistemic.md#epi-obj-annotation-metrics
      - epistemic.md#epi-rte-annotation-score
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-obj-autoeval-thoughts
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      note: The recorded inventory covers operative files, optional vector access structures and episode
        notes. External trace files are included at their AWM-visible boundary, not as a claim about BrowserGym
        storage internals. Provider model weights are computations, not recorded use-updated memory in
        this boundary.
    representational_form:
      assessment: partial
      units:
      - scope: Workflow procedures, concrete exemplar message bodies, conversation input/output text and
          trace thought/action projections
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          - memory.md#mem-obj-conversation
          - memory.md#mem-obj-arena-traces
          - epistemic.md#epi-obj-trajectory-input
          note: Models consume readable tasks, examples, thoughts and procedures through message channels.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        - epistemic.md#epi-obj-trajectory-input
        note: Action spellings and HTML are interpreted by a model on these paths, not installed as executable
          workflow programs.
      - scope: Exemplar roles/specifiers, conversation action/target/statistic fields, reward and autoevaluation
          gate values, annotation metrics
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          - memory.md#mem-obj-conversation
          - memory.md#mem-obj-arena-traces
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - epistemic.md#epi-obj-annotation-metrics
          - epistemic.md#epi-rte-annotation-score
          note: Metadata controls selection/message packaging, rm or reward controls eligibility, and
            numeric metrics encode annotation agreement.
        records:
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - epistemic.md#epi-obj-annotation-metrics
        - epistemic.md#epi-rte-annotation-score
        note: Fixed consumer rules operate on metadata, Booleans, identifiers and metrics separately from
          model-interpreted text.
      - scope: Evaluation reasons and display text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-autoeval-thoughts
          note: Software retains evaluator thoughts and readable reports; downstream induction does not
            consume the reasons.
        records:
        - memory.md#mem-obj-autoeval-thoughts
        note: These are readable judgment material, not the symbolic Boolean consumed by induction.
      - scope: Optional episode scratchpad text
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-rte-episode-memory
          note: Optional model notes are rendered as history text on a later enabled model call.
        records:
        - memory.md#mem-rte-episode-memory
        note: The programmatic history path interprets the note as text; ordinary run.py disables display.
      - scope: Optional retrieval dense representations and index-to-content metadata
        assessment: known
        findings:
        - value: parametric
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Embedding service produces dense representations consumed by FAISS similarity search.
        - value: symbolic
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Numeric index metadata maps selected entries back to full workflow blocks or messages.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: The vectors select content but are not sent to the acting model. The workflow defect does
          not classify ablation as broken.
      - scope: Final screenshot payload used in vision evaluation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-arena-traces
        - epistemic.md#epi-rte-trajectory-check
        note: Records establish image delivery but not a controlled natural-language, symbolic or distributed-parametric
          classification of the consumed image part. Its display text cannot substitute for the payload.
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-exemplar-content
      - memory.md#mem-obj-exemplar-specifier
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-traces
      - epistemic.md#epi-obj-trajectory-input
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - epistemic.md#epi-obj-annotation-metrics
      - epistemic.md#epi-rte-annotation-score
      - memory.md#mem-obj-autoeval-thoughts
      - memory.md#mem-rte-episode-memory
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - epistemic.md#epi-rte-trajectory-check
      note: Textual and symbolic parts and optional dense access vectors are classified separately. Screenshot
        content has no established controlled form in the accepted records; readable captions do not classify
        image payloads.
    lineage:
      assessment: partial
      units:
      - scope: Generated Mind2Web online and WebArena neural/automatic-rule workflow text
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-conversation
          - memory.md#mem-obj-arena-traces
          note: Generated procedure or concrete-example outputs derive from recorded agent activity rather
            than parameter updates.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        note: Saved messages or selected experiment activity feed software/model generation or extraction.
          Task association and semantic fidelity remain limited, but the recorded derivation path is trace-fed.
      - scope: WebArena manually approved generated rule examples
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-arena-workflows
          note: Human-approved examples retain selected query/thought/action text extracted from recorded task experience.
        records:
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-arena-workflows
        note: Exact human approval controls admission, not trace origin; this known generated-output path does not resolve the shipped initial corpus provenance.
      - scope: Mind2Web offline workflow derivation from external annotated training examples
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          note: External annotated training representations supply the offline input content.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          note: Fixed-guidance model induction and textual filtering compile external examples into replacement
            workflow text.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        note: The inspected transformation starts with imported annotated examples. Their upstream recording
          history is outside this local derivation classification.
      - scope: Fixed action reminders appended to generated WebArena workflow files
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          note: The neural writer appends fixed click/select instructions to the generated file.
        records:
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        note: These fixed directions are a separate part from trace-derived procedures; their inclusion
          does not make all output authored from scratch.
      - scope: Initial concrete exemplars/specifiers and five shipped WebArena workflow files
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-obj-arena-workflows
        - epistemic.md#epi-obj-workflow-text
        note: Available content has no established author, extraction history or approval record. Later
          selection/replacement cannot resolve initialization lineage.
      - scope: Saved Mind2Web input/output records and derived annotation metrics
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-conversation
          note: Software saves prediction messages as per-task conversation records.
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-metrics
          - epistemic.md#epi-rte-annotation-score
          note: Programmatic comparisons produce symbolic annotation-agreement metrics.
        records:
        - memory.md#mem-obj-conversation
        - epistemic.md#epi-obj-annotation-metrics
        - epistemic.md#epi-rte-annotation-score
        note: Recorded predictions are raw traces; metrics are a separate fixed-code derivation from predictions
          and imported annotations.
      - scope: External WebArena episode logs, rewards and screenshots entering AWM
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-arena-traces
          note: Induction/evaluation readers acquire BrowserGym experiment evidence from result directories.
        records:
        - memory.md#mem-obj-arena-traces
        note: AWM imports these artifacts; their external production and persistence implementation is
          not inspected, preventing a complete origin account.
      - scope: Autoevaluation Boolean and retained model judgment reasons
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - memory.md#mem-obj-autoeval-thoughts
          - epistemic.md#epi-rte-trajectory-check
          note: Evaluator requests and status parsing derive judgment text and a retained admission signal
            from episode evidence.
        records:
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-obj-autoeval-thoughts
        - epistemic.md#epi-rte-trajectory-check
        note: The local path is evidence projection to model judgment and software status conversion,
          not independent verification of the task result.
      - scope: Optional retrieval output and dense embedding access structure
        assessment: partial
        findings:
        - value: other-compiled
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Standalone selectors compile subsets and embedding/index structures from existing text.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: Selected output reuses retained input text and vectors derive from names/docstrings or specifiers.
          Exact embedding weights and upstream parameter provenance are not pinned or inspected.
      - scope: Optional episode scratchpad
        assessment: known
        findings:
        - value: trace-extracted
          basis: afforded
          records:
          - memory.md#mem-rte-episode-memory
          note: The acting model can emit a note about previous activity that the parser retains for later
            history display.
        records:
        - memory.md#mem-rte-episode-memory
        note: Only the local note-production path is classified; no external diagnostic persistence is
          inferred.
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-obj-exemplar-content
      - memory.md#mem-obj-exemplar-specifier
      - epistemic.md#epi-obj-workflow-text
      - epistemic.md#epi-obj-annotation-metrics
      - epistemic.md#epi-rte-annotation-score
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-obj-autoeval-thoughts
      - epistemic.md#epi-rte-trajectory-check
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      note: Known derivation paths coexist with unresolved initial corpus provenance, external trace production
        and embedding provenance. No shipped example is attributed to an induction route merely because
        it is present.
    behavioral_authority:
      assessment: known
      units:
      - scope: WebArena workflow text at the legacy acting model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - runtime.md#rt-bap-workflow-system
          note: Reread workflow procedures and reminders enter the system message for subsequent action
            decisions.
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-workflow-text
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-bap-workflow-system
          note: Local factual assertions about orders, dates and website locations in the delivered whole file supply reference context to the acting model alongside directions.
        records:
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - runtime.md#rt-bap-workflow-system
        - epistemic.md#epi-obj-workflow-text
        note: System-message directions are interpreted standing guidance, not enforced subroutine dispatch; factual assertions retain their knowledge effect in the same channel.
      - scope: Mind2Web workflow and concrete demonstration content at the prediction model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          - runtime.md#rt-bap-workflow-exemplar
          note: Procedures and concrete examples supply reference context for predictions, subject to
            token-budget omission.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - runtime.md#rt-bap-workflow-exemplar
        note: User-message demonstration delivery supplies contextual advice rather than standing system
          instructions or an action oracle.
      - scope: Saved prediction records and WebArena thought/action experience at automatic workflow-update
          consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-conversation
          - memory.md#mem-obj-arena-traces
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          note: Retained experience feeds automatic regeneration of workflows later delivered to acting
            models.
        records:
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        note: These inputs feed durable behavior-shaping text updates; their update-consumer force is
          separate from the output guidance channel.
      - scope: Imported offline annotated training examples at the Mind2Web workflow-update model
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-mind-workflows
          note: Retained annotated training examples feed automatic workflow induction and file admission, producing durable behavior-shaping context for later predictions.
        records:
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-mind-workflows
        note: Learning authority at this update consumer does not require examples from this agent's own execution; downstream prediction knowledge authority is a separate path.
      - scope: Retained reward/rm signals at induction eligibility consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - memory.md#mem-obj-arena-traces
          note: Retained rm or external reward determines source eligibility against the configured predicate.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - memory.md#mem-obj-arena-traces
          note: False or missing eligible results exclude trajectories from induction inputs.
        records:
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-obj-arena-traces
        note: Truthiness supplies an admissibility criterion and a software veto for source trajectories,
          not certification of generated workflows.
      - scope: Exemplar specifiers at default filter and optional similarity selector
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          note: Website/domain/subdomain substring conditions select the candidate example scope.
        - value: ranking
          basis: afforded
          records:
          - memory.md#mem-obj-exemplar-content
          - memory.md#mem-obj-exemplar-specifier
          - memory.md#mem-rte-exemplar-ablation
          note: Embedded specifiers influence relative retrieval scores for concrete examples in the standalone
            ablation.
        records:
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-rte-exemplar-ablation
        note: Specifier strings are removed before model delivery. Default tag filtering and optional
          semantic ranking have distinct consumers and evidence bases.
      - scope: Workflow names/docstrings, dense vectors and index metadata at optional retrieval
        assessment: known
        findings:
        - value: ranking
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Retained workflow name/docstring representations are candidate scoring inputs to intended
            dense retrieval.
        - value: routing
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Index metadata selects the full retained bodies or messages for the output file.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: Ranking is supported only at the optional mechanism level; the semantic workflow object-handoff
          defect prevents successful retrieval claims.
      - scope: Evaluator reason/display files at human review; annotation metrics at result analysis
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-autoeval-thoughts
          note: Readable reports expose judgments and reasons to a possible human reviewer.
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-metrics
          - epistemic.md#epi-rte-annotation-score
          note: Stored annotation scores supply diagnostic result-analysis evidence rather than workflow
            admission criteria.
        records:
        - memory.md#mem-obj-autoeval-thoughts
        - epistemic.md#epi-obj-annotation-metrics
        - epistemic.md#epi-rte-annotation-score
        note: Readable review is afforded and metrics serve diagnostics. Neither is consumed as the online
          Mind2Web success gate; evaluator reasons do not reach the induction model.
      - scope: Optional scratchpad at later enabled acting-model history consumer
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-rte-episode-memory
          note: Retained notes can be rendered as human-message history for a later decision.
        records:
        - memory.md#mem-rte-episode-memory
        note: Programmatic display supplies contextual notes, not a standing system instruction or established
          cross-task learning route.
      records:
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - runtime.md#rt-bap-workflow-system
      - epistemic.md#epi-obj-workflow-text
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-exemplar-content
      - memory.md#mem-obj-exemplar-specifier
      - runtime.md#rt-bap-workflow-exemplar
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-rte-exemplar-ablation
      - memory.md#mem-rte-workflow-selection
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-obj-autoeval-thoughts
      - epistemic.md#epi-obj-annotation-metrics
      - epistemic.md#epi-rte-annotation-score
      - memory.md#mem-rte-episode-memory
      note: The inventory distinguishes acting directions and factual reference context, online experience
        and imported offline training examples at update consumers, eligibility controls, retrieval ranking
        inputs and display-only reasons. Authority means force at a recorded consumer,
        not observed compliance or benefit. Unconsumed fields have no inferred force.
    write_agency:
      assessment: partial
      units:
      - scope: Mind2Web offline/online induction and WebArena neural regeneration
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          note: Induction, filtering and workflow overwrite are computational admissions.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - workflow.md#wf-rte-pipeline-handoff
        note: The human chooses modes, paths and invocation, while software/model stages admit each replacement
          without per-content approval.
      - scope: WebArena rule concrete-example admission, manual and auto variants
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-rule-admission
          note: Exact human y approves each displayed candidate before inclusion.
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-rule-admission
          note: The auto flag supplies acceptance without a human content decision.
        records:
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-arena-workflows
        note: Both variants have inspected admission branches and retain distinct control. Manual review
          reasons are not persisted.
      - scope: Mind2Web conversation/metric writes and WebArena evaluator result/reason writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-conversation
          - epistemic.md#epi-obj-annotation-metrics
          - epistemic.md#epi-rte-annotation-score
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - memory.md#mem-obj-autoeval-thoughts
          note: Consumer and evaluator software persists the computed records.
        records:
        - memory.md#mem-obj-conversation
        - epistemic.md#epi-obj-annotation-metrics
        - epistemic.md#epi-rte-annotation-score
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-obj-autoeval-thoughts
        note: Models may propose judgments and predictions, but software retains them without per-record
          human approval.
      - scope: Optional retrieval-selected file/index admissions and episode-note retention
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          - memory.md#mem-rte-episode-memory
          note: Standalone selectors write subsets/indexes and the agent parser appends optional notes
            computationally.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        - memory.md#mem-rte-episode-memory
        note: Operator initiation selects configuration, not each retained item or note.
      - scope: Initial shipped exemplar/specifier and website workflow content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-exemplar-content
        - memory.md#mem-obj-exemplar-specifier
        - memory.md#mem-obj-arena-workflows
        note: No author or admission history establishes an explicit human content decision or an automatic
          initial write. Plaintext editability alone is not a manual route.
      - scope: External BrowserGym raw trace/reward/screenshot production
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-arena-traces
        note: AWM reads these files automatically, but that read does not determine control of the external
          production/admission mechanism.
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - workflow.md#wf-rte-pipeline-handoff
      - memory.md#mem-obj-conversation
      - epistemic.md#epi-obj-annotation-metrics
      - epistemic.md#epi-rte-annotation-score
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-obj-autoeval-thoughts
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      - memory.md#mem-obj-exemplar-content
      - memory.md#mem-obj-exemplar-specifier
      - memory.md#mem-obj-arena-traces
      note: Software/model admission and exact human rule approval are classified separately. Starting
        a pipeline does not make subsequent content admission manual. Initial shipped content and external
        trace production remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Mind2Web online saved-message projection to induction examples
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-conversation
          - runtime.md#rt-rte-mind-admission
          note: Selected input/output dictionaries are compressed into environment/action examples for
            the durable workflow update chain.
        records:
        - memory.md#mem-obj-conversation
        - runtime.md#rt-rte-mind-admission
        note: The update retains only last-input/output content, reducing the saved conversation representation
          while the raw file can remain separately available.
      - scope: WebArena rule trace selection and abstract-action-key deduplication
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - runtime.md#rt-rte-rule-admission
          note: Candidates sharing an abstract action key are reduced to sampled representatives.
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-arena-workflows
          note: Selected retained thought/action experience becomes a reduced concrete-example file.
        records:
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-arena-workflows
        note: Template and abstract-action keys reduce retained trajectories to selected concrete representatives;
          ignored fill values do not prove task equivalence.
      - scope: Mind2Web and WebArena neural workflow induction semantics
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-mind-admission
          - runtime.md#rt-rte-neural-admission
          note: Fixed induction instructions request common subroutines with example-specific details
            abstracted away.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - epistemic.md#epi-obj-workflow-text
        note: Requests for recurrent abstract subroutines support intended compression, not implemented
          semantic fidelity. Actual generated content could reshape or introduce claims; no source-linked
          output establishes consolidate versus synthesize for the neural content itself.
      - scope: Optional workflow/exemplar subset outputs
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: Random or similarity selection produces a smaller consumer-ready representation of existing
            workflow blocks/examples.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: These selectors reduce retained inputs without new abstraction. Duplicate returned ablation
          indices are not deduplicated.
      - scope: Optional episode scratchpad content transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-episode-memory
        note: The parser retains optional model text, but the route does not require summarization or
          replace full history. Without an emitted note, no specific curation operation is established.
      records:
      - memory.md#mem-obj-conversation
      - runtime.md#rt-rte-mind-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-arena-workflows
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-neural-admission
      - epistemic.md#epi-obj-workflow-text
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      note: Rule deduplication and reduced retained-message projections establish implemented operations.
        Neural prompts request abstraction, but absent source-linked generated output leaves the semantic
        operation unresolved; replacement alone is neither evolve nor invalidate-with-history.
    read_back_direction:
      assessment: known
      units:
      - scope: Default workflow reads at later Mind2Web sample and WebArena action invocations
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-benchmark-action
          - runtime.md#rt-rte-browser-action
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          note: Later prediction/action invocations request workflow text from the configured path.
        records:
        - runtime.md#rt-rte-benchmark-action
        - runtime.md#rt-rte-browser-action
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        note: Configured workflow paths are request inputs. Reading and delivering the selected whole
          file is one pull chain, not a second push; Mind2Web can omit oversized content.
      - scope: Saved conversation and experiment/result reads at later evaluator or induction calls
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-conversation
          - memory.md#mem-obj-arena-traces
          - memory.md#mem-obj-autoeval-signal
          - epistemic.md#epi-rte-success-selection
          - epistemic.md#epi-rte-trajectory-check
          note: Induction/evaluation invocations request and select persisted conversation or episode
            evidence.
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-autoeval-thoughts
          note: Readable reason/display files afford requested human inspection.
        records:
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-obj-autoeval-thoughts
        - epistemic.md#epi-rte-trajectory-check
        note: Update/evaluation consumers explicitly read accumulated result artifacts. Human report review
          is a possible reader, not unsolicited delivery.
      - scope: Standalone workflow/exemplar retrieval and configured output-file handoff
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-workflow-selection
          - memory.md#mem-rte-exemplar-ablation
          - runtime.md#rt-cmp-openai-embeddings
          note: CLI task/count requests drive selection, with optional later prediction-file consumption.
        records:
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        note: The operator requests selection, and a later configured consumer requests its output. Semantic
          workflow failure limits implementation strength, not the requested direction of the intended
          route.
      - scope: Optional scratchpad return through enabled history
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-episode-memory
          note: A later configured model invocation can receive retained per-step memory in requested
            history.
        records:
        - memory.md#mem-rte-episode-memory
        note: Enabled history/memory flags request the prior notes as context; ordinary CLI disables note
          display. No independent push selector is recorded.
      records:
      - runtime.md#rt-rte-benchmark-action
      - runtime.md#rt-rte-browser-action
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-obj-autoeval-thoughts
      - epistemic.md#epi-rte-trajectory-check
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      note: Recorded later-consumer routes request files, traces or configured history. Optional retrieval
        and scratchpad paths remain afforded, not upgraded to ordinary wiring. The inventory contains
        no independent unsolicited delivery chain; static unchanged corpus shipment is not itself read-back.
    read_back_signal:
      assessment: inapplicable
      units:
      - scope: Default workflow reads, requested update/evaluation evidence, optional retrieval outputs
          and enabled episode history
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-benchmark-action
        - runtime.md#rt-rte-browser-action
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-arena-traces
        - memory.md#mem-obj-autoeval-signal
        - epistemic.md#epi-rte-success-selection
        - memory.md#mem-rte-workflow-selection
        - memory.md#mem-rte-exemplar-ablation
        - runtime.md#rt-cmp-openai-embeddings
        - memory.md#mem-rte-episode-memory
        - memory.md#mem-obj-autoeval-thoughts
        note: Every included read-back operation is requested file/evidence/history consumption. No independent
          push operation remains to classify; identifiers on requested files do not establish identifier-based
          push.
      records:
      - runtime.md#rt-rte-benchmark-action
      - runtime.md#rt-rte-browser-action
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-obj-autoeval-signal
      - epistemic.md#epi-rte-success-selection
      - memory.md#mem-rte-workflow-selection
      - memory.md#mem-rte-exemplar-ablation
      - runtime.md#rt-cmp-openai-embeddings
      - memory.md#mem-rte-episode-memory
      - memory.md#mem-obj-autoeval-thoughts
      note: This axis classifies push selectors. The complete recorded direction inventory is pull-only,
        including optional alternatives; file names, corpus tag filters and requested semantic search
        are not push signals.
    trace_learning:
      assessment: partial
      units:
      - scope: Mind2Web online saved conversation to durable workflow to later prediction
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-conversation
          note: Automatic trace-fed workflow production changes a durable behavior-shaping context artifact.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-conversation
        note: Recorded model messages feed computational induction/overwrite and a later user-exemplar
          consumer. Order-based task pairing limits provenance accuracy, not existence of the write chain.
      - scope: Mind2Web offline annotated training trajectories to durable workflow
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          note: Annotated training trajectories feed software/model generation of retained procedures
            for later samples.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        note: Imported multi-step action examples record task activity; traces need not originate in this
          agent's own execution. Automatic admission and later workflow consumption are inspected.
      - scope: WebArena neural and automatic-rule trajectory to durable system-guidance workflow
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-arena-traces
          note: Selected recorded browser experience feeds automatic durable workflow generation or concrete-example
            admission and subsequent system-message supply.
        records:
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-arena-traces
        - workflow.md#wf-rte-pipeline-handoff
        note: This is wiring for configured eligible traces, not observed default pipeline success. Filename
          mismatch and empty-example generation prevent asserting each replacement is actually trace-fed.
      - scope: WebArena manually approved rule examples
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-rule-admission
        note: This variant has an explicit human per-item admission and therefore is not a qualifying
          automatic write, even though its content derives from traces.
      - scope: Optional episode scratchpad production and later history display
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-episode-memory
        note: 'A later in-episode note consumer is afforded, but durable behavior-shaping retention is
          not established: notes are an in-process list, no checkpoint/reload is recorded, and external
          diagnostic persistence is uninspected. Prevents a yes or bounded no for this route.'
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-arena-traces
      - workflow.md#wf-rte-pipeline-handoff
      - memory.md#mem-rte-episode-memory
      note: Automatic trace-fed durable workflow updates qualify architecturally, without requiring improved
        performance or learning from only the agent's own executions. Manual rule approval is not automatic.
        Optional episode notes have no established durable later-consumer horizon, so a positive workflow
        witness does not resolve that alternative.
    trace_source:
      assessment: partial
      units:
      - scope: Mind2Web online automatic workflow update
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          - memory.md#mem-obj-conversation
          note: Online induction consumes saved model input/output records projected from per-task conversations.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        - memory.md#mem-obj-conversation
        note: Last user input/model output pairs are recorded conversational turns from prediction sessions.
          Benchmark observations and annotated previous actions occur inside those messages; no executed-browser
          trajectory is inferred.
      - scope: Mind2Web offline automatic workflow update
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records:
          - memory.md#mem-obj-mind-workflows
          - runtime.md#rt-rte-mind-admission
          note: Offline induction receives annotated task trajectories rather than online session records.
        records:
        - memory.md#mem-obj-mind-workflows
        - runtime.md#rt-rte-mind-admission
        note: The original imported annotated training examples are multi-step task action representations;
          their external corpus correctness is unverified, but the route's source type is recorded.
      - scope: WebArena neural and automatic-rule workflow updates
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records:
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-arena-traces
          note: Grouped query/thought/action sequences record multi-step browser-task experience.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-arena-workflows
          - runtime.md#rt-rte-neural-admission
          - runtime.md#rt-rte-rule-admission
          - memory.md#mem-obj-arena-traces
          note: Recorded browser action requests from experiment logs feed the workflow update projection.
        records:
        - memory.md#mem-obj-arena-workflows
        - runtime.md#rt-rte-neural-admission
        - runtime.md#rt-rte-rule-admission
        - memory.md#mem-obj-arena-traces
        note: The source is selected linked task thought/action histories. Recorded browser action requests
          are tool activity within that trajectory; screenshots/rewards primarily support admission and
          are not forwarded as full induction inputs.
      - scope: WebArena manual rule variant
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-rule-admission
        note: Its human content admission is outside the qualifying automatic trace-learning route; trace
          provenance remains classified under lineage instead.
      - scope: Optional episode scratchpad update
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-episode-memory
        note: Durable trace learning is unresolved and no emitted note/input provenance is supplied. Possible
          action-effect notes do not establish which original trace content a qualifying durable write
          consumes.
      records:
      - memory.md#mem-obj-mind-workflows
      - runtime.md#rt-rte-mind-admission
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-arena-workflows
      - runtime.md#rt-rte-neural-admission
      - runtime.md#rt-rte-rule-admission
      - memory.md#mem-obj-arena-traces
      - memory.md#mem-rte-episode-memory
      note: Original content of known qualifying workflow updates includes recorded session messages,
        imported annotated multi-step trajectories and WebArena browser trajectories/action requests.
        The optional scratchpad qualification and original input mixture remain unresolved. Adapter/event
        labels are not used as trace origins.
---

# Agent Workflow Memory memory profile

## Comparison rationale

This profile classifies accepted records, not new source observations. Reconciliation makes no supersession: broad epistemic containers and narrower memory parts remain valid, so citations retain their original declaring members. Optional retrieval uses its own afforded consumer handoff; the broader wired selection record does not upgrade either that handoff or the broken semantic workflow branch. [MEM-RTE-workflow-selection](memory.md#mem-rte-workflow-selection) and [MEM-RTE-exemplar-ablation](memory.md#mem-rte-exemplar-ablation) preserve the distinct index handoffs.

The operative workflow store is a file, not a workflow graph. Action notation is interpreted as guidance. WebArena's system-message procedures have instruction authority, while the whole file's local factual assertions about orders, dates and website locations also supply knowledge. System-message placement does not erase this reference-context effect. Mind2Web's user-message demonstrations supply knowledge. At the separate update consumer, saved experience and imported offline annotated training examples have learning authority because they feed durable behavior-shaping files. These paths do not establish compliance, improved capacity or causal benefit. See [EPI-OBJ-workflow-text](epistemic.md#epi-obj-workflow-text), [MEM-OBJ-arena-workflows](memory.md#mem-obj-arena-workflows), [RT-BAP-workflow-system](runtime.md#rt-bap-workflow-system), [RT-BAP-workflow-exemplar](runtime.md#rt-bap-workflow-exemplar), [MEM-OBJ-conversation](memory.md#mem-obj-conversation), [MEM-OBJ-arena-traces](memory.md#mem-obj-arena-traces), [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission) and [MEM-OBJ-mind-workflows](memory.md#mem-obj-mind-workflows).

Eligibility signals supply both a criterion and a veto: validation and enforcement apply to source admission, not to the truth of generated workflows. Retained evaluator reasons have a possible human-review consumer, but induction consumes the Boolean rather than those reasons. Metric records are diagnostics, not the online writer's success gate. See [MEM-OBJ-autoeval-signal](memory.md#mem-obj-autoeval-signal), [MEM-OBJ-autoeval-thoughts](memory.md#mem-obj-autoeval-thoughts) and [EPI-OBJ-annotation-metrics](epistemic.md#epi-obj-annotation-metrics).

Generated manual-rule examples retain trace-extracted lineage: human approval changes admission control, not the origin of selected query/thought/action content. See [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) and [MEM-OBJ-arena-workflows](memory.md#mem-obj-arena-workflows). Known later transformations do not resolve the initial lineage or content-control of shipped exemplars and website files. The vector access route likewise establishes derivation from selector text, not exact embedding-parameter provenance. The final screenshot remains an unresolved consumed part on the form axis rather than being classified through its caption. These limits are carried in [MEM-OBJ-exemplar-content](memory.md#mem-obj-exemplar-content), [MEM-OBJ-exemplar-specifier](memory.md#mem-obj-exemplar-specifier), [MEM-OBJ-arena-workflows](memory.md#mem-obj-arena-workflows), [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) and [EPI-RTE-trajectory-check](epistemic.md#epi-rte-trajectory-check).

Curation separates inspected reduction from requested abstraction. Saved-message projection and concrete rule extraction reduce retained experience; abstract-action deduplication selects representatives. Neural prompts ask for common subroutines, but generated semantic fidelity is unobserved, leaving their actual transformation partial rather than asserting synthesis. Whole-file regeneration does not establish editing an existing entry, decay, promotion, or invalidation that preserves history. See [MEM-OBJ-conversation](memory.md#mem-obj-conversation), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission) and [EPI-OBJ-workflow-text](epistemic.md#epi-obj-workflow-text).

Read-back is pull at the requested consumption operations. A configured file path is not an identity-matching push selector, and supplying requested text is not another push. Optional retrieval is requested preprocessing followed by an optional configured file read. Enabled scratchpad history is also a configured context request, not independently unsolicited supply. Thus read-back signal is inapplicable over the complete recorded direction inventory, not absent or embedding-valued simply because retrieval uses embeddings. See [RT-RTE-benchmark-action](runtime.md#rt-rte-benchmark-action), [RT-RTE-browser-action](runtime.md#rt-rte-browser-action), [MEM-RTE-workflow-selection](memory.md#mem-rte-workflow-selection), [MEM-RTE-exemplar-ablation](memory.md#mem-rte-exemplar-ablation) and [MEM-RTE-episode-memory](memory.md#mem-rte-episode-memory).

Trace learning here is automatic trace-fed durable artifact production, not proven improvement. Offline annotated trajectories can qualify even though they are imported rather than this agent's own runs. Online prediction sessions qualify without live browsing. WebArena automatic routes qualify when selected traces reach regeneration; the default filename mismatch and possible zero-example write prevent treating every scheduled update as an exercised trace-fed one. Manual rule approval stays outside the automatic route. Scratchpad display is only afforded, ordinary run.py disables it, and its durable retention is not established; neither a system-wide no nor a resolved trace source follows. See [RT-RTE-mind-admission](runtime.md#rt-rte-mind-admission), [RT-RTE-neural-admission](runtime.md#rt-rte-neural-admission), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [WF-RTE-pipeline-handoff](workflow.md#wf-rte-pipeline-handoff) and [MEM-RTE-episode-memory](memory.md#mem-rte-episode-memory).

Source-read log: none. Classification used only the supplied accepted records and reconciliation; no source ambiguity required a permitted source read. There are no new records, quotations, observed runs or causal results.
