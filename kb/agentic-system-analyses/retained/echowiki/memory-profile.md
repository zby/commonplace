---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "EchoWiki memory comparison for retained wiki content, acquisition files, editable guidance and access state at the frozen revision."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
source-identity: "https://github.com/mohammadmaso/echowiki"
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
memory-comparison:
  version: 2
  scope: "Retained raw notes/transcripts/audio; summary, concept and entity pages; descriptions, lineage fields, links, index and operation log; stored operator-edited AGENTS.md; persisted pending queue and operator configuration affecting admission/consumption; externally populated source/page/image/utility payload alternatives. Provider retention is unresolved, not presumed absent. Excludes static shipped instructions and fallback strings, current-call drafts/plans/task arrays, release artifacts, host rendering and model weights as computation components rather than established accumulated memory."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Raw acquisition files, wiki bodies/frontmatter/navigation/log, stored AGENTS.md and external utility payload files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents]
              note: "Vault/WikiStorage text and binary files and filesystem utility payloads establish files; wikilinks do not establish a separate graph store."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents]
          note: "The recorded local object inventory resolves substrate independently of actual content and host durability."
        - scope: "Persisted plugin queue and edited configuration"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings]
          note: "Saved plugin data and reload are established, but these records do not identify the host's physical storage substrate; do not substitute files or service-object by assumption."
        - scope: "Possible provider-retained state from chat/STT use"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Remote infrastructure and parameter mutation are opaque; neither an accumulated provider-memory object nor its substrate is established."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Files are supported throughout the local content inventory; host plugin-data substrate and possible provider retention prevent complete coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Raw text; retained summary/concept/entity bodies and descriptions; index/log prose; edited AGENTS.md; utility text"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents, runtime.md#rt-bap-retained-pages]
              note: "Prose receives consequences through human/model interpretation; Markdown serialization does not make its claims symbolic."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents]
          note: "Classification covers the readable prose parts, not opaque media or numerical provider state."
        - scope: "Parsed wikilinks, paths, lineage/type/source fields, catalog structure, log headers, pending entries and configuration fields"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, epistemic.md#epi-rte-link-check]
              note: "Localized identifiers and fields have fixed code consumers; model-visible entity type/count context remains a distinct consumption path."
          records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, epistemic.md#epi-rte-link-check]
          note: "Mixed files are split by operative part rather than classified wholesale."
        - scope: "Retained audio and helper-readable image payloads"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-sources]
          note: "Records establish opaque binary media only. Base64 is transport encoding, not evidence of symbolic or parametric consumption of the payload."
        - scope: "Possible accumulated provider payload/state"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Distributed-parametric computation components do not classify unknown accumulated provider memory."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Readable prose and fixed-rule access structures are resolved; opaque media and possible provider memory prevent a complete form union."
    lineage:
      assessment: partial
      units:
        - scope: "Generated page bodies/descriptions, code-managed lineage fields and catalog/link maintenance"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, epistemic.md#epi-rte-source-lineage]
              note: "Model generation and deterministic maintenance derive these retained parts from input text, prior pages and identifiers; input text is not established as a trace."
          records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index]
          note: "This unit covers the evidenced subsequent production path, not initial existing-page provenance."
        - scope: "Note-copy and STT transcript acquisition; optional instruction-template installation"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-raw, runtime.md#rt-rte-voice-ingest]
              note: "Copied note text and externally returned transcripts enter retained raw files without a factual acceptance check."
            - value: imported
              basis: afforded
              records: [runtime.md#rt-obj-agents, runtime.md#rt-rte-instruction-settings]
              note: "The optional user-installed template affords imported stored guidance; actual installation is not observed."
          records: [memory.md#mem-obj-raw, runtime.md#rt-rte-voice-ingest, runtime.md#rt-obj-agents, runtime.md#rt-rte-instruction-settings]
          note: "Known acquisition alternatives retain their different evidence layers; neither resolves actual installed content."
        - scope: "Explicit operator instruction and configuration edits"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents]
              note: "Operators supply edited guidance and configuration for subsequent loads; compilation does not author AGENTS.md."
          records: [runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents]
          note: "This classifies the edit route, not unknown initial instructions or human edits to actual pages."
        - scope: "Operation-log entries and event-detected pending path/time entries"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval]
              note: "Code retains coarse compilation activity and file-event identifiers/timestamps; trace lineage alone supplies no learning consumer."
          records: [memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval]
          note: "Recorded runtime activity supplies these entries, without retaining a conversation or measured knowledge outcome."
        - scope: "Initial existing wiki/raw/instruction content, audio content origin and external utility payloads"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-raw, memory.md#mem-obj-sources, runtime.md#rt-obj-agents]
          note: "Unknown external authorship/content origin prevents classifying initial objects as authored, imported or trace-derived solely from their location."
        - scope: "Possible provider-retained memory provenance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Provider retention and derivation were not inspected."
      records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-raw, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-page-metadata, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-voice-ingest, runtime.md#rt-rte-instruction-settings, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Known production/edit/acquisition paths coexist with unresolved initialization and opaque alternatives."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Prior page descriptions/previews and entity type/source-count context at the planning model"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-retained-selection, runtime.md#rt-bap-retained-pages, memory.md#mem-obj-page-metadata]
              note: "Briefs supply contextual information, not factual endorsement."
            - value: routing
              basis: wired
              records: [memory.md#mem-rte-retained-selection]
              note: "Retained briefs inform create/update/related operation and target choices through the model planner."
          records: [memory.md#mem-rte-retained-selection, runtime.md#rt-bap-retained-pages, memory.md#mem-obj-page-metadata]
          note: "This records the implemented selection channel, not observed dependence or a relative-priority scoring mechanism."
        - scope: "Selected prior bodies at update generation; raw text at subsequent compilation"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-retained-selection, memory.md#mem-obj-raw, runtime.md#rt-bap-retained-pages]
              note: "Retained content supplies source/context and continuity advice to generation; bodies are not system-role standing directions."
          records: [memory.md#mem-rte-retained-selection, memory.md#mem-obj-raw, runtime.md#rt-bap-retained-pages]
          note: "Known contextual authority does not imply preservation, truth or learned capacity."
        - scope: "Summary/index/page prose and navigation at documented human browsing"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-index, memory.md#mem-rte-page-maintenance]
              note: "Documented Obsidian browsing affords retained reference content; actual reading is unobserved."
          records: [memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-index]
          note: "Human reference use retains affordance strength rather than inheriting the compiler's wired strength."
        - scope: "Stored edited AGENTS.md at compilation models"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-obj-agents, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-rte-instruction-settings]
              note: "Reloaded prose supplies standing directions in system-role content, not an enforced conflict veto."
          records: [runtime.md#rt-obj-agents, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-rte-instruction-settings]
          note: "Consumer/channel/force are explicit; compliance and benefit remain unobserved."
        - scope: "Retained target identities at generated-link checking and cleanup"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-rte-retained-selection, epistemic.md#epi-rte-link-check]
              note: "Existing page names contribute admissible-target criteria; planned names also enter the current-call whitelist."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-link-check, epistemic.md#epi-rte-link-reshape]
              note: "Whitelist-relative rejection removes unrecognized link syntax, not unsupported factual assertions."
          records: [memory.md#mem-rte-retained-selection, epistemic.md#epi-rte-link-check, epistemic.md#epi-rte-link-reshape]
          note: "Retained identities contribute criteria with an enforced formatting effect; no eventual-existence guarantee follows."
        - scope: "Pending queue paths at approval UI/compile handoff and edited configuration at subsequent dispatch"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-instruction-settings]
              note: "Queue paths identify current files for approval/compilation; stored configuration selects services and compilation policy."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-watcher-approval]
              note: "The stored requireApproval setting gates watcher-triggered compilation only; manual/CLI bypass it."
          records: [runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-instruction-settings]
          note: "Routing/gating do not establish queue removal as a universal completion witness or failure-retention guarantee."
        - scope: "Log, opaque audio/images, external utility payloads and possible provider-retained state at unknown later consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-log, memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-raw, memory.md#mem-obj-sources, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Log-to-guidance is bounded absent; media and utility capabilities do not establish later memory consumers, and provider consumers are opaque. No ranking or learning authority is established for these alternatives."
      records: [memory.md#mem-rte-retained-selection, memory.md#mem-rte-page-maintenance, memory.md#mem-obj-page-metadata, memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-index, memory.md#mem-obj-log, memory.md#mem-obj-sources, memory.md#mem-abs-feedback-consumer, runtime.md#rt-obj-agents, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-bap-retained-pages, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-instruction-settings, epistemic.md#epi-rte-link-check, epistemic.md#epi-rte-link-reshape, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Authority is classified at actual local consumers; unspecified utility/media/provider consumption prevents a complete union."
    write_agency:
      assessment: partial
      units:
        - scope: "Page/description/frontmatter/link/index/log admission, watcher queue insertion/removal and returned transcript admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-voice-ingest]
              note: "Software/model admission retains these parts without per-content human approval. Starting compilation, approving a path or stopping a recording does not approve later generated content."
          records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-voice-ingest]
          note: "Human queue rejection is a separate upstream decision; physical persistence is not the admission classification."
        - scope: "Explicit note supply/copy, audio capture choice, queued input approval and operator guidance/configuration edits"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [memory.md#mem-obj-raw, runtime.md#rt-rte-voice-ingest, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-instruction-settings]
              note: "Operators explicitly supply or approve source material and edit stored guidance/configuration. Watcher approval is current-path input admission, not frozen-body or output approval."
          records: [memory.md#mem-obj-raw, runtime.md#rt-rte-voice-ingest, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-instruction-settings]
          note: "These human decisions coexist with automatic subsequent transcript and wiki admission."
        - scope: "Initial external wiki/raw/utility content and generic API/helper caller-supplied changes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-raw, memory.md#mem-obj-sources, runtime.md#rt-rte-document-compile, epistemic.md#epi-rte-helper-access]
          note: "Caller identity and file presence do not establish an operator per-content decision or autonomous caller admission."
        - scope: "Possible provider retention or parameter updates"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Remote admission/update control is uninspected."
      records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-raw, memory.md#mem-obj-concepts, memory.md#mem-obj-entities, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, runtime.md#rt-rte-voice-ingest, runtime.md#rt-rte-instruction-settings, runtime.md#rt-rte-document-compile, epistemic.md#epi-rte-helper-access, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Both automatic and manual mechanisms are supported, with initialization, generic callers and providers unresolved."
    curation_operations:
      assessment: partial
      units:
        - scope: "Brief fallback preview of retained page bodies for planning"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-retained-selection]
              note: "Flattening and limiting a retained body to a 150-character preview reduces its existing representation; the full file remains available for selected updates."
          records: [memory.md#mem-rte-retained-selection]
          note: "This is the inspected retained-content compression branch, not acquisition or an index rebuild."
        - scope: "Existing page/description/catalog revision and operator guidance/configuration replacement"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-index, runtime.md#rt-rte-instruction-settings]
              note: "Existing retained entries are revised/replaced by compiler maintenance or explicit operator edits; semantic preservation is not guaranteed."
          records: [memory.md#mem-rte-page-maintenance, memory.md#mem-obj-index, runtime.md#rt-rte-instruction-settings]
          note: "Whole replacement qualifies as revision, not invalidate, which requires history retention with withdrawn reliance."
        - scope: "Meaning-changing synthesis alternatives in model-generated/rewrite content"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-page-generate, epistemic.md#epi-rte-summary-rewrite, epistemic.md#epi-clm-cross-synthesis]
          note: "Cross-document synthesis is requested, but accepted records do not establish a new claim absent from inputs; semantic relation remains indeterminate. The request alone cannot establish synthesize."
        - scope: "Raw acquisition, append-only operation trace, queue lifecycle and standalone generic utility overwrites"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-log, runtime.md#rt-rte-watcher-approval, memory.md#mem-obj-sources]
          note: "These records establish acquisition, status append, completed/rejected-work removal or untyped writes, not a controlled retained-knowledge curation transformation. Queue removal is not source/claim withdrawal."
        - scope: "Possible provider-side retained-memory transformations"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Opaque provider updates prevent a complete operation inventory."
      records: [memory.md#mem-rte-retained-selection, memory.md#mem-rte-page-maintenance, memory.md#mem-obj-index, memory.md#mem-obj-raw, memory.md#mem-obj-log, memory.md#mem-obj-sources, runtime.md#rt-rte-instruction-settings, runtime.md#rt-rte-watcher-approval, epistemic.md#epi-rte-page-generate, epistemic.md#epi-rte-summary-rewrite, epistemic.md#epi-clm-cross-synthesis, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Compression and revision are wired; semantic novelty and opaque transformations remain unresolved. No dedup, decay, promote or history-preserving invalidation is inferred from route names or collisions."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Automatic context selection/delivery inside subsequent compilation and plugin reload"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-retained-selection, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings]
              note: "Code supplies all eligible briefs, selected update bodies, stored guidance/configuration and reloaded pending entries to their next consumers without those consumers requesting retained material. A compilation trigger is not itself such a request."
          records: [memory.md#mem-rte-retained-selection, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings]
          note: "The finite chain is workflow-triggered, not a continuously running unsolicited-memory service; automatic context supply still constitutes push at the consumer boundary."
        - scope: "Current raw-file reads on compile/preview request"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-raw, runtime.md#rt-rte-document-compile, runtime.md#rt-rte-watcher-approval]
              note: "Compilation/preview requests a selected current file and the storage/host read returns that requested retained content."
          records: [memory.md#mem-obj-raw, runtime.md#rt-rte-document-compile, runtime.md#rt-rte-watcher-approval]
          note: "Returning the requested file is pull, not a second push merely because software delivers it."
        - scope: "Documented human browsing of retained summary/index/page/link material"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-obj-summaries, memory.md#mem-obj-index, memory.md#mem-rte-page-maintenance]
              note: "Opening the index, graph and linked pages requests retained reference material; actual browsing is unobserved."
          records: [memory.md#mem-obj-summaries, memory.md#mem-obj-index, memory.md#mem-rte-page-maintenance]
          note: "Documented consumer role establishes affordance, not observed operation."
        - scope: "External utility/media/log consumers and possible provider-memory consumption"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-sources, memory.md#mem-obj-log, memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-raw, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Utility read capabilities do not establish a later invocation consuming accumulated content; log-to-compiler feedback is absent locally; provider alternatives remain opaque."
      records: [memory.md#mem-rte-retained-selection, memory.md#mem-obj-raw, memory.md#mem-obj-summaries, memory.md#mem-obj-index, memory.md#mem-rte-page-maintenance, memory.md#mem-obj-sources, memory.md#mem-obj-log, memory.md#mem-abs-feedback-consumer, runtime.md#rt-bap-compiler-instructions, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, runtime.md#rt-rte-document-compile, runtime.md#rt-rte-watcher-approval, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Request fulfillment and automatic context supply are different operations within the triggered workflow. Both are supported; unresolved consumers prevent a complete inventory."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Compile-triggered brief enumeration and stored instruction/configuration/plugin-queue reload"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-retained-selection, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings]
              note: "Compile/load is the trigger; folder/extension eligibility or stored-file/data availability selects all eligible briefs or the stored state. Description fallback and 150-character previews are not targeted similarity selection."
          records: [memory.md#mem-rte-retained-selection, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings]
          note: "Stored AGENTS.md availability selects guidance, not an identity match selecting among knowledge entries."
        - scope: "Planner selection of retained update targets and code resolution of those targets into delivered old bodies"
          assessment: known
          findings:
            - value: inferred-judgment
              basis: wired
              records: [memory.md#mem-rte-retained-selection]
              note: "On compilation, the planning model consumes current source/summary and retained briefs to choose update entries whose old bodies are delivered to generation."
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-retained-selection]
              note: "The selected name is sanitized into a concept/entity path and matched to the file whose body is supplied to the corresponding update task; missing pages get a placeholder, not fabricated retained content."
          records: [memory.md#mem-rte-retained-selection]
          note: "Judgment selects targets and exact path resolution selects delivered bodies; an identifier merely appearing in a catalog would not establish this signal."
        - scope: "Requested raw reads and documented human browsing"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-raw, runtime.md#rt-rte-document-compile, runtime.md#rt-rte-watcher-approval, memory.md#mem-obj-index, memory.md#mem-obj-summaries]
          note: "These operations fulfill retained-material requests; a requested path/link is not a push signal."
        - scope: "Potential external utility/media/provider push alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-sources, memory.md#mem-obj-raw, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "No established later consumer/selector resolves whether push exists here or which controlled signal would apply."
      records: [memory.md#mem-rte-retained-selection, runtime.md#rt-obj-agents, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-instruction-settings, memory.md#mem-obj-raw, runtime.md#rt-rte-document-compile, runtime.md#rt-rte-watcher-approval, memory.md#mem-obj-index, memory.md#mem-obj-summaries, memory.md#mem-obj-sources, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "Known automatic supply has coarse, judgment and identifier selectors at distinct stages. Unresolved alternatives prevent making the axis wholly inapplicable or known."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Operation-log/quality-result feedback into subsequent compiler guidance"
          assessment: known
          findings:
            - value: "no"
              basis: wired
              records: [memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-log]
              note: "The append route has no later log-to-guidance or quality-result admission consumer in the searched shipped loop; the bounded absence record warrants this local negative."
          records: [memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-log]
          note: "Complete classification of this bounded feedback route is no, not a system-wide absence of trace learning."
        - scope: "Pending event path/time queue to later approval UI and routing"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval]
          note: "Event metadata is retained access state for pending work, not a learned-parameter or derived behavior-shaping content update. This boundary reason establishes inapplicability, not a separate evidenced absence."
        - scope: "Automatic source-to-page/description updates with later planning/update consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw, memory.md#mem-rte-page-maintenance, memory.md#mem-rte-retained-selection, epistemic.md#epi-obj-source-content]
          note: "Durable generation and later contextual use are wired, but notes/transcripts are not established as activity/experience traces by content and origin. Neither yes nor a universal no follows."
        - scope: "Explicit operator instruction/configuration edits"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents]
          note: "These retained updates are manual, not automatic trace-fed writes; the compiler does not revise its own instructions."
        - scope: "External utility writers and possible provider updates"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-sources, epistemic.md#epi-rte-helper-access, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Caller control, input origin, later consumer and provider retention/update internals are unresolved; no qualifying trace-fed chain is established."
      records: [memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, memory.md#mem-obj-raw, memory.md#mem-rte-page-maintenance, memory.md#mem-rte-retained-selection, epistemic.md#epi-obj-source-content, runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents, memory.md#mem-obj-sources, epistemic.md#epi-rte-helper-access, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "A local log-feedback no is supported by bounded absence, while source origin and external/provider routes remain unresolved. This is not a system-wide no or an assessment of improved capacity."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Operation-log feedback and pending queue mechanisms"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval]
          note: "Neither mechanism establishes a qualifying trace-learning write. The existence of timestamped events/log entries does not by itself classify a learning source."
        - scope: "Source-to-retained-page updates and later consumption"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw, memory.md#mem-rte-page-maintenance, memory.md#mem-rte-retained-selection, epistemic.md#epi-obj-source-content]
          note: "Source is generic note/transcript text, without recorded activity/experience origin. Voice capture is not evidence of timestamped voice cues used as an event-stream learning source; transcript does not imply agent session-log."
        - scope: "Manual instruction/configuration edits"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents]
          note: "No automatic trace-fed update occurs on this manual edit route. Imported static guidance establishes lineage only."
        - scope: "External helper inputs and possible provider update inputs"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-sources, epistemic.md#epi-rte-helper-access, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
          note: "Neither qualifying learning nor original input content is resolved, preventing any session-logs/tool-traces/event-streams/trajectories classification."
      records: [memory.md#mem-abs-feedback-consumer, memory.md#mem-obj-log, runtime.md#rt-obj-pending-queue, runtime.md#rt-rte-watcher-approval, memory.md#mem-obj-raw, memory.md#mem-rte-page-maintenance, memory.md#mem-rte-retained-selection, epistemic.md#epi-obj-source-content, runtime.md#rt-rte-instruction-settings, runtime.md#rt-obj-agents, memory.md#mem-obj-sources, epistemic.md#epi-rte-helper-access, runtime.md#rt-cmp-llm-model, runtime.md#rt-cmp-stt-model]
      note: "No controlled positive source value is established. Local inapplicability cannot settle the unresolved source-content and provider alternatives."
---

# EchoWiki memory profile

## Comparison rationale

The comparison covers accumulated content and its access state, not every storage or permission surface in the runtime. Stored operator edits belong to this boundary because later compilation reloads them. Static fallback instructions, current-call plans, task arrays and shipped model components do not become accumulated memory merely because they affect generation. Opaque provider retention remains an unresolved alternative; the records do not establish that its numerical computation state is a use-generated memory object. The local inventory is supported by [MEM-OBJ-raw](memory.md#mem-obj-raw), the page and metadata objects, [MEM-OBJ-index](memory.md#mem-obj-index), [MEM-OBJ-log](memory.md#mem-obj-log), [MEM-OBJ-sources](memory.md#mem-obj-sources), [RT-OBJ-agents](runtime.md#rt-obj-agents) and [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue).

Reconciliation supersedes EPI-RTE-page-consume with [MEM-RTE-retained-selection](memory.md#mem-rte-retained-selection). All comparison findings for that progression therefore cite the latter. The page objects and metadata remain distinct valid parts alongside the broader epistemic objects; no other supersession affects a value. No record is newly declared here.

Read-back is split at request, selection and delivery boundaries. The memory report calls the chain request-driven because a compilation starts it. That does not mean the planning or generation model requested retained context. Compiler code automatically enumerates briefs and supplies selected old bodies to those consumers. This supports push with coarse eligibility, planner judgment and target-path matching at their respective operations. The path match selects an actually delivered old body, unlike an identifier merely listed in a catalog. Conversely, preview/current-file reads and documented browsing fulfill requests and remain pull. These distinctions derive from [MEM-RTE-retained-selection](memory.md#mem-rte-retained-selection), [RT-RTE-document-compile](runtime.md#rt-rte-document-compile), [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) and [MEM-OBJ-index](memory.md#mem-obj-index), not an assumed query agent.

The planner's retained inputs supply knowledge and help route task choices. No accepted record establishes a relative-priority scoring mechanism, so no ranking value is added. Link validation and enforcement are narrower: retained names help form a whitelist and cleanup changes link syntax. Planned targets enter that whitelist too, so it is not a target-existence or truth guarantee ([EPI-RTE-link-check](epistemic.md#epi-rte-link-check), [EPI-RTE-link-reshape](epistemic.md#epi-rte-link-reshape)). Stored instructions have instruction authority, not an enforced manual-edit veto ([RT-BAP-compiler-instructions](runtime.md#rt-bap-compiler-instructions)).

Preview compression establishes consolidate on an inspected branch. Page and catalog replacement establish evolve, without asserting semantic preservation. The requested cross-document synthesis does not establish a claim absent from inputs; the accepted epistemic generation records retain an indeterminate semantic relation. Consequently synthesize is unresolved rather than inferred from the product's terminology ([MEM-RTE-page-maintenance](memory.md#mem-rte-page-maintenance), [EPI-RTE-page-generate](epistemic.md#epi-rte-page-generate), [EPI-RTE-summary-rewrite](epistemic.md#epi-rte-summary-rewrite)). Source pointers do not establish a populated archive or evidence recovery ([MEM-OBJ-sources](memory.md#mem-obj-sources), [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata)).

Automatic page admission and later use are established, but the original source text is not established as traces. Generic voice transcripts do not imply agent session logs or event-stream cues. This prevents either a positive trace-learning route or a complete negative. Log-to-guidance absence stays local, while event-derived pending entries route work without learning from it. Trace lineage for these access/status entries does not imply trace learning ([MEM-ABS-feedback-consumer](memory.md#mem-abs-feedback-consumer), [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue), [MEM-OBJ-raw](memory.md#mem-obj-raw)).

The reconciliation's failure-retention conflict does not prevent the queue's symbolic form, automatic insertion, routing and reload classifications. It does prevent a universal retry-retention or queue-removal-as-delivery conclusion. Neither is asserted here: the [workflow annotation](workflow.md#annotations) limits the sequential account when another approval returns early on an in-flight path. No classification depends on selecting one report's stronger guarantee.

All positive evidence is wiring or documented affordance. No observed run or causal result is supplied. Initial page/source provenance, unspecified helper callers, opaque media consumption and provider state prevent stronger coverage assessments. This profile does not reopen verification or infer quality, activated learning or improved capacity from persistence.

Source-read log: none. Classification used only the supplied members and their accepted records; no target source file was opened.
