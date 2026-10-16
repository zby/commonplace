---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "A-MEM memory comparison for instance-local notes, semantic metadata, links and Chroma representations."
run-id: AAS-2026-10-16-a-mem-sys-eff95cd80440-01
source-identity: https://github.com/WujiangXu/A-mem-sys
reviewed-boundary: f303dfc71e07bdc787f4bc135d4cea328ae30e99
memory-comparison:
  version: 2
  scope: "Accumulated MemoryNote content, semantic fields, links, usage/history fields and Chroma text/metadata/vector snapshots; admission, direct edits, automatic evolution, index maintenance and later reads within an initialized instance. Provider-side retention is unresolved. Static prompts, inference/embedding model weights, test assertions, external task agents and hypothetical cross-session restoration are not accumulated memory in this boundary."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Live note content, metadata, links and usage/history attributes"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields]
              note: "Python objects in the instance map retain these parts; symbolic links do not establish a graph storage engine."
          records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields]
          note: "All live note field groups are inventoried in the cited objects."
        - scope: "Chroma enhanced documents, metadata and indexed vectors"
          assessment: partial
          findings:
            - value: vector
              basis: wired
              records: [memory.md#mem-obj-chroma-snapshot]
              note: "Collection add and similarity queries establish vector storage/index use, not a particular internal database."
          records: [memory.md#mem-obj-chroma-snapshot]
          note: "Dependency-internal physical storage and durability are uninspected; no sqlite, files or cross-session substrate is inferred."
        - scope: "Possible provider-side retention of supplied memory payloads"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Adapter requests do not expose provider storage or establish that accumulated provider memory exists."
      records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "The local object and collection inventory is explicit; dependency internals and provider retention prevent complete substrate coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Content, context, semantically interpreted keywords/tags/category and enhanced document text"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, epistemic.md#epi-obj-enhanced-document]
              note: "These strings supply model-interpreted descriptions and reader context, including the readable enhanced embedding input."
          records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, epistemic.md#epi-obj-enhanced-document]
          note: "Classification concerns the text consumption paths, not a claim that every caller string is propositional prose."
        - scope: "Links, field containers, IDs, timestamps, counters and metadata serialization"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-obj-chroma-snapshot]
              note: "Fixed lookup, iteration and conversion rules consume localized identifiers and fields."
          records: [memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-obj-chroma-snapshot]
          note: "History containers are covered here; their arbitrary caller payload is separate."
        - scope: "Dense Chroma embedding payload"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-sentence-transformer]
              note: "Stored dense representations distribute numerical state; the readable enhanced_content is not this payload."
          records: [memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-sentence-transformer]
          note: "Form is established without observing numerical vectors or classifying static model weights as memory."
        - scope: "Caller-supplied evolution_history payload and possible provider-retained state"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-usage-fields, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "A list slot and provider request reveal neither payload semantics nor any provider-retained form."
      records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-obj-chroma-snapshot, epistemic.md#epi-obj-enhanced-document, runtime.md#rt-cmp-sentence-transformer, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Text, structural and numerical parts are separated; unconstrained history and provider payloads prevent complete form classification."
    lineage:
      assessment: partial
      units:
        - scope: "Generated semantic fields, applied relationship edits and enhanced document/serialized snapshot derivation"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, memory.md#mem-obj-chroma-snapshot]
              note: "Software/model transformations derive retained representations from supplied notes; no recorded trace origin justifies trace-extracted."
          records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, memory.md#mem-obj-chroma-snapshot]
          note: "This resolves the subsequent derivation path, not the original authorship of its inputs."
        - scope: "Initial caller content, supplied metadata/links/history and direct replacement values"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, runtime.md#rt-rte-direct-mutation]
          note: "Generic caller input may be authored, imported or trace-derived; source records do not distinguish these origins."
        - scope: "Dense embedding derivation and upstream model artifact provenance"
          assessment: partial
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-sentence-transformer]
              note: "Enhanced text feeds the configured embedding function to produce indexed vectors."
          records: [memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-sentence-transformer]
          note: "Exact embedding artifact provenance/version remains uninspected; known derivation does not resolve it."
        - scope: "Possible provider-retained memory provenance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Local adapters provide no retained-provider lineage account."
      records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-rte-direct-mutation, memory.md#mem-obj-memory-content, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-sentence-transformer, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Derived artifacts are supported locally; initial inputs, embedding provenance and provider retention remain unresolved. Acquisition through an API alone does not identify original lineage."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained content and semantic snapshots delivered to later evolution model and Python readers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-neighbor-context, runtime.md#rt-bap-caller-results, memory.md#mem-obj-semantic-metadata]
              note: "Content supplies reference/context to evolution and returned data to callers, not standing instructions or verified truth."
          records: [runtime.md#rt-bap-neighbor-context, runtime.md#rt-bap-caller-results, memory.md#mem-obj-semantic-metadata]
          note: "Delivery wiring is established; actual model reliance or a downstream answering agent is not."
        - scope: "Content/semantic enhanced documents and dense vectors at similarity selection"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-rte-memory-retrieval]
              note: "Retained text/features determine embedding similarity priority, even though ranking code is fixed."
          records: [memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-rte-memory-retrieval]
          note: "This is ranking influence, not evidence of superior retrieval."
        - scope: "Retained link IDs at optional linked-result expansion"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-note-links, runtime.md#rt-rte-memory-retrieval]
              note: "Membership lookup chooses additional note inputs; truncation can prevent appended candidates reaching the caller."
          records: [memory.md#mem-obj-note-links, runtime.md#rt-rte-memory-retrieval]
          note: "Symbolic selection does not grant retained links executable instruction force."
        - scope: "Unconstrained caller history payload and opaque provider retention consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-usage-fields, memory.md#mem-abs-usage-feedback, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "No automatic usage/history selector exists locally; payload meaning and provider consumers are unresolved. No learning or instruction authority is inferred."
      records: [runtime.md#rt-bap-neighbor-context, runtime.md#rt-bap-caller-results, memory.md#mem-obj-semantic-metadata, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-rte-memory-retrieval, memory.md#mem-obj-note-links, memory.md#mem-obj-usage-fields, memory.md#mem-abs-usage-feedback, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Local context, ranking and routing paths are positive; call-local evolution controls and static schemas are not retained-memory enforcement/validation criteria. Opaque consumers prevent a complete union."
    write_agency:
      assessment: partial
      units:
        - scope: "Missing/default semantic-field admission and model-directed relationship/neighbor edits"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition]
              note: "Code admits generated values and fixed-action mutations without a per-content human approval decision."
          records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition]
          note: "Starting ingestion is not approval of each subsequent generated edit; exposed process_memory shares this automatic disposition."
        - scope: "Threshold-triggered bulk snapshot republication"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-index-consolidation]
              note: "The evolution counter triggers software admission to the retriever without reviewing individual contents."
          records: [memory.md#mem-rte-index-consolidation]
          note: "Agency is resolved despite unresolved successful replacement of existing IDs."
        - scope: "Caller content/metadata admission, direct CRUD/live-reference edits, explicit maintenance and direct retriever writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-direct-mutation, memory.md#mem-rte-index-consolidation, memory.md#mem-obj-chroma-snapshot]
          note: "Generic Python caller identity does not establish a human content decision or automatic caller policy; physical software I/O does not resolve admission agency."
        - scope: "Possible provider-retained state admission"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Adapters establish inference requests only, not provider memory admission controls."
      records: [runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition, runtime.md#rt-rte-direct-mutation, memory.md#mem-rte-index-consolidation, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Automatic transformations coexist with unresolved caller control; README review advice does not establish manual admission."
    curation_operations:
      assessment: partial
      units:
        - scope: "Applied neighbor-context/tag replacement and direct existing-note field replacement"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition, runtime.md#rt-rte-direct-mutation]
              note: "Fixed dispatch and direct updates revise retained entries; semantic improvement is not required for revision."
          records: [runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition, runtime.md#rt-rte-direct-mutation]
          note: "Classifies implemented replacement, not reliable requested model judgment."
        - scope: "Semantic relation of generated/replacement descriptions to their inputs"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-metadata-generation, epistemic.md#epi-rte-evolution-judgment]
          note: "Actual outputs and semantic comparison are missing; requests for summaries/interpretations do not establish consolidate or synthesize over retained content."
        - scope: "Caller deletion of retained notes from the retriever and live map"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [runtime.md#rt-rte-direct-mutation, memory.md#mem-obj-note-links]
              note: "Deletion forgets retained entries by removing them from the retriever and then the live map; forgetting need not be gradual or automatic."
          records: [runtime.md#rt-rte-direct-mutation, memory.md#mem-obj-note-links]
          note: "This bounded forgetting mechanism does not establish invalidate: no withdrawal history is retained. Surviving links can dangle, and already delivered copies are not erased."
        - scope: "Index republication"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-index-consolidation]
          note: "Re-adding snapshots alone is index maintenance, not a controlled curation transformation; successful replacement of existing IDs remains unresolved."
        - scope: "Possible provider-side curation"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Inference adapters do not expose retained-state transformations."
      records: [runtime.md#rt-rte-neighbor-evolution, epistemic.md#epi-rte-evolution-disposition, runtime.md#rt-rte-direct-mutation, epistemic.md#epi-rte-metadata-generation, epistemic.md#epi-rte-evolution-judgment, memory.md#mem-rte-index-consolidation, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Entry revision and deletion-based forgetting support evolve and decay; semantic novelty/preservation and opaque provider operations prevent complete curation coverage. Route labels do not establish consolidate, dedup or promote."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Caller-requested ID, similarity and linked retrieval/formatting"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-memory-retrieval, runtime.md#rt-bap-caller-results]
              note: "The caller explicitly requests retained note material; selection and return fulfill that request."
          records: [runtime.md#rt-rte-memory-retrieval, runtime.md#rt-bap-caller-results]
          note: "Optional link expansion remains part of the requested return, not a second unsolicited delivery."
        - scope: "Automatic neighbor selection and delivery to evolution during later add or direct processing"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-bap-neighbor-context, epistemic.md#epi-rte-evolution-judgment]
              note: "Python selects and supplies retained neighbors; the evolution model did not request retrieval."
          records: [runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-bap-neighbor-context, epistemic.md#epi-rte-evolution-judgment]
          note: "A caller's ingestion request can trigger internal push without becoming an autonomous scheduled loop."
        - scope: "Possible provider-internal retained context delivery"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Stateless local requests do not reveal provider retention or later-consumer routes."
      records: [runtime.md#rt-rte-memory-retrieval, runtime.md#rt-bap-caller-results, runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-bap-neighbor-context, epistemic.md#epi-rte-evolution-judgment, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Both local directions are wired. Provider-internal uncertainty is not resolved by those witnesses; no cross-session or task-answer route is inferred."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic evolution neighbor push"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-rte-memory-retrieval, memory.md#mem-obj-chroma-snapshot]
              note: "Trigger is a new note with available neighbors; new-note content queries enhanced-document embeddings and selects up to five retained snapshots for evolution."
          records: [runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-rte-memory-retrieval, memory.md#mem-obj-chroma-snapshot]
          note: "IDs label retrieved neighbors and bound subsequent writes; they are not the push selector. Five is a budget, not a separate coarse selection route."
        - scope: "Explicit caller ID/similarity/link retrieval"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-memory-retrieval, runtime.md#rt-bap-caller-results]
          note: "These operations fulfill pull requests; identifier and embedding selectors on them are not additional push signals."
        - scope: "Possible provider-internal push selection"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "No provider-retained payload or selector is inspectable from the adapters."
      records: [runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-rte-memory-retrieval, memory.md#mem-obj-chroma-snapshot, runtime.md#rt-bap-caller-results, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "Embedding-based internal push is positive; caller pull does not make unresolved provider alternatives inapplicable."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Automatic usage/history/rationale feedback through note usage fields"
          assessment: absent
          findings: []
          records: [memory.md#mem-abs-usage-feedback, memory.md#mem-obj-usage-fields]
          note: "The searched shipped paths do not increment access/count fields, append evolution reasons or feed them back. This bounded absence is not a system-wide no."
        - scope: "Caller input to automatic semantic fields/neighbor edits and later embedding/evolution consumption"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-content, runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-bap-neighbor-context]
          note: "Automatic retained transformations and later consumers exist, but original inputs are not established as activity traces. No qualifying trace-fed yes or comprehensive no follows."
        - scope: "Direct caller replacement/history admission and possible provider learning"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-direct-mutation, memory.md#mem-obj-usage-fields, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Caller agency and payload origin are unknown; provider internal retained updates are uninspected. Local absence of parameter training does not settle artifact-based trace learning."
      records: [memory.md#mem-abs-usage-feedback, memory.md#mem-obj-usage-fields, memory.md#mem-obj-memory-content, runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-bap-neighbor-context, runtime.md#rt-rte-direct-mutation, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "No controlled system finding is established: bounded absent feedback does not resolve the origin/control of other included writes. Improvement evidence is not the missing requirement; trace-fed provenance is."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Absent automatic usage/history feedback route"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-abs-usage-feedback]
          note: "No qualifying write exists on this bounded field-maintenance route, so it has no trace source."
        - scope: "Potential trace-bearing caller content/history transformed into later-consumed metadata"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-content, memory.md#mem-obj-usage-fields, runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution]
          note: "No recorded origin distinguishes session logs, tool traces, trajectories, event streams or nontrace text; labels such as experience/history do not decide."
        - scope: "Possible provider-internal trace-fed retention"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
          note: "Provider inputs to any learning route and retained outputs are not inspected."
      records: [memory.md#mem-abs-usage-feedback, memory.md#mem-obj-memory-content, memory.md#mem-obj-usage-fields, runtime.md#rt-rte-note-admission, runtime.md#rt-rte-neighbor-evolution, runtime.md#rt-cmp-openai, runtime.md#rt-cmp-ollama, runtime.md#rt-cmp-sglang, runtime.md#rt-cmp-open-router]
      note: "The source axis is unresolved rather than globally inapplicable because qualifying trace-fed writes have not been completely ruled out."
---

# A-MEM memory profile

## Comparison rationale

The comparison concerns retained note parts and their access structures, not all runtime state. Instance-local accumulation is sufficient for later read-back. It does not imply restoration across construction: the map starts empty and initialization attempts to reset the collection. The collection's dense vectors, readable enhanced text and symbolic metadata remain separate forms. A link list is a symbolic access structure in Python/Chroma, not evidence of a graph substrate ([MEM-OBJ-chroma-snapshot](memory.md#mem-obj-chroma-snapshot), [MEM-OBJ-note-links](memory.md#mem-obj-note-links), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)).

Reconciliation supersedes the epistemic note-content and semantic-metadata identities with [MEM-OBJ-memory-content](memory.md#mem-obj-memory-content) and [MEM-OBJ-semantic-metadata](memory.md#mem-obj-semantic-metadata). Those canonical objects are cited here. The enhanced-document part remains distinct from its valid Chroma container, so its natural-language classification cites [EPI-OBJ-enhanced-document](epistemic.md#epi-obj-enhanced-document). No route supersession changes a value.

Automatic evolution establishes entry revision because code replaces existing tags/context. It does not establish semantic synthesis or faithful consolidation. The models are asked for summaries and reinterpretations, but actual content relations remain indeterminate. Index consolidation merely republishes representations. Caller deletion removes retained entries from the retriever and live map, supporting decay as forgetting without requiring gradual downweighting or automatic selection. It does not retain withdrawal history, so it does not establish invalidate; surviving links may dangle and previously delivered copies remain outside this deletion mechanism. Thus evolve and decay are supported without importing operations suggested only by method names ([EPI-RTE-evolution-disposition](epistemic.md#epi-rte-evolution-disposition), [EPI-RTE-evolution-judgment](epistemic.md#epi-rte-evolution-judgment), [MEM-RTE-index-consolidation](memory.md#mem-rte-index-consolidation), [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation), [MEM-OBJ-note-links](memory.md#mem-obj-note-links)).

Retained descriptions have knowledge authority at later evolution and reader consumers, and ranking authority when enhanced text determines similarity. Link IDs route expansion. Call-local model decisions authorize mutations, but are not themselves retained standing controls. A later add's automatic embedding selector pushes neighbors to the model; explicit retrieval pulls material to the caller. Requested return is not another push. Neither delivery nor mutation establishes actual reliance, semantic correctness or demonstrated benefit ([RT-BAP-neighbor-context](runtime.md#rt-bap-neighbor-context), [RT-BAP-caller-results](runtime.md#rt-bap-caller-results), [MEM-OBJ-note-links](memory.md#mem-obj-note-links), [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)).

Unknown initial input provenance and generic caller identity are consequential. They prevent authored/manual classifications and prevent assigning a trace source. The automatic transformation chain is not erased, but cannot establish trace learning without trace-origin evidence. Conversely, the bounded absence of usage/history feedback cannot establish a global negative while caller-provided histories and provider processing remain unresolved ([MEM-OBJ-memory-content](memory.md#mem-obj-memory-content), [MEM-OBJ-usage-fields](memory.md#mem-obj-usage-fields), [MEM-ABS-usage-feedback](memory.md#mem-abs-usage-feedback), [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation)).

Provider-side memory is retained as an unresolved alternative, not asserted to exist. Static inference weights are excluded from the accumulated-memory inventory; their unchanged local parameters do not answer trace learning through artifacts. All positive bases are wired implementation, not observed operation or causal benefit. No source reads were made for this profile; classification used only the supplied accepted members and reconciliation.
