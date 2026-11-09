---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory comparison profile of sqz's native retained context, session continuity, process-local reuse and alternative storage APIs."
run-id: "AAS-2026-11-09-sqz-154fb86209ba-01"
source-identity: "https://github.com/ojuschugh1/sqz"
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
memory-comparison:
  version: 2
  scope: "Included: native original/compressed caches and recall/access structures; persisted sessions, checkpoint and guide routes; process-local full tool documentation, WASM memoization and session interchange; statistics/regret state; browser retained counters/settings; alternative URL/search/tee APIs and their unresolved consumer/admission paths. Excluded: shipped static presets/instructions and installed copies unchanged through use, transient current-request/filtering state, external host/provider storage and model parameters. Uninspected transform bodies/site variants limit semantics and deployment parity rather than supplying additional classified stores."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Native cache originals, compressed JSON, access/path metadata, session JSON and production statistics/recall indexes"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-original"
                - "memory.md#mem-obj-cache-compressed"
                - "memory.md#mem-obj-known-files"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-operation-metadata"
                - "memory.md#mem-rte-recall-search"
              note: "Native operative payloads and their access structures reside in the SessionStore SQLite database."
          records:
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-obj-cache-compressed"
            - "memory.md#mem-obj-known-files"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-operation-metadata"
            - "memory.md#mem-rte-recall-search"
          note: "Covers recorded native persistence; JSON/BLOB encodings are not additional substrates."
        -
          scope: "Alternative library checkpoint JSON persistence"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-rte-session-continuity"
              note: "The checkpoint API can save serialized event JSON under snapshot keys in the SQLite cache; no shipped restoration loop is established."
          records:
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-session-continuity"
          note: "This classifies the exposed checkpoint persistence capability separately from wired native session/cache storage."
        -
          scope: "Process-local similarity data, lazy full tool documentation, WASM memoization and recommendation state"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-compressed"
                - "runtime.md#rt-rte-mcp-proxy"
                - "runtime.md#rt-cmp-wasm-engine"
                - "memory.md#mem-obj-operation-metadata"
              note: "Computed indices, tool_docs, memoized strings and recommendations have process-local lifetimes."
          records:
            - "memory.md#mem-obj-cache-compressed"
            - "runtime.md#rt-rte-mcp-proxy"
            - "runtime.md#rt-cmp-wasm-engine"
            - "memory.md#mem-obj-operation-metadata"
          note: "Process-local retention can still serve a later invocation; it is not native disk persistence."
        -
          scope: "Alternative URL and advanced-search storage APIs"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "URL chunks use SQLite/FTS; AdvancedSearch uses an in-memory SQLite database."
          records:
            - "memory.md#mem-cmp-library-stores"
          note: "SQLite is the substrate even when the database lifetime is in memory; no deployed agent retrieval loop is inferred."
        -
          scope: "Tee output and sidecars"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "TeeManager saves text and JSON sidecar files; CLI list/get can consume existing files."
          records:
            - "memory.md#mem-cmp-library-stores"
          note: "Automatic production by ordinary compression remains unestablished, but the exposed storage mechanism is classified."
        -
          scope: "Browser statistics/settings"
          assessment: "known"
          findings:
            -
              value: "kv"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-browser-compress"
              note: "Extension local storage retains key-addressed statistics/settings."
          records:
            - "runtime.md#rt-rte-browser-compress"
          note: "This classifies the extension API surface, not its browser-internal physical backing."
      records:
        - "memory.md#mem-obj-cache-original"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-known-files"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-rte-recall-search"
        - "runtime.md#rt-rte-mcp-proxy"
        - "runtime.md#rt-cmp-wasm-engine"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-rte-browser-compress"
      note: "Known within the recorded inventory of retained objects and alternative storage APIs; excludes transient filtering databases, external provider storage and shipped static guidance."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Cached text, session narrative/facts/corrections, generated guide and lazy documentation at text consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-compressed"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-snapshot"
                - "runtime.md#rt-rte-mcp-proxy"
              note: "These parts supply interpreted context or documentation rather than distributed weights."
          records:
            - "memory.md#mem-obj-cache-compressed"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-snapshot"
            - "runtime.md#rt-rte-mcp-proxy"
          note: "Only the text interpretation path is classified here; typed wrappers belong to the next unit."
        -
          scope: "Hashes, reference tokens, JSON wrappers, access flags, counts, sparse similarity indices and search metadata at code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-original"
                - "memory.md#mem-obj-cache-compressed"
                - "memory.md#mem-obj-known-files"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-obj-operation-metadata"
                - "memory.md#mem-rte-recall-search"
              note: "Localized fields have fixed lookup, freshness, ranking or structural-consumption rules."
          records:
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-obj-cache-compressed"
            - "memory.md#mem-obj-known-files"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-obj-operation-metadata"
            - "memory.md#mem-rte-recall-search"
          note: "Numeric MinHash and recommendation data do not establish distributed-parametric form."
        -
          scope: "Alternative URL chunks and tee text versus IDs/sidecars"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "Derived Markdown, indexed text and tee strings can be interpreted as text."
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "Chunk identifiers, TTLs, index structures and sidecars are code-consumed fields."
          records:
            - "memory.md#mem-cmp-library-stores"
          note: "Exposed mixed parts are classified without inventing an agent consumer."
        -
          scope: "WASM cached strings and browser statistics/settings"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-wasm-engine"
                - "runtime.md#rt-rte-browser-compress"
              note: "Memoized compressed strings are returned to text consumers."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-wasm-engine"
                - "runtime.md#rt-rte-browser-compress"
              note: "Hashes and extension counters/settings are fixed-rule data."
          records:
            - "runtime.md#rt-cmp-wasm-engine"
            - "runtime.md#rt-rte-browser-compress"
          note: "No native recovery or learned weights are inferred."
        -
          scope: "Arbitrary native original bytes and caller-dependent encoded/source payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-obj-cache-compressed"
          note: "Raw BLOB retention alone does not determine the payload's operative interpretation; opaque bytes cannot be classified from their container."
      records:
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-snapshot"
        - "runtime.md#rt-rte-mcp-proxy"
        - "memory.md#mem-obj-cache-original"
        - "memory.md#mem-obj-known-files"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-rte-recall-search"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-cmp-wasm-engine"
        - "runtime.md#rt-rte-browser-compress"
      note: "Supported text and symbolic parts coexist with unrestricted original payloads; no complete form union or parametric finding follows."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Acquired native original bodies and CTX/WASM imported session content"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-original"
                - "memory.md#mem-rte-session-continuity"
                - "runtime.md#rt-cmp-wasm-engine"
              note: "The system acquires caller/file/tool bytes or supplied interchange content; import does not authenticate earlier provenance."
          records:
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-rte-session-continuity"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "Immediate acquisition is known; original authorship is separately unresolved."
        -
          scope: "Compressed cache representations, direct CLI guide projections and recall/access structures"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cache-compressed"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-rte-recall-search"
                - "memory.md#mem-obj-known-files"
              note: "Deterministic transforms, projections and derived access structures compile admitted inputs."
          records:
            - "memory.md#mem-obj-cache-compressed"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-recall-search"
            - "memory.md#mem-obj-known-files"
          note: "This establishes transformation lineage for wired cache, direct CLI guide and access-structure paths, not semantic faithfulness or wired checkpoint construction."
        -
          scope: "Alternative library budgeted checkpoint derivation"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-rte-session-continuity"
              note: "The exposed builder deterministically selects retained session events by priority and byte budget into checkpoint JSON; no shipped checkpoint production/restoration loop is established."
          records:
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-session-continuity"
          note: "Checkpoint derivation retains the library capability basis independently of wired direct CLI guide projection."
        -
          scope: "Tool-result-derived compressed cache text and operation measurements"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-proxy"
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-obj-operation-metadata"
              note: "Tool results feed retained compressed context; relevant operations also feed retained raw metrics."
          records:
            - "runtime.md#rt-rte-mcp-proxy"
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-obj-operation-metadata"
          note: "Trace origin applies to these inputs, not every file or session stored in the same database."
        -
          scope: "Alternative library supplied text, fetched pages and derived chunks"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "AdvancedSearch accepts caller-authored text."
            -
              value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "URL fetching and tee saving acquire supplied external content."
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "HTML-to-Markdown conversion and heading chunking derive representations."
          records:
            - "memory.md#mem-cmp-library-stores"
          note: "These APIs do not establish deployment or a human author."
        -
          scope: "Initial full-session assembly and prior history of imported facts/corrections or arbitrary cached bodies"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-rte-session-continuity"
          note: "The records do not establish whether initial content was authored, extracted from sessions, or derived elsewhere."
      records:
        - "memory.md#mem-obj-cache-original"
        - "memory.md#mem-rte-session-continuity"
        - "runtime.md#rt-cmp-wasm-engine"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-rte-recall-search"
        - "memory.md#mem-obj-known-files"
        - "runtime.md#rt-rte-mcp-proxy"
        - "runtime.md#rt-rte-cache-recovery"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-cmp-library-stores"
        - "memory.md#mem-obj-session"
      note: "Immediate imported and compiled paths are established; unresolved initial-session and arbitrary-input derivation prevents complete provenance classification."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Recovered originals, compressed text, snippets, session guides and lazy documentation at later text consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-rte-recall-search"
                - "memory.md#mem-rte-session-continuity"
                - "runtime.md#rt-rte-mcp-proxy"
              note: "Delivered text supplies context/reference/advice; a knowledge wrapper or correction arrow grants no truth warrant."
          records:
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-rte-recall-search"
            - "memory.md#mem-rte-session-continuity"
            - "runtime.md#rt-rte-mcp-proxy"
          note: "Wired delivery to CLI/host is not observed model compliance; standing instruction priority is not established for arbitrary payloads."
        -
          scope: "Retained text/features used by recall ranking and compressed baselines used by similarity selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recall-search"
                - "memory.md#mem-obj-cache-compressed"
              note: "Retained text and derived features influence BM25 or near-duplicate candidate priority."
          records:
            - "memory.md#mem-rte-recall-search"
            - "memory.md#mem-obj-cache-compressed"
          note: "Fixed scoring rules still consume retained ranking inputs."
        -
          scope: "Retained hash/path/access/pin/compaction metadata at CacheManager and CLI proxy"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-known-files"
                - "memory.md#mem-bap-reference-policy"
                - "runtime.md#rt-rte-cache-recovery"
              note: "Metadata selects reference/body/baseline paths and annotation scope."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-bap-reference-policy"
                - "memory.md#mem-rte-cache-maintenance"
                - "runtime.md#rt-rte-cache-recovery"
              note: "Stored flags/times/markers determine reference eligibility against the residency policy."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-bap-reference-policy"
                - "memory.md#mem-rte-cache-maintenance"
                - "runtime.md#rt-rte-cache-recovery"
              note: "The same code refuses stale unpinned reference substitution or permits pinned bypass."
          records:
            - "memory.md#mem-obj-known-files"
            - "memory.md#mem-bap-reference-policy"
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-rte-cache-maintenance"
          note: "This is enforceable representation eligibility, not filesystem authorization or a truthful residency guarantee."
        -
          scope: "Retained tool experience at the automatic compression/delta update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-proxy"
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-obj-cache-compressed"
              note: "Retained tool-result baselines feed automatic durable continuation representations for later context; this update force is distinct from downstream knowledge delivery."
          records:
            - "runtime.md#rt-rte-mcp-proxy"
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-obj-cache-compressed"
          note: "The controlled authority describes the trace-fed durable update path, not improved capacity or weight training."
        -
          scope: "Statistics at reports and explicit session selection metadata at resume"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-operation-metadata"
              note: "Reports expose operating measurements to a human/CLI consumer."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-continuity"
                - "memory.md#mem-obj-session"
              note: "Session IDs/timestamps select the session projected into the next guide."
          records:
            - "memory.md#mem-obj-operation-metadata"
            - "memory.md#mem-rte-session-continuity"
            - "memory.md#mem-obj-session"
          note: "Measurements do not establish an automatically consumed adaptive production policy."
        -
          scope: "Alternative library stores, recommendation outputs and WASM imported turns/corrections without established downstream behavior"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-cmp-library-stores"
            - "memory.md#mem-obj-operation-metadata"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "Storage/search or numeric recommendations alone do not establish actual downstream authority; imported WASM session consumer is unestablished."
      records:
        - "runtime.md#rt-rte-cache-recovery"
        - "memory.md#mem-rte-recall-search"
        - "memory.md#mem-rte-session-continuity"
        - "runtime.md#rt-rte-mcp-proxy"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-known-files"
        - "memory.md#mem-bap-reference-policy"
        - "memory.md#mem-rte-cache-maintenance"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-cmp-wasm-engine"
      note: "Authority is classified at named consumers; alternative APIs and imported session branches lack enough consumer facts for a complete inventory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Ordinary native cache, dependency pre-cache, recall-index and operation-metric admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-rte-dependency-precache"
                - "memory.md#mem-rte-recall-search"
                - "memory.md#mem-obj-operation-metadata"
              note: "Software admits eligible input and derived indexing/metrics without a per-content human decision."
          records:
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-rte-dependency-precache"
            - "memory.md#mem-rte-recall-search"
            - "memory.md#mem-obj-operation-metadata"
          note: "A human starting a command is not manual admission of each retained item."
        -
          scope: "CTX/WASM parser admission and same-ID session upsert"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-continuity"
                - "memory.md#mem-obj-session"
                - "runtime.md#rt-cmp-wasm-engine"
              note: "Software accepts structurally valid supplied content; caller identity is not per-content human approval."
          records:
            - "memory.md#mem-rte-session-continuity"
            - "memory.md#mem-obj-session"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "This classifies parser/save admission, not how an operator obtained or selected the imported content."
        -
          scope: "WASM memoization and browser counters/settings updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-wasm-engine"
                - "runtime.md#rt-rte-browser-compress"
              note: "Successful transforms memoize strings and browser operations record counters through code."
          records:
            - "runtime.md#rt-cmp-wasm-engine"
            - "runtime.md#rt-rte-browser-compress"
          note: "Accept/submit affects current editor adoption, not proof of manual admission to retained memory."
        -
          scope: "Alternative URL/search/tee storage decisions"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "Successful fetch/index upsert or configured tee-mode predicate governs software admission."
          records:
            - "memory.md#mem-cmp-library-stores"
          note: "The exposed APIs impose no per-item human veto; automatic capture wiring is separately unestablished."
        -
          scope: "Explicit pin/add/replace/reset choices and initial full-session assembly"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-cache-maintenance"
            - "memory.md#mem-obj-session"
          note: "Explicit callers may be human or automated; the records do not establish a human decision supplying, editing or approving the retained content. Manual cannot be inferred."
      records:
        - "runtime.md#rt-rte-cache-recovery"
        - "memory.md#mem-rte-dependency-precache"
        - "memory.md#mem-rte-recall-search"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-rte-session-continuity"
        - "memory.md#mem-obj-session"
        - "runtime.md#rt-cmp-wasm-engine"
        - "runtime.md#rt-rte-browser-compress"
        - "memory.md#mem-cmp-library-stores"
        - "memory.md#mem-rte-cache-maintenance"
      note: "Software admissions are classified independently of unresolved caller control on explicit maintenance and initial-content routes."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "CLI projection of retained sessions into a smaller guide"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-rte-session-continuity"
              note: "Selection/clipping/grouping reduces retained session material to existing claims; it does not establish a new synthesized claim."
          records:
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-session-continuity"
          note: "CLI resume directly projects sessions.data into a guide; it does not consume the separate library checkpoint."
        -
          scope: "Alternative library budgeted checkpoint construction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-rte-session-continuity"
              note: "The exposed builder selects retained session events by priority and byte budget into a reduced checkpoint representation."
          records:
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-session-continuity"
          note: "Checkpoint construction and persistence/load remain a library capability, not a wired acquisition-to-restoration loop; wired CLI guide projection does not upgrade this alternative."
        -
          scope: "Same-ID session replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session"
                - "memory.md#mem-rte-session-continuity"
              note: "Import/save upsert revises the existing session entry."
          records:
            - "memory.md#mem-obj-session"
            - "memory.md#mem-rte-session-continuity"
          note: "Revision can be externally supplied; no automatic criticism or quality improvement is implied."
        -
          scope: "Native reference-policy maintenance"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-maintenance"
                - "memory.md#mem-bap-reference-policy"
              note: "Compaction markers withdraw reference-residency reliance while leaving payloads recoverable."
            -
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-maintenance"
                - "memory.md#mem-bap-reference-policy"
              note: "Pinning raises the retained entry's residency eligibility by bypassing ordinary reference age/marker gates."
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-maintenance"
              note: "Explicit deletion/reset forgets cache content and removes recovery availability."
          records:
            - "memory.md#mem-rte-cache-maintenance"
            - "memory.md#mem-bap-reference-policy"
          note: "These are code-policy/content effects, not host message eviction or withdrawal of source truth."
        -
          scope: "Lower-level LRU and alternative URL/search replacement"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-cache-maintenance"
              note: "Exposed LRU deletes entries until its own accounted-size target fits."
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "Refetch deletes/replaces old URL data; search upsert replaces stored indexed content."
          records:
            - "memory.md#mem-rte-cache-maintenance"
            - "memory.md#mem-cmp-library-stores"
          note: "No automatic LRU invocation or deployed URL consumer is inferred."
        -
          scope: "Arbitrary native cache transformations and uninspected helper/session-authoring alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-cache-compressed"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-cmp-context-controls"
          note: "Representation changes do not alone settle all curation semantics; exact-hit suppression and index primary-key collisions do not establish dedup. No recorded per-claim semantic derivation establishes synthesize."
      records:
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-rte-session-continuity"
        - "memory.md#mem-rte-cache-maintenance"
        - "memory.md#mem-bap-reference-policy"
        - "memory.md#mem-cmp-library-stores"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-cmp-context-controls"
      note: "Supported consolidation, evolution, invalidation, promotion and forgetting remain local; unresolved transformation semantics prevent an exhaustive operation union."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit recall/expand, tee get and proxy tool-help requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recall-search"
                - "runtime.md#rt-rte-cache-recovery"
                - "runtime.md#rt-rte-mcp-proxy"
              note: "The consumer explicitly requests retained snippets, content or documentation."
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-library-stores"
              note: "CLI tee get requests existing retained output files."
          records:
            - "memory.md#mem-rte-recall-search"
            - "runtime.md#rt-rte-cache-recovery"
            - "runtime.md#rt-rte-mcp-proxy"
            - "memory.md#mem-cmp-library-stores"
          note: "Search followed by expansion is two requested operations, not an unsolicited push."
        -
          scope: "Native repeat file/tool/command compression and WASM identical-call reuse"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-cache-recovery"
                - "runtime.md#rt-rte-cli-compress"
                - "runtime.md#rt-cmp-wasm-engine"
              note: "Automatic cache selection occurs within fulfillment of the consumer's content/transform request."
          records:
            - "runtime.md#rt-rte-cache-recovery"
            - "runtime.md#rt-rte-cli-compress"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "The implementation's choice of prior representation does not make requested delivery independent memory injection."
        -
          scope: "Requested resume/export versus installed SessionStart compact guide"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-continuity"
              note: "Explicit session ID/latest resume or export requests retained session material."
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-continuity"
                - "memory.md#mem-obj-snapshot"
              note: "The installed compact SessionStart hook invokes resume without a foreground request for the retained session guide."
          records:
            - "memory.md#mem-rte-session-continuity"
            - "memory.md#mem-obj-snapshot"
          note: "The push route is wired to host stdout; actual model injection/compliance remains external and unobserved."
        -
          scope: "Stored library checkpoints, URL/search capabilities, imported WASM sessions and recommendation alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-cmp-library-stores"
            - "runtime.md#rt-cmp-wasm-engine"
            - "memory.md#mem-obj-operation-metadata"
          note: "Available store/load or recommendation APIs do not establish deployed later-consumer chains."
      records:
        - "memory.md#mem-rte-recall-search"
        - "runtime.md#rt-rte-cache-recovery"
        - "runtime.md#rt-rte-mcp-proxy"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-rte-cli-compress"
        - "runtime.md#rt-cmp-wasm-engine"
        - "memory.md#mem-rte-session-continuity"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-operation-metadata"
      note: "Both requested retrieval and an installed automatic guide route are supported; alternative API consumer wiring remains unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "SessionStart compact guide push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-continuity"
                - "memory.md#mem-obj-snapshot"
              note: "Trigger: compact SessionStart; selector input: latest-session timestamp then category/recency/byte budget; selected parts: summary, five recent turns, facts and correction pairs."
          records:
            - "memory.md#mem-rte-session-continuity"
            - "memory.md#mem-obj-snapshot"
          note: "Latest-session choice is not a matched task identity; no query/embedding or judgment selector is established. The explicit-ID resume variant is pull, not identifier push."
        -
          scope: "Known requested recall/expand/help/tee and repeat-cache deliveries"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-recall-search"
            - "runtime.md#rt-rte-cache-recovery"
            - "runtime.md#rt-rte-mcp-proxy"
            - "memory.md#mem-cmp-library-stores"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "These fulfill requested retained-material/transform delivery; their hashes, query terms or IDs do not establish push signals."
        -
          scope: "Unestablished library checkpoint/URL/search/WASM-session consumer alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-cmp-library-stores"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "No established delivery operation means no push selector can be assigned; pull witnesses cannot make this branch inapplicable."
      records:
        - "memory.md#mem-rte-session-continuity"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-rte-recall-search"
        - "runtime.md#rt-rte-cache-recovery"
        - "runtime.md#rt-rte-mcp-proxy"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-cmp-wasm-engine"
      note: "A coarse installed guide selector is known; unresolved alternative delivery routes prevent complete push-selection coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic retained compression of upstream tool results and later cache/context use"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-proxy"
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-obj-cache-compressed"
              note: "Tool execution results feed software compression, durable cached representations and later baseline/recovery/context consumers; deterministic continuation compression qualifies without observed improvement."
          records:
            - "runtime.md#rt-rte-mcp-proxy"
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-obj-cache-compressed"
          note: "This is the recorded raw-tool-result to durable-derived-context to later-consumer chain, not weight training or epistemic acceptance."
        -
          scope: "Session acquisition, imported corrections, checkpoint generation/restoration and WASM imported sessions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-rte-session-continuity"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "Imported traces may exist, but automatic initial trace acquisition/extraction and the checkpoint restoration chain are unresolved. Current guide printing alone does not establish a separately retained automatic summary."
        -
          scope: "Raw operating logs, separate regret recommendations and auxiliary store/caller inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-operation-metadata"
            - "memory.md#mem-cmp-library-stores"
            - "memory.md#mem-cmp-context-controls"
          note: "Raw logs are not enough; no inspected production compressor consumes the recommendations. Input origin and qualifying durable later-consumer routes remain incomplete; no canonical bounded-absence record warrants a local no."
      records:
        - "runtime.md#rt-rte-mcp-proxy"
        - "runtime.md#rt-rte-cache-recovery"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-rte-session-continuity"
        - "runtime.md#rt-cmp-wasm-engine"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-cmp-library-stores"
        - "memory.md#mem-cmp-context-controls"
      note: "A wired tool-trace learning route establishes yes locally and in the supported union; unresolved alternatives prevent complete learning coverage. No no finding is asserted."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Qualifying upstream tool-result compression route"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-proxy"
                - "runtime.md#rt-rte-cache-recovery"
                - "memory.md#mem-obj-cache-compressed"
              note: "Original inputs are recorded upstream execution results automatically compressed/retained for later context use."
          records:
            - "runtime.md#rt-rte-mcp-proxy"
            - "runtime.md#rt-rte-cache-recovery"
            - "memory.md#mem-obj-cache-compressed"
          note: "Tool-result origin, not JSON serialization, supplies the source classification."
        -
          scope: "Arbitrary cache inputs, initial/imported sessions, checkpoint and auxiliary recommendation/store alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-cache-original"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-obj-operation-metadata"
            - "memory.md#mem-cmp-library-stores"
            - "runtime.md#rt-cmp-wasm-engine"
          note: "Session turns are present as a content type, but a qualifying automatic trace-fed retained update from them is not established. Other inputs can be static files or caller data; no session-logs, event-streams or trajectories finding follows merely from labels."
      records:
        - "runtime.md#rt-rte-mcp-proxy"
        - "runtime.md#rt-rte-cache-recovery"
        - "memory.md#mem-obj-cache-compressed"
        - "memory.md#mem-obj-cache-original"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-operation-metadata"
        - "memory.md#mem-cmp-library-stores"
        - "runtime.md#rt-cmp-wasm-engine"
      note: "Tool traces are established on the qualifying wired route; unresolved origins and update/consumer chains remain included, not inapplicable."
---

# sqz memory profile

## Comparison rationale

This profile classifies the accepted records, not a new source inspection or an execution. All positive findings are implementation wiring or exposed capabilities. None claims observed model use, reliable reconstruction, improved capacity or causal benefit. Storage coverage is known only for the explicitly recorded inventory; unrestricted payload interpretation and incomplete admission/consumer chains keep the other inventories partial.

**Canonical identity.** Reconciliation supersedes the epistemic SessionState object with [MEM-OBJ-session](memory.md#mem-obj-session). All session-object classifications therefore use that canonical record. The narrower import and resume functions remain valid alongside [MEM-RTE-session-continuity](memory.md#mem-rte-session-continuity); no further supersession affects a value. Cache originals, compressed representations and metadata remain distinct rather than being replaced by the broad context-text container.

**Memory versus current context.** SQLite retention does not establish model-window membership. [MEM-OBJ-known-files](memory.md#mem-obj-known-files) and [MEM-BAP-reference-policy](memory.md#mem-bap-reference-policy) support routing, eligibility validation and enforcement at code consumers, not truthful residency or model compliance. Reference invalidation leaves payloads recoverable. Pins promote residency eligibility but do not inject the pinned body. [MEM-RTE-cache-maintenance](memory.md#mem-rte-cache-maintenance) supports actual deletion separately from compact's hypothetical host evictions. The latter supplies no decay finding about a host window.

**Trace-fed retention.** [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) and [MEM-OBJ-cache-compressed](memory.md#mem-obj-cache-compressed) jointly establish upstream tool results entering automatic compression and durable cache admission, followed by later compressed-baseline or recovery/context consumption. Under the profile's trace-learning definition, a retained continuation representation qualifies even when deterministic and even without a novel claim or measured improvement. That supports a local wired "yes" and tool-traces, not a conclusion about all cached inputs. Retained tool baselines have learning force at the durable-update consumer; returned text has knowledge force at the context consumer. The two authorities are separate paths.

The initial producer of full sessions remains unresolved. [MEM-OBJ-session](memory.md#mem-obj-session) records caller/import acquisition and invalid synthetic dashboard rows, not an automatic complete trace capture system. [MEM-OBJ-snapshot](memory.md#mem-obj-snapshot) distinguishes a stored checkpoint API from the actual CLI projection. Imported session turns do not alone establish a qualifying session-log learning route; printing a guide does not prove its separate durable retention. [MEM-OBJ-operation-metadata](memory.md#mem-obj-operation-metadata) likewise does not connect raw regret logs or exposed recommendations to an automatically updated production policy. These limits prohibit complete learning/source coverage, but do not erase the wired tool-result witness. No accepted evidenced-absence declaration warrants a local trace-learning "no".

**Curation and semantic limits.** Projection of retained sessions is consolidation, including when raw sessions survive. CLI guide projection has wired support; the separate budgeted checkpoint builder and its SQLite persistence are afforded capabilities. Their storage, curation and lineage findings occupy separate units so that extracted classifications retain that evidence-strength distinction. Direct CLI guide and cache/access-structure derivation support wired other-compiled lineage; budgeted checkpoint derivation supports other-compiled only at the afforded basis. Same-ID upsert is evolution. Reference-residency markers invalidate reliance on an access premise, not source truth. Exact-repeat substitution, index upsert and cache collision checks do not themselves establish duplicate removal or merging. Meaning-changing compression has unresolved per-input semantics; no synthesize finding follows from a possible faithfulness defect. These distinctions follow [MEM-OBJ-snapshot](memory.md#mem-obj-snapshot), [MEM-RTE-session-continuity](memory.md#mem-rte-session-continuity), [MEM-OBJ-cache-compressed](memory.md#mem-obj-cache-compressed) and [MEM-RTE-cache-maintenance](memory.md#mem-rte-cache-maintenance).

**Requested versus automatic delivery.** Recall, expansion and tool help are pull. Automatic baseline choice within a requested read/transform is still fulfillment of that request, not independent push. By contrast the installed compact SessionStart hook invokes resume without an explicit request for retained session knowledge. Its timestamp/latest-session and category/budget selector is coarse, not identifier-based targeting. Explicit session-ID resume is the separate pull variant. [MEM-RTE-session-continuity](memory.md#mem-rte-session-continuity) supports the installed command; [EPI-RTE-resume-guide](epistemic.md#epi-rte-resume-guide) limits the resulting influence to potential external adoption. Host delivery and actual model consumption remain unobserved.

**Capabilities and unresolved alternatives.** [MEM-CMP-library-stores](memory.md#mem-cmp-library-stores) supports URL/search/tee storage and transformations at the afforded layer. Tee get is an actual file consumer, but ordinary automatic tee production is not established. The proxy's lazy full documentation and [RT-CMP-wasm-engine](runtime.md#rt-cmp-wasm-engine) memoization are process-local, unlike SQLite content; imported WASM turns/corrections lack an established behavioral consumer. None inherits native recovery guarantees. Opaque original bytes are not classified from a readable wrapper, and unknown caller humanity does not establish manual admission.

**Source-read log.** No frozen-source files were read for this profile. All classifications use the supplied accepted records and their retained passages; no new evidence, record or source identity was added.
