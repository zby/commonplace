---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "OpenViking memory profile of retained session context, derived memory, policy files, access structures and selected shipped consumers at a partial-loop boundary."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
source-identity: "https://github.com/volcengine/OpenViking"
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
memory-comparison:
  version: 2
  scope: "Retained raw session archives and externalized tool results; archive overviews and cumulative/legacy checkpoints; ordinary memory, case, trajectory, experience and skill files; their vectors, abstracts and symbolic metadata; recall ledger and OpenCode capture/retry state; write, maintenance, extraction and selected OpenCode/VikingBot consumption routes. Resource processing, alternate admission, snapshot/batch variants, bot local files and other shipped consumers remain included with unresolved coverage. Excludes transient query plans and recall digests as new memory objects, static shipped prompts/schemas, provider weights and third-party host scheduling. Runtime settings are not substituted for the retained-memory boundary."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Session raw archives, overviews and checkpoint metadata"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint]
              note: "VikingFS/AGFS archive files retain messages, derived text and metadata; a filesystem service does not turn file objects into service-object storage."
          records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint]
          note: "Covers the recorded archive parts, including cumulative and legacy checkpoint metadata, not native backend internals."
        - scope: "Externalized tool payload and synopsis/reference fields"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-tool-result]
              note: "Raw payload is a ToolResultStore file; message fields retain its reduced representation. Payload encoding is independent of its file substrate."
          records: [memory.md#mem-obj-tool-result]
          note: "Opaque payload semantics do not obscure the inspected storage route."
        - scope: "Ordinary memory, case, trajectory and experience files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience]
              note: "Each recorded product is a persisted VikingFS memory file, including body and symbolic fields/links."
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience]
          note: "Policy snapshots used only in current computation are not a separate accumulated in-memory store. Optional snapshot retention remains unresolved below."
        - scope: "Processed skill package content and auxiliary files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-skill-admission]
              note: "The memory annotation records package content, auxiliary files and source metadata written by SkillProcessor."
          records: [runtime.md#rt-rte-skill-admission]
          note: "File storage is established even though auxiliary content and later invocation are not completely classified."
        - scope: "Memory index vectors, URI fields and abstracts"
          assessment: known
          findings:
            - value: vector
              basis: wired
              records: [memory.md#mem-obj-memory-index]
              note: "The configured vector backend holds embeddings and associated retrieval records."
          records: [memory.md#mem-obj-memory-index]
          note: "Backend engine identity and convergence are unresolved, but the recorded access substrate is vector storage."
        - scope: "RecallLedger and OpenCode session mapping/pending queue"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-recall-ledger, workflow.md#wf-rte-session-capture, runtime.md#rt-rte-plugin-recall]
              note: "The ledger is session JSON; captured state reloads from version-2 persistence and pending queue entries are JSON files."
          records: [memory.md#mem-obj-recall-ledger, workflow.md#wf-rte-session-capture, runtime.md#rt-rte-plugin-recall]
          note: "Recorded file persistence is distinct from deployment durability and full queue housekeeping."
        - scope: "VikingBot local MEMORY.md and HISTORY.md"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-rte-bot-recall]
              note: "The record establishes local persistent text-file read/write methods, not a complete current consumer loop."
          records: [memory.md#mem-rte-bot-recall]
          note: "Substrate is known; admission and subsequent use are not."
        - scope: "Remaining resource products, optional policy snapshots, native storage and alternate shipped memory paths"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-session-commit, runtime.md#rt-rte-skill-admission, memory.md#mem-rte-experience-maintenance, memory.md#mem-rte-resource-withdrawal, memory.md#mem-rte-bot-recall]
          note: "The records retain partial resource/processor, snapshot, native and bot-loop coverage. They do not enumerate every retained object or concrete storage alternative."
      records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-memory-file, memory.md#mem-obj-memory-index, workflow.md#wf-rte-session-capture, memory.md#mem-rte-experience-maintenance, memory.md#mem-rte-bot-recall]
      note: "Files and vector storage are supported witnesses, not an exhaustive substrate union for all included paths."
    representational_form:
      assessment: partial
      units:
        - scope: "Recorded conversational text, archive overview and checkpoint abstract consumed as model context"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-session-reconstruction]
              note: "Message and summary text is interpreted by later models; checkpoint mapping fields are classified separately."
          records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-session-reconstruction]
          note: "Covers readable context parts, not all embedded tool/media content."
        - scope: "Ordinary memory, case, trajectory and experience bodies and readable index abstracts"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-obj-memory-index]
              note: "Readable bodies supply model context, diagnostics or reusable instructions; readable abstracts support reranking/display."
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-obj-memory-index]
          note: "Mixed metadata and numerical index vectors are not folded into this text unit."
        - scope: "Archive controls, checkpoint anchors/source IDs, file fields/links, index identity fields, ledger and capture/retry metadata"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-obj-memory-index, memory.md#mem-obj-recall-ledger, workflow.md#wf-rte-session-capture]
              note: "Localized identifiers, versions, counters and status fields have code-defined consumers independent of prose interpretation."
          records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-obj-memory-index, memory.md#mem-obj-recall-ledger, workflow.md#wf-rte-session-capture]
          note: "Classifies recorded control/identity fields without claiming every field is consumed."
        - scope: "Dense memory-index embeddings at similarity retrieval"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-memory-index, runtime.md#rt-cmp-account-embedder, runtime.md#rt-rte-session-search]
              note: "Dense numerical representations distribute retrieval information across dimensions; these are index representations, not retained model weights."
          records: [memory.md#mem-obj-memory-index, runtime.md#rt-cmp-account-embedder, runtime.md#rt-rte-session-search]
          note: "The recorded dense-vector path establishes this form independently of exact model provenance."
        - scope: "Tool-result display synopsis and its integrity/location metadata"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-tool-result]
              note: "The display synopsis is readable text, not a classification of the stored raw payload."
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-tool-result, memory.md#mem-rte-tool-externalization]
              note: "Hash, reference, MIME type and source offset/limit fields drive integrity/location and hydration operations."
          records: [memory.md#mem-obj-tool-result, memory.md#mem-rte-tool-externalization]
          note: "Both known findings apply to the reduced representation; raw payload is a separate unresolved part."
        - scope: "Hydrated original tool payloads and skill auxiliary code/opaque files"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-tool-result, runtime.md#rt-rte-skill-admission]
          note: "Recorded alternatives include natural-language, symbolic and opaque encoded tool outputs and auxiliary skill files; display text cannot establish the consumed payload's form."
        - scope: "Skill instruction text at its recorded instruction-processing route"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-rte-skill-admission]
              note: "Trace-to-skill admission retains reusable instruction text, distinct from its auxiliary payloads."
          records: [runtime.md#rt-rte-skill-admission]
          note: "This does not establish that every foreground host invoked the instructions."
        - scope: "Bot local file text, resource transformations and other untraced consumer payloads"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-bot-recall, memory.md#mem-rte-resource-withdrawal, memory.md#mem-rte-experience-maintenance]
          note: "Local text I/O and available alternatives do not establish all operative consumption paths or mixed payload forms."
      records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-memory-index, memory.md#mem-obj-tool-result, runtime.md#rt-rte-skill-admission, memory.md#mem-rte-bot-recall]
      note: "Natural-language, symbolic and parametric parts coexist; opaque and untraced payloads prevent complete coverage."
    lineage:
      assessment: partial
      units:
        - scope: "Captured session messages, tool results and OpenCode pending payloads at entry"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-tool-result, workflow.md#wf-rte-session-capture]
              note: "Host conversation/tool material enters retained stores; importing a raw trace is distinct from extracting its derived memory."
          records: [runtime.md#rt-obj-session-commit, memory.md#mem-obj-tool-result, workflow.md#wf-rte-session-capture]
          note: "Entry lineage is known, not the ultimate provenance or truth of every assertion/tool payload."
        - scope: "Archive overviews, checkpoint abstracts and ordinary session-derived memory"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-rte-session-reconstruction]
              note: "Models derive retained summaries/fields from archived or live session traces and prior retained context."
          records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-rte-session-reconstruction]
          note: "Known subsequent derivation does not resolve initial manual content, which remains separate below."
        - scope: "Session-derived cases, trajectory diagnostics, experience policies and session skills"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
              note: "Recorded session/rollout analysis and model operations produce these durable products."
          records: [memory.md#mem-obj-case, memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
          note: "This unit excludes the alternate first-message case protocol and imported skill installation."
        - scope: "Index abstracts and vectors derived from persisted memory"
          assessment: partial
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-memory-index]
              note: "Body reread, link stripping, truncation/template rendering and embedding submission compile an access representation from existing files."
          records: [memory.md#mem-obj-memory-index, runtime.md#rt-cmp-account-embedder]
          note: "Local compilation is established; exact embedding-model provenance and backend completion are not."
        - scope: "Ledger counters/URI entries, server-owned checkpoint anchors and capture/retry controls"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-recall-ledger, memory.md#mem-obj-checkpoint, workflow.md#wf-rte-session-capture]
              note: "Code constructs access/association state from served entries, owned anchors and capture/transmission outcomes, rather than model-extracting claims."
          records: [memory.md#mem-obj-recall-ledger, memory.md#mem-obj-checkpoint, workflow.md#wf-rte-session-capture]
          note: "This classification concerns generated bookkeeping, not the trace payload transported by it."
        - scope: "Caller-supplied initial memory, training-case fast path, skill uploads, resource products and bot local content"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, runtime.md#rt-rte-skill-admission, memory.md#mem-rte-bot-recall]
          note: "Caller-supplied content and alternative protocols exist, but complete initial derivation/authorship and resource transformation paths are not established. No blanket authored or trace-extracted value follows."
      records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-memory-index, memory.md#mem-obj-case, runtime.md#rt-rte-skill-admission, workflow.md#wf-rte-session-capture]
      note: "Imported raw inputs, trace-extracted products and compiled access structures are supported; initial and alternate provenance remains local uncertainty."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Memory and derived session text at later retrieval/planning and host-context consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-session-reconstruction, runtime.md#rt-rte-plugin-recall, runtime.md#rt-bap-recall-context, memory.md#mem-rte-bot-recall]
              note: "Selected text supplies context/reference to planning or host input, not enforced truth or compliance."
          records: [memory.md#mem-rte-session-reconstruction, runtime.md#rt-rte-plugin-recall, runtime.md#rt-bap-recall-context, memory.md#mem-rte-bot-recall]
          note: "Wired delivery is the authority path; actual useful interpretation remains unobserved."
        - scope: "Experience bodies at VikingBot reminder and schema-declared future instruction consumer"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-bap-experience-reminder, memory.md#mem-rte-bot-recall, epistemic.md#epi-obj-experience-instructions]
              note: "Retained reusable directions reach a user-role Experience Reminder; instruction authority follows content and consumer, not system-role placement."
            - value: instruction
              basis: claimed
              records: [epistemic.md#epi-obj-experience-instructions]
              note: "The schema requests system-prompt injection. This separate claimed channel is not upgraded by the wired user-role reminder."
          records: [memory.md#mem-bap-experience-reminder, memory.md#mem-rte-bot-recall, epistemic.md#epi-obj-experience-instructions]
          note: "Known channel-local classifications preserve the claimed/wired distinction, not a claim of universal host adoption."
        - scope: "Retained prior memory, trajectory diagnostics and experience/skill policy at update consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-rte-memory-application, memory.md#mem-rte-experience-maintenance, epistemic.md#epi-rte-policy-training, runtime.md#rt-rte-skill-admission]
              note: "Retained context, trajectories and policy feed durable memory/instruction revision or successor-policy planning. This force does not establish improved future capacity."
          records: [memory.md#mem-rte-memory-application, memory.md#mem-rte-experience-maintenance, epistemic.md#epi-rte-policy-training, runtime.md#rt-rte-skill-admission]
          note: "Update consumption is separate from output knowledge/instruction delivery and from the unresolved general learning property."
        - scope: "Index vectors, stored abstracts and case relevance at scored retrieval"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-memory-index, runtime.md#rt-rte-session-search, memory.md#mem-rte-bot-recall]
              note: "Retained embeddings and abstracts influence similarity/rerank priority; top-case selection uses relevance. Ranking does not require a learned retained ranking policy."
          records: [memory.md#mem-obj-memory-index, runtime.md#rt-rte-session-search, memory.md#mem-rte-bot-recall]
          note: "Filter-only find is a separate unranked branch, not evidence against the scored branch."
        - scope: "Terminal/archive/checkpoint controls, case links, tool refs and OpenCode association/retry state"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-session-commit, memory.md#mem-rte-session-reconstruction, memory.md#mem-obj-checkpoint, memory.md#mem-rte-tool-externalization, memory.md#mem-rte-bot-recall, workflow.md#wf-rte-session-capture]
              note: "Retained IDs/status/links select processing eligibility, source windows, linked experience input or replay/session destination."
          records: [runtime.md#rt-rte-session-commit, memory.md#mem-rte-session-reconstruction, memory.md#mem-obj-checkpoint, memory.md#mem-rte-tool-externalization, memory.md#mem-rte-bot-recall, workflow.md#wf-rte-session-capture]
          note: "Names actual control consumers; unconsumed provenance labels are not granted force."
        - scope: "Recall ledger URI/turn/detail state at server gather"
          assessment: known
          findings:
            - value: enforcement
              basis: wired
              records: [memory.md#mem-bap-ledger-selection, memory.md#mem-obj-recall-ledger]
              note: "The cooled-URI set excludes recent content from delivery under code rules; it is a bounded read veto, not a truth gate."
          records: [memory.md#mem-bap-ledger-selection, memory.md#mem-obj-recall-ledger]
          note: "Bare-URI, expired and malformed records have explicit exceptions; persistence failures weaken coverage rather than changing this local force."
        - scope: "Retained existing-file/link state at patch and replacement-delete checks"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [epistemic.md#epi-rte-memory-guards, epistemic.md#epi-rte-memory-withdrawal]
              note: "Existing content determines patch applicability; replacement/link state determines whether proposed deletion is admissible. Static schemas are outside this memory unit."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-memory-withdrawal]
              note: "Failed replacement/link migration can veto removal of retained source content."
          records: [epistemic.md#epi-rte-memory-guards, epistemic.md#epi-rte-memory-withdrawal]
          note: "Mechanical checks and vetoes are distinct from epistemic acceptance."
        - scope: "Full skill invocation, resource derivatives, bot local files and alternate host/batch consumers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-skill-admission, memory.md#mem-rte-bot-recall, memory.md#mem-rte-resource-withdrawal, epistemic.md#epi-rte-policy-training]
          note: "Readable skill text or a file method alone does not establish every actual downstream force; opaque payload effects and alternate consumers remain unresolved."
      records: [runtime.md#rt-bap-recall-context, memory.md#mem-bap-experience-reminder, memory.md#mem-bap-ledger-selection, memory.md#mem-obj-memory-index, epistemic.md#epi-rte-memory-withdrawal, epistemic.md#epi-rte-policy-training]
      note: "All seven authority values have local warrants; unresolved consumers prevent complete authority inventory and no finding proves compliance or benefit."
    write_agency:
      assessment: partial
      units:
        - scope: "Archive/capture/offload/checkpoint/overview admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-session-commit, memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-tool-externalization, workflow.md#wf-rte-session-capture]
              note: "Code/model processing retains captured traces and derived summaries under workflow rules, without a per-content human decision."
          records: [runtime.md#rt-rte-session-commit, memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-tool-externalization, workflow.md#wf-rte-session-capture]
          note: "A caller starting commit or a host scheduling compaction does not make subsequent admissions manual."
        - scope: "Ordinary memory application, compile proposals, experience and conditional skill updates"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-memory-application, epistemic.md#epi-rte-memory-consolidation, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
              note: "Models propose operations and software admits them; guards and errors are computational vetoes, not human approval."
          records: [memory.md#mem-rte-memory-application, epistemic.md#epi-rte-memory-consolidation, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
          note: "Covers inspected persistent branches; dry-run and generic batch updater alternatives are retained below."
        - scope: "Index update, recall-ledger record and automatic linked-memory cleanup"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-memory-index, memory.md#mem-obj-recall-ledger, memory.md#mem-rte-resource-withdrawal]
              note: "Successful writes, served entries and resource-removal events trigger software-controlled derivative bookkeeping or reference revision."
          records: [memory.md#mem-obj-memory-index, memory.md#mem-obj-recall-ledger, memory.md#mem-rte-resource-withdrawal]
          note: "The caller decision to remove the primary resource remains separate from computed downstream cleanup."
        - scope: "Initial/plain memory content, training-case fast path, skill/resource installs, primary explicit forgetting and bot local file writers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, runtime.md#rt-rte-skill-admission, memory.md#mem-rte-resource-withdrawal, memory.md#mem-rte-bot-recall]
          note: "Caller identity does not establish an explicit human content decision. A description requesting confirmation is not an enforced approval path; no manual finding is warranted."
        - scope: "Alternate resource/watch admission, policy snapshot/restore and batch updater variants"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-session-commit, memory.md#mem-rte-experience-maintenance, epistemic.md#epi-rte-policy-training]
          note: "Incomplete producer/admission coverage prevents extending the known automatic mechanisms to every included write."
      records: [memory.md#mem-rte-memory-application, memory.md#mem-rte-session-reconstruction, workflow.md#wf-rte-session-capture, memory.md#mem-rte-experience-maintenance, memory.md#mem-rte-bot-recall]
      note: "Automatic admission is supported on inspected routes; unresolved explicit and initial paths neither establish manual control nor its absence."
    curation_operations:
      assessment: partial
      units:
        - scope: "Archive overviews, checkpoints and ordinary standing-memory extraction"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-rte-session-reconstruction]
              note: "Retained trace content is compressed or selected into summaries/standing fields even when raw messages remain accessible. Semantic fidelity is not required for this operation classification."
          records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-obj-memory-file, memory.md#mem-rte-session-reconstruction]
          note: "This is a reduced existing-content representation, not evidence of a new claim or improved knowledge."
        - scope: "Existing memory and experience/skill files at actual replace/patch consumers"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-memory-application, epistemic.md#epi-rte-memory-write, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
              note: "The inspected updater revises retained fields/files and policy instructions; source-native gradients do not denote numerical weight optimization."
          records: [memory.md#mem-rte-memory-application, epistemic.md#epi-rte-memory-write, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
          note: "Revisions are implemented, while actual instances and their correctness are unobserved."
        - scope: "Explicit memory/skill/resource deletion at inspected removal mechanisms"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [epistemic.md#epi-rte-memory-withdrawal, memory.md#mem-rte-resource-withdrawal, runtime.md#rt-rte-skill-admission]
              note: "Successful filesystem/index removal forgets retained entries. This maps explicit forgetting, not a time-based decay rule or complete derivative revocation."
          records: [epistemic.md#epi-rte-memory-withdrawal, memory.md#mem-rte-resource-withdrawal, runtime.md#rt-rte-skill-admission]
          note: "Guards/bypass/partial failures bound the deletion routes; removal does not establish history-preserving invalidate."
        - scope: "Compile model's deduplication/consolidation objective"
          assessment: partial
          findings:
            - value: dedup
              basis: claimed
              records: [epistemic.md#epi-rte-memory-consolidation]
              note: "The provider explicitly requests deduplication of repeated/paraphrased facts. Actual duplicate removal is not established by the shared write executor."
          records: [epistemic.md#epi-rte-memory-consolidation]
          note: "The model's semantic transformation is not witnessed by candidate/output instances; route naming cannot upgrade the requested operation."
        - scope: "Tool synopsis semantics, trajectory/experience generalization and opaque resource/auxiliary transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-tool-externalization, memory.md#mem-rte-experience-maintenance, epistemic.md#epi-obj-experience-instructions, runtime.md#rt-rte-skill-admission]
          note: "Exact synopsis and policy content transformations are unresolved; abstraction or model use alone cannot establish synthesize, promote or another controlled operation. Known file revision remains in its own unit."
      records: [memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-memory-application, epistemic.md#epi-rte-memory-consolidation, epistemic.md#epi-rte-memory-withdrawal, memory.md#mem-rte-experience-maintenance]
      note: "Consolidation, revision and forgetting have inspected mechanisms; deduplication remains requested. Index rebuilds and recall cooling are not treated as semantic curation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested search/find/context returns, session reconstruction and explicit tool-result reload"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-session-search, runtime.md#rt-rte-direct-find, runtime.md#rt-rte-context-assembly, memory.md#mem-rte-session-reconstruction]
              note: "These operations fulfill consumer requests for retained context; internal scoring and response delivery do not add a second push."
            - value: pull
              basis: afforded
              records: [memory.md#mem-rte-tool-externalization]
              note: "Explicit tool-result read/search/list APIs afford targeted reload; the record does not establish all public callers."
          records: [runtime.md#rt-rte-session-search, runtime.md#rt-rte-direct-find, runtime.md#rt-rte-context-assembly, memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-tool-externalization]
          note: "Wired requested context and afforded optional reload retain their distinct bases."
        - scope: "OpenCode chat-hook recall and VikingBot query-time memory/reminder augmentation"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-plugin-recall, runtime.md#rt-bap-recall-context, memory.md#mem-rte-bot-recall, memory.md#mem-bap-experience-reminder]
              note: "Code automatically supplies retained context to the foreground input without a foreground request for that material. Upstream database requests remain pull."
          records: [runtime.md#rt-rte-plugin-recall, runtime.md#rt-bap-recall-context, memory.md#mem-rte-bot-recall, memory.md#mem-bap-experience-reminder]
          note: "Conditional on gates/host hooks; not a claim of deployment activation or universal automatic recall."
        - scope: "Extraction-only tool-payload hydration"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-tool-externalization]
              note: "Code restores retained raw/source-slice content into the prepared extraction copy automatically from captured references."
          records: [memory.md#mem-rte-tool-externalization]
          note: "Hydration failure leaves the stub; public explicit reload is separately pull."
        - scope: "Untraced bot local-file, full skill invocation, alternative host and generic training/executor delivery paths"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-bot-recall, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-policy-training]
          note: "Storage and generic successor flow do not enumerate every requested versus automatic consumer operation."
      records: [runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-plugin-recall, memory.md#mem-rte-bot-recall, memory.md#mem-rte-tool-externalization, epistemic.md#epi-rte-policy-training]
      note: "Both pull and push exist in different operations of the same chains; unresolved alternative consumers prevent complete coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "OpenCode automatic recall relevance chain"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-session-search, memory.md#mem-obj-memory-index, runtime.md#rt-rte-plugin-recall]
              note: "On a chat-message trigger, current user text supplies the query whose embedded similarity selects stored candidates for automatic delivery."
            - value: inferred-judgment
              basis: wired
              records: [runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-plugin-recall, epistemic.md#epi-rte-digest-contract]
              note: "Optional expansion/rewrite interprets query/selected fragments and can choose a digest or no_relevant, changing which retained content reaches the hook output."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-plugin-recall, runtime.md#rt-rte-context-assembly]
              note: "Enabled/healthy/minimum-query/bypass gates and quota/token budgets determine availability or amount; they are separate from targeted relevance selection."
          records: [runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-plugin-recall, epistemic.md#epi-rte-digest-contract]
          note: "Covers the inspected automatic recall branch, not parallel session injection or every deployed callback."
        - scope: "VikingBot automatic case-to-experience and user-memory selection"
          assessment: partial
          findings:
            - value: inferred-embedding
              basis: wired
              records: [memory.md#mem-rte-bot-recall, runtime.md#rt-rte-session-search, memory.md#mem-obj-memory-index]
              note: "The current query drives semantic search of retained memory/cases before automatic message augmentation."
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-bot-recall, memory.md#mem-obj-case]
              note: "After top-case selection, stored links identify experience bodies to load and deliver in the reminder; actual link matching, not mere catalog IDs, supplies this signal."
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-bot-recall]
              note: "Flags, per-type quotas and character budgets gate and limit automatically supplied profiles/memory/experience bodies."
          records: [memory.md#mem-rte-bot-recall, memory.md#mem-obj-case, memory.md#mem-obj-memory-index]
          note: "The explicit exact-case lookup and complete profile/skill loading are not fully audited; these alternatives remain unresolved within the unit."
        - scope: "Automatic extraction hydration of retained tool output"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-tool-externalization, memory.md#mem-obj-tool-result]
              note: "At extraction preparation, a retained ref/source-ref selects the raw tool file or identified source slice restored into model input."
          records: [memory.md#mem-rte-tool-externalization, memory.md#mem-obj-tool-result]
          note: "Reference/truncation flags gate hydration; the payload identity and offset/limit actually select supplied material."
        - scope: "Requested search/find/session returns and explicit tool-result reload"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-session-search, runtime.md#rt-rte-direct-find, memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-tool-externalization]
          note: "These bounded operations are pull; their URI/anchor, lexical or relevance selectors do not establish a push signal merely by selecting a requested return."
        - scope: "Untraced parallel session injection, bot local-file, skill and other host/training consumers"
          assessment: uninspected
          findings: []
          records: [workflow.md#wf-rte-session-capture, runtime.md#rt-rte-plugin-recall, memory.md#mem-rte-bot-recall, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-policy-training]
          note: "The reports leave these delivery/payload paths incomplete; one known pull route cannot make unresolved alternative push selection inapplicable."
      records: [runtime.md#rt-rte-plugin-recall, runtime.md#rt-rte-context-assembly, memory.md#mem-rte-bot-recall, memory.md#mem-rte-tool-externalization, epistemic.md#epi-rte-policy-training]
      note: "Coarse, embedding, judgment and actual identifier selection have route-local warrants. Lexical retrieval on a requested route is not promoted into a push-signal finding."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic archive overview/checkpoint production followed by session/search consumption"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-session-reconstruction]
              note: "Traces feed automatically retained continuation summaries; later model context/planning consumes them. This qualifies without new knowledge or measured benefit."
          records: [memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-session-reconstruction]
          note: "Includes the recorded cumulative and legacy summary consumer branches, not a guarantee of faithful continuity."
        - scope: "Session-derived ordinary memory/case files followed by retrieval or later extraction"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-rte-memory-application, memory.md#mem-rte-bot-recall]
              note: "Automatic trace-fed writes produce durable context/routing artifacts with later consumers; retaining the raw archive alone would not suffice."
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-rte-memory-application, memory.md#mem-rte-bot-recall]
          note: "Covers ordinary session producers; initial content and training-case fast path remain unresolved below."
        - scope: "Trace-to-trajectory/experience and conditional session-skill maintenance"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-policy-training]
              note: "Automatic diagnostic/policy writes persist across sessions or batches and feed later estimation, policy loading or selected reminder context. Skills reenter future policy sets even without observed host invocation."
          records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-experience, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-policy-training]
          note: "This write-route classification is independent of the reports' uninspected improved-capacity, reflection or theory-builder properties."
        - scope: "Raw trace/offload/index/bookkeeping routes as independent learning mechanisms"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-tool-externalization, memory.md#mem-obj-memory-index, memory.md#mem-obj-recall-ledger, workflow.md#wf-rte-session-capture]
          note: "These parts participate in qualifying chains, but the records do not completely establish distinct behavior-shaping learning writes or a bounded absence for every offload/selector alternative. No system-wide or local no is inferred from transport terminology."
        - scope: "Resource-derived producers, initial/manual memory, training-case fast path, bot local writers and alternate batch/snapshot variants"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-memory-file, memory.md#mem-obj-case, memory.md#mem-rte-experience-maintenance, memory.md#mem-rte-bot-recall, epistemic.md#epi-rte-policy-training]
          note: "Missing producer, persistent-updater or later-consumer facts prevent complete classification; dry-run policy snapshots are not silently treated as persisted learning."
      records: [memory.md#mem-rte-session-reconstruction, memory.md#mem-rte-memory-application, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-policy-training]
      note: "Qualifying wired trace-fed writes exist; no bounded absence records support no, and alternative writes prevent a complete assessment."
    trace_source:
      assessment: partial
      units:
        - scope: "Overview/checkpoint and ordinary session-memory writes from conversational turns"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [runtime.md#rt-rte-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-memory-application]
              note: "Recorded user/assistant turns from agent sessions feed summaries and standing-memory extraction; user messages count without treating their assertions as verified."
          records: [runtime.md#rt-rte-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-obj-checkpoint, memory.md#mem-rte-memory-application]
          note: "This unit classifies the conversational portion; hydrated tool input is separate."
        - scope: "Hydrated tool requests/results in qualifying session extraction and overview generation"
          assessment: partial
          findings:
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-tool-result, memory.md#mem-rte-tool-externalization, memory.md#mem-obj-archive-overview, runtime.md#rt-rte-session-commit]
              note: "Captured ToolPart output can be restored into extraction input, and overview lineage includes hydrated tool outputs. Original source content is tool activity, not the synopsis label."
          records: [memory.md#mem-obj-tool-result, memory.md#mem-rte-tool-externalization, memory.md#mem-obj-archive-overview]
          note: "Tool content may be opaque/mixed or an existing-source slice; the records do not enumerate additional original source classes or guarantee successful hydration."
        - scope: "Session-rollout trajectory/experience and skill writes"
          assessment: partial
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-trajectory, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission]
              note: "Session rollout messages feed diagnostic and reusable-policy extraction."
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-trajectory, memory.md#mem-rte-experience-maintenance]
              note: "Completed read-tool traces determine consumed-experience lineage in the diagnostic/experience chain."
          records: [memory.md#mem-obj-trajectory, memory.md#mem-rte-experience-maintenance, runtime.md#rt-rte-skill-admission, epistemic.md#epi-rte-rollout-feedback]
          note: "Optional evaluation inputs and external/offline rollouts have unresolved content/origin. A source-native trajectory object alone does not establish linked state/action/outcome trajectories as the original source class."
        - scope: "Other qualifying or potentially qualifying producers, external evaluation inputs and opaque imported/resource/bot paths"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-case, memory.md#mem-rte-experience-maintenance, memory.md#mem-rte-bot-recall, epistemic.md#epi-rte-rollout-feedback, epistemic.md#epi-rte-policy-training]
          note: "Missing provenance prevents complete original-source coverage. Host event callbacks that transport conversation do not themselves add event-streams; neither event-streams nor trajectories is inferred absent."
      records: [runtime.md#rt-rte-session-commit, memory.md#mem-obj-archive-overview, memory.md#mem-rte-tool-externalization, memory.md#mem-rte-experience-maintenance, epistemic.md#epi-rte-rollout-feedback, epistemic.md#epi-rte-policy-training]
      note: "Session logs and tool traces support qualifying writes. Mixed payloads and alternative producer/evaluator origins prevent a complete source union; trace source is not inapplicable in the presence of supported learning routes."
---

# OpenViking memory profile

## Comparison rationale

This profile classifies accepted records, not new source evidence. All ten axes remain partial because the recorded boundary retains unresolved included producers, payloads or consumers. A known unit covers its named part only. It does not resolve an alternative merely because the alternative shares a file format, updater or service endpoint.

The raw archive, derived overview, checkpoint, external tool payload and access metadata remain distinct parts. The valid container [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) is not replaced by [MEM-OBJ-archive-overview](memory.md#mem-obj-archive-overview) or [MEM-OBJ-checkpoint](memory.md#mem-obj-checkpoint). Reconciliation proposes no supersessions; therefore no value depends on replacing an ID. Likewise, memory assertion fields and experience instruction fields overlap file content without replacing the complete file/policy objects. Numerical index representations are parametric form on vector storage, not evidence of local weight learning: [MEM-OBJ-memory-index](memory.md#mem-obj-memory-index).

The memory boundary includes opaque tool and skill payloads. Their file substrate is known while their actual consumed form remains unresolved. A readable display synopsis does not classify a hydrated original: [MEM-OBJ-tool-result](memory.md#mem-obj-tool-result). Initial caller content and explicit administrative choices retain unresolved write agency. No manual classification follows from a route called manual, a generic caller, or a request to confirm forgetting: [MEM-RTE-resource-withdrawal](memory.md#mem-rte-resource-withdrawal). The corrected account-template account separates managed edits from persisted-template consumption. No embedding-template editing capability or blanket human-curated lineage is inferred from the index consumer.

Authority follows the actual retained part and consumer. File text supplies context; experience directions supply instruction; prior policy and trajectory content feed durable revision; embeddings/abstracts affect ranking; identifiers and status state route work; the ledger vetoes recent delivery; retained target/link content supplies mechanical validation and deletion vetoes. These forces do not establish truth acceptance, compliance or benefit. The schema's requested system-prompt channel remains claimed alongside the wired VikingBot user-role reminder: [EPI-OBJ-experience-instructions](epistemic.md#epi-obj-experience-instructions), [MEM-BAP-experience-reminder](memory.md#mem-bap-experience-reminder).

Curation follows implemented effects. Summary/standing-fact extraction consolidates, field replacement evolves, and successful removal forgets entries within the controlled decay meaning. Deletion does not by itself establish history-preserving invalidation or universal revocation. Compile explicitly requests deduplication, but its model-mediated semantic result is unobserved; that finding stays claimed rather than borrowing wiring from the physical updater: [EPI-RTE-memory-consolidation](epistemic.md#epi-rte-memory-consolidation). There is no supported synthesis finding merely because a model generalizes or because semantic preservation is unresolved.

Requested database returns are pull. Automatic host augmentation is push; both occur within one chain rather than competing as system-wide labels. Automatic hydration is a distinct identifier-selected supply into extraction input. OpenCode recall combines coarse gates/budgets, semantic candidate selection and optional model omission/rewrite. VikingBot's links actually select delivered experience bodies, unlike a bare URI in a catalog: [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall), [MEM-RTE-bot-recall](memory.md#mem-rte-bot-recall), [MEM-RTE-tool-externalization](memory.md#mem-rte-tool-externalization). Requested session reconstruction does not become an additional push merely because code selects summaries or inserts anchor checkpoints.

Trace learning here means automatic trace-fed durable artifacts with later consumers, not demonstrated improvement. Continuation summaries qualify alongside standing memory and reusable policies. The reports' independent uninspected learning/theory/reflection conclusions do not negate this architectural write-route classification: [MEM-RTE-session-reconstruction](memory.md#mem-rte-session-reconstruction), [MEM-RTE-experience-maintenance](memory.md#mem-rte-experience-maintenance), [EPI-RTE-policy-training](epistemic.md#epi-rte-policy-training). Tool capture contributes tool-traces where it actually feeds those writes. Event callbacks transporting conversational messages do not create an event-stream source; a derived object named Trajectory does not establish the original linked state/action/outcome source class. Optional evaluator inputs and alternative producer paths retain uncertainty rather than being excluded to obtain a known union.

Source-read log: no source files were read. Classification uses only the supplied accepted records and their annotations, with reconciliation used to resolve identities. No evidence passages, analyst records or source facts were added.
