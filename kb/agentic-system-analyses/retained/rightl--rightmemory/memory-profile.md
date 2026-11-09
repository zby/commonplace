---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "RightMemory memory comparison across canonical documents, evidence, correction cases, retrieval continuity, maintenance and shared-view paths."
run-id: "AAS-2026-11-08-rightmemory-cbec05309c2b-01"
source-identity: "https://github.com/rightl/rightmemory"
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
memory-comparison:
  version: 2
  scope: "Accumulated Memory/Pursuit graph and backing evidence/instructions; Agent Corrections and edit feedback; submissions, inbox and batches; retrieval snapshots, coverage, opaque provider continuation and vector cache; maintenance logs/history and operation/editor state; shared-view documents, policy, permissions, imports and feedback. Includes uncertain initialization and remote/provider alternatives. Excludes static shipped package policy/configuration, external inference weights, transient current requests/results without established retention, and the enclosing host's unrelated state."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Local semantic documents, evidence, snapshots, queue/batch records, shared artifacts, editor and operation state"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-markdown-evidence"
                - "memory.md#mem-obj-memory-skill"
                - "memory.md#mem-obj-pursuits"
                - "memory.md#mem-obj-agent-corrections"
                - "memory.md#mem-obj-edit-feedback"
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-guidance-inbox"
                - "memory.md#mem-obj-retrieve-context"
                - "memory.md#mem-obj-insight-logs"
                - "memory.md#mem-obj-shared-view"
              note: "Markdown and JSON/TOML retain content and access state."
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-agent-corrections"
                - "runtime.md#rt-obj-semantic-operation"
              note: "Git retains canonical documents and operation/history state."
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-pursuits"
              note: "Parsed IDs, typed edges and recursive roots organize the retained document trees."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-markdown-evidence"
            - "memory.md#mem-obj-memory-skill"
            - "memory.md#mem-obj-pursuits"
            - "memory.md#mem-obj-agent-corrections"
            - "memory.md#mem-obj-edit-feedback"
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-guidance-inbox"
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-insight-logs"
            - "memory.md#mem-obj-shared-view"
          note: "Known local substrate; not an assertion that every file belongs to the graph."
        -
          scope: "Derived retained passage vectors"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "JSON cache persists numerical vectors."
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
                - "runtime.md#rt-rte-embedding-retrieval"
              note: "Reusable dense-vector index supplies similarity retrieval."
          records:
            - "memory.md#mem-obj-vectors"
            - "runtime.md#rt-rte-embedding-retrieval"
          note: "Cache is indexing state, not model weights."
        -
          scope: "Provider-managed continuation payload"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieve-context"
          note: "Provider persistence internals are not described sufficiently to classify their substrate."
      records:
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-markdown-evidence"
        - "memory.md#mem-obj-memory-skill"
        - "memory.md#mem-obj-pursuits"
        - "memory.md#mem-obj-agent-corrections"
        - "memory.md#mem-obj-edit-feedback"
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-guidance-inbox"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-insight-logs"
        - "memory.md#mem-obj-shared-view"
        - "memory.md#mem-obj-vectors"
        - "runtime.md#rt-rte-embedding-retrieval"
      note: "Local file/repository/graph/vector findings coexist with unresolved provider continuation storage. External inference weights and static package policy are not accumulated memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Document prose, evidence, correction contrasts, instructions, snapshots and logs at model/host consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-markdown-evidence"
                - "memory.md#mem-obj-memory-skill"
                - "memory.md#mem-obj-pursuits"
                - "memory.md#mem-obj-agent-corrections"
                - "memory.md#mem-obj-edit-feedback"
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-guidance-inbox"
                - "memory.md#mem-obj-retrieve-context"
                - "memory.md#mem-obj-insight-logs"
                - "memory.md#mem-obj-shared-view"
              note: "Meaning is supplied through model or human interpretation, including complete S instructions and provider retriever policy."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-markdown-evidence"
            - "memory.md#mem-obj-memory-skill"
            - "memory.md#mem-obj-pursuits"
            - "memory.md#mem-obj-agent-corrections"
            - "memory.md#mem-obj-edit-feedback"
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-guidance-inbox"
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-insight-logs"
            - "memory.md#mem-obj-shared-view"
          note: "Natural-language parts exclude fixed-rule access fields."
        -
          scope: "IDs, graph edges, delivery coverage, cache keys, recipe permission and operation/editor state at code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-retrieve-context"
                - "memory.md#mem-obj-vectors"
                - "epistemic.md#epi-obj-view-permission"
                - "runtime.md#rt-obj-semantic-operation"
                - "runtime.md#rt-rte-pursuit-editor"
              note: "Localized fields have fixed selection, validity, permission and replay effects."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-vectors"
            - "epistemic.md#epi-obj-view-permission"
            - "runtime.md#rt-obj-semantic-operation"
            - "runtime.md#rt-rte-pursuit-editor"
          note: "These are separate operative parts from the prose."
        -
          scope: "Cached dense passage representations"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "Dense distributed numerical representations are consumed by similarity scoring, not as explicit rules."
          records:
            - "memory.md#mem-obj-vectors"
          note: "This does not classify the cache as learned weights."
        -
          scope: "Opaque provider continuation payload beyond described history"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieve-context"
          note: "Readable snapshots and thread IDs do not expose all consumed continuation representations."
      records:
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-markdown-evidence"
        - "memory.md#mem-obj-memory-skill"
        - "memory.md#mem-obj-pursuits"
        - "memory.md#mem-obj-agent-corrections"
        - "memory.md#mem-obj-edit-feedback"
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-guidance-inbox"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-insight-logs"
        - "memory.md#mem-obj-shared-view"
        - "memory.md#mem-obj-vectors"
        - "epistemic.md#epi-obj-view-permission"
        - "runtime.md#rt-obj-semantic-operation"
        - "runtime.md#rt-rte-pursuit-editor"
      note: "Mixed local parts are split by consumption; provider payload form remains unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Subsequent submitted-interaction reconciliation into Memory and correction cases"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-agent-corrections"
                - "runtime.md#rt-rte-isolated-update"
              note: "The supported branch derives reusable guidance/cases from submitted agent actions, user responses and outcomes."
          records:
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-agent-corrections"
            - "runtime.md#rt-rte-isolated-update"
          note: "Only the interaction-evidence branch, not every submission."
        -
          scope: "Human Pursuit edits and approved host guidance authorship"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pursuit-editor"
                - "memory.md#mem-obj-pursuits"
              note: "Human-facing editor supplies direction content."
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-guidance-review"
                - "runtime.md#rt-rte-manual-maintenance"
              note: "Host writes requested or approved semantic content under explicit procedures."
          records:
            - "runtime.md#rt-rte-pursuit-editor"
            - "memory.md#mem-obj-pursuits"
            - "memory.md#mem-rte-guidance-review"
            - "runtime.md#rt-rte-manual-maintenance"
          note: "Authorship is distinct from admission control."
        -
          scope: "Synchronized and mirrored external content"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sync-admission"
                - "runtime.md#rt-rte-file-import"
                - "memory.md#mem-obj-shared-view"
              note: "Incoming state and external distributions supply retained local content."
          records:
            - "runtime.md#rt-rte-sync-admission"
            - "runtime.md#rt-rte-file-import"
            - "memory.md#mem-obj-shared-view"
          note: "Remote initial authorship and factual warrant remain outside this import lineage."
        -
          scope: "Snapshots, vectors, extractive distributions and generated view artifacts"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieve-context"
                - "memory.md#mem-obj-vectors"
                - "epistemic.md#epi-rte-view-build"
              note: "Root projection, vector encoding and view generation derive representations from retained material."
          records:
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-vectors"
            - "epistemic.md#epi-rte-view-build"
          note: "Compilation here does not imply semantic equivalence of generative output."
        -
          scope: "Real preexisting roots, edit-feedback initialization and mixed submission origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-edit-feedback"
            - "memory.md#mem-obj-update-evidence"
          note: "Sample copying does not establish real initial provenance; generic caller/session labels cannot classify every input."
      records:
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-agent-corrections"
        - "runtime.md#rt-rte-isolated-update"
        - "runtime.md#rt-rte-pursuit-editor"
        - "memory.md#mem-obj-pursuits"
        - "memory.md#mem-rte-guidance-review"
        - "runtime.md#rt-rte-manual-maintenance"
        - "runtime.md#rt-rte-sync-admission"
        - "runtime.md#rt-rte-file-import"
        - "memory.md#mem-obj-shared-view"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-vectors"
        - "epistemic.md#epi-rte-view-build"
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-edit-feedback"
      note: "Known subsequent derivation/import routes do not resolve real initial population or every upstream input."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained prose supplied to retrieval, foreground hosts and maintenance models as context"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-markdown-evidence"
                - "memory.md#mem-obj-agent-corrections"
                - "memory.md#mem-obj-insight-logs"
                - "runtime.md#rt-bap-host-context"
              note: "Facts, evidence, case contrasts and prior logs inform interpretation and work."
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-skill"
                - "memory.md#mem-obj-memory"
                - "epistemic.md#epi-obj-retriever-policy"
                - "memory.md#mem-rte-question-view"
              note: "Standing guidance, complete playbooks and provider policy direct model behavior when supplied."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-markdown-evidence"
            - "memory.md#mem-obj-agent-corrections"
            - "memory.md#mem-obj-insight-logs"
            - "memory.md#mem-obj-memory-skill"
            - "epistemic.md#epi-obj-retriever-policy"
            - "memory.md#mem-rte-question-view"
            - "runtime.md#rt-bap-host-context"
          note: "Supply/consumer force is wired; obedience is unobserved."
        -
          scope: "Retained interaction evidence and edit feedback at automatic semantic-update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-edit-feedback"
                - "runtime.md#rt-rte-isolated-update"
              note: "Experience and correction exemplars shape durable Memory/case revisions rather than parameters."
          records:
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-edit-feedback"
            - "runtime.md#rt-rte-isolated-update"
          note: "Learning force here is update use, not measured improved capacity."
        -
          scope: "Retained text, vectors and access/control metadata at deterministic selectors and gates"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
                - "runtime.md#rt-rte-embedding-retrieval"
              note: "Retained text/vector features affect relative retrieval priority."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieve-context"
                - "runtime.md#rt-obj-semantic-operation"
                - "memory.md#mem-rte-opening-context"
              note: "Coverage, operation phases and graph identity/edges select later inputs or actions."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-view-permission"
                - "memory.md#mem-rte-question-view"
              note: "Unapproved retained permission blocks answering."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
                - "epistemic.md#epi-rte-view-approval"
              note: "Retained model/root cache identity and recipe selections supply conformity checks."
          records:
            - "memory.md#mem-obj-vectors"
            - "runtime.md#rt-rte-embedding-retrieval"
            - "memory.md#mem-obj-retrieve-context"
            - "runtime.md#rt-obj-semantic-operation"
            - "memory.md#mem-rte-opening-context"
            - "epistemic.md#epi-obj-view-permission"
            - "memory.md#mem-rte-question-view"
            - "epistemic.md#epi-rte-view-approval"
          note: "Only actual consumed parts have these forces; unconsumed metadata is not authority."
        -
          scope: "Opaque provider continuation and untraced note/completed-batch later consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-shared-view"
            - "memory.md#mem-obj-update-evidence"
          note: "Internal consumer force and additional automatic adoption are not established by thread/storage/listing APIs."
      records:
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-markdown-evidence"
        - "memory.md#mem-obj-agent-corrections"
        - "memory.md#mem-obj-insight-logs"
        - "memory.md#mem-obj-memory-skill"
        - "epistemic.md#epi-obj-retriever-policy"
        - "memory.md#mem-rte-question-view"
        - "runtime.md#rt-bap-host-context"
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-edit-feedback"
        - "runtime.md#rt-rte-isolated-update"
        - "memory.md#mem-obj-vectors"
        - "runtime.md#rt-rte-embedding-retrieval"
        - "memory.md#mem-obj-retrieve-context"
        - "runtime.md#rt-obj-semantic-operation"
        - "memory.md#mem-rte-opening-context"
        - "epistemic.md#epi-obj-view-permission"
        - "epistemic.md#epi-rte-view-approval"
        - "memory.md#mem-obj-shared-view"
      note: "Authority is local to the named consumer; package-owned static criteria are excluded. No activation or benefit follows from delivery."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Internal/native Update, capture, maintenance and derived local bookkeeping admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-isolated-update"
                - "runtime.md#rt-rte-native-assistant"
                - "epistemic.md#epi-rte-guidance-capture"
                - "runtime.md#rt-rte-maintenance-cycles"
                - "memory.md#mem-obj-retrieve-context"
                - "memory.md#mem-obj-vectors"
              note: "Models/code admit content or derived state without per-content human approval."
          records:
            - "runtime.md#rt-rte-isolated-update"
            - "runtime.md#rt-rte-native-assistant"
            - "epistemic.md#epi-rte-guidance-capture"
            - "runtime.md#rt-rte-maintenance-cycles"
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-vectors"
          note: "Evidence-submission approval in a host mode is not approval of final Update wording."
        -
          scope: "Human browser direction edits and explicitly approved inbox proposals"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pursuit-editor"
              note: "The evidenced human-facing editor supplies selected direction changes."
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-guidance-review"
              note: "Explicit approval of each semantic proposal authorizes host curation."
          records:
            - "runtime.md#rt-rte-pursuit-editor"
            - "memory.md#mem-rte-guidance-review"
          note: "Generic Pursuit API callers are not covered by the human-facing witness."
        -
          scope: "Sync/import and semantic view refresh publication"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sync-admission"
                - "runtime.md#rt-rte-file-import"
                - "memory.md#mem-rte-view-refresh"
              note: "Software publishes validated incoming/refreshed state; refresh carries old approval forward."
          records:
            - "runtime.md#rt-rte-sync-admission"
            - "runtime.md#rt-rte-file-import"
            - "memory.md#mem-rte-view-refresh"
          note: "Prior configuration or approval does not make refreshed wording manually admitted."
        -
          scope: "Existing root/edit-feedback initialization, generic view approval and broad requested maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-edit-feedback"
            - "epistemic.md#epi-rte-view-approval"
            - "runtime.md#rt-rte-manual-maintenance"
          note: "Initial control and generic caller identities are unresolved; a broad request alone need not approve each host-chosen revision."
      records:
        - "runtime.md#rt-rte-isolated-update"
        - "runtime.md#rt-rte-native-assistant"
        - "epistemic.md#epi-rte-guidance-capture"
        - "runtime.md#rt-rte-maintenance-cycles"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-vectors"
        - "runtime.md#rt-rte-pursuit-editor"
        - "memory.md#mem-rte-guidance-review"
        - "runtime.md#rt-rte-sync-admission"
        - "runtime.md#rt-rte-file-import"
        - "memory.md#mem-rte-view-refresh"
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-edit-feedback"
        - "epistemic.md#epi-rte-view-approval"
        - "runtime.md#rt-rte-manual-maintenance"
      note: "Classifies admission, not physical writes or authorship; unknown principals remain separate from explicit human decisions."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Update canonical reconciliation and bounded correction-set maintenance"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-isolated-update"
                - "memory.md#mem-obj-agent-corrections"
              note: "Semantic reconciliation can reduce submitted interaction evidence into reusable scoped context/cases."
            -
              value: "dedup"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-isolated-update"
                - "memory.md#mem-obj-memory"
              note: "Keep/merge/skip judgments remove overlap rather than retaining every candidate."
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-isolated-update"
                - "memory.md#mem-obj-memory"
              note: "Role-directed edits revise existing canonical content."
          records:
            - "runtime.md#rt-rte-isolated-update"
            - "memory.md#mem-obj-agent-corrections"
            - "memory.md#mem-obj-memory"
          note: "Model transformations are afforded by executable edit/publication machinery and semantic instructions, not observed compliant outputs."
        -
          scope: "Pruner reduction of the active retained corpus"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-maintenance-cycles"
              note: "Semantic age/use/grace judgment can forget active items while Git history remains."
          records:
            - "runtime.md#rt-rte-maintenance-cycles"
          note: "Not FIFO; requested deletions are not proof of falsehood or actual execution."
        -
          scope: "Extractive shared-view rendering"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-view-build"
                - "epistemic.md#epi-obj-view-document"
              note: "Deterministic selection reduces provider material to a distribution of surviving source claims."
          records:
            - "epistemic.md#epi-rte-view-build"
            - "epistemic.md#epi-obj-view-document"
          note: "Compiler/index rebuild alone is not the warrant; source selection is."
        -
          scope: "Insight and generative shared-view semantic transformations; opaque provider maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-insight-logs"
            - "epistemic.md#epi-rte-view-build"
            - "memory.md#mem-obj-retrieve-context"
          note: "No concrete new proposition or semantic-preservation evidence resolves synthesis versus other transformations; provider internals remain opaque."
      records:
        - "runtime.md#rt-rte-isolated-update"
        - "memory.md#mem-obj-agent-corrections"
        - "memory.md#mem-obj-memory"
        - "runtime.md#rt-rte-maintenance-cycles"
        - "epistemic.md#epi-rte-view-build"
        - "epistemic.md#epi-obj-view-document"
        - "memory.md#mem-obj-insight-logs"
        - "memory.md#mem-obj-retrieve-context"
      note: "Conservative evidence layers retain afforded semantic operations and wired extraction separately. Requested novelty, cache eviction and graph validation do not establish synthesis, invalidation or promotion."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested internal/native retrieval, explicit provider question and opening-context return"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agent-retrieval"
                - "runtime.md#rt-rte-embedding-retrieval"
                - "runtime.md#rt-rte-native-assistant"
                - "memory.md#mem-rte-question-view"
                - "memory.md#mem-rte-opening-context"
              note: "A consumer requests context, question response or a map projection; delivery fulfills that request."
          records:
            - "runtime.md#rt-rte-agent-retrieval"
            - "runtime.md#rt-rte-embedding-retrieval"
            - "runtime.md#rt-rte-native-assistant"
            - "memory.md#mem-rte-question-view"
            - "memory.md#mem-rte-opening-context"
          note: "Model/ranker selection inside a requested return is not another unsolicited push."
        -
          scope: "Automatic retained-context supply inside internal role invocations"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agent-retrieval"
                - "memory.md#mem-obj-retrieve-context"
                - "runtime.md#rt-rte-maintenance-cycles"
              note: "New-conversation snapshots, changed/pending/delivery notices and role maintenance history are supplied without a separate request for each retained part."
          records:
            - "runtime.md#rt-rte-agent-retrieval"
            - "memory.md#mem-obj-retrieve-context"
            - "runtime.md#rt-rte-maintenance-cycles"
          note: "Envelope supply and requested terminal retrieval are separate operations."
        -
          scope: "Provider continuation internals and untraced completed-batch/provider-note consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-shared-view"
          note: "Storage and listing do not establish every later delivery route."
      records:
        - "runtime.md#rt-rte-agent-retrieval"
        - "runtime.md#rt-rte-embedding-retrieval"
        - "runtime.md#rt-rte-native-assistant"
        - "memory.md#mem-rte-question-view"
        - "memory.md#mem-rte-opening-context"
        - "memory.md#mem-obj-retrieve-context"
        - "runtime.md#rt-rte-maintenance-cycles"
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-shared-view"
      note: "Known pull and push coexist; opaque alternatives prevent complete inventory coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Internal retrieval automatic snapshot/pending/change envelope"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agent-retrieval"
                - "memory.md#mem-obj-retrieve-context"
              note: "New conversation triggers root snapshot; commit/visibility changes trigger broad diffs or pending notices, not semantic targeting."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieve-context"
                - "runtime.md#rt-rte-agent-retrieval"
              note: "Changed-delivery supply compares retained session delivery coverage/source identities with current sources to target notices about previously delivered parts."
          records:
            - "runtime.md#rt-rte-agent-retrieval"
            - "memory.md#mem-obj-retrieve-context"
          note: "Trigger, input and selected part are the conversation/change condition, saved coverage/current versions, and envelope snapshot/notices. Explicit include-returned remains pull."
        -
          scope: "Other role-history supply and opaque provider selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-maintenance-cycles"
            - "memory.md#mem-obj-edit-feedback"
            - "memory.md#mem-obj-retrieve-context"
          note: "Prompts identify history/feedback use, but records do not fully resolve every automatic selector's inputs and selected payload. No inferred signal is assigned from requested retrieval ranking alone."
      records:
        - "runtime.md#rt-rte-agent-retrieval"
        - "memory.md#mem-obj-retrieve-context"
        - "runtime.md#rt-rte-maintenance-cycles"
        - "memory.md#mem-obj-edit-feedback"
      note: "Signals classify push only; numerical/model selection for a requested return does not establish an inferred push signal."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic Update of Memory/rules and correction cases from submitted interaction evidence"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-agent-corrections"
                - "runtime.md#rt-rte-isolated-update"
                - "runtime.md#rt-bap-host-context"
              note: "Submitted actions, user redirections and outcomes feed automatic durable guidance/case writes that can reach future hosts through retrieval."
          records:
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-agent-corrections"
            - "runtime.md#rt-rte-isolated-update"
            - "runtime.md#rt-bap-host-context"
          note: "This is a supported qualifying branch, not a claim that all submissions are traces or that capacity improved."
        -
          scope: "Opaque provider continuation transformations, mixed-origin updates and other untraced feedback adoption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-edit-feedback"
            - "memory.md#mem-obj-shared-view"
          note: "No complete input/update/consumer inventory exists for provider summaries or every feedback-writing route. Raw retention and vector indexing do not alone establish learning."
      records:
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-agent-corrections"
        - "runtime.md#rt-rte-isolated-update"
        - "runtime.md#rt-bap-host-context"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-edit-feedback"
        - "memory.md#mem-obj-shared-view"
      note: "A wired yes survives unresolved alternatives. No local or system-wide no is warranted: the accepted set declares no bounded absence record for this inventory."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Interaction-evidence branch of automatic Update to future guidance/cases"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-update-evidence"
                - "memory.md#mem-obj-agent-corrections"
                - "runtime.md#rt-rte-isolated-update"
              note: "Recorded prior agent work, conversational user redirection and settled responses/outcomes supply the qualifying write."
          records:
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-agent-corrections"
            - "runtime.md#rt-rte-isolated-update"
          note: "A submitted excerpt can carry session evidence without constituting a complete transcript."
        -
          scope: "Other mixed submissions and opaque provider/feedback trace-fed alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-update-evidence"
            - "memory.md#mem-obj-retrieve-context"
            - "memory.md#mem-obj-edit-feedback"
          note: "Generic session IDs do not identify original content. Tool requests/results, linked trajectories and environmental events are not established for these alternatives."
      records:
        - "memory.md#mem-obj-update-evidence"
        - "memory.md#mem-obj-agent-corrections"
        - "runtime.md#rt-rte-isolated-update"
        - "memory.md#mem-obj-retrieve-context"
        - "memory.md#mem-obj-edit-feedback"
      note: "Only evidenced original interaction content is classified; queue events and adapter labels do not add event-streams, tool-traces or trajectories."
---

# RightMemory memory profile

## Comparison rationale

The comparison covers retained content and its access/maintenance state, not every storage object in the runtime. File persistence, repository history and graph organization coexist; dense retained vectors are classified separately from external inference weights. Natural-language content, fixed-rule identity/control fields and distributed numerical vectors have different consumers. Provider-managed continuation is included but unresolved rather than inferred from readable snapshots. See [MEM-OBJ-memory](memory.md#mem-obj-memory), [MEM-OBJ-retrieve-context](memory.md#mem-obj-retrieve-context) and [MEM-OBJ-vectors](memory.md#mem-obj-vectors).

Automatic Update is a qualifying trace-learning route when its submitted evidence records agent work and user redirection: a semantic model admits durable guidance/cases and later retrieval supplies them to a host. That supports a wired local "yes", not observed improvement, universal trace provenance, weight training or successful self-improvement. Ordinary document import and raw history retention are different paths. Opaque continuation processing and mixed submissions remain separate unresolved units. See [MEM-OBJ-update-evidence](memory.md#mem-obj-update-evidence), [MEM-OBJ-agent-corrections](memory.md#mem-obj-agent-corrections), [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) and [RT-BAP-host-context](runtime.md#rt-bap-host-context).

Curation uses conservative evidence layers. Models are afforded keep/merge/revise and pruning operations through the executable roles and their semantic instructions; the source does not supply compliant output traces. Extractive distribution selection is deterministic and wired. Generative view production and Insight requests do not establish a newly synthesized claim without a recorded input/output relation. A faithfulness defect would not itself prove synthesis. See [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), [EPI-RTE-view-build](epistemic.md#epi-rte-view-build) and [MEM-OBJ-insight-logs](memory.md#mem-obj-insight-logs).

Requested retrieval remains pull even when models or numerical ranking select its answer. Internal snapshot/diff/pending/changed-delivery additions are a distinct automatic supply operation. The identifier finding concerns saved delivery coverage identifying changed previously delivered sources, not merely IDs in a requested selector. Opening-context projection fulfills an explicit consumer request; graph adjacency does not independently establish identifier-based push. See [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [MEM-OBJ-retrieve-context](memory.md#mem-obj-retrieve-context) and [MEM-RTE-opening-context](memory.md#mem-rte-opening-context).

Write agency follows admission: native/internal semantic edits and refresh are automatic despite upstream workflow initiation. Human editor decisions and explicit inbox-proposal approval establish local manual routes. Generic approval callers and initial feedback population remain unresolved. Permission flags enforce sharing/answer eligibility; they are not factual acceptance. See [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant), [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor), [MEM-RTE-guidance-review](memory.md#mem-rte-guidance-review), [MEM-RTE-view-refresh](memory.md#mem-rte-view-refresh) and [EPI-OBJ-view-permission](epistemic.md#epi-obj-view-permission).

Reconciliation supersedes the epistemic correction-case, edit-feedback, inbox, Insight-log and shared-view container declarations with the corresponding memory declarations. It supersedes the epistemic provider-question route with the memory question-view route. All classifications use these canonical records; the declared epistemic view-document, retriever-policy and permission parts remain distinct. The broader epistemic Memory container is not substituted for any single memory part. These identity resolutions change citation targets, not evidence strength or coverage.

Every axis retains unresolved included coverage rather than inferring complete enumeration from a positive witness. Actual deployments, initial content control, provider payload internals, full remote transport/withdrawal behavior and additional feedback adoption are not resolved by these records. No bounded absence record supports a trace-learning negative. No observed or causal basis is asserted.

Source-read log: no source files were read. This classification uses only the supplied accepted members and reconciliation; no additional quotations, records or evidence were introduced.
