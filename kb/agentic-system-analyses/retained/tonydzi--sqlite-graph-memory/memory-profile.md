---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "sqlite-graph-memory memory comparison across retained Markdown, derived index, transcript ledger, checkpoints and evaluation history."
run-id: "AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01"
source-identity: "https://github.com/tonydzi/sqlite-graph-memory"
reviewed-boundary: "f05db2778159d50a0ad8a35be4f2be3a6aea94b1"
memory-comparison:
  version: 2
  scope: "Retained source Markdown and live link fields, derived snippet/vector index and freshness manifest, Stop-hook ledger and per-session checkpoint, A/B telemetry and retained evaluation references/results, with their admission, maintenance and later consumers. Excludes external model weights and provider internals, private vault/pipeline, enclosing host conversation management and adoption, static shipped maintenance/contributor instructions, invocation-local query/candidate/PPR state, temporary answer files and setup-time benchmark raw-note copies. External note origin and supplied-reference control remain included unknowns, not excluded alternatives."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Source notes and their persistent link structure"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
              note: "Markdown files retain prose, frontmatter and link targets."
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "runtime.md#rt-rte-recall-options"
              note: "Retained wikilinks and replacement references supply graph structure read from current notes; no persisted SQL graph is implied."
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-recall-options"
          note: "Source files and live link inputs are covered; private temporal-edge implementations are excluded."
        -
          scope: "Persisted index vectors"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-e5"
              note: "NumPy matrix is retained on disk."
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-e5"
              note: "Chunk embeddings form the retained numerical similarity index."
          records:
            - "memory.md#mem-obj-brain-e5"
            - "runtime.md#rt-rte-index-admission"
          note: "Vectors are output representations, not model weights."
        -
          scope: "Snippet/access metadata and refresh manifest"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-meta"
                - "memory.md#mem-obj-brain-manifest"
              note: "Pickled snippet metadata and JSON freshness manifest are separate retained files."
          records:
            - "memory.md#mem-obj-brain-meta"
            - "memory.md#mem-obj-brain-manifest"
          note: "Encoding and substrate are distinguished; pickle and JSON are not separate substrates."
        -
          scope: "Transcript ledger and A/B telemetry"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
                - "memory.md#mem-obj-ab-recall"
              note: "The turns and ab_recall tables retain derived text and telemetry."
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ab-recall"
              note: "Optional A/B JSON retains ranked comparisons separately."
          records:
            - "memory.md#mem-obj-turns"
            - "memory.md#mem-obj-ab-recall"
          note: "Different configured database paths are possible; one shared database is not assumed."
        -
          scope: "Hook offset"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turnstate-offset"
              note: "Session-specific temporary offset file is retained between hook calls."
          records:
            - "memory.md#mem-obj-turnstate-offset"
          note: "Ephemeral lifetime does not remove its later selector role."
        -
          scope: "Evaluation history"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
              note: "Gold/score JSONL and benchmark JSON retain questions, answers and metrics."
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
              note: "Optional gold_eval SQL retains evaluation history."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
          note: "Invocation-local evaluator state and raw-note RAM copies are excluded from accumulated storage."
      records:
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-recall-options"
        - "memory.md#mem-obj-brain-e5"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-brain-meta"
        - "memory.md#mem-obj-brain-manifest"
        - "memory.md#mem-obj-turns"
        - "memory.md#mem-obj-ab-recall"
        - "memory.md#mem-obj-turnstate-offset"
        - "epistemic.md#epi-obj-evaluation-records"
      note: "Covers retained note/index, ledger, offset, telemetry and evaluation parts. External weights, static shipped instructions, per-query candidates, temporary answer files and setup-time raw maps are not usage-accumulated memory."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Source and indexed prose delivered as context"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-brain-meta"
                - "runtime.md#rt-bap-context-delivery"
              note: "Notes and snippet text supply human/model-interpreted content."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-brain-meta"
            - "runtime.md#rt-bap-context-delivery"
          note: "Body text is distinct from access fields."
        -
          scope: "Retained graph and index access/control fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-brain-meta"
                - "memory.md#mem-obj-brain-manifest"
                - "memory.md#mem-obj-turnstate-offset"
              note: "Link targets, paths, dates, freshness fingerprints and offsets have fixed code consumers."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-brain-meta"
            - "memory.md#mem-obj-brain-manifest"
            - "memory.md#mem-obj-turnstate-offset"
          note: "These localized fields select access, reuse and transcript input windows."
        -
          scope: "Stored dense chunk representations"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-e5"
              note: "Numerical representations are consumed through matrix scoring, not readable propositions."
          records:
            - "memory.md#mem-obj-brain-e5"
          note: "Classifies output embeddings, not the external encoder's weights."
        -
          scope: "Ledger prose and structured event fields"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
              note: "Ask, assistant summary and decision strings reach operator display."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
              note: "Session, tool/file/command lists and evidence pointers have structured parse/display consumers."
          records:
            - "memory.md#mem-obj-turns"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Parts are separated by consumption path, not by SQLite encoding."
        -
          scope: "Telemetry and evaluation retained parts"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ab-recall"
                - "epistemic.md#epi-obj-evaluation-records"
              note: "Query, answer, quote and snippet text retain interpretable content."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ab-recall"
                - "epistemic.md#epi-obj-evaluation-records"
              note: "Ranks, scores, counters, references, hashes and run metadata feed fixed reporting/checking rules."
          records:
            - "memory.md#mem-obj-ab-recall"
            - "epistemic.md#epi-obj-evaluation-records"
          note: "No inferred propositions are assigned to numerical scores."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-brain-meta"
        - "runtime.md#rt-bap-context-delivery"
        - "memory.md#mem-obj-brain-manifest"
        - "memory.md#mem-obj-turnstate-offset"
        - "memory.md#mem-obj-brain-e5"
        - "memory.md#mem-obj-turns"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-ab-recall"
        - "epistemic.md#epi-obj-evaluation-records"
      note: "All inventoried operative parts have recorded representation and consumer paths."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Original note authorship and origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
          note: "Initial authorship, trace provenance and human approval are unresolved; importing the corpus does not settle them."
        -
          scope: "Note text entering the index"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-brain-meta"
              note: "Caller-selected external Markdown supplies index content."
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-meta"
          note: "Acquisition origin is known even though earlier note provenance is not."
        -
          scope: "Derived snippet, vector and manifest production"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-brain-meta"
                - "memory.md#mem-obj-brain-e5"
                - "memory.md#mem-obj-brain-manifest"
              note: "Fixed parsing/chunking, embedding inference and filesystem fingerprints produce index artifacts."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-meta"
            - "memory.md#mem-obj-brain-e5"
            - "memory.md#mem-obj-brain-manifest"
          note: "Default and injected encoders are supported; this classifies the derivation path, not the injected encoder's provenance."
        -
          scope: "Injected encoder provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-brain-e5"
            - "runtime.md#rt-rte-index-admission"
          note: "The caller may supply an encoder; accepted records do not identify its internal derivation or training history."
        -
          scope: "Transcript ledger and checkpoint"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
                - "memory.md#mem-obj-turnstate-offset"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Hook extracts/clips host transcript content and advances the consumed byte boundary."
          records:
            - "memory.md#mem-obj-turns"
            - "memory.md#mem-obj-turnstate-offset"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Original host transcript content is distinct from its derived ledger."
        -
          scope: "A/B and evaluation generated artifacts"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ab-recall"
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
              note: "Computed rankings, extracted answers, generated labels and metric arithmetic produce retained comparison artifacts."
          records:
            - "memory.md#mem-obj-ab-recall"
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Does not establish authenticated execution of supplied result files."
        -
          scope: "Caller-supplied evaluation references"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
              note: "Scorers consume supplied reference sets/questions as inputs."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Original reference authoring and warrant are not settled by the import path."
      records:
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-brain-meta"
        - "memory.md#mem-obj-brain-e5"
        - "memory.md#mem-obj-brain-manifest"
        - "memory.md#mem-obj-turns"
        - "memory.md#mem-obj-turnstate-offset"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-ab-recall"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-evaluation-paths"
      note: "Known import and compilation paths coexist with unresolved initial notes and injected-encoder provenance."
    behavioral_authority:
      assessment: "known"
      units:
        -
          scope: "Returned note snippets at the MCP host"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-meta"
                - "runtime.md#rt-bap-context-delivery"
                - "runtime.md#rt-rte-mcp-recall"
              note: "Snippets reach the requesting agent as advisory context/evidence, not enforced standing directions."
          records:
            - "memory.md#mem-obj-brain-meta"
            - "runtime.md#rt-bap-context-delivery"
            - "runtime.md#rt-rte-mcp-recall"
          note: "Wiring establishes delivery; host activation/compliance is unobserved."
        -
          scope: "Retained ranking inputs at retrieval consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-e5"
                - "memory.md#mem-obj-brain-meta"
                - "memory.md#mem-obj-notes"
                - "runtime.md#rt-rte-recall-options"
              note: "Vectors, optional cross-encoder snippet/title pairs and live links influence membership and relative order."
          records:
            - "memory.md#mem-obj-brain-e5"
            - "memory.md#mem-obj-brain-meta"
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-recall-options"
          note: "Fixed algorithms give retained content ranking force without learning a ranking policy."
        -
          scope: "Refresh manifest and hook checkpoint at code selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-manifest"
                - "memory.md#mem-obj-turnstate-offset"
                - "runtime.md#rt-rte-index-admission"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Manifest selects reuse/regeneration; offset selects the next transcript slice."
          records:
            - "memory.md#mem-obj-brain-manifest"
            - "memory.md#mem-obj-turnstate-offset"
            - "runtime.md#rt-rte-index-admission"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Maintenance control is distinct from knowledge delivery."
        -
          scope: "Ledger at operator viewer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Selected ledger text supplies operational history to a person."
          records:
            - "memory.md#mem-obj-turns"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Decision-looking text is information, not proven adopted guidance."
        -
          scope: "Telemetry at external inspection"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-ab-recall"
                - "runtime.md#rt-rte-recall-options"
              note: "Comparison artifacts afford operator inspection, without an inspected automatic feedback consumer."
          records:
            - "memory.md#mem-obj-ab-recall"
            - "runtime.md#rt-rte-recall-options"
          note: "No dashboard or selector-policy update is wired by these records."
        -
          scope: "Evaluation references at scorers and result gates"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
                - "epistemic.md#epi-rte-bench-score"
                - "epistemic.md#epi-rte-bench-gate"
              note: "Retained gold/reference and hash criteria determine metric/check conformance."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "epistemic.md#epi-rte-bench-gate"
              note: "Reference/hash mismatches cause rejection status consumed by configured CI continuation."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
            - "epistemic.md#epi-rte-bench-score"
            - "epistemic.md#epi-rte-bench-gate"
          note: "Force is benchmark/reporting-local, not validation of source-note truth or repository-wide merge enforcement."
        -
          scope: "Evaluation history at later maintainer decisions"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
              note: "Persisted results afford later comparison and review."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Actual maintainer adoption or deployed successor behavior remains uninspected."
      records:
        - "memory.md#mem-obj-brain-meta"
        - "runtime.md#rt-bap-context-delivery"
        - "runtime.md#rt-rte-mcp-recall"
        - "memory.md#mem-obj-brain-e5"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-recall-options"
        - "memory.md#mem-obj-brain-manifest"
        - "memory.md#mem-obj-turnstate-offset"
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-turns"
        - "memory.md#mem-obj-ab-recall"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-evaluation-paths"
        - "epistemic.md#epi-rte-bench-score"
        - "epistemic.md#epi-rte-bench-gate"
      note: "Classifies actual or afforded retained-content consumers. Static portable temporal rules are excluded as non-accumulated instructions; their publication does not give retrieved note text instruction authority."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Original source-note admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
          note: "Generic note authors/callers do not establish an explicit human per-content decision or software-only admission."
        -
          scope: "Index entry admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
              note: "Software filters, chunks and embeds without per-note operator approval."
          records:
            - "runtime.md#rt-rte-index-admission"
          note: "Starting indexing is not manual content admission."
        -
          scope: "Hook ledger and offset writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-turnstate-capture"
                - "memory.md#mem-obj-turns"
                - "memory.md#mem-obj-turnstate-offset"
              note: "Parser and SQL/offset writers admit derived material without per-row approval."
          records:
            - "runtime.md#rt-rte-turnstate-capture"
            - "memory.md#mem-obj-turns"
            - "memory.md#mem-obj-turnstate-offset"
          note: "Host registration is upstream workflow control, not a human decision on each row."
        -
          scope: "A/B telemetry admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ab-recall"
                - "runtime.md#rt-rte-recall-options"
              note: "Code appends query-comparison artifacts without human per-query approval."
          records:
            - "memory.md#mem-obj-ab-recall"
            - "runtime.md#rt-rte-recall-options"
          note: "Swallowed write errors limit reliability, not agency."
        -
          scope: "Generated evaluation history admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
              note: "Evaluator software persists computed outputs; mutant mode withholds history."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Calling an evaluator does not make its result writes manual."
        -
          scope: "Supplied evaluation-reference authoring"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Reference sets are caller-supplied; records do not establish the per-content human/software admission mechanism."
      records:
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-turns"
        - "memory.md#mem-obj-turnstate-offset"
        - "memory.md#mem-obj-ab-recall"
        - "runtime.md#rt-rte-recall-options"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-evaluation-paths"
      note: "Automatic known transformations do not resolve external content and reference initialization control."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Transcript-derived ledger extraction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Selected asks, concatenated/clipped assistant text and structured activity fields reduce a retained transcript into an operational record."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turns"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Unique decisions and tool/file lists remove repeated captured items."
          records:
            - "memory.md#mem-obj-turns"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Clipping/selection preserves fragments of existing claims, not synthesis or learned improvement."
        -
          scope: "Index snippet reduction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-brain-meta"
              note: "Chunk-prefix clipping produces reduced retained representations of supplied note text."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-meta"
          note: "An index rebuild alone is not curation; the supporting transformation is retained text reduction."
        -
          scope: "Changed index entries"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-brain-meta"
                - "memory.md#mem-obj-brain-e5"
              note: "Refresh replaces rows for changed files with newly derived snippets/vectors."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-meta"
            - "memory.md#mem-obj-brain-e5"
          note: "Current entries change, but no versioned withdrawal history or epistemic invalidation is established."
        -
          scope: "External note maintenance behavior"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-bap-temporal-instructions"
          note: "Closing/replacing with reasons is prescribed to an external writer, but records do not establish how accumulated source notes were actually curated."
      records:
        - "memory.md#mem-obj-turns"
        - "runtime.md#rt-rte-turnstate-capture"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-brain-meta"
        - "memory.md#mem-obj-brain-e5"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-bap-temporal-instructions"
      note: "Implemented reductions, duplicate removal and entry revision are classified locally. Portable temporal doctrine is not an implemented invalidation route; unresolved source-note maintenance prevents complete coverage."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Note/index recall and evaluation requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-recall"
                - "runtime.md#rt-rte-recall-options"
                - "runtime.md#rt-rte-evaluation-paths"
              note: "Host or evaluator explicitly requests retained note material; internal selection/return fulfills that request."
          records:
            - "runtime.md#rt-rte-mcp-recall"
            - "runtime.md#rt-rte-recall-options"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Graph expansion and optional reranking inside a request are not independent push."
        -
          scope: "Requested ledger inspection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-turnstate-capture"
                - "memory.md#mem-obj-turns"
              note: "Operator viewer requests session/recency-selected retained rows."
          records:
            - "runtime.md#rt-rte-turnstate-capture"
            - "memory.md#mem-obj-turns"
          note: "No automatic injection into model context is established."
        -
          scope: "Automatic refresh-control consumption"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-brain-manifest"
              note: "Indexer automatically reloads retained manifest/settings and applies them without a separate consumer request for that material."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-manifest"
          note: "Trigger is index build; code supplies prior freshness metadata to its reuse/regeneration selector."
        -
          scope: "Automatic checkpoint consumption"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-turnstate-capture"
                - "memory.md#mem-obj-turnstate-offset"
              note: "On Stop, hook automatically reads the session checkpoint to choose its transcript slice."
          records:
            - "runtime.md#rt-rte-turnstate-capture"
            - "memory.md#mem-obj-turnstate-offset"
          note: "Host event triggers work; checkpoint supply is not a requested ledger return."
        -
          scope: "Evaluation reference/history and telemetry inspection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-evaluation-records"
                - "runtime.md#rt-rte-evaluation-paths"
                - "memory.md#mem-obj-ab-recall"
              note: "Explicit evaluation/validation and inspection consume retained references/results; telemetry inspection is afforded rather than a wired dashboard."
          records:
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
            - "memory.md#mem-obj-ab-recall"
          note: "No autonomous feedback loop is inferred from persisted scores."
      records:
        - "runtime.md#rt-rte-mcp-recall"
        - "runtime.md#rt-rte-recall-options"
        - "runtime.md#rt-rte-evaluation-paths"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-turns"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-brain-manifest"
        - "memory.md#mem-obj-turnstate-offset"
        - "epistemic.md#epi-obj-evaluation-records"
        - "memory.md#mem-obj-ab-recall"
      note: "Separates requested content retrieval from automatic supply of retained control metadata. Static instruction installation is not usage-accumulated read-back."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "Indexer manifest push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-manifest"
                - "runtime.md#rt-rte-index-admission"
              note: "At index-build trigger, current file paths/settings identify retained manifest entries used to choose reuse versus regeneration."
          records:
            - "memory.md#mem-obj-brain-manifest"
            - "runtime.md#rt-rte-index-admission"
          note: "Actual matching selects consumed prior metadata, not simply a name printed in a catalog."
        -
          scope: "Hook checkpoint push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-turnstate-offset"
                - "runtime.md#rt-rte-turnstate-capture"
              note: "Stop event session ID selects the corresponding retained offset file, whose integer selects the subsequent transcript window."
          records:
            - "memory.md#mem-obj-turnstate-offset"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Session identity selects control metadata; it is not semantic recall."
        -
          scope: "Requested note, ledger and evaluator content"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-recall"
            - "runtime.md#rt-rte-turnstate-capture"
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-evaluation-paths"
            - "memory.md#mem-obj-ab-recall"
          note: "Push-signal classification does not apply to material delivered only in response to a request; query embeddings and session filters on those pull operations are not push signals."
      records:
        - "memory.md#mem-obj-brain-manifest"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-turnstate-offset"
        - "runtime.md#rt-rte-turnstate-capture"
        - "runtime.md#rt-rte-mcp-recall"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-evaluation-paths"
        - "memory.md#mem-obj-ab-recall"
      note: "Identifier classification is limited to automatic manifest/checkpoint supply; retrieval similarity and lexical extraction are not relabelled as push selection."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Transcript-derived ledger and later viewer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-turns"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Automatic trace-fed rows are retained and displayed, but no later behavior-shaping artifact/update consumer is established. No canonical evidenced-absence record warrants a local no."
        -
          scope: "Transcript checkpoint and later hook"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-turnstate-offset"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Offset is routine input-window control, not an established durable behavior-shaping artifact from experience. Accepted records provide no bounded-absence declaration supporting no."
        -
          scope: "Note-derived index"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-brain-e5"
            - "memory.md#mem-obj-brain-meta"
          note: "Automatic indexing is known, but original note trace provenance is unresolved; no qualifying automatic trace-to-durable-behavior chain or bounded absence is established."
        -
          scope: "A/B and evaluation feedback"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-ab-recall"
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-recall-options"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Retained comparisons/measurements have reporting consumers, not an established automatic update to durable behavior; actual maintainer adoption is uninspected. No absence record supports no."
      records:
        - "memory.md#mem-obj-turns"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-turnstate-offset"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-brain-e5"
        - "memory.md#mem-obj-brain-meta"
        - "memory.md#mem-obj-ab-recall"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-recall-options"
        - "runtime.md#rt-rte-evaluation-paths"
      note: "No supported controlled yes or no follows from accepted records. Raw trace retention, curation, routing and measurement remain independent of qualifying trace learning."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Ledger/checkpoint candidate learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-turns"
            - "memory.md#mem-obj-turnstate-offset"
            - "runtime.md#rt-rte-turnstate-capture"
          note: "Session text and attempted tool-use inputs are recorded, but a qualifying learning write/later behavior-shaping consumer is not established; raw trace origin alone cannot classify this axis."
        -
          scope: "Index candidate learning route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-index-admission"
          note: "Original notes may have opaque provenance and no qualifying trace-fed learning chain is established."
        -
          scope: "Telemetry/evaluation candidate learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-ab-recall"
            - "epistemic.md#epi-obj-evaluation-records"
            - "runtime.md#rt-rte-recall-options"
            - "runtime.md#rt-rte-evaluation-paths"
          note: "Queries/rankings/metrics do not establish original inputs to a qualifying learning update; later adaptation remains unresolved."
      records:
        - "memory.md#mem-obj-turns"
        - "memory.md#mem-obj-turnstate-offset"
        - "runtime.md#rt-rte-turnstate-capture"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-ab-recall"
        - "epistemic.md#epi-obj-evaluation-records"
        - "runtime.md#rt-rte-recall-options"
        - "runtime.md#rt-rte-evaluation-paths"
      note: "Not inapplicable: accepted records do not establish a completely assessed bounded absence of qualifying trace learning."
---

# sqlite-graph-memory memory profile

## Comparison rationale

This profile classifies accepted records, not target execution. Wired findings
describe implemented paths; afforded inspection describes an available consumer
role, not a deployed dashboard or an observed maintainer decision. No finding
claims observed activation, improved capability or causal benefit.

### Retained boundary and representation

The package name does not make its note index a SQLite graph. Source Markdown
retains links; NumPy vectors and pickled snippets are separate files, while
SQLite holds transcript and comparison records. Graph and vector findings name
access structures over retained material, not SQL schema claims
([MEM-OBJ-notes](memory.md#mem-obj-notes),
[MEM-OBJ-brain-e5](memory.md#mem-obj-brain-e5),
[MEM-OBJ-brain-meta](memory.md#mem-obj-brain-meta),
[MEM-OBJ-turns](memory.md#mem-obj-turns),
[MEM-OBJ-ab-recall](memory.md#mem-obj-ab-recall)).

The numerical index is parametric representation, not updated encoder weights.
Natural-language snippets and symbolic path/date fields have separate consumer
paths even though one pickle holds both. In-memory candidates, PPR cache and
the benchmark raw-note map are working copies or invocation state, not another
accumulated store. The benchmark can nevertheless consume retained source-note
text beyond the snippet prefix
([MEM-OBJ-brain-e5](memory.md#mem-obj-brain-e5),
[MEM-OBJ-brain-meta](memory.md#mem-obj-brain-meta),
[MEM-OBJ-benchmark-raw](memory.md#mem-obj-benchmark-raw),
[RT-RTE-recall-options](runtime.md#rt-rte-recall-options)).

### Admission, lineage and transformations

External note origin stays unresolved beside known import and automatic
index derivation. A caller starting indexing does not supply a per-note human
approval decision. Similarly, evaluator reference inputs do not reveal their
original admission control. No manual finding is licensed merely by operator
installation or a CLI trigger
([MEM-OBJ-notes](memory.md#mem-obj-notes),
[RT-RTE-index-admission](runtime.md#rt-rte-index-admission),
[EPI-OBJ-evaluation-records](epistemic.md#epi-obj-evaluation-records)).

Consolidation identifies reduction of retained text: transcript extraction and
snippet clipping. Duplicate removal in captured lists supplies a separate
deduplication finding. Changed-file refresh revises existing index entries;
it does not preserve withdrawal history, certify a corrected claim or synthesize
new knowledge. Temporal closing and reason retention remain external-writer
prescriptions, not an implemented package invalidation operation
([MEM-OBJ-turns](memory.md#mem-obj-turns),
[RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture),
[RT-RTE-index-admission](runtime.md#rt-rte-index-admission),
[RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions),
[RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope)).

### Consumer force and read-back

Snippet delivery supplies knowledge context, while retained vectors, text and
links supply ranking inputs. Manifest and offset metadata route subsequent
maintenance work. They do not become instructions merely because they affect
behavior. Stored evaluation references and hashes supply validation criteria;
the configured result gate can enforce rejection locally. These forces do not
validate note truth or establish system-wide merge enforcement
([RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery),
[MEM-OBJ-brain-manifest](memory.md#mem-obj-brain-manifest),
[MEM-OBJ-turnstate-offset](memory.md#mem-obj-turnstate-offset),
[EPI-RTE-bench-score](epistemic.md#epi-rte-bench-score),
[EPI-RTE-bench-gate](epistemic.md#epi-rte-bench-gate)).

Requested recall remains pull throughout candidate selection and delivery.
Graph expansion is not an unsolicited context injection. Automatic control
metadata supply is different: index-build code matches prior manifest entries
by path/settings, and Stop-hook code selects a session-specific offset. These
identifier push findings concern control metadata, not semantic targeting of
delivered note snippets. Pull-route query embeddings, ledger recency and lexical
benchmark extraction do not supply additional push-signal values
([RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall),
[RT-RTE-index-admission](runtime.md#rt-rte-index-admission),
[MEM-OBJ-brain-manifest](memory.md#mem-obj-brain-manifest),
[RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture),
[MEM-OBJ-turnstate-offset](memory.md#mem-obj-turnstate-offset),
[EPI-RTE-extract-answer](epistemic.md#epi-rte-extract-answer)).

### Trace-learning limits and canonical identity

Automatic transcript extraction reaches a ledger viewer, not an established
later behavior-shaping artifact consumer. Offsets select a future input window
but are routine checkpoints; telemetry and evaluator history do not establish
automatic policy adaptation. Original note trace origin remains unresolved.
The accepted records contain no canonical evidenced-absence declaration
warranting a local trace-learning "no". Therefore neither "yes" nor "no" is
asserted, and trace source remains not-determinable rather than inapplicable.
This preserves the distinction between trace-extracted lineage and a qualifying
trace-learning route
([MEM-OBJ-turns](memory.md#mem-obj-turns),
[MEM-OBJ-turnstate-offset](memory.md#mem-obj-turnstate-offset),
[MEM-OBJ-notes](memory.md#mem-obj-notes),
[MEM-OBJ-ab-recall](memory.md#mem-obj-ab-recall),
[EPI-OBJ-evaluation-records](epistemic.md#epi-obj-evaluation-records),
[RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)).

Reconciliation supersedes the epistemic turns declaration with
[MEM-OBJ-turns](memory.md#mem-obj-turns), so ledger findings cite that canonical
object. It also supersedes the epistemic diagnostic route with
[MEM-RTE-vault-health](memory.md#mem-rte-vault-health); those diagnostics do not
retain a report history or automatically curate memory and add no profile
operation. Neither supersession changes a controlled value. The broader
epistemic note/snippet and recall-state containers remain valid overlaps, not
aliases of one memory object.

No frozen-source read was needed or performed for this classification. All
warrants remain in the accepted record citations; no new records, quotations,
execution evidence or amendments are introduced.
