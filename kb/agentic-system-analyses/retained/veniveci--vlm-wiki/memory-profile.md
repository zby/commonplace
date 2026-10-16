---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "VLM-wiki memory comparison of accumulated local media/wiki state, import admission metadata and later review/delivery routes."
run-id: "AAS-2026-10-14-vlm-wiki-311faef777b4-01"
source-identity: "https://github.com/veniVeci/VLM-wiki"
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
memory-comparison:
  version: 2
  scope: "Accumulated raw media/text and frames; analysis prose/status and physical metadata; import manifest; personal/project wiki articles, archives, index and logs; historical/work reviews and runtime briefs; helper-target report revisions and their admission, maintenance and established later consumers. Static shipped AGENTS/prompts/config/templates and external host/provider weights are not accumulated memory. Unknown initial authorship and missing output consumers remain included uncertainties; external host internals, private input/config state and unaudited media semantics are not silently classified."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Raw copies, frames, analysis prose and JSON; manifest; personal/project articles, index, logs, review Markdown, runtime briefs and helper-target reports"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-inputs"
                - "memory.md#mem-obj-import-manifest"
                - "memory.md#mem-obj-analysis-reports"
                - "memory.md#mem-obj-frame-images"
                - "memory.md#mem-obj-analysis-results"
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-wiki-log"
                - "memory.md#mem-obj-history-reviews"
                - "memory.md#mem-obj-work-review"
                - "memory.md#mem-obj-runtime-briefs"
                - "epistemic.md#epi-obj-vlm-analysis"
              note: "All included accumulated objects are local files. Implemented file writers establish the substrate; instructed wiki writing and tracked examples use the same substrate, not a separate repository-backed storage engine."
          records:
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-import-manifest"
            - "memory.md#mem-obj-analysis-reports"
            - "memory.md#mem-obj-frame-images"
            - "memory.md#mem-obj-analysis-results"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-history-reviews"
            - "memory.md#mem-obj-work-review"
            - "memory.md#mem-obj-runtime-briefs"
            - "epistemic.md#epi-obj-vlm-analysis"
          note: "All included accumulated objects are local files. Implemented file writers establish the substrate; instructed wiki writing and tracked examples use the same substrate, not a separate repository-backed storage engine."
      records:
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-import-manifest"
        - "memory.md#mem-obj-analysis-reports"
        - "memory.md#mem-obj-frame-images"
        - "memory.md#mem-obj-analysis-results"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-project-pages"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-history-reviews"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-obj-runtime-briefs"
        - "epistemic.md#epi-obj-vlm-analysis"
      note: "The accepted object inventory covers the shipped retained boundary. Git tracks some examples but is not their operative memory storage API; static configuration, prompts and external provider weights are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Natural-language output encoding of automatically persisted provider reports, project/review prose, logs, brief payloads and helper provenance labels; no downstream interpretation asserted"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-inputs"
                - "memory.md#mem-obj-analysis-reports"
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-wiki-log"
                - "memory.md#mem-obj-history-reviews"
                - "memory.md#mem-obj-work-review"
                - "memory.md#mem-obj-runtime-briefs"
                - "epistemic.md#epi-obj-vlm-analysis"
              note: "Implemented writers persist natural-language prose. This finding concerns output encoding only: a wired producer does not establish a later semantic consumer, including for briefs and helper targets."
          records:
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-analysis-reports"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-history-reviews"
            - "memory.md#mem-obj-work-review"
            - "memory.md#mem-obj-runtime-briefs"
            - "epistemic.md#epi-obj-vlm-analysis"
          note: "Known encoding does not resolve later consumption. Host interpretation and missing readers are separated below."
        -
          scope: "Raw prose, personal/project article bodies and index summaries at instructed host compilation/query"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: [memory.md#mem-obj-raw-inputs, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-project-pages, memory.md#mem-obj-wiki-index, runtime.md#rt-rte-agent-workflow, runtime.md#rt-rte-wiki-query]
              note: "Instructions request semantic interpretation and synthesis; wired page production does not establish host execution."
          records: [memory.md#mem-obj-raw-inputs, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-project-pages, memory.md#mem-obj-wiki-index, runtime.md#rt-rte-agent-workflow, runtime.md#rt-rte-wiki-query]
          note: "This classifies the instructed path at claimed strength, independently of output encoding."
        -
          scope: "Work-review prose delivered by the cycle sender to human recipients"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: [memory.md#mem-obj-work-review, runtime.md#rt-rte-work-cycle]
              note: "The sender supplies selected advisory prose for human interpretation; actual receipt and interpretation remain unobserved."
          records: [memory.md#mem-obj-work-review, runtime.md#rt-rte-work-cycle]
          note: "Wiring covers only the selected preview, not every retained prose output."
        -
          scope: "Historical-review prose at the documented standalone sender's human recipient"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records: [memory.md#mem-obj-history-reviews, memory.md#mem-clm-daily-delivery]
              note: "Documentation affords this consumer path through the fallback projection, not the intended embedded preview."
          records: [memory.md#mem-obj-history-reviews, memory.md#mem-clm-daily-delivery]
          note: "A documented caller does not establish an implemented historical-review delivery cycle."
        -
          scope: "Later semantic consumption of brief payloads, helper provenance labels, analysis reports and operational logs"
          assessment: "not-determinable"
          findings: []
          records: [memory.md#mem-obj-runtime-briefs, epistemic.md#epi-obj-vlm-analysis, epistemic.md#epi-rte-disclaimer-rewrite, memory.md#mem-obj-analysis-reports, memory.md#mem-obj-wiki-log]
          note: "Natural-language output encoding is known, but later readers and delivered payloads are not established. Their operative semantic interpretation paths therefore remain unresolved."
        -
          scope: "Manifest keys/fields, metadata/status JSON, article fields at the parser, path/link/date wrappers, runtime structures, and encoded source/frame media"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-import-manifest"
                - "memory.md#mem-obj-analysis-results"
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-runtime-briefs"
                - "memory.md#mem-obj-raw-inputs"
                - "memory.md#mem-obj-frame-images"
                - "memory.md#mem-clm-parser-projection"
              note: "These are symbolic encodings. Actual programmatic consumption is established for manifest membership, parsed article fields and media-tool inputs; output serialization alone establishes no later status/brief reader. Depicted meaning is a separate interpretation path."
          records:
            - "memory.md#mem-obj-import-manifest"
            - "memory.md#mem-obj-analysis-results"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-runtime-briefs"
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-frame-images"
            - "memory.md#mem-clm-parser-projection"
          note: "Known symbolic encoding does not establish consumption of every serialized output. Media bytes are not parametric memory."
      records:
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-analysis-reports"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-project-pages"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-history-reviews"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-obj-runtime-briefs"
        - "epistemic.md#epi-obj-vlm-analysis"
        - "memory.md#mem-obj-import-manifest"
        - "memory.md#mem-obj-analysis-results"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-frame-images"
        - "memory.md#mem-clm-parser-projection"
      note: "Encoding and consumption are distinguished. Wired outputs do not upgrade claimed host reading, afforded historical delivery or unresolved brief/helper/report/log readers; missing consumers leave path coverage partial. Provider parameters are outside the accumulated-memory boundary, so model calls establish no parametric memory finding."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Importer copies and copied external text previews in project pages"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-inputs"
                - "memory.md#mem-obj-project-pages"
                - "runtime.md#rt-rte-source-import"
              note: "Byte copying and preview acquisition establish imported paths, not original authorship."
          records:
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-project-pages"
            - "runtime.md#rt-rte-source-import"
          note: "Byte copying and preview acquisition establish imported paths, not original authorship."
        -
          scope: "Direct provider-response prose and fixed authored project/review interpretations"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-analysis-reports"
                - "epistemic.md#epi-rte-history-interpretation"
                - "epistemic.md#epi-rte-work-interpretation"
              note: "Models or fixed authored strings supply prose; this is independent of admission control and factual warrant."
          records:
            - "memory.md#mem-obj-analysis-reports"
            - "epistemic.md#epi-rte-history-interpretation"
            - "epistemic.md#epi-rte-work-interpretation"
          note: "Models or fixed authored strings supply prose; this is independent of admission control and factual warrant."
        -
          scope: "Host article/archive writing and index/log maintenance"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-wiki-index"
                - "runtime.md#rt-rte-agent-workflow"
              note: "Instructions request model authorship; historical examples are not thereby authenticated."
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-wiki-index"
            - "runtime.md#rt-rte-agent-workflow"
          note: "Instructions request model authorship; historical examples are not thereby authenticated."
        -
          scope: "Frame sampling, physical metadata/status, manifest records and derived index/brief structure"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-frame-images"
                - "memory.md#mem-obj-analysis-results"
                - "memory.md#mem-obj-import-manifest"
                - "memory.md#mem-obj-runtime-briefs"
                - "memory.md#mem-obj-wiki-index"
              note: "Code compiles representations without establishing learned parameters or historical initial provenance."
          records:
            - "memory.md#mem-obj-frame-images"
            - "memory.md#mem-obj-analysis-results"
            - "memory.md#mem-obj-import-manifest"
            - "memory.md#mem-obj-runtime-briefs"
            - "memory.md#mem-obj-wiki-index"
          note: "Code compiles representations without establishing learned parameters or historical initial provenance."
        -
          scope: "External work activity/Git metadata into project pages and reviews; article/diary history into historical reports"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-work-review"
                - "memory.md#mem-obj-history-reviews"
                - "runtime.md#rt-rte-work-cycle"
                - "runtime.md#rt-rte-history-review"
              note: "Selected activity and historical clues are extracted into durable reports. This lineage finding alone does not prove every route qualifies as trace learning."
          records:
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-work-review"
            - "memory.md#mem-obj-history-reviews"
            - "runtime.md#rt-rte-work-cycle"
            - "runtime.md#rt-rte-history-review"
          note: "Selected activity and historical clues are extracted into durable reports. This lineage finding alone does not prove every route qualifies as trace learning."
        -
          scope: "Initial checked-in analysis reports, personal articles, index rows and historical raw content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-analysis-reports"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-raw-inputs"
          note: "Original producing invocation, authorship and derivation are unresolved. Known future transformations cannot settle these origins."
      records:
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-project-pages"
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-obj-analysis-reports"
        - "epistemic.md#epi-rte-history-interpretation"
        - "epistemic.md#epi-rte-work-interpretation"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-wiki-index"
        - "runtime.md#rt-rte-agent-workflow"
        - "memory.md#mem-obj-frame-images"
        - "memory.md#mem-obj-analysis-results"
        - "memory.md#mem-obj-import-manifest"
        - "memory.md#mem-obj-runtime-briefs"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-obj-history-reviews"
        - "runtime.md#rt-rte-work-cycle"
        - "runtime.md#rt-rte-history-review"
      note: "Positive paths coexist with unknown initialization. No imported/authored classification is invented for unauthenticated sample history."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Raw media/text at interpretation; project/article fields at historical report builders; work preview at human recipients"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-inputs"
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-history-reviews"
                - "memory.md#mem-obj-work-review"
                - "runtime.md#rt-rte-history-review"
                - "runtime.md#rt-rte-work-cycle"
              note: "Retained evidence/context shapes reports or supplies human advice; recommendations do not become standing host instructions merely by using imperative prose."
          records:
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-history-reviews"
            - "memory.md#mem-obj-work-review"
            - "runtime.md#rt-rte-history-review"
            - "runtime.md#rt-rte-work-cycle"
          note: "Retained evidence/context shapes reports or supplies human advice; recommendations do not become standing host instructions merely by using imperative prose."
        -
          scope: "Personal/project articles at index-led host answering"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-project-pages"
                - "runtime.md#rt-rte-wiki-query"
              note: "The host is told to prefer article evidence; compliance and answer dependence remain unobserved."
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-project-pages"
            - "runtime.md#rt-rte-wiki-query"
          note: "The host is told to prefer article evidence; compliance and answer dependence remain unobserved."
        -
          scope: "Index links and summaries at host article selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-index"
                - "runtime.md#rt-rte-wiki-query"
                - "memory.md#mem-clm-index-targets"
              note: "Retained navigation selects article inputs, without a demonstrated ranking algorithm or complete target consistency."
          records:
            - "memory.md#mem-obj-wiki-index"
            - "runtime.md#rt-rte-wiki-query"
            - "memory.md#mem-clm-index-targets"
          note: "Retained navigation selects article inputs, without a demonstrated ranking algorithm or complete target consistency."
        -
          scope: "Manifest membership at later import admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-import-manifest"
                - "runtime.md#rt-rte-source-import"
              note: "A retained fingerprint is an exclusion criterion and executable skip veto; descriptive manifest fields have no equivalent force."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-import-manifest"
                - "runtime.md#rt-rte-source-import"
              note: "A retained fingerprint is an exclusion criterion and executable skip veto; descriptive manifest fields have no equivalent force."
          records:
            - "memory.md#mem-obj-import-manifest"
            - "runtime.md#rt-rte-source-import"
          note: "A retained fingerprint is an exclusion criterion and executable skip veto; descriptive manifest fields have no equivalent force."
        -
          scope: "Retained article dates/tags and diary repetition at historical priority selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-clm-parser-projection"
                - "epistemic.md#epi-rte-history-statistics"
                - "epistemic.md#epi-rte-history-interpretation"
              note: "Retained fields determine latest/top-place and repeated-line priority under fixed rules; no learned ranking policy is required."
          records:
            - "memory.md#mem-clm-parser-projection"
            - "epistemic.md#epi-rte-history-statistics"
            - "epistemic.md#epi-rte-history-interpretation"
          note: "Retained fields determine latest/top-place and repeated-line priority under fixed rules; no learned ranking policy is required."
        -
          scope: "Retained project activity at automatic durable report production for subsequent human/history consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-work-review"
                - "runtime.md#rt-rte-work-cycle"
                - "runtime.md#rt-rte-history-review"
              note: "Activity records feed durable behavior-shaping advice and pages, with a later sender/history consumer. This update-consumer force is separate from downstream knowledge and proves no improved capacity."
          records:
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-work-review"
            - "runtime.md#rt-rte-work-cycle"
            - "runtime.md#rt-rte-history-review"
          note: "Activity records feed durable behavior-shaping advice and pages, with a later sender/history consumer. This update-consumer force is separate from downstream knowledge and proves no improved capacity."
        -
          scope: "Analysis reports, metadata/status outputs, briefs, logs and helper-target labels without an established later consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-analysis-reports"
            - "memory.md#mem-obj-analysis-results"
            - "memory.md#mem-obj-runtime-briefs"
            - "memory.md#mem-obj-wiki-log"
            - "epistemic.md#epi-obj-vlm-analysis"
          note: "Retention or a trust warning alone cannot establish downstream authority; missing reader/activation facts prevent assigning a force to these alternatives."
      records:
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-project-pages"
        - "memory.md#mem-obj-history-reviews"
        - "memory.md#mem-obj-work-review"
        - "runtime.md#rt-rte-history-review"
        - "runtime.md#rt-rte-work-cycle"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-clm-index-targets"
        - "memory.md#mem-obj-import-manifest"
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-clm-parser-projection"
        - "epistemic.md#epi-rte-history-statistics"
        - "epistemic.md#epi-rte-history-interpretation"
        - "memory.md#mem-obj-analysis-reports"
        - "memory.md#mem-obj-analysis-results"
        - "memory.md#mem-obj-runtime-briefs"
        - "memory.md#mem-obj-wiki-log"
        - "epistemic.md#epi-obj-vlm-analysis"
      note: "Actual retained parts and consumers determine force. Static AGENTS/config authority is excluded. Missing consumers are retained as uncertainty, not silently classified as instruction or enforcement."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Importer admissions, decoder/metadata writes, direct response persistence, project/index/review/brief/log production and marker-controlled repair"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-import"
                - "memory.md#mem-rte-frame-extraction"
                - "memory.md#mem-rte-metadata-extraction"
                - "runtime.md#rt-rte-image-analysis"
                - "runtime.md#rt-rte-history-review"
                - "runtime.md#rt-rte-work-cycle"
                - "epistemic.md#epi-rte-disclaimer-rewrite"
              note: "Software admits individual outputs without a per-content human decision. Confirmation, configuration and workflow launch are not content approval."
          records:
            - "runtime.md#rt-rte-source-import"
            - "memory.md#mem-rte-frame-extraction"
            - "memory.md#mem-rte-metadata-extraction"
            - "runtime.md#rt-rte-image-analysis"
            - "runtime.md#rt-rte-history-review"
            - "runtime.md#rt-rte-work-cycle"
            - "epistemic.md#epi-rte-disclaimer-rewrite"
          note: "Software admits individual outputs without a per-content human decision. Confirmation, configuration and workflow launch are not content approval."
        -
          scope: "Requested host compilation, related-page editing, archive and navigation/log updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-workflow"
                - "memory.md#mem-obj-wiki-articles"
                - "memory.md#mem-obj-wiki-index"
              note: "The model chooses and admits content under instructions; an archive request initiates work rather than approving each assertion."
          records:
            - "runtime.md#rt-rte-agent-workflow"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-wiki-index"
          note: "The model chooses and admits content under instructions; an archive request initiates work rather than approving each assertion."
        -
          scope: "Original raw submissions and initialization of tracked reports/articles/index/history"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-analysis-reports"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-wiki-log"
          note: "The records do not identify per-content human supplying/editing/approval decisions. File editability alone cannot establish manual admission."
      records:
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-rte-frame-extraction"
        - "memory.md#mem-rte-metadata-extraction"
        - "runtime.md#rt-rte-image-analysis"
        - "runtime.md#rt-rte-history-review"
        - "runtime.md#rt-rte-work-cycle"
        - "epistemic.md#epi-rte-disclaimer-rewrite"
        - "runtime.md#rt-rte-agent-workflow"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-analysis-reports"
        - "memory.md#mem-obj-wiki-log"
      note: "Known automatic mechanisms do not resolve initial control or hypothetical later human edits; no unsupported manual finding is added."
    curation_operations:
      assessment: "known"
      units:
        -
          scope: "Retained article metadata and diary lines reduced to snapshots and selected clues"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-history-review"
                - "memory.md#mem-clm-parser-projection"
                - "epistemic.md#epi-rte-history-statistics"
              note: "The report reduces retained information; lossy parsing bounds fidelity, not the existence of consolidation."
          records:
            - "runtime.md#rt-rte-history-review"
            - "memory.md#mem-clm-parser-projection"
            - "epistemic.md#epi-rte-history-statistics"
          note: "The report reduces retained information; lossy parsing bounds fidelity, not the existence of consolidation."
        -
          scope: "Historical and work interpretation branches over retained/current activity"
          assessment: "known"
          findings:
            -
              value: "synthesize"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-history-interpretation"
                - "epistemic.md#epi-rte-work-interpretation"
                - "memory.md#mem-obj-project-pages"
              note: "Recorded counterexamples establish claims not entailed by input counters or filenames. These are authored conjectures, not accepted knowledge."
          records:
            - "epistemic.md#epi-rte-history-interpretation"
            - "epistemic.md#epi-rte-work-interpretation"
            - "memory.md#mem-obj-project-pages"
          note: "Recorded counterexamples establish claims not entailed by input counters or filenames. These are authored conjectures, not accepted knowledge."
        -
          scope: "Existing helper-target report changed by warning prefix and replacements; Projects index section replaced"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-disclaimer-rewrite"
                - "memory.md#mem-obj-wiki-index"
                - "runtime.md#rt-rte-work-cycle"
              note: "Implemented edits revise existing retained entries. Independent full-file regeneration without reading old content is not automatically semantic evolution."
          records:
            - "epistemic.md#epi-rte-disclaimer-rewrite"
            - "memory.md#mem-obj-wiki-index"
            - "runtime.md#rt-rte-work-cycle"
          note: "Implemented edits revise existing retained entries. Independent full-file regeneration without reading old content is not automatically semantic evolution."
        -
          scope: "Requested wiki extraction/archive, related-page updates and new pattern claims"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-workflow"
                - "memory.md#mem-obj-wiki-articles"
                - "epistemic.md#epi-clm-wiki-compounding"
              note: "Instructions request reduced accounts, revisions and discovery. These remain claimed operations, not implemented general model curation."
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-workflow"
                - "memory.md#mem-obj-wiki-articles"
                - "epistemic.md#epi-clm-wiki-compounding"
              note: "Instructions request reduced accounts, revisions and discovery. These remain claimed operations, not implemented general model curation."
            -
              value: "synthesize"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-workflow"
                - "memory.md#mem-obj-wiki-articles"
                - "epistemic.md#epi-clm-wiki-compounding"
              note: "Instructions request reduced accounts, revisions and discovery. These remain claimed operations, not implemented general model curation."
          records:
            - "runtime.md#rt-rte-agent-workflow"
            - "memory.md#mem-obj-wiki-articles"
            - "epistemic.md#epi-clm-wiki-compounding"
          note: "Instructions request reduced accounts, revisions and discovery. These remain claimed operations, not implemented general model curation."
      records:
        - "runtime.md#rt-rte-history-review"
        - "memory.md#mem-clm-parser-projection"
        - "epistemic.md#epi-rte-history-statistics"
        - "epistemic.md#epi-rte-history-interpretation"
        - "epistemic.md#epi-rte-work-interpretation"
        - "memory.md#mem-obj-project-pages"
        - "epistemic.md#epi-rte-disclaimer-rewrite"
        - "memory.md#mem-obj-wiki-index"
        - "runtime.md#rt-rte-work-cycle"
        - "runtime.md#rt-rte-agent-workflow"
        - "memory.md#mem-obj-wiki-articles"
        - "epistemic.md#epi-clm-wiki-compounding"
      note: "Inventory covers the recorded transformations, with evidence strength local to each. Import fingerprint collision checks are not deduplication; index rebuild is not promotion. The helper does not establish dependency-wide invalidation or truth repair."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Later importer manifest lookup; frame/image metadata requests; historical-review collection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-import"
                - "memory.md#mem-rte-metadata-extraction"
                - "runtime.md#rt-rte-history-review"
              note: "The invoked consumer requests retained files/fields needed for its operation. Internal delivery fulfilling that request is not another push."
          records:
            - "runtime.md#rt-rte-source-import"
            - "memory.md#mem-rte-metadata-extraction"
            - "runtime.md#rt-rte-history-review"
          note: "The invoked consumer requests retained files/fields needed for its operation. Internal delivery fulfilling that request is not another push."
        -
          scope: "Question-led host index/article reads and documented human browsing"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-wiki-query"
                - "memory.md#mem-obj-wiki-articles"
              note: "The user question causes retrieval; model relevance choice within that requested retrieval remains pull."
          records:
            - "runtime.md#rt-rte-wiki-query"
            - "memory.md#mem-obj-wiki-articles"
          note: "The user question causes retrieval; model relevance choice within that requested retrieval remains pull."
        -
          scope: "Producer-initiated work-review preview delivery to configured WeCom recipients"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-work-cycle"
                - "memory.md#mem-obj-work-review"
              note: "After cycle invocation, code launches sender and supplies selected retained review content without a recipient query. Scheduler recurrence and successful receipt are not established."
          records:
            - "runtime.md#rt-rte-work-cycle"
            - "memory.md#mem-obj-work-review"
          note: "After cycle invocation, code launches sender and supplies selected retained review content without a recipient query. Scheduler recurrence and successful receipt are not established."
        -
          scope: "Standalone historical-review sender documented in README"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-clm-daily-delivery"
                - "memory.md#mem-obj-history-reviews"
              note: "A documented caller supplies the file to the same outbound sender; the daily preview marker mismatch changes selected content, not direction."
          records:
            - "memory.md#mem-clm-daily-delivery"
            - "memory.md#mem-obj-history-reviews"
          note: "A documented caller supplies the file to the same outbound sender; the daily preview marker mismatch changes selected content, not direction."
      records:
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-rte-metadata-extraction"
        - "runtime.md#rt-rte-history-review"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-rte-work-cycle"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-clm-daily-delivery"
        - "memory.md#mem-obj-history-reviews"
      note: "Read-back inventory distinguishes requested reads from unsolicited downstream delivery. Reports/briefs/logs without established readers add no inferred direction; their limitation is explicit in the cited object inventory."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "Work-cycle push: cycle completion triggers preview availability/heading and fixed line/character-budget selection of the produced review"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-work-cycle"
                - "memory.md#mem-obj-work-review"
              note: "The selector uses a static preview section and budgets, not question relevance, embedding similarity or matched recipient/content identities. The upstream review path is a requested file handoff, not identifier-targeted selection."
          records:
            - "runtime.md#rt-rte-work-cycle"
            - "memory.md#mem-obj-work-review"
          note: "The selector uses a static preview section and budgets, not question relevance, embedding similarity or matched recipient/content identities. The upstream review path is a requested file handoff, not identifier-targeted selection."
        -
          scope: "Documented historical-review push: caller invokes sender with daily file; fallback chooses first twenty nonempty cleaned lines"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-clm-daily-delivery"
              note: "The English preview heading fails the Chinese marker test; fallback and 4000-character cap determine recipient payload. Selector implementation is wired, but this additional consumer route is afforded."
          records:
            - "memory.md#mem-clm-daily-delivery"
          note: "The English preview heading fails the Chinese marker test; fallback and 4000-character cap determine recipient payload. Selector implementation is wired, but this additional consumer route is afforded."
      records:
        - "runtime.md#rt-rte-work-cycle"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-clm-daily-delivery"
      note: "All recorded push branches use coarse content availability/section/budget rules. Host judgment belongs to requested pull selection and does not justify inferred-judgment push; manifest identity lookup is also on a pull route."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "External project activity/Git metadata automatically converted to retained project pages and work advice, consumed by later history invocation or sender"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-work-review"
                - "runtime.md#rt-rte-work-cycle"
                - "runtime.md#rt-rte-history-review"
              note: "Automatic trace-fed durable behavior-shaping material has a later consumer. Fixed Python rules and human-facing advice do not disqualify the route; no parameter update, recursive review adaptation or improvement is asserted."
          records:
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-work-review"
            - "runtime.md#rt-rte-work-cycle"
            - "runtime.md#rt-rte-history-review"
          note: "Automatic trace-fed durable behavior-shaping material has a later consumer. Fixed Python rules and human-facing advice do not disqualify the route; no parameter update, recursive review adaptation or improvement is asserted."
        -
          scope: "Historical article/diary transformation, host media/archive routes and initial sample content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-history-reviews"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-runtime-briefs"
            - "runtime.md#rt-rte-agent-workflow"
          note: "Inputs mix personal text, derived work history and unknown origins. The records do not establish qualifying trace provenance and later-consumed guidance for every included alternative; brief retention alone supplies no later consumer."
      records:
        - "memory.md#mem-obj-project-pages"
        - "memory.md#mem-obj-work-review"
        - "runtime.md#rt-rte-work-cycle"
        - "runtime.md#rt-rte-history-review"
        - "memory.md#mem-obj-history-reviews"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-runtime-briefs"
        - "runtime.md#rt-rte-agent-workflow"
      note: "A positive qualifying work route coexists with unresolved origins/consumers. No bounded absence record licenses a global or local no, and unchanged rules do not negate trace learning through durable advice."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Qualifying work trace-fed update: timestamped external file activity and Git commit history into project pages/work advice"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-work-cycle"
                - "memory.md#mem-obj-project-pages"
                - "memory.md#mem-obj-work-review"
              note: "The original trace component records discrete external work events, rather than this system's session transcript or tool execution feedback. Static project text previews add imported content, not a second trace-source value."
          records:
            - "runtime.md#rt-rte-work-cycle"
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-work-review"
          note: "The original trace component records discrete external work events, rather than this system's session transcript or tool execution feedback. Static project text previews add imported content, not a second trace-source value."
        -
          scope: "Mixed project-preview origins and article/diary or host/archive inputs on other potential qualifying routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-project-pages"
            - "memory.md#mem-obj-raw-inputs"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-history-reviews"
            - "runtime.md#rt-rte-agent-workflow"
          note: "Diary prose and article placement alone do not establish calendar/event, conversational, tool-trace or trajectory origin. Missing original content/derivation prevents complete source enumeration; advice/log labels are not source evidence."
      records:
        - "runtime.md#rt-rte-work-cycle"
        - "memory.md#mem-obj-project-pages"
        - "memory.md#mem-obj-work-review"
        - "memory.md#mem-obj-raw-inputs"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-history-reviews"
        - "runtime.md#rt-rte-agent-workflow"
      note: "The work activity component supports event-streams locally. No session-logs, tool-traces or trajectories value follows merely from model use, Git subprocess transport, or a diary filename."
---

# VLM-wiki memory profile

## Comparison rationale

The memory inventory is the accepted memory member's object inventory, not every storage or authority surface in the enclosing runtime. A Git checkout does not by itself turn file memory into a repo substrate. Shipped agent instructions and configuration constrain operation but are not accumulated through use. External provider weights are opaque components, not an established trace-updated memory alternative within this scoped repository mechanism. See [MEM-OBJ-raw-inputs](memory.md#mem-obj-raw-inputs), [MEM-OBJ-import-manifest](memory.md#mem-obj-import-manifest), [MEM-OBJ-runtime-briefs](memory.md#mem-obj-runtime-briefs) and [RT-CMP-qwen](runtime.md#rt-cmp-qwen).

Assessment describes coverage, not activation. The known file and curation inventories do not claim observed use or semantic accuracy. Form coverage is partial: implemented output encoding is distinct from claimed host reading, wired work-preview delivery, afforded historical delivery and unresolved later readers of briefs, helper labels, reports and logs. Claimed host operations stay distinct from wired Python operations; unknown initial content control prevents complete lineage and agency. A missing later consumer prevents an authority finding, not a storage finding. The parser and navigation limitations remain material: [MEM-CLM-parser-projection](memory.md#mem-clm-parser-projection) and [MEM-CLM-index-targets](memory.md#mem-clm-index-targets) prevent equating an on-disk article with faithful report or answer context.

Curation and trace learning are independent. Consolidation reduces retained fields; fixed rules also synthesize unsupported interpretive claims, as established by [EPI-RTE-history-interpretation](epistemic.md#epi-rte-history-interpretation) and [EPI-RTE-work-interpretation](epistemic.md#epi-rte-work-interpretation). The work activity-to-page/advice-to-later-consumer chain qualifies locally as trace learning even though it neither rewrites Python nor demonstrates better future capacity. Other origins and output consumers remain unresolved. Imperative advice is knowledge at its human consumer, not automatically standing agent instruction. No semantic acceptance or causal benefit is implied.

Read-back distinguishes the consumer request from downstream unsolicited supply. Host relevance selection stays on a requested pull route. Preview-section and fixed-budget sender selection supplies a coarse push, not identifier targeting merely because the sender receives a file path. Historical delivery has only its documented caller warrant, and its fallback does not select the intended embedded preview: [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle), [MEM-CLM-daily-delivery](memory.md#mem-clm-daily-delivery).

Reconciliation supersedes the epistemic image-metadata route with [MEM-RTE-metadata-extraction](memory.md#mem-rte-metadata-extraction); all profile references to that preparation/read-back mechanism use the surviving record. Other overlapping containers and epistemic parts remain valid separate referents. No other supersession changes a classification.

Source-read log: none. This profile classifies supplied accepted records only; it adds no source quotation, record, execution or evidence layer.
