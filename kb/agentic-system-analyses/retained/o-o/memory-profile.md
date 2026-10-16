---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'o-o memory profile: document-local research, operator-maintained guidance, library projections
  and browser preference at the frozen commit.'
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
source-identity: https://github.com/jahala/o-o
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
memory-comparison:
  version: 2
  scope: Retained local article prose/structure, embedded image payloads and captions, operative manifest,
    source/fact cache, changelog, operator-edited instantiated contract and shared-code replacements,
    rebuilt library projection, and browser oo-theme preference, with their admission and later-consumer
    routes. Excludes unchanged shipped instructions/machinery as accumulated memory, transient image downloads,
    external research pages, provider weights and external Claude session stores. Host handling of requested
    reads and possible compaction/checkpoints remains an explicit unresolved delivery/trace-route limitation,
    not a claim about all runtime storage.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Article, manifest, instantiated contract, source/fact cache, changelog, embedded images,
          rebuilt index, and operator-replaced shell/JS/CSS
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-article
          - memory.md#mem-obj-source-cache
          - memory.md#mem-obj-facts
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-contract
          - memory.md#mem-obj-changelog
          - memory.md#mem-obj-index-content
          - memory.md#mem-obj-images
          - runtime.md#rt-obj-shared-shell
          - runtime.md#rt-rte-code-sync
          note: Local HTML/bash files retain these parts across later invocations.
        records: *id001
        note: All included document parts persist in local polyglot files; encoded image data and JSON
          are not separate substrates.
      - scope: Browser oo-theme preference
        assessment: known
        findings:
        - value: kv
          basis: wired
          records:
          - memory.md#mem-obj-oo-theme
          note: Browser localStorage retains the light/dark value under oo-theme.
        records:
        - memory.md#mem-obj-oo-theme
        note: The key/value mechanism is inspected; browser-origin deployment and actual persistence are
          not observed.
      records:
      - memory.md#mem-obj-article
      - memory.md#mem-obj-source-cache
      - memory.md#mem-obj-facts
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-contract
      - memory.md#mem-obj-changelog
      - memory.md#mem-obj-index-content
      - memory.md#mem-obj-images
      - runtime.md#rt-obj-shared-shell
      - runtime.md#rt-rte-code-sync
      - memory.md#mem-obj-oo-theme
      note: The inventory covers retained document parts, operator-replaced machinery, the library projection
        and UI preference. External Claude sessions, provider weights and host checkpoints are outside
        this shipped-memory boundary; they are not inferred from file reuse.
    representational_form:
      assessment: partial
      units:
      - scope: Article prose, source titles/descriptions, facts, contract guidance, change summaries,
          index titles/excerpts and image captions
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-article
          - memory.md#mem-obj-source-cache
          - memory.md#mem-obj-facts
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-contract
          - memory.md#mem-obj-changelog
          - memory.md#mem-obj-index-content
          - memory.md#mem-obj-images
          note: Humans or the model interpret prose, instructions, factual summaries and captions.
        records:
        - memory.md#mem-obj-article
        - memory.md#mem-obj-source-cache
        - memory.md#mem-obj-facts
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-contract
        - memory.md#mem-obj-changelog
        - memory.md#mem-obj-index-content
        - memory.md#mem-obj-images
        note: These are interpreted text paths, distinct from their fixed-rule containers.
      - scope: HTML/reference structure, JSON locators and dates, shell-consumed control fields, index
          navigation, theme string and operator-replaced code
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-article
          - memory.md#mem-obj-source-cache
          - memory.md#mem-obj-facts
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-contract
          - memory.md#mem-obj-changelog
          - memory.md#mem-obj-index-content
          - memory.md#mem-obj-images
          - runtime.md#rt-obj-shared-shell
          - runtime.md#rt-rte-code-sync
          - memory.md#mem-obj-oo-theme
          note: Shell/browser rules consume field values, markup, navigation, code and the theme string.
        records:
        - memory.md#mem-obj-article
        - memory.md#mem-obj-source-cache
        - memory.md#mem-obj-facts
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-contract
        - memory.md#mem-obj-changelog
        - memory.md#mem-obj-index-content
        - memory.md#mem-obj-images
        - runtime.md#rt-obj-shared-shell
        - runtime.md#rt-rte-code-sync
        - memory.md#mem-obj-oo-theme
        note: Fixed consumer rules establish the symbolic parts; this does not classify image meaning
          or external model weights.
      - scope: Decoded content of embedded image payloads at browser consumption
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-images
        note: Payloads were located but not decoded or visually reviewed. Base64 is encoding, not evidence
          that the consumed image content has a controlled representational form.
      records:
      - memory.md#mem-obj-article
      - memory.md#mem-obj-source-cache
      - memory.md#mem-obj-facts
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-contract
      - memory.md#mem-obj-changelog
      - memory.md#mem-obj-index-content
      - memory.md#mem-obj-images
      - runtime.md#rt-obj-shared-shell
      - runtime.md#rt-rte-code-sync
      - memory.md#mem-obj-oo-theme
      note: Readable text and fixed-rule structure are classified separately. Embedded image bytes are
        retained but not decoded or visually inspected; readable captions cannot classify that payload.
    lineage:
      assessment: partial
      units:
      - scope: User-supplied topic/scope/configuration, theme choice and explicitly operator-authored
          machinery replacements
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-batch-create
          - runtime.md#rt-rte-contract-edit
          - runtime.md#rt-rte-code-sync
          - memory.md#mem-obj-oo-theme
          note: A person supplies parameters, changes guidance/code or chooses the preference.
        records:
        - runtime.md#rt-rte-batch-create
        - runtime.md#rt-rte-contract-edit
        - runtime.md#rt-rte-code-sync
        - memory.md#mem-obj-oo-theme
        note: These routes name human content selection; classification concerns the route, not proof
          of sample history.
      - scope: Template initialization and deterministic library projection
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-batch-create
          - memory.md#mem-obj-index-content
          note: Template expansion and index extraction are non-trace compilation paths.
        records:
        - runtime.md#rt-rte-batch-create
        - memory.md#mem-obj-index-content
        note: Code emits initialized objects and derives navigation/excerpts from retained documents.
      - scope: Requested web-acquired source material and embedded images
        assessment: partial
        findings:
        - value: imported
          basis: claimed
          records:
          - epistemic.md#epi-rte-web-research
          - memory.md#mem-obj-images
          note: The contract requests web acquisition and image downloading for retention.
        records:
        - epistemic.md#epi-rte-web-research
        - memory.md#mem-obj-images
        - memory.md#mem-obj-source-cache
        note: Import is requested; original pages and image provenance are unavailable, and actual sample
          production is unverified.
      - scope: Requested agent-authored article and research summaries
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - epistemic.md#epi-rte-web-research
          - memory.md#mem-obj-changelog
          note: The external agent is instructed to write article prose and change summaries.
        records:
        - epistemic.md#epi-rte-web-research
        - memory.md#mem-obj-facts
        - memory.md#mem-obj-changelog
        note: Writing is requested, but no input/output trace resolves each assertion’s initial source
          or derivation; authored output does not imply novel claims.
      - scope: Actual initial provenance of populated caches, article assertions, summaries and image
          payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-cache
        - memory.md#mem-obj-facts
        - memory.md#mem-obj-article
        - memory.md#mem-obj-changelog
        - memory.md#mem-obj-images
        note: Persisted examples are not authenticated production traces; their actual authored/imported/derived
          composition cannot be fully reconstructed.
      records:
      - runtime.md#rt-rte-batch-create
      - runtime.md#rt-rte-contract-edit
      - runtime.md#rt-rte-code-sync
      - memory.md#mem-obj-oo-theme
      - memory.md#mem-obj-index-content
      - epistemic.md#epi-rte-web-research
      - memory.md#mem-obj-images
      - memory.md#mem-obj-source-cache
      - memory.md#mem-obj-facts
      - memory.md#mem-obj-changelog
      - memory.md#mem-obj-article
      note: Known construction and derivation routes coexist with unverified sample authorship and imported-image
        provenance. A contract requesting research does not establish how populated examples were produced.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Prior article, sources/facts and change summaries at the later research agent
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-bap-cache-reuse
          - runtime.md#rt-rte-document-update
          - memory.md#mem-obj-article
          - memory.md#mem-obj-changelog
          note: Prior research and reachable summaries supply background/context to the instructed later
            reader.
        records:
        - runtime.md#rt-rte-document-update
        - memory.md#mem-bap-cache-reuse
        - memory.md#mem-obj-article
        - memory.md#mem-obj-changelog
        note: The later whole-file/cache read is requested, not observed delivery or dependence.
      - scope: Operator-edited instantiated contract at the research agent
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-contract
          - runtime.md#rt-rte-contract-edit
          note: Changed preferences, procedure and research constraints guide future research by requested
            file read.
        records:
        - memory.md#mem-obj-contract
        - runtime.md#rt-rte-contract-edit
        note: Scope includes retained operator changes, not static shipped instructions standing alone.
      - scope: Manifest dates and interval at direct/batch freshness gates
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-manifest
          - runtime.md#rt-rte-document-update
          - runtime.md#rt-rte-batch-create
          note: Persisted freshness values select whether the research operation is invoked.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-manifest
          - runtime.md#rt-rte-document-update
          - runtime.md#rt-rte-batch-create
          note: The local gate refuses ordinary fresh-document dispatch; this is not a universal veto
            against force or direct edits.
        records:
        - memory.md#mem-obj-manifest
        - runtime.md#rt-rte-document-update
        - runtime.md#rt-rte-batch-create
        note: The same metadata both selects dispatch and supports the local skip decision; force is an
          explicit alternate path.
      - scope: Manifest as_of at the later research agent
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-manifest
          - epistemic.md#epi-rte-cache-reuse
          note: The retained date is requested to select the temporal scope of later research.
        records:
        - memory.md#mem-obj-manifest
        - epistemic.md#epi-rte-cache-reuse
        note: Date-focus instruction is weaker than the executable freshness gate.
      - scope: Article/reference text, manifest display and library excerpts at browser/human readers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-article
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-index-content
          - runtime.md#rt-rte-library-read
          note: Readers receive retained article claims, metadata and lossy excerpts as reference/context.
        records:
        - memory.md#mem-obj-article
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-index-content
        - runtime.md#rt-rte-library-read
        note: Rendering delivers reference content; no factual acceptance is inferred.
      - scope: Retained document dates and displayed text at index/browser ordering and filtering consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-index-content
          - runtime.md#rt-rte-library-read
          - epistemic.md#epi-rte-index-excerpt
          note: Dates determine top-eight prominence; search/sort rules use retained display material
            to change relative visibility.
        records:
        - memory.md#mem-obj-index-content
        - runtime.md#rt-rte-library-read
        - epistemic.md#epi-rte-index-excerpt
        note: Ranking concerns visibility, not research quality or a learned policy.
      - scope: Theme value at later browser initialization
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-oo-theme
          note: JS uses the saved preference to select light/dark presentation.
        records:
        - memory.md#mem-obj-oo-theme
        note: The saved string selects presentation state only.
      - scope: Operator-replaced shell at future Bash invocation
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-shared-shell
          - runtime.md#rt-rte-code-sync
          note: The retained executable block determines permitted dispatch and local effects under shell
            rules.
        records:
        - runtime.md#rt-obj-shared-shell
        - runtime.md#rt-rte-code-sync
        note: Replacement code is an executable control, not advisory prose; individual new payload behavior
          is not inspected.
      - scope: Changed contract budget at external CLI enforcement, replacement JS/CSS payload effects,
          and decoded image semantics
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-contract
        - runtime.md#rt-cmp-claude
        - runtime.md#rt-rte-code-sync
        - memory.md#mem-obj-images
        note: Budget is passed but external enforcement is uninspected. Arbitrary replacement presentation
          payloads and decoded images lack enough recorded consumer-effect detail for further controlled
          authority findings.
      records:
      - runtime.md#rt-rte-document-update
      - memory.md#mem-bap-cache-reuse
      - memory.md#mem-obj-article
      - memory.md#mem-obj-changelog
      - memory.md#mem-obj-contract
      - runtime.md#rt-rte-contract-edit
      - memory.md#mem-obj-manifest
      - runtime.md#rt-rte-batch-create
      - epistemic.md#epi-rte-cache-reuse
      - memory.md#mem-obj-index-content
      - runtime.md#rt-rte-library-read
      - epistemic.md#epi-rte-index-excerpt
      - memory.md#mem-obj-oo-theme
      - runtime.md#rt-obj-shared-shell
      - runtime.md#rt-rte-code-sync
      - runtime.md#rt-cmp-claude
      - memory.md#mem-obj-images
      note: Authority is assigned at consumers, not from storage labels. Wired shell/browser effects and
        requested model effects retain separate bases. No inspected consumer establishes image truth,
        trace-fed learning authority or external budget enforcement.
    write_agency:
      assessment: known
      units:
      - scope: Human creation parameters, explicit configuration supply/removal, shared-code propagation
          and theme choice
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-batch-create
          - runtime.md#rt-rte-contract-edit
          - runtime.md#rt-rte-code-sync
          - memory.md#mem-obj-oo-theme
          note: Topic/settings, contract changes, selected code replacements and theme values reflect
            explicit operator content decisions.
        records:
        - runtime.md#rt-rte-batch-create
        - runtime.md#rt-rte-contract-edit
        - runtime.md#rt-rte-code-sync
        - memory.md#mem-obj-oo-theme
        note: A person explicitly supplies/selects the retained content or replacement; software applying
          it does not make admission automatic.
      - scope: Template defaults/empty-state emission, index rebuild and agent-selected research edits
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-batch-create
          - runtime.md#rt-rte-library-read
          - runtime.md#rt-rte-document-update
          - epistemic.md#epi-rte-document-retention
          note: Code generates defaults/projections and dispatch admits model-selected file edits without
            per-edit approval.
        records:
        - runtime.md#rt-rte-batch-create
        - runtime.md#rt-rte-library-read
        - runtime.md#rt-rte-document-update
        - epistemic.md#epi-rte-document-retention
        note: Starting these workflows is not per-content approval; agent-selected content is admitted
          directly without a separate human veto.
      records:
      - runtime.md#rt-rte-batch-create
      - runtime.md#rt-rte-contract-edit
      - runtime.md#rt-rte-code-sync
      - memory.md#mem-obj-oo-theme
      - runtime.md#rt-rte-library-read
      - runtime.md#rt-rte-document-update
      - epistemic.md#epi-rte-document-retention
      note: Admission mechanisms, rather than physical writes or authorship, are classified. Actual sample
        production remains unknown under lineage, but shipped creation, edits, projection, research admission
        and preference writes have named control owners.
    curation_operations:
      assessment: partial
      units:
      - scope: Index excerpt/card projection from retained documents
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-index-content
          - epistemic.md#epi-rte-index-excerpt
          note: The code selects and compresses existing article text into retained library excerpts.
        records:
        - memory.md#mem-obj-index-content
        - epistemic.md#epi-rte-index-excerpt
        note: Selection and 120-character compression reduce retained material. Citation removal and possible
          qualification loss are faithfulness limits, not evidence of synthesis.
      - scope: Operator contract edits and shared-code replacements
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-contract-edit
          - runtime.md#rt-rte-code-sync
          note: Explicit configuration edits and block replacements revise existing retained guidance/machinery.
        records:
        - runtime.md#rt-rte-contract-edit
        - runtime.md#rt-rte-code-sync
        note: These overwrite/revise retained entries. Deletion without history does not establish invalidate
          as defined here.
      - scope: Agent-requested article/cache/manifest maintenance
        assessment: partial
        findings:
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-document-update
          - epistemic.md#epi-rte-web-research
          - epistemic.md#epi-rte-source-selection
          note: The maintenance procedure requests updating existing research and retaining still-valid
            sources.
        records:
        - runtime.md#rt-rte-document-update
        - epistemic.md#epi-rte-web-research
        - epistemic.md#epi-rte-source-selection
        note: Incremental revision is requested, but semantic relations and exact fact/source maintenance
          operations remain unspecified or unobserved.
      - scope: Image resize/rejection and external context transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-images
        - runtime.md#rt-cmp-claude
        - runtime.md#rt-rte-document-update
        note: Requested image resizing/acquisition alone establishes no controlled curation operation
          over retained claims. Host compaction, trimming and checkpoint transformations are uninspected
          and outside local implementation.
      records:
      - memory.md#mem-obj-index-content
      - epistemic.md#epi-rte-index-excerpt
      - runtime.md#rt-rte-contract-edit
      - runtime.md#rt-rte-code-sync
      - runtime.md#rt-rte-document-update
      - epistemic.md#epi-rte-web-research
      - epistemic.md#epi-rte-source-selection
      - memory.md#mem-obj-images
      - runtime.md#rt-cmp-claude
      note: Implemented projection and explicit content revision are supported. Requested research editing
        does not establish new claims absent from its inputs, duplicate merging, tombstone invalidation
        or trace extraction. Opaque external transformations and unverified research outcomes prevent
        a complete operation inventory.
    read_back_direction:
      assessment: known
      units:
      - scope: Requested document/cache read by later research agent
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-rte-document-update
          - memory.md#mem-bap-cache-reuse
          note: A later invocation requests the document and prior research through file reads.
        records:
        - runtime.md#rt-rte-document-update
        - memory.md#mem-bap-cache-reuse
        note: The path and contract request retained material; neither the filename nor returned read
          is another unsolicited push.
      - scope: Operator-requested library rebuild/browser article or index viewing/configuration display
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-library-read
          - runtime.md#rt-rte-contract-edit
          note: Consumers request retained files, projections or displayed contract fields.
        records:
        - runtime.md#rt-rte-library-read
        - runtime.md#rt-rte-contract-edit
        note: Requested delivery is pull even though code renders it.
      - scope: Automatic selection within index rebuilding, shell freshness extraction and browser theme
          replay
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-index-content
          - memory.md#mem-obj-manifest
          - memory.md#mem-obj-oo-theme
          - runtime.md#rt-rte-library-read
          - runtime.md#rt-rte-document-update
          note: Code automatically supplies date-selected cards, freshness metadata and saved theme state
            to their later consumers.
        records:
        - memory.md#mem-obj-index-content
        - memory.md#mem-obj-manifest
        - memory.md#mem-obj-oo-theme
        - runtime.md#rt-rte-library-read
        - runtime.md#rt-rte-document-update
        note: Separate selector operations choose retained input within the requested workflow, without
          a request for those particular retained parts.
      records:
      - runtime.md#rt-rte-document-update
      - memory.md#mem-bap-cache-reuse
      - runtime.md#rt-rte-library-read
      - runtime.md#rt-rte-contract-edit
      - memory.md#mem-obj-index-content
      - memory.md#mem-obj-manifest
      - memory.md#mem-obj-oo-theme
      note: Inventory covers document/cache requests, library/browser reads, automatic projection selection
        and UI preference replay. The external host’s treatment after a requested read remains uninspected,
        not a new established local read-back route.
    read_back_signal:
      assessment: known
      units:
      - scope: 'Index rebuild trigger: discovered files and dates select retained entries/excerpts; later
          dispatch trigger: first freshness metadata supplies gate input'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-index-content
          - memory.md#mem-obj-manifest
          - runtime.md#rt-rte-library-read
          - runtime.md#rt-rte-document-update
          note: Discovery/availability and dates select index parts; freshness-field availability supplies
            automatic gate metadata.
        records:
        - memory.md#mem-obj-index-content
        - memory.md#mem-obj-manifest
        - runtime.md#rt-rte-library-read
        - runtime.md#rt-rte-document-update
        note: Availability, date ordering, first-match extraction and eight-card limit are broad structural
          selection, not inferred semantic retrieval.
      - scope: 'Browser initialization trigger: localStorage lookup selects saved oo-theme preference'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-oo-theme
          note: getItem(oo-theme) selects the saved light/dark value for automatic presentation replay.
        records:
        - memory.md#mem-obj-oo-theme
        note: The key is the actual selector of the delivered retained setting, not merely a label on
          a requested document.
      records:
      - memory.md#mem-obj-index-content
      - memory.md#mem-obj-manifest
      - runtime.md#rt-rte-library-read
      - runtime.md#rt-rte-document-update
      - memory.md#mem-obj-oo-theme
      note: Signals classify the automatic selectors only. Requested filenames and catalog identifiers
        alone do not establish targeted push; index card selection is coarse and theme replay performs
        an actual key lookup.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Research article/cache and product-change summaries with later whole-file consumption
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-facts
        - memory.md#mem-obj-changelog
        - runtime.md#rt-rte-document-update
        - epistemic.md#epi-rte-web-research
        note: Research outputs have unverified execution provenance. Change summaries do not supply a
          recorded trace-to-derived-artifact chain or evidence of their use as update experience; neither
          yes nor bounded no is warranted.
      - scope: Index, operator-maintained guidance/machinery and UI preference routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-index-content
        - runtime.md#rt-rte-contract-edit
        - runtime.md#rt-rte-code-sync
        - memory.md#mem-obj-oo-theme
        note: The records identify deterministic projection or explicit operator supply, not qualifying
          automatic trace-fed writes. They do not declare a searched bounded absence for all trace-learning
          alternatives.
      - scope: Host compaction/checkpoint alternatives affecting later file-read context
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-claude
        - runtime.md#rt-rte-document-update
        note: External host session retention, summaries and checkpoints are uninspected. No local profile
          value can be inferred from their opacity; this names a delivery limitation, not inclusion of
          all provider storage.
      records:
      - memory.md#mem-obj-facts
      - memory.md#mem-obj-changelog
      - runtime.md#rt-rte-document-update
      - epistemic.md#epi-rte-web-research
      - memory.md#mem-obj-index-content
      - runtime.md#rt-rte-contract-edit
      - runtime.md#rt-rte-code-sync
      - memory.md#mem-obj-oo-theme
      - runtime.md#rt-cmp-claude
      note: No accepted bounded-absence record establishes a local no, and no accepted trace-fed write
        establishes yes. Research persistence and attributed change summaries are insufficient; external
        compaction remains uninspected rather than negative.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Original inputs of any qualifying research-summary or host-mediated retained-context update
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-changelog
        - memory.md#mem-obj-facts
        - runtime.md#rt-rte-document-update
        - runtime.md#rt-cmp-claude
        note: Research citations and product summaries do not establish original trace content. External
          context processing is opaque, so it cannot supply a trace-source classification.
      records:
      - memory.md#mem-obj-changelog
      - memory.md#mem-obj-facts
      - runtime.md#rt-rte-document-update
      - runtime.md#rt-cmp-claude
      note: No qualifying trace-learning route is established, but its complete bounded absence is also
        not established. Therefore trace_source is not made inapplicable and no session/tool/event/trajectory
        value is invented.
---

# o-o memory profile

## Comparison rationale

This profile classifies the accepted record inventory, not an observed update.
Local persistence and shell/browser consumers have wired support. Agent research,
source-validity selection and later cache use remain requested behavior; wiring
the CLI request does not upgrade those paths. See
[RT-RTE-document-update](runtime.md#rt-rte-document-update),
[EPI-RTE-web-research](epistemic.md#epi-rte-web-research) and
[MEM-BAP-cache-reuse](memory.md#mem-bap-cache-reuse).

The reconciliation supersedes the epistemic article, manifest, changelog and
contract objects with their memory declarations. Those canonical destinations
are used here. The cache container remains distinct from its source and fact
parts; the image route spanning staging and embedding remains distinct from
persistent image payloads. See
[MEM-OBJ-article](memory.md#mem-obj-article),
[MEM-OBJ-manifest](memory.md#mem-obj-manifest),
[MEM-OBJ-changelog](memory.md#mem-obj-changelog),
[MEM-OBJ-contract](memory.md#mem-obj-contract),
[EPI-OBJ-source-cache](epistemic.md#epi-obj-source-cache) and
[MEM-OBJ-images](memory.md#mem-obj-images).
No supersession changes an evidence basis or establishes actual production
provenance.

The substrate union is files plus browser key/value storage, not repo merely
because the evidence was captured in Git. Image encoding does not establish its
consumed representational form. Readable captions are classified without
claiming inspection of the image payload. See
[MEM-OBJ-images](memory.md#mem-obj-images) and
[MEM-OBJ-oo-theme](memory.md#mem-obj-oo-theme).

Manual supply and automatic admission coexist within creation: the operator
chooses topic/settings while code emits default state. Research admission is
automatic even when the operator starts the workflow. Operator contract changes
and selected machinery replacements remain manual. See
[RT-RTE-batch-create](runtime.md#rt-rte-batch-create),
[RT-RTE-contract-edit](runtime.md#rt-rte-contract-edit) and
[RT-RTE-code-sync](runtime.md#rt-rte-code-sync).

Index excerpts consolidate retained material, even when truncation loses a
qualification. Such a faithfulness defect does not establish synthesis.
Research instructions to synthesize an article do not establish the controlled
synthesize operation, which requires a claim absent from the inputs. No linked
inputs/outputs settle that distinction here. See
[EPI-RTE-index-excerpt](epistemic.md#epi-rte-index-excerpt) and
[EPI-RTE-web-research](epistemic.md#epi-rte-web-research).

Pull delivery and push selection are separate operations: requested document or
index viewing is pull, while code selects prominent cards and automatically
replays saved presentation state. An eight-card/date filter is coarse; an actual
localStorage key lookup is identifier selection. A filename in the agent's read
request is not another push signal. See
[RT-RTE-library-read](runtime.md#rt-rte-library-read),
[MEM-OBJ-index-content](memory.md#mem-obj-index-content),
[MEM-OBJ-oo-theme](memory.md#mem-obj-oo-theme) and
[MEM-BAP-cache-reuse](memory.md#mem-bap-cache-reuse).

Trace learning is not inferred from research reuse or the label changelog.
The retained summaries lack authenticated execution provenance and an established
trace-fed update chain. No accepted bounded-absence record supports a controlled
no either. Host compaction could be material but is uninspected; a known local
file route cannot settle it. The resulting trace-source uncertainty is not
inapplicability. See [MEM-OBJ-changelog](memory.md#mem-obj-changelog),
[MEM-OBJ-facts](memory.md#mem-obj-facts) and
[RT-CMP-claude](runtime.md#rt-cmp-claude).

Source-read log: none. This classification used only the supplied members and
reconciliation; it introduced no source evidence or records.
