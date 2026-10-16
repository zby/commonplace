---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Basic Memory memory comparison: retained notes, graph/access state, session checkpoints and incomplete host/provider alternatives at the frozen partial-loop boundary."
run-id: "AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01"
source-identity: "https://github.com/basicmachines-co/basic-memory"
reviewed-boundary: "a72751c5d626380dedeed30f55f7a80ba3dc710d"
memory-comparison:
  version: 2
  scope: "Included: accepted and materialized notes; graph/search/vector access structures; note revision/publication state; raw lifecycle archives; Pi direct and Python-hook checkpoints; Tau handoffs and persisted receipts; Hermes continuity; OpenClaw captured notes and cross-invocation recall cache; retained schema criteria and stored-case evaluator consumers. Included unresolved alternatives: filesystem/import/CI/cloud admission, other read/maintenance paths, opaque host/provider accumulated state and evaluator feedback/persistence. Excluded: static shipped instructions/skills as memory objects, current request drafts and prepared current-mutation publication payloads without established later memory consumers, inference-only model weights as accumulated memory, external host internals and uncaptured live infrastructure. Shipped skill prescriptions remain evidence about potential writes and maintenance, not evidence of exercised operation."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Accepted note bodies and note identity/version/publication state"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-markdown-content"
                - "memory.md#mem-obj-sync-state"
                - "runtime.md#rt-rte-note-write"
              note: "Accepted Markdown and symbolic sync fields are database rows; the records do not establish a particular backend for every deployment."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-markdown-content"
                - "runtime.md#rt-rte-note-materialization"
              note: "Accepted bodies are materialized as Markdown files on the inspected local route."
          records:
            - "memory.md#mem-obj-markdown-content"
            - "memory.md#mem-obj-sync-state"
            - "runtime.md#rt-rte-note-write"
            - "runtime.md#rt-rte-note-materialization"
          note: "The accepted database body and materialized file are distinct completion points, both established locally."
        - scope: "Published graph relations and observations at later context traversal"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-publication"
                - "runtime.md#rt-rte-context-build"
              note: "Published symbolic relations and observations support later graph traversal."
          records:
            - "memory.md#mem-obj-graph-publication"
            - "runtime.md#rt-rte-context-build"
          note: "Classifies published graph memory consumed by later traversal, not every graph repository implementation. The process-local prepared payload belongs to current-mutation publication machinery; the records do not establish its qualifying retention and later memory consumption, so it supplies no substrate finding."
        - scope: "Raw lifecycle inbox and processed envelopes"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-envelope"
                - "memory.md#mem-rte-trace-archive"
              note: "UUID JSON files persist in inbox and processed directories and are reread during later flushes."
          records:
            - "memory.md#mem-obj-envelope"
            - "memory.md#mem-rte-trace-archive"
          note: "The local JSON archive substrate is explicit; it is not a conversation-note graph."
        - scope: "OpenClaw recall cache between bootstrap and assemble"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-rte-openclaw-context"
              note: "Session-keyed process-local cached recall is consumed by a later assemble call."
          records:
            - "memory.md#mem-rte-openclaw-context"
          note: "This short-horizon accumulated selection is separate from durable note storage."
        - scope: "Tau persisted host branch receipts and branch trace storage"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-capture-record"
            - "memory.md#mem-rte-tau-handoff"
          note: "Host custom entries are persisted, but the backing substrate and guarantees are not inspected; a host entry label does not establish files, a database or service-object."
        - scope: "Persisted embeddings, semantic chunks, caches and opaque provider-side accumulated state"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-note-materialization"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Vector work and numerical provider outputs are established, but accepted records do not trace vector-table/backend/cache storage or accumulated opaque provider state. Inference weights are not automatically accumulated memory."
        - scope: "Other importer/watch/CI/cloud stores and retained evaluator artifacts"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-markdown-content"
            - "runtime.md#rt-rte-note-write"
            - "epistemic.md#epi-obj-qa-case"
          note: "The recorded inventory leaves alternate storage paths and evaluator persistence incomplete. QA in-process objects cannot be joined to the separately described benchmark files without a recorded path."
      records:
        - "memory.md#mem-obj-markdown-content"
        - "memory.md#mem-obj-sync-state"
        - "runtime.md#rt-rte-note-write"
        - "runtime.md#rt-rte-note-materialization"
        - "memory.md#mem-obj-graph-publication"
        - "runtime.md#rt-rte-context-build"
        - "memory.md#mem-obj-envelope"
        - "memory.md#mem-rte-trace-archive"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-obj-capture-record"
        - "memory.md#mem-rte-tau-handoff"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
        - "epistemic.md#epi-obj-qa-case"
      note: "Positive local substrates do not enumerate the partial-loop memory inventory. Host receipts, vector storage, remote alternatives and evaluator persistence remain unresolved; no sqlite, repo or model-weights finding follows from packaging or static model availability."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Retained note and checkpoint prose at later human/model readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-markdown-content"
                - "memory.md#mem-rte-note-reload"
                - "runtime.md#rt-rte-pi-checkpoint"
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-rte-hermes-continuity"
                - "memory.md#mem-rte-openclaw-context"
              note: "Note assertions, extractive threads and model handoffs reach later readers as interpreted prose."
          records:
            - "memory.md#mem-obj-markdown-content"
            - "memory.md#mem-rte-note-reload"
            - "runtime.md#rt-rte-pi-checkpoint"
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-rte-hermes-continuity"
            - "memory.md#mem-rte-openclaw-context"
          note: "Covers the inspected prose consumption paths, not all note types or host readers."
        - scope: "Note metadata, parsed graph topology, envelopes and receipts at fixed-rule consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sync-state"
                - "memory.md#mem-obj-graph-publication"
                - "memory.md#mem-obj-envelope"
                - "memory.md#mem-obj-capture-record"
              note: "Localized IDs, checksums, generations, replay keys and receipt states are consumed by deterministic rules."
          records:
            - "memory.md#mem-obj-sync-state"
            - "memory.md#mem-obj-graph-publication"
            - "memory.md#mem-obj-envelope"
            - "memory.md#mem-obj-capture-record"
          note: "Separates access/control fields from natural-language observation text within the same containers."
        - scope: "Dense numerical embeddings used by inspected semantic inference/vector work"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-fastembed-provider"
                - "runtime.md#rt-cmp-openai-provider"
                - "runtime.md#rt-cmp-litellm-provider"
                - "runtime.md#rt-rte-note-materialization"
              note: "Dense vector representations are distributed numerical material, not symbolic graph topology or prose."
          records:
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-rte-note-materialization"
          note: "The numerical form is established; exact persistence and deployment choice are independently incomplete."
        - scope: "Stored QA cases at rejudging"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-qa-case"
                - "epistemic.md#epi-rte-qa-judge"
              note: "Question, gold, candidate answer and reason retain prose interpreted by the judge."
            - value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-qa-case"
                - "epistemic.md#epi-rte-qa-judge"
              note: "Correct/error/model/accounting fields are localized fields used by metric code."
          records:
            - "epistemic.md#epi-obj-qa-case"
            - "epistemic.md#epi-rte-qa-judge"
          note: "Stored-case rejudging is established independently of untraced artifact-file persistence."
        - scope: "Opaque host/provider state and untraced alternative imports, tools and consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-capture-record"
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-obj-markdown-content"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Readable output does not classify opaque retained payloads or uninspected alternate routes. The recorded coverage prevents an exhaustive form inventory."
      records:
        - "memory.md#mem-obj-markdown-content"
        - "memory.md#mem-rte-note-reload"
        - "runtime.md#rt-rte-pi-checkpoint"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-obj-sync-state"
        - "memory.md#mem-obj-graph-publication"
        - "memory.md#mem-obj-envelope"
        - "memory.md#mem-obj-capture-record"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-rte-note-materialization"
        - "epistemic.md#epi-obj-qa-case"
        - "epistemic.md#epi-rte-qa-judge"
      note: "Known mixed prose, symbolic and dense numerical parts remain separate. Static shipped skills and provider weights used only for inference are not substituted for memory accumulated through use."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller-supplied note body: documented authoring and import paths"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-markdown-content"
                - "runtime.md#rt-rte-note-write"
              note: "Caller-authored Markdown is admitted as note content; this does not resolve human versus model authorship."
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-markdown-content"
              note: "Imported files are a recorded note-content lineage; per-format fidelity remains separate."
          records:
            - "memory.md#mem-obj-markdown-content"
            - "runtime.md#rt-rte-note-write"
          note: "Classifies these recorded derivation paths, not the unknown provenance of every possible note."
        - scope: "Pi direct/hook, Tau and Hermes checkpoint derivation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-rte-hermes-continuity"
              note: "Public session text is selected or summarized into durable checkpoints for later recall."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "runtime.md#rt-rte-hook-checkpoint"
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-rte-hermes-continuity"
          note: "Model-authored Tau wording does not erase its trace-fed derivation; no claim of faithful extraction is implied."
        - scope: "OpenClaw daily captured conversation and lifecycle notes"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-openclaw-context"
              note: "Host turn/lifecycle events supply automatically appended conversation and handoff material."
          records:
            - "memory.md#mem-rte-openclaw-context"
          note: "Child-note later consumers remain unresolved independently of the captured origin."
        - scope: "Published parsed graph and retained mutation/publication metadata"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-publication"
                - "memory.md#mem-obj-sync-state"
              note: "Fixed parsing and mutation/publication rules derive retained published graph structure and sync state from accepted content and storage outcomes, excluding the transient prepared publication payload."
          records:
            - "memory.md#mem-obj-graph-publication"
            - "memory.md#mem-obj-sync-state"
          note: "These artifacts are compiled operational representations, not new independent source findings."
        - scope: "Normalized lifecycle envelope metadata and Tau write receipts"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-envelope"
              note: "Harness lifecycle activity is normalized into raw structured metadata."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-record"
                - "memory.md#mem-rte-tau-handoff"
              note: "Receipt identities, digests and pending/confirmed state are assembled for write reconciliation."
          records:
            - "memory.md#mem-obj-envelope"
            - "memory.md#mem-obj-capture-record"
            - "memory.md#mem-rte-tau-handoff"
          note: "The two findings attach to distinct explicitly named parts in this operational-metadata unit."
        - scope: "Initial content provenance, embedding provenance and alternate import/CI/cloud derivations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-markdown-content"
            - "runtime.md#rt-rte-note-materialization"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Known note and vector routes do not resolve all initial content, exact weight/vector lineage or transformations in untraced alternatives."
      records:
        - "memory.md#mem-obj-markdown-content"
        - "runtime.md#rt-rte-note-write"
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-obj-graph-publication"
        - "memory.md#mem-obj-sync-state"
        - "memory.md#mem-obj-envelope"
        - "memory.md#mem-obj-capture-record"
        - "runtime.md#rt-rte-note-materialization"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Authored, imported, trace-extracted and fixed compiled paths are supported locally. Initial/embedding provenance and alternate acquisition paths prevent complete lineage coverage."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Note/checkpoint prose delivered to later readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-reload"
                - "runtime.md#rt-rte-context-build"
                - "runtime.md#rt-bap-recall-data"
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-rte-hermes-continuity"
                - "memory.md#mem-rte-openclaw-context"
              note: "Tool callers and foreground assistants receive retained assertions, excerpts and handoffs as reference context; systemPromptAddition alone does not make reference text standing instructions."
          records:
            - "memory.md#mem-rte-note-reload"
            - "runtime.md#rt-rte-context-build"
            - "runtime.md#rt-bap-recall-data"
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-rte-hermes-continuity"
            - "memory.md#mem-rte-openclaw-context"
          note: "Delivery establishes a knowledge channel, not compliance, factual endorsement or benefit."
        - scope: "Prior Tau handoff at the next durable handoff update"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "A previously retained handoff is passed into subsequent summary calls that produce a new durable behavior-shaping handoff."
          records:
            - "memory.md#mem-rte-tau-handoff"
          note: "Names the update consumer separately from downstream knowledge supply; it does not claim improved capacity."
        - scope: "Retained text and indexed representations at query ranking/selection"
          assessment: "partial"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "memory.md#mem-rte-hermes-continuity"
              note: "Prompt/query-driven searches order note hits whose retained excerpts become recall; text is an input to relative selection, not a learned ranking policy."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "memory.md#mem-rte-hermes-continuity"
          note: "Local query/hit selection is recorded; full ranking algorithms, optional reranking and all consumers remain uninspected."
        - scope: "Sync/version metadata at mutation and materialization gates"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sync-state"
                - "runtime.md#rt-rte-note-write"
                - "runtime.md#rt-rte-note-materialization"
              note: "Stored revision/checksum state determines whether a candidate mutation or file write conforms to current-state requirements."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sync-state"
                - "runtime.md#rt-rte-note-write"
                - "runtime.md#rt-rte-note-materialization"
              note: "Failed revision/file guards can refuse mutation or publication."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sync-state"
                - "runtime.md#rt-rte-note-materialization"
              note: "Retained completion/version state selects stale retirement and recovery work."
          records:
            - "memory.md#mem-obj-sync-state"
            - "runtime.md#rt-rte-note-write"
            - "runtime.md#rt-rte-note-materialization"
          note: "These forces are operational consistency controls, not truth criteria."
        - scope: "Tau persisted receipts at orient and uncertain-write recovery"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-record"
                - "memory.md#mem-rte-tau-handoff"
              note: "Confirmed active-branch receipt selects a checkpoint; pending receipts select reconciliation rather than blind resubmission."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-record"
                - "memory.md#mem-rte-tau-handoff"
              note: "Stored capture identity/digest is a criterion for matching an uncertain write."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-record"
                - "memory.md#mem-rte-tau-handoff"
              note: "Ambiguous identity or changed digest prevents accepting the candidate reconciliation."
          records:
            - "memory.md#mem-obj-capture-record"
            - "memory.md#mem-rte-tau-handoff"
          note: "Distinct receipt consumers give distinct effects; host persistence guarantees remain outside inspection."
        - scope: "Retained schema definitions at requested structural validation"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-schema-validation"
              note: "Resolved schema criteria determine pass/warnings/errors for note structure."
          records:
            - "epistemic.md#epi-rte-schema-validation"
          note: "The check returns a report, not a core factual endorsement or automatic write veto."
        - scope: "Processed envelope keys at later archive replay accounting"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-envelope"
                - "memory.md#mem-rte-trace-archive"
              note: "Previously processed keys determine duplicate bookkeeping on a later flush."
          records:
            - "memory.md#mem-obj-envelope"
            - "memory.md#mem-rte-trace-archive"
          note: "Counting duplicates is an operational branch, not knowledge acceptance or semantic deduplication."
        - scope: "Other host child-note readers, provider state, schema observers and evaluator-to-product consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-openclaw-context"
            - "epistemic.md#epi-rte-schema-validation"
            - "epistemic.md#epi-obj-qa-case"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "No authority is inferred for unconsumed metadata or untraced external observers/child notes. Optional ranking and other note consumers are incomplete."
      records:
        - "memory.md#mem-rte-note-reload"
        - "runtime.md#rt-rte-context-build"
        - "runtime.md#rt-bap-recall-data"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "memory.md#mem-rte-openclaw-context"
        - "runtime.md#rt-rte-pi-checkpoint"
        - "memory.md#mem-obj-sync-state"
        - "runtime.md#rt-rte-note-write"
        - "runtime.md#rt-rte-note-materialization"
        - "memory.md#mem-obj-capture-record"
        - "epistemic.md#epi-rte-schema-validation"
        - "memory.md#mem-obj-envelope"
        - "memory.md#mem-rte-trace-archive"
        - "epistemic.md#epi-obj-qa-case"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "The recorded consumer paths support multiple independent forces. Static shipped directions are excluded; retained payload placement is not itself instruction or enforcement. Unknown consumers prevent an exhaustive authority union."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Pi direct and Python hook automatic checkpoint admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
              note: "Enabled event handlers select trace text and submit durable notes without per-content human approval."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "runtime.md#rt-rte-hook-checkpoint"
          note: "Workspace trust and project configuration enable automation; they are not decisions approving each checkpoint."
        - scope: "Tau, Hermes and OpenClaw enabled capture/update admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-rte-hermes-continuity"
                - "memory.md#mem-rte-openclaw-context"
              note: "Code/model-selected content passes software gates and common write rules without per-note human review."
          records:
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-rte-hermes-continuity"
            - "memory.md#mem-rte-openclaw-context"
          note: "Lifecycle/manual triggering does not by itself change subsequent content admission to manual."
        - scope: "Derived publication, sync state, raw envelopes and Tau receipts"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-note-materialization"
                - "memory.md#mem-obj-graph-publication"
                - "memory.md#mem-obj-sync-state"
                - "memory.md#mem-obj-envelope"
                - "memory.md#mem-rte-trace-archive"
                - "memory.md#mem-obj-capture-record"
              note: "Software derives and retains publication/control/trace/recovery state, without a content-specific operator approval."
          records:
            - "runtime.md#rt-rte-note-materialization"
            - "memory.md#mem-obj-graph-publication"
            - "memory.md#mem-obj-sync-state"
            - "memory.md#mem-obj-envelope"
            - "memory.md#mem-rte-trace-archive"
            - "memory.md#mem-obj-capture-record"
          note: "Classifies these downstream state writes separately from unresolved upstream generic note admission."
        - scope: "Research workflow saving decision"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-research-note"
              note: "The prescribed human yes/no/modify decision controls which researched note is saved."
          records:
            - "epistemic.md#epi-rte-research-note"
          note: "Doctrine names a per-content human decision; ordinary service admission does not enforce this workflow."
        - scope: "Reflection content admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-notes"
              note: "Prescribed assistant judges and writes durable items without per-item human approval."
          records:
            - "epistemic.md#epi-rte-reflect-notes"
          note: "Model-facing prescription, not an observed or autonomously scheduled execution."
        - scope: "Generic note/API callers and direct filesystem, importer, CI/cloud and initial-state admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-note-write"
            - "memory.md#mem-obj-markdown-content"
            - "memory.md#mem-rte-note-withdrawal"
          note: "Generic caller identity cannot resolve human versus model control. Alternate admission bodies and initial control remain incomplete."
        - scope: "Provider-side accumulated writes and evaluator persistence/adoption"
          assessment: "uninspected"
          findings: []
          records:
            - "epistemic.md#epi-obj-qa-case"
            - "epistemic.md#epi-rte-qa-judge"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Inference calls and stored-case availability do not establish every provider write or how evaluator artifacts are admitted into later operation."
      records:
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "memory.md#mem-rte-openclaw-context"
        - "runtime.md#rt-rte-note-materialization"
        - "memory.md#mem-obj-graph-publication"
        - "memory.md#mem-obj-sync-state"
        - "memory.md#mem-obj-envelope"
        - "memory.md#mem-rte-trace-archive"
        - "memory.md#mem-obj-capture-record"
        - "epistemic.md#epi-rte-research-note"
        - "epistemic.md#epi-rte-reflect-notes"
        - "runtime.md#rt-rte-note-write"
        - "memory.md#mem-obj-markdown-content"
        - "memory.md#mem-rte-note-withdrawal"
        - "epistemic.md#epi-obj-qa-case"
        - "epistemic.md#epi-rte-qa-judge"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Automatic checkpoint and downstream state admission coexist with a claimed human research gate. Generic caller requests and untraced alternatives prevent complete agency classification."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Pi direct/hook and Hermes extractive checkpoints"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
                - "memory.md#mem-rte-hermes-continuity"
              note: "Opening/last-turn extraction, clipping and selected thread formatting reduce retained session claims into continuation representations."
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
                - "memory.md#mem-rte-hermes-continuity"
              note: "Stable Pi checkpoint overwrite and Hermes session-note appends revise an existing retained entry."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "runtime.md#rt-rte-hook-checkpoint"
            - "memory.md#mem-rte-hermes-continuity"
          note: "Consolidation does not require a model call; clipping fidelity and actual usefulness remain unobserved."
        - scope: "Tau incremental handoff transformation"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Chunked public conversation and prior handoff are incrementally folded into a bounded retained handoff."
          records:
            - "memory.md#mem-rte-tau-handoff"
          note: "The implemented request/retention chain supports consolidation, not evidence that a novel claim was synthesized. Output fidelity and semantic novelty remain unresolved."
        - scope: "Raw processed-envelope age pruning"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-archive"
              note: "Processed JSON older than the configured retention window is removed."
          records:
            - "memory.md#mem-rte-trace-archive"
          note: "Age-based forgetting is wired; replay detection only counts duplicates and does not establish dedup."
        - scope: "Source-linked reflection maintenance"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-notes"
              note: "The skill prescribes selecting lasting facts from retained raw notes."
            - value: "evolve"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-notes"
              note: "Existing topic notes are updated with source-linked durable items."
            - value: "invalidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-notes"
              note: "Dated old facts are closed while retained, only when a source states the change and time."
          records:
            - "epistemic.md#epi-rte-reflect-notes"
          note: "These are prescribed transformations. Semantic examples remain indeterminate and do not establish synthesis or successful factual integration."
        - scope: "Lifecycle archive-and-status guidance"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-note-withdrawal"
              note: "Prescribed move/status edits preserve content but can remove it from active-status selection."
          records:
            - "memory.md#mem-rte-note-withdrawal"
          note: "This is not the implemented delete route: deletion alone does not establish withdrawal while retaining history."
        - scope: "Other edit/move modes, curation/defrag instructions, remote maintenance and vector/cache transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-withdrawal"
            - "runtime.md#rt-rte-note-materialization"
            - "memory.md#mem-obj-graph-publication"
          note: "Skill names, index rebuilding, deletion and primary-key checks do not establish consolidation, dedup, synthesis or promotion. Included maintenance alternatives remain uninspected."
      records:
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "memory.md#mem-rte-hermes-continuity"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-trace-archive"
        - "epistemic.md#epi-rte-reflect-notes"
        - "memory.md#mem-rte-note-withdrawal"
        - "runtime.md#rt-rte-note-materialization"
        - "memory.md#mem-obj-graph-publication"
      note: "Implemented consolidation, evolution and age forgetting coexist with claimed history-preserving invalidation. No supported novelty test establishes synthesize; replay accounting and similar-note advice do not establish dedup. Remaining transformations prevent complete coverage."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested note/graph reads and explicit Pi/Hermes recall"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-reload"
                - "runtime.md#rt-rte-context-build"
                - "runtime.md#rt-rte-pi-checkpoint"
                - "memory.md#mem-rte-hermes-continuity"
              note: "Consumers request identifiers, graph context or query-based previews; returning that requested selection remains pull."
          records:
            - "memory.md#mem-rte-note-reload"
            - "runtime.md#rt-rte-context-build"
            - "runtime.md#rt-rte-pi-checkpoint"
            - "memory.md#mem-rte-hermes-continuity"
          note: "These are established requested operations, not proof of every alternative reader."
        - scope: "Pi direct automatic recall and Python hook session briefs"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
                - "runtime.md#rt-bap-recall-data"
              note: "Eligible agent/session-start callbacks automatically select prior checkpoint/task/decision context and supply host output without a request for those notes."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "runtime.md#rt-rte-hook-checkpoint"
            - "runtime.md#rt-bap-recall-data"
          note: "Automatic selection is distinct from explicit recall commands within the same integrations."
        - scope: "Tau orientation and post-compaction supply chain"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Orient/read operations request a saved body or graph context; underlying MCP reads fulfill those requests."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Lifecycle orientation/post-compaction machinery supplies selected recall or checkpoint pointers to the host."
          records:
            - "memory.md#mem-rte-tau-handoff"
          note: "The internal requested read and outer automatic context supply are distinct operations, not double-counted delivery."
        - scope: "OpenClaw bootstrap and later assemble"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-openclaw-context"
              note: "Bootstrap selects tasks/recent activity and later assemble supplies cached recall as systemPromptAddition."
          records:
            - "memory.md#mem-rte-openclaw-context"
          note: "Automatic retained-context selection is push even though underlying search calls return requested rows."
        - scope: "Tau previous-handoff update input, archive replay keys and sync/recovery reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-rte-trace-archive"
                - "runtime.md#rt-rte-note-materialization"
              note: "Later synthesis/recovery/flush consumers explicitly load retained handoffs or metadata for their operations."
          records:
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-rte-trace-archive"
            - "runtime.md#rt-rte-note-materialization"
          note: "Read-back includes later deterministic consumers; not every archive is read by a model."
        - scope: "Stored QA case rejudging"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-qa-judge"
              note: "Rejudge explicitly receives stored cases and preserves their generated answers for a new verdict."
          records:
            - "epistemic.md#epi-rte-qa-judge"
          note: "No untraced production injection or artifact-file path is assumed."
        - scope: "Hermes outer injection, OpenClaw child-note readers, alternate tools, cloud/provider and evaluator consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-hermes-continuity"
            - "memory.md#mem-rte-openclaw-context"
            - "memory.md#mem-rte-note-reload"
            - "epistemic.md#epi-obj-qa-case"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Known pull and push witnesses do not resolve the incomplete outer-host and alternative consumer inventory."
      records:
        - "memory.md#mem-rte-note-reload"
        - "runtime.md#rt-rte-context-build"
        - "runtime.md#rt-rte-pi-checkpoint"
        - "memory.md#mem-rte-hermes-continuity"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "runtime.md#rt-bap-recall-data"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-rte-trace-archive"
        - "runtime.md#rt-rte-note-materialization"
        - "epistemic.md#epi-rte-qa-judge"
        - "epistemic.md#epi-obj-qa-case"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Both requested retrieval and automatic host supply are wired. Unresolved read-back alternatives remain included; known pull routes do not turn the signal axis inapplicable."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Pi direct before-agent-start checkpoint push"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
              note: "Trigger is first eligible agent start; project/type/timeframe eligibility and five-hit/500-character budgets filter the retained checkpoints."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
          note: "The current prompt or fallback query drives search, but the records leave ranking/provider behavior uninspected. Query presence alone does not resolve lexical versus embedding or judgment selection."
        - scope: "Python hook session-start brief push"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-checkpoint"
              note: "Session-start selects fixed active-task/open-decision/profile-session classes and caps merged session results."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-checkpoint"
              note: "Repository-scoped coding-session selection uses repository identity when available to select retained session parts."
          records:
            - "runtime.md#rt-rte-hook-checkpoint"
          note: "Memory annotation supplies the task/decision/session queries and repository scope; other adapters and exact search internals remain incomplete."
        - scope: "Tau orientation and successful-compaction pointer push"
          assessment: "partial"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
                - "memory.md#mem-obj-capture-record"
              note: "Active persisted branch and confirmed capture identity select the checkpoint body/pointer delivered to the host."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Profile/project/status and recall-character limits select/filter additional retained work, tasks and decisions."
          records:
            - "memory.md#mem-rte-tau-handoff"
            - "memory.md#mem-obj-capture-record"
          note: "Identity selection is actual branch-to-capture selection, not merely an identifier printed on a note. Topic discovery search details and complete placement policy remain unresolved."
        - scope: "OpenClaw bootstrap recall push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-openclaw-context"
              note: "Bootstrap trigger selects active Task hits and one-day recent activity, then clips task previews and caps recall at 1200 characters."
          records:
            - "memory.md#mem-rte-openclaw-context"
          note: "Fixed class/status/time selection is coarse; no prompt-specific semantic selector is established here."
        - scope: "Hermes possible background delivery and other host/remote automatic supply"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-hermes-continuity"
            - "memory.md#mem-rte-openclaw-context"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "Outer Hermes context injection and alternative automatic consumers are incomplete; their selector inputs and selected retained parts cannot be exhaustively classified."
      records:
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-obj-capture-record"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-rte-hermes-continuity"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Signals characterize automatic push selection only. Prompt query, identity match and coarse eligibility remain distinct; underlying requested reads and catalog identifiers do not themselves establish a push signal."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Pi direct and Python hook durable checkpoints with later recall"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
                - "runtime.md#rt-rte-hook-checkpoint"
                - "runtime.md#rt-bap-recall-data"
              note: "Automatic session-text extraction writes durable continuation notes that later session/agent-start consumers receive."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
            - "runtime.md#rt-rte-hook-checkpoint"
            - "runtime.md#rt-bap-recall-data"
          note: "A wired trace-fed durable context route qualifies even without parameter training, semantic novelty or observed benefit."
        - scope: "Tau incremental handoff with subsequent summary/orient consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Automatic public-session summarization persists handoffs read by later orientation and by subsequent handoff updates."
          records:
            - "memory.md#mem-rte-tau-handoff"
          note: "The external model is opaque; the trace-to-durable-handoff-to-later-consumer chain is wired."
        - scope: "Hermes extractive summary/session notes with later prefetch"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hermes-continuity"
              note: "Enabled session capture and endpoint-summary writes produce durable session context available to later query prefetch."
          records:
            - "memory.md#mem-rte-hermes-continuity"
          note: "The code-wired later search/preview path qualifies without guaranteeing selection of a particular note or outer-host use."
        - scope: "Prescribed reflection of recorded experience"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-notes"
              note: "The assistant is directed to turn retained meeting/daily/capture/transcript experience into durable lessons/preferences and a next-reflection checkpoint without per-item approval."
          records:
            - "epistemic.md#epi-rte-reflect-notes"
          note: "Claimed trace-fed behavior-shaping output is not an implemented scheduler or observed learning benefit."
        - scope: "OpenClaw daily conversation and child handoff learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-openclaw-context"
          note: "Automatic trace writes are wired, but bootstrap reads tasks/recent titles rather than conversation bodies and a child handoff reader is not established. Tools afford access without completing every qualifying later-consumer chain."
        - scope: "Raw archive alternatives, generic imported traces, provider updates and evaluator-to-policy routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-archive"
            - "runtime.md#rt-rte-note-write"
            - "epistemic.md#epi-obj-qa-case"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "The inspected raw sweep is bookkeeping, not a behavior-shaping update; broader archive readers, generic content origins and further automatic update consumers remain uninspected. No system-wide no is warranted."
      records:
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "runtime.md#rt-bap-recall-data"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "epistemic.md#epi-rte-reflect-notes"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-rte-trace-archive"
        - "runtime.md#rt-rte-note-write"
        - "epistemic.md#epi-obj-qa-case"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Positive trace-fed durable-context routes are local wired yes findings, independent of the reports’ unestablished improved-capacity learning property. Opaque and untraced writes remain unresolved rather than being classified no."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Pi direct checkpoint source"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-checkpoint"
              note: "Branch extraction consumes recorded user/assistant conversational turns; it excludes tool-role and nontext blocks."
          records:
            - "runtime.md#rt-rte-pi-checkpoint"
          note: "This is the original session content, not event-streams merely because a lifecycle callback triggers capture."
        - scope: "Python hook authored checkpoint source"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-checkpoint"
              note: "Pi payload turns and other harness transcript/user-message extraction feed the durable checkpoint."
          records:
            - "runtime.md#rt-rte-hook-checkpoint"
          note: "The checkpoint source is conversational text. Raw lifecycle envelopes are separate event metadata and do not add event-streams to this learning route."
        - scope: "Tau model handoff source"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tau-handoff"
              note: "Chunked public user/assistant entries, with prior trace-derived handoff context, feed incremental synthesis."
          records:
            - "memory.md#mem-rte-tau-handoff"
          note: "Hidden reasoning/tool-result frames are excluded by the inspected public-entry selection."
        - scope: "Hermes extractive continuity source"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hermes-continuity"
              note: "Recorded user/assistant turns supply appended session text and the first-user/last-assistant summary."
          records:
            - "memory.md#mem-rte-hermes-continuity"
          note: "No tool-trace or trajectory input is established by this formatter."
        - scope: "Reflection over mixed raw-note experience"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-reflect-notes"
          note: "The prescription includes meeting/daily/capture/transcript sources but does not individuate their original content sufficiently to distinguish agent session logs, event streams or other source kinds. Claimed trace-fed consolidation does not by itself resolve a controlled trace-source value."
        - scope: "OpenClaw and other unresolved qualifying writes, provider updates and mixed imported experience"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-openclaw-context"
            - "memory.md#mem-rte-trace-archive"
            - "runtime.md#rt-rte-note-write"
            - "runtime.md#rt-cmp-fastembed-provider"
            - "runtime.md#rt-cmp-openai-provider"
            - "runtime.md#rt-cmp-litellm-provider"
          note: "A raw lifecycle event is not a source of trace learning without a qualifying durable behavior-shaping write and later consumer. Mixed/imported inputs and unresolved routes prevent a complete source inventory."
      records:
        - "runtime.md#rt-rte-pi-checkpoint"
        - "runtime.md#rt-rte-hook-checkpoint"
        - "memory.md#mem-rte-tau-handoff"
        - "memory.md#mem-rte-hermes-continuity"
        - "epistemic.md#epi-rte-reflect-notes"
        - "memory.md#mem-rte-openclaw-context"
        - "memory.md#mem-rte-trace-archive"
        - "runtime.md#rt-rte-note-write"
        - "runtime.md#rt-cmp-fastembed-provider"
        - "runtime.md#rt-cmp-openai-provider"
        - "runtime.md#rt-cmp-litellm-provider"
      note: "Session-log positives follow the qualifying write routes. Callback labels do not add event-streams; absent captured tool-role inputs do not establish system-wide absence of tool-traces or trajectories. This axis is not inapplicable while qualifying positive and unresolved routes coexist."
---

# Basic Memory memory profile

## Comparison rationale

The profile classifies accepted source records, not a deployed configuration or an observed run. Every axis remains partial because the accepted inventory retains material alternatives whose control, storage, consumption or transformation is unresolved. A wired witness establishes its local path, not complete coverage. Provider inference components support the numerical embedding distinction, but do not establish accumulated provider-side memory or parameter learning.

The schema-report duplicate is resolved to [EPI-RTE-schema-validation](epistemic.md#epi-rte-schema-validation). This is the only reconciliation supersession affecting the classifications; the transient validation result is not itself a retained certificate. Stored schema criteria can supply validation authority without a write veto or factual endorsement.

The accepted [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint), [RT-RTE-hook-checkpoint](runtime.md#rt-rte-hook-checkpoint), [MEM-RTE-tau-handoff](memory.md#mem-rte-tau-handoff) and [MEM-RTE-hermes-continuity](memory.md#mem-rte-hermes-continuity) connect automatic trace-fed writes to later context consumption. They therefore support trace_learning yes even though the reports establish neither improved capacity nor successful self-improvement. Tau uses a model and prior handoff; Pi/Hermes use fixed extraction. Both can consolidate existing claims. The word synthesis does not establish creation of a claim absent from inputs. [EPI-RTE-reflect-notes](epistemic.md#epi-rte-reflect-notes) supports separate claimed consolidation/evolution/invalidation and a claimed trace-fed continuation, not wired execution.

Raw [MEM-RTE-trace-archive](memory.md#mem-rte-trace-archive) retains and rereads operational metadata, prunes by age, and counts replay keys. It neither merges duplicate knowledge nor establishes a promotion pipeline. [MEM-RTE-note-withdrawal](memory.md#mem-rte-note-withdrawal) deletes accepted state; only the separately prescribed archive/status path supports history-preserving invalidation. These distinctions prevent unsupported dedup or promote values.

The direction and signal axes split internal requested reads from automatic host supply. [MEM-RTE-openclaw-context](memory.md#mem-rte-openclaw-context) provides coarse task/recent-activity recall through systemPromptAddition; that channel alone does not turn retained reference content into instruction. Tau branch receipts actually select the pushed checkpoint; a requested note path alone would not establish identifier push. Pi prompt-driven search is recorded, but its query alone does not resolve lexical, embedding or model-judgment selection; that uncertainty remains beside the known coarse eligibility filters.

Retained reasons are local: Tau requests decisions and rationale and passes earlier handoffs to later synthesis; presence and faithfulness remain unobserved. Generic Markdown can carry reasons without requiring them. QA rejudging is a later consumer of stored cases, but the separately described benchmark file writer cannot be joined into a particular QA persistence or product-update loop. See [MEM-RTE-tau-handoff](memory.md#mem-rte-tau-handoff), [MEM-OBJ-markdown-content](memory.md#mem-obj-markdown-content) and [EPI-RTE-qa-judge](epistemic.md#epi-rte-qa-judge).

The storage classification of [MEM-OBJ-graph-publication](memory.md#mem-obj-graph-publication) covers published graph rows consumed by [RT-RTE-context-build](runtime.md#rt-rte-context-build), not the process-local prepared payload in the current mutation. Its retention into a later memory invocation is not established. That transient payload is excluded across the profile's classifications; retained graph and publication metadata remain included. The independent cross-invocation OpenClaw recall cache still supports in-memory storage through [MEM-RTE-openclaw-context](memory.md#mem-rte-openclaw-context).

Source-read log: no source checkout files were read. Classification used only the supplied accepted members and reconciliation. No records, quotations or execution evidence were added.
