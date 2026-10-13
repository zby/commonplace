---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory comparison of claude-obsidian: retained user-vault knowledge, context, access structures,
  configuration and recovery state at the frozen commit.'
run-id: AAS-2026-10-13-claude-obsidian-c5e56e25c8bb-01
source-identity: https://github.com/AgriciDaniel/claude-obsidian
reviewed-boundary: 32ac5a02c4e082e4a5628ca810776375e134708e
memory-comparison:
  version: 2
  scope: Package-owned retained user-vault pages/navigation/hot, raw payloads and provenance, operation
    log/folds, Canvas/Bases views, manifest and filing/threshold configuration, chunks/BM25 and rerank/tiling
    caches, capture queue/predecessor, transaction backups/journals/results and optional Git checkpoint
    history/metadata; includes unresolved initial/adopted content, raw encodings and caller payloads.
    Excludes static installed skills/templates before use, transient unadmitted worker drafts and current
    host turns, external host compaction/checkpoints, provider-internal caches/weights and external renderer/service
    implementation.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Vault notes, orientation, navigation, logs/folds, raw payloads and ledgers, manifest, views,
          configuration, derived chunks/index/vectors, queue/predecessor and transaction/checkpoint metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-chunks
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          - memory.md#mem-obj-queue
          - runtime.md#rt-obj-transaction-bundle
          - runtime.md#rt-rte-save-apply
          note: Executable persistence and reload routes establish local files for raw, derived and recovery
            state.
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-log
          - memory.md#mem-obj-mode
          - memory.md#mem-obj-vault-views
          note: Model-facing knowledge and view workflows name retained local files; this does not show
            an actual user vault.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-log
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - memory.md#mem-obj-queue
        - memory.md#mem-obj-mode
        - memory.md#mem-obj-vault-views
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        note: Records identify these operative retained parts as local Markdown, JSON/YAML, binary files
          or original-byte backups; optional checkpoint metadata is local state.
      - scope: Optional operation-scoped Git checkpoint history
        assessment: known
        findings:
        - value: repo
          basis: wired
          records:
          - runtime.md#rt-rte-save-apply
          - epistemic.md#epi-rte-checkpoint-gate
          note: Explicit checkpoint construction consumes completed-operation paths and records Git history.
        records:
        - runtime.md#rt-rte-save-apply
        - epistemic.md#epi-rte-checkpoint-gate
        note: The memory annotation traces durable Git history as an alternative audit/recovery representation;
          it is not a model loader.
      records:
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-log
      - memory.md#mem-obj-chunks
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - memory.md#mem-obj-queue
      - memory.md#mem-obj-mode
      - memory.md#mem-obj-vault-views
      - runtime.md#rt-obj-transaction-bundle
      - runtime.md#rt-rte-save-apply
      - epistemic.md#epi-rte-checkpoint-gate
      note: The recorded package-owned inventory is file-backed; optional Git checkpoint history adds
        a repo substrate. Opaque raw bytes do not make their file substrate unknown. External host compaction
        and provider stores are excluded, not classified from service labels.
    representational_form:
      assessment: partial
      units:
      - scope: Wiki prose, hot orientation, log/fold text, claim text/notes, locators and view text cards
          at human/model readers
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-vault-views
          note: Readers interpret prose as context, evidence or organization.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-vault-views
        note: This unit covers the textual parts, not their structured metadata.
      - scope: Raw excerpts and generated prefix text at lexical retrieval and optional embedding consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-chunks
          - runtime.md#rt-rte-prefix-generation
          - epistemic.md#epi-rte-synthetic-prefix
          note: Contextualized text combines the retained prefix and raw excerpt; the displayed snippet
            is only raw text.
        records:
        - memory.md#mem-obj-chunks
        - runtime.md#rt-rte-prefix-generation
        - epistemic.md#epi-rte-synthetic-prefix
        note: Both synthetic and model tiers expose text rather than weights or opaque summaries.
      - scope: Frontmatter/links, ledger status/evidence relations, manifests, sparse postings, vector
          keys, queue state, mode, view layouts/filters and journal/checkpoint controls
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-chunks
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          - memory.md#mem-obj-queue
          - memory.md#mem-obj-mode
          - runtime.md#rt-obj-transaction-bundle
          - runtime.md#rt-rte-save-apply
          note: Executable consumers interpret JSON fields, hashes, keys, postings and control state.
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-vault-views
          note: Shipped procedures specify frontmatter, links and external renderer layouts/filters.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - memory.md#mem-obj-queue
        - memory.md#mem-obj-mode
        - memory.md#mem-obj-vault-views
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        note: Fixed schema, navigation, indexing, scheduling, routing and recovery consumers use localized
          structured fields.
      - scope: Rerank and tiling dense embedding vectors at cosine consumers
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          note: Cached dense vectors feed later cosine ranking/diagnosis; no weight update is implied.
        records:
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        note: Numerical distributed representations are distinct from their symbolic keys and thresholds.
      - scope: Original binary/opaque raw evidence and arbitrary queue completion payload content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        note: File retention and bounded JSON shape do not establish the encoding/semantic consumption
          of original raw evidence or all completion content. No live extracted payload or queue executor
          was supplied.
      records:
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-log
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-vault-views
      - memory.md#mem-obj-chunks
      - runtime.md#rt-rte-prefix-generation
      - epistemic.md#epi-rte-synthetic-prefix
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - memory.md#mem-obj-queue
      - memory.md#mem-obj-mode
      - runtime.md#rt-obj-transaction-bundle
      - runtime.md#rt-rte-save-apply
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-rte-queue-resumption
      note: Text, symbolic consumer state and dense numerical representations are established separately.
        Raw binary payload semantics and arbitrary caller completion payloads remain unresolved; no display
        summary substitutes for them.
    lineage:
      assessment: partial
      units:
      - scope: New model/human wiki, ledger, hot and view proposals in Save/Ingest/Research and organization
          workflows
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-vault-views
          - runtime.md#rt-rte-ingest-drafts
          - epistemic.md#epi-rte-canonical-integration
          note: Model/human drafts and assessments precede admission.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-vault-views
        - runtime.md#rt-rte-save-apply
        - runtime.md#rt-rte-ingest-drafts
        - epistemic.md#epi-rte-canonical-integration
        note: This unit describes the documented new-content path, not initial vault authorship.
      - scope: Selected conversation to Save notes/hot/log; selected operation accounts to fold text
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-save-apply
          - memory.md#mem-obj-log
          - memory.md#mem-rte-log-fold
          note: Save selects conversational knowledge; the fold asks for extractive themes/outcomes from
            authored operation entries. Faithful extraction is unobserved.
        records:
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        note: These derivations consume activity accounts, not independent source corroboration or a full
          transcript.
      - scope: Captured source payloads and setup seed content
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - runtime.md#rt-rte-direct-capture
          note: Capture retains source bytes; the setup builder can seed templates while adoption preserves
            existing files.
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - runtime.md#rt-rte-direct-capture
        note: Raw acquisition and template seeding are identifiable incoming paths; remote source truth
          is not established.
      - scope: Page-derived chunks/prefixes, sparse index, embedding caches and executable queue/journal/checkpoint
          transitions
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-chunks
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          - memory.md#mem-obj-queue
          - runtime.md#rt-obj-transaction-bundle
          - memory.md#mem-rte-chunk-maintenance
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          - memory.md#mem-rte-queue-resumption
          - runtime.md#rt-rte-save-apply
          note: Code compiles chunks/index, caches inference results and persists derived transition/recovery
            state.
        records:
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - memory.md#mem-obj-queue
        - runtime.md#rt-obj-transaction-bundle
        - memory.md#mem-rte-chunk-maintenance
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-rte-save-apply
        note: This unit classifies the recorded derivation from input content/state, not hidden provider
          initialization.
      - scope: User-selected filing mode and reviewed view/configuration changes
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-mode
          - memory.md#mem-obj-vault-views
          - runtime.md#rt-rte-mode-extension
          note: Users select mode/configuration; models draft requested views for review.
        records:
        - memory.md#mem-obj-mode
        - memory.md#mem-obj-vault-views
        - runtime.md#rt-rte-mode-extension
        note: Explicit configuration and drafted organization have a specified authorship path.
      - scope: Initial adopted wiki/hot/ledger/view content and original provenance behind inference vectors
          or caller-supplied queue payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-vault-views
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - memory.md#mem-obj-queue
        note: No live user-vault history, provider provenance or caller-content derivation was supplied;
          a known subsequent transform cannot resolve these origins.
      records:
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-vault-views
      - runtime.md#rt-rte-save-apply
      - runtime.md#rt-rte-ingest-drafts
      - epistemic.md#epi-rte-canonical-integration
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - runtime.md#rt-rte-direct-capture
      - memory.md#mem-obj-chunks
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - memory.md#mem-obj-queue
      - runtime.md#rt-obj-transaction-bundle
      - memory.md#mem-rte-chunk-maintenance
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-rte-queue-resumption
      - memory.md#mem-obj-mode
      - runtime.md#rt-rte-mode-extension
      note: Known production paths do not resolve initial adopted/user content or provider embedding provenance.
        Imported material and trace-derived proposals remain separate from mechanically compiled access
        structures.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Wiki/hot/claim text and source locators at later Query and drafting models
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-bap-vault-evidence
          - runtime.md#rt-rte-vault-query
          note: Current pages and ledgers guide evidence-grounded answers; hot is orientation only.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-hot
          - runtime.md#rt-rte-session-context
          note: The hook emits retained hot bytes as bounded untrusted context; actual host injection/effect
            is unobserved.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-bap-vault-evidence
        - runtime.md#rt-rte-vault-query
        - runtime.md#rt-rte-session-context
        note: The force is evidence/context under the installed rules, not standing directions or demonstrated
          obedience.
      - scope: Fold text at later discoverers and view text at afforded human/model readers
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-log
          - memory.md#mem-rte-log-fold
          - memory.md#mem-obj-vault-views
          note: Index-discoverable folds and inspectable view content supply history/organization to readers.
        records:
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-vault-views
        note: Cataloguing and organization afford contextual use, not a mandatory deployed loader.
      - scope: Contextualized chunk text/postings and rerank cached vectors at retrieval scoring; tiling
          vectors and bands at diagnostic scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-chunks
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          - runtime.md#rt-rte-vault-query
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          - epistemic.md#epi-rte-diagnostic-selection
          note: BM25, cosine ordering and configured bands consume retained inputs; truth judgment and
            learned ranking policy are not implied.
        records:
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - runtime.md#rt-rte-vault-query
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - epistemic.md#epi-rte-diagnostic-selection
        note: Fixed algorithms use retained text/features/vectors to prioritize candidates or diagnostic
          attention.
      - scope: Manifest source/hash identity, mode/folder config, queue state and checkpoint operation-path
          state at next-operation consumers
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-manifest
          note: Ingest uses source/manifest identity for unchanged-input and address decisions.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-mode
          - memory.md#mem-obj-queue
          - runtime.md#rt-rte-save-apply
          - memory.md#mem-rte-queue-resumption
          - memory.md#mem-bap-filing-config
          note: Mode helper suggests filing destinations; queue chooses claims/retries; checkpoint selects
            completed-operation paths.
        records:
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-mode
        - memory.md#mem-obj-queue
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-rte-queue-resumption
        - memory.md#mem-bap-filing-config
        note: These parts select work, destination, delta scope or checkpoint inputs rather than supply
          factual warrant.
      - scope: Source/claim support metadata at ledger validator and prospective transaction gate
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-claim-ledger
          - epistemic.md#epi-rte-ledger-check
          - epistemic.md#epi-rte-ledger-disposition
          note: Current/prospective metadata determines eligibility violations within validator semantics.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-claim-ledger
          - epistemic.md#epi-rte-ledger-check
          - epistemic.md#epi-rte-ledger-disposition
          note: Violations veto ledger-bearing transactions; no semantic truth test is performed.
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - epistemic.md#epi-rte-ledger-check
        - epistemic.md#epi-rte-ledger-disposition
        note: Retained status, freshness, review, independence and evidence links supply admission criteria.
      - scope: Journal/backups/results and queue tokens/state at recovery, replay and transition code
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-transaction-bundle
          - runtime.md#rt-rte-save-apply
          - memory.md#mem-obj-queue
          - memory.md#mem-rte-queue-resumption
          note: Stored hashes/modes, journals and claim tokens determine conformance of replay/recovery
            or queue updates.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-transaction-bundle
          - runtime.md#rt-rte-save-apply
          - memory.md#mem-obj-queue
          - memory.md#mem-rte-queue-resumption
          note: Drift, incompatible state or invalid tokens can refuse effects.
        records:
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        note: Original note backups are restoration bytes here, not Query evidence.
      - scope: Opaque raw payload consumption, arbitrary queue result consumers and rejected/deprecated
          downstream presentation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        - memory.md#mem-bap-vault-evidence
        note: Locators and state labels do not establish every actual payload consumer/effect; generic
          current-support rules do not prove complete semantic retraction.
      records:
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-bap-vault-evidence
      - runtime.md#rt-rte-vault-query
      - runtime.md#rt-rte-session-context
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-vault-views
      - memory.md#mem-obj-chunks
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - epistemic.md#epi-rte-diagnostic-selection
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-mode
      - memory.md#mem-obj-queue
      - runtime.md#rt-rte-save-apply
      - memory.md#mem-rte-queue-resumption
      - memory.md#mem-bap-filing-config
      - epistemic.md#epi-rte-ledger-check
      - epistemic.md#epi-rte-ledger-disposition
      - runtime.md#rt-obj-transaction-bundle
      note: The inventory establishes contextual, ranking, routing and computational gate effects at named
        consumers. Opaque raw/caller payload consumers and some downstream withdrawal/rendering effects
        remain unresolved. Static installed instructions and provider weights are outside this memory
        scope.
    write_agency:
      assessment: partial
      units:
      - scope: Explicit selected-content Save, reviewed canonical replacement/Research merge, forced fold
          replacement, mode and view changes
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-save-apply
          - epistemic.md#epi-rte-canonical-integration
          - memory.md#mem-rte-log-fold
          - runtime.md#rt-rte-mode-extension
          - memory.md#mem-obj-mode
          - memory.md#mem-obj-vault-views
          note: The human supplies selected content or reviews/approves the retained proposal; replacement/second
            merge have explicit decisions.
        records:
        - runtime.md#rt-rte-save-apply
        - epistemic.md#epi-rte-canonical-integration
        - memory.md#mem-rte-log-fold
        - runtime.md#rt-rte-mode-extension
        - memory.md#mem-obj-mode
        - memory.md#mem-obj-vault-views
        note: This unit is the prescribed operator decision, not a claim that every CLI invocation actually
          received human approval.
      - scope: Chunk/prefix admission, rerank vector cache and tiling cache publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-prefix-generation
          - memory.md#mem-rte-chunk-maintenance
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          note: Code accepts first-line prefixes or usable vectors and persists derived records without
            per-content human decisions.
        records:
        - runtime.md#rt-rte-prefix-generation
        - memory.md#mem-rte-chunk-maintenance
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        note: Workflow/egress initiation is separate from per-entry content admission.
      - scope: Transaction journal/result/backup persistence and queue runtime transition bookkeeping
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-obj-transaction-bundle
          - runtime.md#rt-rte-save-apply
          - memory.md#mem-obj-queue
          - memory.md#mem-rte-queue-resumption
          note: Executors persist recovery/replay and claim-transition state.
        records:
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        note: Software derives and admits operation evidence and state changes; this does not classify
          who supplied proposal/result content.
      - scope: Direct capture content decision; queue enqueue/result payload admission; initial adoption;
          CLI hash without authenticated review; optional checkpoint content choice
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-capture
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - runtime.md#rt-rte-save-apply
        - runtime.md#rt-rte-mode-extension
        note: Generic caller identity and a correct approval digest do not establish an explicit human
          per-content decision. No supplied trace resolves initialization or checkpoint human control.
      records:
      - runtime.md#rt-rte-save-apply
      - epistemic.md#epi-rte-canonical-integration
      - memory.md#mem-rte-log-fold
      - runtime.md#rt-rte-mode-extension
      - memory.md#mem-obj-mode
      - memory.md#mem-obj-vault-views
      - runtime.md#rt-rte-prefix-generation
      - memory.md#mem-rte-chunk-maintenance
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - runtime.md#rt-obj-transaction-bundle
      - memory.md#mem-obj-queue
      - memory.md#mem-rte-queue-resumption
      - runtime.md#rt-rte-direct-capture
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-claim-ledger
      note: Explicit reviewed content paths and automatic code admission coexist. Approval hashes do not
        authenticate human review. Direct-capture callers, initial adopted state, queue submissions and
        optional checkpoint control remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Synthetic prefix copying/truncation and retained page chunk reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - epistemic.md#epi-rte-synthetic-prefix
          - memory.md#mem-obj-chunks
          - memory.md#mem-rte-chunk-maintenance
          note: Synthetic generation selects and truncates retained page text into a reduced framing representation.
        records:
        - epistemic.md#epi-rte-synthetic-prefix
        - memory.md#mem-obj-chunks
        - memory.md#mem-rte-chunk-maintenance
        note: Selected opening text is reduced into prefix context; paragraph chunking alone is not a
          new claim.
      - scope: Selected operation-log entries to extractive fold representation
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-obj-log
          - memory.md#mem-rte-log-fold
          note: The instruction requests outcomes/themes with entry citations, preserving children and
            not upgrading evidence; faithful execution is unobserved.
        records:
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        note: Both reports agree on requested extractive content; the claimed versus afforded implementation-status
          conflict prevents an unqualified implementation status. Later discovery is not executable extraction.
      - scope: Reviewed existing wiki/claim/hot/view content replacement and Research canonical revision
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-vault-views
          - runtime.md#rt-rte-save-apply
          - epistemic.md#epi-rte-canonical-integration
          note: Reviewed replacement revises existing retained content rather than requiring another independent
            store.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-vault-views
        - runtime.md#rt-rte-save-apply
        - epistemic.md#epi-rte-canonical-integration
        note: The requested revision path is supported as procedure; no actual revision instance was supplied.
      - scope: Existing derived chunk/vector records and sparse-index availability
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-chunk-maintenance
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          - memory.md#mem-obj-chunks
          - memory.md#mem-obj-embed-cache
          - memory.md#mem-obj-tiling-cache
          note: Changed chunk/page or body/model keys regenerate/update derived records.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-chunk-maintenance
          - memory.md#mem-rte-tiling-diagnosis
          note: Surplus chunks and non-live tiling embeddings are deleted; this is forgetting, not historical
            invalidation.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-chunk-maintenance
          note: BM25 index removal withdraws reliance before rebuilding changed chunks; source pages remain
            retained.
        records:
        - memory.md#mem-rte-chunk-maintenance
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        note: Code recomputes changed derivatives, prunes stale/orphan entries and withdraws index availability
          before mutations.
      - scope: Source supersession/rejection, claim deprecation and optional model-prefix semantic transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-bap-vault-evidence
        - runtime.md#rt-rte-prefix-generation
        note: Metadata permits changed reliance but complete downstream withdrawal is unresolved; no input/output
          instance proves consolidation versus synthesis for model-generated prefixes.
      records:
      - epistemic.md#epi-rte-synthetic-prefix
      - memory.md#mem-obj-chunks
      - memory.md#mem-rte-chunk-maintenance
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-obj-vault-views
      - runtime.md#rt-rte-save-apply
      - epistemic.md#epi-rte-canonical-integration
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-bap-vault-evidence
      - runtime.md#rt-rte-prefix-generation
      note: Recorded code establishes derived-store revision/removal and index withdrawal; instructions
        request extractive folds and canonical revision. Model-prefix meaning and complete source-status
        withdrawal remain unresolved. No new claim is inferred merely from a synthesis label.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested Query/Save/Ingest/Research pages, ledgers, manifest and mode selection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-vault-query
          - memory.md#mem-obj-mode
          - memory.md#mem-bap-filing-config
          note: Requested retrieval returns current candidate pages and mode helper reads persisted settings.
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-source-ledger
          - memory.md#mem-obj-claim-ledger
          - memory.md#mem-obj-manifest
          - runtime.md#rt-rte-ingest-drafts
          - epistemic.md#epi-rte-canonical-integration
          note: Skills request orientation, current pages, evidence and provenance for the named operation.
        records:
        - runtime.md#rt-rte-vault-query
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-claim-ledger
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-mode
        - runtime.md#rt-rte-ingest-drafts
        - epistemic.md#epi-rte-canonical-integration
        - memory.md#mem-bap-filing-config
        note: A request for retained material remains pull even when software ranks or delivers the response.
      - scope: Requested rerank/tiling, queue list/claim/resume/recover and transaction/checkpoint recovery/replay
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-optional-rerank
          - memory.md#mem-rte-tiling-diagnosis
          - memory.md#mem-rte-queue-resumption
          - runtime.md#rt-rte-save-apply
          - runtime.md#rt-obj-transaction-bundle
          note: Code loads durable vectors, scheduling state, journals/results or checkpoint metadata
            on request.
        records:
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-rte-save-apply
        - runtime.md#rt-obj-transaction-bundle
        note: These later command invocations request and consume retained caches/control state.
      - scope: Index-discoverable folds and inspectable/renderable views
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-log
          - memory.md#mem-rte-log-fold
          - memory.md#mem-obj-vault-views
          note: Later readers can request catalogued folds/views.
        records:
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-vault-views
        note: This is an afforded reader route, not an automatic model loader.
      - scope: Opted-in later SessionStart hot emission and Stop retained-journal warnings
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-session-context
          - memory.md#mem-obj-hot
          - runtime.md#rt-obj-transaction-bundle
          note: Consent and bounds select hot or recovery state for emitted context/status.
        records:
        - runtime.md#rt-rte-session-context
        - memory.md#mem-obj-hot
        - runtime.md#rt-obj-transaction-bundle
        note: Lifecycle triggers supply retained orientation/status without a current request for that
          material; external host delivery is unobserved.
      - scope: Raw opaque payload extraction and queued external executor delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-ledger
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-rte-direct-capture
        note: Raw ingest is documented but not all payload extraction paths or queue executors/consumption
          are established; state completion is not delivery evidence.
      records:
      - runtime.md#rt-rte-vault-query
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-source-ledger
      - memory.md#mem-obj-claim-ledger
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-mode
      - runtime.md#rt-rte-ingest-drafts
      - epistemic.md#epi-rte-canonical-integration
      - memory.md#mem-bap-filing-config
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-rte-queue-resumption
      - runtime.md#rt-rte-save-apply
      - runtime.md#rt-obj-transaction-bundle
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-vault-views
      - runtime.md#rt-rte-session-context
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-queue
      - runtime.md#rt-rte-direct-capture
      note: Requested vault/code consumption and lifecycle hot supply are distinct operations. Fold/view
        discovery is afforded. Queue external delivery, opaque raw extraction and external host state
        do not become known from these witnesses.
    read_back_signal:
      assessment: partial
      units:
      - scope: SessionStart startup/resume/clear/compact hot context and Stop journal/status warnings
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-session-context
          - memory.md#mem-obj-hot
          - runtime.md#rt-obj-transaction-bundle
          note: Fixed hot-file availability and consent/budget filtering are coarse selection. Vault identity
            consent is not a content identity match selecting targeted delivered memory.
        records:
        - runtime.md#rt-rte-session-context
        - memory.md#mem-obj-hot
        - runtime.md#rt-obj-transaction-bundle
        note: Trigger is lifecycle event; inputs are opt-in/vault eligibility, hot availability/byte cap
          or bounded journal/status scan; selected parts are hot bytes or recovery warnings.
      - scope: Requested retrieval, configuration, caches, queue and recovery/fold/view reads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-vault-query
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-vault-views
        - memory.md#mem-bap-filing-config
        note: These assessed operations fulfill requests and therefore have no push-selection signal;
          lexical/cosine request ranking is not a push signal.
      - scope: Unresolved queued external payload delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        note: No executor/delivery chain establishes whether later payload supply is requested or pushed,
          much less its selector.
      records:
      - runtime.md#rt-rte-session-context
      - memory.md#mem-obj-hot
      - runtime.md#rt-obj-transaction-bundle
      - runtime.md#rt-rte-vault-query
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-rte-queue-resumption
      - runtime.md#rt-rte-save-apply
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-vault-views
      - memory.md#mem-bap-filing-config
      - memory.md#mem-obj-queue
      note: Lifecycle push uses coarse availability/consent/budget selection, not targeted relevance.
        Pull routes have no push selector. Unresolved external execution/delivery cannot be removed by
        the known hook witness.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Conversation-derived Save notes/hot/log and operation-log folds
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-hot
        note: Trace inputs and potential later context/discovery are recorded, but explicit reviewed content
          retention does not establish automatic trace-fed admission; the hash does not resolve actual
          human control. No qualifying automatic route or bounded absence is established.
      - scope: Automatic page-derived prefixes/chunks and embedding caches
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - runtime.md#rt-rte-prefix-generation
        - memory.md#mem-rte-chunk-maintenance
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        - memory.md#mem-obj-wiki-pages
        note: Automatic writes and later consumers are known, but pages are the immediate input. Their
          recorded mixed/unknown initial lineage does not establish a trace-origin input for these writes
          or bounded absence of one.
      - scope: Queue transition/results, transaction history and optional checkpoint state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        note: Runtime bookkeeping is retained, but no automatic trace-to-durable behavior-shaping artifact
          and later contextual/update consumer is established. Arbitrary result provenance/control remains
          unresolved; this is not a system-wide no.
      - scope: Explicit configuration, raw acquisition, adopted notes and views
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-mode
        - runtime.md#rt-rte-mode-extension
        - memory.md#mem-obj-source-ledger
        - runtime.md#rt-rte-direct-capture
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-vault-views
        note: Configured or imported content alone establishes neither qualifying automatic trace learning
          nor bounded absence across unknown initial/caller content.
      records:
      - runtime.md#rt-rte-save-apply
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-chunks
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - runtime.md#rt-rte-prefix-generation
      - memory.md#mem-rte-chunk-maintenance
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-queue
      - memory.md#mem-rte-queue-resumption
      - runtime.md#rt-obj-transaction-bundle
      - memory.md#mem-obj-mode
      - runtime.md#rt-rte-mode-extension
      - memory.md#mem-obj-source-ledger
      - runtime.md#rt-rte-direct-capture
      - memory.md#mem-obj-vault-views
      note: No canonical bounded-absence record supports a negative, and the accepted records establish
        no qualifying automatic trace-fed durable behavior-shaping chain. Manual retention and automatic
        page-derived caches must not be combined into such a chain.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Save/fold proposed trace-derived retention
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        note: Selected conversational knowledge and authored operation accounts are named, but no qualifying
          automatic admission/later-consumer chain is established. Do not assert session-logs or event-streams
          merely from these labels.
      - scope: Page-derived caches and opaque initial/caller provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-chunks
        - memory.md#mem-obj-embed-cache
        - memory.md#mem-obj-tiling-cache
        - memory.md#mem-obj-queue
        - memory.md#mem-rte-queue-resumption
        - runtime.md#rt-rte-prefix-generation
        - runtime.md#rt-rte-optional-rerank
        - memory.md#mem-rte-tiling-diagnosis
        note: The original source of any qualifying trace-fed update remains unresolved; document inference
          over pages is not itself a tool-trace learning input.
      - scope: Recovery/checkpoint, acquisition and configuration paths
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-transaction-bundle
        - runtime.md#rt-rte-save-apply
        - memory.md#mem-obj-source-ledger
        - runtime.md#rt-rte-direct-capture
        - memory.md#mem-obj-mode
        - runtime.md#rt-rte-mode-extension
        note: Runtime events and captured/configured bytes have known roles, but no qualifying learning
          write is established and no bounded all-route absence warrants inapplicability.
      records:
      - runtime.md#rt-rte-save-apply
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-chunks
      - memory.md#mem-obj-embed-cache
      - memory.md#mem-obj-tiling-cache
      - memory.md#mem-obj-queue
      - memory.md#mem-rte-queue-resumption
      - runtime.md#rt-rte-prefix-generation
      - runtime.md#rt-rte-optional-rerank
      - memory.md#mem-rte-tiling-diagnosis
      - runtime.md#rt-obj-transaction-bundle
      - memory.md#mem-obj-source-ledger
      - runtime.md#rt-rte-direct-capture
      - memory.md#mem-obj-mode
      - runtime.md#rt-rte-mode-extension
      note: Trace-source values apply to qualifying automatic trace-fed writes, not every recorded conversation
        or runtime event. Qualification is unresolved, so no positive source value or inapplicability
        is asserted.
---

# claude-obsidian memory profile

## Comparison rationale

This classification uses the supplied accepted records and their annotations only. No source files were read, no new evidence or records were added, and no target program was executed. Evidence is implementation or declared procedure, not observed use or causal benefit. The package-owned memory inventory includes computational scheduling and recovery state as well as prose; it does not classify every host/provider storage surface.

### Parts and consumers

[MEM-OBJ-chunks](memory.md#mem-obj-chunks) separates natural-language ranking input from symbolic postings and metadata. [MEM-OBJ-embed-cache](memory.md#mem-obj-embed-cache) and [MEM-OBJ-tiling-cache](memory.md#mem-obj-tiling-cache) separate dense parametric representations from keys and thresholds. File encoding is their substrate, not their representational form. Initial embedding provenance remains unresolved even though inference-derived cache writes are wired. Raw files in [MEM-OBJ-source-ledger](memory.md#mem-obj-source-ledger) have a known substrate but can have unresolved operative form; locators do not classify their opaque payloads.

Knowledge at later models is distinct from ranking at retrieval code, routing at filing/queue consumers and validation/enforcement at admission or recovery. [EPI-RTE-ledger-check](epistemic.md#epi-rte-ledger-check) uses retained support metadata as criteria; [EPI-RTE-ledger-disposition](epistemic.md#epi-rte-ledger-disposition) gives violations an enforced veto. Neither establishes semantic truth. [RT-OBJ-transaction-bundle](runtime.md#rt-obj-transaction-bundle), with its memory annotation, supplies retained recovery state, not a second knowledge ledger. No learning authority is inferred merely from reuse of vectors or stored results.

### Agency, transformations and delivery

Manual findings describe explicit operator decisions prescribed by [RT-RTE-save-apply](runtime.md#rt-rte-save-apply), [EPI-RTE-canonical-integration](epistemic.md#epi-rte-canonical-integration) and the configuration/view/fold procedures. They do not turn the approval hash into an authenticated human judgment. [RT-RTE-direct-capture](runtime.md#rt-rte-direct-capture) leaves caller control unresolved; code-only derived-cache admission is independently automatic. Initial adoption and arbitrary queue submissions retain their separate uncertainty.

Synthetic prefix copying supports consolidation locally through [EPI-RTE-synthetic-prefix](epistemic.md#epi-rte-synthetic-prefix). Model prefixes do not inherit that classification, and model synthesis labels do not establish a novel claim. Deleting orphan vectors/surplus chunks is forgetting; withdrawing the BM25 index before mutation is invalidation of an access representation. [MEM-RTE-chunk-maintenance](memory.md#mem-rte-chunk-maintenance) and [MEM-RTE-tiling-diagnosis](memory.md#mem-rte-tiling-diagnosis) do not establish complete semantic withdrawal of source/claim prose.

[RT-RTE-vault-query](runtime.md#rt-rte-vault-query) is a requested read chain, including ranking and return. It is not converted into push merely because code selects pages. [RT-RTE-session-context](runtime.md#rt-rte-session-context) separately supplies fixed hot context on lifecycle triggers and emits retained recovery status on Stop. These are coarse selection operations with availability, consent and budget filters; neither query relevance nor a matching content identifier is established. Actual external host delivery and obedience remain unobserved.

### Supersessions and unresolved coverage

The supplied reconciliation supersedes the epistemic claim-ledger declaration with [MEM-OBJ-claim-ledger](memory.md#mem-obj-claim-ledger); all profile claim-ledger findings use that canonical object. It also supersedes the epistemic extractive-fold declaration with [MEM-RTE-log-fold](memory.md#mem-rte-log-fold). The fold retains the disagreement between claimed and afforded implementation status: the profile uses claimed for the shared requested extractive transformation and afforded only for its recorded discovery/read path. The curation unit remains partial rather than assigning one unqualified implementation conclusion. No source reread or adjudication reopens report verification.

The source-ledger and derived-context containers are not whole-record supersessions of their memory parts. Separate rerank/tiling use identities remain separate without asserting two deployed models. The profile therefore keeps local consumer warrants rather than upgrading all branches from one executable witness.

No accepted bounded-absence record establishes trace-learning no. Save and folds have recorded trace-derived content, but their reviewed retention does not establish an automatic trace-fed write. Automatic prefix/vector caches consume pages whose initial and mixed lineage remains unresolved. Queue/journal retention alone is not a qualifying behavior-shaping update. These limits in [RT-RTE-save-apply](runtime.md#rt-rte-save-apply), [MEM-RTE-log-fold](memory.md#mem-rte-log-fold), [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages) and [MEM-RTE-queue-resumption](memory.md#mem-rte-queue-resumption) prevent both a qualifying positive and a bounded negative. Trace source consequently remains not-determinable, not inapplicable. External host compacted summaries are deliberately outside this package-owned memory scope, not opaque alternatives silently dropped to make these axes known.
