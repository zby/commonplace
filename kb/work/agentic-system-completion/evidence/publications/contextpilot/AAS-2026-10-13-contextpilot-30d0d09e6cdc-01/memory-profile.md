---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'ContextPilot memory comparison: task findings and access structures, retained context replacements,
  evaluation artifacts and trace-trained policy/checkpoint state.'
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
source-identity: https://github.com/Tencent/ContextPilot
reviewed-boundary: 782cbb6611fb610c4cf6fafda6022b7e89cae191
memory-comparison:
  version: 2
  scope: 'Included: through-use structured findings and simple notes, their symbolic graph and dense access
    representations, retained original traces and context replacements, branch copies, saved task/evaluation
    artifacts at their later consumers, trace-derived credit, updated actor/rollout parameters and configured
    checkpoint/recovery state; generic initialization, optional merge and possible opaque endpoint-side
    retention remain included uncertainties. Excluded: shipped static prompts/tools, ordinary attached-document/chunk/search
    state and chunk vectors as current-task input rather than accumulated memory, and unchanged provider/base-model
    parameters without an evidenced through-use retention path. Separate inference adoption of trained
    checkpoints is not established.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Task-local findings, simple notes, symbolic access graph, signature vectors, original history,
          replacement maps and branch copies
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          - runtime.md#rt-rte-branch-credit
          note: Task and branch objects reside in process-local containers, including graph dictionaries
            and dense arrays.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        - runtime.md#rt-rte-branch-credit
        note: These parts are retained in Python containers or NumPy arrays across later calls; branch
          copies preserve them. Their distinct forms do not change their local substrate.
      - scope: Serialized task trajectories and prediction/evaluation artifacts at their report consumers
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - epistemic.md#epi-obj-answer-content
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-offline-evaluation
          note: JSONL/result/trajectory files retain task products for logging and evaluation.
        records:
        - runtime.md#rt-obj-full-history
        - epistemic.md#epi-obj-answer-content
        - epistemic.md#epi-obj-evaluation-results
        - epistemic.md#epi-rte-offline-evaluation
        note: History/edit maps are exported to files; saved predictions are later read by the offline
          evaluator. This does not establish a fresh-task note-store reload.
      - scope: Training actor and synchronized rollout policy parameters
        assessment: known
        findings:
        - value: model-weights
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Gradient updates persist in the actor/rollout parameter tensors.
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Worker model/device memory holds the live tensors.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: Updated numerical policy is consumed by later rollout generations; exact initial weights
          and deployed inference adoption are unresolved.
      - scope: Configured training checkpoint and recovery artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          note: Checkpoint files and data-loader/latest-step recovery files are saved and reloaded.
        records:
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        note: Checkpoint storage is distinct from task note dictionaries; contents are configuration-dependent.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its storage substrate; no local witness
          resolves it. Fixed or unpinned provider weights alone are not classified as accumulated memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-branch-credit
      - epistemic.md#epi-obj-answer-content
      - epistemic.md#epi-obj-evaluation-results
      - epistemic.md#epi-rte-offline-evaluation
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Inventory covers task stores, access structures, retained history/replacements, exported traces
        and the training policy/checkpoint route. Endpoint-side retention remains uninspected; no repository/database
        substrate is inferred from JSON encoding or dictionary graph structure.
    representational_form:
      assessment: partial
      units:
      - scope: Finding and simple-note content, summaries and optional relation/evidence prose at the
          QA policy
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          note: Full content and advertised summaries supply model-interpreted text.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        note: The model interprets these strings rather than executing them as dispatcher rules.
      - scope: Replacement summaries, spans, compression output and retained conversational/tool-result
          text at later model calls
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Replacement and retained original text receive consequences through model interpretation.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: A deletion notice is not evidence; summary/span bytes are natural-language input even when
          semantically lossy.
      - scope: Keys, normalized graph signatures, adjacency scores, history edit maps and checkpoint/ancestry
          controls
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          note: IDs, sets, scores and recovery markers determine fixed selection/render/recovery behavior.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        note: Fixed matching, ordering and visibility rules consume these localized units. This does not
          turn textual entity descriptions into executable rules.
      - scope: Memory signature vectors at pair scoring
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-mem-embeddings
          note: Distributed dense representations contribute the similarity bonus.
        records:
        - memory.md#mem-obj-mem-embeddings
        note: Dense arrays are separate from their text inputs and from provider parameters.
      - scope: Updated actor/rollout parameters at generation
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Policy tensors shape later token distributions.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: The route changes distributed numerical state, not a retained prose criticism.
      - scope: Saved answers and evaluation results
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-answer-content
          - epistemic.md#epi-obj-evaluation-results
          note: Answers and judge supporting prose are interpreted text.
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-answer-content
          - epistemic.md#epi-obj-evaluation-results
          note: Option labels, parsed verdicts and rewards have fixed scoring/aggregation consumers.
        records:
        - epistemic.md#epi-obj-answer-content
        - epistemic.md#epi-obj-evaluation-results
        note: Answer text and judge reasoning differ from option labels, booleans and scalar rewards.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its representational form; no local
          witness resolves it. Fixed or unpinned provider weights alone are not classified as accumulated
          memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - epistemic.md#epi-obj-answer-content
      - epistemic.md#epi-obj-evaluation-results
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Operative text, symbolic selectors and dense numerical state are split by consumption. Unknown
        provider retention is not classified from readable API results.
    lineage:
      assessment: partial
      units:
      - scope: Foreground model findings and simple-note text on the inspected write route
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          note: Foreground policy authors the admitted text under evidence-saving guidance.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        note: The model supplies retained content; software normalizes fields and admits it. Generic caller
          initialization is a separate unresolved unit.
      - scope: Generated history summaries, selected spans and compressed replacements
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: The retained replacement is derived from accumulated history rather than a shipped instruction.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: Recorded assistant/tool messages feed retained replacements which enter later model calls.
          External compressor semantics and initial model provenance remain separately unresolved.
      - scope: Normalized signatures, graph edges and locally computed memory-vector derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          note: Normalization, feature overlap and vector computation produce access structures from stored
            content.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        note: These are compiled from current retained text; this known derivation does not identify embedding-model
          provenance.
      - scope: Default optional merge concatenation
        assessment: known
        findings:
        - value: other-compiled
          basis: afforded
          records:
          - memory.md#mem-rte-memory-merge
          note: Implemented concatenation compiles selected entries without establishing a novel claim.
        records:
        - memory.md#mem-rte-memory-merge
        note: Existing entries are concatenated into a reduced-schema object; optional replacement-summary
          origin is not settled by that default.
      - scope: Reward-derived training policy changes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Task experience drives retained policy changes consumed by rollout synchronization.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: Generated actions/outcomes feed rewards and advantages, then numerical updates. This finding
          concerns update lineage, not the initial checkpoint.
      - scope: Initial task-store dictionaries, configured initial policy/checkpoint and embedding-provider
          provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-document-index
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-cmp-embedding-provider
        - runtime.md#rt-cmp-actor-module
        note: Generic callers may initialize dictionaries; model paths/endpoint names do not identify
          how initial retained content or numerical representations originated. An imported versus authored
          or trace-derived initial lineage cannot be completed from these records.
      - scope: Optional merge caller-supplied replacement summary
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-merge
        note: The concatenation branch is known, but a hypothetical caller can supply another summary.
          Its origin and relation to the inputs are unspecified.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its lineage; no local witness resolves
          it. Fixed or unpinned provider weights alone are not classified as accumulated memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - memory.md#mem-rte-memory-merge
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - memory.md#mem-obj-document-index
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Known derivation routes coexist with unresolved initialization and embedding/model provenance.
        Model authorship of saved text does not prove whether any particular proposition was copied, derived
        or conjectured.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Saved findings, simple notes and history replacements consumed by the QA policy
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Later model calls receive the saved or compacted evidence as context.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: Delivered text supplies context/evidence/advice; the records do not establish standing retained
          instructions or guaranteed obedience.
      - scope: Memory content/features/vectors and graph scores consumed by neighbor ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          note: Text-derived features, dense similarity and retained edge scores prioritize neighbor projections.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        note: Stored content influences relative priority through fixed overlap rules and optional cosine
          similarity; no learned ranking policy is required.
      - scope: Retained keys, edit markers and restoration eligibility at fixed store/renderer controls
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Keys and message IDs select entries and rendering positions.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Stored deletion/edit markers suppress or substitute original history at rendering.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Retained restore eligibility and membership determine whether requested restoration/read
            targets are admissible.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: Keys route addressed reads; deletion/replacement markers enforce visibility. Eligibility
          determines whether an explicit restore is admissible, not whether text is true.
      - scope: Training trajectory outcomes, terminal ancestry and reward metadata at row selection and
          actor update
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-answer-reward
          note: Trace-derived rewards/advantages feed an update of durable policy parameters.
        - value: ranking
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-answer-reward
          note: Reward comparisons determine relative advantage for policy optimization.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-answer-reward
          note: Prefix ancestry assigns descendant outcomes to snapshot rows.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-answer-reward
          note: Terminal-lineage presence determines admissibility of training rows.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-answer-reward
          note: Rows lacking terminal descendants are dropped rather than delivered to optimization.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - epistemic.md#epi-obj-evaluation-results
        - epistemic.md#epi-rte-answer-reward
        note: The update consumer uses retained experience to change policy parameters; ancestry also
          selects eligible descendants/rows. These effects do not accept memory claims as true.
      - scope: Updated policy tensors at later rollout generation
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          - runtime.md#rt-rte-policy-update
          note: Updated tensors determine relative token probabilities at the rollout policy.
        records:
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        - runtime.md#rt-rte-policy-update
        note: Numerical parameters shape action/token preferences, distinct from the learning authority
          of the experience at the updater.
      - scope: Checkpoint and data-loader recovery state at the trainer
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-policy-update
          note: Latest-step and data-loader recovery state select the resumed training position.
        records:
        - runtime.md#rt-rte-policy-update
        note: Saved step/data-loader state selects resumption and policy tensors restore the training
          machinery; deployment of a checkpoint to separate inference is not established.
      - scope: Saved answer and judgment files at offline evaluation/aggregation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-answer-content
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-offline-evaluation
          note: Retained predictions supply the candidate evidence presented to the evaluator.
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-obj-answer-content
          - epistemic.md#epi-obj-evaluation-results
          - epistemic.md#epi-rte-offline-evaluation
          note: Retained prediction IDs match references and select rows for scoring.
        records:
        - epistemic.md#epi-obj-answer-content
        - epistemic.md#epi-obj-evaluation-results
        - epistemic.md#epi-rte-offline-evaluation
        note: Predictions supply evaluation inputs; symbolic judgment labels determine recorded counts
          and aggregates, not a pre-answer veto.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its consumer and behavioral authority;
          no local witness resolves it. Fixed or unpinned provider weights alone are not classified as
          accumulated memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - epistemic.md#epi-obj-evaluation-results
      - epistemic.md#epi-rte-answer-reward
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - epistemic.md#epi-obj-answer-content
      - epistemic.md#epi-rte-offline-evaluation
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: 'Authority is local to actual consumers: evidence at the QA model, ranking and visibility
        at selectors/renderers, and learning at the training update consumer. Hidden provider retention
        prevents complete coverage; static prompt authority is outside this memory scope.'
    write_agency:
      assessment: partial
      units:
      - scope: Foreground finding/note admission and update in inference and training
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          note: Software/model admission determines retained content.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        note: Models propose content and software checks modes/keys/arguments; no per-finding human approval
          is present in the traced route.
      - scope: Foreground history editing, compressor/fallback output and host eviction maps
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Model calls and runtime limit/recovery rules admit the replacement/visibility state.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: A supplied manual summary means model-supplied text here, not a human content decision.
          Code applies edits after target checks.
      - scope: Graph/signature/vector refresh on ordinary finding writes and branch cloning
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-rte-branch-credit
          note: Local computation admits refreshed access structures and branch state.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        - runtime.md#rt-rte-branch-credit
        note: Software recomputes or copies retained state after admitted actions.
      - scope: Training parameter updates and configured periodic checkpoint saves
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Trainer and workers determine each parameter update and checkpoint write.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: The optimizer can skip nonfinite gradients; otherwise computation admits updates. Periodic
          validation is not per-update human or quality approval.
      - scope: Prediction/trajectory recording and offline annotation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-fsm-inference
          - epistemic.md#epi-rte-offline-evaluation
          - epistemic.md#epi-obj-evaluation-results
          note: Runner and evaluator code admit output records without per-record operator approval.
        records:
        - runtime.md#rt-rte-fsm-inference
        - epistemic.md#epi-rte-offline-evaluation
        - epistemic.md#epi-obj-evaluation-results
        note: The runner/evaluator writes outputs programmatically after task execution or failure.
      - scope: Generic caller initialization or replacement of stores/initial checkpoint
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-document-index
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-cmp-vllm-client
        note: Caller identity and configurable model paths do not establish who approves particular retained
          content. Neither automatic nor manual is inferred for this separate admission mechanism.
      - scope: Optional merge invocation and supplied replacement summary
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-merge
        note: The code has no approval dialog, but generic caller identity does not identify human per-content
          control. Implemented mutation alone does not classify its admission agency.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its write admission control; no local
          witness resolves it. Fixed or unpinned provider weights alone are not classified as accumulated
          memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - runtime.md#rt-rte-fsm-inference
      - epistemic.md#epi-rte-offline-evaluation
      - epistemic.md#epi-obj-evaluation-results
      - memory.md#mem-obj-document-index
      - runtime.md#rt-cmp-vllm-client
      - memory.md#mem-rte-memory-merge
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Inspected foreground writes, compaction and training updates use computational admission without
        a per-content human decision. Starting a run is not manual admission. Generic initialization,
        optional merge callers and endpoint state remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Finding/simple-note append and overwrite
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          note: Append/overwrite revises retained entries and their advertised summaries.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        note: Existing entries can be revised; training and inference differ in how omitted new summaries
          are handled.
      - scope: Finding withdrawal from current stores
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-simple-notes
          - memory.md#mem-rte-findings-write
          - memory.md#mem-rte-findings-delivery
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          note: Deleted current entries cease to supply current-store read-back despite retained history.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        note: Delete removes current lookup/injection and graph edges, while old trace/snapshot copies
          can remain; withdrawal is operational, not a judgment of falsity.
      - scope: History summary, selected-span and local random-word fallback routes
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: History is reduced to a summary, chosen span or sampled-word representation for later
            calls.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: These retain a reduced representation of recorded material. A dropped negation is a faithfulness
          defect, not synthesis. Original history remains host-reachable.
      - scope: Host history stubbing and configured old-checkpoint retention
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-context-control
          - runtime.md#rt-rte-training-rollout
          - runtime.md#rt-rte-policy-update
          note: Budget/age rules remove historical material from later prompt availability and older configured
            checkpoints from storage.
        records:
        - runtime.md#rt-rte-context-control
        - runtime.md#rt-rte-training-rollout
        - runtime.md#rt-rte-policy-update
        note: Context eviction forgets material from the live prompt view; checkpoint retention can delete
          older saves. Neither implies decay of all note entries.
      - scope: Optional merge of selected retained structured entries
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - memory.md#mem-rte-memory-merge
          note: Several retained entries become one reduced-schema combined entry.
        records:
        - memory.md#mem-rte-memory-merge
        note: Default concatenation combines entries and removes originals/metadata; it is not dedup or
          validated synthesis.
      - scope: External compressor output transformation and optional merge supplied summary
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        - memory.md#mem-rte-memory-merge
        note: The compressor is called and its output retained, but opaque semantic transformation is
          not classified from its name or output size. The merge caller can supply a replacement summary
          with unknown content relation. Known local fallback/default-concatenation findings remain.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its curation transformation; no local
          witness resolves it. Fixed or unpinned provider weights alone are not classified as accumulated
          memory.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-training-rollout
      - runtime.md#rt-rte-policy-update
      - memory.md#mem-rte-memory-merge
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Positive operations concern implemented changes to retained content or availability. Index
        rebuilds alone are not curation; no synthesis or dedup is inferred from labels, lossiness or merging.
        Opaque compression and optional summary branches prevent complete classification.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit note and structured-memory key reads, with separate neighbor expansion
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-findings-delivery
          - memory.md#mem-obj-mem-edges
          note: Requested readNote/loadMemory returns the addressed full entry.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-findings-delivery
          - memory.md#mem-obj-mem-edges
          note: Graph code adds ranked neighbor projections beyond the requested anchor.
        records:
        - memory.md#mem-rte-findings-delivery
        - memory.md#mem-obj-mem-edges
        note: The policy requests an anchor entry. Its requested return is pull; graph-selected additional
          projections are unsolicited selection within the same chain.
      - scope: Automatic all-summary rendering and mandatory-review failure recovery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-findings-delivery
          - runtime.md#rt-rte-fsm-inference
          note: Renderer injection and runtime recovery automatically select and deliver retained material.
        records:
        - memory.md#mem-rte-findings-delivery
        - runtime.md#rt-rte-fsm-inference
        note: Each rebuild supplies summaries without a fresh read request. API failure can make the FSM
          select/read the latest key without model selection.
      - scope: Edited-history rendering and branch continuation copies
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          - runtime.md#rt-rte-branch-credit
          note: Runtime rebuild/copy routes supply retained content without a new content request.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        - runtime.md#rt-rte-branch-credit
        note: Retained replacements are substituted on subsequent payload construction; branch reconstruction
          supplies copied retained task state to continuations.
      - scope: Reward rows and updated policy synchronization
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Automatic credit propagation and weight transfer supply retained experience/parameters
            to later consumers.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: The worker/trainer forwards trace-derived credit into updates and changed policy tensors
          into later rollout generation.
      - scope: Configured checkpoint resume and offline prediction-file evaluation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-policy-update
          - epistemic.md#epi-rte-offline-evaluation
          note: Named resume/scoring operations request retained files for their consumers.
        records:
        - runtime.md#rt-rte-policy-update
        - epistemic.md#epi-rte-offline-evaluation
        note: A trainer resume operation explicitly loads saved state; the scoring CLI explicitly requests
          its prediction file.
      - scope: Optional merged entry after a configured invocation
        assessment: known
        findings:
        - value: push
          basis: afforded
          records:
          - memory.md#mem-rte-memory-merge
          note: A merged summary can enter the automatic list.
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-memory-merge
          note: A configured caller can request the merged entry by key.
        records:
        - memory.md#mem-rte-memory-merge
        note: Once admitted, merged summaries participate in injection and full content can be requested
          by key; no shipped merge caller is established.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its read-back direction; no local
          witness resolves it. Fixed or unpinned provider weights alone are not classified as accumulated
          memory.
      records:
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-mem-edges
      - runtime.md#rt-rte-fsm-inference
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - epistemic.md#epi-rte-offline-evaluation
      - memory.md#mem-rte-memory-merge
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Both requested return and unsolicited selection/delivery occur. Document search over ordinary
        task input and loading static instructions are excluded; requested returns are not counted as
        additional pushes merely because code delivers them.
    read_back_signal:
      assessment: partial
      units:
      - scope: All-summary injection and latest-key FSM recovery
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-findings-delivery
          note: All available summaries and the latest inserted key are selected without semantic relevance
            ranking.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-findings-delivery
          note: The automatically selected recovery key is matched to the full retained entry delivered
            by the synthetic read.
        records:
        - memory.md#mem-rte-findings-delivery
        note: 'Trigger: payload rebuild or review API failure. Selector inputs: current store availability/insertion
          order. Selected parts: all current summaries or the latest entry. Keyed recovery then resolves
          that selected key exactly.'
      - scope: Graph neighbor projections accompanying a requested anchor
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          note: Normalized overlapping textual/structured features score and select related entries.
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-obj-mem-edges
          - memory.md#mem-obj-mem-embeddings
          - memory.md#mem-rte-findings-delivery
          note: When configured and successful, dense similarity adds a selection bonus to graph edges.
        records:
        - memory.md#mem-obj-mem-edges
        - memory.md#mem-obj-mem-embeddings
        - memory.md#mem-rte-findings-delivery
        note: 'Trigger: loadMemory. Selector inputs: stored normalized entity/time/facet/relation features
          and edge scores. Selected parts: bounded neighbor summaries/episodes/reasons, not opaque full
          payloads.'
      - scope: Edited-history push at later payload construction
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Actual message-ID membership selects which retained replacement bytes are delivered.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: 'Trigger: rebuild. Selector input: retained message IDs and edit/precedence maps. Selected
          part: the corresponding replacement or original at that message position.'
      - scope: Branch reconstruction, credit propagation and rollout synchronization
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Branch copies and weight synchronization deliver available task/parameter state without
            semantic targeting.
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          note: Prefix-node ancestry matches terminal descendant outcomes to the snapshot rows receiving
            reward.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        note: 'Triggers: allocated continuation, reward assignment and weight sync. Complete clone/current
          parameter delivery is coarse; prefix-node ancestry targets the snapshot rewards delivered to
          the trainer.'
      - scope: Optional merged summary automatic listing
        assessment: known
        findings:
        - value: coarse
          basis: afforded
          records:
          - memory.md#mem-rte-memory-merge
          note: The same all-summary availability selector can supply the merged summary.
        records:
        - memory.md#mem-rte-memory-merge
        note: If merge is invoked, its resulting summary joins all available summaries at the next render;
          this is not targeted selection by new-key identity.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its push selector and selected retained
          part; no local witness resolves it. Fixed or unpinned provider weights alone are not classified
          as accumulated memory.
      records:
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-mem-edges
      - memory.md#mem-obj-mem-embeddings
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - memory.md#mem-rte-memory-merge
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      - runtime.md#rt-cmp-llmlingua2
      note: Signals classify actual push selectors, not the key on a requested pull. Summary availability,
        graph targeting, message-ID substitution and training delivery have distinct warrants. Opaque
        alternative retention prevents complete coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic retained history summary/span/local-fallback production and later policy input
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Automatic trace-fed retained context changes shape later model inputs.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: Recorded assistant/tool messages feed software/model-admitted replacements retained across
          invocations, then delivered as context. Durability here is later in-task consumption, not proven
          cross-session persistence.
      - scope: Scored rollout/branch experience to parameters and later rollout consumer
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          - epistemic.md#epi-rte-answer-reward
          note: The wired trace-to-policy-to-rollout chain meets the write-route definition; improved
            capacity is unobserved.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        - epistemic.md#epi-rte-answer-reward
        note: Trajectories/outcomes produce rewards and advantages, automatic optimizer changes persist
          in parameters/checkpoints, and synchronization supplies later generations.
      - scope: Saved finding/note writes with variable source and generic initial content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        - memory.md#mem-obj-document-index
        note: The write and later consumer are wired, but the records describe generally source-passage-driven
          model content rather than fixing the original input of every write. Imported document content
          is not made a trace solely by delivery as a tool result. Full qualifying/nonqualifying coverage
          cannot be completed.
      - scope: Optional merge caller-supplied summary and opaque external compaction semantics
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-merge
        - runtime.md#rt-cmp-llmlingua2
        - epistemic.md#epi-rte-context-replacement
        note: Default concatenation is not an independent established trace-fed learning route; a configured
          caller or external producer may have unknown trace inputs. Do not promote generic capability
          to a wired automatic trace write.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its automatic trace-fed write and
          later consumer; no local witness resolves it. Fixed or unpinned provider weights alone are not
          classified as accumulated memory.
      records:
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - epistemic.md#epi-rte-answer-reward
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-document-index
      - memory.md#mem-rte-memory-merge
      - runtime.md#rt-cmp-llmlingua2
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      note: Qualifying compacted-history and policy-update routes establish yes without observed improvement.
        Finding-write input provenance, generic callers and opaque endpoint retention remain unresolved;
        no local or system-wide no is inferred from missing execution evidence.
    trace_source:
      assessment: partial
      units:
      - scope: History-derived retained summaries/spans/local compression fallback
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Recorded assistant conversational turns feed retained replacement context.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-obj-full-history
          - runtime.md#rt-rte-context-control
          - epistemic.md#epi-obj-context-replacements
          - epistemic.md#epi-rte-context-replacement
          note: Recorded tool-result messages feed retained replacement context.
        records:
        - runtime.md#rt-obj-full-history
        - runtime.md#rt-rte-context-control
        - epistemic.md#epi-obj-context-replacements
        - epistemic.md#epi-rte-context-replacement
        note: The input is accumulated assistant/tool history. Conversational turns and recorded tool
          output are distinct source parts, not an event stream merely because each has an ID.
      - scope: Training branch/rollout policy-update chain
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records:
          - runtime.md#rt-rte-branch-credit
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-module
          - runtime.md#rt-bap-rollout-weights
          - epistemic.md#epi-rte-answer-reward
          note: Linked generated states/actions/outcomes are scored and used for durable numerical policy
            adaptation.
        records:
        - runtime.md#rt-rte-branch-credit
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-cmp-actor-module
        - runtime.md#rt-bap-rollout-weights
        - epistemic.md#epi-rte-answer-reward
        note: The original experience is linked task state, management actions and terminal outcomes;
          references/judge scores evaluate that experience but do not establish a separate environmental
          event stream.
      - scope: Variable finding/note inputs and generic initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-simple-notes
        - memory.md#mem-rte-findings-write
        - memory.md#mem-rte-findings-delivery
        - memory.md#mem-obj-document-index
        note: It is not established which writes consume conversational experience, tool execution feedback,
          source-document content or arbitrary caller material. Dataset names and tool-result wrapping
          cannot establish original trace kind.
      - scope: Optional merge supplied summary and external compressor alternative
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-merge
        - runtime.md#rt-cmp-llmlingua2
        - epistemic.md#epi-rte-context-replacement
        note: The caller summary origin and external transformation inputs beyond the recorded selected
          history are not resolved. The local history source findings remain valid without classifying
          unknown provider-added material.
      - scope: Possible endpoint-side retained state behind policy, compressor, embedding, reranker and
          judge adapters
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-cmp-reranker-endpoint
        - runtime.md#rt-cmp-vllm-client
        - runtime.md#rt-cmp-judge-answer
        - runtime.md#rt-cmp-llmlingua2
        note: Provider internals and hidden retention were not inspected. The adapters do not establish
          whether this alternative retains through-use material, nor its original input of any qualifying
          trace-fed write; no local witness resolves it. Fixed or unpinned provider weights alone are
          not classified as accumulated memory.
      records:
      - runtime.md#rt-obj-full-history
      - runtime.md#rt-rte-context-control
      - epistemic.md#epi-obj-context-replacements
      - epistemic.md#epi-rte-context-replacement
      - runtime.md#rt-rte-branch-credit
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-module
      - runtime.md#rt-bap-rollout-weights
      - epistemic.md#epi-rte-answer-reward
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-simple-notes
      - memory.md#mem-rte-findings-write
      - memory.md#mem-rte-findings-delivery
      - memory.md#mem-obj-document-index
      - memory.md#mem-rte-memory-merge
      - runtime.md#rt-cmp-llmlingua2
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-cmp-reranker-endpoint
      - runtime.md#rt-cmp-vllm-client
      - runtime.md#rt-cmp-judge-answer
      note: Sources follow the original content of qualifying writes, not adapter names. Recorded conversation/tool
        activity and linked training experience are supported; unresolved finding inputs and endpoint
        state prevent complete enumeration.
---

# ContextPilot memory profile

## Comparison rationale

This profile classifies accepted records, not execution. Its positive bases are
wired routes or explicitly afforded alternatives. No observation, beneficial
learning or causal improvement is established. Coverage remains partial because
generic initialization, optional caller-controlled branches and endpoint-side
retention are unresolved; strong local witnesses do not resolve them.

The task stores are retained outside the rendered history, but remain in process
memory. Dictionary adjacency is not evidence of a separate graph database;
NumPy vectors are not evidence of a vector service. Checkpoints and exports add
file retention without establishing cross-session note reload. These distinctions
follow [MEM-OBJ-notes](memory.md#mem-obj-notes),
[MEM-OBJ-mem-edges](memory.md#mem-obj-mem-edges),
[MEM-OBJ-mem-embeddings](memory.md#mem-obj-mem-embeddings) and
[RT-RTE-policy-update](runtime.md#rt-rte-policy-update).

Read-back separates the requested anchor from automatically chosen neighbors.
All-summary injection is coarse; graph expansion selects by normalized feature
overlap and optional embeddings; replacement rendering uses actual message-ID
matches. A key on a pull alone supplies no push signal. See
[MEM-RTE-findings-delivery](memory.md#mem-rte-findings-delivery) and
[RT-RTE-context-control](runtime.md#rt-rte-context-control).

Compaction is qualifying trace learning when recorded history feeds an automatic
retained replacement and a later policy invocation receives it. Semantic
preservation is not required for that classification. The substring countercase
and random-word fallback limit faithfulness, not the existence of consolidation;
they do not establish synthesis as a curation operation. The external compressor
branch retains its semantic uncertainty. See
[EPI-RTE-context-replacement](epistemic.md#epi-rte-context-replacement).

Training has separate consumers: experience and reward influence parameter
updates; updated weights subsequently determine generation probabilities.
Learning authority at the updater and ranking authority at generation are not
interchangeable. Checkpoint recovery markers instead route resumption. The
trace-learning yes is a write-route finding, not the improved-capacity meaning
of learning. See [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit),
[RT-RTE-policy-update](runtime.md#rt-rte-policy-update) and
[RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights).

Reconciliation resolves the duplicate document-index and simple-note declarations
to [MEM-OBJ-document-index](memory.md#mem-obj-document-index) and
[MEM-OBJ-simple-notes](memory.md#mem-obj-simple-notes), and the duplicate merge
route to [MEM-RTE-memory-merge](memory.md#mem-rte-memory-merge). Only canonical
destinations are used for those referents. The valid combined structured-memory
container is not treated as a supersession of its content/access/vector parts;
context replacements remain parts of full history. The merge findings remain
afforded, not wired, despite implemented local mutation. No current unresolved
cross-report conflict changes a value.

Source-read log: none. This classification used only the supplied accepted
members and reconciliation; no source ambiguity was resolved by a new source
read. Missing facts are kept beside the units whose coverage they prevent.
