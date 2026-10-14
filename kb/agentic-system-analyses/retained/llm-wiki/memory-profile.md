---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of llm-wiki: accumulated project documents, maintained Markdown and mutable
  guidance with an opaque optional qmd index.'
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
source-identity: https://github.com/cobusgreyling/llm-wiki
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
memory-comparison:
  version: 2
  scope: Human-admitted raw originals; maintained source, entity/concept, synthesis, contradiction and
    answer pages; changed catalog, page access metadata and operation history; instructions and templates
    only as changed through use; their write, maintenance and later-consumer routes, including optional
    opaque qmd retained index state. Excludes unchanged shipped scaffolds, transient computed graphs/reports
    and watcher suppression, external host context/compaction and provider model weights.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: source summary prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-sources
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id001
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: entity and concept prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-topics
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id002
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: revised synthesis prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-synthesis
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id003
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: contradiction claims and resolution prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-contradictions
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id004
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: filed answer prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-answers
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id005
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: maintained catalog prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id006
          - memory.md#mem-obj-index
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id006
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: appended operation history prose
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id007
          - memory.md#mem-obj-log
          note: Retained Markdown file; implemented corpus enumeration and reload expose these files,
            while semantic production remains prescribed.
        records: *id007
        note: Retained Markdown file; implemented corpus enumeration and reload expose these files, while
          semantic production remains prescribed.
      - scope: human-curated raw originals
        assessment: known
        findings:
        - value: files
          basis: claimed
          records: &id008
          - memory.md#mem-obj-raw
          note: Original documents persist in project raw storage under the prescribed acquisition protocol.
        records: *id008
        note: Original documents persist in project raw storage under the prescribed acquisition protocol.
      - scope: modified maintainer instructions and project templates
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id009
          - runtime.md#rt-rte-instruction-sync
          - runtime.md#rt-rte-page-create
          note: Sync and template consumption use filesystem text; only versions changed through use are
            included.
        records: *id009
        note: Sync and template consumption use filesystem text; only versions changed through use are
          included.
      - scope: optional qmd retained collection and numerical/index state
        assessment: uninspected
        findings: []
        records: &id019
        - runtime.md#rt-rte-qmd-search
        note: External storage implementation is not recorded; a vector or database substrate cannot be
          inferred from embedding setup.
      records:
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-topics
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-contradictions
      - memory.md#mem-obj-answers
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-rte-page-create
      - runtime.md#rt-rte-qmd-search
      note: Files are supported across the retained project inventory. The included alternative qmd store
        prevents complete substrate coverage. Optional Git initialization alone does not establish retained
        memory in a repository.
    representational_form:
      assessment: partial
      units:
      - scope: source summary prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id010
          - memory.md#mem-obj-sources
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id010
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: entity and concept prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id011
          - memory.md#mem-obj-topics
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id011
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: revised synthesis prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id012
          - memory.md#mem-obj-synthesis
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id012
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: contradiction claims and resolution prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id013
          - memory.md#mem-obj-contradictions
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id013
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: filed answer prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id014
          - memory.md#mem-obj-answers
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id014
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: maintained catalog prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id015
          - memory.md#mem-obj-index
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id015
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: appended operation history prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id016
          - memory.md#mem-obj-log
          note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
            classified.
        records: *id016
        note: This part supplies prose interpreted by a human or agent; symbolic access fields are separately
          classified.
      - scope: raw source prose
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: *id008
          note: The protocol requires source reading; this classifies document prose, not every imported
            encoding.
        records: *id008
        note: The protocol requires source reading; this classifies document prose, not every imported
          encoding.
      - scope: raw images and unspecified data-file encodings
        assessment: not-determinable
        findings: []
        records: *id008
        note: The record includes images and data but does not establish a controlled form for all of
          them.
      - scope: page names, raw_file, sources, wikilinks and parsed log headings at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id017
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-rte-log-read
          note: Association, link resolution and log parsing consume localized fields under fixed code
            rules.
        records: *id017
        note: Association, link resolution and log parsing consume localized fields under fixed code rules.
      - scope: changed maintainer instructions and template guidance interpreted by agents
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id018
          - runtime.md#rt-rte-instruction-sync
          - runtime.md#rt-bap-maintainer-instructions
          - runtime.md#rt-rte-page-create
          note: Modified guidance has natural-language consumption; static package text alone is outside
            accumulated memory.
        records: *id018
        note: Modified guidance has natural-language consumption; static package text alone is outside
          accumulated memory.
      - scope: qmd retained numerical/index representation
        assessment: uninspected
        findings: []
        records: *id019
        note: Adapter display snippets do not establish the form of the opaque retained index.
      records:
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-topics
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-contradictions
      - memory.md#mem-obj-answers
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-rte-log-read
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-bap-maintainer-instructions
      - runtime.md#rt-rte-page-create
      - runtime.md#rt-rte-qmd-search
      note: Natural-language and symbolic parts have separate consumers. Raw nonprose encodings and qmd
        state remain unresolved; external model weights and host context are excluded.
    lineage:
      assessment: partial
      units:
      - scope: source summary prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id020
          - memory.md#mem-obj-sources
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id020
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: entity and concept prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id021
          - memory.md#mem-obj-topics
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id021
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: revised synthesis prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id022
          - memory.md#mem-obj-synthesis
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id022
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: contradiction claims and resolution prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id023
          - memory.md#mem-obj-contradictions
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id023
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: filed answer prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id024
          - memory.md#mem-obj-answers
          - runtime.md#rt-rte-wiki-query
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id024
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: maintained catalog prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id025
          - memory.md#mem-obj-index
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id025
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: appended operation history prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id026
          - memory.md#mem-obj-log
          - runtime.md#rt-rte-source-ingest
          note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
            reasoning and faithful derivation are not established.
        records: *id026
        note: The protocol assigns content writing or incremental integration to the maintainer. Model-internal
          reasoning and faithful derivation are not established.
      - scope: raw originals admitted by human source curation
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records: *id008
          note: Externally acquired originals enter raw storage; authenticity and conversion are not established.
        records: *id008
        note: Externally acquired originals enter raw storage; authenticity and conversion are not established.
      - scope: rendered page templates becoming retained placeholders or forced replacements
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id027
          - runtime.md#rt-rte-page-create
          note: Implemented placeholder substitution derives retained page text from project templates;
            this is not semantic synthesis.
        records: *id027
        note: Implemented placeholder substitution derives retained page text from project templates;
          this is not semantic synthesis.
      - scope: changed canonical guidance copied to scaffold/example instruction files
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id028
          - runtime.md#rt-rte-instruction-sync
          note: Whole-text synchronization imports canonical instruction bytes into target files without
            a semantic transformation.
        records: *id028
        note: Whole-text synchronization imports canonical instruction bytes into target files without
          a semantic transformation.
      - scope: initial admission and derivation of mutable instructions, templates and metadata
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-sync
        - memory.md#mem-obj-page-metadata
        - runtime.md#rt-rte-page-create
        note: Records identify caller/agent fields and co-evolution but not every origin or initial-content
          derivation.
      - scope: qmd index and embedding provenance
        assessment: uninspected
        findings: []
        records: *id019
        note: External index construction and embedding provenance remain outside the inspected adapter.
      records:
      - memory.md#mem-obj-sources
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-topics
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-contradictions
      - memory.md#mem-obj-answers
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-page-create
      - runtime.md#rt-rte-instruction-sync
      - memory.md#mem-obj-page-metadata
      - runtime.md#rt-rte-qmd-search
      note: Authored interpretations, imported originals/copies and compiled placeholders coexist. No
        trace-extracted lineage follows from an authored operation log; opaque provenance remains included.
    behavioral_authority:
      assessment: partial
      units:
      - scope: retained subject-matter prose at later answering and maintenance agents
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id029
          - memory.md#mem-bap-wiki-content
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-topics
          - memory.md#mem-obj-synthesis
          - memory.md#mem-obj-contradictions
          - memory.md#mem-obj-answers
          - memory.md#mem-obj-index
          - memory.md#mem-obj-log
          note: Requested later reload supplies evidence, interpretation, prior analysis and discovery
            advice; compliance and benefit remain unobserved.
        records: *id029
        note: Requested later reload supplies evidence, interpretation, prior analysis and discovery advice;
          compliance and benefit remain unobserved.
      - scope: changed maintainer guidance at external maintainer
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records: &id030
          - runtime.md#rt-rte-instruction-sync
          - runtime.md#rt-bap-maintainer-instructions
          note: Reloaded changed conventions provide standing directions, conditional on host loading.
        records: *id030
        note: Reloaded changed conventions provide standing directions, conditional on host loading.
      - scope: retained prose and frontmatter at built-in BM25 scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id031
          - runtime.md#rt-rte-wiki-query
          note: Current file text and boosted headings determine relative retrieval scores under fixed
            lexical code.
        records: *id031
        note: Current file text and boosted headings determine relative retrieval scores under fixed lexical
          code.
      - scope: raw_file, sources, paths and wikilinks at structural inspectors
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id032
          - memory.md#mem-obj-page-metadata
          - runtime.md#rt-rte-wiki-lint
          note: Retained associations and references supply criteria for structural conformity, not source
            truth or pre-write semantic acceptance.
        records: *id032
        note: Retained associations and references supply criteria for structural conformity, not source
          truth or pre-write semantic acceptance.
      - scope: source association metadata at coverage classifier and pending notification selector
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id033
          - memory.md#mem-obj-page-metadata
          - epistemic.md#epi-rte-source-coverage
          - runtime.md#rt-rte-pending-watch
          note: The retained raw-file mapping changes pending/ingested classification and which filenames
            are notified. Process-local suppression state is excluded.
        records: *id033
        note: The retained raw-file mapping changes pending/ingested classification and which filenames
          are notified. Process-local suppression state is excluded.
      - scope: qmd retained state at external ranking and selection consumers
        assessment: uninspected
        findings: []
        records: *id019
        note: The adapter returns scored results, but the consumed retained parts and their internal effects
          are not inspected.
      records:
      - memory.md#mem-bap-wiki-content
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-topics
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-contradictions
      - memory.md#mem-obj-answers
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-bap-maintainer-instructions
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-obj-page-metadata
      - runtime.md#rt-rte-wiki-lint
      - epistemic.md#epi-rte-source-coverage
      - runtime.md#rt-rte-pending-watch
      - runtime.md#rt-rte-qmd-search
      note: Knowledge and instruction concern different external consumers; ranking, structural validation
        and notification routing concern inspected code. Opaque qmd effects prevent a complete authority
        inventory. No automatic log-fed learning consumer is established.
    write_agency:
      assessment: partial
      units:
      - scope: human admission of raw originals
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: *id008
          note: An explicit human source-curation decision supplies the retained originals.
        records: *id008
        note: An explicit human source-curation decision supplies the retained originals.
      - scope: agent semantic admission during ingest and prescribed immediate lint corrections
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id034
          - runtime.md#rt-rte-source-ingest
          - runtime.md#rt-rte-wiki-lint
          note: Agent determines individual writes; an initiating human request or discussion is not per-content
            approval. Batch ingest supplies a countercase to universal discussion.
        records: *id034
        note: Agent determines individual writes; an initiating human request or discussion is not per-content
          approval. Batch ingest supplies a countercase to universal discussion.
      - scope: optional answer filing admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-query
        - memory.md#mem-obj-answers
        note: An offer to file is recorded, but no explicit acceptance handshake establishes whether the
          human or agent admits each retained answer.
      - scope: page creation and forced replacement admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-page-create
        note: Generic caller chooses title/type/force; caller identity does not establish a human decision
          supplying or replacing retained content.
      - scope: changed instruction and template admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-sync
        - runtime.md#rt-rte-page-create
        note: Human co-evolution is requested, but final per-change control and template editing decisions
          are unspecified. Blind copying is physical propagation, not proof of admission agency.
      - scope: qmd collection admission and subsequent refresh
        assessment: not-determinable
        findings: []
        records: *id019
        note: Manual setup is afforded, but records do not establish control of all retained content or
          refresh writes.
      records:
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-wiki-lint
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-obj-answers
      - runtime.md#rt-rte-page-create
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-rte-qmd-search
      note: Human raw curation and prescribed model admission have separate warrants. Filing, generic
        scaffold callers, guidance changes and external index admission retain control uncertainty.
    curation_operations:
      assessment: partial
      units:
      - scope: source summaries from retained raw documents
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records: &id035
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-sources
          note: Requested extraction reduces source assertions into a summary; no execution or fidelity
            is established.
        records: *id035
        note: Requested extraction reduces source assertions into a summary; no execution or fidelity
          is established.
      - scope: incremental topic, synthesis and contradiction revisions
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id036
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-topics
          - memory.md#mem-obj-synthesis
          - memory.md#mem-obj-contradictions
          note: Protocol requests revision of existing entries when new source content changes the picture;
            this supports requested evolution, not observed updates.
        records: *id036
        note: Protocol requests revision of existing entries when new source content changes the picture;
          this supports requested evolution, not observed updates.
      - scope: semantic fixes during delegated lint
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id037
          - runtime.md#rt-rte-wiki-lint
          note: The agent is instructed to fix existing errors and review conflicts; toolkit diagnosis
            itself does not transform retained memory.
        records: *id037
        note: The agent is instructed to fix existing errors and review conflicts; toolkit diagnosis itself
          does not transform retained memory.
      - scope: cross-source synthesis and answer transformation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-query
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-obj-wiki-pages
        note: 'Semantic correspondence is indeterminate: route names and synthesized wording do not establish
          a new claim absent from inputs.'
      - scope: instruction convention revision semantics
        assessment: not-determinable
        findings: []
        records: *id028
        note: Co-evolution requests changes but does not record an implemented transformation class over
          accumulated guidance.
      - scope: qmd retained index maintenance
        assessment: uninspected
        findings: []
        records: *id019
        note: External index maintenance does not inherit a curation operation from wiki edits.
      records:
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-topics
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-contradictions
      - runtime.md#rt-rte-wiki-lint
      - runtime.md#rt-rte-wiki-query
      - epistemic.md#epi-obj-wiki-pages
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-rte-qmd-search
      note: Claimed consolidation and evolution are retained at their doctrine layer, not upgraded by
        implemented template writes. No recorded semantic correspondence establishes synthesize; opaque
        maintenance remains unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: question-driven catalog/search and page/section expansion
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: *id031
          note: Consumer/agent requests retained material; ranked selection and code delivery fulfill
            that request rather than create an unsolicited push.
        records: *id031
        note: Consumer/agent requests retained material; ranked selection and code delivery fulfill that
          request rather than create an unsolicited push.
      - scope: requested metadata, log, status and lint inspection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id038
          - memory.md#mem-rte-metadata-read
          - memory.md#mem-rte-log-read
          - epistemic.md#epi-rte-source-coverage
          - runtime.md#rt-rte-wiki-lint
          note: Later inspection requests read current accumulated content or associations and return
            selected data.
        records: *id038
        note: Later inspection requests read current accumulated content or associations and return selected
          data.
      - scope: requested qmd alternative search
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: *id019
          note: Inspected adapter invokes qmd for a consumer query and returns adapted results; internal
            state and freshness remain opaque.
        records: *id019
        note: Inspected adapter invokes qmd for a consumer query and returns adapted results; internal
          state and freshness remain opaque.
      - scope: direct agent file reads prescribed for later maintenance
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id039
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-bap-wiki-content
          note: The external maintainer is instructed to read affected retained pages.
        records: *id039
        note: The external maintainer is instructed to read affected retained pages.
      - scope: later loading of changed instructions and templates by external host
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-instruction-sync
        - runtime.md#rt-bap-maintainer-instructions
        - runtime.md#rt-rte-page-create
        note: Later guidance consumption is afforded, but host loading trigger and request-versus-unsolicited
          delivery are not established.
      records:
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-rte-metadata-read
      - memory.md#mem-rte-log-read
      - epistemic.md#epi-rte-source-coverage
      - runtime.md#rt-rte-wiki-lint
      - runtime.md#rt-rte-qmd-search
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-bap-wiki-content
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-bap-maintainer-instructions
      - runtime.md#rt-rte-page-create
      note: Tool and protocol file-request routes support pull. Host loading of changed guidance remains
        unresolved. Watch notifications expose pending filenames, not a wired unsolicited knowledge-context
        delivery; no push is inferred from requested search returns.
    read_back_signal:
      assessment: uninspected
      units:
      - scope: fully inspected requested CLI/MCP knowledge and inspection returns
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-query
        - runtime.md#rt-rte-qmd-search
        - memory.md#mem-rte-metadata-read
        - memory.md#mem-rte-log-read
        note: These are pull operations; identifiers and BM25 relevance in a requested response do not
          establish push signals.
      - scope: external host loading of changed guidance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-instruction-sync
        - runtime.md#rt-bap-maintainer-instructions
        note: Without an established direction, trigger or selector input, neither a push signal nor pull-only
          inapplicability can be assigned.
      records:
      - runtime.md#rt-rte-wiki-query
      - runtime.md#rt-rte-qmd-search
      - memory.md#mem-rte-metadata-read
      - memory.md#mem-rte-log-read
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-bap-maintainer-instructions
      note: No positive push selector is established. Pull-only tool units are inapplicable locally; unresolved
        guidance loading prevents axis-wide inapplicability.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: semantic ingest, answer filing and authored operation history
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-wiki-query
        - memory.md#mem-obj-log
        note: Recorded inputs are documents and questions plus selected knowledge, not an established
          automatic trace-to-durable-update chain. An authored history alone cannot establish trace learning
          or a bounded system-wide no.
      - scope: instruction convention changes and synchronization
        assessment: not-determinable
        findings: []
        records: *id028
        note: No automatic log-to-guidance update is recorded; absence of a wired connection in this account
          is not a dedicated bounded absence warrant for every qualifying update.
      - scope: optional qmd retained updates
        assessment: uninspected
        findings: []
        records: *id019
        note: External update inputs and later consumers are not inspected; embedding setup alone establishes
          no qualifying trace-fed write.
      records:
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-obj-log
      - runtime.md#rt-rte-instruction-sync
      - runtime.md#rt-rte-qmd-search
      note: No accepted record establishes a qualifying automatic trace-fed write or a complete bounded
        absence across the included update inventory. Host session compaction and provider weight updates
        are excluded, not classified as no.
    trace_source:
      assessment: not-determinable
      units:
      - scope: ingest, answer/history and instruction changes without an established qualifying trace-fed
          update
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-wiki-query
        - runtime.md#rt-rte-instruction-sync
        - memory.md#mem-obj-log
        note: Original trace inputs to a qualifying update are not established. Questions do not automatically
          constitute consumed session logs, and authored history is not authenticated tool/session traces.
      - scope: qmd update provenance
        assessment: uninspected
        findings: []
        records: *id019
        note: External input provenance cannot establish or exclude any controlled trace source.
      records:
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-wiki-query
      - runtime.md#rt-rte-instruction-sync
      - memory.md#mem-obj-log
      - runtime.md#rt-rte-qmd-search
      note: Trace learning is unresolved, not completely assessed absent. Consequently trace source cannot
        be declared system-wide inapplicable or assigned from serialization or log names.
---

# llm-wiki memory profile

## Comparison rationale

The inventory separates accumulated project content from unchanged shipped instructions and transient helper results. Markdown is a file substrate, not a graph substrate merely because reconstructed wikilinks form a graph. Optional Git initialization does not establish repository-based retained memory. The alternative index stays unresolved rather than inheriting BM25 classifications. See [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata), [MEM-RTE-metadata-read](memory.md#mem-rte-metadata-read), [RT-RTE-project-init](runtime.md#rt-rte-project-init) and [RT-RTE-qmd-search](runtime.md#rt-rte-qmd-search).

Prescribed semantic writing supplies claimed authorship, consolidation and evolution. Implemented template rendering supplies other-compiled lineage, not semantic synthesis. The epistemic container retains indeterminate semantic correspondence; its name cannot establish a novel claim. Initial provenance, generic caller identity and filing offers remain separate admission gaps. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-page-create](runtime.md#rt-rte-page-create), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [EPI-OBJ-wiki-pages](epistemic.md#epi-obj-wiki-pages).

Retained text can supply knowledge to an agent and ranking features to code without supplying enforcement or learning. Retained association fields can supply structural validation criteria and route pending notifications without authenticating source claims. Changed maintainer guidance supplies instruction authority only at its external consumer. These effects do not establish activation, benefit or a log-fed update. See [MEM-BAP-wiki-content](memory.md#mem-bap-wiki-content), [RT-BAP-maintainer-instructions](runtime.md#rt-bap-maintainer-instructions), [EPI-RTE-source-coverage](epistemic.md#epi-rte-source-coverage) and [RT-RTE-instruction-sync](runtime.md#rt-rte-instruction-sync).

Requested ranked returns and explicit heading matches remain pull. They are not push merely because software selects and delivers text. Changed guidance loading remains unresolved, so read-back signal is not globally inapplicable. Recent-log delivery omits bodies and hyphenated operations; the retained full log still has a separate reload path. See [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-RTE-log-read](memory.md#mem-rte-log-read) and [MEM-CLM-log-parser](memory.md#mem-clm-log-parser).

Reconciliation supersedes the epistemic raw, source-page and contradiction objects with the corresponding memory objects, and the epistemic catalog route with the memory metadata route. All classifications use those canonical declarations. The broader epistemic wiki-page container and combined log-inspection route remain valid rather than being split-superseded. No supersession changes a positive controlled value; the separate memory objects preserve local lineage and consumer distinctions.

No frozen-source files were read for this classification. Only the supplied accepted members and contracts were used. No records, quotations or evidence were added. Missing execution evidence limits observation and benefit, not the inspected helper wiring. Missing update/input records prevent a stronger trace-learning or trace-source assessment; an unknown is not converted into a negative.
