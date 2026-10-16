---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Self-Training-LLM memory profile: retained curriculum and answer artifacts, selection scores, learned checkpoints, evaluation caches and exposed topic-helper state."
run-id: "AAS-2026-10-15-self-training-llm-5b5ee621bde2-01"
source-identity: "https://github.com/wj210/Self-Training-LLM"
reviewed-boundary: "97839b29d0fd8bb474f5549fa3e9d6ca504732e0"
memory-comparison:
  version: 2
  scope: "Retained title/document cache; generated question, test, context-label and answer files (text, metadata and unresolved generation payload details); derived selection scores; persisted known subset and model responses; SFT/DPO parameter checkpoints including adapter/merge forms; judge outcome cache and aggregate reports; exposed WordNet, popularity, embedding, category and train/test topic caches. Includes unknown initialization/replacement provenance locally. Excludes shipped static prompts/examples/configuration as accumulated objects, transient current-run batches/tensors, compiled caches and external dataset/provider/trainer internals. Dependency opacity and unestablished later report consumption remain limits, not evidence of absence."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Retained document, curriculum, answer/score, evaluation and alternative topic-helper files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-test"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-answer-scores"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-responses"
                - "memory.md#mem-obj-judge-cache"
                - "memory.md#mem-obj-results"
                - "memory.md#mem-obj-topic-caches"
              note: "JSONL, pickle and appended text files persist these parts across invocations; dense-vector encoding does not make the pickle a vector database."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-test"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-answer-scores"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-responses"
            - "memory.md#mem-obj-judge-cache"
            - "memory.md#mem-obj-results"
            - "memory.md#mem-obj-topic-caches"
          note: "The accepted inventory identifies the local persistence substrate for every listed file part, including vectors and symbolic access keys."
        - scope: "Locally saved SFT/DPO parameters, optional adapters and merged checkpoints"
          assessment: "known"
          findings:
            - value: "model-weights"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-causal-model"
                - "runtime.md#rt-rte-model-training"
                - "runtime.md#rt-bap-checkpoint-consumption"
              note: "Saved parameters are the operative retained model state, subsequently resolved by a model loader or a separately configured server."
          records:
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-bap-checkpoint-consumption"
          note: "Checkpoint directories store weights. Transient GPU state is not a separate accumulated memory object; TGI identity uncertainty does not change this substrate classification."
      records:
        - "memory.md#mem-obj-topic-docu"
        - "memory.md#mem-obj-questions"
        - "memory.md#mem-obj-context-answer"
        - "memory.md#mem-obj-test"
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-answer-scores"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-responses"
        - "memory.md#mem-obj-judge-cache"
        - "memory.md#mem-obj-results"
        - "memory.md#mem-obj-topic-caches"
        - "runtime.md#rt-cmp-causal-model"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-bap-checkpoint-consumption"
      note: "Covers accumulated local artifacts and trained parameter products, including exposed helper caches. External pretrained/provider internals are dependencies, not retained state written by this workflow; static source and current-run tensors are excluded."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Text-bearing article, question, label, sampled-answer, response and report fields"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-test"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-responses"
                - "memory.md#mem-obj-results"
                - "memory.md#mem-obj-topic-caches"
              note: "Article assertions, questions, generated answers and report labels retain language content, separate from their keys and numerical fields."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-test"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-responses"
            - "memory.md#mem-obj-results"
            - "memory.md#mem-obj-topic-caches"
          note: "Classifies the explicitly described textual parts only, not complete serialized generation objects."
        - scope: "Title/category/instruction addressing, file field structure, selection scores, clusters, cache labels, aggregates and helper topic/count alignment"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-test"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-answer-scores"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-responses"
                - "memory.md#mem-obj-judge-cache"
                - "memory.md#mem-obj-results"
                - "memory.md#mem-obj-topic-caches"
              note: "Fixed consumers interpret exact keys, role fields, numeric scores, memberships, outcome categories and topic lists through localized rules."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-test"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-answer-scores"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-responses"
            - "memory.md#mem-obj-judge-cache"
            - "memory.md#mem-obj-results"
            - "memory.md#mem-obj-topic-caches"
          note: "Includes symbolic access structures and report numbers; natural-language payload and dense embeddings are separate units."
        - scope: "Saved causal-model parameters and retained WordNet/topic embedding arrays"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-causal-model"
                - "memory.md#mem-obj-topic-caches"
              note: "Model weights and dense topic/noun vectors are distributed numerical representations, not readable summaries of the source strings."
          records:
            - "runtime.md#rt-cmp-causal-model"
            - "memory.md#mem-obj-topic-caches"
          note: "Representation is established even where embedding-model initialization or vector/title alignment is unresolved."
        - scope: "Additional token/log-probability details in retained provider generation objects"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-answer-content"
            - "epistemic.md#epi-obj-raw-answer"
          note: "Records distinguish generated_text from the complete payload but do not establish all operative extra fields and their consumption. Text display cannot classify the full wrapper or prove its numerical details are parametric rather than symbolic."
      records:
        - "memory.md#mem-obj-topic-docu"
        - "memory.md#mem-obj-questions"
        - "memory.md#mem-obj-context-answer"
        - "memory.md#mem-obj-test"
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-responses"
        - "memory.md#mem-obj-results"
        - "memory.md#mem-obj-topic-caches"
        - "memory.md#mem-obj-answer-scores"
        - "memory.md#mem-obj-judge-cache"
        - "runtime.md#rt-cmp-causal-model"
        - "epistemic.md#epi-obj-raw-answer"
      note: "Positive classifications cover named text, symbolic and dense-numerical parts. Complete provider-output payload structure remains unresolved, so the inventory is not completely classified."
    lineage:
      assessment: "partial"
      units:
        - scope: "Wikipedia article text retained in the document cache and embedded document fields; WordNet lexical strings and imported popularity inputs"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-topic-caches"
                - "epistemic.md#epi-rte-document-transform"
              note: "External corpus, lexical and Wikimedia content enters the retained local artifacts; its truth and upstream derivation are not certified."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-topic-caches"
            - "epistemic.md#epi-rte-document-transform"
          note: "Imported content is classified at the acquisition edge, not as an endogenous experience trace."
        - scope: "New model-authored question, answer and response text at the recorded generation mechanisms"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-test"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-responses"
                - "runtime.md#rt-rte-data-generation"
              note: "Models propose the retained language content. Authorship here is not human approval and does not establish entailment from document context."
          records:
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-test"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-responses"
            - "runtime.md#rt-rte-data-generation"
          note: "Covers the implemented production paths, not authenticated provenance of arbitrary files reused at their paths."
        - scope: "Cleaned answer text and parsed judge labels extracted from recorded generation or judge returns"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-judge-cache"
                - "epistemic.md#epi-rte-answer-cleaning"
                - "runtime.md#rt-rte-pairwise-evaluation"
              note: "Cleanup extracts surviving answer text, and the judge parser derives retained outcome labels from returned choices."
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-judge-cache"
            - "epistemic.md#epi-rte-answer-cleaning"
            - "runtime.md#rt-rte-pairwise-evaluation"
          note: "Derived retained parts differ from complete raw outputs. Extraction alone is not factual acceptance or qualifying trace learning."
        - scope: "Derived score fields, known-subset structure, report aggregates, topic representations and trained parameter products"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-scores"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-results"
                - "memory.md#mem-obj-topic-caches"
                - "runtime.md#rt-cmp-causal-model"
                - "runtime.md#rt-rte-model-training"
              note: "Computations derive numerical/structural artifacts and optimize or merge weights; these products are not merely model-authored prose."
          records:
            - "memory.md#mem-obj-answer-scores"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-results"
            - "memory.md#mem-obj-topic-caches"
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-rte-model-training"
          note: "Classifies the recorded local derivation edges, not the opaque initial pretrained lineage."
        - scope: "Initial contents of preexisting reused files, supplied embedder provenance and inherited pretrained parameter content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-data-generation"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-topic-caches"
            - "runtime.md#rt-cmp-causal-model"
          note: "File existence does not authenticate an initial producer or edits; the WordNet embedder and upstream weight derivation are unresolved. Known subsequent transformations cannot supply these missing histories."
      records:
        - "memory.md#mem-obj-topic-docu"
        - "memory.md#mem-obj-topic-caches"
        - "epistemic.md#epi-rte-document-transform"
        - "memory.md#mem-obj-questions"
        - "memory.md#mem-obj-context-answer"
        - "memory.md#mem-obj-test"
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-responses"
        - "runtime.md#rt-rte-data-generation"
        - "memory.md#mem-obj-judge-cache"
        - "epistemic.md#epi-rte-answer-cleaning"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "memory.md#mem-obj-answer-scores"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-results"
        - "runtime.md#rt-cmp-causal-model"
        - "runtime.md#rt-rte-model-training"
      note: "All supported local derivation paths remain positive, but initial-file and inherited-parameter provenance prevent complete lineage coverage. Static examples contribute to generation without becoming accumulated-memory objects."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained document/question/answer text as context or comparison evidence at producer, answer-model, NLI and judge consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-test"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-responses"
                - "runtime.md#rt-rte-data-generation"
                - "runtime.md#rt-rte-response-generation"
                - "runtime.md#rt-rte-pairwise-evaluation"
              note: "Selected retained text supplies context, reference or comparison evidence. This names its operational role, not truth certification."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-test"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-responses"
            - "runtime.md#rt-rte-data-generation"
            - "runtime.md#rt-rte-response-generation"
            - "runtime.md#rt-rte-pairwise-evaluation"
          note: "Model-interpreted influence is distinguished from execution permission and from optimization authority."
        - scope: "Retained SFT labels, context-answer labels and DPO candidate answers admitted to optimization"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-context-answer"
                - "runtime.md#rt-rte-model-training"
                - "epistemic.md#epi-rte-preference-selection"
              note: "Stored label and preference text feeds parameter updates through SFT/DPO formatting; scores/documents need not survive as trainer metadata."
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-context-answer"
            - "runtime.md#rt-rte-model-training"
            - "epistemic.md#epi-rte-preference-selection"
          note: "Learning authority is at the update consumer. It does not claim better future capacity or factual acceptance."
        - scope: "Stored selection scores at question eligibility, pair admissibility and chosen/rejected priority consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-scores"
                - "runtime.md#rt-rte-model-training"
                - "epistemic.md#epi-rte-preference-selection"
              note: "Stored answer scores affect which candidates receive preferred/rejected positions and their relative selection."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-scores"
                - "runtime.md#rt-rte-model-training"
                - "epistemic.md#epi-rte-preference-selection"
              note: "Threshold comparisons use stored scores as criteria for admitting questions and training candidates."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-scores"
                - "runtime.md#rt-rte-model-training"
                - "epistemic.md#epi-rte-preference-selection"
              note: "On branches where thresholds are called, score-based exclusion prevents examples from reaching optimization; the nonpositive-threshold bypass remains outside that veto."
          records:
            - "memory.md#mem-obj-answer-scores"
            - "runtime.md#rt-rte-model-training"
            - "epistemic.md#epi-rte-preference-selection"
          note: "These are distinct effects of retained scores under fixed code, not a retained selection policy or independent truth oracle."
        - scope: "Retained identity fields and completed-context labels selecting subsequent producer/evaluation work"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-responses"
                - "memory.md#mem-obj-judge-cache"
                - "runtime.md#rt-rte-data-generation"
                - "runtime.md#rt-rte-pairwise-evaluation"
              note: "Exact title/instruction matches choose documents or matching answers, completed context-label questions leave the other label stream, and a cache hit selects reuse instead of a provider request."
          records:
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-responses"
            - "memory.md#mem-obj-judge-cache"
            - "runtime.md#rt-rte-data-generation"
            - "runtime.md#rt-rte-pairwise-evaluation"
          note: "Only consumed identity/state is classified; merely stored metadata has no inferred authority."
        - scope: "Retained popularity counts and embedding arrays at exposed topic-ranking helpers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-topic-caches"
              note: "View counts and query/topic-vector similarities prioritize topic identities in exposed helper code."
          records:
            - "memory.md#mem-obj-topic-caches"
          note: "This is a helper-level affordance, not active predefined-topic generation or observed semantic retrieval; unresolved FAISS and caller wiring remain limits."
        - scope: "Saved parameter product at downstream generation and cached outcomes at aggregate-report consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-bap-checkpoint-consumption"
            - "memory.md#mem-obj-judge-cache"
            - "memory.md#mem-obj-results"
            - "runtime.md#rt-rte-pairwise-evaluation"
          note: "Records establish numerical generation force and direct reuse of outcome categories, but do not establish a controlled authority label for those effects alone. Weights are not standing prose instructions; cached labels do not rank future answers or gate checkpoints."
        - scope: "Terminal report content at any later human decision consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-results"
          note: "Appending an operator-facing report does not establish an actual later reader, reliance decision or operational consequence; no authority value is inferred for that possible consumer."
      records:
        - "memory.md#mem-obj-topic-docu"
        - "memory.md#mem-obj-questions"
        - "memory.md#mem-obj-test"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-responses"
        - "runtime.md#rt-rte-data-generation"
        - "runtime.md#rt-rte-response-generation"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "memory.md#mem-obj-context-answer"
        - "runtime.md#rt-rte-model-training"
        - "epistemic.md#epi-rte-preference-selection"
        - "memory.md#mem-obj-answer-scores"
        - "memory.md#mem-obj-judge-cache"
        - "memory.md#mem-obj-topic-caches"
        - "runtime.md#rt-cmp-causal-model"
        - "runtime.md#rt-bap-checkpoint-consumption"
        - "memory.md#mem-obj-results"
      note: "Named retained inputs establish knowledge, learning, ranking, validation, enforcement and routing at their specific consumers. Neither generic numerical behavior nor a merely possible report reader justifies a blanket authority value; those included effects remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Implemented document admission, generated-data admission/rescoring, subset creation, optimization/save, response persistence and judge-cache admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-data-generation"
                - "runtime.md#rt-rte-model-training"
                - "runtime.md#rt-rte-response-generation"
                - "runtime.md#rt-rte-pairwise-evaluation"
                - "memory.md#mem-obj-topic-docu"
                - "memory.md#mem-obj-questions"
                - "memory.md#mem-obj-context-answer"
                - "memory.md#mem-obj-answer-scores"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-responses"
                - "memory.md#mem-obj-judge-cache"
                - "memory.md#mem-obj-results"
              note: "After launch, length/lexical/model/score/parser decisions admit contents without per-content human approval. Operators select modes and paths, not every admitted record."
          records:
            - "runtime.md#rt-rte-data-generation"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-rte-response-generation"
            - "runtime.md#rt-rte-pairwise-evaluation"
            - "memory.md#mem-obj-topic-docu"
            - "memory.md#mem-obj-questions"
            - "memory.md#mem-obj-context-answer"
            - "memory.md#mem-obj-answer-scores"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-responses"
            - "memory.md#mem-obj-judge-cache"
            - "memory.md#mem-obj-results"
          note: "Covers the software admission mechanisms rather than treating physical file I/O or workflow launch as the authority decision."
        - scope: "Exposed topic-helper cache construction and topic/split selection"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-topic-caches"
              note: "Software builds and saves helper representations/counts/lists without per-item human review."
          records:
            - "memory.md#mem-obj-topic-caches"
          note: "Admission is identifiable inside helpers despite absent active caller wiring."
        - scope: "Initial preexisting file supply/replacement, externally supplied WordNet embedder state and independently served checkpoint replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-data-generation"
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-topic-caches"
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-rte-response-generation"
          note: "Mutable files and an operator-configured endpoint can resolve other content, but the records do not establish how that content was admitted. Selecting a checkpoint to read is not evidence of manual checkpoint-content replacement."
      records:
        - "runtime.md#rt-rte-data-generation"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-rte-response-generation"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "memory.md#mem-obj-topic-docu"
        - "memory.md#mem-obj-questions"
        - "memory.md#mem-obj-context-answer"
        - "memory.md#mem-obj-answer-scores"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-responses"
        - "memory.md#mem-obj-judge-cache"
        - "memory.md#mem-obj-results"
        - "memory.md#mem-obj-topic-caches"
        - "memory.md#mem-obj-answer-content"
        - "runtime.md#rt-cmp-causal-model"
      note: "Known producer and helper mechanisms are automatic. Neither operator launch nor mutable-file capability establishes manual admission; unverified initialization and replacement keep coverage partial."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Reprocessing retained answer/score records and replacing their computed score fields"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-answer-scores"
                - "runtime.md#rt-rte-data-generation"
              note: "Reloaded retained answers are rescored and their score fields replaced before the answer artifact is overwritten."
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-answer-scores"
            - "runtime.md#rt-rte-data-generation"
          note: "This is revision of existing retained entries, not merely initial acquisition or a named maintenance command."
        - scope: "Reduction of retained answer records into known-subset records, and retained cached outcomes into report aggregates"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-known"
                - "memory.md#mem-obj-judge-cache"
                - "memory.md#mem-obj-results"
                - "runtime.md#rt-rte-pairwise-evaluation"
              note: "Known-subset persistence reduces retained answer records to selected instruction/document/category fields; reporting reduces retained outcome categories to numerical summaries of the same results."
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-known"
            - "memory.md#mem-obj-judge-cache"
            - "memory.md#mem-obj-results"
            - "runtime.md#rt-rte-pairwise-evaluation"
          note: "Classifies reduced representations of existing material, not new factual synthesis. Cleanup defects do not turn deletion into synthesis."
        - scope: "Parameter optimization/adapter merge, configured checkpoint retention and alternative helper maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-cmp-causal-model"
            - "memory.md#mem-obj-topic-caches"
          note: "Parameter changes and adapter cleanup are recorded, but their mapping to a controlled memory-curation operation is not established. Save limits are configuration, with external trainer semantics uninspected; acquisition-time duplicate checks alone do not establish curation of retained memory."
        - scope: "Opaque model contribution to generated or regenerated semantic content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-answer-content"
            - "epistemic.md#epi-obj-gold-answer"
            - "epistemic.md#epi-rte-score-evidence"
          note: "No concrete input/output interpretation establishes a new claim, semantic preservation or a further curation operation for opaque generated content. Do not infer synthesize from fluency or failed entailment proof."
      records:
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-answer-scores"
        - "runtime.md#rt-rte-data-generation"
        - "memory.md#mem-obj-known"
        - "memory.md#mem-obj-judge-cache"
        - "memory.md#mem-obj-results"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-cmp-causal-model"
        - "memory.md#mem-obj-topic-caches"
        - "epistemic.md#epi-obj-gold-answer"
        - "epistemic.md#epi-rte-score-evidence"
      note: "Inspected retained-data reductions and score revisions support consolidate and evolve. Other transformations and opaque semantic changes are not completely classifiable; no complete negative about dedup, decay, invalidate, promote or synthesize is asserted."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Later generation/training/inference/evaluation invocations requesting retained files and trained parameters"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-data-generation"
                - "runtime.md#rt-rte-model-training"
                - "runtime.md#rt-rte-response-generation"
                - "runtime.md#rt-rte-pairwise-evaluation"
                - "runtime.md#rt-bap-checkpoint-consumption"
              note: "Explicit stage requests lead to file/model selection, loading and delivery. Exact-match cache reuse fulfills the evaluation request rather than adding an unsolicited push."
          records:
            - "runtime.md#rt-rte-data-generation"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-rte-response-generation"
            - "runtime.md#rt-rte-pairwise-evaluation"
            - "runtime.md#rt-bap-checkpoint-consumption"
          note: "Includes stored documents/questions/labels/scores, known/test records, responses and judge labels, plus direct or operator-configured checkpoint consumption. Batch delivery is not a separate push operation."
        - scope: "Explicit topic-helper calls returning requested cached lexical/topic/count/vector material"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-topic-caches"
              note: "Helpers reload or select material in response to caller requests; similarity selection does not itself make delivery push."
          records:
            - "memory.md#mem-obj-topic-caches"
          note: "Helper-level requested access is established, while a deployed downstream workflow caller is not."
        - scope: "Terminal aggregate reports at a later consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-results"
          note: "No later automatic reader or actual human decision is recorded. Persistence alone does not establish a read-back route or its direction."
      records:
        - "runtime.md#rt-rte-data-generation"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-rte-response-generation"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "runtime.md#rt-bap-checkpoint-consumption"
        - "memory.md#mem-obj-topic-caches"
        - "memory.md#mem-obj-results"
      note: "All established read-back operations are request-driven. Terminal reports remain included retained objects without an established later consumer, so the broader inventory is partial rather than a system-wide pull-only assertion."
    read_back_signal:
      assessment: "not-determinable"
      units:
        - scope: "Established requested file/checkpoint/cache chains and explicit topic-helper returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-data-generation"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-rte-response-generation"
            - "runtime.md#rt-rte-pairwise-evaluation"
            - "runtime.md#rt-bap-checkpoint-consumption"
            - "memory.md#mem-obj-topic-caches"
          note: "These assessed direction units are pull operations. File identifiers, exact prompt matching, semantic helper queries and budgets within the requested chain do not establish a push selector."
        - scope: "Possible later consumption of terminal aggregate reports"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-results"
          note: "Direction and consumer are not established, so no trigger, selector input or selected retained part can be classified as a push signal. This unresolved branch cannot be declared pull-only or inapplicable."
      records:
        - "runtime.md#rt-rte-data-generation"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-rte-response-generation"
        - "runtime.md#rt-rte-pairwise-evaluation"
        - "runtime.md#rt-bap-checkpoint-consumption"
        - "memory.md#mem-obj-topic-caches"
        - "memory.md#mem-obj-results"
      note: "No supported positive push-signal value exists in the accepted inventory. The known pull units are locally inapplicable, but the unresolved report-consumer branch prevents an axis-wide inapplicable or absent assessment."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Retained generated question/answer experience and derived feedback feeding SFT/DPO parameters with later checkpoint consumption"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-answer-content"
                - "memory.md#mem-obj-answer-scores"
                - "runtime.md#rt-rte-model-training"
                - "runtime.md#rt-bap-checkpoint-consumption"
              note: "Automatic selection and optimization transform retained model-produced answers and scoring feedback into durable parameters that a later inference invocation can consume."
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-answer-scores"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-bap-checkpoint-consumption"
          note: "This qualifies as a wired trace-fed update, not mere retention and not demonstrated improvement. Imported documents and static examples are mixed inputs, not independently qualifying traces."
        - scope: "Additional opaque generation-payload fields and initially supplied/reused state at their possible update consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-topic-caches"
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-rte-data-generation"
          note: "Complete payload/provenance and external initialization are unresolved. No extra qualifying route or bounded local no can be inferred from that opacity; helper encoding alone is not proof of trace-fed learning."
      records:
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-answer-scores"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-bap-checkpoint-consumption"
        - "memory.md#mem-obj-topic-caches"
        - "runtime.md#rt-cmp-causal-model"
        - "runtime.md#rt-rte-data-generation"
      note: "A durable trace-fed parameter path is positively wired. Complete provenance and extra opaque payload roles remain unresolved, so this is not a complete enumeration or a blanket negative for every other stored part. Cache/report retention alone is not another qualifying learning route."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Original mixed inputs to the qualifying generated-data SFT/DPO parameter update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-answer-scores"
            - "runtime.md#rt-rte-model-training"
            - "runtime.md#rt-bap-checkpoint-consumption"
            - "epistemic.md#epi-obj-raw-answer"
            - "epistemic.md#epi-rte-score-evidence"
          note: "The accepted records name imported Wikipedia, static examples, generated questions/answers and NLI/provider-derived scores. They do not identify these retained datasets as conversational session logs, recorded tool requests/results, discrete runtime event streams or linked state-action-outcome trajectories. Model output is experience, but that alone does not determine one of the four controlled source categories."
        - scope: "Opaque initial/reused content and additional generation-object details potentially feeding updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-answer-content"
            - "memory.md#mem-obj-topic-caches"
            - "runtime.md#rt-cmp-causal-model"
            - "runtime.md#rt-rte-data-generation"
          note: "Neither source contents/origin nor a complete qualifying trace-fed write is established for these additional parts. Known trace learning elsewhere does not resolve their provenance."
      records:
        - "memory.md#mem-obj-answer-content"
        - "memory.md#mem-obj-answer-scores"
        - "runtime.md#rt-rte-model-training"
        - "runtime.md#rt-bap-checkpoint-consumption"
        - "epistemic.md#epi-obj-raw-answer"
        - "epistemic.md#epi-rte-score-evidence"
        - "memory.md#mem-obj-topic-caches"
        - "runtime.md#rt-cmp-causal-model"
        - "runtime.md#rt-rte-data-generation"
      note: "Trace learning is positively established, so trace_source is not inapplicable. No controlled origin can be established from the accepted records alone; do not relabel model-return datasets as tool-traces or trajectories without the missing origin/sequence evidence."
---

# Self-Training-LLM memory profile

## Comparison rationale

### Boundary, coverage and evidence

This profile classifies the accepted records, not an executed experiment. The retained inventory comes from [MEM-OBJ-topic-docu](memory.md#mem-obj-topic-docu), [MEM-OBJ-questions](memory.md#mem-obj-questions), [MEM-OBJ-context-answer](memory.md#mem-obj-context-answer), [MEM-OBJ-test](memory.md#mem-obj-test), [MEM-OBJ-answer-content](memory.md#mem-obj-answer-content), [MEM-OBJ-answer-scores](memory.md#mem-obj-answer-scores), [MEM-OBJ-known](memory.md#mem-obj-known), [MEM-OBJ-responses](memory.md#mem-obj-responses), [MEM-OBJ-judge-cache](memory.md#mem-obj-judge-cache), [MEM-OBJ-results](memory.md#mem-obj-results), [MEM-OBJ-topic-caches](memory.md#mem-obj-topic-caches) and [RT-CMP-causal-model](runtime.md#rt-cmp-causal-model). Shipped static directions are not accumulated memory. External provider weights and trainer internals are excluded dependencies, not inspected retained objects of this workflow.

Local lifecycle wiring supports wired findings without showing operation or benefit. Exposed topic helpers retain afforded findings because their active workflow caller and some dependencies are unresolved. The predefined-topic witness does not upgrade the helper alternatives. File storage is known even where file provenance or complete payload form is not. The provider wrapper is not equated with its readable answer text.

### Update force is not downstream instruction

[RT-RTE-model-training](runtime.md#rt-rte-model-training) and [EPI-RTE-preference-selection](epistemic.md#epi-rte-preference-selection) establish learning authority for retained examples at optimization. Stored scores separately rank and admit examples; a called threshold can enforce exclusion, but a nonpositive unknown threshold bypasses the filtered subset. The reference override covers the single pair and first multiple-preference pair, not subsequent gold-sample pairs. These bounds qualify selection authority rather than eliminating it.

[RT-BAP-checkpoint-consumption](runtime.md#rt-bap-checkpoint-consumption) establishes numerical generation force through later weights, not a standing prose instruction or a demonstrated gain in capacity. The controlled authority vocabulary does not automatically classify every numerical effect. DPO formatting drops document and score metadata; a downstream checkpoint is not a rationale-retrieval interface. An aggregate report's possible human reader likewise cannot be assigned authority without a recorded consumer.

### Local transformations and uncertain origins

[MEM-OBJ-answer-scores](memory.md#mem-obj-answer-scores) supports evolve for replacing scores on retained records. [MEM-OBJ-known](memory.md#mem-obj-known) and [MEM-OBJ-results](memory.md#mem-obj-results) support reduced representations of retained answer records and outcome categories, hence consolidate. They do not establish synthesize. [EPI-RTE-answer-cleaning](epistemic.md#epi-rte-answer-cleaning) establishes deletion at candidate processing, not by itself curation over already-retained memory. [EPI-OBJ-gold-answer](epistemic.md#epi-obj-gold-answer) retains indeterminate semantic relations of opaque generated content; failure to prove entailment is not proof of a new claim. Initial duplicate checks do not establish dedup over retained memory, and configured save limits do not by themselves establish an inspected decay implementation.

Authored model text, extracted cleaned text or judge labels, imported source content and compiled numerical products name different derivation edges. Known local transformations do not authenticate preexisting files or inherited parameters. The generation/training `_qf` path mismatch and alternate-generator exact-instruction remapping keep actual dataset continuity conditional; neither defeats the inspectable local update path.

### Requested access and qualifying trace-fed change

[RT-RTE-data-generation](runtime.md#rt-rte-data-generation), [RT-RTE-response-generation](runtime.md#rt-rte-response-generation) and [RT-RTE-pairwise-evaluation](runtime.md#rt-rte-pairwise-evaluation) describe requested loading and selection. Exact prompt-key cache reuse fulfills a comparison request. Similarity inside an explicitly requested helper return is also not unsolicited supply. These pull chains establish no push signal. Reports remain included retained artifacts without an established later consumer; that uncertainty prevents declaring the entire inventory pull-only or its signal axis inapplicable.

The generated-answer/feedback-to-parameters-to-later-inference chain supports trace_learning yes at wired basis. It does not establish observed learning benefit, session-log extraction, tool-trace learning, event-stream learning or trajectory learning. The accepted source account identifies model-produced datasets and derived scores, but lacks the original trace structure needed to choose one of those four source categories. Imported Wikipedia and static examples do not supply that missing origin. No negative trace-learning finding is invented for an opaque alternative.

### Reconciliation and source-read log

The supplied reconciliation establishes no supersessions. Container/part overlaps therefore remain canonical in their declaring members: this profile uses the memory inventory for retained file parts and runtime for stage/parameter routes, with epistemic records for local transformations and selection limits. It does not count overlapping containers as additional mechanisms or treat absent workflow declarations as missing operation evidence.

No target source files were read for this profile. All classifications and uncertainty limits derive from the supplied accepted records; no records, quotations or execution evidence were added.
