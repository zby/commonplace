---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Curated Thoughts memory comparison of retained vault sources, derived wiki content, vectors, verification state and later consumers, with opaque alternative routes retained."
run-id: "AAS-2026-11-08-curated-thoughts-00ab3a770403-01"
source-identity: "https://github.com/equationalapplications/curated-thoughts"
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
memory-comparison:
  version: 2
  scope: "Use-accumulated vault files/chunks, retained wiki/entity/edge/task content, proposal/evidence records, derived embeddings, verification ledgers/indexes, extraction watermarks and cross-invocation verification queues; their admission, maintenance and later-consumer routes. Includes unresolved external-engine output, import, merge/draft, replay and replica alternatives named by the accepted inventory. Excludes shipped static instructions, inference weights not established as changed through use, ordinary current-call context, and external CTI host injection internals."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Vault source files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-material"
              note: "Ordinary retained source text resides in the vault filesystem."
          records:
            - "memory.md#mem-obj-source-material"
          note: "Known local source-file substrate."
        -
          scope: "Indexed chunks, wiki text, structural rows, evidence and embedding blobs"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-material"
                - "memory.md#mem-obj-wiki-content"
                - "memory.md#mem-obj-embedding-blobs"
                - "epistemic.md#epi-obj-fact-evidence"
              note: "These operative retained parts occupy SQLite rows/blobs."
          records:
            - "memory.md#mem-obj-source-material"
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-embedding-blobs"
            - "epistemic.md#epi-obj-fact-evidence"
          note: "Dense embedding encoding does not imply a vector database substrate."
        -
          scope: "Verification carriers and derived indexes"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-verification-ledgers"
              note: "Symbolic JSONL ledgers persist under stated/."
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-verification-ledgers"
              note: "Derived confirmation and denial metadata occupy SQLite."
          records:
            - "memory.md#mem-obj-verification-ledgers"
          note: "Separate durable carriers and derived database indexes."
        -
          scope: "Verification solicitation queue"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-unverified-match"
              note: "The drop file carries queued IDs and snapshots between invocations."
          records:
            - "memory.md#mem-obj-unverified-match"
          note: "Included as operational memory, not admitted knowledge."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "memory.md#mem-obj-source-material"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-embedding-blobs"
        - "epistemic.md#epi-obj-fact-evidence"
        - "memory.md#mem-obj-verification-ledgers"
        - "memory.md#mem-obj-unverified-match"
        - "runtime.md#rt-rte-wiki-maintenance"
      note: "Local files and SQLite are established; external-engine state and remote replica durability/storage internals are unresolved. No repo or graph substrate follows merely from source versioning or graph-shaped rows."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source prose, wiki bodies/entity summaries, proposal reasoning and evidence quotes"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-material"
                - "memory.md#mem-obj-wiki-content"
                - "epistemic.md#epi-obj-proposal-items"
                - "epistemic.md#epi-obj-fact-evidence"
              note: "Humans/models interpret the retained prose at extraction, review and recall."
          records:
            - "memory.md#mem-obj-source-material"
            - "memory.md#mem-obj-wiki-content"
            - "epistemic.md#epi-obj-proposal-items"
            - "epistemic.md#epi-obj-fact-evidence"
          note: "This unit excludes symbolic labels and numerical embeddings."
        -
          scope: "IDs, edges/tasks, hashes, lineage, confirmation/denial keys and queued fact IDs"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "memory.md#mem-obj-verification-ledgers"
                - "memory.md#mem-obj-unverified-match"
                - "epistemic.md#epi-obj-fact-evidence"
              note: "Fixed code rules consume localized identifiers, relationship structure and metadata."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-verification-ledgers"
            - "memory.md#mem-obj-unverified-match"
            - "epistemic.md#epi-obj-fact-evidence"
          note: "Readable labels do not convert structural consumption to natural-language interpretation."
        -
          scope: "Stored text-derived embeddings"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-blobs"
              note: "Dense numerical representations enter cosine ranking and candidate selection."
          records:
            - "memory.md#mem-obj-embedding-blobs"
          note: "This classification concerns retained vectors, not inference weights changing during use."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "memory.md#mem-obj-source-material"
        - "memory.md#mem-obj-wiki-content"
        - "epistemic.md#epi-obj-proposal-items"
        - "epistemic.md#epi-obj-fact-evidence"
        - "memory.md#mem-obj-verification-ledgers"
        - "memory.md#mem-obj-unverified-match"
        - "memory.md#mem-obj-embedding-blobs"
        - "runtime.md#rt-rte-wiki-maintenance"
      note: "Mixed operative parts are split by consumption; external-engine payload internals remain unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Explicit human capture and direct content edits"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-human-maintenance"
              note: "The app decision surface supplies or edits retained content directly."
          records:
            - "memory.md#mem-rte-human-maintenance"
          note: "This is source-supported authorship capacity, not authenticated historical use."
        -
          scope: "External vault documents and bundle-derived content"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-material"
                - "memory.md#mem-obj-wiki-content"
              note: "External assertions enter through files; the accepted wiki inventory also includes import capability."
          records:
            - "memory.md#mem-obj-source-material"
            - "memory.md#mem-obj-wiki-content"
          note: "Initial general vault acquisition details and import conflict semantics are not resolved."
        -
          scope: "Stored embeddings and model-derived proposals/facts"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-blobs"
                - "runtime.md#rt-rte-librarian-synthesis"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Software/model transformations produce retained vectors and admitted proposal content."
          records:
            - "memory.md#mem-obj-embedding-blobs"
            - "runtime.md#rt-rte-librarian-synthesis"
            - "runtime.md#rt-rte-proposal-admission"
          note: "The derivation path is known; original training and generic caller text provenance are not."
        -
          scope: "Trace origin of agent deposits and opaque engine/import/replay alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "An agent-lane label does not establish extraction from recorded experience; mixed or copied origins and engine internals remain unresolved."
      records:
        - "memory.md#mem-rte-human-maintenance"
        - "memory.md#mem-obj-source-material"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-embedding-blobs"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "runtime.md#rt-rte-proposal-admission"
        - "runtime.md#rt-rte-wiki-maintenance"
      note: "Authored, imported and compiled paths coexist. No trace-extracted lineage is inferred merely from a post-task deposit protocol."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained fact bodies at external callers and candidate prose at librarian"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-retained-fact"
                - "memory.md#mem-obj-wiki-content"
              note: "Selected prose supplies reference/context or advice, not standing instructions."
          records:
            - "memory.md#mem-bap-retained-fact"
            - "memory.md#mem-obj-wiki-content"
          note: "Delivery is wired; recipient compliance and benefit are unobserved."
        -
          scope: "Retained text, vectors and confidence/tier/time metadata at ranking consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-blobs"
                - "memory.md#mem-rte-wisdom-match"
                - "runtime.md#rt-rte-context-recall"
              note: "Cosine and lexical/tier/confidence/time scoring prioritize retained results."
          records:
            - "memory.md#mem-obj-embedding-blobs"
            - "memory.md#mem-rte-wisdom-match"
            - "runtime.md#rt-rte-context-recall"
          note: "Fixed scoring still makes retained content a ranking input."
        -
          scope: "Verification, lifecycle and lineage metadata at selectors/checks"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-verification-state"
                - "memory.md#mem-rte-wisdom-match"
                - "epistemic.md#epi-rte-anchor-check"
              note: "Denial/archive/eligibility and live-anchor predicates exclude rows or veto writes."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-verification-state"
                - "epistemic.md#epi-rte-anchor-check"
              note: "Content hashes, denial keys and live evidence anchors are conformance/admission criteria."
          records:
            - "memory.md#mem-rte-verification-state"
            - "memory.md#mem-rte-wisdom-match"
            - "epistemic.md#epi-rte-anchor-check"
          note: "These symbolic effects do not establish factual correctness or universal suppression."
        -
          scope: "Retained extraction watermark and queued verification IDs"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
                - "memory.md#mem-rte-verification-prompt"
              note: "Hash/model watermark selects processing eligibility; queued IDs select the live rows shown for review."
          records:
            - "runtime.md#rt-rte-librarian-synthesis"
            - "memory.md#mem-rte-verification-prompt"
          note: "Operational state controls later work or selected inputs rather than interpreting an explanation."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "memory.md#mem-bap-retained-fact"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-embedding-blobs"
        - "memory.md#mem-rte-wisdom-match"
        - "runtime.md#rt-rte-context-recall"
        - "memory.md#mem-rte-verification-state"
        - "epistemic.md#epi-rte-anchor-check"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "memory.md#mem-rte-verification-prompt"
        - "runtime.md#rt-rte-wiki-maintenance"
      note: "Supported consumer forces are local. Shipped static prompts and bridge tool gates are excluded from accumulated memory; uncertain trace-fed updates do not establish learning authority."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Folder-driven proposal generation and automatic admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Model/software constructs proposals and accept-all decisions without per-content operator approval."
          records:
            - "runtime.md#rt-rte-librarian-synthesis"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Starting deposit or CLI execution does not make subsequent content admission manual."
        -
          scope: "GUI proposal decisions, app capture/edit/archive and confirmation/denial"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-proposal-admission"
                - "memory.md#mem-rte-human-maintenance"
                - "memory.md#mem-rte-verification-state"
              note: "Explicit operator decisions supply, edit, approve or reject the retained content or its trust state."
          records:
            - "runtime.md#rt-rte-proposal-admission"
            - "memory.md#mem-rte-human-maintenance"
            - "memory.md#mem-rte-verification-state"
          note: "The implemented human surface is not proof of authenticated historical judgment."
        -
          scope: "Reference healing, delayed pruning and ledger reconstruction"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
                - "memory.md#mem-rte-verification-state"
              note: "Code determines affected rows from references, age and ledger keys; launching maintenance is not per-row approval."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
            - "memory.md#mem-rte-verification-state"
          note: "Symbolic maintenance has its own admission mechanism."
        -
          scope: "Generic deposit/CLI caller decisions and initial vault acquisition"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Caller identity and terminal presence do not determine whether a human made each content decision."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "runtime.md#rt-rte-librarian-synthesis"
        - "runtime.md#rt-rte-proposal-admission"
        - "memory.md#mem-rte-human-maintenance"
        - "memory.md#mem-rte-verification-state"
        - "memory.md#mem-rte-memory-withdrawal"
        - "memory.md#mem-obj-source-material"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "Both automatic and manual mechanisms are established, while generic callers, initialization and alternative writers remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Shared fact-add normalized-body duplicate gate"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-fact-retention"
              note: "Existing normalized body in the redirect cluster causes duplicate outcome instead of another entry."
          records:
            - "epistemic.md#epi-rte-fact-retention"
          note: "This is content deduplication, not just primary-key collision handling."
        -
          scope: "Direct fact and summary edits"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-human-maintenance"
              note: "Existing body/summary content is replaced and fact embeddings replaced or cleared."
          records:
            - "memory.md#mem-rte-human-maintenance"
          note: "The implemented operator edit changes an existing entry."
        -
          scope: "Archive/denial and grounding-based soft withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-human-maintenance"
                - "memory.md#mem-rte-verification-state"
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Current reliance is withdrawn with archived rows/history retained until later pruning."
          records:
            - "memory.md#mem-rte-human-maintenance"
            - "memory.md#mem-rte-verification-state"
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Soft withdrawal is distinct from hard erasure."
        -
          scope: "Delayed pruning of old archived inferred rows"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Eligible archived inferred rows are physically forgotten after seven days."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
          note: "A bounded age-based forgetting route, not universal salience decay."
        -
          scope: "Explicit confirmation"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-fact-confirmation"
              note: "Confirmation raises source/confidence status and human-tier delivery eligibility."
          records:
            - "epistemic.md#epi-rte-fact-confirmation"
          note: "Tier/salience promotion does not certify truth."
        -
          scope: "Semantic transformation in librarian model output"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-librarian-synthesis"
            - "epistemic.md#epi-obj-proposal-items"
          note: "Accepted records leave reshaping, derivation and conjecture indeterminate. A synthesis name or summarization request does not establish consolidate or synthesize as an implemented semantic transformation."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "epistemic.md#epi-rte-fact-retention"
        - "memory.md#mem-rte-human-maintenance"
        - "memory.md#mem-rte-verification-state"
        - "memory.md#mem-rte-memory-withdrawal"
        - "epistemic.md#epi-rte-fact-confirmation"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "epistemic.md#epi-obj-proposal-items"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "Implemented local maintenance supports five operations. Semantic synthesis/consolidation and opaque alternative transformations remain unresolved; pending supersession requests are not applied revisions."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested external recall, CLI matching, graph/search and direct getters"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recall"
                - "memory.md#mem-rte-wisdom-match"
                - "memory.md#mem-rte-alternate-read"
              note: "A consumer asks for retained material; selection and response fulfill that request."
          records:
            - "runtime.md#rt-rte-context-recall"
            - "memory.md#mem-rte-wisdom-match"
            - "memory.md#mem-rte-alternate-read"
          note: "A skill recommendation to recall does not itself make delivery push."
        -
          scope: "Existing candidate facts/summaries in document-triggered librarian invocation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
              note: "Code automatically supplies selected existing content when a document triggers synthesis, without a model request for those retained parts."
          records:
            - "runtime.md#rt-rte-librarian-synthesis"
          note: "This automatic candidate selection is distinct from returning the model's output."
        -
          scope: "Recall-triggered verification prompting"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-verification-prompt"
              note: "An automatic selector queues review and later displays selected current facts to the operator."
          records:
            - "memory.md#mem-rte-verification-prompt"
          note: "The pushed recipient is the desktop operator, not an automatically injected external agent context."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "runtime.md#rt-rte-context-recall"
        - "memory.md#mem-rte-wisdom-match"
        - "memory.md#mem-rte-alternate-read"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "memory.md#mem-rte-verification-prompt"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "Both pull and push exist locally; external-engine and untraced alternative consumer routes prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Librarian candidate selection on document processing"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
              note: "Trigger: document synthesis. Input: mean chunk embeddings. Selected part: candidate entities and associated summaries/facts."
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
              note: "Trigger: document synthesis. Input: source name hits. Selected part: candidate entities and their retained content."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-librarian-synthesis"
              note: "Candidate/fact caps, recency and summary clipping bound delivery separately from targeted candidate matching."
          records:
            - "runtime.md#rt-rte-librarian-synthesis"
          note: "The aggregate 4,000-character prefix budget can omit selected suffix material."
        -
          scope: "Desktop verification prompt selection"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-verification-prompt"
              note: "Trigger: non-human-tier recall hit and later capped drain. Source type, unacked status and drain cap determine eligibility/budget."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-verification-prompt"
              note: "Trigger: prompt drain. Queued fact_id is matched to the live database row; current content, not stored display snapshot, is supplied."
          records:
            - "memory.md#mem-rte-verification-prompt"
          note: "The exact-ID reread is an actual identity selector within the push chain."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "runtime.md#rt-rte-librarian-synthesis"
        - "memory.md#mem-rte-verification-prompt"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "Signals classify automatic supply, not the selectors on requested pull results. CTI injection is excluded; opaque engine delivery remains unresolved."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Agent finding deposit through automatic librarian admission and later recall"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
            - "runtime.md#rt-rte-librarian-synthesis"
            - "runtime.md#rt-rte-proposal-admission"
            - "runtime.md#rt-clm-agent-workflow"
          note: "Automatic derived-content production and later consumption exist, but the original caller text is not established as traces. The protocol alone establishes neither a qualifying trace-fed write nor bounded absence."
        -
          scope: "Human capture/edit/verification, operational ledgers and maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-human-maintenance"
            - "memory.md#mem-rte-verification-state"
            - "memory.md#mem-rte-memory-withdrawal"
            - "memory.md#mem-obj-unverified-match"
          note: "These inspected paths do not establish automatic trace-fed production of durable behavior-shaping artifacts; no bounded absence record warrants a local no."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "memory.md#mem-obj-source-material"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "runtime.md#rt-rte-proposal-admission"
        - "runtime.md#rt-clm-agent-workflow"
        - "memory.md#mem-rte-human-maintenance"
        - "memory.md#mem-rte-verification-state"
        - "memory.md#mem-rte-memory-withdrawal"
        - "memory.md#mem-obj-unverified-match"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "No controlled yes or no follows from the accepted records: trace origin and opaque alternative updates remain unresolved. Stored vectors do not establish weight training; missing operation evidence is not absence."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Potential experience-derived agent deposits"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
            - "runtime.md#rt-clm-agent-workflow"
            - "runtime.md#rt-rte-librarian-synthesis"
          note: "No original recorded conversational turns, tool results, environmental event feed or linked trajectories are established as the automatic update's input."
        -
          scope: "Verification event queue and metadata updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-unverified-match"
            - "memory.md#mem-rte-verification-prompt"
            - "memory.md#mem-rte-verification-state"
          note: "The queue records events but is not established as input to a qualifying automatic trace-learning transformation."
        -
          scope: "External wiki-engine retained output and alternative import, merge/draft, replay and replica mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-obj-wiki-content"
          note: "The accepted inventory includes these alternatives but does not establish their internal retained parts or complete operation semantics; a known local witness cannot resolve them."
      records:
        - "memory.md#mem-obj-source-material"
        - "runtime.md#rt-clm-agent-workflow"
        - "runtime.md#rt-rte-librarian-synthesis"
        - "memory.md#mem-obj-unverified-match"
        - "memory.md#mem-rte-verification-prompt"
        - "memory.md#mem-rte-verification-state"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-wiki-content"
      note: "No qualifying automatic trace-fed route has established source content. This axis is not inapplicable because complete bounded absence of trace learning is not established."
---

# Curated Thoughts memory profile

## Comparison rationale

The profile classifies accepted records, not fresh source evidence. All positive findings use implementation wiring, not observed operation or causal benefit. No source files were read for this mapping. Reconciliation supplied no supersessions: broader runtime routes and narrower epistemic parts remain valid at their own scopes.

The retained-content inventory is wider than the fact prose alone. [MEM-OBJ-source-material](memory.md#mem-obj-source-material), [MEM-OBJ-wiki-content](memory.md#mem-obj-wiki-content), [MEM-OBJ-embedding-blobs](memory.md#mem-obj-embedding-blobs) and [MEM-OBJ-verification-ledgers](memory.md#mem-obj-verification-ledgers) establish separate prose, numerical and symbolic parts. Graph-shaped SQLite rows do not establish graph storage, and embedding blobs do not establish a separate vector store. Provider parameters and shipped static prompts are not substituted for use-accumulated memory.

Authority follows the actual consumer. Fact prose is knowledge at the caller and librarian; vectors and scored prose are ranking inputs. Ledger keys and lifecycle metadata have symbolic eligibility and conformance effects. The proposal watermark and queued IDs route later work. [MEM-BAP-retained-fact](memory.md#mem-bap-retained-fact), [MEM-RTE-verification-state](memory.md#mem-rte-verification-state), [MEM-RTE-wisdom-match](memory.md#mem-rte-wisdom-match) and [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis) support these distinctions. “Guidance” does not by itself turn a recalled fact into a standing instruction. No learning authority is inferred without the qualifying update consumer.

The proposal filter and live-anchor commit check are successive mechanisms, not interchangeable truth checks. [EPI-RTE-evidence-filter](epistemic.md#epi-rte-evidence-filter) can keep a nonempty proposal after unknown references disappear; [EPI-RTE-anchor-check](epistemic.md#epi-rte-anchor-check) can still veto insertion. Manual review and folder-driven automatic approval remain distinct admission units in [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission). Neither generic CLI identity nor workflow initiation proves a per-content human decision.

Curation findings describe implemented transformations. Normalized-body duplicate rejection in [EPI-RTE-fact-retention](epistemic.md#epi-rte-fact-retention) is deduplication; direct replacement is evolution; soft withdrawal is invalidation; delayed physical forgetting is decay; human-tier confirmation is promotion. The model's semantic relation to its inputs remains indeterminate in [EPI-OBJ-proposal-items](epistemic.md#epi-obj-proposal-items). Thus the name “synthesis” does not establish new-claim synthesis, and requested summaries alone do not establish implemented consolidation. [EPI-RTE-supersession-pending](epistemic.md#epi-rte-supersession-pending) also prevents treating a retained correction request as an applied revision.

External requests are pull. Internal candidate supply on document processing and unsolicited desktop review prompts are push, each with its own selector. [MEM-RTE-verification-prompt](memory.md#mem-rte-verification-prompt) establishes an actual queued-ID match to current retained content, unlike an identifier merely printed in a requested result. Candidate name/vector targeting and coarse caps remain separate findings on [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis). The opaque external-engine route in [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) is not made known by these local witnesses.

Trace learning remains not determinable, not absent. [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow) requests post-task findings, but [MEM-OBJ-source-material](memory.md#mem-obj-source-material) explicitly leaves their experience, copied-material or model origin unresolved. The recorded queue event in [MEM-OBJ-unverified-match](memory.md#mem-obj-unverified-match) is not itself a durable derived lesson. No accepted bounded absence record permits a local “no,” and no established original trace input permits a supported “yes” or trace-source value. Provider and external-engine opacity remain local limitations rather than negative learning conclusions.

The unresolved import, engine, identity/draft, replay and replica paths named in [MEM-OBJ-wiki-content](memory.md#mem-obj-wiki-content) and [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) prevent complete inventories. Supported findings survive those gaps, but no axis with classified findings claims complete system coverage. No retained reasons, confidence stamp or successful return is treated as proof of factual correctness, actual later use or improved capacity.
