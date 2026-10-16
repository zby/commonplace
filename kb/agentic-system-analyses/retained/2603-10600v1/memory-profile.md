---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Memory profile of trajectory-informed memory generation: declared retained tips, access representations, semantic maintenance and later-task prompt supply."
run-id: AAS-2026-10-14-2603-10600v1-a956324c9a82-01
source-identity: https://arxiv.org/html/2603.10600v1
reviewed-boundary: "arxiv-2603.10600v1-html-captured-2026-10-14"
memory-comparison:
  version: 2
  scope: >-
    Documented cross-task memory: generated and consolidated strategy, recovery and
    optimization tips; original task, generated subtask and canonical descriptions;
    stored embeddings; structured tip metadata; extraction/admission, consolidation
    and both pre-task retrieval routes. Completed trajectories supply the trace-fed
    write, but durable raw-input retention and intake control remain unresolved.
    Extraction intermediates and transient query vectors have no established later
    invocation consumer. Static prompts, provider model weights, external API state
    and benchmark machinery are not accumulated memory within this profile; no
    parameter-update route is established. Physical persistence, initialization,
    maintenance implementation and actual activation remain unverified.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Stored tip and description embeddings"
          assessment: known
          findings:
            - value: vector
              basis: claimed
              records: [memory.md#mem-obj-embeddings]
              note: "The declared memory vectors enter vector storage; this is not an inspected database."
          records: [memory.md#mem-obj-embeddings]
          note: "Covers stored content/purpose and description vectors, not transient query vectors or provider parameters."
        - scope: "Tip text, description text and structured metadata storage"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata]
          note: "Memory-system storage and structured attributes are described, but no controlled substrate is identified for these parts. Encoding does not establish files, a relational database or a key-value store."
        - scope: "Possible durably retained raw trajectories"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trajectories]
          note: "Neither durable raw retention nor its substrate is specified; no raw-log storage value follows from its use as extraction input."
      records: [memory.md#mem-obj-embeddings, memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata, memory.md#mem-obj-trajectories]
      note: "The retained product/access inventory is documented, but only vector storage has a controlled positive; other physical substrates and possible raw retention remain unresolved."
    representational_form:
      assessment: known
      units:
        - scope: "Guidance text and description text at model/semantic consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-tips, memory.md#mem-obj-descriptions]
              note: "Advice, purposes, steps, triggers and descriptions are interpreted as language, including API names used as advice."
          records: [memory.md#mem-obj-tips, memory.md#mem-obj-descriptions]
          note: "Covers task/subtask and generic/domain advice and original/generated/canonical description text, not their vectors."
        - scope: "Metadata at fixed filter/grouping consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-metadata]
              note: "Identifiers and category, priority and context attributes have localized filter/grouping uses."
          records: [memory.md#mem-obj-metadata]
          note: "The symbolic consumption path is distinct from semantic interpretation of source outcomes."
        - scope: "Source outcome descriptions at the consolidation model"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-metadata]
              note: "The model interprets outcome descriptions when comparing guidance."
          records: [memory.md#mem-obj-metadata]
          note: "This is the linguistic part of otherwise structured metadata."
        - scope: "Stored dense vectors at clustering and retrieval consumers"
          assessment: known
          findings:
            - value: parametric
              basis: claimed
              records: [memory.md#mem-obj-embeddings]
              note: "Dense numerical representations distribute information across vector coordinates; this does not mean model weights are updated."
          records: [memory.md#mem-obj-embeddings]
          note: "Both content/purpose and description vectors have this form despite their unresolved index relationship."
      records: [memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata, memory.md#mem-obj-embeddings]
      note: "The declared retained output inventory separates text, symbolic attributes and dense numerical representations. Unknown physical storage does not obscure these forms; raw inputs and transient intermediates are not established additional retained outputs."
    lineage:
      assessment: partial
      units:
        - scope: "Extracted tips, generated subtask descriptions and source-derived metadata"
          assessment: known
          findings:
            - value: trace-extracted
              basis: claimed
              records: [runtime.md#rt-rte-trajectory-extraction, memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata]
              note: "The trajectory-analysis pipeline produces guidance, subtask access text and provenance/outcome fields from completed execution."
          records: [runtime.md#rt-rte-trajectory-extraction, memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata]
          note: "Covers the documented extraction derivation, not arbitrary initial corpus admission."
        - scope: "Original task descriptions reused as task-level access keys"
          assessment: known
          findings:
            - value: imported
              basis: claimed
              records: [memory.md#mem-obj-descriptions, memory.md#mem-obj-trajectories]
              note: "The original task request is reused as description text rather than generated by description abstraction."
          records: [memory.md#mem-obj-descriptions, memory.md#mem-obj-trajectories]
          note: "This branch is kept distinct from generated subtask and canonical descriptions."
        - scope: "Consolidated successors, canonical descriptions and stored vector derivation"
          assessment: known
          findings:
            - value: other-compiled
              basis: claimed
              records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-embeddings, memory.md#mem-obj-descriptions]
              note: "Semantic merging/canonicalization compiles prior outputs; the embedding model transforms retained text into dense access representations."
          records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-embeddings, memory.md#mem-obj-descriptions]
          note: "These immediate transformations coexist with upstream trace extraction; neither implies learned embedding-model provenance."
        - scope: "Initial corpus and raw-input provenance beyond the documented derivation"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
          note: "Initial authorship/intake and durable raw artifacts are unspecified; the known extraction path cannot enumerate all initial-content provenance."
      records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata, memory.md#mem-obj-embeddings, memory.md#mem-obj-trajectories]
      note: "Positive derivation paths are documented, but initial corpus provenance is unresolved. Provider training lineage is outside the accumulated-memory boundary."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained tips at the later ReAct agent's guidelines consumer"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [runtime.md#rt-bap-guidelines-channel, memory.md#mem-obj-tips]
              note: "Conditional prescriptions, steps and triggers supply advisory directions for the current task, not executable permissions."
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-tips, runtime.md#rt-bap-guidelines-channel]
              note: "Delivered explanatory purpose and reference advice supply context for interpreting the prescription; full source evidence is not delivered."
          records: [memory.md#mem-obj-tips, runtime.md#rt-bap-guidelines-channel]
          note: "Both effects concern delivered text; actual compliance or content-dependent activation is not observed."
        - scope: "Accumulated tips consumed by semantic consolidation"
          assessment: known
          findings:
            - value: learning
              basis: claimed
              records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips]
              note: "Retained experience-derived guidance feeds an automatic update of durable successor guidance for later agents."
          records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips]
          note: "Authority at the update consumer is separate from the successor's advisory authority and from demonstrated improvement."
        - scope: "Stored descriptions/vectors and priority/outcome fields at selection consumers"
          assessment: known
          findings:
            - value: ranking
              basis: claimed
              records: [memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings, memory.md#mem-obj-metadata, epistemic.md#epi-rte-conflict-check, runtime.md#rt-rte-llm-selection]
              note: "Description/vector similarity ranks retrieval and clustering candidates; priority and source outcomes influence relative retrieval/merge preference."
          records: [memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings, memory.md#mem-obj-metadata, epistemic.md#epi-rte-conflict-check, runtime.md#rt-rte-llm-selection]
          note: "Fixed scoring still gives retained representations ranking force; no learned ranking policy is inferred."
        - scope: "Stored application/task/category metadata at LLM-guided retrieval"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-metadata, runtime.md#rt-rte-llm-selection]
              note: "Stored attributes determine the query's eligible domain/category scope, including generic null-context guidance."
          records: [memory.md#mem-obj-metadata, runtime.md#rt-rte-llm-selection]
          note: "This is access-scope selection, not an API capability grant or independent truth-validation gate."
        - scope: "Possible retained raw trajectories at extraction"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
          note: "Trace evidence feeds extraction, but raw retention across invocations is unspecified; its authority as an accumulated raw-memory object cannot be completed."
      records: [memory.md#mem-obj-tips, memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings, memory.md#mem-obj-metadata, memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, runtime.md#rt-rte-llm-selection, runtime.md#rt-bap-guidelines-channel, epistemic.md#epi-rte-conflict-check]
      note: "Declared consumers support advisory, update, ranking and scope effects. Raw retention and uninspected maintenance consumers prevent a complete accumulated-memory authority inventory; benchmark scoring is not a memory authority route."
    write_agency:
      assessment: partial
      units:
        - scope: "Model extraction and subsequent consolidation admission"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation]
              note: "The model pipeline proposes tips and decides merged successors without an established per-content human approval requirement. Workflow initiation is not manual admission."
          records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation]
          note: "Covers both task/subtask extraction and semantic management, not merely physical I/O."
        - scope: "Initial/raw-input admission and corpus initialization"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
          note: "Intake controller and initial-content control are unspecified; neither manual nor automatic initialization follows from model authorship downstream."
      records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-trajectories]
      note: "Known computational successor admission coexists with unresolved initialization; no manual finding is established."
    curation_operations:
      assessment: partial
      units:
        - scope: "Documented semantic consolidation over accumulated tips and descriptions"
          assessment: partial
          findings:
            - value: consolidate
              basis: claimed
              records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-descriptions]
              note: "Description abstraction and merging reduce overlapping retained content into canonical access text and guidance."
            - value: dedup
              basis: claimed
              records: [runtime.md#rt-rte-tip-consolidation]
              note: "The model is requested to merge redundant tips into non-overlapping guidance."
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-descriptions, epistemic.md#epi-rte-conflict-disposition]
              note: "Canonical descriptions replace individual descriptions and precedence changes retained successor guidance."
          records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-descriptions, epistemic.md#epi-rte-conflict-disposition]
          note: "These are declared transformations, not observed semantic success. Requested synthesis of complementary guidance does not establish a new claim absent from its inputs; actual successor semantics remain indeterminate."
        - scope: "Other maintenance, withdrawal, expiry and recovery mechanisms"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-metadata]
          note: "No executable pruning, expiry, reversible invalidation or rollback account is available. Timestamps and conflict precedence alone do not establish those operations."
      records: [runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-descriptions, memory.md#mem-obj-metadata, epistemic.md#epi-rte-conflict-disposition]
      note: "Declared consolidation, deduplication and revision are positives; unknown successor semantics and maintenance coverage prevent completeness. Extraction's novel conjectures are not by themselves curation over retained memory."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Pre-task cosine and LLM-guided tip selection and guidelines insertion"
          assessment: known
          findings:
            - value: push
              basis: claimed
              records: [runtime.md#rt-rte-cosine-retrieval, runtime.md#rt-rte-llm-selection, runtime.md#rt-bap-guidelines-channel]
              note: "A new task triggers automatic selection of tips into the consumer's initial prompt before reasoning; the foreground agent does not request retained material."
          records: [runtime.md#rt-rte-cosine-retrieval, runtime.md#rt-rte-llm-selection, runtime.md#rt-bap-guidelines-channel]
          note: "Both alternative selectors share the same delivery channel; internal query execution is not a separate consumer pull."
        - scope: "Other later-consumer routes, including raw-memory reload"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-agent-execution]
          note: "Raw retention, reload and mid-run memory access are unspecified, not evidenced absent; no additional pull route can be classified."
      records: [runtime.md#rt-rte-cosine-retrieval, runtime.md#rt-rte-llm-selection, runtime.md#rt-bap-guidelines-channel, memory.md#mem-obj-trajectories, runtime.md#rt-rte-agent-execution]
      note: "The documented cross-task routes are push; implementation/reload gaps prevent a complete inventory rather than establish pull-only or push-only deployed behavior."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Cosine branch: new task to stored descriptions to associated tips"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: claimed
              records: [runtime.md#rt-rte-cosine-retrieval, memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings]
              note: "Task embedding similarity selects stored descriptions and their associated tips, subject to threshold and optional top-k."
          records: [runtime.md#rt-rte-cosine-retrieval, memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings]
          note: "Top-3 and uncapped variants remain configuration-specific; an item cap is not a token budget."
        - scope: "LLM-guided branch: task interpretation and hybrid query selecting tips"
          assessment: known
          findings:
            - value: inferred-judgment
              basis: claimed
              records: [runtime.md#rt-rte-llm-selection, memory.md#mem-obj-metadata]
              note: "The model infers application/category and relevant guidance classes from the new task, shaping eligible tips."
            - value: inferred-embedding
              basis: claimed
              records: [runtime.md#rt-rte-llm-selection, memory.md#mem-obj-embeddings]
              note: "The resulting query also uses semantic similarity, alongside metadata filters and priority-weighted ranking."
          records: [runtime.md#rt-rte-llm-selection, memory.md#mem-obj-metadata, memory.md#mem-obj-embeddings]
          note: "The documented hybrid selector targets tips; source IDs alone do not establish identifier-targeted push."
        - scope: "Selection on unspecified additional reload/access routes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-agent-execution, memory.md#mem-obj-trajectories]
          note: "Additional read-back and any corresponding selector are unresolved; known initial push does not classify them."
      records: [runtime.md#rt-rte-cosine-retrieval, runtime.md#rt-rte-llm-selection, memory.md#mem-obj-descriptions, memory.md#mem-obj-embeddings, memory.md#mem-obj-metadata, runtime.md#rt-rte-agent-execution, memory.md#mem-obj-trajectories]
      note: "Embedding and judgment selection are documented locally. Missing access-route coverage and index wiring prevent complete system enumeration."
    trace_learning:
      assessment: partial
      units:
        - scope: "Completed trajectories through extraction and consolidation to later-task guidelines"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips, runtime.md#rt-bap-guidelines-channel]
              note: "Automatic trace-fed production yields intended durable behavioral tips, subsequently selected for a later agent's context. Parameter updates or demonstrated benefit are unnecessary for this route classification."
          records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips, runtime.md#rt-bap-guidelines-channel]
          note: "Task/subtask and labeled/self-inferred outcomes share this declared durable-guidance chain; operation is unobserved."
        - scope: "Unspecified initialization and other maintenance writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation]
          note: "The capture does not enumerate intake control or executable maintenance, preventing assessment of every possible qualifying write."
      records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation, memory.md#mem-obj-tips, runtime.md#rt-bap-guidelines-channel]
      note: "A positive design-level route is established; unknown additional writes do not erase it or justify a system-wide negative. Actual benefit and exercised self-improvement remain separate questions."
    trace_source:
      assessment: partial
      units:
        - scope: "Original completed-execution input to the documented guidance write"
          assessment: known
          findings:
            - value: trajectories
              basis: claimed
              records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
              note: "The input links sequential contexts, reasoning, actions, results and final outcome as multi-step experience."
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
              note: "Recorded agent invocations include prompts/contexts and agent responses with thoughts/reflections used in extraction."
            - value: tool-traces
              basis: claimed
              records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
              note: "Recorded actions and their results supply execution/error feedback used to derive recovery and other guidance."
          records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction]
          note: "These values identify overlapping content of the same original input, not three independent learning routes. Optional evaluation reports augment outcomes without establishing an event-stream source."
        - scope: "Original inputs to unspecified additional qualifying writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation]
          note: "Unresolved intake/maintenance coverage leaves additional learning inputs unclassified; it is not an inapplicable branch."
      records: [memory.md#mem-obj-trajectories, runtime.md#rt-rte-trajectory-extraction, runtime.md#rt-rte-tip-consolidation]
      note: "The positive sources describe the documented write chain; unknown additional writes prevent a complete original-input inventory."
---

# Trajectory-informed memory generation memory profile

## Comparison rationale

All positive findings are **claimed**. The accepted records describe doctrine and attributed aggregate results, not inspected wiring, observed extraction/retrieval traces or a registered causal experiment. A resolved classification within a declared unit therefore does not assert implementation or operation. In particular, the form inventory is known at the documented retained-output boundary even though physical persistence and other admission/access mechanisms remain unresolved.

Reconciliation supersedes the epistemic trajectory, tip and metadata duplicates with the memory objects. This profile uses [MEM-OBJ-trajectories](memory.md#mem-obj-trajectories), [MEM-OBJ-tips](memory.md#mem-obj-tips) and [MEM-OBJ-metadata](memory.md#mem-obj-metadata). Those amendments change citation identity, not classification strength. The description-index container remains valid, but separate [MEM-OBJ-descriptions](memory.md#mem-obj-descriptions) and [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings) preserve the different text and numerical consumers. No supersession changes a positive value.

The storage union contains vector, not model-weights: dense access representations are retained outputs, while provider weights are producing/consuming components with no established update in this memory boundary. Likewise, parametric form refers to those dense representations, not evidence of parameter training. The unresolved relationship between content/purpose vectors and description indices prevents a complete schema claim, but does not change their shared numerical form. See [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings).

Instruction and knowledge distinguish prescription from explanatory context at the guidelines consumer. Learning instead concerns retained experience feeding a successor update at consolidation. Ranking concerns retained descriptions, vectors and outcome/priority attributes at actual selectors. Routing concerns metadata selecting retrieval scope. None grants API permission or demonstrates that an instruction changed an action. These paths are supported by [RT-BAP-guidelines-channel](runtime.md#rt-bap-guidelines-channel), [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation), [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection) and [EPI-RTE-conflict-check](epistemic.md#epi-rte-conflict-check).

The curation union intentionally does not equate the source's word synthesis with the controlled value synthesize. [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation) establishes requested semantic merging; [EPI-RTE-conflict-disposition](epistemic.md#epi-rte-conflict-disposition) retains indeterminate successor semantics. Combining complementary steps does not establish a claim absent from the inputs. Conversely, the extraction example's broader conjecture is established in [EPI-RTE-attribution-generation](epistemic.md#epi-rte-attribution-generation), but that production from a trace is not by itself an operation over already retained memory. No positive synthesis finding is therefore established for curation. Expiry, decay, reversible invalidation and promotion cannot be inferred from timestamps or source-outcome precedence.

Both retrieval alternatives supply selected tips automatically on a task trigger. Executing an internal query is not a foreground agent's request for memory. Embedding selection and model-derived query criteria remain separate signals; top-k settings bound item counts only, and retained identifiers alone do not establish identity-targeted delivery. See [RT-RTE-cosine-retrieval](runtime.md#rt-rte-cosine-retrieval) and [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection).

The trace-learning positive classifies automatic production of durable cross-task guidance, not improved capacity or exercised self-improvement. The original input contains conversational material and action/result feedback organized as complete trajectories, so all three source findings survive the union. Optional labels and self-inferred outcomes alter warrant, not that original trace origin. Neither aggregate gains nor counterexamples upgrade these design-level findings; [RT-CLM-reported-results](runtime.md#rt-clm-reported-results) explicitly preserves configuration-specific harm and missing component attribution.

Source-read log: none. Classification used only the handed accepted records and reconciliation; no frozen-source ambiguity required a source read. No records or evidence were added.
