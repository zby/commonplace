---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "ClawVault memory comparison: retained documents, trace derivatives, selector state and later-consumer routes at the frozen revision."
run-id: "AAS-2026-10-17-clawvault-38c16ae4ab34-01"
source-identity: "https://github.com/Versatly/clawvault"
reviewed-boundary: "bd702e9cce436bc3065827714cd576e8be20c375"
memory-comparison:
  version: 2
  scope: "Accumulated Markdown memories and metadata, raw transcript ledger, observations/reflections, extracted facts and entity profiles, handoff/checkpoint/recovery state, maintenance hashes/reports/archives, local search/graph/vector access state and cross-invocation session recap; their admission, transformation and later-consumer routes, including peer, Python, task/project/import and evaluation alternatives retained as unresolved where reports lack coverage. Excludes shipped static instructions/templates, provider model weights not shown updated through use, current outbound-message/scoring intermediates, and the separate repository-development/autoresearch change plane. External host incorporation and provider internals are not inspected memory mechanisms."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Retained Markdown bodies, frontmatter, observations, entity profiles, handoffs and archive copies"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-observations"
                - "epistemic.md#epi-obj-entity-profile"
                - "runtime.md#rt-rte-session-handoff"
                - "memory.md#mem-rte-observation-archive"
              note: "Core and Python routes retain ordinary files; Git is optional handoff packaging, not a substitute substrate for ordinary memory."
          records:
            - "runtime.md#rt-obj-vault-documents"
            - "memory.md#mem-obj-observations"
            - "epistemic.md#epi-obj-entity-profile"
            - "runtime.md#rt-rte-session-handoff"
            - "memory.md#mem-rte-observation-archive"
          note: "Core and Python routes retain ordinary files; Git is optional handoff packaging, not a substitute substrate for ordinary memory."
        -
          scope: "Raw transcript ledger, FactStore and checkpoint/recovery files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-transcripts"
                - "memory.md#mem-obj-fact-store"
                - "runtime.md#rt-rte-session-handoff"
              note: "JSONL and JSON are file encodings; FactStore reloads ID/entity/relation maps from its file."
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-session-handoff"
          note: "JSONL and JSON are file encodings; FactStore reloads ID/entity/relation maps from its file."
        -
          scope: "Derived local search, graph and FactStore access structures"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-fact-store"
                - "runtime.md#rt-rte-slot-store"
              note: "Reindex and reload construct local search/graph state and lookup maps; graph describes the access structure, not all vault content."
            -
              value: "graph"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-fact-store"
                - "runtime.md#rt-rte-slot-store"
              note: "Reindex and reload construct local search/graph state and lookup maps; graph describes the access structure, not all vault content."
          records:
            - "runtime.md#rt-obj-vault-documents"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-slot-store"
          note: "Reindex and reload construct local search/graph state and lookup maps; graph describes the access structure, not all vault content."
        -
          scope: "Retained document embedding selector"
          assessment: "partial"
          findings:
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-cmp-hosted-embeddings"
              note: "Dense stored vectors establish vector substrate; the local cache API does not establish its physical serialization. Do not infer SQLite or a service database."
          records:
            - "memory.md#mem-obj-embedding-cache"
            - "runtime.md#rt-cmp-hosted-embeddings"
          note: "Dense stored vectors establish vector substrate; the local cache API does not establish its physical serialization. Do not infer SQLite or a service database."
        -
          scope: "Separate serialized entity graph snapshot"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-store"
              note: "A JSON file is established, but its later consumer and graph interpretation remain uninspected."
          records:
            - "memory.md#mem-obj-fact-store"
          note: "A JSON file is established, but its later consumer and graph interpretation remain uninspected."
        -
          scope: "Transient cross-invocation session recap and once-injected cache"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
              note: "Session cache spans prompt invocations and is cleared at session end; distinct from static mandate text."
          records:
            - "runtime.md#rt-rte-prompt-recall"
          note: "Session cache spans prompt invocations and is cleared at session end; distinct from static mandate text."
        -
          scope: "Included task/project/kanban/migration/entity alternatives, SDK helper state and evaluation-adapter memory"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
            - "runtime.md#rt-rte-capture-turn"
          note: "The report inventory retains these alternatives without enough object/storage coverage to enumerate their operative retained parts."
      records:
        - "runtime.md#rt-obj-vault-documents"
        - "memory.md#mem-obj-observations"
        - "epistemic.md#epi-obj-entity-profile"
        - "runtime.md#rt-rte-session-handoff"
        - "memory.md#mem-rte-observation-archive"
        - "memory.md#mem-obj-raw-transcripts"
        - "memory.md#mem-obj-fact-store"
        - "runtime.md#rt-rte-slot-store"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-cmp-hosted-embeddings"
        - "runtime.md#rt-rte-prompt-recall"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-python-vault"
        - "runtime.md#rt-rte-capture-turn"
      note: "Files, local access structures and vectors are supported. Cache serialization and included alternative state are unresolved; runtime provider weights are not asserted to be use-updated memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Readable Markdown bodies, observation summaries, handoff prose and recap delivered to later readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-session-handoff"
                - "runtime.md#rt-rte-prompt-recall"
              note: "Meaning reaches model/human readers through natural-language interpretation, not by the Markdown encoding alone."
          records:
            - "runtime.md#rt-obj-vault-documents"
            - "memory.md#mem-obj-observations"
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-rte-prompt-recall"
          note: "Meaning reaches model/human readers through natural-language interpretation, not by the Markdown encoding alone."
        -
          scope: "Fact entity/value/rawText and delivered triple prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-store"
                - "memory.md#mem-rte-fact-context"
                - "epistemic.md#epi-rte-fact-context"
              note: "Readable values become concise statements in context; rawText is retained but is not delivered by the fact snippet branch."
          records:
            - "memory.md#mem-obj-fact-store"
            - "memory.md#mem-rte-fact-context"
            - "epistemic.md#epi-rte-fact-context"
          note: "Readable values become concise statements in context; rawText is retained but is not delivered by the fact snippet branch."
        -
          scope: "Frontmatter IDs/status/date, fact relations/validity/confidence, checkpoint flags and processed hashes at code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-fact-store"
                - "runtime.md#rt-rte-session-handoff"
                - "runtime.md#rt-bap-worker-state"
              note: "Fixed code uses these localized fields for lookup, exclusion, ranking and recovery; prose fields remain separate."
          records:
            - "runtime.md#rt-obj-vault-documents"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-bap-worker-state"
          note: "Fixed code uses these localized fields for lookup, exclusion, ranking and recovery; prose fields remain separate."
        -
          scope: "Entity profile summary at readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-entity-profile"
                - "epistemic.md#epi-rte-entity-synthesis"
              note: "Newest-prefix summary is readable prose; its semantic fidelity is not established."
          records:
            - "epistemic.md#epi-obj-entity-profile"
            - "epistemic.md#epi-rte-entity-synthesis"
          note: "Newest-prefix summary is readable prose; its semantic fidelity is not established."
        -
          scope: "Entity kind, links, evidence IDs, counts and mtimes at structured consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-entity-profile"
                - "epistemic.md#epi-rte-entity-synthesis"
              note: "Generated labels and finite file-domain fields are symbolic; this is not a distributed representation."
          records:
            - "epistemic.md#epi-obj-entity-profile"
            - "epistemic.md#epi-rte-entity-synthesis"
          note: "Generated labels and finite file-domain fields are symbolic; this is not a distributed representation."
        -
          scope: "Dense document vectors at similarity consumer"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-cmp-hosted-embeddings"
              note: "Distributed numerical representation is parametric in this vocabulary, not a parameter update to the embedding model."
          records:
            - "memory.md#mem-obj-embedding-cache"
            - "runtime.md#rt-cmp-hosted-embeddings"
          note: "Distributed numerical representation is parametric in this vocabulary, not a parameter update to the embedding model."
        -
          scope: "Embedding IDs, hash and model/provider signature"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-cache"
              note: "Freshness/compatibility metadata is symbolic and distinct from the numerical vector payload."
          records:
            - "memory.md#mem-obj-embedding-cache"
          note: "Freshness/compatibility metadata is symbolic and distinct from the numerical vector payload."
        -
          scope: "Raw captured strings and embedded tool/output payloads"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-transcripts"
              note: "Ordinary message text is readable, but embedded payload interpretation and later reprocessing consumers are unresolved."
          records:
            - "memory.md#mem-obj-raw-transcripts"
          note: "Ordinary message text is readable, but embedded payload interpretation and later reprocessing consumers are unresolved."
        -
          scope: "Uninspected graph/matcher branches, SDK helpers, task/project/import mutations and evaluation adapter"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
            - "runtime.md#rt-rte-capture-turn"
          note: "Included consumption paths lack part-level form coverage; inspected display summaries do not classify every payload."
      records:
        - "runtime.md#rt-obj-vault-documents"
        - "memory.md#mem-obj-observations"
        - "runtime.md#rt-rte-session-handoff"
        - "runtime.md#rt-rte-prompt-recall"
        - "memory.md#mem-obj-fact-store"
        - "memory.md#mem-rte-fact-context"
        - "epistemic.md#epi-rte-fact-context"
        - "runtime.md#rt-bap-worker-state"
        - "epistemic.md#epi-obj-entity-profile"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-cmp-hosted-embeddings"
        - "memory.md#mem-obj-raw-transcripts"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-python-vault"
        - "runtime.md#rt-rte-capture-turn"
      note: "Mixed natural-language, symbolic and numerical parts are split by consumer. Embedded raw payloads and alternative consumers prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Direct caller-supplied Markdown and handoff/checkpoint prose"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-slot-store"
                - "runtime.md#rt-rte-python-vault"
                - "runtime.md#rt-rte-session-handoff"
              note: "Callers supply or author content; authored does not establish that the caller is human. Initial outside provenance remains unresolved."
          records:
            - "runtime.md#rt-rte-slot-store"
            - "runtime.md#rt-rte-python-vault"
            - "runtime.md#rt-rte-session-handoff"
          note: "Callers supply or author content; authored does not establish that the caller is human. Initial outside provenance remains unresolved."
        -
          scope: "Peer-transferred local documents"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-peer-sync"
              note: "Software imports peer content into local files; original peer authorship/warrant is unknown."
          records:
            - "runtime.md#rt-rte-peer-sync"
          note: "Software imports peer content into local files; original peer authorship/warrant is unknown."
        -
          scope: "Raw transcript strings and replay export inputs"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-transcripts"
                - "memory.md#mem-rte-history-replay"
              note: "Inputs are acquired from drivers/exports, sometimes already normalized; this establishes imported lineage, not authentic original speaker attribution."
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "memory.md#mem-rte-history-replay"
          note: "Inputs are acquired from drivers/exports, sometimes already normalized; this establishes imported lineage, not authentic original speaker attribution."
        -
          scope: "Live observation and capture derivatives and extracted facts"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-capture-turn"
                - "epistemic.md#epi-rte-fact-extraction"
                - "memory.md#mem-rte-fact-context"
              note: "Recorded session/response/event text feeds retained derivatives. Extractor/model branches do not resolve every original input origin."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-capture-turn"
            - "epistemic.md#epi-rte-fact-extraction"
            - "memory.md#mem-rte-fact-context"
          note: "Recorded session/response/event text feeds retained derivatives. Extractor/model branches do not resolve every original input origin."
        -
          scope: "Replay-derived observations and reflection"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-replay"
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-reflect-week"
              note: "Imported historical conversation is automatically transformed into retained trace derivatives; import and extraction are separate derivation steps."
          records:
            - "memory.md#mem-rte-history-replay"
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
          note: "Imported historical conversation is automatically transformed into retained trace derivatives; import and extraction are separate derivation steps."
        -
          scope: "Entity profile labels, copied summary, cooccurrence counts and mtimes"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-entity-profile"
                - "epistemic.md#epi-rte-entity-synthesis"
              note: "Rules compile profiles from retained documents; this is other compilation, even where a label conjectures beyond its inputs."
          records:
            - "epistemic.md#epi-obj-entity-profile"
            - "epistemic.md#epi-rte-entity-synthesis"
          note: "Rules compile profiles from retained documents; this is other compilation, even where a label conjectures beyond its inputs."
        -
          scope: "Embedding vectors and symbolic cache metadata"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-cache"
              note: "Inspected rebuild derives vectors and hashes from document content and model/provider signature; source-document origins and all alternate cache producers are unresolved."
          records:
            - "memory.md#mem-obj-embedding-cache"
          note: "Inspected rebuild derives vectors and hashes from document content and model/provider signature; source-document origins and all alternate cache producers are unresolved."
        -
          scope: "Weekly consolidation and maintenance derivatives"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reflect-week"
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Software compiles retained observations/inbox material into weekly or categorized products; some upstream material is itself trace-extracted."
          records:
            - "runtime.md#rt-rte-reflect-week"
            - "runtime.md#rt-rte-maintain-inbox"
          note: "Software compiles retained observations/inbox material into weekly or categorized products; some upstream material is itself trace-extracted."
        -
          scope: "Patch input and initial task/project/kanban/migration/entity/SDK-helper/evaluation contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-document-patch"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
          note: "Caller and initial-content provenance or alternate producer semantics are unresolved; no complete lineage inventory follows."
      records:
        - "runtime.md#rt-rte-slot-store"
        - "runtime.md#rt-rte-python-vault"
        - "runtime.md#rt-rte-session-handoff"
        - "runtime.md#rt-rte-peer-sync"
        - "memory.md#mem-obj-raw-transcripts"
        - "memory.md#mem-rte-history-replay"
        - "runtime.md#rt-rte-observe-session"
        - "runtime.md#rt-rte-capture-turn"
        - "epistemic.md#epi-rte-fact-extraction"
        - "memory.md#mem-rte-fact-context"
        - "runtime.md#rt-rte-reflect-week"
        - "epistemic.md#epi-obj-entity-profile"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-rte-maintain-inbox"
        - "memory.md#mem-rte-document-patch"
        - "memory.md#mem-rte-explicit-context"
      note: "Derivation steps retain authored, imported, trace-extracted and compiled positives without treating one inspected producer as complete initial provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Vault snippets, facts, observations, handoffs and entity summaries at later context/read consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-system-context"
                - "runtime.md#rt-rte-tool-recall"
                - "runtime.md#rt-rte-session-handoff"
                - "memory.md#mem-rte-fact-context"
                - "epistemic.md#epi-rte-entity-synthesis"
              note: "Retained content supplies context/reference/advice. Privileged system delivery does not establish correctness or model compliance."
          records:
            - "runtime.md#rt-bap-system-context"
            - "runtime.md#rt-rte-tool-recall"
            - "runtime.md#rt-rte-session-handoff"
            - "memory.md#mem-rte-fact-context"
            - "epistemic.md#epi-rte-entity-synthesis"
          note: "Retained content supplies context/reference/advice. Privileged system delivery does not establish correctness or model compliance."
        -
          scope: "Retained injectable rule content at the documented agent/operator prompt consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-explicit-context"
              note: "Injectable items are selected as prompt rules; CLI/API return affords subsequent standing guidance but does not wire their insertion into a deployed model."
          records:
            - "memory.md#mem-rte-explicit-context"
          note: "Injectable items are selected as prompt rules; CLI/API return affords subsequent standing guidance but does not wire their insertion into a deployed model."
        -
          scope: "Retained document text/vectors and facts confidence/validity at retrieval and context priority consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-vault-documents"
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-rte-prompt-recall"
                - "epistemic.md#epi-rte-fact-context"
              note: "Fixed lexical/hybrid relevance scoring and confidence-based context priority consume retained features; a learned ranking policy is not required."
          records:
            - "runtime.md#rt-obj-vault-documents"
            - "memory.md#mem-obj-embedding-cache"
            - "runtime.md#rt-rte-prompt-recall"
            - "epistemic.md#epi-rte-fact-context"
          note: "Fixed lexical/hybrid relevance scoring and confidence-based context priority consume retained features; a learned ranking policy is not required."
        -
          scope: "Existing daily observations and weekly prior text at automatic update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-reflect-week"
                - "memory.md#mem-obj-observations"
              note: "Retained prior experience conditions the next durable summary/update. Learning force is local to this update consumer; output prose separately supplies knowledge, not demonstrated improved capacity."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
            - "memory.md#mem-obj-observations"
          note: "Retained prior experience conditions the next durable summary/update. Learning force is local to this update consumer; output prose separately supplies knowledge, not demonstrated improved capacity."
        -
          scope: "Maintenance processed hashes at pending-item admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-worker-state"
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Persisted processed membership is a criterion for candidate eligibility and excludes items before work; this supplies validation and an enforced veto on reprocessing."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-worker-state"
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Persisted processed membership is a criterion for candidate eligibility and excludes items before work; this supplies validation and an enforced veto on reprocessing."
          records:
            - "runtime.md#rt-bap-worker-state"
            - "runtime.md#rt-rte-maintain-inbox"
          note: "Persisted processed membership is a criterion for candidate eligibility and excludes items before work; this supplies validation and an enforced veto on reprocessing."
        -
          scope: "Fact validity fields at active-set read gate"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-store"
                - "epistemic.md#epi-rte-fact-supersession"
                - "epistemic.md#epi-rte-fact-context"
              note: "validUntil withholds superseded facts from active queries. It enforces availability, not factual truth."
          records:
            - "memory.md#mem-obj-fact-store"
            - "epistemic.md#epi-rte-fact-supersession"
            - "epistemic.md#epi-rte-fact-context"
          note: "validUntil withholds superseded facts from active queries. It enforces availability, not factual truth."
        -
          scope: "Checkpoint flags/session state, retained category/status fields and prior reflection keys at operation/window selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-handoff"
                - "runtime.md#rt-obj-vault-documents"
                - "runtime.md#rt-rte-reflect-week"
              note: "Recovery state and metadata select subsequent recovery/context inputs; prior keys exclude already reflected material."
          records:
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-obj-vault-documents"
            - "runtime.md#rt-rte-reflect-week"
          note: "Recovery state and metadata select subsequent recovery/context inputs; prior keys exclude already reflected material."
        -
          scope: "Retained snippets at outbound rewrite and cancellation consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
                - "epistemic.md#epi-rte-question-rewrite"
              note: "Hits supply knowledge to the rewrite; their text can also determine whether a question remains and a cancellation is requested. Enforcing effect is scoped to the honoring host channel."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
                - "epistemic.md#epi-rte-question-rewrite"
              note: "Hits supply knowledge to the rewrite; their text can also determine whether a question remains and a cancellation is requested. Enforcing effect is scoped to the honoring host channel."
          records:
            - "runtime.md#rt-rte-outbound-filter"
            - "epistemic.md#epi-rte-question-rewrite"
          note: "Hits supply knowledge to the rewrite; their text can also determine whether a question remains and a cancellation is requested. Enforcing effect is scoped to the honoring host channel."
        -
          scope: "Raw logs, separate entity graph snapshot, maintenance reports and unresolved alternate consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-maintain-inbox"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
          note: "Retention or display alone establishes no force. Later report/log/graph readers and other alternative authority paths are uninspected."
      records:
        - "runtime.md#rt-bap-system-context"
        - "runtime.md#rt-rte-tool-recall"
        - "runtime.md#rt-rte-session-handoff"
        - "memory.md#mem-rte-fact-context"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-obj-vault-documents"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-rte-prompt-recall"
        - "epistemic.md#epi-rte-fact-context"
        - "runtime.md#rt-rte-observe-session"
        - "runtime.md#rt-rte-reflect-week"
        - "memory.md#mem-obj-observations"
        - "runtime.md#rt-bap-worker-state"
        - "runtime.md#rt-rte-maintain-inbox"
        - "memory.md#mem-obj-fact-store"
        - "epistemic.md#epi-rte-fact-supersession"
        - "runtime.md#rt-rte-outbound-filter"
        - "epistemic.md#epi-rte-question-rewrite"
        - "memory.md#mem-obj-raw-transcripts"
        - "runtime.md#rt-rte-python-vault"
      note: "Authority is consumer-specific: advisory knowledge and afforded rules coexist with ranking, update learning and symbolic controls. Static recall mandate and provider parameters are outside accumulated-memory scope."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Observation threshold/flush, raw capture and replay derivative admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "memory.md#mem-obj-raw-transcripts"
                - "memory.md#mem-rte-history-replay"
              note: "Software/model writes and admits derived items without a per-item human decision; choosing replay or starting sleep is not such approval."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "memory.md#mem-obj-raw-transcripts"
            - "memory.md#mem-rte-history-replay"
          note: "Software/model writes and admits derived items without a per-item human decision; choosing replay or starting sleep is not such approval."
        -
          scope: "Turn-capture quality admission, fact extraction/conflict and entity-profile refresh"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-turn"
                - "epistemic.md#epi-rte-fact-extraction"
                - "epistemic.md#epi-rte-fact-supersession"
                - "epistemic.md#epi-rte-entity-synthesis"
              note: "Model/rule proposals and code admission lack per-content human veto."
          records:
            - "runtime.md#rt-rte-capture-turn"
            - "epistemic.md#epi-rte-fact-extraction"
            - "epistemic.md#epi-rte-fact-supersession"
            - "epistemic.md#epi-rte-entity-synthesis"
          note: "Model/rule proposals and code admission lack per-content human veto."
        -
          scope: "Maintenance, weekly reflection and archive movement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-inbox"
                - "runtime.md#rt-rte-reflect-week"
                - "memory.md#mem-rte-observation-archive"
              note: "Workers admit writes and move files automatically; dry-run and workflow initiation do not change item-level agency."
          records:
            - "runtime.md#rt-rte-maintain-inbox"
            - "runtime.md#rt-rte-reflect-week"
            - "memory.md#mem-rte-observation-archive"
          note: "Workers admit writes and move files automatically; dry-run and workflow initiation do not change item-level agency."
        -
          scope: "Peer file admission and embedding regeneration/pruning"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-peer-sync"
                - "memory.md#mem-obj-embedding-cache"
              note: "Manifest comparison and cache rebuild select/admit contents without per-file human approval."
          records:
            - "runtime.md#rt-rte-peer-sync"
            - "memory.md#mem-obj-embedding-cache"
          note: "Manifest comparison and cache rebuild select/admit contents without per-file human approval."
        -
          scope: "Interactive sleep fields"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-handoff"
              note: "Optional interactive questions allow the human to supply retained next steps/blockers. This manual mechanism is distinct from generic noninteractive callers and later Git confirmation."
          records:
            - "runtime.md#rt-rte-session-handoff"
          note: "Optional interactive questions allow the human to supply retained next steps/blockers. This manual mechanism is distinct from generic noninteractive callers and later Git confirmation."
        -
          scope: "Direct slot/core/Python store, caller patch and noninteractive handoff/checkpoint contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-slot-store"
            - "runtime.md#rt-rte-python-vault"
            - "memory.md#mem-rte-document-patch"
            - "runtime.md#rt-rte-session-handoff"
          note: "Generic caller identity does not establish human content decisions or autonomous model admission. Serialization itself settles neither."
        -
          scope: "Task/project/kanban/migration/sync-bd and other inventoried write alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-capture-turn"
            - "runtime.md#rt-rte-python-vault"
          note: "Accepted inventory retains uninspected alternate edits/admissions; their item-level control cannot be supplied by a known observer writer."
      records:
        - "runtime.md#rt-rte-observe-session"
        - "memory.md#mem-obj-raw-transcripts"
        - "memory.md#mem-rte-history-replay"
        - "runtime.md#rt-rte-capture-turn"
        - "epistemic.md#epi-rte-fact-extraction"
        - "epistemic.md#epi-rte-fact-supersession"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "runtime.md#rt-rte-maintain-inbox"
        - "runtime.md#rt-rte-reflect-week"
        - "memory.md#mem-rte-observation-archive"
        - "runtime.md#rt-rte-peer-sync"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-rte-session-handoff"
        - "runtime.md#rt-rte-slot-store"
        - "runtime.md#rt-rte-python-vault"
        - "memory.md#mem-rte-document-patch"
        - "memory.md#mem-rte-explicit-context"
      note: "Automatic derived writes and an optional human-supplied interactive handoff are supported. Generic callers and uninspected alternate writers remain unresolved; Git approval is not approval of the earlier handoff write."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Session-message compression and fact extraction into durable observations/triples"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "memory.md#mem-rte-fact-context"
                - "epistemic.md#epi-rte-fact-extraction"
              note: "Transforms retained/recorded input into selected reduced representations of its claims. Scope-loss defects do not by themselves turn extraction into synthesis."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "memory.md#mem-rte-fact-context"
            - "epistemic.md#epi-rte-fact-extraction"
          note: "Transforms retained/recorded input into selected reduced representations of its claims. Scope-loss defects do not by themselves turn extraction into synthesis."
        -
          scope: "Normalized observation merging and router duplicate/containment suppression"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "memory.md#mem-obj-observations"
                - "epistemic.md#epi-rte-router-admission"
              note: "Merging duplicates in retained observations and suppressing repeated category material implements deduplication, not a truth check."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "memory.md#mem-obj-observations"
            - "epistemic.md#epi-rte-router-admission"
          note: "Merging duplicates in retained observations and suppressing repeated category material implements deduplication, not a truth check."
        -
          scope: "Weekly reflection consolidation, prior-key exclusion and promotion"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reflect-week"
              note: "Parsed/promoted observations become a weekly reduced representation, unseen keys suppress duplicates and promotion raises selected observations into the reflection tier."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reflect-week"
              note: "Parsed/promoted observations become a weekly reduced representation, unseen keys suppress duplicates and promotion raises selected observations into the reflection tier."
            -
              value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reflect-week"
              note: "Parsed/promoted observations become a weekly reduced representation, unseen keys suppress duplicates and promotion raises selected observations into the reflection tier."
          records:
            - "runtime.md#rt-rte-reflect-week"
          note: "Parsed/promoted observations become a weekly reduced representation, unseen keys suppress duplicates and promotion raises selected observations into the reflection tier."
        -
          scope: "Maintenance distillation and janitor duplicate/stale archive"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Distillation reduces long-form input; janitor merges/removes duplicates and age-based movement reduces active availability. LLM recommendations alone are not implemented changes."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Distillation reduces long-form input; janitor merges/removes duplicates and age-based movement reduces active availability. LLM recommendations alone are not implemented changes."
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-inbox"
              note: "Distillation reduces long-form input; janitor merges/removes duplicates and age-based movement reduces active availability. LLM recommendations alone are not implemented changes."
          records:
            - "runtime.md#rt-rte-maintain-inbox"
          note: "Distillation reduces long-form input; janitor merges/removes duplicates and age-based movement reduces active availability. LLM recommendations alone are not implemented changes."
        -
          scope: "Caller document body replacement and repeated daily/weekly updates"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-document-patch"
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-reflect-week"
              note: "Existing entries are rewritten or merged; patch authorship control is separate from the implemented evolution."
          records:
            - "memory.md#mem-rte-document-patch"
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
          note: "Existing entries are rewritten or merged; patch authorship control is separate from the implemented evolution."
        -
          scope: "FactStore conflict withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-store"
                - "epistemic.md#epi-rte-fact-supersession"
              note: "Predecessor validUntil withdraws current reliance while historical interval access remains possible; same-ID replacement prevents an immutable-history guarantee."
          records:
            - "memory.md#mem-obj-fact-store"
            - "epistemic.md#epi-rte-fact-supersession"
          note: "Predecessor validUntil withdraws current reliance while historical interval access remains possible; same-ID replacement prevents an immutable-history guarantee."
        -
          scope: "Dated observation archive withdrawal from ordinary indexing"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-observation-archive"
              note: "Age selects copies retained in archive while active originals disappear from ordinary reindex. This supplies decay and invalidation locally, not universal erasure."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-observation-archive"
              note: "Age selects copies retained in archive while active originals disappear from ordinary reindex. This supplies decay and invalidation locally, not universal erasure."
          records:
            - "memory.md#mem-rte-observation-archive"
          note: "Age selects copies retained in archive while active originals disappear from ordinary reindex. This supplies decay and invalidation locally, not universal erasure."
        -
          scope: "Entity-kind generation from names/categories"
          assessment: "known"
          findings:
            -
              value: "synthesize"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-synthesis"
                - "epistemic.md#epi-obj-entity-profile"
              note: "Heuristic kind creates a claim not entailed by source category/name, unlike the separate finite cooccurrence counts; synthesis is not inferred merely from the command name."
          records:
            - "epistemic.md#epi-rte-entity-synthesis"
            - "epistemic.md#epi-obj-entity-profile"
          note: "Heuristic kind creates a claim not entailed by source category/name, unlike the separate finite cooccurrence counts; synthesis is not inferred merely from the command name."
        -
          scope: "Opaque model rewriting, full task/category transformation, detailed patch helpers and other mutation alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-reflect-week"
            - "epistemic.md#epi-rte-router-admission"
            - "memory.md#mem-rte-document-patch"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
          note: "Known transformations above do not establish all operations performed by these included branches or all meanings of model outputs."
      records:
        - "runtime.md#rt-rte-observe-session"
        - "memory.md#mem-rte-fact-context"
        - "epistemic.md#epi-rte-fact-extraction"
        - "memory.md#mem-obj-observations"
        - "epistemic.md#epi-rte-router-admission"
        - "runtime.md#rt-rte-reflect-week"
        - "runtime.md#rt-rte-maintain-inbox"
        - "memory.md#mem-rte-document-patch"
        - "memory.md#mem-obj-fact-store"
        - "epistemic.md#epi-rte-fact-supersession"
        - "memory.md#mem-rte-observation-archive"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "epistemic.md#epi-obj-entity-profile"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-python-vault"
      note: "All seven controlled operations have local supported transformations, but this union is not a complete per-route operation classification. Index rebuild or primary-key collision rejection alone adds no curation value."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Foreground tools, slot search/recall, sleep/wake recovery and Python search/wake"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-tool-recall"
                - "runtime.md#rt-rte-slot-store"
                - "runtime.md#rt-rte-session-handoff"
                - "runtime.md#rt-rte-python-vault"
              note: "Caller requests retained content and receives snippets/files/context. Formatting and software delivery fulfill the request rather than adding another push."
          records:
            - "runtime.md#rt-rte-tool-recall"
            - "runtime.md#rt-rte-slot-store"
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-rte-python-vault"
          note: "Caller requests retained content and receives snippets/files/context. Formatting and software delivery fulfill the request rather than adding another push."
        -
          scope: "Explicit context, strategy recall and command inject"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-explicit-context"
                - "memory.md#mem-rte-fact-context"
              note: "Agent/operator task/message request initiates selection and return; an automatic matcher within requested assembly is still pull."
          records:
            - "memory.md#mem-rte-explicit-context"
            - "memory.md#mem-rte-fact-context"
          note: "Agent/operator task/message request initiates selection and return; an automatic matcher within requested assembly is still pull."
        -
          scope: "Host before-prompt-build vault snippets and session recap"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
                - "runtime.md#rt-bap-system-context"
              note: "Host lifecycle triggers independent retained-content selection before the foreground answer without a request for that memory."
          records:
            - "runtime.md#rt-rte-prompt-recall"
            - "runtime.md#rt-bap-system-context"
          note: "Host lifecycle triggers independent retained-content selection before the foreground answer without a request for that memory."
        -
          scope: "Outbound-message filter memory lookup"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
              note: "Enabled question detection initiates unsolicited memory retrieval and supplies snippets to rewrite; the sender did not request memory content."
          records:
            - "runtime.md#rt-rte-outbound-filter"
          note: "Enabled question detection initiates unsolicited memory retrieval and supplies snippets to rewrite; the sender did not request memory content."
        -
          scope: "Existing observations, prior reflections and processed maintenance state at later worker calls"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-reflect-week"
                - "runtime.md#rt-bap-worker-state"
              note: "Later update/maintenance computations load retained inputs to fulfill their invoked work; this is a pull at the worker consumer, not evidence of foreground prompt push."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
            - "runtime.md#rt-bap-worker-state"
          note: "Later update/maintenance computations load retained inputs to fulfill their invoked work; this is a pull at the worker consumer, not evidence of foreground prompt push."
        -
          scope: "Raw-log reprocessing, graph snapshot/report readers and other alternative read paths"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-maintain-inbox"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
          note: "Raw persistence and serialized/display state alone do not establish every later consumer; alternative read direction remains uninspected."
      records:
        - "runtime.md#rt-rte-tool-recall"
        - "runtime.md#rt-rte-slot-store"
        - "runtime.md#rt-rte-session-handoff"
        - "runtime.md#rt-rte-python-vault"
        - "memory.md#mem-rte-explicit-context"
        - "memory.md#mem-rte-fact-context"
        - "runtime.md#rt-rte-prompt-recall"
        - "runtime.md#rt-bap-system-context"
        - "runtime.md#rt-rte-outbound-filter"
        - "runtime.md#rt-rte-observe-session"
        - "runtime.md#rt-rte-reflect-week"
        - "runtime.md#rt-bap-worker-state"
        - "memory.md#mem-obj-raw-transcripts"
        - "memory.md#mem-obj-fact-store"
        - "runtime.md#rt-rte-maintain-inbox"
      note: "Both requested return and unsolicited host delivery are supported. Known pulls do not resolve uninspected reader alternatives or make their selection signals inapplicable."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Prompt-build vault-memory push: current prompt to relevance search"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
                - "runtime.md#rt-obj-vault-documents"
              note: "Trigger is before_prompt_build; sanitized foreground text is the lexical query; matching retained document snippets are selected for system context."
          records:
            - "runtime.md#rt-rte-prompt-recall"
            - "runtime.md#rt-obj-vault-documents"
          note: "Trigger is before_prompt_build; sanitized foreground text is the lexical query; matching retained document snippets are selected for system context."
        -
          scope: "Optional vector branch of prompt-build search"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-cmp-hosted-embeddings"
              note: "The same prompt push can use a query embedding with compatible retained document vectors to select snippets. Optional configuration and available compatible cache bound this wired alternative."
          records:
            - "runtime.md#rt-rte-prompt-recall"
            - "memory.md#mem-obj-embedding-cache"
            - "runtime.md#rt-cmp-hosted-embeddings"
          note: "The same prompt push can use a query embedding with compatible retained document vectors to select snippets. Optional configuration and available compatible cache bound this wired alternative."
        -
          scope: "Prompt-build recent recap and cached session recap"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
              note: "Prompt event selects recent capped entries coarsely; session-key lookup identifies the retained session recap. Identity matching and recency filtering are separate selectors, not document path labels."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
              note: "Prompt event selects recent capped entries coarsely; session-key lookup identifies the retained session recap. Identity matching and recency filtering are separate selectors, not document path labels."
          records:
            - "runtime.md#rt-rte-prompt-recall"
          note: "Prompt event selects recent capped entries coarsely; session-key lookup identifies the retained session recap. Identity matching and recency filtering are separate selectors, not document path labels."
        -
          scope: "Prompt-build score/recency/availability filtering"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-prompt-recall"
              note: "After relevance selection, nonempty content, recency and result/snippet limits coarsely filter what is supplied; limits do not establish targeted identifier matching."
          records:
            - "runtime.md#rt-rte-prompt-recall"
          note: "After relevance selection, nonempty content, recency and result/snippet limits coarsely filter what is supplied; limits do not establish targeted identifier matching."
        -
          scope: "Outbound question push: question text to retained document hits"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
                - "epistemic.md#epi-rte-question-rewrite"
              note: "Enabled message hook and question detector trigger query-based lexical selection; up to two qualifying memory snippets reach the rewrite helper."
          records:
            - "runtime.md#rt-rte-outbound-filter"
            - "epistemic.md#epi-rte-question-rewrite"
          note: "Enabled message hook and question detector trigger query-based lexical selection; up to two qualifying memory snippets reach the rewrite helper."
        -
          scope: "Optional hybrid selector and bounded result filtering on outbound lookup"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-cmp-hosted-embeddings"
              note: "Search can use compatible document embeddings; score thresholds and capped hits separately coarsen delivery. This does not show an opaque model choosing specific memories by judgment."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-outbound-filter"
                - "memory.md#mem-obj-embedding-cache"
                - "runtime.md#rt-cmp-hosted-embeddings"
              note: "Search can use compatible document embeddings; score thresholds and capped hits separately coarsen delivery. This does not show an opaque model choosing specific memories by judgment."
          records:
            - "runtime.md#rt-rte-outbound-filter"
            - "memory.md#mem-obj-embedding-cache"
            - "runtime.md#rt-cmp-hosted-embeddings"
          note: "Search can use compatible document embeddings; score thresholds and capped hits separately coarsen delivery. This does not show an opaque model choosing specific memories by judgment."
        -
          scope: "Requested context/wake/tool and worker-read operations only"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-tool-recall"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
          note: "These scoped operations fulfill requests; push selection signals do not apply to them. They do not establish pull-only coverage for the whole system."
        -
          scope: "Unresolved alternate consumers/selectors, including detailed matcher/graph and SDK/evaluation helpers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
            - "memory.md#mem-obj-fact-store"
            - "runtime.md#rt-rte-maintain-inbox"
          note: "Accepted records do not resolve whether every remaining later-consumer branch is pull or push, nor its actual selector."
      records:
        - "runtime.md#rt-rte-prompt-recall"
        - "runtime.md#rt-obj-vault-documents"
        - "memory.md#mem-obj-embedding-cache"
        - "runtime.md#rt-cmp-hosted-embeddings"
        - "runtime.md#rt-rte-outbound-filter"
        - "epistemic.md#epi-rte-question-rewrite"
        - "runtime.md#rt-rte-tool-recall"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-session-handoff"
        - "runtime.md#rt-rte-observe-session"
        - "runtime.md#rt-rte-reflect-week"
        - "runtime.md#rt-rte-python-vault"
        - "memory.md#mem-obj-fact-store"
        - "runtime.md#rt-rte-maintain-inbox"
      note: "Push witnesses support lexical, embedding, coarse and session-identity selection. Requested inject LLM matching is not recast as unsolicited judgment push; unknown alternatives remain included."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Live transcript observation to retained daily/category knowledge and later wake/search/update consumers"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-session-handoff"
              note: "Automatic compression is retained and later read as context or update input; qualifying trace learning does not require new knowledge or measured improvement."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "memory.md#mem-obj-observations"
            - "runtime.md#rt-rte-session-handoff"
          note: "Automatic compression is retained and later read as context or update input; qualifying trace learning does not require new knowledge or measured improvement."
        -
          scope: "Historical conversation replay to retained observation/reflection and later consumers"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-replay"
                - "runtime.md#rt-rte-observe-session"
                - "runtime.md#rt-rte-reflect-week"
              note: "Software imports and transforms session traces into durable derivatives with later ordinary memory routes."
          records:
            - "memory.md#mem-rte-history-replay"
            - "runtime.md#rt-rte-observe-session"
            - "runtime.md#rt-rte-reflect-week"
          note: "Software imports and transforms session traces into durable derivatives with later ordinary memory routes."
        -
          scope: "Compaction/reset hook and observation-derived fact writes to explicit fact context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-fact-extraction"
                - "memory.md#mem-rte-fact-context"
                - "epistemic.md#epi-rte-fact-context"
              note: "Automatic rule/model extraction and conflict admission produce persistent facts that a later explicit context build consumes."
          records:
            - "epistemic.md#epi-rte-fact-extraction"
            - "memory.md#mem-rte-fact-context"
            - "epistemic.md#epi-rte-fact-context"
          note: "Automatic rule/model extraction and conflict admission produce persistent facts that a later explicit context build consumes."
        -
          scope: "Assistant-response capture to stored documents and later retrieval"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-turn"
                - "runtime.md#rt-rte-prompt-recall"
              note: "Recorded assistant text feeds automatic candidate admission; accepted files reach subsequent search/context. Internal extraction details remain unresolved without negating the wired chain."
          records:
            - "runtime.md#rt-rte-capture-turn"
            - "runtime.md#rt-rte-prompt-recall"
          note: "Recorded assistant text feeds automatic candidate admission; accepted files reach subsequent search/context. Internal extraction details remain unresolved without negating the wired chain."
        -
          scope: "Weekly observation reflection to future reflection/search"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reflect-week"
                - "memory.md#mem-obj-observations"
              note: "Trace-derived observations feed automatic retained weekly products, prior text/keys shape later updates and eligible Markdown is later retrievable."
          records:
            - "runtime.md#rt-rte-reflect-week"
            - "memory.md#mem-obj-observations"
          note: "Trace-derived observations feed automatic retained weekly products, prior text/keys shape later updates and eligible Markdown is later retrievable."
        -
          scope: "Raw JSONL alone, generic direct stores/checkpoints and mixed-source maintenance/entity/peer alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "runtime.md#rt-rte-slot-store"
            - "runtime.md#rt-rte-session-handoff"
            - "runtime.md#rt-rte-maintain-inbox"
            - "epistemic.md#epi-rte-entity-synthesis"
            - "runtime.md#rt-rte-peer-sync"
          note: "Raw logging alone lacks a demonstrated consumer; generic supplied content and mixed retained documents do not establish trace origin and automatic trace-fed behavior shaping for every path. No bounded absence record licenses a local no."
        -
          scope: "Task/project/migration/import, SDK semantic helpers and separate evaluation routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
            - "runtime.md#rt-rte-capture-turn"
          note: "Included alternatives lack a complete write-to-later-consumer trace-learning assessment."
      records:
        - "runtime.md#rt-rte-observe-session"
        - "memory.md#mem-obj-observations"
        - "runtime.md#rt-rte-session-handoff"
        - "memory.md#mem-rte-history-replay"
        - "runtime.md#rt-rte-reflect-week"
        - "epistemic.md#epi-rte-fact-extraction"
        - "memory.md#mem-rte-fact-context"
        - "epistemic.md#epi-rte-fact-context"
        - "runtime.md#rt-rte-capture-turn"
        - "runtime.md#rt-rte-prompt-recall"
        - "memory.md#mem-obj-raw-transcripts"
        - "runtime.md#rt-rte-slot-store"
        - "runtime.md#rt-rte-maintain-inbox"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "runtime.md#rt-rte-peer-sync"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-python-vault"
      note: "Several automatic trace-to-durable-context chains establish yes at wiring level. The union is positive, not evidence of improved future capacity, and it cannot imply system-wide absence for other routes."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversation content entering live observation, historical replay and response capture"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observe-session"
                - "memory.md#mem-rte-history-replay"
                - "runtime.md#rt-rte-capture-turn"
              note: "Original conversational turns, including assistant responses, are session logs. Historical date grouping or an adapter label does not turn them into event streams."
          records:
            - "runtime.md#rt-rte-observe-session"
            - "memory.md#mem-rte-history-replay"
            - "runtime.md#rt-rte-capture-turn"
          note: "Original conversational turns, including assistant responses, are session logs. Historical date grouping or an adapter label does not turn them into event streams."
        -
          scope: "Observation-derived facts and weekly reflection of conversational observations"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-context"
                - "epistemic.md#epi-rte-fact-extraction"
                - "runtime.md#rt-rte-reflect-week"
                - "memory.md#mem-obj-observations"
              note: "Session-derived input remains session-log lineage after intermediate observation Markdown; it does not acquire a new event-stream origin from its wrapper."
          records:
            - "memory.md#mem-rte-fact-context"
            - "epistemic.md#epi-rte-fact-extraction"
            - "runtime.md#rt-rte-reflect-week"
            - "memory.md#mem-obj-observations"
          note: "Session-derived input remains session-log lineage after intermediate observation Markdown; it does not acquire a new event-stream origin from its wrapper."
        -
          scope: "Mixed hook fields, embedded tool/output strings and normalized replay input alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-transcripts"
            - "epistemic.md#epi-rte-fact-extraction"
            - "memory.md#mem-rte-fact-context"
            - "memory.md#mem-rte-history-replay"
          note: "The collector admits selected text fields, while raw strings may embed tool/output content and normalizers are uninspected. Records do not establish precisely which original tool requests/results, environmental events or linked state/action/outcome sequences feed each qualifying write. No extra trace-source value follows from hook labels alone."
        -
          scope: "Mixed-source maintenance/entity writes and remaining task/project/SDK/evaluation alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-maintain-inbox"
            - "epistemic.md#epi-rte-entity-synthesis"
            - "memory.md#mem-rte-explicit-context"
            - "runtime.md#rt-rte-python-vault"
          note: "Whether each branch qualifies as trace learning and its original source content remain unresolved; known session routes cannot make these units inapplicable."
      records:
        - "runtime.md#rt-rte-observe-session"
        - "memory.md#mem-rte-history-replay"
        - "runtime.md#rt-rte-capture-turn"
        - "memory.md#mem-rte-fact-context"
        - "epistemic.md#epi-rte-fact-extraction"
        - "runtime.md#rt-rte-reflect-week"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-raw-transcripts"
        - "runtime.md#rt-rte-maintain-inbox"
        - "epistemic.md#epi-rte-entity-synthesis"
        - "memory.md#mem-rte-explicit-context"
        - "runtime.md#rt-rte-python-vault"
      note: "Session-log source is positively supported for qualifying conversational writes. Mixed or opaque origin remains unresolved; event-streams, tool-traces and trajectories are neither asserted nor ruled out system-wide."
---

# ClawVault memory profile

## Comparison rationale

The profile classifies accepted records, not a new source inspection. All positive findings are wired unless a finding explicitly identifies an afforded consumer. No record supplies observed operation or causal benefit. Axis coverage is partial even where several units are known: the memory report inventories included alternative mutations and consumers without complete part-level coverage. Those alternatives remain named rather than being removed to obtain complete statistics.

### Objects, forms and origin

[RT-OBJ-vault-documents](runtime.md#rt-obj-vault-documents) is a container for [MEM-OBJ-observations](memory.md#mem-obj-observations) and [EPI-OBJ-entity-profile](epistemic.md#epi-obj-entity-profile), not another copy of either family. Prose, fixed-rule metadata and dense vectors retain separate form findings. Vector cache serialization remains unresolved in [MEM-OBJ-embedding-cache](memory.md#mem-obj-embedding-cache); vector existence does not establish SQLite or provider-object storage. Provider weights are inference dependencies, not established use-derived retained memory. Raw strings and the separate graph snapshot remain in the inventory without inventing later foreground readers.

Reconciliation supersedes EPI-OBJ-extracted-facts with [MEM-OBJ-fact-store](memory.md#mem-obj-fact-store), and EPI-RTE-replay-import with [MEM-RTE-history-replay](memory.md#mem-rte-history-replay). The profile cites the canonical targets. These identity amendments do not erase the distinct epistemic extraction, supersession and context-selection findings. [EPI-RTE-fact-extraction](epistemic.md#epi-rte-fact-extraction), [EPI-RTE-fact-supersession](epistemic.md#epi-rte-fact-supersession) and [EPI-RTE-fact-context](epistemic.md#epi-rte-fact-context) refine rather than supersede the combined memory route.

### Force and admission

Existing observations condition later compression, giving them learning force at that update consumer; their later snippets separately supply knowledge. Fixed-code scoring of retained prose/vectors establishes ranking without a retained learned ranking policy. Persisted processed hashes supply an eligibility criterion and veto at maintenance admission; fact validity controls active delivery. These local code effects do not make delivered prose an enforced truth. See [RT-BAP-worker-state](runtime.md#rt-bap-worker-state), [RT-RTE-observe-session](runtime.md#rt-rte-observe-session) and [EPI-RTE-fact-context](epistemic.md#epi-rte-fact-context).

The optional interactive handoff permits a human to supply retained content, unlike generic direct store, patch or checkpoint callers whose control remains unresolved. The later Git approval does not retroactively approve the memory write. [RT-RTE-session-handoff](runtime.md#rt-rte-session-handoff), with its workflow annotation, retains this distinction. Automatic writes elsewhere do not resolve these caller-dependent mechanisms.

Curation follows transformations, not names. Compression/extraction consolidates even where fidelity fails; the concrete kind conjecture in [EPI-RTE-entity-synthesis](epistemic.md#epi-rte-entity-synthesis) independently supports synthesis. [RT-RTE-reflect-week](runtime.md#rt-rte-reflect-week) supports weekly consolidation/promotion, not theory criticism by its name. [MEM-RTE-observation-archive](memory.md#mem-rte-observation-archive) establishes only local age-based withdrawal; derivatives and other enumerators prevent universal forgetting.

### Delivery and trace updates

Requested wake, tools, explicit context and inject remain pull even when code selects their returned parts. The unsolicited prompt hook and outbound lookup are push. Prompt-derived relevance, optional compatible vectors, recency/availability caps and session-key recap lookup have separate signal warrants in [RT-RTE-prompt-recall](runtime.md#rt-rte-prompt-recall). Path labels on selected snippets are not another identifier selector. Optional LLM matching on a requested inject path is not evidence of judgment-based push.

Automatic observation, replay, capture, fact extraction and weekly consolidation provide qualifying trace-to-retained-context chains. This is the profile's trace-learning definition, not demonstrated capacity improvement. Raw capture alone supplies no such conclusion. Original conversational content supports session-logs; neither a hook callback label nor normalized journal-like serialization proves environmental event origin. Mixed hook/tool payloads, normalizers and alternative writers remain unresolved under [MEM-OBJ-raw-transcripts](memory.md#mem-obj-raw-transcripts), [MEM-RTE-history-replay](memory.md#mem-rte-history-replay) and [EPI-RTE-fact-extraction](epistemic.md#epi-rte-fact-extraction).

### Source-read log

No frozen source files were read for this classification. Only the supplied contracts and pinned members were read; no ambiguity required an authorized source reread. The profile adds no records, quotations or evidence.
