---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "MemexOS memory comparison: retained sources, wiki, classification, repair, retrieval access structures and evaluation state at the frozen revision."
run-id: "AAS-2026-11-07-memexos-5cd34a715eb7-01"
source-identity: "https://github.com/liushengyu/memexos"
reviewed-boundary: "bb9e9b2ac0adbca87d13a9f7600867128b5f71b9"
memory-comparison:
  version: 2
  scope: "Retained and use-modified raw sources, session snapshots, feedback, attachments, staged/held and published wiki/inbox content, catalog/taxonomy revisions, processing ledgers, review/usage state, timing controls, FTS/qmd access structures and evaluation references/results with their later consumers. Includes incompletely inspected media state, taxonomy lifecycle, inbox research and evaluation provenance. Excludes static shipped instructions/configuration/fixtures as such, invocation-local messages without later consumption, external model parameters and ordinary consuming agents' own reasoning. External CLI context-management alternatives remain unresolved rather than classified from display summaries."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Retained raw text, attachments, session snapshots, feedback, wiki, inbox, catalog, taxonomy and processing ledgers"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-session-snapshots"
                - "memory.md#mem-obj-feedback"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-catalog"
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-obj-assets"
              note: "These operative files are retained in the vault filesystem and Git; the stage organization is not an additional memory substrate."
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-session-snapshots"
                - "memory.md#mem-obj-feedback"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-catalog"
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-obj-assets"
              note: "These operative files are retained in the vault filesystem and Git; the stage organization is not an additional memory substrate."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-session-snapshots"
            - "memory.md#mem-obj-feedback"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-catalog"
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-obj-ledgers"
            - "memory.md#mem-obj-assets"
          note: "These operative files are retained in the vault filesystem and Git; the stage organization is not an additional memory substrate."
        -
          scope: "Local usage/review records, evaluation references/results and rerank timing state"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-rte-rerank-budget"
                - "epistemic.md#epi-obj-questions"
                - "epistemic.md#epi-obj-rank-results"
                - "epistemic.md#epi-obj-answer-judgments"
                - "epistemic.md#epi-obj-calibration-results"
                - "epistemic.md#epi-obj-cli-traces"
                - "epistemic.md#epi-obj-tool-metrics"
              note: "JSON/JSONL and timing files persist outside or alongside the published wiki."
          records:
            - "memory.md#mem-obj-usage"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-rte-rerank-budget"
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-obj-rank-results"
            - "epistemic.md#epi-obj-answer-judgments"
            - "epistemic.md#epi-obj-calibration-results"
            - "epistemic.md#epi-obj-cli-traces"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "JSON/JSONL and timing files persist outside or alongside the published wiki."
        -
          scope: "Built-in full-text access structure"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts"
              note: "FTS5 is an operative SQLite cache, not a vector representation."
          records:
            - "memory.md#mem-obj-fts"
          note: "FTS5 is an operative SQLite cache, not a vector representation."
        -
          scope: "qmd access structure and local configuration"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "The recorded named SQLite vector index and configuration are retained; unknown internal schema does not erase the established substrates."
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "The recorded named SQLite vector index and configuration are retained; unknown internal schema does not erase the established substrates."
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "The recorded named SQLite vector index and configuration are retained; unknown internal schema does not erase the established substrates."
          records:
            - "memory.md#mem-obj-vectors"
          note: "The recorded named SQLite vector index and configuration are retained; unknown internal schema does not erase the established substrates."
        -
          scope: "Included lower-level media and inbox research-cache retained parts"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Files for attachments are established, but lower-level numerical media state and complete research-cache storage were not inspected; no complete substrate union is warranted."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-obj-feedback"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-catalog"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-obj-usage"
        - "memory.md#mem-obj-review"
        - "memory.md#mem-rte-rerank-budget"
        - "epistemic.md#epi-obj-questions"
        - "epistemic.md#epi-obj-rank-results"
        - "epistemic.md#epi-obj-answer-judgments"
        - "epistemic.md#epi-obj-calibration-results"
        - "epistemic.md#epi-obj-cli-traces"
        - "epistemic.md#epi-obj-tool-metrics"
        - "memory.md#mem-obj-fts"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
      note: "Established file/Git, FTS and qmd substrates coexist with incompletely recorded lower-level retained parts."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Raw, snapshot, feedback and wiki prose consumed by compiler, maintenance and asking agents"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-session-snapshots"
                - "memory.md#mem-obj-feedback"
                - "memory.md#mem-obj-wiki"
              note: "Interpretation of claims, evidence and source pointers supplies content."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-session-snapshots"
            - "memory.md#mem-obj-feedback"
            - "memory.md#mem-obj-wiki"
          note: "Interpretation of claims, evidence and source pointers supplies content."
        -
          scope: "Catalog summaries, taxonomy definitions, inbox questions, review reasons and usage excerpts"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-catalog"
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-obj-usage"
              note: "These prose parts guide classifiers, writers and operators; their symbolic control fields are separate."
          records:
            - "memory.md#mem-obj-catalog"
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-obj-usage"
          note: "These prose parts guide classifiers, writers and operators; their symbolic control fields are separate."
        -
          scope: "Headers, page links, ledgers, catalog/category identities, queue/verdict fields, usage selectors and timing scalars"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-obj-catalog"
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-obj-usage"
                - "memory.md#mem-rte-rerank-budget"
              note: "Fixed code consumes localized keys, statuses and numerical scalars; a timing number is not distributed-parametric form."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-ledgers"
            - "memory.md#mem-obj-catalog"
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-obj-usage"
            - "memory.md#mem-rte-rerank-budget"
          note: "Fixed code consumes localized keys, statuses and numerical scalars; a timing number is not distributed-parametric form."
        -
          scope: "FTS tokens and qmd configuration/marker"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts"
                - "memory.md#mem-obj-vectors"
              note: "Access metadata and tokenization are fixed-rule parts, not the meaning of the retrieved page."
          records:
            - "memory.md#mem-obj-fts"
            - "memory.md#mem-obj-vectors"
          note: "Access metadata and tokenization are fixed-rule parts, not the meaning of the retrieved page."
        -
          scope: "qmd retained dense vectors"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "Distributed numerical text representations are separate from external model weights and readable snippets."
          records:
            - "memory.md#mem-obj-vectors"
          note: "Distributed numerical text representations are separate from external model weights and readable snippets."
        -
          scope: "Evaluation questions/reference prose and answer/calibration judgment prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-questions"
                - "epistemic.md#epi-obj-answer-judgments"
                - "epistemic.md#epi-obj-calibration-results"
              note: "These parts are interpreted as benchmark references or diagnostic judgments."
          records:
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-obj-answer-judgments"
            - "epistemic.md#epi-obj-calibration-results"
          note: "These parts are interpreted as benchmark references or diagnostic judgments."
        -
          scope: "Evaluation IDs, qrels, ranks, recorded calls, comparator flags and procedure metrics"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-questions"
                - "epistemic.md#epi-obj-rank-results"
                - "epistemic.md#epi-obj-calibration-results"
                - "epistemic.md#epi-obj-cli-traces"
                - "epistemic.md#epi-obj-tool-metrics"
              note: "Fixed selectors and arithmetic consume these parts."
          records:
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-obj-rank-results"
            - "epistemic.md#epi-obj-calibration-results"
            - "epistemic.md#epi-obj-cli-traces"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "Fixed selectors and arithmetic consume these parts."
        -
          scope: "Binary attachment interpretation, lower-level media state and full inbox research payload"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Readable text or display cannot establish the form of opaque consumed payloads."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-obj-feedback"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-catalog"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-review"
        - "memory.md#mem-obj-usage"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-rte-rerank-budget"
        - "memory.md#mem-obj-fts"
        - "memory.md#mem-obj-vectors"
        - "epistemic.md#epi-obj-questions"
        - "epistemic.md#epi-obj-answer-judgments"
        - "epistemic.md#epi-obj-calibration-results"
        - "epistemic.md#epi-obj-rank-results"
        - "epistemic.md#epi-obj-cli-traces"
        - "epistemic.md#epi-obj-tool-metrics"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
      note: "Mixed objects are split by operative consumption; opaque payloads prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Captured external source text and original attachments"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-assets"
              note: "Acquisition imports content; import does not authenticate its truth."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-assets"
          note: "Acquisition imports content; import does not authenticate its truth."
        -
          scope: "Model-selected session snapshots and conversation-derived feedback"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-snapshots"
                - "memory.md#mem-obj-feedback"
                - "memory.md#mem-rte-session-distillation"
              note: "Recorded session material is distilled, rather than replayed verbatim."
          records:
            - "memory.md#mem-obj-session-snapshots"
            - "memory.md#mem-obj-feedback"
            - "memory.md#mem-rte-session-distillation"
          note: "Recorded session material is distilled, rather than replayed verbatim."
        -
          scope: "Writer-produced wiki prose and review criticisms"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-review"
                - "runtime.md#rt-rte-compile-publish"
              note: "Model authorship is distinct from automatic admission; the actual semantic transformation of every output remains unresolved."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-review"
            - "runtime.md#rt-rte-compile-publish"
          note: "Model authorship is distinct from automatic admission; the actual semantic transformation of every output remains unresolved."
        -
          scope: "Usage feedback and repair problems"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage"
                - "memory.md#mem-rte-usage-repair"
              note: "Host-session activity feeds diagnostics retained for later repair."
          records:
            - "memory.md#mem-obj-usage"
            - "memory.md#mem-rte-usage-repair"
          note: "Host-session activity feeds diagnostics retained for later repair."
        -
          scope: "Catalog model labels/summaries and subsequent taxonomy proposals"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-catalog"
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-rte-catalog-reuse"
              note: "These are authored characterizations and proposals; initial shipped taxonomy is excluded from accumulated memory."
          records:
            - "memory.md#mem-obj-catalog"
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-rte-catalog-reuse"
          note: "These are authored characterizations and proposals; initial shipped taxonomy is excluded from accumulated memory."
        -
          scope: "Processing sets, FTS, embedding update output and timing estimates"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-obj-fts"
                - "memory.md#mem-obj-vectors"
                - "memory.md#mem-rte-rerank-budget"
              note: "Code derives state and access representations; per-vector provenance and immutable embedding identity remain unresolved."
          records:
            - "memory.md#mem-obj-ledgers"
            - "memory.md#mem-obj-fts"
            - "memory.md#mem-obj-vectors"
            - "memory.md#mem-rte-rerank-budget"
          note: "Code derives state and access representations; per-vector provenance and immutable embedding identity remain unresolved."
        -
          scope: "Evaluation metric and procedure artifacts"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rank-results"
                - "epistemic.md#epi-obj-calibration-results"
                - "epistemic.md#epi-obj-cli-traces"
                - "epistemic.md#epi-obj-tool-metrics"
              note: "Code records/computes these operative outputs from selected calls, references and judgments."
          records:
            - "epistemic.md#epi-obj-rank-results"
            - "epistemic.md#epi-obj-calibration-results"
            - "epistemic.md#epi-obj-cli-traces"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "Code records/computes these operative outputs from selected calls, references and judgments."
        -
          scope: "Retained answer judgments and bank verifier revisions"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-answer-judgments"
                - "epistemic.md#epi-obj-questions"
                - "epistemic.md#epi-rte-evaluation-bank"
              note: "Models author diagnostic judgments and admitted reference revisions."
          records:
            - "epistemic.md#epi-obj-answer-judgments"
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-rte-evaluation-bank"
          note: "Models author diagnostic judgments and admitted reference revisions."
        -
          scope: "Initial bank/qrel provenance, media transformation provenance and complete inbox research derivation"
          assessment: "uninspected"
          findings: []
          records:
            - "epistemic.md#epi-obj-questions"
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Generation/mining/pool provenance and lower-level transformations are uninspected; no initial-origin conclusion follows from subsequent known updates."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-assets"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-obj-feedback"
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-review"
        - "runtime.md#rt-rte-compile-publish"
        - "memory.md#mem-obj-usage"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-catalog"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-rte-catalog-reuse"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-obj-fts"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-rte-rerank-budget"
        - "epistemic.md#epi-obj-rank-results"
        - "epistemic.md#epi-obj-calibration-results"
        - "epistemic.md#epi-obj-cli-traces"
        - "epistemic.md#epi-obj-tool-metrics"
        - "epistemic.md#epi-obj-answer-judgments"
        - "epistemic.md#epi-obj-questions"
        - "epistemic.md#epi-rte-evaluation-bank"
        - "runtime.md#rt-rte-inbox-maintenance"
      note: "Known derivation paths do not resolve every initial object or opaque alternative."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Raw/snapshot/wiki content delivered to compiler, maintenance and asking agents"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-session-snapshots"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-search-get"
              note: "Content supplies evidence and context, not an enforced host answer policy."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-session-snapshots"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-search-get"
          note: "Content supplies evidence and context, not an enforced host answer policy."
        -
          scope: "Taxonomy definitions and catalog scope guidance delivered to classifiers and writers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-rte-catalog-reuse"
                - "memory.md#mem-obj-catalog"
              note: "Retained category definitions and scope guidance direct classification/use, independently of their correctness."
          records:
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-rte-catalog-reuse"
            - "memory.md#mem-obj-catalog"
          note: "Retained category definitions and scope guidance direct classification/use, independently of their correctness."
        -
          scope: "Retained wiki/raw text and qmd representations at retrieval scorers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts"
                - "memory.md#mem-obj-vectors"
                - "runtime.md#rt-rte-search-get"
              note: "Retained text/vectors affect relative retrieval priority; requested retrieval remains pull."
          records:
            - "memory.md#mem-obj-fts"
            - "memory.md#mem-obj-vectors"
            - "runtime.md#rt-rte-search-get"
          note: "Retained text/vectors affect relative retrieval priority; requested retrieval remains pull."
        -
          scope: "Processing sets and retained timing state at future batch/budget selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-rte-rerank-budget"
              note: "Path/status sets select eligible work; timing determines future rerank input size."
          records:
            - "memory.md#mem-obj-ledgers"
            - "memory.md#mem-rte-rerank-budget"
          note: "Path/status sets select eligible work; timing determines future rerank input size."
        -
          scope: "Held/processed sets at automatic work exclusion"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ledgers"
                - "runtime.md#rt-rte-compile-publish"
              note: "Held/processed paths are excluded from ordinary automatic work, a bounded software veto rather than a semantic truth guarantee."
          records:
            - "memory.md#mem-obj-ledgers"
            - "runtime.md#rt-rte-compile-publish"
          note: "Held/processed paths are excluded from ordinary automatic work, a bounded software veto rather than a semantic truth guarantee."
        -
          scope: "Retained review verdict fields at enabled gate disposition"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review"
                - "epistemic.md#epi-rte-review-decision"
              note: "Recorded criteria-bearing verdicts determine admissibility and can veto publication on enabled paths; off/no-change exceptions remain."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review"
                - "epistemic.md#epi-rte-review-decision"
              note: "Recorded criteria-bearing verdicts determine admissibility and can veto publication on enabled paths; off/no-change exceptions remain."
          records:
            - "memory.md#mem-obj-review"
            - "epistemic.md#epi-rte-review-decision"
          note: "Recorded criteria-bearing verdicts determine admissibility and can veto publication on enabled paths; off/no-change exceptions remain."
        -
          scope: "Retained session experience and usage feedback at automatic snapshot and repair producers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
                - "memory.md#mem-rte-usage-repair"
              note: "Experience feeds durable behavior-shaping text; the output separately supplies knowledge. This does not establish improved capacity."
          records:
            - "memory.md#mem-rte-session-distillation"
            - "memory.md#mem-rte-usage-repair"
          note: "Experience feeds durable behavior-shaping text; the output separately supplies knowledge. This does not establish improved capacity."
        -
          scope: "Stored review reasons delivered as corrective tasks to later fix writers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review"
                - "memory.md#mem-rte-usage-repair"
              note: "Rendered targeted problems request revisions, not merely report a status."
          records:
            - "memory.md#mem-obj-review"
            - "memory.md#mem-rte-usage-repair"
          note: "Rendered targeted problems request revisions, not merely report a status."
        -
          scope: "Retained evaluation bank fields at scoring/grading consumers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-questions"
                - "epistemic.md#epi-rte-evaluation-bank"
                - "epistemic.md#epi-rte-retrieval-scoring"
                - "epistemic.md#epi-rte-answer-grading"
              note: "References define benchmark conformity, not production truth endorsement."
          records:
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-rte-evaluation-bank"
            - "epistemic.md#epi-rte-retrieval-scoring"
            - "epistemic.md#epi-rte-answer-grading"
          note: "References define benchmark conformity, not production truth endorsement."
        -
          scope: "Evaluation reports, usage summaries and answer judgments at operators/lint"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage"
                - "epistemic.md#epi-obj-answer-judgments"
                - "epistemic.md#epi-obj-rank-results"
                - "epistemic.md#epi-obj-calibration-results"
                - "epistemic.md#epi-obj-tool-metrics"
              note: "Reports supply diagnostic context; no automatic production optimizer is established by evaluation reports."
          records:
            - "memory.md#mem-obj-usage"
            - "epistemic.md#epi-obj-answer-judgments"
            - "epistemic.md#epi-obj-rank-results"
            - "epistemic.md#epi-obj-calibration-results"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "Reports supply diagnostic context; no automatic production optimizer is established by evaluation reports."
        -
          scope: "Full taxonomy registry, inbox research consumption and binary/media payload consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Their complete consumer/effect paths are not established; delivered display text cannot resolve them."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-search-get"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-rte-catalog-reuse"
        - "memory.md#mem-obj-catalog"
        - "memory.md#mem-obj-fts"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-rte-rerank-budget"
        - "runtime.md#rt-rte-compile-publish"
        - "memory.md#mem-obj-review"
        - "epistemic.md#epi-rte-review-decision"
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-rte-usage-repair"
        - "epistemic.md#epi-obj-questions"
        - "epistemic.md#epi-rte-evaluation-bank"
        - "epistemic.md#epi-rte-retrieval-scoring"
        - "epistemic.md#epi-rte-answer-grading"
        - "memory.md#mem-obj-usage"
        - "epistemic.md#epi-obj-answer-judgments"
        - "epistemic.md#epi-obj-rank-results"
        - "epistemic.md#epi-obj-calibration-results"
        - "epistemic.md#epi-obj-tool-metrics"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
      note: "Authority is attached to actual consumers. Static shipped AGENTS/Policy are not classified as accumulated memory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Unattended session admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
              note: "The model chooses content and code admits scanned/normalized outputs without per-content human approval."
          records:
            - "memory.md#mem-rte-session-distillation"
          note: "The model chooses content and code admits scanned/normalized outputs without per-content human approval."
        -
          scope: "Manual session-snapshot procedure"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-session-distillation"
              note: "The separately documented manual procedure asks person agreement; this is an afforded alternative, not the unattended mechanism."
          records:
            - "memory.md#mem-rte-session-distillation"
          note: "The separately documented manual procedure asks person agreement; this is an afforded alternative, not the unattended mechanism."
        -
          scope: "Staged wiki writing, maintenance and metadata synchronization"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-publish"
                - "runtime.md#rt-rte-inbox-maintenance"
                - "epistemic.md#epi-rte-catalog-sync"
              note: "Model proposals and program checks admit changes without routine per-content human approval."
          records:
            - "runtime.md#rt-rte-compile-publish"
            - "runtime.md#rt-rte-inbox-maintenance"
            - "epistemic.md#epi-rte-catalog-sync"
          note: "Model proposals and program checks admit changes without routine per-content human approval."
        -
          scope: "Catalog rows/drafts, usage feedback/fix jobs, index updates and timing state"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-catalog-reuse"
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-fts"
                - "memory.md#mem-obj-vectors"
                - "memory.md#mem-rte-rerank-budget"
              note: "Software/model admission is not manual merely because an operator launched the command."
          records:
            - "memory.md#mem-rte-catalog-reuse"
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-obj-fts"
            - "memory.md#mem-obj-vectors"
            - "memory.md#mem-rte-rerank-budget"
          note: "Software/model admission is not manual merely because an operator launched the command."
        -
          scope: "Evaluation bank verification and recorded metric/judgment admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-evaluation-bank"
                - "epistemic.md#epi-obj-rank-results"
                - "epistemic.md#epi-obj-answer-judgments"
                - "epistemic.md#epi-obj-calibration-results"
                - "epistemic.md#epi-obj-cli-traces"
                - "epistemic.md#epi-obj-tool-metrics"
              note: "Model keep plus code conditions or deterministic persistence admit the relevant records."
          records:
            - "epistemic.md#epi-rte-evaluation-bank"
            - "epistemic.md#epi-obj-rank-results"
            - "epistemic.md#epi-obj-answer-judgments"
            - "epistemic.md#epi-obj-calibration-results"
            - "epistemic.md#epi-obj-cli-traces"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "Model keep plus code conditions or deterministic persistence admit the relevant records."
        -
          scope: "Caller-requested captures, category decisions and generic inbox-decision API"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-taxonomy"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Caller identity does not establish explicit human content approval; source-native person terminology is not authentication."
        -
          scope: "Lower-level media and full inbox research admission"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Admission mechanisms for these included alternatives remain incompletely inspected."
      records:
        - "memory.md#mem-rte-session-distillation"
        - "runtime.md#rt-rte-compile-publish"
        - "runtime.md#rt-rte-inbox-maintenance"
        - "epistemic.md#epi-rte-catalog-sync"
        - "memory.md#mem-rte-catalog-reuse"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-fts"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-rte-rerank-budget"
        - "epistemic.md#epi-rte-evaluation-bank"
        - "epistemic.md#epi-obj-rank-results"
        - "epistemic.md#epi-obj-answer-judgments"
        - "epistemic.md#epi-obj-calibration-results"
        - "epistemic.md#epi-obj-cli-traces"
        - "epistemic.md#epi-obj-tool-metrics"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-obj-assets"
      note: "Automatic mechanisms and an afforded manual procedure are supported; generic caller control and lower-level alternatives remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Session-to-standing-snapshot distillation"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
                - "memory.md#mem-obj-session-snapshots"
              note: "Retained session messages are selected/compressed into reusable conclusions; unchanged raw logs need not be deleted."
          records:
            - "memory.md#mem-rte-session-distillation"
            - "memory.md#mem-obj-session-snapshots"
          note: "Retained session messages are selected/compressed into reusable conclusions; unchanged raw logs need not be deleted."
        -
          scope: "Repair and reclassification of existing entries"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-rte-catalog-reuse"
                - "epistemic.md#epi-rte-catalog-sync"
              note: "Fix revises retained wiki and append/latest-row or sync changes effective classifications."
          records:
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-rte-catalog-reuse"
            - "epistemic.md#epi-rte-catalog-sync"
          note: "Fix revises retained wiki and append/latest-row or sync changes effective classifications."
        -
          scope: "Aging top-level inbox reports and idle taxonomy drafts"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-rte-catalog-reuse"
              note: "Lint deletes old top-level Markdown and idle drafts expire/rehome; this is bounded forgetting, not universal raw deletion."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-rte-catalog-reuse"
          note: "Lint deletes old top-level Markdown and idle drafts expire/rehome; this is bounded forgetting, not universal raw deletion."
        -
          scope: "Semantic operation of general compilation"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-writer-transform"
          note: "Requested summaries/inferences do not establish the semantic relation of concrete outputs; synthesis is not inferred from request wording."
        -
          scope: "Complete taxonomy lifecycle, media and inbox research transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Uninspected transformations prevent an exhaustive curation inventory. Index rebuilds, primary-key checks and hit deduplication alone are not memory curation."
      records:
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-rte-catalog-reuse"
        - "epistemic.md#epi-rte-catalog-sync"
        - "memory.md#mem-obj-inbox"
        - "epistemic.md#epi-rte-writer-transform"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
      note: "Implemented consolidation, revision and bounded decay survive unresolved semantic and alternative-route coverage."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Ordinary caller search/get and requested file reloads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-search-get"
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
              note: "Question/keywords or page request precedes selection; code ranking/delivery within the request is not an additional push."
          records:
            - "runtime.md#rt-rte-search-get"
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
          note: "Question/keywords or page request precedes selection; code ranking/delivery within the request is not an additional push."
        -
          scope: "Pending source batches selected for compiler"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-publish"
                - "memory.md#mem-obj-ledgers"
                - "memory.md#mem-rte-session-distillation"
              note: "Ingest trigger selects unprocessed/unheld retained sources and supplies paths to a fresh writer without a writer request for those items."
          records:
            - "runtime.md#rt-rte-compile-publish"
            - "memory.md#mem-obj-ledgers"
            - "memory.md#mem-rte-session-distillation"
          note: "Ingest trigger selects unprocessed/unheld retained sources and supplies paths to a fresh writer without a writer request for those items."
        -
          scope: "Catalog precedents and taxonomy supplied to classifiers"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-catalog-reuse"
                - "memory.md#mem-obj-taxonomy"
              note: "Classification trigger selects retained same-URL/author examples and standing category text for a new call."
          records:
            - "memory.md#mem-rte-catalog-reuse"
            - "memory.md#mem-obj-taxonomy"
          note: "Classification trigger selects retained same-URL/author examples and standing category text for a new call."
        -
          scope: "Stored feedback/review problems and usage report context supplied to repair/lint"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-obj-usage"
                - "runtime.md#rt-rte-inbox-maintenance"
              note: "Fix/lint triggers select retained problems or report context for a fresh writer; additional source-file requests remain pull."
          records:
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-obj-usage"
            - "runtime.md#rt-rte-inbox-maintenance"
          note: "Fix/lint triggers select retained problems or report context for a fresh writer; additional source-file requests remain pull."
        -
          scope: "Full inbox research, media consumers and external CLI context alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-inbox-maintenance"
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-backend-execution"
          note: "Complete selection/delivery operations are not established for these included alternatives."
      records:
        - "runtime.md#rt-rte-search-get"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-compile-publish"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-rte-catalog-reuse"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-review"
        - "memory.md#mem-obj-usage"
        - "runtime.md#rt-rte-inbox-maintenance"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-backend-execution"
      note: "Both requested retrieval and automatic write-side context supply exist; one pull route cannot resolve all alternatives."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Ingest pending-source push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-publish"
                - "memory.md#mem-obj-ledgers"
              note: "Trigger ingest; selector uses processed/held membership and batch/companion availability; selected retained parts are pending raw files, not question-targeted retrieval."
          records:
            - "runtime.md#rt-rte-compile-publish"
            - "memory.md#mem-obj-ledgers"
          note: "Trigger ingest; selector uses processed/held membership and batch/companion availability; selected retained parts are pending raw files, not question-targeted retrieval."
        -
          scope: "Classification precedent push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-catalog-reuse"
              note: "Trigger classification; exact normalized URL/author matches select earlier catalog rows, bounded to two URL and three author precedents."
          records:
            - "memory.md#mem-rte-catalog-reuse"
          note: "Trigger classification; exact normalized URL/author matches select earlier catalog rows, bounded to two URL and three author precedents."
        -
          scope: "Standing taxonomy supply to classifier"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-taxonomy"
                - "memory.md#mem-rte-catalog-reuse"
              note: "Trigger classification; taxonomy/draft availability selects standing category guidance, distinct from identifier-targeted precedent selection."
          records:
            - "memory.md#mem-obj-taxonomy"
            - "memory.md#mem-rte-catalog-reuse"
          note: "Trigger classification; taxonomy/draft availability selects standing category guidance, distinct from identifier-targeted precedent selection."
        -
          scope: "Fix/lint retained problem and usage-context push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-obj-usage"
              note: "Trigger fix/lint; unfixed-directory/status/time/budget filters select review problems and bounded usage reports; identifiers on work items do not alone establish targeted push."
          records:
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-obj-usage"
          note: "Trigger fix/lint; unfixed-directory/status/time/budget filters select review problems and bounded usage reports; identifiers on work items do not alone establish targeted push."
        -
          scope: "Full inbox research and opaque context selection"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-inbox-maintenance"
            - "runtime.md#rt-rte-backend-execution"
          note: "No complete trigger/input/selected-part account is supplied for these alternatives."
        -
          scope: "Ordinary requested search/get branch"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-search-get"
          note: "Push-signal classification does not apply to selection fulfilling the caller's request; lexical/vector ranking there is not a push signal."
      records:
        - "runtime.md#rt-rte-compile-publish"
        - "memory.md#mem-obj-ledgers"
        - "memory.md#mem-rte-catalog-reuse"
        - "memory.md#mem-obj-taxonomy"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-review"
        - "memory.md#mem-obj-usage"
        - "runtime.md#rt-rte-inbox-maintenance"
        - "runtime.md#rt-rte-backend-execution"
        - "runtime.md#rt-rte-search-get"
      note: "Identifier and coarse push selectors are supported; requested search ranking does not add inferred-lexical or inferred-embedding push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Session distillation to retained snapshots and later compiler/asking context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
                - "memory.md#mem-obj-session-snapshots"
              note: "Automatic trace-fed durable text reaches later consumers. Fixed model weights do not negate this route."
          records:
            - "memory.md#mem-rte-session-distillation"
            - "memory.md#mem-obj-session-snapshots"
          note: "Automatic trace-fed durable text reaches later consumers. Fixed model weights do not negate this route."
        -
          scope: "Usage diagnostics to retained problems, repaired wiki and later retrieval"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-usage"
                - "memory.md#mem-obj-review"
                - "memory.md#mem-obj-wiki"
              note: "Session experience feeds automatic repair artifacts and subsequent consumers; successful improvement is unobserved."
          records:
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-obj-usage"
            - "memory.md#mem-obj-review"
            - "memory.md#mem-obj-wiki"
          note: "Session experience feeds automatic repair artifacts and subsequent consumers; successful improvement is unobserved."
        -
          scope: "Rerank execution timing to durable future budget control"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-rerank-budget"
              note: "Execution feedback automatically updates retained behavior-shaping scalar state used by later searches."
          records:
            - "memory.md#mem-rte-rerank-budget"
          note: "Execution feedback automatically updates retained behavior-shaping scalar state used by later searches."
        -
          scope: "Media, full inbox research, taxonomy lifecycle and evaluation-derived update alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
            - "memory.md#mem-obj-taxonomy"
            - "epistemic.md#epi-obj-questions"
            - "epistemic.md#epi-obj-tool-metrics"
          note: "Incomplete provenance/update-consumer coverage prevents a complete learning inventory. Diagnostic evaluation storage alone does not prove a qualifying behavior update."
      records:
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-obj-session-snapshots"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-usage"
        - "memory.md#mem-obj-review"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-rte-rerank-budget"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
        - "memory.md#mem-obj-taxonomy"
        - "epistemic.md#epi-obj-questions"
        - "epistemic.md#epi-obj-tool-metrics"
      note: "Supported yes routes establish existence, not a complete value inventory or improved capacity. No local no is asserted without an evidenced-absence record."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Session snapshot production"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
              note: "Original input mixes conversational turns and recorded tool outcomes; a session adapter label is not an environmental event origin."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-distillation"
              note: "Original input mixes conversational turns and recorded tool outcomes; a session adapter label is not an environmental event origin."
          records:
            - "memory.md#mem-rte-session-distillation"
          note: "Original input mixes conversational turns and recorded tool outcomes; a session adapter label is not an environmental event origin."
        -
          scope: "Usage-driven repair"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-usage"
              note: "Host logs contain question/answer and recorded searches/opens; retained excerpts feed diagnostic and repair writes."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-repair"
                - "memory.md#mem-obj-usage"
              note: "Host logs contain question/answer and recorded searches/opens; retained excerpts feed diagnostic and repair writes."
          records:
            - "memory.md#mem-rte-usage-repair"
            - "memory.md#mem-obj-usage"
          note: "Host logs contain question/answer and recorded searches/opens; retained excerpts feed diagnostic and repair writes."
        -
          scope: "Rerank budget update"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-rerank-budget"
              note: "Original input is measured execution timing/count feedback from qmd reranking, not semantic knowledge or a trajectory."
          records:
            - "memory.md#mem-rte-rerank-budget"
          note: "Original input is measured execution timing/count feedback from qmd reranking, not semantic knowledge or a trajectory."
        -
          scope: "External compaction-origin detail and uninspected alternative media/research/evaluation updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-session-distillation"
            - "memory.md#mem-obj-assets"
            - "runtime.md#rt-rte-inbox-maintenance"
            - "epistemic.md#epi-obj-questions"
          note: "Opaque upstream provenance and uninspected qualifying alternatives prevent complete source coverage; none is silently made inapplicable."
      records:
        - "memory.md#mem-rte-session-distillation"
        - "memory.md#mem-rte-usage-repair"
        - "memory.md#mem-obj-usage"
        - "memory.md#mem-rte-rerank-budget"
        - "memory.md#mem-obj-assets"
        - "runtime.md#rt-rte-inbox-maintenance"
        - "epistemic.md#epi-obj-questions"
      note: "Trace origin follows actual content, not JSONL format or event labels; no environmental event-stream or linked-trajectory input is established by these records."
---

# MemexOS memory profile

## Comparison rationale

This comparison classifies accepted records, not live operation. All positive implementation findings retain the wired basis; none establishes compliance, improved answers or causal benefit. The manual snapshot procedure has only an afforded basis, separate from unattended admission ([MEM-RTE-session-distillation](memory.md#mem-rte-session-distillation)).

The sole identity supersession affecting this profile is the epistemic wiki object to the memory wiki object. Accordingly the content classifications cite [MEM-OBJ-wiki](memory.md#mem-obj-wiki), not the superseded declaration. Catalog and review containers overlap other objects without identical scope, so they are not counted as independent extra stores merely because two analysts describe them. Evaluation parts keep their separate consumers rather than inheriting a blanket production-admission effect from their container ([EPI-OBJ-questions](epistemic.md#epi-obj-questions), [EPI-OBJ-rank-results](epistemic.md#epi-obj-rank-results), [EPI-OBJ-tool-metrics](epistemic.md#epi-obj-tool-metrics)).

The qmd index contributes vector storage and parametric representation, not model-weight training. Its readable snippets do not resolve internal vector schema or per-vector provenance ([MEM-OBJ-vectors](memory.md#mem-obj-vectors)). Scalar timing state instead has symbolic form and routing authority; its automatic trace-fed write has a later budget consumer, so it qualifies for trace learning without claiming learned neural weights or semantic improvement ([MEM-RTE-rerank-budget](memory.md#mem-rte-rerank-budget)).

Session distillation is consolidation even when raw messages remain available. General writer compilation is left semantically unresolved: requested synthesis and a general ability to rewrite do not establish a new claim absent from actual inputs ([MEM-RTE-session-distillation](memory.md#mem-rte-session-distillation), [EPI-RTE-writer-transform](epistemic.md#epi-rte-writer-transform)). Catalog synchronization establishes revision of effective metadata, not an independent semantic truth check ([EPI-RTE-catalog-sync](epistemic.md#epi-rte-catalog-sync)). Search hit suppression, FTS rebuilds and unused-name checks do not establish retained-memory deduplication.

Read-back is split within chains. Search/get fulfills a caller request and is pull, despite automatic ranking. Ingest, classifier precedent supply and fix/lint select retained inputs for fresh workers and are push. Exact URL/author matching establishes identifier selection only for the precedent branch; availability/status/budget selection stays coarse ([RT-RTE-search-get](runtime.md#rt-rte-search-get), [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish), [MEM-RTE-catalog-reuse](memory.md#mem-rte-catalog-reuse), [MEM-RTE-usage-repair](memory.md#mem-rte-usage-repair)).

Trace learning means the automatic trace-fed write plus durable behavior-shaping output and later consumer required by this member's contract. It does not upgrade the reports' independent learning-as-improved-capacity conclusion. Session and usage routes yield a supported system existence finding of yes. No system-wide no or complete-value conclusion follows; unresolved media, research, taxonomy and evaluator provenance remain included. Session logs and tool outcomes are original inputs; serialization as events does not establish event-stream origin ([MEM-RTE-session-distillation](memory.md#mem-rte-session-distillation), [MEM-RTE-usage-repair](memory.md#mem-rte-usage-repair)).

Retained review verdicts can validate and veto enabled publication while their prose directs a later repair writer. Published page content supplies knowledge to asking agents. Neither path implies uniform enforcement of truth, and the gate-off/no-change and metadata-sync paths remain exceptions ([MEM-OBJ-review](memory.md#mem-obj-review), [EPI-RTE-review-decision](epistemic.md#epi-rte-review-decision), [RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages), [EPI-RTE-catalog-sync](epistemic.md#epi-rte-catalog-sync)).

Every axis is partial because the accepted inventory includes incompletely inspected alternatives. These limits are not negative findings. No evidenced-absence record supports a local trace-learning no. Caller identity alone leaves manual admission unresolved for category, capture and inbox decision APIs. Static initialization does not resolve subsequent human control ([MEM-OBJ-taxonomy](memory.md#mem-obj-taxonomy), [MEM-OBJ-raw](memory.md#mem-obj-raw), [RT-RTE-inbox-maintenance](runtime.md#rt-rte-inbox-maintenance)).

Source-read log: none. No named record ambiguity required direct source inspection; no new evidence, record, source or report correction is introduced.
