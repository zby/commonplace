---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of ai-memex-cli: local retained documents, guidance, access metadata and
  later-consumer projections'
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
source-identity: https://github.com/zelixag/ai-memex-cli
reviewed-boundary: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
memory-comparison:
  version: 2
  scope: Local accumulated raw/session documents, wiki text and metadata, live-schema additions, catalog/action
    history, semantic findings, recomputed access index, scene manifests, context registry, local copies
    and installed host projections, including their admission, maintenance and later-consumer routes.
    Excludes unchanged shipped workflow text, ordinary transient invocation/lint state without durable
    projection, external agent/provider histories, weights and checkpoints, and qmd internal indexes;
    qmd-backed requested retrieval remains a pull route, not a classification of its internal storage.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Raw and session documents, wiki bodies and headers, live schema, catalog/log, local copies,
          scene manifests, registry and host bootstrap files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-index-log
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-scene-manifest
          - memory.md#mem-obj-context-registry
          - memory.md#mem-obj-host-bootstrap
          note: Persistent Markdown/YAML and JSON artifacts are ordinary files; no repository commit policy
            is implied.
        records: *id001
        note: Each retained local artifact has a filesystem location in the accepted inventory.
      - scope: Recomputed wiki index used to access retained pages
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-page-metadata
          note: buildWikiIndex constructs process objects from retained metadata and links.
        records:
        - memory.md#mem-obj-page-metadata
        note: An access structure is rebuilt from page files rather than persisted as a separate index.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-wiki-schema
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-local-projection
      - memory.md#mem-obj-scene-manifest
      - memory.md#mem-obj-context-registry
      - memory.md#mem-obj-host-bootstrap
      note: The local retained-object and access-structure inventory is covered. Files, not Markdown encoding
        or the product Git description, establish the substrate; external provider and qmd internals are
        outside this memory boundary.
    representational_form:
      assessment: known
      units:
      - scope: Source/session prose, wiki prose and descriptions, catalog/history, live guidance, semantic
          findings and generated local/host text at interpreting consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-index-log
          - memory.md#mem-obj-lint-results
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-scene-manifest
          - memory.md#mem-obj-host-bootstrap
          note: Documents, guidance and readable projections retain textual content at these consumers.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-index-log
        - memory.md#mem-obj-lint-results
        - memory.md#mem-obj-local-projection
        - memory.md#mem-obj-scene-manifest
        - memory.md#mem-obj-host-bootstrap
        note: Natural-language payloads are delivered or made available for human/model interpretation;
          this does not establish host activation.
      - scope: Page IDs, tags, links and metadata at fixed selectors/checkers; schema/local include directives;
          session provenance fields; registry and scene fields; host markers/configuration
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-context-registry
          - memory.md#mem-obj-scene-manifest
          - memory.md#mem-obj-host-bootstrap
          note: Structured fields determine indexing, include resolution, dispatch or rendering independently
            of the prose interpretation path.
        records:
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-local-projection
        - memory.md#mem-obj-context-registry
        - memory.md#mem-obj-scene-manifest
        - memory.md#mem-obj-host-bootstrap
        note: These operative parts have localized fields interpreted by fixed parsing, selection or rendering
          rules.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-wiki-schema
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-lint-results
      - memory.md#mem-obj-local-projection
      - memory.md#mem-obj-scene-manifest
      - memory.md#mem-obj-host-bootstrap
      - memory.md#mem-obj-context-registry
      note: Coverage separates interpreting consumers from fixed-rule access consumers. No external model
        parameters or opaque provider checkpoint is included.
    lineage:
      assessment: partial
      units:
      - scope: Web/local raw material entering the vault
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-capture-source
          - epistemic.md#epi-rte-fetch-render
          note: Fetched/existing external documents enter retained raw files; authenticity and source
            truth remain unknown.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-capture-source
        - epistemic.md#epi-rte-fetch-render
        note: Source acquisition is an import path, not production of the imported claims.
      - scope: Mechanical session Markdown
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - epistemic.md#epi-rte-session-render
          note: Recorded turns are selected and rendered into durable session documents; this does not
            imply lesson extraction or complete fidelity.
        records:
        - memory.md#mem-obj-session-markdown
        - epistemic.md#epi-rte-session-render
        note: Structured parsing and fallback rendering have a recorded original-session input and derived
          file output.
      - scope: Delegated session summaries and live-schema learning additions
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-rte-session-distill
          note: An implemented child prompt requests decisions/practices and a schema note from recorded
            sessions; execution and faithfulness are unobserved.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-rte-session-distill
        note: The requested derivation path is known even though no resulting note is supplied.
      - scope: Wiki content and metadata admitted through ingestion, semantic repair or foreground answer
          saving
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-page-metadata
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-semantic-lint
          note: The delegated model creates or edits retained prose and headers.
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-rte-query-save
          note: The foreground workflow permits a model-authored durable answer, subject to conflicting
            save protocols.
        records:
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-page-metadata
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-semantic-lint
        - memory.md#mem-rte-query-save
        note: Agent authorship and source-based derivation are established as paths. Without actual inputs/outputs,
          trace-derived versus non-trace source provenance cannot be exhaustively classified for this
          open writer.
      - scope: Seeded schema/scaffolds, catalog/log and generated local/host projections, computed index
          and context registry
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-index-log
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-host-bootstrap
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-context-registry
          note: Code seeds templates, renders or copies retained content, parses an access index and serializes
            control/history entries.
        records:
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-index-log
        - memory.md#mem-obj-local-projection
        - memory.md#mem-obj-host-bootstrap
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-context-registry
        note: Known template/copy/render/parse paths classify these derived parts without asserting the
          provenance of every future content edit.
      - scope: Initial scene-manifest content and authoring path
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-scene-manifest
        note: Only reading and rendering existing named manifests is established; the missing creation
          path prevents assigning initial lineage.
      records:
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-capture-source
      - epistemic.md#epi-rte-fetch-render
      - memory.md#mem-obj-session-markdown
      - epistemic.md#epi-rte-session-render
      - memory.md#mem-obj-wiki-schema
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-page-metadata
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-semantic-lint
      - memory.md#mem-rte-query-save
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-local-projection
      - memory.md#mem-obj-host-bootstrap
      - memory.md#mem-obj-context-registry
      - memory.md#mem-obj-scene-manifest
      note: Known derivation and import paths do not establish every initial author or the semantic origin
        of hypothetical model output. Scene-manifest creation remains unresolved.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained raw/session/wiki material and catalog/findings supplied to interpreting maintenance
          or answering consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-index-log
          - memory.md#mem-obj-lint-results
          - runtime.md#rt-rte-context-delivery
          note: Search/page/injection and maintenance routes expose retained content for interpretation.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-index-log
        - memory.md#mem-obj-lint-results
        - runtime.md#rt-rte-context-delivery
        note: These parts supply context or evidence rather than a factual acceptance oracle.
      - scope: Live-schema experience notes at later maintenance agents
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-bap-schema-prompt
          note: The retained note supplies standing guidance through interpreted prompt instructions.
        records:
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-bap-schema-prompt
        note: The live schema is reloaded into later child prompts, including appended notes if written.
      - scope: Rendered scene triggers and host bootstrap at later project hosts
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-scene-manifest
          - memory.md#mem-obj-host-bootstrap
          - runtime.md#rt-bap-host-bootstrap
          note: Generated consultation instructions persist in host files for later sessions.
        records:
        - memory.md#mem-obj-scene-manifest
        - memory.md#mem-obj-host-bootstrap
        - runtime.md#rt-bap-host-bootstrap
        note: The host-loading contract supplies guidance; its activation is not observed.
      - scope: Page name/ID/tag/description fields at fixed keyword scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-page-metadata
          - runtime.md#rt-rte-context-delivery
          note: Retained metadata changes relative scores and which bodies fit the selection cap.
        records:
        - memory.md#mem-obj-page-metadata
        - runtime.md#rt-rte-context-delivery
        note: Ranking uses metadata rather than page bodies; no learned ranker is implied.
      - scope: Include directives and context registry at file selection and refresh dispatch
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-context-registry
          - runtime.md#rt-rte-context-delivery
          note: Includes choose payload files and installed context entries choose refresh destinations.
        records:
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-local-projection
        - memory.md#mem-obj-context-registry
        - runtime.md#rt-rte-context-delivery
        note: Access/control fields select files or destinations, not truth or user permission.
      - scope: Retained page-ID inventory at link membership evaluation
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-page-metadata
          - epistemic.md#epi-rte-mechanical-check
          - epistemic.md#epi-rte-link-check
          note: An extracted link conforms only if its target belongs to the parsed retained-ID inventory.
        records:
        - memory.md#mem-obj-page-metadata
        - epistemic.md#epi-rte-mechanical-check
        - epistemic.md#epi-rte-link-check
        note: The retained IDs provide a bounded conformance criterion; advisory diagnostics do not enforce
          rejection of page content.
      - scope: Recorded session experience at the delegated schema-note update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-rte-session-distill
          note: Session records feed a requested durable behavior-shaping schema append. No parameter
            training or improvement is established.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-rte-session-distill
        note: Learning authority at the update consumer is separate from instruction authority at the
          later maintenance consumer.
      - scope: Arbitrary resulting model-authored pages, saved answers and opaque semantic judgments
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-rte-query-save
        - runtime.md#rt-rte-semantic-lint
        note: The open model routes have no supplied output corpus or consumption trace; further standing
          directions, enforcement or other effects cannot be classified from page-type names.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-lint-results
      - runtime.md#rt-rte-context-delivery
      - memory.md#mem-obj-wiki-schema
      - runtime.md#rt-bap-schema-prompt
      - memory.md#mem-obj-scene-manifest
      - memory.md#mem-obj-host-bootstrap
      - runtime.md#rt-bap-host-bootstrap
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-local-projection
      - memory.md#mem-obj-context-registry
      - epistemic.md#epi-rte-mechanical-check
      - epistemic.md#epi-rte-link-check
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-rte-query-save
      - runtime.md#rt-rte-semantic-lint
      note: Recorded knowledge, instruction, ranking, routing, validation and learning paths remain distinct.
        Initial scene authorship is not needed to identify rendered guidance, but no actual host use or
        exhaustive model-internal effects are established.
    write_agency:
      assessment: partial
      units:
      - scope: Mechanical session conversion, delegated distillation/ingestion/semantic repair, scaffold/template
          seeding, migration, projections and context regeneration
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-semantic-lint
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-local-projection
          - memory.md#mem-obj-host-bootstrap
          - memory.md#mem-obj-context-registry
          note: Code or a model determines retained output; starting the command does not make subsequent
            admission manual.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-semantic-lint
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-local-projection
        - memory.md#mem-obj-host-bootstrap
        - memory.md#mem-obj-context-registry
        note: Known software/model decisions admit these outputs without a wired per-content human gate.
      - scope: Interactive direct keyword-fetch result selection
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-capture-source
          - memory.md#mem-obj-raw
          note: The operator chooses result indices, all or none before the selected captures are written.
        records:
        - runtime.md#rt-rte-capture-source
        - memory.md#mem-obj-raw
        note: This branch requires an explicit human choice of returned sources, not verification of their
          claims.
      - scope: Yes-all/direct rule-based and delegated capture admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-capture-source
          - memory.md#mem-obj-raw
          note: Code selects all results under --yes or fixed URL/crawl rules, and the delegated branch
            admits model-selected capture output.
        records:
        - runtime.md#rt-rte-capture-source
        - memory.md#mem-obj-raw
        note: Automatic result admission is a distinct alternative to the interactive decision.
      - scope: Foreground save/archive under installed query reference
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - memory.md#mem-rte-query-save
          note: The installed reference requires a user save/archive request for the answer.
        records:
        - memory.md#mem-rte-query-save
        note: An explicit user save decision is an afforded admission alternative, not a universal gate.
      - scope: Foreground durability-based saving under vault-schema doctrine
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-rte-query-save
          note: The foreground agent may decide an answer is durable and file it under the schema protocol.
        records:
        - memory.md#mem-rte-query-save
        note: The conflicting schema alternative delegates the admission decision to model judgment.
      - scope: Initial manifest creation, arbitrary source/manual edits and caller-supplied log entries
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-scene-manifest
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-index-log
        note: The records do not identify a human content decision for every generic caller or an initial
          manifest writer. Authorship or software I/O alone cannot settle admission control.
      records:
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-schema
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-semantic-lint
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-local-projection
      - memory.md#mem-obj-host-bootstrap
      - memory.md#mem-obj-context-registry
      - runtime.md#rt-rte-capture-source
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-query-save
      - memory.md#mem-obj-scene-manifest
      - memory.md#mem-obj-index-log
      note: Software/model admission is recorded for deterministic and delegated paths. Generic CLI invocation
        is not human content approval. Explicit source selection and optional save decisions remain local,
        while manifest initialization and some caller-supplied content control are unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Delegated session extraction and schema-note generation
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-rte-session-distill
          note: Requested extraction compresses existing session content into a summary and brief learning
            note.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-rte-session-distill
        note: The implemented prompt requests selecting decisions/practices into reduced retained representations;
          model compliance is not observed.
      - scope: Existing-page ingestion and semantic repair
        assessment: partial
        findings:
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-body
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-semantic-lint
          note: The maintenance prompt requests updating existing wiki pages and directly repairing safe
            defects.
        - value: dedup
          basis: claimed
          records:
          - runtime.md#rt-rte-semantic-lint
          - memory.md#mem-obj-wiki-body
          note: Semantic repair requests treatment of unambiguous duplicates, including page-merge stubs;
            actual merging is not supplied.
        records:
        - memory.md#mem-obj-wiki-body
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-semantic-lint
        note: Revision and duplicate treatment are requested. No concrete result establishes every implemented
          semantic transformation or resolves new-claim synthesis.
      - scope: Host digest rendering from retained metadata
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-host-bootstrap
          - memory.md#mem-obj-page-metadata
          note: First-five-per-scene selection, whitespace collapse and description truncation reduce
            the retained catalog representation without establishing new claims.
        records:
        - memory.md#mem-obj-host-bootstrap
        - memory.md#mem-obj-page-metadata
        note: The fixed renderer selects a bounded subset and compresses existing descriptions.
      - scope: Unseen semantic outputs of ingestion, semantic diagnosis and foreground synthesis/save
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-semantic-lint
        - memory.md#mem-rte-query-save
        - epistemic.md#epi-clm-synthetic-pages
        note: The type label synthesis is not evidence of a new claim. Input/output propositions are missing,
          preventing a positive synthesize finding or complete transformation classification.
      records:
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-schema
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-obj-wiki-body
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-semantic-lint
      - memory.md#mem-obj-host-bootstrap
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-rte-query-save
      - epistemic.md#epi-clm-synthetic-pages
      note: Requested model transformations have weaker warrants than implemented fixed transformations.
        Model output is unavailable, so synthesis, semantic preservation and complete operation coverage
        cannot be settled.
    read_back_direction:
      assessment: known
      units:
      - scope: Search, foreground page reads, explicit injection and project-local retrieval/projection
          requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-context-delivery
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-wiki-body
          - memory.md#mem-obj-local-projection
          note: Search/inject/glob and explicit page access return selected retained material.
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-query-save
          note: Foreground query guidance directs the answering agent to look up and read retained pages.
        records:
        - runtime.md#rt-rte-context-delivery
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-body
        - memory.md#mem-obj-local-projection
        - memory.md#mem-rte-query-save
        note: These operations fulfill a consumer request for retained material; their return is not another
          independent push.
      - scope: Automatic schema/catalog selection into maintenance-child prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-session-distill
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-index-log
          note: Each new management invocation receives reloaded schema/catalog without the child requesting
            those individual retained parts.
        records:
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-session-distill
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-index-log
        note: A target workflow request does not itself request each retained guidance/catalog part; code
          preselects them for the child.
      - scope: After-clean refresh into registered later-host context files
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-context-delivery
          - memory.md#mem-obj-context-registry
          - memory.md#mem-obj-host-bootstrap
          - runtime.md#rt-rte-watch-repair
          note: The loop renders and supplies a persisted bootstrap/digest to registered hosts without
            a new retrieval request from those consumers.
        records:
        - runtime.md#rt-rte-context-delivery
        - memory.md#mem-obj-context-registry
        - memory.md#mem-obj-host-bootstrap
        - runtime.md#rt-rte-watch-repair
        note: The automatic clean-triggered projection is distinct from a subsequent explicit host page
          lookup.
      records:
      - runtime.md#rt-rte-context-delivery
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-wiki-body
      - memory.md#mem-obj-local-projection
      - memory.md#mem-rte-query-save
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-obj-wiki-schema
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-context-registry
      - memory.md#mem-obj-host-bootstrap
      - runtime.md#rt-rte-watch-repair
      note: Coverage includes explicit retrieval requests and automatic preselection/projection supply.
        Delivery into files and prompts is wired; actual external host loading remains unobserved.
    read_back_signal:
      assessment: known
      units:
      - scope: Per-invocation maintenance schema/catalog preselection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-session-distill
          - memory.md#mem-obj-wiki-schema
          - memory.md#mem-obj-index-log
          note: Automatically inlined live schema and index are broad standing context for the child.
        records:
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-session-distill
        - memory.md#mem-obj-wiki-schema
        - memory.md#mem-obj-index-log
        note: Trigger is a management invocation; selection uses availability and the configured schema/catalog
          roles, not task matching.
      - scope: Clean-triggered host digest construction
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-host-bootstrap
          - memory.md#mem-obj-context-registry
          - runtime.md#rt-rte-context-delivery
          note: Default first-five-per-scene digest and minimal/full mode are availability/order filtering,
            not task inference.
        records:
        - memory.md#mem-obj-host-bootstrap
        - memory.md#mem-obj-context-registry
        - runtime.md#rt-rte-context-delivery
        note: Trigger is a zero-issue report; selector uses the reloaded wiki inventory/order and configured
          mode; selected parts are count-bounded page names/descriptions.
      - scope: Bound-scene manifest selection during host projection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-scene-manifest
          - memory.md#mem-obj-host-bootstrap
          - memory.md#mem-obj-context-registry
          note: A bound scene name identifies the manifest whose description/triggers are rendered into
            host context.
        records:
        - memory.md#mem-obj-scene-manifest
        - memory.md#mem-obj-host-bootstrap
        - memory.md#mem-obj-context-registry
        note: Explicit scene names select corresponding retained manifests for rendered trigger guidance.
          This does not filter the full page digest and bulk refresh can lose bindings.
      records:
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-obj-wiki-schema
      - memory.md#mem-obj-index-log
      - memory.md#mem-obj-host-bootstrap
      - memory.md#mem-obj-context-registry
      - runtime.md#rt-rte-context-delivery
      - memory.md#mem-obj-scene-manifest
      note: Signals describe only included push operations, not explicit query terms or addressed pull
        files. Registry host keys choose destinations; they do not by themselves identify selected page
        payloads.
    trace_learning:
      assessment: partial
      units:
      - scope: Delegated session extraction to durable schema learning note to later maintenance prompt
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-schema
          - runtime.md#rt-rte-session-distill
          - runtime.md#rt-bap-schema-prompt
          note: Recorded session experience automatically supplies a requested retained behavior-shaping
            note that later management invocations receive.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-schema
        - runtime.md#rt-rte-session-distill
        - runtime.md#rt-bap-schema-prompt
        note: The code requests a trace-fed durable guidance update and later reloads that artifact. The
          wired basis does not assert compliance or benefit.
      - scope: Session-derived summaries/pages used as later knowledge context
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - memory.md#mem-obj-wiki-body
          - runtime.md#rt-rte-session-distill
          - runtime.md#rt-rte-ingest-write
          - runtime.md#rt-rte-context-delivery
          note: The delegated branch requests retained decisions/practices from sessions; later ingestion
            and answering routes can consume that derived context.
        records:
        - memory.md#mem-obj-session-markdown
        - memory.md#mem-obj-wiki-body
        - runtime.md#rt-rte-session-distill
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-context-delivery
        note: The summary extraction/retention and ordinary later-consumer paths are wired; open ingestion
          can also take non-trace sources and resulting artifacts are not supplied.
      - scope: Other source-to-wiki, semantic-repair and foreground-save writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-body
        - runtime.md#rt-rte-ingest-write
        - runtime.md#rt-rte-semantic-lint
        - memory.md#mem-rte-query-save
        note: No complete input/output inventory identifies every additional qualifying automatic trace-fed
          update. Neither the absence of examples nor mechanical conversion by itself warrants a system-wide
          no.
      records:
      - memory.md#mem-obj-session-markdown
      - memory.md#mem-obj-wiki-schema
      - runtime.md#rt-rte-session-distill
      - runtime.md#rt-bap-schema-prompt
      - memory.md#mem-obj-wiki-body
      - runtime.md#rt-rte-ingest-write
      - runtime.md#rt-rte-context-delivery
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-semantic-lint
      - memory.md#mem-rte-query-save
      note: The qualifying positive is an automatic session-fed schema update and reload chain, not demonstrated
        improvement. Mechanical conversion alone is not learning; open source-to-wiki alternatives are
        not made negative merely because their inputs are missing.
    trace_source:
      assessment: partial
      units:
      - scope: Recorded turns feeding delegated session summaries and schema learning notes
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - runtime.md#rt-rte-session-distill
          - memory.md#mem-obj-wiki-schema
          note: The qualifying update consumes recorded conversational turns from agent work sessions.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-session-markdown
          - runtime.md#rt-rte-session-distill
          note: Session origin can include recorded textual tool messages and tool-use names; only surviving/selected
            tool-derived content is covered, not universally preserved arguments or nested tool results.
        records:
        - memory.md#mem-obj-session-markdown
        - runtime.md#rt-rte-session-distill
        - memory.md#mem-obj-wiki-schema
        note: The input is session material, but input hints and provider formats leave the full mixed
          content unenumerated.
      - scope: Other qualifying source-to-wiki and saved-answer alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-body
        - runtime.md#rt-rte-ingest-write
        - memory.md#mem-rte-query-save
        note: The records contain no actual source corpus establishing additional original trace classes
          or excluding them; event-streams and trajectories are not inferred from timestamps or action-log
          persistence.
      records:
      - memory.md#mem-obj-session-markdown
      - runtime.md#rt-rte-session-distill
      - memory.md#mem-obj-wiki-schema
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-wiki-body
      - runtime.md#rt-rte-ingest-write
      - memory.md#mem-rte-query-save
      note: Original session content, rather than parser labels or Markdown serialization, establishes
        the known source. Mixed or omitted tool detail and open input hints prevent exhaustive source
        classification.
---

# ai-memex-cli memory profile

## Comparison rationale

The local artifact inventory separates bodies, access fields and guidance rather than assigning the entire runtime one storage or authority value. [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata) supports both a files-backed header and a recomputed in-memory access structure. The Git-backed product description does not establish repository-backed memory writes. External model weights and qmd internals are excluded dependencies, not silently classified from their interfaces.

The reconciliation supplies no supersessions. Its valid object containers remain alongside operative parts; this profile cites the narrower memory parts where their consumers differ. No record is renamed or replaced. Classification rests on the supplied accepted records only; no frozen-source file was read for this job.

The strongest trace-fed path is the implemented request to append session learnings to the live schema, followed by later schema loading: [RT-RTE-session-distill](runtime.md#rt-rte-session-distill), [MEM-OBJ-wiki-schema](memory.md#mem-obj-wiki-schema) and [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt). Experience has learning authority at that update consumer and the resulting note has instruction authority at the later maintenance agent. The separate summary-to-later-context path also qualifies without requiring a new claim or observed improvement. Mechanical rendering alone does not establish lesson learning. Tool-origin classification is restricted to selected surviving tool-derived session content described by [MEM-OBJ-session-markdown](memory.md#mem-obj-session-markdown); no complete tool transcript or all-source coverage is asserted.

Curation deliberately retains weaker findings. The record of a model request establishes requested consolidation, revision or duplicate treatment, not an observed successful transformation. The fixed digest renderer independently establishes wired consolidation. No synthesize finding follows from a synthesis page type: [EPI-CLM-synthetic-pages](epistemic.md#epi-clm-synthetic-pages) and the route assessments leave actual new-claim production unresolved. Template seeding, primary-key refusal and simple index rebuilding are not independently called curation.

Read-back separates requested retrieval from preselected context. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) supports pull search/injection and a distinct after-clean persistent supply route. The latter is push to host files, not proof of unsolicited delivery into an already running model. Broad digest slicing is coarse selection; exact bound scene names select retained manifest guidance, but registry destination keys do not establish page-level identifier matching. Scene-binding loss and missing per-entry vault identity in [MEM-OBJ-context-registry](memory.md#mem-obj-context-registry) limit the persistence of that targeting without negating its initial wired path.

The partial axes retain unknown initial manifest admission, generic caller control, mixed trace inputs and unseen semantic outputs. Those gaps prevent exhaustive lineage, admission, curation and trace classifications; they do not erase positive paths. Actual user approval, model compliance, host activation, accuracy and benefit remain unobserved throughout. The conflicting foreground-save alternatives in [MEM-RTE-query-save](memory.md#mem-rte-query-save) are classified separately rather than promoted into a universal human gate.
