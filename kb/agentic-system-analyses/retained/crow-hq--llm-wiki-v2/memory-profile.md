---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "LLM Wiki v2 memory comparison: retained knowledge, access structure, operational history and response reuse at the frozen source boundary."
run-id: "AAS-2026-11-08-llm-wiki-v2-5abff9a6c5c3-01"
source-identity: "https://github.com/crow-hq/llm-wiki-v2"
reviewed-boundary: "e0a205afe60bd1913d083a3ed4cdab81e38e4c26"
memory-comparison:
  version: 2
  scope: "Through-use bundle note bodies and metadata, raw extracted sources, folder indexes/descriptions, archives, logs, sync wrapper state, area proposals, classifier cache, benchmark replay and recorded evaluation inputs/results; their admission, maintenance and later consumption. Includes unresolved injected cache/custom-Step alternatives and caller provenance. Excludes static shipped prompts, transient current-call/relay state, enclosing MCP client memory, external provider parameters and external connector internals; opaque cursor payload interpretation remains unresolved rather than inferred from its wrapper."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Bundle note bodies, frontmatter, indexes, raw copies and archives"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-body"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-raw"
                -
                  "memory.md#mem-obj-archive"
              note: "Markdown/YAML and directory state persist on disk; repository distribution is not a memory repo substrate."
          records:
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-archive"
          note: "All named bundle parts have file-backed retention; reconstructed Python objects are working views, not a second durable substrate."
        -
          scope: "Log, sync wrapper state, proposal queue and benchmark replay/results"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "memory.md#mem-obj-sync-state"
                -
                  "memory.md#mem-obj-proposals"
                -
                  "memory.md#mem-obj-replay"
                -
                  "memory.md#mem-obj-evaluation-results"
              note: "Markdown log, JSON/JSONL control records, replay JSON and retained benchmark files."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-proposals"
            -
              "memory.md#mem-obj-replay"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "This classifies the recorded wrapper stores, not the opaque connector cursor's external interpretation."
        -
          scope: "Default classifier answer cache"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-answer-cache"
              note: "The default cache is classifier.sqlite, not classifier parameter storage."
          records:
            -
              "memory.md#mem-obj-answer-cache"
          note: "Default implementation is inspected."
        -
          scope: "Injected AnswerCache and caller-defined retained state in custom Steps"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-answer-cache"
            -
              "runtime.md#rt-rte-source-filing"
          note: "Alternative implementation contracts do not establish their actual substrates; known default stores cannot classify these alternatives."
      records:
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-archive"
        -
          "memory.md#mem-obj-log"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-proposals"
        -
          "memory.md#mem-obj-replay"
        -
          "memory.md#mem-obj-evaluation-results"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "runtime.md#rt-rte-source-filing"
      note: "Known file and SQLite witnesses coexist with opaque injectable implementations. External provider weights, static packaged instructions and transient relay jobs are excluded from accumulated-memory storage."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Retained note/raw/archive prose, folder descriptions, descriptive metadata, proposal prose and replay writer replies"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-body"
                -
                  "memory.md#mem-obj-raw"
                -
                  "memory.md#mem-obj-archive"
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-proposals"
                -
                  "memory.md#mem-obj-replay"
              note: "Models or callers interpret prose; only the delivered title/summary/main body reaches ordinary answering."
          records:
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-archive"
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-proposals"
            -
              "memory.md#mem-obj-replay"
          note: "Prose is separated from code-consumed fields in the next unit; raw copies are extracted text rather than original office bytes."
        -
          scope: "Retained code-consumed metadata, structure, sheet rows, log counters, cursor wrapper, cost history, proposals, classifier/replay answers and evaluator metrics"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-raw"
                -
                  "memory.md#mem-obj-archive"
                -
                  "memory.md#mem-obj-log"
                -
                  "memory.md#mem-obj-sync-state"
                -
                  "memory.md#mem-obj-proposals"
                -
                  "memory.md#mem-obj-answer-cache"
                -
                  "memory.md#mem-obj-replay"
                -
                  "memory.md#mem-obj-evaluation-results"
              note: "Fixed rules consume paths, IDs, hashes, fields, state flags, scalar probabilities, counters and metric rows; scalar outputs are not distributed parameters."
          records:
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-archive"
            -
              "memory.md#mem-obj-log"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-proposals"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-obj-replay"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "This covers inspected encodings and consumers, not the semantics of connector-owned payloads."
        -
          scope: "Opaque connector cursor payload and injected cache/custom-Step memory"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "runtime.md#rt-rte-source-filing"
          note: "The wrapper's symbolic cursor string does not disclose the connector's operative representation; alternatives have no recorded internal encoding."
      records:
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-archive"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "memory.md#mem-obj-proposals"
        -
          "memory.md#mem-obj-replay"
        -
          "memory.md#mem-obj-log"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-evaluation-results"
        -
          "runtime.md#rt-rte-source-filing"
      note: "The recorded memory has natural-language and symbolic paths. Provider models are not retained through-use memory objects in this scope; no parametric-memory finding follows from calling them."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Ingested extracted source text and externally supplied retained Markdown"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-raw"
                -
                  "memory.md#mem-obj-note-body"
              note: "Caller documents and locally authored files enter the bundle from outside the filing transformation."
          records:
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-note-body"
          note: "Imported describes the entry path, not human authorship or source truth."
        -
          scope: "Model-generated note bodies, descriptive metadata and taxonomy"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-body"
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "runtime.md#rt-rte-source-filing"
              note: "Summarization, merging, planning and splitting author retained text."
          records:
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "runtime.md#rt-rte-source-filing"
          note: "The generated path is known even though particular source-to-note fidelity is not."
        -
          scope: "Regenerated indexes, copied archives and serialized source/control metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-archive"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-raw"
              note: "Code assembles indexes, snapshots and lineage/control fields from existing objects."
          records:
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-archive"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-raw"
          note: "Mechanical derivation is distinct from prose authorship; an archive keeps the earlier content's unresolved upstream provenance."
        -
          scope: "Recorded split events, sync progress/cost history and cached/replayed model replies"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "memory.md#mem-obj-sync-state"
                -
                  "memory.md#mem-obj-answer-cache"
                -
                  "memory.md#mem-obj-replay"
              note: "Code records operation outcomes, progress and model responses for later reuse."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-obj-replay"
          note: "This is output/history capture, not a claim that every such capture qualifies as trace learning."
        -
          scope: "Initial caller content, remember payload derivation, caller area proposals, evaluation inputs and injected alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-proposals"
            -
              "memory.md#mem-obj-evaluation-results"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-answer-cache"
          note: "Caller identity and imported labels do not disclose how initial claims or experience summaries were produced; evaluator families and arbitrary custom implementations are not fully traced."
      records:
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-obj-archive"
        -
          "memory.md#mem-obj-log"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-replay"
        -
          "memory.md#mem-obj-proposals"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Supported derivation paths do not resolve initial authorship, all benchmark label provenance or external client extraction. Imports can later become inputs to authored or mechanically compiled objects."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Note/raw/archive content at answering, merging, rebuild and MCP read consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-body"
                -
                  "memory.md#mem-obj-raw"
                -
                  "memory.md#mem-obj-archive"
                -
                  "memory.md#mem-bap-retained-knowledge"
                -
                  "runtime.md#rt-rte-question-answer"
                -
                  "memory.md#mem-rte-note-read"
              note: "Selected retained assertions supply reference/context; ordinary full_text excludes most metadata and See-also."
          records:
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-archive"
            -
              "memory.md#mem-bap-retained-knowledge"
            -
              "runtime.md#rt-rte-question-answer"
            -
              "memory.md#mem-rte-note-read"
          note: "Knowledge force is wired delivery and interpretation, not truth acceptance or observed compliance."
        -
          scope: "Retained descriptions and note summaries at classic/CROW relevance consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "runtime.md#rt-rte-question-answer"
              note: "Descriptions and summaries influence relative relevance and thresholded/top-k selection."
            -
              value: "routing"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "runtime.md#rt-rte-source-filing"
              note: "Retained descriptions and organization influence where incoming material is filed."
          records:
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "runtime.md#rt-rte-question-answer"
            -
              "runtime.md#rt-rte-source-filing"
          note: "Distinct consumers support distinct forces; related-link display alone does not prove its target was delivered."
        -
          scope: "Fields, hashes, source references, previous-version paths, proposal state and cached decisions at code consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-sync-state"
                -
                  "memory.md#mem-obj-answer-cache"
                -
                  "memory.md#mem-rte-answer-reuse"
                -
                  "memory.md#mem-obj-proposals"
              note: "Origins/cursors select work windows; predecessor paths select history; cached answers can choose routes and proposal IDs select maintenance targets."
            -
              value: "validation"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-proposals"
                -
                  "runtime.md#rt-rte-manual-maintenance"
              note: "Fields, generated-body hashes and open proposal state determine admissibility of merges, replacement or confirmation."
            -
              value: "enforcement"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-proposals"
                -
                  "runtime.md#rt-rte-manual-maintenance"
              note: "Those code checks can exclude candidates, block automatic replacement or reject stale/closed proposals."
            -
              value: "ranking"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-answer-cache"
                -
                  "memory.md#mem-rte-answer-reuse"
              note: "Reused classifier relevance responses can substitute for fresh ranking decisions."
          records:
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-rte-answer-reuse"
            -
              "memory.md#mem-obj-proposals"
            -
              "runtime.md#rt-rte-manual-maintenance"
          note: "Content used only for display or attribution has no additional inferred force."
        -
          scope: "Split-attempt log at subsequent split suppression and sync cost history at estimates"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "Folder-specific prior attempt counts suppress a later split at the same multiple."
            -
              value: "knowledge"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-sync-state"
              note: "Recorded cost history supplies numerical evidence for a later cost estimate."
            -
              value: "learning"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "Recorded split experience feeds an automatically retained retry-control artifact used in a later decision; this is a local update path, not demonstrated improved competence."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "runtime.md#rt-rte-batch-sync"
            -
              "memory.md#mem-obj-sync-state"
          note: "Operational-history influence is distinct from semantic factual acceptance."
        -
          scope: "Retained benchmark wiki/mappings/labels at offline evaluators"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-evaluation-results"
              note: "Retained wiki and run mappings supply evaluator inputs."
            -
              value: "validation"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-evaluation-results"
              note: "Expected final-note mappings and planted fact labels provide bounded comparison criteria, not an online admission gate."
          records:
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Metrics license selected-note identity or lexical comparisons, not proposition truth."
        -
          scope: "Client-submitted preferences/experience, injected consumers and incompletely traced evaluator parts"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-raw"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-evaluation-results"
            -
              "memory.md#mem-obj-answer-cache"
          note: "The records do not establish standing instruction consumption, automatic host learning, or every custom consumer's force. Connection instructions and per-question conflict hints are static/transient, not retained memory."
      records:
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-archive"
        -
          "memory.md#mem-bap-retained-knowledge"
        -
          "runtime.md#rt-rte-question-answer"
        -
          "memory.md#mem-rte-note-read"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "memory.md#mem-obj-proposals"
        -
          "runtime.md#rt-rte-manual-maintenance"
        -
          "memory.md#mem-obj-log"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Each force belongs to its named retained part and consumer. Unresolved callers and evaluation branches prevent complete authority coverage; no blanket instruction authority is assigned to note-embedded requests."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Default filing, reduction, merge/revision/archive and automatic plan/split admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-source-filing"
                -
                  "memory.md#mem-rte-source-reduction"
                -
                  "epistemic.md#epi-rte-revision-admit"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "Model/software admits generated content after structural and heuristic checks, without per-content human approval."
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-rte-source-reduction"
            -
              "epistemic.md#epi-rte-revision-admit"
            -
              "runtime.md#rt-rte-batch-sync"
          note: "Starting ingest/sync or choosing a mode is not a human decision approving each resulting retained item."
        -
          scope: "Classifier/replay response capture, log and sync wrapper state writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                -
                  "memory.md#mem-rte-answer-reuse"
                -
                  "memory.md#mem-obj-answer-cache"
                -
                  "memory.md#mem-obj-replay"
                -
                  "memory.md#mem-obj-log"
                -
                  "memory.md#mem-obj-sync-state"
              note: "Software captures successful responses, split events, page cursors and cost rows; requesting a replay save does not select each response's content."
          records:
            -
              "memory.md#mem-rte-answer-reuse"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-obj-replay"
            -
              "memory.md#mem-obj-log"
            -
              "memory.md#mem-obj-sync-state"
          note: "Physical file I/O and model authorship are separate from admission."
        -
          scope: "Direct Markdown edits, source supply, caller areas/proposals, audit apply, purge/rebuild and benchmark setup"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-proposals"
            -
              "runtime.md#rt-rte-manual-maintenance"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Generic caller values, user origin labels and confirmation booleans do not verify explicit human decisions over retained content. No supported manual finding is inferred from route names."
        -
          scope: "Custom Steps and injected cache admission"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-answer-cache"
          note: "Caller-defined implementation can change admission; default software control does not resolve that alternative."
      records:
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-rte-source-reduction"
        -
          "epistemic.md#epi-rte-revision-admit"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-replay"
        -
          "memory.md#mem-obj-log"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-proposals"
        -
          "runtime.md#rt-rte-manual-maintenance"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Default transformations and control recording are automatic. Human-versus-software provenance of caller-directed edits and approvals remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Default summarize/merge and source reduction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-source-filing"
                -
                  "memory.md#mem-rte-source-reduction"
                -
                  "memory.md#mem-obj-note-body"
              note: "The implemented route reduces source/existing content into derived notes; fidelity and the one-subject goal remain unproved."
            -
              value: "evolve"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-source-filing"
                -
                  "memory.md#mem-obj-note-body"
                -
                  "epistemic.md#epi-rte-revision-admit"
              note: "Merge and qualifying replacement revise existing retained entries."
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-rte-source-reduction"
            -
              "memory.md#mem-obj-note-body"
            -
              "epistemic.md#epi-rte-revision-admit"
          note: "Verbatim and append fallbacks coexist with reduction; requested semantic deduplication is not treated as demonstrated duplicate elimination."
        -
          scope: "Revision replacement with retained predecessor"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-archive"
                -
                  "epistemic.md#epi-rte-revision-admit"
              note: "Prior active content is displaced but kept as an archive accessible through a classified historical route."
          records:
            -
              "memory.md#mem-obj-archive"
            -
              "epistemic.md#epi-rte-revision-admit"
          note: "This is withdrawal of ordinary active reliance, not deletion of all history or semantic falsification."
        -
          scope: "Automatic splitting, moves, rebuild, purge, index regeneration and source-removal marking"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-batch-sync"
            -
              "runtime.md#rt-rte-manual-maintenance"
            -
              "epistemic.md#epi-rte-origin-purge"
            -
              "memory.md#mem-obj-raw"
            -
              "memory.md#mem-obj-folder-index"
          note: "Organization/reacquisition alone establishes no listed curation operation. Purge deletes lineage and refiles other sources; marking removed leaves derived notes usable. The records do not warrant decay, promotion or retained-history invalidation for these whole routes."
        -
          scope: "Caller edits, custom transformations and all possible model-created novel assertions"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-note-body"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Content changes are possible but their semantic operation is not enumerated. Epistemic indeterminacy does not establish synthesis, and a preservation defect does not turn consolidation into synthesis."
      records:
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-rte-source-reduction"
        -
          "memory.md#mem-obj-note-body"
        -
          "epistemic.md#epi-rte-revision-admit"
        -
          "memory.md#mem-obj-archive"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "runtime.md#rt-rte-manual-maintenance"
        -
          "epistemic.md#epi-rte-origin-purge"
        -
          "memory.md#mem-obj-raw"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Consolidation, evolution and bounded archived invalidation are supported. No complete curation taxonomy or observed successful deduplication follows from names and prompt goals."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Question/recall, explicit note reads, maintenance/rebuild and requested replay/cache answer return"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-question-answer"
                -
                  "memory.md#mem-rte-note-read"
                -
                  "runtime.md#rt-rte-manual-maintenance"
                -
                  "memory.md#mem-rte-answer-reuse"
              note: "Consumers request answers, specific notes, reconstruction or model results; fulfilling these requests is pull even when software selects the response."
          records:
            -
              "runtime.md#rt-rte-question-answer"
            -
              "memory.md#mem-rte-note-read"
            -
              "runtime.md#rt-rte-manual-maintenance"
            -
              "memory.md#mem-rte-answer-reuse"
          note: "Question-conditioned semantic selection is within a requested retrieval chain, not independent proactive injection into the client."
        -
          scope: "Automatic source-filing context and split retry-control supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-source-filing"
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "On ingest/split triggers, code supplies current structure/matched content and prior folder-attempt state to internal decision consumers without those consumers requesting retained items."
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-folder-index"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-log"
            -
              "runtime.md#rt-rte-batch-sync"
          note: "Internal unsolicited supply is distinct from returning the caller's filing result."
        -
          scope: "Sync resume/cost wrapper and proposal targeting chains"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-sync-state"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "A later sync injects its saved connector cursor into change acquisition; estimate code supplies accumulated history to calculation."
            -
              value: "pull"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-proposals"
                -
                  "runtime.md#rt-rte-manual-maintenance"
              note: "List/confirm/dismiss explicitly request retained queue items or actions."
          records:
            -
              "memory.md#mem-obj-sync-state"
            -
              "runtime.md#rt-rte-batch-sync"
            -
              "memory.md#mem-obj-proposals"
            -
              "runtime.md#rt-rte-manual-maintenance"
          note: "Resume injection is not a proactive natural-language memory message to an MCP client."
        -
          scope: "Injected cache/custom Steps and remaining offline evaluator consumers"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-answer-cache"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Records establish selected routes, not all possible automatic deliveries and caller requests."
      records:
        -
          "runtime.md#rt-rte-question-answer"
        -
          "memory.md#mem-rte-note-read"
        -
          "runtime.md#rt-rte-manual-maintenance"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-obj-folder-index"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "memory.md#mem-obj-log"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-proposals"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Both request-directed retrieval and internal automatic state supply are supported. External host injection/compaction is excluded, not silently classified."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Internal filing push of folder/note context"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-folder-index"
                -
                  "runtime.md#rt-rte-source-filing"
              note: "Ingest trigger supplies current tree/available candidate listings subject to structural scope."
            -
              value: "inferred-judgment"
              basis: "wired"
              records:
                -
                  "runtime.md#rt-rte-source-filing"
                -
                  "memory.md#mem-obj-note-metadata"
                -
                  "memory.md#mem-obj-note-body"
              note: "Classic model or CROW classifier chooses semantic route/match and hence the retained note delivered to merge."
          records:
            -
              "memory.md#mem-obj-folder-index"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-note-metadata"
            -
              "memory.md#mem-obj-note-body"
          note: "Trigger is incoming source; selector inputs are source candidate plus descriptions/summaries; selected parts are folder structure and matched existing note. These are internal pushes, not unsolicited answers."
        -
          scope: "Split retry log and connector cursor automatic supply"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
                -
                  "memory.md#mem-obj-sync-state"
              note: "On split, folder identity selects matching previous attempt counts; on sync, connector/account identifies the saved cursor supplied to that connector."
            -
              value: "coarse"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-sync-state"
              note: "Estimate consumes available retained sync cost rows to compute the mean rather than semantic matching."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "runtime.md#rt-rte-batch-sync"
            -
              "memory.md#mem-obj-sync-state"
          note: "Actual identity matches select delivered control state. No embedding signal is inferred from scalar classifier probabilities."
        -
          scope: "Explicit requested notes, question answers, queue items and cached response returns"
          assessment: "inapplicable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-question-answer"
            -
              "memory.md#mem-rte-note-read"
            -
              "memory.md#mem-obj-proposals"
            -
              "memory.md#mem-rte-answer-reuse"
          note: "These named deliveries fulfill retained-material/result requests; their paths/digests or semantic selectors do not by themselves establish a push signal."
        -
          scope: "Custom/injected implementations and remaining evaluator paths"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "No accepted record exposes every alternative selector's trigger/input/delivered part."
      records:
        -
          "memory.md#mem-obj-folder-index"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-obj-note-metadata"
        -
          "memory.md#mem-obj-note-body"
        -
          "memory.md#mem-obj-log"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-obj-sync-state"
        -
          "runtime.md#rt-rte-question-answer"
        -
          "memory.md#mem-rte-note-read"
        -
          "memory.md#mem-obj-proposals"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "Supported push signals apply only to internal unsolicited context/control delivery. The unresolved inventory prevents a complete selector assessment."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic split-attempt history to durable retry control and later splitting"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "Code records previous attempts and later reads folder-specific counts to suppress another split at that count multiple; a durable behavior-shaping control artifact is automatically trace-fed."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "runtime.md#rt-rte-batch-sync"
          note: "Qualifies at wired level without requiring new knowledge, changed weights or successful improvement."
        -
          scope: "Client remember content to notes and later questions"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-raw"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-note-body"
            -
              "runtime.md#rt-rte-question-answer"
          note: "Experience-derived durable outcomes are afforded, but original trace inputs and client extraction/admission control are not established; no automatic host trace capture is wired by the server."
        -
          scope: "Classifier/replay response reuse, sync checkpoints/cost history and offline evaluator feedback"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-rte-answer-reuse"
            -
              "memory.md#mem-obj-answer-cache"
            -
              "memory.md#mem-obj-replay"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Records establish automatic recording/reuse and estimates, but do not fully distinguish qualifying behavior-shaping trace updates from memoized inference, progress plumbing and reported metrics, nor trace every original input and later feedback path."
        -
          scope: "Injected custom Step/cache update paths"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-answer-cache"
          note: "No recorded bounded absence covers these alternatives and no qualifying route is exposed."
      records:
        -
          "memory.md#mem-obj-log"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-obj-raw"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-obj-note-body"
        -
          "runtime.md#rt-rte-question-answer"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "memory.md#mem-obj-answer-cache"
        -
          "memory.md#mem-obj-replay"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-evaluation-results"
      note: "A supported local yes coexists with unresolved routes. No local or system-wide no is asserted because the reports declare no bounded absence records; wired adaptation is not observed benefit."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Qualifying split-history retry-control write"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                -
                  "memory.md#mem-obj-log"
                -
                  "runtime.md#rt-rte-batch-sync"
              note: "Original input is discrete filing/split-attempt activity with folder/count/outcome, recorded as operational log events and consumed by later splitting."
          records:
            -
              "memory.md#mem-obj-log"
            -
              "runtime.md#rt-rte-batch-sync"
          note: "The log is not a conversation transcript or full prompt/tool trace; folder-count events establish this source locally."
        -
          scope: "Potential client-experience, cache/replay, sync and evaluator trace-fed updates"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "memory.md#mem-obj-raw"
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-rte-answer-reuse"
            -
              "memory.md#mem-obj-sync-state"
            -
              "memory.md#mem-obj-evaluation-results"
          note: "Remember accepts self-contained text, not an exposed transcript extractor; model reply reuse and connector wrappers do not disclose all original qualifying trace content. No session-log, tool-trace or trajectory value is inferred from API names."
        -
          scope: "Custom Steps and injected cache paths"
          assessment: "not-determinable"
          findings: []
          records:
            -
              "runtime.md#rt-rte-source-filing"
            -
              "memory.md#mem-obj-answer-cache"
          note: "Original input to any qualifying alternative update is not recorded."
      records:
        -
          "memory.md#mem-obj-log"
        -
          "runtime.md#rt-rte-batch-sync"
        -
          "memory.md#mem-obj-raw"
        -
          "runtime.md#rt-rte-source-filing"
        -
          "memory.md#mem-rte-answer-reuse"
        -
          "memory.md#mem-obj-sync-state"
        -
          "memory.md#mem-obj-evaluation-results"
        -
          "memory.md#mem-obj-answer-cache"
      note: "The supported event-stream source belongs only to the split-history update. Opaque or unresolved learning alternatives are retained, not made inapplicable by one known route."
---

# LLM Wiki v2 memory profile

## Comparison rationale

This profile classifies accepted records, not new source evidence. Reconciliation establishes no whole-record supersessions. The source/candidate containers remain distinct from retained raw and note parts; classification uses the latter wherever their consumption differs. The unresolved check-result part separation prevents a complete evaluator-level classification. It does not negate the separately recorded retention and offline consumption in [MEM-OBJ-evaluation-results](memory.md#mem-obj-evaluation-results).

**Storage is not model architecture.** Notes, indexes and provenance are file-backed; the classifier response cache is SQLite. Calling a distributed-parametric classifier does not make its retained scalar answers parametric memory. Neither file retention nor imported-source lineage establishes truth warrant. The readable answer display carries title, summary and main body, not every field or linked target: [MEM-OBJ-note-body](memory.md#mem-obj-note-body), [MEM-OBJ-note-metadata](memory.md#mem-obj-note-metadata), [MEM-OBJ-answer-cache](memory.md#mem-obj-answer-cache).

**Admission is not authorship.** Default model/software transformation is automatic even when a human starts ingest. Caller-provided edits, proposal origins and confirmation flags do not establish human content approval. The profile therefore retains those mechanisms as unresolved rather than inventing a manual witness: [RT-RTE-source-filing](runtime.md#rt-rte-source-filing), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [MEM-OBJ-proposals](memory.md#mem-obj-proposals).

**Authority follows the actual consumer.** Prose supplies knowledge to later writing and answering. Summaries/descriptions influence ranking and routing; fields, hashes and queue status can supply validation and enforced vetoes. These do not give arbitrary instructions embedded in notes standing authority. Automatic archive replacement withdraws ordinary active reliance while retaining a historical read route. Purge instead deletes referenced lineage and refiles other sources; source-removal marking leaves derived notes usable. Those distinctions prevent a blanket invalidation classification: [MEM-BAP-retained-knowledge](memory.md#mem-bap-retained-knowledge), [MEM-OBJ-archive](memory.md#mem-obj-archive), [EPI-RTE-origin-purge](epistemic.md#epi-rte-origin-purge), [MEM-OBJ-raw](memory.md#mem-obj-raw).

**Read-back chains contain different operations.** Asking a question, requesting a note or requesting a model response is pull. Automatic supply of retained context to internal filing consumers and folder-specific prior-attempt state to splitting is push. The folder identity match is a targeted signal because it actually selects the supplied count; a note path on a requested read alone is not a push signal. This distinction does not establish proactive injection into an enclosing client: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [MEM-RTE-note-read](memory.md#mem-rte-note-read), [MEM-RTE-answer-reuse](memory.md#mem-rte-answer-reuse), [MEM-OBJ-log](memory.md#mem-obj-log).

**The trace-learning positive is deliberately local.** Split attempts feed an automatically retained control artifact, and later splitting consumes it to change retry behavior. The original input is operational events, not session logs. This supports wired trace learning and learning authority at that update path, not empirical improvement. Memoized model results and sync checkpoints are recorded automatic control updates, but the records do not settle every qualifying behavior-shaping update and original input there. Client-written durable experiences also leave extraction control unresolved. These branches remain separate unknowns, not negative findings: [MEM-OBJ-log](memory.md#mem-obj-log), [RT-RTE-batch-sync](runtime.md#rt-rte-batch-sync), [MEM-RTE-answer-reuse](memory.md#mem-rte-answer-reuse), [MEM-OBJ-sync-state](memory.md#mem-obj-sync-state), [MEM-OBJ-raw](memory.md#mem-obj-raw).

All positive findings are implementation-level wiring. No finding is promoted to observed operation or causal benefit. Incomplete custom implementation, caller provenance and evaluator coverage keep the relevant inventories partial. No bounded-absence record is declared in the supplied members, so the profile supplies neither a local trace-learning negative nor a system-wide negative.

Source-read log: none. This mapping used only the supplied accepted members and governing contracts; no frozen-source ambiguity required a source reread.
