---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "MemoryOS accumulated dialogue, derived profile/fact memory and access structures across JSON, ChromaDB, MCP, Playground and evaluation."
run-id: "AAS-2026-10-16-memoryos-bb72a1b70e03-01"
source-identity: "https://github.com/BAI-LAB/MemoryOS"
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
memory-comparison:
  version: 2
  scope: "Accumulated recent dialogue, sessions/pages and summaries/overviews; user profiles and user/assistant facts; their dense indices and symbolic maintenance/access state; ChromaDB collections and separately persisted metadata; bundled MCP and Playground admission/read/clear routes; evaluation sample memories and retained answer/reference ledger. Includes initial-loaded/direct-update provenance uncertainty, uninspected ChromaDB index internals and remaining shipped driver/helper consumer coverage. Excludes shipped static prompts/source as memory, transient personality-display output, external provider/encoder weights and caches, and external MCP-host internal storage/behavior."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "JSON recent dialogue deque and session/page, profile, user/assistant knowledge stores, including MCP and Playground bundled JSON paths"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "JSON serialization/reload retains the dialogue and derived objects."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "Bounded deques and session dictionaries hold the operative state between saves."
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
            - "runtime.md#rt-rte-mcp-access"
            - "runtime.md#rt-rte-playground-control"
          note: "These operative objects are retained as JSON files and reloaded into process collections; files and process state are separate substrate findings."
        - scope: "JSON access structures: stored vectors, counters, flags, rebuilt FAISS indices and heat heap"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "JSON persists vectors and control metadata."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "The heap, counters and rebuilt search state operate in process."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "FAISS indices provide vector access to retained representations."
          records:
            - "memory.md#mem-obj-memory-access"
          note: "Dense encoding is not by itself a vector substrate; the operative FAISS index supplies that access substrate."
        - scope: "ChromaDB collections and separately saved short-term/profile/session metadata"
          assessment: "known"
          findings:
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Persistent collections retain and retrieve vectors plus dialogue/fact metadata."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Separate JSON metadata retains profiles, recent dialogue and session/control state on save."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Shared metadata/session dictionaries are operative before close."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Persistent vector collections and process metadata with JSON close/exit persistence are distinguished. No dependency-internal SQLite or other physical substrate is inferred."
        - scope: "Evaluation sample memory, selector state and retained answer/reference results"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "memory.md#mem-obj-loco-results"
              note: "Sample-specific JSON and all_loco_results.json are retained."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
              note: "Lists, session dictionaries and mutable search statistics operate in process."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Sample JSON memories and result files are distinct from product stores; operative lists and access state exist in process."
        - scope: "ChromaDB dependency-internal retained index details"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chroma-storage"
          note: "Vector collection existence is resolved above; internal organization was not inspected and cannot establish additional substrates."
      records:
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-obj-mid-term"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-user-knowledge"
        - "memory.md#mem-obj-assistant-knowledge"
        - "runtime.md#rt-rte-mcp-access"
        - "runtime.md#rt-rte-playground-control"
        - "memory.md#mem-obj-memory-access"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "memory.md#mem-obj-loco-results"
        - "runtime.md#rt-rte-locomo-evaluation"
      note: "The recorded operative inventory establishes files, process collections and vector access. Dependency internals remain unresolved; external model weights and static source repositories are not accumulated memory substrates here."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Original dialogue and derived summaries, chain overviews, profile and fact text at response/maintenance model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "Models interpret dialogue, summaries, traits and extracted statements as text."
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
          note: "Natural-language payloads are separate from their metadata and dense selectors."
        - scope: "JSON identity/time/link envelopes, heat/access counts, analyzed flags and heaps at fixed code consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-memory-access"
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-user-knowledge"
              note: "Keys, links, counters, flags and capacities determine fixed navigation and maintenance behavior."
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-memory-access"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
          note: "Localized metadata is consumed under fixed rules; textual JSON serialization does not make these fields natural-language content."
        - scope: "Dense session/page/knowledge embeddings at similarity consumers"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "Dense embeddings spread selection information across numerical dimensions."
          records:
            - "memory.md#mem-obj-memory-access"
          note: "The numerical representations are distributed-parametric form, not trained memory-model parameters."
        - scope: "ChromaDB dialogue, fact and profile payloads at model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Original/derived text is delivered as context; wrapped profiles can retain raw text."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Raw vector-page dialogue remains readable. Initial-page backup overviews are not delivered after overwrite; surviving merged backups can supply them."
        - scope: "ChromaDB bookkeeping and dense collection representations at code selectors"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Session IDs, timestamps, flags and access state govern fixed code paths."
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Dense collection embeddings drive semantic selection."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "String-converted metadata still carries symbolic fields; collection vectors remain distributed numerical representations."
        - scope: "Evaluation dialogue/profile/fact and answer/reference text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "memory.md#mem-obj-loco-results"
              note: "Retained text supplies answer context and later lexical comparison."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "memory.md#mem-obj-loco-results"
          note: "The scorer consumes text lexically; it does not make the stored questions and answers nonlinguistic."
        - scope: "Evaluation metadata and dense retrieval representations"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "memory.md#mem-obj-loco-results"
              note: "IDs, links, counters and result categories are fixed-rule fields."
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
              note: "Dense embeddings select sessions and pages."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "memory.md#mem-obj-loco-results"
          note: "Sample/category envelopes and selector representations have distinct operative forms."
        - scope: "Dependency-internal ChromaDB access representation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chroma-storage"
          note: "The inspected collection interface does not enumerate every internal retained representation."
      records:
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-obj-mid-term"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-user-knowledge"
        - "memory.md#mem-obj-assistant-knowledge"
        - "memory.md#mem-obj-memory-access"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "memory.md#mem-obj-loco-results"
      note: "The recorded text, symbolic control fields and dense selectors are all retained. Dependency index details prevent claiming exhaustive internal form coverage; transient personality display assignments and static prompts are excluded."
    lineage:
      assessment: "partial"
      units:
        - scope: "Newly admitted caller/imported dialogue and existing file-loaded content"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "runtime.md#rt-rte-memory-admission"
                - "runtime.md#rt-rte-playground-control"
              note: "Caller-supplied exchanges and Playground imported exchanges enter retained stores."
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
            - "runtime.md#rt-rte-memory-admission"
            - "runtime.md#rt-rte-playground-control"
          note: "The known import path does not resolve initial content authorship, authenticity or the derivation of loaded profiles/vectors."
        - scope: "Generated exchanges, dialogue-derived summaries/overviews and extracted profiles/facts"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-admission"
                - "runtime.md#rt-rte-profile-analysis"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "Recorded exchanges feed summaries, continuity overviews, profile revision and fact extraction."
          records:
            - "runtime.md#rt-rte-memory-admission"
            - "runtime.md#rt-rte-profile-analysis"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
          note: "The raw-to-derived paths are implemented, independently of semantic faithfulness or successful operation."
        - scope: "Embeddings, access counts, heat, analyzed flags and rebuilt selectors"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "Encoders and fixed code derive access representations and maintenance state."
          records:
            - "memory.md#mem-obj-memory-access"
          note: "Generated embeddings compile text into selectors; counters/flags compile access and processing activity. Initial loaded-vector provenance remains unresolved."
        - scope: "ChromaDB new-session and later-merge retained dialogue and derived state"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Overflow summary/continuity derives from dialogue; surviving merged pages can feed profile/fact derivation."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Embeddings and maintenance metadata derive from text and access activity."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "New-session vector dialogue survives subject to dependency success, but its overwritten backup cannot supply extraction. Later merged backup pages can supply extraction. Initial loaded content provenance remains unknown."
        - scope: "Evaluation imported conversations and their derived sample memory"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Dataset dialogue and captions are preprocessed into QA pages."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Conversation pages feed summaries, profiles and facts."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
              note: "Embeddings and access bookkeeping are computed for retrieval."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Dataset origin is established, not dataset validity or provenance of preexisting sample files."
        - scope: "Evaluation answer/reference result ledger"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-loco-results"
              note: "Dataset references enter the retained result envelope."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-loco-results"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Question/answer activity is recorded for later scoring."
          records:
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Generated answers and imported references coexist; source validity is not established."
        - scope: "Direct-update supplied profile/facts and initial ChromaDB payload/embedding origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-direct-update"
            - "memory.md#mem-obj-chroma-storage"
          note: "Generic caller identity and loaded storage do not establish human authorship or upstream derivation; no authored value follows."
      records:
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-obj-mid-term"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-user-knowledge"
        - "memory.md#mem-obj-assistant-knowledge"
        - "runtime.md#rt-rte-memory-admission"
        - "runtime.md#rt-rte-playground-control"
        - "runtime.md#rt-rte-profile-analysis"
        - "memory.md#mem-obj-memory-access"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-loco-results"
        - "memory.md#mem-rte-direct-update"
      note: "Known import, trace-derivation and compilation paths coexist with unresolved initialization and direct-update origins. No explicit per-content human authorship is established by these records."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Recent/history pages, overviews and user facts at response model"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-knowledge"
                - "runtime.md#rt-bap-user-context"
              note: "Response generation receives recent and recalled user/history material as context."
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-knowledge"
            - "runtime.md#rt-bap-user-context"
          note: "These are evidence/background context, not local truth checks or enforced commands."
        - scope: "User profile and assistant statements at response model"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-assistant-knowledge"
                - "runtime.md#rt-bap-user-context"
                - "runtime.md#rt-bap-assistant-context"
              note: "Profiles and assistant claims provide retained background/knowledge."
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-assistant-knowledge"
                - "runtime.md#rt-bap-user-context"
                - "runtime.md#rt-bap-assistant-context"
              note: "Retained preferences and system-message assistant traits guide later response behavior."
          records:
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-assistant-knowledge"
            - "runtime.md#rt-bap-user-context"
            - "runtime.md#rt-bap-assistant-context"
          note: "Trait/preference text supplies standing style/persona guidance as well as reference content; message position does not establish compliance."
        - scope: "Retained dialogue and old profile at summary/profile/fact update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-profiles"
                - "runtime.md#rt-rte-profile-analysis"
                - "runtime.md#rt-rte-memory-admission"
              note: "Retained experience and prior interpretations feed durable behavior-shaping summaries/profiles/facts."
          records:
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-profiles"
            - "runtime.md#rt-rte-profile-analysis"
            - "runtime.md#rt-rte-memory-admission"
          note: "The update consumer and the later answering consumer are distinct authority paths."
        - scope: "Retained summaries, page/fact content and embeddings at similarity ranking consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
                - "memory.md#mem-obj-memory-access"
                - "runtime.md#rt-rte-dialogue-response"
              note: "Retained representations affect relative retrieval priority and threshold selection."
          records:
            - "memory.md#mem-obj-mid-term"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
            - "memory.md#mem-obj-memory-access"
            - "runtime.md#rt-rte-dialogue-response"
          note: "Fixed ranking code does not remove the ranking authority of retained inputs."
        - scope: "Access/heat/analyzed state at LFU, heat selection and analysis eligibility consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "Visits/frequency/heat influence retention and analysis priority."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
                - "runtime.md#rt-rte-profile-analysis"
              note: "Heat and analyzed status select the session and input window for maintenance."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
                - "runtime.md#rt-rte-profile-analysis"
              note: "Analyzed flags suppress repeat extraction from marked pages."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
                - "runtime.md#rt-rte-profile-analysis"
              note: "The retained analyzed flag is checked as an eligibility criterion before pages enter extraction."
          records:
            - "memory.md#mem-obj-memory-access"
            - "runtime.md#rt-rte-profile-analysis"
          note: "Counters choose survival and next analysis input; analyzed flags exclude previously processed pages. The flags supply eligibility criteria, not factual validation."
        - scope: "ChromaDB dialogue, profile and fact text at response consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Vector-page dialogue and retained profile/facts supply response context."
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
                - "runtime.md#rt-bap-assistant-context"
              note: "Retained traits and assistant knowledge condition response style/role."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
            - "runtime.md#rt-bap-assistant-context"
          note: "Vector dialogue and retained profile/facts supply context and standing guidance at the response model, independently of maintenance eligibility."
        - scope: "ChromaDB vectors, summary keywords and access state at retrieval and retention priority consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Vectors, summary keywords and access state prioritize retrieved/retained material."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Retained representations and access state affect relative retrieval and retention priority under fixed code."
        - scope: "ChromaDB retained heat and surviving-backup analyzed flags at maintenance input selection and eligibility consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Heat and surviving backup flags select maintenance inputs."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "The heat updater checks retained analyzed flags as eligibility criteria before backup pages can enter extraction."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "A true analyzed flag excludes its retained backup page from the unanalyzed-page input, vetoing repeat extraction."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Surviving merged backups retain analyzed flags consumed by the extraction filter. These flags supply both an admissibility criterion and an enforced exclusion, not factual validation. New-session backup loss does not remove this surviving branch."
        - scope: "ChromaDB surviving backup dialogue and old profile at durable profile/fact update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Only surviving backup dialogue and old profile can feed durable profile/fact updates; newly inserted original pages cannot."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Retained dialogue and prior profile feed durable behavior-shaping updates when backup inputs survive. This update authority is separate from the output's response-context authority and from the flags' eligibility veto."
        - scope: "Evaluation sample memory at answer and update consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Retained conversations, profile and facts supply benchmark answer context."
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Full profile and assistant persona/knowledge condition the answer model."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
              note: "Session/page vectors, keywords and user-fact representations prioritize recall."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Stored session/control state selects extraction input."
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Retained conversations and prior profile feed durable sample profile/fact derivation."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Benchmark memory is not the product algorithm. Full profile/all assistant content and query-selected user/history material have distinct delivery paths."
        - scope: "Retained benchmark answer/reference ledger at offline scorer"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-loco-results"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Retained reference answers determine token-set F1 conformity of saved predictions."
          records:
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "References define the lexical conformity target and predictions supply the candidate; the score does not veto memory writes."
        - scope: "MCP return at external host and browser display at operator"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-access"
            - "memory.md#mem-rte-profile-display"
          note: "Delivery is wired, but downstream host channels and operator action are not established; a lossy display cannot classify the consumed profile as an enforced instruction."
      records:
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-obj-mid-term"
        - "memory.md#mem-obj-user-knowledge"
        - "runtime.md#rt-bap-user-context"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-assistant-knowledge"
        - "runtime.md#rt-bap-assistant-context"
        - "runtime.md#rt-rte-profile-analysis"
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-obj-memory-access"
        - "runtime.md#rt-rte-dialogue-response"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-loco-results"
        - "runtime.md#rt-rte-mcp-access"
        - "memory.md#mem-rte-profile-display"
      note: "Authority is localized to actual consumers, including update learning, downstream guidance, ranking and control eligibility. Host reliance remains unresolved; no static prompt/schema guard is classified as accumulated-memory authority."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Generated dialogue, overflow migration and profile/fact proposals under orchestrator admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dialogue-response"
                - "runtime.md#rt-rte-memory-admission"
                - "runtime.md#rt-rte-profile-analysis"
              note: "Code and models admit generated exchanges and derived content without an item-level human decision."
          records:
            - "runtime.md#rt-rte-dialogue-response"
            - "runtime.md#rt-rte-memory-admission"
            - "runtime.md#rt-rte-profile-analysis"
          note: "Initiating the request or forcing analysis is not per-content approval."
        - scope: "MCP add and Playground import admission after supplied-content checks"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-access"
                - "runtime.md#rt-rte-playground-control"
              note: "Callbacks apply nonempty-side checks and invoke automatic library admission."
          records:
            - "runtime.md#rt-rte-mcp-access"
            - "runtime.md#rt-rte-playground-control"
          note: "Software admits supplied pairs; the records do not identify the upstream supplier as a human approving each retained item."
        - scope: "ChromaDB generated content, metadata and surviving-backup derivation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "The orchestrator admits dialogue and generated/parsed content without human quality veto."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Code/model admission is implemented despite separate durability windows and the new-session backup defect."
        - scope: "Evaluation import, derivation and result-file writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "memory.md#mem-obj-loco-results"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Dataset loops and model/code maintenance admit sample memory and answer/reference results."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Configured benchmark execution does not make each derived item manually approved."
        - scope: "Access metadata changes following retrieval and analysis"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-access"
              note: "Software updates access/processing state and rebuilds selectors."
          records:
            - "memory.md#mem-obj-memory-access"
          note: "Counters, heat and analyzed markers change under fixed code."
        - scope: "Direct setters/alternative updater and initial JSON/ChromaDB contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-direct-update"
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-obj-chroma-storage"
          note: "Caller identity and initial filesystem provenance do not identify explicit human content decisions; neither manual nor automatic initialization control is established."
      records:
        - "runtime.md#rt-rte-dialogue-response"
        - "runtime.md#rt-rte-memory-admission"
        - "runtime.md#rt-rte-profile-analysis"
        - "runtime.md#rt-rte-mcp-access"
        - "runtime.md#rt-rte-playground-control"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "memory.md#mem-obj-loco-results"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-memory-access"
        - "memory.md#mem-rte-direct-update"
        - "memory.md#mem-obj-short-term"
      note: "Automatic admissions are supported on shipped transformations. Initial-content and alternative-caller control remain unresolved; no manual finding is inferred from an API call or a workflow start."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "JSON dialogue-to-session migration and continuity overview updates"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mid-term"
                - "runtime.md#rt-rte-memory-admission"
              note: "Dialogue is compressed into session summaries and continuity overviews while raw pages can remain."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mid-term"
                - "runtime.md#rt-rte-memory-admission"
              note: "New overviews propagate through stored links and existing sessions acquire pages."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mid-term"
                - "runtime.md#rt-rte-memory-admission"
              note: "Overflow moves retained exchanges from the recent tier into mid-term sessions."
          records:
            - "memory.md#mem-obj-mid-term"
            - "runtime.md#rt-rte-memory-admission"
          note: "Summaries reduce existing dialogue claims; propagation revises retained overviews and migration raises storage tier. Semantic fidelity is not certified."
        - scope: "JSON profile replacement, fact extraction and bounded capacity/LFU removal"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
                - "runtime.md#rt-rte-profile-analysis"
              note: "Standing statements are extracted from retained session dialogue."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-profiles"
                - "runtime.md#rt-rte-profile-analysis"
              note: "Old profile plus new dialogue produces a replacement retained profile."
            - value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-profile-analysis"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
                - "memory.md#mem-obj-user-profiles"
              note: "Heat-selected mid-term content becomes long-term profile/fact material."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-short-term"
                - "memory.md#mem-obj-mid-term"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "Capacity limits and LFU remove retained content."
          records:
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
            - "memory.md#mem-obj-mid-term"
            - "runtime.md#rt-rte-profile-analysis"
          note: "Fact extraction is consolidation, not synthesis merely because no entailment check exists. Profile replacement evolves retained interpretation; capacity/LFU forget retained entries."
        - scope: "ChromaDB migration, merge-created backups, long-term updates and timestamp/LFU deletion"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Dialogue summaries and surviving-backup fact extraction reduce retained content."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Session merges and profile replacement change retained objects."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Dialogue moves to mid-term vectors; surviving backup pages can yield long-term material."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "LFU session removal and timestamp capacity deletion forget content."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Initial backup loss blocks that page-to-profile branch, not vector recall or all later merged-page derivation; no dedup/upsert guarantee follows from collection add."
        - scope: "Evaluation summary, profile merge and extracted knowledge"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Conversation summaries and standing facts reduce retained exchanges."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Old and newly analyzed profiles are merged by another model call."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Imported short-term dialogue migrates to sessions and supplies long-term derivation."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Evaluation long-term lists lack product deque bounds; product decay semantics are not imported."
        - scope: "Alternative direct profile updater/setter"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-direct-update"
              note: "Direct profile replacement/merge changes an existing retained entry."
          records:
            - "memory.md#mem-rte-direct-update"
          note: "The afforded alternative replaces or concatenates profile content, with no established shipped invocation."
        - scope: "Whether model-generated profile interpretations introduce new claims rather than compression/revision"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-user-profiles"
            - "runtime.md#rt-rte-profile-analysis"
            - "epistemic.md#epi-obj-summaries"
          note: "Actual generated input/output and semantic checking are missing; inference requests alone cannot establish synthesize. No dedup or history-retaining invalidation is inferred from method names or deletion."
      records:
        - "memory.md#mem-obj-mid-term"
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-user-knowledge"
        - "memory.md#mem-obj-assistant-knowledge"
        - "runtime.md#rt-rte-profile-analysis"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-rte-direct-update"
        - "epistemic.md#epi-obj-summaries"
      note: "Implemented consolidation, evolution, tier promotion and forgetting coexist. Novel-claim generation remains indeterminate; destructive clear is not history-retaining invalidation, and index rebuilds do not establish deduplication."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested JSON response context retrieval and delivery"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dialogue-response"
              note: "The current query initiates semantic retrieval and context assembly."
          records:
            - "runtime.md#rt-rte-dialogue-response"
          note: "A foreground response query requests retained context as part of generation; selection and formatting are fulfillment, not independent unsolicited supply."
        - scope: "Requested ChromaDB response retrieval and attempted backup enrichment"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chroma-dialogue"
                - "memory.md#mem-obj-chroma-storage"
              note: "Response requests retrieve vector dialogue and retained profile/fact context."
          records:
            - "runtime.md#rt-rte-chroma-dialogue"
            - "memory.md#mem-obj-chroma-storage"
          note: "Missing initial-page backups limit enrichment, not direction; surviving vector text is returned on request."
        - scope: "MCP retrieve/profile tool return and Playground state/profile display"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-access"
                - "memory.md#mem-rte-profile-display"
              note: "Tool and HTTP requests obtain retained memories/profile data."
          records:
            - "runtime.md#rt-rte-mcp-access"
            - "memory.md#mem-rte-profile-display"
          note: "The host/browser explicitly asks for retained material; actual host model use is separate and unresolved."
        - scope: "Evaluation question answering and offline result scoring"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-locomo-evaluation"
                - "memory.md#mem-obj-evaluation-memory"
                - "memory.md#mem-obj-loco-results"
              note: "Benchmark questions and scorer invocation request their retained inputs."
          records:
            - "runtime.md#rt-rte-locomo-evaluation"
            - "memory.md#mem-obj-evaluation-memory"
            - "memory.md#mem-obj-loco-results"
          note: "Question requests retrieve sample memory; the separate scorer explicitly reads the retained result file."
        - scope: "Additional consumers in remaining demonstration drivers and uninspected included helpers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-chroma-dialogue"
            - "runtime.md#rt-rte-locomo-evaluation"
            - "runtime.md#rt-rte-mcp-access"
          note: "Records establish the named routes but not an exhaustive inventory of every shipped demonstration/helper consumer. No additional push can be asserted or ruled out."
      records:
        - "runtime.md#rt-rte-dialogue-response"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-mcp-access"
        - "memory.md#mem-rte-profile-display"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-evaluation-memory"
        - "memory.md#mem-obj-loco-results"
      note: "Every established response/tool/display/scorer route is requested pull. Remaining included demonstration/helper coverage prevents a whole-boundary pull-only conclusion; automatic formatting alone adds no push."
    read_back_signal:
      assessment: "uninspected"
      units:
        - scope: "Assessed pull-only JSON, ChromaDB, MCP, Playground and evaluation request chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-dialogue-response"
            - "runtime.md#rt-rte-chroma-dialogue"
            - "runtime.md#rt-rte-mcp-access"
            - "memory.md#mem-rte-profile-display"
            - "runtime.md#rt-rte-locomo-evaluation"
            - "memory.md#mem-obj-loco-results"
          note: "Signals classify push selectors only. Query embeddings and IDs on these requested reads do not establish push signals."
        - scope: "Remaining included demonstration/helper consumer alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-chroma-dialogue"
            - "runtime.md#rt-rte-locomo-evaluation"
            - "runtime.md#rt-rte-mcp-access"
          note: "The accepted inventory does not inspect every such consumer; direction and any push selector remain uninspected. A known pull witness cannot make this branch inapplicable."
      records:
        - "runtime.md#rt-rte-dialogue-response"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "runtime.md#rt-rte-mcp-access"
        - "memory.md#mem-rte-profile-display"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-loco-results"
      note: "No positive push signal is established. The inspected request chains are inapplicable locally; remaining consumer coverage is uninspected, so no system-wide inapplicability or evidenced absence is asserted."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "JSON dialogue-fed summary/continuity production and profile/fact updates"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-admission"
                - "memory.md#mem-obj-mid-term"
                - "runtime.md#rt-rte-profile-analysis"
                - "memory.md#mem-obj-user-profiles"
                - "memory.md#mem-obj-user-knowledge"
                - "memory.md#mem-obj-assistant-knowledge"
              note: "Recorded conversational experience automatically yields durable behavior-shaping content with later consumers."
          records:
            - "runtime.md#rt-rte-memory-admission"
            - "memory.md#mem-obj-mid-term"
            - "runtime.md#rt-rte-profile-analysis"
            - "memory.md#mem-obj-user-profiles"
            - "memory.md#mem-obj-user-knowledge"
            - "memory.md#mem-obj-assistant-knowledge"
          note: "Automatic writes persist behavior-shaping summaries/profiles/facts read by later selection, update or response calls; this does not establish improved capacity."
        - scope: "ChromaDB dialogue-derived summaries and surviving merged-backup profile/fact updates"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Dialogue supplies retained summaries; surviving merged-page backups can supply durable profile/facts consumed later."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "New-session initial pages cannot feed the backup-only extractor. Summary selection and later merged-page derivation still qualify; no intact initial-backup chain is implied."
        - scope: "Evaluation imported conversation-to-summary/profile/fact route"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Recorded conversations automatically produce retained sample memory that conditions later question answers."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Imported dialogue retains its session origin; benchmark answers/results are a separate ledger rather than feedback adaptation."
        - scope: "Benchmark answer/reference result ledger to offline scorer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "The recorded main/scorer route saves and compares answers, but supplies no canonical bounded-absence record resolving trace learning for this ledger. It establishes no qualifying behavior-shaping update and cannot establish controlled no."
        - scope: "Initial loaded state, alternative direct-update producer and uninspected extra driver routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-rte-direct-update"
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Upstream producer/trace input and complete extra-driver wiring are not established; these cannot inherit the known positive derivation route."
      records:
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-obj-mid-term"
        - "runtime.md#rt-rte-profile-analysis"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-user-knowledge"
        - "memory.md#mem-obj-assistant-knowledge"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-loco-results"
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-rte-direct-update"
      note: "Qualifying automatic conversational derivation is wired. The result ledger lacks a qualifying positive or canonical bounded-absence warrant; unknown initial/direct/extra-driver production remains included. No local or system-wide no is asserted."
    trace_source:
      assessment: "partial"
      units:
        - scope: "JSON qualifying summary, overview, profile and fact writes"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-admission"
                - "memory.md#mem-obj-mid-term"
                - "runtime.md#rt-rte-profile-analysis"
                - "memory.md#mem-obj-user-profiles"
              note: "Stored conversational turns supply the qualifying transformations."
          records:
            - "runtime.md#rt-rte-memory-admission"
            - "memory.md#mem-obj-mid-term"
            - "runtime.md#rt-rte-profile-analysis"
            - "memory.md#mem-obj-user-profiles"
          note: "Original input is recorded user/assistant conversation, including user messages; timestamps and wrapper metadata do not create event-stream provenance."
        - scope: "ChromaDB qualifying summary and surviving merged-page extraction routes"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chroma-storage"
                - "runtime.md#rt-rte-chroma-dialogue"
              note: "Conversational exchange records feed summaries and eligible surviving-backup updates."
          records:
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-chroma-dialogue"
          note: "Only surviving backup dialogue supports the profile/fact branch; vectors alone do not repair lost initial extraction inputs."
        - scope: "Evaluation qualifying imported-conversation memory derivation"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-memory"
                - "runtime.md#rt-rte-locomo-evaluation"
              note: "Recorded conversations supply the automatic summary/profile/fact transformations."
          records:
            - "memory.md#mem-obj-evaluation-memory"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Dataset conversations remain session logs when imported; captions attached to turns do not establish tool traces, trajectories or event streams."
        - scope: "Answer/reference ledger at offline scorer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-loco-results"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "The ledger has no established qualifying learning write, but no canonical bounded-absence record resolves trace learning. Source therefore cannot be made inapplicable from the scoring witness alone."
        - scope: "Initial/direct-update origins and remaining uninspected drivers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-short-term"
            - "memory.md#mem-rte-direct-update"
            - "memory.md#mem-obj-chroma-storage"
            - "runtime.md#rt-rte-locomo-evaluation"
          note: "Their qualifying-write status and original inputs are unresolved; no negative trace-source conclusion follows from known conversational routes."
      records:
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-obj-mid-term"
        - "runtime.md#rt-rte-profile-analysis"
        - "memory.md#mem-obj-user-profiles"
        - "memory.md#mem-obj-chroma-storage"
        - "runtime.md#rt-rte-chroma-dialogue"
        - "memory.md#mem-obj-evaluation-memory"
        - "runtime.md#rt-rte-locomo-evaluation"
        - "memory.md#mem-obj-loco-results"
        - "memory.md#mem-obj-short-term"
        - "memory.md#mem-rte-direct-update"
      note: "Session logs are established for each recorded qualifying write family. Unknown upstream/driver routes prevent complete source enumeration; imports, timestamps and scorer results alone establish no extra source value."
---

# MemoryOS memory profile

## Comparison rationale

All findings classify accepted records at the frozen revision. The strongest
basis used is `wired`, not observed operation or causal benefit. No source
files were read for this profile; no new records or evidence are added.

The comparison keeps original dialogue, derived text, dense selection material
and symbolic maintenance state separate. File encoding does not establish a
vector substrate; the FAISS index and ChromaDB collections do. External model
weights are dependencies, not accumulated memory changed by these routes.
Initial-file and direct-caller provenance does not establish human approval.
The known automatic derivations therefore coexist with unresolved origins
([MEM-OBJ-memory-access](memory.md#mem-obj-memory-access),
[MEM-RTE-direct-update](memory.md#mem-rte-direct-update)).

The reconciliation supersedes the epistemic profile, user-knowledge and
assistant-knowledge objects with their memory counterparts. This profile uses
[MEM-OBJ-user-profiles](memory.md#mem-obj-user-profiles),
[MEM-OBJ-user-knowledge](memory.md#mem-obj-user-knowledge) and
[MEM-OBJ-assistant-knowledge](memory.md#mem-obj-assistant-knowledge) throughout.
Raw dialogue and summary parts remain valid alongside the larger memory
containers; they are not treated as additional independent systems.

Learning authority at the update consumer is distinct from knowledge or
instruction at the answering consumer. Dialogue and old profiles feed durable
updates; resulting preferences and assistant traits then guide later answers.
Retained embeddings/text influence ranking even though scoring code is fixed.
Analyzed flags determine extraction eligibility, supplying a validation
criterion and an enforced exclusion, not evidence of factual acceptance
([RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis),
[MEM-OBJ-memory-access](memory.md#mem-obj-memory-access),
[RT-BAP-user-context](runtime.md#rt-bap-user-context),
[RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context)).

Extraction of standing facts is consolidation. Unchecked model interpretation
does not establish synthesis: the accepted epistemic account leaves semantic
relations indeterminate. Profile replacement is evolution, and capacity/LFU
removal is decay, not history-retaining invalidation. Tier migration and
heat-selected long-term admission establish promotion without establishing
truth or improvement
([MEM-OBJ-mid-term](memory.md#mem-obj-mid-term),
[MEM-OBJ-user-profiles](memory.md#mem-obj-user-profiles),
[RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis),
[EPI-OBJ-summaries](epistemic.md#epi-obj-summaries)).

The ChromaDB correction matters locally. New-session insertion overwrites the
JSON page backup before saving; original vector text can still be recalled,
but those initial pages cannot feed backup-only extraction or chain overview
enrichment. Later merges can retain new backup pages. Their retained analyzed flags are
checked before extraction: the flag is an eligibility criterion (validation),
and a marked page is excluded (enforcement), as well as selecting the input
window (routing). These control effects have their own known unit, separate
from text at response consumers, ranking inputs and dialogue at update
consumers. Positive trace learning therefore rests on dialogue-derived summaries and eligible surviving-backup
updates, never an assumed intact initial-page extraction chain. Dependency
collection-add behavior remains unresolved separately
([MEM-OBJ-chroma-storage](memory.md#mem-obj-chroma-storage),
[RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)).

Automatic selection within a requested response is still pull. MCP/browser
requests and benchmark/scorer reads are also pull; no extra push is counted
for formatting their returns. The remaining uninspected driver/helper coverage
prevents a global pull-only assertion and leaves push-signal coverage
uninspected rather than globally inapplicable
([RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response),
[RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access),
[MEM-RTE-profile-display](memory.md#mem-rte-profile-display),
[RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)).

Trace learning means a qualifying automatic conversational write and later
consumer, not demonstrated better capacity or weight training. Imported
benchmark conversations remain session-log sources. The answer/reference
ledger has a scoring consumer without an established feedback update. The
accepted records supply no canonical bounded-absence warrant for a controlled
local `no`; its trace-learning and trace-source units remain not-determinable.
Unknown upstream/direct producers cannot inherit the known conversational source
([MEM-OBJ-evaluation-memory](memory.md#mem-obj-evaluation-memory),
[MEM-OBJ-loco-results](memory.md#mem-obj-loco-results),
[RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)).
