---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: KBLaM memory comparison of retained knowledge records, numerical representations, learned
  state and research-analysis artifacts, with opaque external alternatives retained.
run-id: AAS-2026-10-15-kblam-5a0c2fe96cc1-01
source-identity: https://github.com/microsoft/KBLaM
reviewed-boundary: 69683ad096e022b58854fd88c0c58968c7d8c470
memory-comparison:
  version: 2
  scope: Retained Entity/DataPoint content and structure; paired base key/value arrays; trained encoder/model/checkpoint
    and KB configuration state; exported answers, attention snapshots, reduced metrics and the separate
    reference/open-ended judgment parts; local authentication access metadata and unresolved SDK/provider
    retained-state alternatives. Includes their writes, maintenance and later-consumer chains, plus unresolved
    initial corpus/checkpoint/query-head histories. Excludes shipped static prompts/instructions as accumulated
    memory, ordinary current-generation KV state, ephemeral training prefix truncation, unshipped hosts
    and later revisions.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Retained Entity and DataPoint text/field records
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - memory.md#mem-obj-data-point
          note: JSONL/JSON persists records for later generator, encoder, training and evaluation loads.
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        note: Classifies retained disk objects, not their temporary Python dictionaries.
      - scope: Retained base key and value arrays
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          note: Paired .npy files retain dense vectors; numerical encoding does not establish a vector
            database.
        records:
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        note: Keys and values remain distinct parts even though both have the same file substrate.
      - scope: Trained encoder and Llama/Phi parameter checkpoints
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          note: State dictionaries and save_pretrained artifacts persist to disk.
        - value: model-weights
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          note: The retained operative payload is learned encoder/model parameter state, subsequently
            loaded as machinery.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Known local save representation; externally supplied checkpoint contents and history remain
          unavailable.
      - scope: Persisted KB configuration
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-kblam-config
          note: Training saves symbolic configuration as JSON for attempted resume.
        records:
        - memory.md#mem-obj-kblam-config
        note: Evaluation constructs its own configuration; exact reuse is not implied.
      - scope: Attention snapshots, reduced metrics and exported answer traces
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          note: NumPy, JSON/CSV and prediction text are retained experiment artifacts.
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        note: Current-call text KV caches are excluded; sweep snapshots have a bounded deletion horizon.
      - scope: Reference-answer judgment part
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-reference-judgment
          note: The returned dataclass list feeds main-block mean reporting.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-reference-judgment
          note: Main-block save appends JSONL after batch return.
        records:
        - memory.md#mem-obj-reference-judgment
        note: The list is an operative result at a later reporting function, not a claim of a subsequent
          saved-file reload.
      - scope: Open-ended judgment part
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: The accumulating list can reach reporting on the caught-exception prefix-return branch.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Each admitted judgment is appended before normal batch completion.
        records:
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Normal completion returns None, so completed mean reporting is not established.
      - scope: Local authentication record
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-cmp-gpt-session
          note: The client serializes auth_record.json and configures a persistent SDK credential cache.
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Local access metadata is included separately from semantic KB content; cache internals are
          not established.
      - scope: SDK credential-cache internal storage
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: The client requests persistence but the SDK implementation and physical cache representation
          were not inspected.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no storage substrate classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-kblam-config
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Files, parameter state and operative judgment lists are supported locally. Provider retention
        and SDK cache internals prevent complete substrate coverage; dense .npy encoding alone is not
        vector storage.
    representational_form:
      assessment: partial
      units:
      - scope: Entity and DataPoint semantic text at QA, encoding, ICL and supervision consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - memory.md#mem-obj-data-point
          note: Names, properties, questions, answers and literal ICL context require semantic interpretation.
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        note: The text path is separate from field/index control and dense encoding.
      - scope: Entity/DataPoint field structure and positional joins
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - memory.md#mem-obj-data-point
          note: Field extraction, templates, row indexing and paired-array joins use fixed code rules.
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        note: Symbolic structure supplies no independent semantic warrant.
      - scope: Base key vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          note: Dense key representations feed learned projection and numerical matching.
        records:
        - memory.md#mem-obj-embd-key
        note: A readable companion row does not replace the numerical payload.
      - scope: Base value vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-embd-value
          note: Dense description representations feed value projection and aggregation.
        records:
        - memory.md#mem-obj-embd-value
        note: Values have a different consumer role from keys.
      - scope: Retained encoder/model weights
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          note: Distributed learned parameters determine projection and generation computation.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Does not individuate propositions or authenticate external checkpoint history.
      - scope: KB configuration and local authentication fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-kblam-config
          - runtime.md#rt-cmp-gpt-session
          note: Configuration branches and credential deserialization/access use fixed consumer rules.
        records:
        - memory.md#mem-obj-kblam-config
        - runtime.md#rt-cmp-gpt-session
        note: Provider payloads and SDK cache internals are assessed separately.
      - scope: Attention snapshots and reduced accuracy data
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          note: Indexed numerical scores, positional labels and aggregate reports have fixed metric/converter
            rules.
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: Numerical arrays are not automatically distributed-parametric; these are measured indexed
          outputs, not learned knowledge vectors.
      - scope: Exported model-answer trace
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          note: Scorers interpret decoded candidate answers and references.
        records:
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        note: Token IDs are an intermediate, not the retained semantic answer part.
      - scope: Reference judgment text and reference
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-reference-judgment
          note: Candidate and supplied reference are semantic comparison content.
        records:
        - memory.md#mem-obj-reference-judgment
        note: No provider rationale is retained in this part.
      - scope: Reference judgment score/structure
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-reference-judgment
          note: Numeric score feeds fixed mean/reporting and JSON serialization.
        records:
        - memory.md#mem-obj-reference-judgment
        note: Numeric parse is not a range or truth check.
      - scope: Open-ended evidence/question/response/reason
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Evidence and parsed explanatory assessment are natural-language content.
        records:
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Retained reason is provider prose, not hidden reasoning or independently checked evidence.
      - scope: Open-ended judgment score/structure
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Float score and fields feed serialization and conditional prefix reporting.
        records:
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Normal aggregate reporting remains defective.
      - scope: SDK credential-cache internal payload
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Only persistence options are inspected; internal encoding is not established.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no representational form classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-kblam-config
      - runtime.md#rt-cmp-gpt-session
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      note: Mixed records are split by semantic text, fixed-rule fields/scores and distributed vectors/weights.
        Opaque retained alternatives prevent a complete form inventory.
    lineage:
      assessment: partial
      units:
      - scope: New provider-written Entity content admitted by the shipped generator
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - runtime.md#rt-rte-dataset-production
          note: GPT proposes synthetic entity prose, which code parses and appends.
        records:
        - memory.md#mem-obj-entity
        - runtime.md#rt-rte-dataset-production
        note: Known authoring path, not authenticated history for supplied corpora.
      - scope: Loaded corpus instances and upstream Enron extraction
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          note: Downstream drivers acquire supplied rows rather than establishing their source truth.
        records:
        - memory.md#mem-obj-data-point
        note: Acquisition is wired; the upstream Enron extraction account is separately only attributed
          doctrine.
      - scope: Enron upstream extraction provenance as described in the dataset card
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records:
          - memory.md#mem-obj-data-point
          note: The card attributes automated extraction/entity linking upstream of imported rows.
        records:
        - memory.md#mem-obj-data-point
        note: Claimed provenance is not an inspected implementation or authenticated row history.
      - scope: Template-derived QA/key strings
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - epistemic.md#epi-rte-template-qa
          note: Code copies properties into formatted questions, answers and key strings.
        records:
        - memory.md#mem-obj-data-point
        - epistemic.md#epi-rte-template-qa
        note: Formatting does not establish new source warrant.
      - scope: Perturbed questions and extended QA
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - epistemic.md#epi-rte-augment-qa
          note: Provider-generated strings overwrite Q or add extension fields.
        records:
        - memory.md#mem-obj-data-point
        - epistemic.md#epi-rte-augment-qa
        note: Known model authoring route does not determine whether actual extended claims are new or
          faithful; CLI and guidance-delivery defects remain.
      - scope: Base key/value vectors
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          note: Embedding generation compiles key/description text into numerical arrays.
        records:
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        note: The transform is wired, but historical input alignment and provider/model revision remain
          unresolved.
      - scope: Locally trained parameter state and saved configuration
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          - memory.md#mem-obj-kblam-config
          note: Optimizer updates and configured serialization produce durable numerical machinery and
            configuration.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - memory.md#mem-obj-kblam-config
        note: Known local derivation does not establish the initialization history of an externally selected
          checkpoint.
      - scope: Historical supplied corpora, external checkpoints and alternative query-head state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Generating calls, human curation, exact initial weights and the alternative query-head producer
          are not established by a load path.
      - scope: Answer traces
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          note: The local model generates decoded candidate answers which may be exported.
        records:
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        note: No entailment or factual acceptance is inferred from generation.
      - scope: Attention snapshots
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          note: Snapshots record selected attention activity for later metric analysis.
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: They are incomplete activity records, not full conversational or tool traces.
      - scope: Reduced attention metrics
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          note: Metric reports derive from recorded attention snapshots under positional labels.
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: This is retained analysis of runtime activity, not automatically trace learning.
      - scope: Reference judgment derived record
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-reference-judgment
          note: Exported answer/reference traces feed provider scoring and a parsed scalar result.
        records:
        - memory.md#mem-obj-reference-judgment
        note: Reference content is dataset-derived; opaque scoring does not independently authenticate
          it.
      - scope: Open-ended judgment derived record
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Exported evidence/question/response traces feed the retained parsed score/reason.
        records:
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Reason authorship does not establish factual acceptance or a behavior-shaping later reader.
      - scope: Initial authentication record/cache lineage
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Software serializes authentication results, but the records do not establish a controlled
          semantic derivation category for the credentials or opaque SDK cache.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no lineage classification of that alternative
          follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - runtime.md#rt-rte-dataset-production
      - memory.md#mem-obj-data-point
      - epistemic.md#epi-rte-template-qa
      - epistemic.md#epi-rte-augment-qa
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-kblam-config
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Known authored, imported, compiled and trace-derived paths coexist with missing historical
        provenance. A known embedding/save path cannot authenticate the initial corpus or checkpoint.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained Entity properties at QA construction
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-entity
          note: Properties supply semantic content to the later template/augmentation consumer.
        records:
        - memory.md#mem-obj-entity
        note: Input reliance is not a factual endorsement.
      - scope: DataPoint knowledge at ICL and numerical inference
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - runtime.md#rt-bap-knowledge-attention
          note: Descriptions supply answer context as literal prose or encoded values.
        records:
        - memory.md#mem-obj-data-point
        - runtime.md#rt-bap-knowledge-attention
        note: No standing-instruction priority or truth guarantee is established.
      - scope: Retained key text/base key vectors at matching consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - memory.md#mem-obj-embd-key
          - runtime.md#rt-rte-kb-attention
          note: Retained keys determine query/key scores and optional top-k row priority.
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - runtime.md#rt-rte-kb-attention
        note: Fixed attention code still uses retained features as ranking inputs; pruning alignment is
          qualified.
      - scope: Retained base value vectors at aggregation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-bap-knowledge-attention
          note: Projected values supply numerical external-knowledge context to generation.
        records:
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-bap-knowledge-attention
        note: Numerical influence is wired, specific answer dependence is unobserved.
      - scope: Retained QA targets at supervised optimizer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - runtime.md#rt-rte-adapter-training
          note: Dataset answers and extended answers determine loss feeding durable parameter updates.
        records:
        - memory.md#mem-obj-data-point
        - runtime.md#rt-rte-adapter-training
        note: Learning authority does not itself establish a trace-origin learning route or realized improvement.
      - scope: References and row labels at answer/attention evaluators
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          - runtime.md#rt-rte-evaluation-modes
          note: Expected references/indices define the criteria for reference agreement and positional
            correctness.
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - runtime.md#rt-rte-evaluation-modes
        note: Bounded assessment criteria, not an answer-release veto or independent truth oracle.
      - scope: Trained encoder and learned query-head parameters at projection/matching
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          - runtime.md#rt-rte-kb-attention
          note: Loaded key projections and optional trained query heads shape numerical match scores.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - runtime.md#rt-rte-kb-attention
        note: This describes the scoring consumer, not arbitrary external weights or successful checkpoint
          reload.
      - scope: Other retained model/value-projection parameter effects at token computation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - runtime.md#rt-bap-checkpoint-consumption
        note: The records establish behavior-determining machinery, but do not individuate which controlled
          knowledge/instruction/other force covers all externally loaded numerical content.
      - scope: Retained KB configuration at attention/resume
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-kblam-config
          note: Layer frequency and mode/budget fields select attention branches and admitted input windows.
        records:
        - memory.md#mem-obj-kblam-config
        note: Only actual config consumers are classified; evaluation may construct a different config.
      - scope: Exported answers and reference/open-ended evidence at scorer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          - memory.md#mem-obj-reference-judgment
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Candidate/reference/evidence prose supplies the context to the judgment consumer.
        records:
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Scorer inputs are not automatically accepted propositions.
      - scope: Judgment score/reason and reduced metric outputs at reporting
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: Reporting/mean/conversion force is established, but no controlled authority value follows
          solely from being a report. Saved reasons have no inspected later inference consumer.
      - scope: Local retained authentication data at service access
        assessment: partial
        findings:
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-cmp-gpt-session
          note: Reused authentication data supplies the service-access credential, not answer advice.
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Wiring of access is established; actual grants, expiry and external enforcement contracts
          are not inspected.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no behavioral authority classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - runtime.md#rt-bap-knowledge-attention
      - memory.md#mem-obj-embd-key
      - runtime.md#rt-rte-kb-attention
      - memory.md#mem-obj-embd-value
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - runtime.md#rt-rte-evaluation-modes
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-bap-checkpoint-consumption
      - memory.md#mem-obj-kblam-config
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Knowledge, ranking, learning, validation, routing and access enforcement apply to the named
        consumers only. Parameter machinery and reporting are not assigned blanket authority; no judgment-to-successor
        selection is established.
    write_agency:
      assessment: partial
      units:
      - scope: Entity parsing/append admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - runtime.md#rt-rte-dataset-production
          note: Software admits structurally constructible provider content without per-record human approval.
        records:
        - memory.md#mem-obj-entity
        - runtime.md#rt-rte-dataset-production
        note: Launching the script is not manual content approval.
      - scope: Template, perturbation and extension field admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - epistemic.md#epi-rte-template-qa
          - epistemic.md#epi-rte-augment-qa
          note: Code formats or assigns returned fields and saves them without a semantic human veto.
        records:
        - memory.md#mem-obj-data-point
        - epistemic.md#epi-rte-template-qa
        - epistemic.md#epi-rte-augment-qa
        note: The ordinary generator CLI defect limits reachability, not the implemented admission mechanism.
      - scope: Embedding and paired-split admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-rte-dataset-production
          note: Scripts transform loaded inputs and write arrays/partitions without per-row approval.
        records:
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-rte-dataset-production
        note: No multi-file atomicity or human curation follows from configured paths.
      - scope: Optimizer updates, periodic checkpoint and config saves
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          - memory.md#mem-obj-kblam-config
          note: Configured optimizer steps and periodic saves admit current state without validation improvement
            or per-update human approval.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - memory.md#mem-obj-kblam-config
        note: Explicit checkpoint loading is not a separate evidenced manual write.
      - scope: Answer/attention/metric and judgment persistence
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          - memory.md#mem-obj-reference-judgment
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Code writes generated outputs, metrics and parseable judgments; no per-result approval
            is wired.
        records:
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Reference post-batch saving and open-ended per-record saving retain their distinct failure
          limits.
      - scope: Authentication serialization and sweep cleanup
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-cmp-gpt-session
          - memory.md#mem-rte-result-cleanup
          note: Client writes authenticated state; sweep code removes/recreates configured directories
            without a per-content decision.
        records:
        - runtime.md#rt-cmp-gpt-session
        - memory.md#mem-rte-result-cleanup
        note: User authentication is not approval of generated KB content.
      - scope: Initial corpus/checkpoint and alternative query-head admission or replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Generic caller path selection and possible file editing do not identify an explicit human
          per-content decision. Manual editing is a capacity, not demonstrated admission control.
      - scope: Manually runnable notebook scratch deletion
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: The records identify an operator-run shell cleanup cell but do not establish a per-content
          retention decision; launching code alone cannot classify manual admission.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no write agency classification of that
          alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - runtime.md#rt-rte-dataset-production
      - memory.md#mem-obj-data-point
      - epistemic.md#epi-rte-template-qa
      - epistemic.md#epi-rte-augment-qa
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-kblam-config
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Automatic local admission is supported. No manual finding is inferred merely from operator
        launch, path configuration, replaceability or checkpoint selection; unresolved initial/external
        writes remain included.
    curation_operations:
      assessment: partial
      units:
      - scope: Retained DataPoint Q replacement by perturbation
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - epistemic.md#epi-rte-augment-qa
          note: The model-written Q replaces the existing Q field while other knowledge/answer fields
            remain.
        records:
        - memory.md#mem-obj-data-point
        - epistemic.md#epi-rte-augment-qa
        note: This is entry revision; it neither guarantees name-only change nor checks factual faithfulness.
      - scope: QA extension semantic transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - epistemic.md#epi-rte-augment-qa
        note: Adding extended fields is wired, but actual outputs are absent and the relation is indeterminate.
          A request to extend cannot establish synthesis or faithful consolidation.
      - scope: Entity-to-QA formatting, embedding generation and paired splits
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - epistemic.md#epi-rte-template-qa
        note: Template expansion, encoding and index slicing establish derivation/acquisition, not one
          of the controlled retained-content curation transformations.
      - scope: Evolution of retained trained numerical state
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          note: Optimizer steps revise existing encoder and optionally query-head parameter entries; periodic
            saves retain the revised state.
        records:
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Numerical-state revision is not synthesis of a warranted proposition; external checkpoint
          history remains unresolved.
      - scope: Accuracy-sweep raw-result removal
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          note: Code forgets raw retained attention snapshots by removing the directory after metric derivation.
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        note: Classifies forgetting, not semantic invalidation with retained history. Raw evidence can
          disappear before final summary writing.
      - scope: Attention metric derivation and reference/open-ended judgment production
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: Metrics and opaque rubric judgments are new analysis outputs. The records do not establish
          a reduced representation of the same claims, duplicate merging, promotion or checked synthesis
          of a new claim.
      - scope: Initial/external corpus and checkpoint maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Historical maintenance procedures are not authenticated; no absence or positive curation
          operation follows from a loader.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no curation operation classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-data-point
      - epistemic.md#epi-rte-augment-qa
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - epistemic.md#epi-rte-template-qa
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Entry/parameter revision and raw-evidence forgetting are supported. Reformatting/index rebuilding
        alone is not consolidation; opaque extension/scoring does not establish synthesis. No complete
        negative for other operations is justified.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit file/checkpoint loads, generator reload and scorer/converter requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-entity
          - memory.md#mem-obj-data-point
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - memory.md#mem-obj-encoder
          - runtime.md#rt-cmp-llama3-model
          - runtime.md#rt-cmp-phi3-model
          - runtime.md#rt-rte-adapter-training
          - memory.md#mem-obj-kblam-config
          - epistemic.md#epi-obj-model-output
          - memory.md#mem-obj-eval-example
          - memory.md#mem-obj-attention-weights
          - memory.md#mem-rte-result-cleanup
          - memory.md#mem-obj-reference-judgment
          - memory.md#mem-obj-open-judgment
          - epistemic.md#epi-rte-open-judgment
          note: Later functions request retained paths or inputs and code fulfills those requests; the
            return is not an extra push.
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - memory.md#mem-obj-kblam-config
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        note: 'Conditional implemented branches only: unchanged evaluator entry, resume and scorer defects
          prevent claiming successful execution.'
      - scope: Driver-selected KB and supervision supplied to model/optimizer
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-rte-accuracy-generation
          - runtime.md#rt-rte-adapter-training
          - runtime.md#rt-rte-evaluation-modes
          note: On an experiment step the driver automatically selects rows and supplies context/targets
            without the model or optimizer requesting particular retained records.
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-rte-accuracy-generation
        - runtime.md#rt-rte-adapter-training
        - runtime.md#rt-rte-evaluation-modes
        note: Upstream operator configuration supplies budgets and paths; requested disk load and subsequent
          unsolicited model-context supply are different operations.
      - scope: Llama optional query-conditioned top-k delivery within attention
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-rte-kb-attention
          note: At configured layers the automatic selector supplies the top-ranked retained key/value
            parts to attention.
        records:
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-rte-kb-attention
        note: Phi has no corresponding inspected pruning branch; Llama score/value alignment is qualified.
      - scope: Authentication record reuse by initialized client
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-cmp-gpt-session
          note: Client initialization requests the existing record/cache for subsequent authentication.
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention is separate from local requested reuse.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no read-back direction classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-kblam-config
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-rte-accuracy-generation
      - runtime.md#rt-rte-evaluation-modes
      - runtime.md#rt-rte-kb-attention
      - runtime.md#rt-cmp-gpt-session
      note: Request-driven loading coexists with automatic row delivery and optional internal pruning.
        Current-generation cache continuation is excluded. Unknown provider routes prevent a complete
        direction inventory.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic driver context/supervision selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-data-point
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-rte-accuracy-generation
          - runtime.md#rt-rte-adapter-training
          - runtime.md#rt-rte-evaluation-modes
          note: 'Trigger: experiment step. Inputs: configured KB size, first-N boundaries, random indices
            and mode. Selected parts: corresponding record text, QA targets or cached key/value rows.'
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-rte-accuracy-generation
        - runtime.md#rt-rte-adapter-training
        - runtime.md#rt-rte-evaluation-modes
        note: Array indexing implements a coarse/random selection decision, not a semantic identity match;
          requested filenames alone add no identifier push.
      - scope: Llama optional sparsification
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-obj-embd-key
          - memory.md#mem-obj-embd-value
          - runtime.md#rt-rte-kb-attention
          note: 'Trigger: configured attention layer. Selector inputs: current query states and retained
            key vectors. Selected parts: top-k keys and paired values by summed dot-product scores.'
        records:
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - runtime.md#rt-rte-kb-attention
        note: Top-k is inference-time selection, not durable deletion; its score-return slicing limits
          correctness, not the existence of numerical selection.
      - scope: Explicit reload/scorer/converter/authentication request operations
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        - runtime.md#rt-cmp-gpt-session
        note: These operations fulfill requests rather than supply unsolicited selected context, so a
          push-selection signal is inapplicable locally.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no push-selection signal classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - runtime.md#rt-rte-accuracy-generation
      - runtime.md#rt-rte-adapter-training
      - runtime.md#rt-rte-evaluation-modes
      - runtime.md#rt-rte-kb-attention
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-cmp-gpt-session
      note: Both coarse driver selection and inferred-embedding Llama selection are supported. Pull-only
        operations need no signal, but they cannot make the opaque provider alternative inapplicable.
    trace_learning:
      assessment: uninspected
      units:
      - scope: Inspected synthetic/imported dataset-to-embedding/parameter routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - runtime.md#rt-rte-dataset-production
        note: The described local update uses supplied/generated Entity/QA content and expected tokens,
          not an established trace source. Computing token errors alone does not establish recorded activity
          input. The accepted set declares no bounded-absence record to license a controlled no, and external
          input histories remain unresolved.
      - scope: Inspected answer/attention-to-metric/judgment reporting routes
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        - runtime.md#rt-rte-evaluation-modes
        note: Activity records produce retained analysis, but no recorded downstream path makes scores/reasons
          durable answering behavior or admits successor checkpoints. This does not establish yes; without
          a canonical bounded-absence record it also does not license a controlled no.
      - scope: Initial imported corpora, external weights and alternative query-head histories
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: The original inputs to externally supplied artifacts are not authenticated. A known local
          non-trace route cannot exclude trace-fed upstream production.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no trace learning classification of
          that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - runtime.md#rt-rte-dataset-production
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-rte-evaluation-modes
      - runtime.md#rt-cmp-gpt-session
      note: No controlled trace-learning value is established. Local recorded routes do not establish
        qualifying trace-fed behavior-shaping writes, but the set contains no bounded-absence declarations
        licensing no. External/provider routes remain uninspected; ordinary supervised adaptation is not
        denied.
    trace_source:
      assessment: uninspected
      units:
      - scope: Inspected synthetic/supervised and analysis-only local routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-embd-key
        - memory.md#mem-obj-embd-value
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        - memory.md#mem-obj-attention-weights
        - memory.md#mem-rte-result-cleanup
        - epistemic.md#epi-obj-model-output
        - memory.md#mem-obj-eval-example
        - memory.md#mem-obj-reference-judgment
        - memory.md#mem-obj-open-judgment
        - epistemic.md#epi-rte-open-judgment
        - runtime.md#rt-rte-dataset-production
        - runtime.md#rt-rte-evaluation-modes
        note: The assessed local routes establish neither a qualifying automatic trace-fed write nor a
          canonical bounded-absence warrant for all such writes. No original input can be assigned to
          a qualifying route, and local inapplicability is not established.
      - scope: Original training inputs to imported/external corpus, checkpoint and query-head alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-data-point
        - memory.md#mem-obj-encoder
        - runtime.md#rt-cmp-llama3-model
        - runtime.md#rt-cmp-phi3-model
        - runtime.md#rt-rte-adapter-training
        note: Original input histories are unavailable; no source value can be selected and system-wide
          inapplicability is prevented.
      - scope: Included provider-side retained state behind chat/embedding endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-gpt-session
        note: Provider retention and internals were not inspected; no qualifying trace source classification
          of that alternative follows from local client behavior.
      records:
      - memory.md#mem-obj-entity
      - memory.md#mem-obj-data-point
      - memory.md#mem-obj-embd-key
      - memory.md#mem-obj-embd-value
      - memory.md#mem-obj-encoder
      - runtime.md#rt-cmp-llama3-model
      - runtime.md#rt-cmp-phi3-model
      - runtime.md#rt-rte-adapter-training
      - memory.md#mem-obj-attention-weights
      - memory.md#mem-rte-result-cleanup
      - epistemic.md#epi-obj-model-output
      - memory.md#mem-obj-eval-example
      - memory.md#mem-obj-reference-judgment
      - memory.md#mem-obj-open-judgment
      - epistemic.md#epi-rte-open-judgment
      - runtime.md#rt-rte-dataset-production
      - runtime.md#rt-rte-evaluation-modes
      - runtime.md#rt-cmp-gpt-session
      note: No positive source classification or bounded complete inapplicability is established. The
        local route records do not identify a qualifying original trace input; external/provider original
        inputs remain uninspected, not absent.
---

# KBLaM memory profile

## Comparison rationale

This profile classifies accepted records, not new source observations. The
inventory separates semantic knowledge from its index/field structure, dense
base representations, learned machinery and retained experiment evidence.
A dense array is a file-backed representation, not evidence of a vector
store. Model weights are separately retained parameter state, not prose
instructions. See [MEM-OBJ-embd-key](memory.md#mem-obj-embd-key),
[MEM-OBJ-embd-value](memory.md#mem-obj-embd-value) and
[MEM-OBJ-encoder](memory.md#mem-obj-encoder).

Coverage and strength are independent. Wired local transformations survive
missing historical provenance and unobserved operation, but they cannot resolve
opaque initialization or provider retention. The unchanged evaluator import
failure, generator typo, processor compatibility issues, resume layout mismatch
and scorer defects remain limits on reachability and completed operation.
No finding claims an observed activation or causal benefit. See
[RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation),
[RT-RTE-dataset-production](runtime.md#rt-rte-dataset-production),
[RT-RTE-direct-inference](runtime.md#rt-rte-direct-inference),
[RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training) and
[MEM-OBJ-open-judgment](memory.md#mem-obj-open-judgment).

Requested loading and subsequent automatic context selection are different
operations. Paths and row indices do not by themselves establish identifier
push. Random/subset driver selection is coarse; the optional Llama top-k
selector uses current queries and retained numerical keys. The score-slicing
qualification prevents treating that pruning as a proven equivalent
optimization. See [RT-RTE-kb-attention](runtime.md#rt-rte-kb-attention) and
[RT-RTE-accuracy-generation](runtime.md#rt-rte-accuracy-generation).

Learning authority belongs to QA targets at the optimizer. It does not imply
trace learning: the recorded local supervision is supplied/generated content,
not an established recorded-experience source. The accepted set declares no
bounded-absence records, so neither a controlled trace-learning no nor
trace-source inapplicability is asserted. Conversely answer traces and attention snapshots do
feed retained analysis, but the recorded downstream consumers do not turn
those analyses into durable answering behavior. The two judgment parts remain
separate: scalar reference agreement has post-batch saving and reporting;
open-ended assessment retains a reason per record but lacks a normal list
return and a shipped reason-to-inference reader. See
[RT-RTE-adapter-training](runtime.md#rt-rte-adapter-training),
[MEM-OBJ-attention-weights](memory.md#mem-obj-attention-weights),
[MEM-OBJ-reference-judgment](memory.md#mem-obj-reference-judgment) and
[MEM-OBJ-open-judgment](memory.md#mem-obj-open-judgment).

Reconciliation supersedes the epistemic Entity, reference-judgment and
open-judgment declarations by the corresponding memory declarations; those
canonical destinations are used here. DataPoint and judgment containers remain
valid alongside their parts; no container supersession is inferred. The
remaining extension-guidance qualification does not license a wired
QA-only constraint: the mapping relies on field mutation/admission, not
provider compliance. Extension semantics remain indeterminate, so no synthesis
finding is inferred. See [MEM-OBJ-entity](memory.md#mem-obj-entity),
[MEM-OBJ-reference-judgment](memory.md#mem-obj-reference-judgment),
[MEM-OBJ-open-judgment](memory.md#mem-obj-open-judgment) and
[EPI-RTE-augment-qa](epistemic.md#epi-rte-augment-qa).

Source-read log: none. All classifications and limits use supplied records
and their annotations; no target source was reread and no records or evidence
were added.
