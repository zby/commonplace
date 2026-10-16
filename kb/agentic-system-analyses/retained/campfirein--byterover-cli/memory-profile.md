---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of ByteRover CLI: retained topics, derived context, access feedback and continuation memory within the frozen partial loop."
run-id: "AAS-2026-10-15-byterover-cli-71610aaf716b-01"
source-identity: "https://github.com/campfirein/byterover-cli"
reviewed-boundary: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
memory-comparison:
  version: 2
  scope: "Included: accumulated local topic bodies and selection metadata; derived summaries, abstracts, overviews and manifest; query caches; runtime signals; archive/review/recovery state; retained compaction summaries and task-sandbox checkpoints; imported bundle/skill admission and unresolved registered alternative persistence/consumer routes. Excluded: static shipped workflow/schema/hook text, ordinary unretained protocol state, provider weights and internals, Cloud server storage, excluded external host and dependency implementations. Installation and caller adapters remain included without assuming host activation."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Live topic bodies and selection markup"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-tree"
                - "memory.md#mem-obj-bv-rule"
                - "memory.md#mem-obj-bv-reason"
                - "memory.md#mem-obj-bv-topic"
                - "epistemic.md#epi-obj-topic-statements"
              note: "Topics are local HTML/markdown files; markup is encoding, not a graph substrate."
          records:
            - "runtime.md#rt-obj-context-tree"
            - "memory.md#mem-obj-bv-rule"
            - "memory.md#mem-obj-bv-reason"
            - "memory.md#mem-obj-bv-topic"
            - "epistemic.md#epi-obj-topic-statements"
          note: "Topics are local HTML/markdown files; markup is encoding, not a graph substrate."
        -
          scope: "Hierarchical summaries, abstract/overview siblings, manifest and archive cue/full/dream files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-obj-archive-stub"
                - "memory.md#mem-obj-full-archive"
                - "memory.md#mem-obj-dream-archive"
              note: "These retained parts use filesystem files. The archive service API does not establish an ordinary automatic archive cycle."
          records:
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-obj-full-archive"
            - "memory.md#mem-obj-dream-archive"
          note: "These retained parts use filesystem files. The archive service API does not establish an ordinary automatic archive cycle."
        -
          scope: "Runtime signal sidecar: logical store"
          assessment: "known"
          findings:
            -
              value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Signals use composite keys in IKeyStorage."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Signals use composite keys in IKeyStorage."
        -
          scope: "Runtime signal sidecar: daemon backing"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Daemon construction injects FileKeyStorage; logical KV and physical files describe separate layers of the same object."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Daemon construction injects FileKeyStorage; logical KV and physical files describe separate layers of the same object."
        -
          scope: "Process-local query result caches"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-cache"
                - "runtime.md#rt-rte-query-retrieval"
              note: "Two bounded process-local caches retain response/envelope strings for later requests."
          records:
            - "memory.md#mem-obj-query-cache"
            - "runtime.md#rt-rte-query-retrieval"
          note: "Two bounded process-local caches retain response/envelope strings for later requests."
        -
          scope: "Rolling checkpoint variable within the task sandbox"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-progress"
                - "runtime.md#rt-rte-context-control"
              note: "Progress JSON survives history clear in the task sandbox, not demonstrated process restart or task deletion."
          records:
            - "memory.md#mem-obj-checkpoint-progress"
            - "runtime.md#rt-rte-context-control"
          note: "Progress JSON survives history clear in the task sandbox, not demonstrated process restart or task deletion."
        -
          scope: "Full compaction boundary logical message store"
          assessment: "known"
          findings:
            -
              value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
              note: "StoredMessage retains summary and boundary fields in message key storage; no physical backend classification is inferred here."
          records:
            - "memory.md#mem-obj-compaction-boundary"
          note: "StoredMessage retains summary and boundary fields in message key storage; no physical backend classification is inferred here."
        -
          scope: "Compaction message-store physical backing and complete recovery/log storage inventory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "runtime.md#rt-rte-context-control"
            - "epistemic.md#epi-rte-dream-undo"
            - "epistemic.md#epi-rte-review-decision"
          note: "Key-storage use and saved recovery records do not settle all physical backing or log persistence details."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "runtime.md#rt-obj-context-tree"
        - "memory.md#mem-obj-bv-rule"
        - "memory.md#mem-obj-bv-reason"
        - "memory.md#mem-obj-bv-topic"
        - "epistemic.md#epi-obj-topic-statements"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-archive-stub"
        - "memory.md#mem-obj-full-archive"
        - "memory.md#mem-obj-dream-archive"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-obj-query-cache"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-obj-compaction-boundary"
        - "epistemic.md#epi-rte-dream-undo"
        - "epistemic.md#epi-rte-review-decision"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-cloud-sync"
        - "memory.md#mem-rte-search-recall"
      note: "File, KV and process-local witnesses coexist. Unresolved backing and alternative state routes prevent a complete substrate inventory; provider weights and remote Cloud internals are excluded, not classified as accumulated local memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Topic assertions, rule/decision bodies and reasons at model/human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-tree"
                - "memory.md#mem-obj-bv-rule"
                - "memory.md#mem-obj-bv-reason"
                - "memory.md#mem-obj-bv-topic"
                - "epistemic.md#epi-obj-topic-statements"
              note: "Prose is interpreted as claims, advice or directions; rendered severity is not executable enforcement."
          records:
            - "runtime.md#rt-obj-context-tree"
            - "memory.md#mem-obj-bv-rule"
            - "memory.md#mem-obj-bv-reason"
            - "memory.md#mem-obj-bv-topic"
            - "epistemic.md#epi-obj-topic-statements"
          note: "Prose is interpreted as claims, advice or directions; rendered severity is not executable enforcement."
        -
          scope: "Topic paths, relations, typed markup and metadata at fixed parser/lookup consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bv-topic"
                - "memory.md#mem-obj-bv-rule"
                - "runtime.md#rt-obj-context-tree"
              note: "Localized attributes drive parsing, rendering and lookup; this does not mechanically verify prose."
          records:
            - "memory.md#mem-obj-bv-topic"
            - "memory.md#mem-obj-bv-rule"
            - "runtime.md#rt-obj-context-tree"
          note: "Localized attributes drive parsing, rendering and lookup; this does not mechanically verify prose."
        -
          scope: "Summary/abstract/overview prose and archive cue prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
                - "memory.md#mem-obj-archive-stub"
              note: "These are readable condensations; opaque generation quality does not change their readable form."
          records:
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
            - "memory.md#mem-obj-archive-stub"
          note: "These are readable condensations; opaque generation quality does not change their readable form."
        -
          scope: "Summary frontmatter, archive pointers, manifest entries and runtime numerical signals"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-archive-stub"
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Hashes, paths, token counts, tiers and scores have fixed-rule consumers, not distributed-parametric encoding."
          records:
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Hashes, paths, token counts, tiers and scores have fixed-rule consumers, not distributed-parametric encoding."
        -
          scope: "Cached rendered bodies or internal response text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-cache"
                - "runtime.md#rt-rte-query-retrieval"
              note: "The readable payload is separate from cache selectors and envelopes."
          records:
            - "memory.md#mem-obj-query-cache"
            - "runtime.md#rt-rte-query-retrieval"
          note: "The readable payload is separate from cache selectors and envelopes."
        -
          scope: "Cache query tokens/fingerprint/timestamps and envelope control fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-cache"
                - "runtime.md#rt-rte-query-retrieval"
              note: "Fixed matching and expiry consumers act on these fields."
          records:
            - "memory.md#mem-obj-query-cache"
            - "runtime.md#rt-rte-query-retrieval"
          note: "Fixed matching and expiry consumers act on these fields."
        -
          scope: "Full compaction summary text and checkpoint assistant snippets"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Later model interpretation consumes summary text or retrieved snippets."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Later model interpretation consumes summary text or retrieved snippets."
        -
          scope: "Compaction boundary/session links and checkpoint counts/tool names"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Message traversal and structured progress access operate on localized metadata."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Message traversal and structured progress access operate on localized metadata."
        -
          scope: "Verbatim full/dream archive payload forms beyond the documented prose and wrapper cases"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-obj-full-archive"
            - "memory.md#mem-obj-dream-archive"
          note: "Verbatim bytes inherit the source form; the records do not enumerate every archived source part."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "runtime.md#rt-obj-context-tree"
        - "memory.md#mem-obj-bv-rule"
        - "memory.md#mem-obj-bv-reason"
        - "memory.md#mem-obj-bv-topic"
        - "epistemic.md#epi-obj-topic-statements"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-obj-archive-stub"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-obj-query-cache"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "memory.md#mem-obj-full-archive"
        - "memory.md#mem-obj-dream-archive"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-cloud-sync"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-rte-search-recall"
      note: "Readable and symbolic parts are split by consumption. No model-weights or embedding-memory finding follows from the presence of a configurable content generator; alternative payload coverage remains open."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller/internal-model authored topic text and rationale"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-tree"
                - "memory.md#mem-obj-bv-rule"
                - "memory.md#mem-obj-bv-reason"
                - "memory.md#mem-obj-bv-topic"
                - "epistemic.md#epi-obj-topic-statements"
                - "runtime.md#rt-rte-agent-curation"
              note: "Authoring routes produce topic content; this is distinct from admission and from a verified provenance chain for every existing topic."
          records:
            - "runtime.md#rt-obj-context-tree"
            - "memory.md#mem-obj-bv-rule"
            - "memory.md#mem-obj-bv-reason"
            - "memory.md#mem-obj-bv-topic"
            - "epistemic.md#epi-obj-topic-statements"
            - "runtime.md#rt-rte-agent-curation"
          note: "Authoring routes produce topic content; this is distinct from admission and from a verified provenance chain for every existing topic."
        -
          scope: "Publisher bundles and Cloud snapshots admitted locally"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hub-install"
                - "runtime.md#rt-rte-cloud-sync"
              note: "Externally supplied bytes enter retained local memory; import preserves no demonstrated factual warrant."
          records:
            - "runtime.md#rt-rte-hub-install"
            - "runtime.md#rt-rte-cloud-sync"
          note: "Externally supplied bytes enter retained local memory; import preserves no demonstrated factual warrant."
        -
          scope: "Derived summaries, abstracts, overviews, archive cues and manifest"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-obj-archive-stub"
              note: "These artifacts derive from existing content or structure; their source is not established as activity traces merely because an agent may generate them."
          records:
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-obj-archive-stub"
          note: "These artifacts derive from existing content or structure; their source is not established as activity traces merely because an agent may generate them."
        -
          scope: "Cached result content/envelopes"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-cache"
                - "runtime.md#rt-rte-query-retrieval"
              note: "The cache retains assembled query outputs, not an independently authored source of truth."
          records:
            - "memory.md#mem-obj-query-cache"
            - "runtime.md#rt-rte-query-retrieval"
          note: "The cache retains assembled query outputs, not an independently authored source of truth."
        -
          scope: "Access/write-history signals and full-summary/rolling-checkpoint products"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Usage and conversation activity feed automatic derived signals or continuation material."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Usage and conversation activity feed automatic derived signals or continuation material."
        -
          scope: "Initial provenance of directly edited topics and verbatim archived originals"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-direct-edit"
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-obj-full-archive"
            - "memory.md#mem-obj-dream-archive"
          note: "A client replacement or byte-preserving archive move does not establish the original authoring/import/trace derivation path."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "runtime.md#rt-obj-context-tree"
        - "memory.md#mem-obj-bv-rule"
        - "memory.md#mem-obj-bv-reason"
        - "memory.md#mem-obj-bv-topic"
        - "epistemic.md#epi-obj-topic-statements"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-hub-install"
        - "runtime.md#rt-rte-cloud-sync"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-archive-stub"
        - "memory.md#mem-obj-query-cache"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-direct-edit"
        - "memory.md#mem-obj-full-archive"
        - "memory.md#mem-obj-dream-archive"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-rte-search-recall"
      note: "Known derivation paths are retained without assigning one lineage to all initial content. Archive copying preserves unresolved original provenance; other registered writers remain incompletely inventoried."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Topic descriptive statements and reasons at query/read answering or update authors"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-topic-statements"
                - "memory.md#mem-obj-bv-reason"
                - "memory.md#mem-rte-topic-read"
                - "runtime.md#rt-bap-topic-guidance"
              note: "Returned prose supplies reference/context; delivery does not establish factual acceptance or actual reliance."
          records:
            - "epistemic.md#epi-obj-topic-statements"
            - "memory.md#mem-obj-bv-reason"
            - "memory.md#mem-rte-topic-read"
            - "runtime.md#rt-bap-topic-guidance"
          note: "Returned prose supplies reference/context; delivery does not establish factual acceptance or actual reliance."
        -
          scope: "Retained rule/decision directions at later calling agents"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bv-rule"
                - "epistemic.md#epi-obj-topic-rules"
                - "runtime.md#rt-bap-topic-guidance"
              note: "Retained directions can guide later work through rendered text. Their force is advisory; no host enforcement is inferred."
          records:
            - "memory.md#mem-obj-bv-rule"
            - "epistemic.md#epi-obj-topic-rules"
            - "runtime.md#rt-bap-topic-guidance"
          note: "Retained directions can guide later work through rendered text. Their force is advisory; no host enforcement is inferred."
        -
          scope: "Retained topic/summary/cue text scored by search"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-search-recall"
                - "runtime.md#rt-rte-query-retrieval"
              note: "Retained content influences relative priority under deterministic lexical search; a retained learned ranking policy is unnecessary."
          records:
            - "memory.md#mem-rte-search-recall"
            - "runtime.md#rt-rte-query-retrieval"
          note: "Retained content influences relative priority under deterministic lexical search; a retained learned ranking policy is unnecessary."
        -
          scope: "Runtime signal fields at later search and prune selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "epistemic.md#epi-rte-prune-candidates"
              note: "Importance/access/maturity influence scoring and candidate ordering. Validated is a tier label, not truth acceptance."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "epistemic.md#epi-rte-prune-candidates"
          note: "Importance/access/maturity influence scoring and candidate ordering. Validated is a tier label, not truth acceptance."
        -
          scope: "Retained usage traces at the signal-update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Access activity feeds durable behavior-shaping ranking metadata; no improved capacity or semantic knowledge revision is asserted."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Access activity feeds durable behavior-shaping ranking metadata; no improved capacity or semantic knowledge revision is asserted."
        -
          scope: "Retained conversation/tool history at compaction and checkpoint builders"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
                - "runtime.md#rt-rte-context-control"
              note: "Recorded experience feeds a durable continuation artifact for later model invocation. This authority is at the update, distinct from downstream context use."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
            - "runtime.md#rt-rte-context-control"
          note: "Recorded experience feeds a durable continuation artifact for later model invocation. This authority is at the update, distinct from downstream context use."
        -
          scope: "Summary/checkpoint text at subsequent internal task model calls"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Summary/snippet content supplies continuation context. The full-summary delivery conflict and explicit checkpoint reload requirement remain local limits."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Summary/snippet content supplies continuation context. The full-summary delivery conflict and explicit checkpoint reload requirement remain local limits."
        -
          scope: "Manifest paths/lane entries at context resolver; archive pointers and boundary links at reload consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-obj-archive-stub"
                - "memory.md#mem-rte-archive-expansion"
                - "memory.md#mem-obj-compaction-boundary"
              note: "Retained structure selects files, reload destinations or history windows. It is not all user-facing knowledge."
          records:
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-rte-archive-expansion"
            - "memory.md#mem-obj-compaction-boundary"
          note: "Retained structure selects files, reload destinations or history windows. It is not all user-facing knowledge."
        -
          scope: "Summary/abstract/overview and archived prose at internal prompt or explicit expansion consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-rte-archive-expansion"
                - "memory.md#mem-obj-full-archive"
              note: "Selected readable content supplies context; abstract preference and lossy overview are not full-source equivalence."
          records:
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-rte-archive-expansion"
            - "memory.md#mem-obj-full-archive"
          note: "Selected readable content supplies context; abstract preference and lossy overview are not full-source equivalence."
        -
          scope: "Saved review statuses at legacy Cloud export filter"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-decision"
                - "runtime.md#rt-rte-cloud-sync"
              note: "Pending/rejected status blocks selected exports. This does not gate local query or establish universal push policy."
          records:
            - "epistemic.md#epi-rte-review-decision"
            - "runtime.md#rt-rte-cloud-sync"
          note: "Pending/rejected status blocks selected exports. This does not gate local query or establish universal push policy."
        -
          scope: "Saved review/dream recovery state at rollback consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-decision"
                - "epistemic.md#epi-rte-dream-undo"
                - "memory.md#mem-obj-dream-archive"
              note: "Task/path, operation kind and backup availability choose restoration/deletion actions; factual reacceptance is not implied."
          records:
            - "epistemic.md#epi-rte-review-decision"
            - "epistemic.md#epi-rte-dream-undo"
            - "memory.md#mem-obj-dream-archive"
          note: "Task/path, operation kind and backup availability choose restoration/deletion actions; factual reacceptance is not implied."
        -
          scope: "Installed hub skill files at external host loading/placement"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-hub-install"
          note: "Installation is wired but actual host loading and resulting authority are unresolved; standing instruction force is not upgraded from availability alone."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "epistemic.md#epi-obj-topic-statements"
        - "memory.md#mem-obj-bv-reason"
        - "memory.md#mem-rte-topic-read"
        - "runtime.md#rt-bap-topic-guidance"
        - "memory.md#mem-obj-bv-rule"
        - "epistemic.md#epi-obj-topic-rules"
        - "memory.md#mem-rte-search-recall"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "epistemic.md#epi-rte-prune-candidates"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-archive-stub"
        - "memory.md#mem-rte-archive-expansion"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-obj-full-archive"
        - "epistemic.md#epi-rte-review-decision"
        - "runtime.md#rt-rte-cloud-sync"
        - "epistemic.md#epi-rte-dream-undo"
        - "memory.md#mem-obj-dream-archive"
        - "runtime.md#rt-rte-hub-install"
        - "runtime.md#rt-rte-agent-curation"
      note: "Authority belongs to actual part/consumer/effect paths. Static shipped schemas and hook instructions are outside accumulated-memory scope, so their validation/instruction effects are not classified here; unresolved consumers remain included."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Daemon topic admission after CLI/MCP continuation and internal generation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-curate-session"
                - "runtime.md#rt-rte-topic-admission"
                - "runtime.md#rt-rte-agent-curation"
              note: "Software/model admission requires no per-content human decision; an initiating request or overwrite flag is not human semantic approval."
          records:
            - "runtime.md#rt-rte-curate-session"
            - "runtime.md#rt-rte-topic-admission"
            - "runtime.md#rt-rte-agent-curation"
          note: "Software/model admission requires no per-content human decision; an initiating request or overwrite flag is not human semantic approval."
        -
          scope: "Human control of caller-authored/direct-editor content before admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-curate-session"
            - "runtime.md#rt-rte-direct-edit"
          note: "Generic caller/client identity does not establish explicit human supplying, editing or approval; no manual finding follows."
        -
          scope: "Signal updates, compaction boundaries and rolling checkpoints"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Code/model constructs and admits derived material without per-content operator approval."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Code/model constructs and admits derived material without per-content operator approval."
        -
          scope: "Cache insertion, manifest rebuild and inspected summary/abstract queue writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-cache"
                - "runtime.md#rt-rte-query-retrieval"
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
              note: "Software/model generation or assembly admits these derived artifacts; not every current HTML write is shown to invoke every generator."
          records:
            - "memory.md#mem-obj-query-cache"
            - "runtime.md#rt-rte-query-retrieval"
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
          note: "Software/model generation or assembly admits these derived artifacts; not every current HTML write is shown to invoke every generator."
        -
          scope: "Hub bundle/skill installation and Cloud snapshot admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hub-install"
                - "runtime.md#rt-rte-cloud-sync"
              note: "Selecting an install/sync workflow is not per-file content approval; the service admits downloaded/snapshot content under guards."
          records:
            - "runtime.md#rt-rte-hub-install"
            - "runtime.md#rt-rte-cloud-sync"
          note: "Selecting an install/sync workflow is not per-file content approval; the service admits downloaded/snapshot content under guards."
        -
          scope: "Review replacement, dream archive decisions and initial archive-service content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-review-decision"
            - "runtime.md#rt-rte-dream-maintenance"
            - "memory.md#mem-obj-archive-stub"
            - "memory.md#mem-obj-full-archive"
          note: "Reviewer/caller decisions are explicit but principal identity is unresolved; archive writer capacity alone does not identify its ordinary admission owner."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "runtime.md#rt-rte-curate-session"
        - "runtime.md#rt-rte-topic-admission"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-direct-edit"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "memory.md#mem-obj-query-cache"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "runtime.md#rt-rte-hub-install"
        - "runtime.md#rt-rte-cloud-sync"
        - "epistemic.md#epi-rte-review-decision"
        - "runtime.md#rt-rte-dream-maintenance"
        - "memory.md#mem-obj-archive-stub"
        - "memory.md#mem-obj-full-archive"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-rte-search-recall"
      note: "Automatic admissions are positive witnesses, not a statement that humans never author memory. Explicit human control and several alternative write mechanisms remain unresolved, preventing manual or automatic-only completeness."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Full history summary, deterministic rolling progress and content-summary/abstract/overview/cue reductions"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "memory.md#mem-obj-checkpoint-progress"
                - "memory.md#mem-obj-summary-index"
                - "memory.md#mem-obj-file-abstract"
                - "memory.md#mem-obj-file-overview"
                - "memory.md#mem-obj-archive-stub"
              note: "These transformations select/compress existing material. Truncation or fidelity failure does not establish synthesis; archive cue generation is an inspected service capability."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "memory.md#mem-obj-checkpoint-progress"
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
            - "memory.md#mem-obj-archive-stub"
          note: "These transformations select/compress existing material. Truncation or fidelity failure does not establish synthesis; archive cue generation is an inspected service capability."
        -
          scope: "Topic overwrite/replacement and signal field revision"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-topic-admission"
                - "runtime.md#rt-rte-agent-curation"
                - "runtime.md#rt-rte-direct-edit"
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Existing retained entries are revised; byte replacement and numerical revision do not imply semantic improvement."
          records:
            - "runtime.md#rt-rte-topic-admission"
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-direct-edit"
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Existing retained entries are revised; byte replacement and numerical revision do not imply semantic improvement."
        -
          scope: "Access/update-driven maturity and importance increases"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "runtime.md#rt-rte-topic-admission"
              note: "Software raises tier/salience from activity; this is not epistemic validation."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "runtime.md#rt-rte-topic-admission"
          note: "Software raises tier/salience from activity; this is not epistemic validation."
        -
          scope: "Decayed sidecar contribution in later search scoring"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-search-recall"
                - "memory.md#mem-obj-runtime-signals"
              note: "Downweighting affects ranking contribution, not demonstrated deletion of topic claims."
          records:
            - "memory.md#mem-rte-search-recall"
            - "memory.md#mem-obj-runtime-signals"
          note: "Downweighting affects ranking contribution, not demonstrated deletion of topic claims."
        -
          scope: "Dream archive withdrawal from active tree with retained former bytes"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dream-maintenance"
                - "memory.md#mem-obj-dream-archive"
              note: "Requested rename withdraws active-tree availability while preserving history; cache reuse prevents universal immediate retraction."
          records:
            - "runtime.md#rt-rte-dream-maintenance"
            - "memory.md#mem-obj-dream-archive"
          note: "Requested rename withdraws active-tree availability while preserving history; cache reuse prevents universal immediate retraction."
        -
          scope: "Caller semantic merge, link and synthesis outcomes; other registered transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-dream-maintenance"
            - "runtime.md#rt-rte-agent-curation"
            - "memory.md#mem-obj-summary-index"
          note: "Candidate names and prompts do not establish implemented deduplication or novel-claim synthesis. Semantic caller outcomes and complete alternate worker transformations are not determined."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-obj-archive-stub"
        - "runtime.md#rt-rte-topic-admission"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-direct-edit"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-rte-search-recall"
        - "runtime.md#rt-rte-dream-maintenance"
        - "memory.md#mem-obj-dream-archive"
        - "runtime.md#rt-rte-cloud-sync"
        - "runtime.md#rt-rte-context-control"
      note: "Only supported transformations receive values. Index rebuild, import and collision checks establish no curation operation by themselves. Opaque semantic branches do not erase wired consolidation/evolution/promotion/decay/withdrawal witnesses."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested public query/cache, ranked search, focused topic read and archive/overview expansion returns"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-retrieval"
                - "memory.md#mem-obj-query-cache"
                - "memory.md#mem-rte-search-recall"
                - "memory.md#mem-rte-topic-read"
                - "memory.md#mem-rte-archive-expansion"
              note: "Consumers request retained material. Code selecting and delivering the requested response is not a second push."
          records:
            - "runtime.md#rt-rte-query-retrieval"
            - "memory.md#mem-obj-query-cache"
            - "memory.md#mem-rte-search-recall"
            - "memory.md#mem-rte-topic-read"
            - "memory.md#mem-rte-archive-expansion"
          note: "Consumers request retained material. Code selecting and delivering the requested response is not a second push."
        -
          scope: "Broad manifest context automatically selected inside internal requested query"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
              note: "The query requests execution, while automatic lane selection supplies broad retained context without a separate request for those parts. The resolver ignores query text; this is not unsolicited execution."
          records:
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
          note: "The query requests execution, while automatic lane selection supplies broad retained context without a separate request for those parts. The resolver ignores query text; this is not unsolicited execution."
        -
          scope: "Retained signals automatically loaded into later search/prune selectors"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "epistemic.md#epi-rte-prune-candidates"
              note: "Selector code supplies persisted numerical metadata to later ranking/maintenance consumers without a separate request for those signal records."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "epistemic.md#epi-rte-prune-candidates"
          note: "Selector code supplies persisted numerical metadata to later ranking/maintenance consumers without a separate request for those signal records."
        -
          scope: "Full compaction summary supplied to subsequent model invocation"
          assessment: "partial"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
              note: "Message-loader implementation includes the retained boundary automatically. The runtime wording conflicts about exactly what reload contains, so this is a local memory-record witness, not a resolved complete reload account."
          records:
            - "memory.md#mem-obj-compaction-boundary"
          note: "Message-loader implementation includes the retained boundary automatically. The runtime wording conflicts about exactly what reload contains, so this is a local memory-record witness, not a resolved complete reload account."
        -
          scope: "Rolling checkpoint payload retrieved through explicit code access"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-progress"
                - "runtime.md#rt-rte-context-control"
              note: "Continuation requests the model read the variable; the JSON payload is not automatically dereferenced. Wired access does not establish observed reload."
          records:
            - "memory.md#mem-obj-checkpoint-progress"
            - "runtime.md#rt-rte-context-control"
          note: "Continuation requests the model read the variable; the JSON payload is not automatically dereferenced. Wired access does not establish observed reload."
        -
          scope: "Complete alternative compression, worker and host delivery inventory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
            - "runtime.md#rt-rte-hub-install"
          note: "Other registered routes and excluded host placement prevent exhaustive direction coverage; a known pull branch cannot make alternatives inapplicable."
      records:
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-obj-query-cache"
        - "memory.md#mem-rte-search-recall"
        - "memory.md#mem-rte-topic-read"
        - "memory.md#mem-rte-archive-expansion"
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "epistemic.md#epi-rte-prune-candidates"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-context-control"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-cloud-sync"
        - "runtime.md#rt-rte-hub-install"
      note: "Pull requests coexist with automatic context/metadata supply. Operations within each chain are distinguished; the full-summary wording conflict and alternative delivery inventory prevent known coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Manifest context push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-manifest"
                - "memory.md#mem-rte-manifest-injection"
              note: "Trigger: internal query branch. Inputs: available paths/types, condensation order, default importance and lane budgets. Selected parts: summary/context/stub entries, preferring abstracts. No query relevance or actual identity-match targeting is established."
          records:
            - "memory.md#mem-obj-context-manifest"
            - "memory.md#mem-rte-manifest-injection"
          note: "Trigger: internal query branch. Inputs: available paths/types, condensation order, default importance and lane budgets. Selected parts: summary/context/stub entries, preferring abstracts. No query relevance or actual identity-match targeting is established."
        -
          scope: "Signal metadata push into later search/prune"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "epistemic.md#epi-rte-prune-candidates"
              note: "Trigger: later search/index acquisition or scan. Input: result/topic path. Composite signal-key lookup selects the corresponding retained metadata delivered to the selector; this is an actual identity match, not merely a catalog identifier."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "epistemic.md#epi-rte-prune-candidates"
          note: "Trigger: later search/index acquisition or scan. Input: result/topic path. Composite signal-key lookup selects the corresponding retained metadata delivered to the selector; this is an actual identity match, not merely a catalog identifier."
        -
          scope: "Compaction-boundary context push"
          assessment: "partial"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
              note: "Trigger: post-compaction reload/next invocation. Inputs: session traversal and boundary stop rule. Selected retained part: summary boundary with the retained tail. Exact cross-report reload wording is unresolved; no lexical or embedding relevance selector is established."
          records:
            - "memory.md#mem-obj-compaction-boundary"
          note: "Trigger: post-compaction reload/next invocation. Inputs: session traversal and boundary stop rule. Selected retained part: summary boundary with the retained tail. Exact cross-report reload wording is unresolved; no lexical or embedding relevance selector is established."
        -
          scope: "Explicit requested query/search/read/expansion and checkpoint payload returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-query-retrieval"
            - "memory.md#mem-rte-topic-read"
            - "memory.md#mem-rte-search-recall"
            - "memory.md#mem-rte-archive-expansion"
            - "memory.md#mem-obj-checkpoint-progress"
          note: "These named delivery operations are pull, so their query/path/variable selectors do not classify push signal. This local inapplicability says nothing about alternative push routes."
        -
          scope: "Alternative registered worker/compression and host push selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
            - "runtime.md#rt-rte-hub-install"
          note: "No complete accepted inventory identifies each alternative automatic selector, its input and the retained part delivered."
      records:
        - "memory.md#mem-obj-context-manifest"
        - "memory.md#mem-rte-manifest-injection"
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "epistemic.md#epi-rte-prune-candidates"
        - "memory.md#mem-obj-compaction-boundary"
        - "runtime.md#rt-rte-query-retrieval"
        - "memory.md#mem-rte-topic-read"
        - "memory.md#mem-rte-search-recall"
        - "memory.md#mem-rte-archive-expansion"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-cloud-sync"
        - "runtime.md#rt-rte-context-control"
        - "runtime.md#rt-rte-hub-install"
      note: "Push signals classify their actual operations only. Lexical ranking on a requested query is not an inferred-lexical push witness. Known pull branches do not justify boundary-wide inapplicability."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Returned-hit activity to persisted signals to later search/prune consumers"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
                - "epistemic.md#epi-rte-prune-candidates"
              note: "Automatic usage-fed updates produce durable behavior-shaping ranking/maintenance metadata. Confirmed reading, factual acceptance and improved performance are not required or established."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
            - "epistemic.md#epi-rte-prune-candidates"
          note: "Automatic usage-fed updates produce durable behavior-shaping ranking/maintenance metadata. Confirmed reading, factual acceptance and improved performance are not required or established."
        -
          scope: "Conversation history to retained full-compaction summary to later model context"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
                - "runtime.md#rt-rte-context-control"
              note: "The memory object records a wired trace-summary-later-invocation chain. Runtime reload wording conflicts; it does not erase summary retention or this local positive, but prevents complete route coverage."
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "runtime.md#rt-rte-context-control"
          note: "The memory object records a wired trace-summary-later-invocation chain. Runtime reload wording conflicts; it does not erase summary retention or this local positive, but prevents complete route coverage."
        -
          scope: "Conversation/tool activity to sandbox progress to later explicit task-model read"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-progress"
                - "runtime.md#rt-rte-context-control"
              note: "Automatic checkpoint retains counts, tool names and assistant snippets across history clear for continuation. Horizon is later task invocations, not demonstrated restart persistence or observed use."
          records:
            - "memory.md#mem-obj-checkpoint-progress"
            - "runtime.md#rt-rte-context-control"
          note: "Automatic checkpoint retains counts, tool names and assistant snippets across history clear for continuation. Horizon is later task invocations, not demonstrated restart persistence or observed use."
        -
          scope: "Topic authoring/import/replacement and derived content provenance outside the three qualifying routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-curate-session"
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-direct-edit"
            - "runtime.md#rt-rte-hub-install"
            - "runtime.md#rt-rte-cloud-sync"
            - "memory.md#mem-obj-summary-index"
            - "memory.md#mem-obj-file-abstract"
            - "memory.md#mem-obj-file-overview"
          note: "These routes do not establish original trace input for each content write. No bounded absence record supports a local no; unknown provenance is not a negative."
        -
          scope: "Other registered ingest/map/swarm persistence, version/worktree/migration replacements, alternate compression and downstream log consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "Accepted records do not close these alternate write, replacement and consumer branches. Their unresolved object inventory prevents a complete boundary-wide classification; no absence is inferred."
      records:
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "epistemic.md#epi-rte-prune-candidates"
        - "memory.md#mem-obj-compaction-boundary"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-curate-session"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-direct-edit"
        - "runtime.md#rt-rte-hub-install"
        - "runtime.md#rt-rte-cloud-sync"
        - "memory.md#mem-obj-summary-index"
        - "memory.md#mem-obj-file-abstract"
        - "memory.md#mem-obj-file-overview"
        - "memory.md#mem-rte-search-recall"
      note: "Wired trace-fed behavior-shaping artifacts establish yes without observed improvement. No system-wide or local no is inferred from uninspected writers; source and consumer coverage remain incomplete."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Search returned-hit activity feeding the signal updater"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-signals"
                - "memory.md#mem-rte-signal-feedback"
              note: "Original input is recorded retrieval result-path/hit activity from the search operation, not a wrapper event or a confirmed success judgment."
          records:
            - "memory.md#mem-obj-runtime-signals"
            - "memory.md#mem-rte-signal-feedback"
          note: "Original input is recorded retrieval result-path/hit activity from the search operation, not a wrapper event or a confirmed success judgment."
        -
          scope: "Full compaction conversational message input"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-boundary"
              note: "First five plus last thirty-five history messages feed the summary. Conversational turns qualify even though the complete raw conversation need not be retained in-window."
          records:
            - "memory.md#mem-obj-compaction-boundary"
          note: "First five plus last thirty-five history messages feed the summary. Conversational turns qualify even though the complete raw conversation need not be retained in-window."
        -
          scope: "Rolling checkpoint assistant-message snippets"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-progress"
              note: "The builder extracts recent assistant content from task-session history."
          records:
            - "memory.md#mem-obj-checkpoint-progress"
          note: "The builder extracts recent assistant content from task-session history."
        -
          scope: "Rolling checkpoint tool-call names/counts"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-progress"
              note: "Recorded tool calls feed toolsUsed and totalToolCalls; outcomes and full feedback are not demonstrated to survive."
          records:
            - "memory.md#mem-obj-checkpoint-progress"
          note: "Recorded tool calls feed toolsUsed and totalToolCalls; outcomes and full feedback are not demonstrated to survive."
        -
          scope: "Other content in full-compaction history and complete alternate trace-fed writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-compaction-boundary"
            - "runtime.md#rt-rte-agent-curation"
            - "runtime.md#rt-rte-cloud-sync"
            - "runtime.md#rt-rte-context-control"
            - "memory.md#mem-rte-search-recall"
          note: "The record bounds selected message count but does not enumerate all original message types or every alternative write input. No event-streams or trajectories value is inferred from session links or callback wrappers."
      records:
        - "memory.md#mem-obj-runtime-signals"
        - "memory.md#mem-rte-signal-feedback"
        - "memory.md#mem-obj-compaction-boundary"
        - "memory.md#mem-obj-checkpoint-progress"
        - "runtime.md#rt-rte-agent-curation"
        - "runtime.md#rt-rte-cloud-sync"
        - "runtime.md#rt-rte-context-control"
        - "memory.md#mem-rte-search-recall"
      note: "Session and tool activity have local positive sources. Partial trace-learning inventory and mixed full-summary inputs prevent complete source enumeration; trace_source cannot become inapplicable from known non-trace acquisition routes."
---

# ByteRover CLI memory profile

## Comparison rationale

This profile classifies the accepted records, not a fresh source inspection. All positive bases are implementation wiring local to the named part or mechanism; none claims observed activation, factual acceptance or improved performance. The inventories are partial because the records retain alternative writers, compression branches and consumers without establishing a complete account of their retained objects and routes.

### Retained content, access state and authority

Topic prose, typed selection markup and runtime signals have different consumers. Rule/decision text can supply directions to later agents; statements and reasons supply knowledge. Neither becomes enforcement merely because the renderer preserves a severity label. Search treats retained text and access metadata as ranking inputs. Numerical sidecar updates also form a trace-fed behavior-shaping route. Their tier label does not validate the underlying claim. See [MEM-OBJ-bv-rule](memory.md#mem-obj-bv-rule), [MEM-OBJ-bv-reason](memory.md#mem-obj-bv-reason), [MEM-RTE-search-recall](memory.md#mem-rte-search-recall) and [MEM-RTE-signal-feedback](memory.md#mem-rte-signal-feedback).

The same sidecar has a KV interface and file backing; these are layered substrate witnesses, not two independent memories. Compaction's logical message key store has no stronger physical-backing classification here. Model execution does not establish retained model-weight updates. See [MEM-OBJ-runtime-signals](memory.md#mem-obj-runtime-signals), [MEM-OBJ-compaction-boundary](memory.md#mem-obj-compaction-boundary) and [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator).

Review statuses have enforcing force at legacy Cloud export, while recovery metadata routes rollback. The static writer schema is not accumulated memory and therefore does not create a validation-authority finding in this profile. Pending review does not prevent local retrieval. See [EPI-RTE-review-decision](epistemic.md#epi-rte-review-decision), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) and [EPI-RTE-dream-undo](epistemic.md#epi-rte-dream-undo).

### Admission and transformations

Software admission is automatic where no explicit per-content human decision is required. This does not deny possible human authorship. Generic callers, editor clients and reviewers do not establish manual control; those paths retain unresolved principal identity. Installation or workflow initiation is not approval of every retained part. See [RT-RTE-curate-session](runtime.md#rt-rte-curate-session), [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation), [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit) and [RT-RTE-hub-install](runtime.md#rt-rte-hub-install).

Consolidation covers reductions of existing retained content and activity, including deterministic checkpoints. It does not require novel knowledge or faithful output. Semantic merge/synthesis requests do not establish dedup or synthesize operations. Archive withdrawal preserves former bytes and is distinct from irreversible deletion; imperfect HTML-cache invalidation prevents claiming immediate removal from every consumer. See [MEM-OBJ-summary-index](memory.md#mem-obj-summary-index), [MEM-OBJ-checkpoint-progress](memory.md#mem-obj-checkpoint-progress), [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance), [MEM-OBJ-dream-archive](memory.md#mem-obj-dream-archive) and [MEM-OBJ-query-cache](memory.md#mem-obj-query-cache).

### Request, automatic supply and continuation

Requested query, search, focused read and expansion are pull operations. Ranking a requested return does not make it push. Internal manifest context is a separate automatic supply operation within a requested execution: code selects broad entries without a request for those particular retained parts, and the resolver ignores query relevance. Its coarse lane/budget selector is not search's activity ranking because this constructor omits the signal store. See [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval), [MEM-RTE-topic-read](memory.md#mem-rte-topic-read), [MEM-RTE-archive-expansion](memory.md#mem-rte-archive-expansion) and [MEM-RTE-manifest-injection](memory.md#mem-rte-manifest-injection).

The full-summary product has a local automatic loading witness in [MEM-OBJ-compaction-boundary](memory.md#mem-obj-compaction-boundary). Reconciliation leaves a wording conflict with [RT-RTE-context-control](runtime.md#rt-rte-context-control): the runtime says only post-boundary messages reload, whereas the memory record includes the summary boundary itself. This profile does not settle that conflict. It retains the local memory-record positive and marks the affected reload units partial rather than asserting one complete cross-report history inventory. Rolling checkpoint JSON is separate: the continuation asks the model to read it, so payload retrieval is pull, not automatic dereferencing. See [MEM-OBJ-checkpoint-progress](memory.md#mem-obj-checkpoint-progress).

Signal feedback, full compaction and rolling checkpoints qualify independently as trace learning: activity feeds automatic writes, retained results shape later ranking or task context, and within-task persistence can suffice. This says nothing about observed improvement. Search hit activity and checkpoint tool calls support tool-traces; conversational message content supports session-logs. Unenumerated mixed inputs remain unresolved. No event-stream or trajectory source follows merely from callbacks, timestamps or linked message identities.

### Canonical records and coverage limits

The supplied reconciliation supersedes the epistemic runtime-signal declaration with [MEM-OBJ-runtime-signals](memory.md#mem-obj-runtime-signals), and the epistemic focused-read declaration with [MEM-RTE-topic-read](memory.md#mem-rte-topic-read). All classifications use those canonical destinations. Supersession changes identity resolution, not value or strength. The topic container, its semantic/selection parts, the context-control route and its two retained products remain distinct.

Markdown-oriented summaries/manifests and HTML-oriented dream maintenance cannot stand for one universally covered memory plane. The archive cue/full service is not the dream archive, and exposed expansion is not an observed automatic archive lifecycle. Registered ingest/map/swarm paths, alternate compression, version/worktree/migration replacements, downstream log consumers and external host placement prevent stronger complete-inventory claims. These are unresolved included alternatives, not absence findings. See [MEM-OBJ-summary-index](memory.md#mem-obj-summary-index), [MEM-OBJ-archive-stub](memory.md#mem-obj-archive-stub), [MEM-OBJ-full-archive](memory.md#mem-obj-full-archive), [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) and [RT-RTE-context-control](runtime.md#rt-rte-context-control).

Source-read log: no target source files read. Only supplied invocation, governing contracts and pinned members were read; no new evidence, quotations or analyst records were added.
