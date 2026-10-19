---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Memory profile of fragility-grid's retained evaluation measurements, reporting artifacts and summary-driven resume at the frozen revision."
run-id: AAS-2026-10-18-fragility-grid-38b12f71fceb-01
source-identity: https://github.com/NikolaTesla-007/fragility-grid
reviewed-boundary: "3f51444ead009d8351de1b6b19bf901c4da3d420"
memory-comparison:
  version: 2
  scope: >-
    Retained correctness records, per-model summaries and their existence markers,
    exported configuration legend, analysis JSON and figure exports; collector and
    analysis admission, overwrite and later CPU, shell and reporting consumers.
    Includes unresolved initialization/manual replacement and opaque dependency-cache
    reuse where the accepted records retain those alternatives. Excludes shipped
    static source instructions, unchanged pretrained weights as learned memory,
    current-invocation prompt/output arrays, temporary scheduling queues and diagnostic
    logs without a behavior-shaping update route. Other experiments are outside this subsystem.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Records, summaries/markers, legend, analysis JSON and exported figures"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
              note: "Collector and reporting outputs persist in results/figures filesystem paths; JSON and PNG/PDF are encodings, not separate substrates."
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
          note: "The named local retained artifact inventory has explicit persistence wiring."
        - scope: "Dependency-managed backend and compilation cache contents reused across calls"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "The adapter and externally loaded model establish dependency-managed state, not the substrate inventory of opaque retained cache parts. Configured paths do not classify all internal state."
      records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-cmp-engine, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
      note: "Files are established for explicit outputs; external cache internals prevent complete storage coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Record bits/IDs/instrumentation, summary fields and existence marker, legend metadata, analysis numbers and identifiers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis]
              note: "Fixed loaders, arithmetic and filesystem predicates interpret localized fields, including numerical measurements."
          records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-bap-summary-skip, memory.md#mem-obj-config-legend]
          note: "Covers structured machine-consumed fields, not model weights or unconsumed question semantics."
        - scope: "Embedded record questions and retained analysis interpretation strings / figure labels"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-obj-records, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
              note: "These outputs retain ordinary-language questions, interpretations and labels. CPU loading discards question text; retention does not establish its machine consumption."
          records: [runtime.md#rt-obj-records, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
          note: "Classifies textual parts separately from numeric fields and graphical displays."
        - scope: "Figure graphical encodings of selected aggregate statistics"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-fragility-figures]
              note: "Axes, bands, ranks and plotted quantities encode localized statistical values; rendering does not make them distributed parameters."
          records: [memory.md#mem-obj-fragility-figures]
          note: "The accepted figure record describes displays of symbolic statistics, distinct from their natural-language labels."
        - scope: "Opaque dependency-cache payloads"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "No recorded payload decomposition establishes their form. Loaded pretrained parameters are excluded as unchanged model inputs, not used to classify opaque caches."
      records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-cmp-engine]
      note: "Explicit outputs have mixed symbolic and natural-language parts; opaque cache forms remain unresolved."
    lineage:
      assessment: partial
      units:
        - scope: "Question/gold material embedded in collector records"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-obj-records, epistemic.md#epi-obj-benchmark-items]
              note: "External benchmark content enters through loaders; import does not authenticate its truth or immutable dataset identity."
          records: [runtime.md#rt-obj-records, epistemic.md#epi-obj-benchmark-items]
          note: "Known acquisition path, without a claim about the external content's original authorship."
        - scope: "Collector correctness/instrumentation fields and their per-model summaries"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-rte-generation-grid, runtime.md#rt-rte-likelihood-grid, runtime.md#rt-obj-records, runtime.md#rt-obj-summary]
              note: "Model-call returns are parsed/scored into outcome bits, then aggregated. The retained objects are derived outcomes, not verbatim raw-answer archives."
          records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary]
          note: "Covers the known collector derivation, not possible manual initialization of files."
        - scope: "Exported legend descriptors and permutation metadata"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-config-legend]
              note: "Fixed source definitions and requested permutation count are serialized, rather than extracted from inference experience."
          records: [memory.md#mem-obj-config-legend]
          note: "The export path is known independently of inference success."
        - scope: "Analysis statistics, authored interpretation templates and figure construction"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, epistemic.md#epi-rte-result-labeling]
              note: "Fixed formulas and plotting/labeling code compile retained measurements into aggregates and displays. Their upstream outcomes retain trace-extracted lineage separately."
            - value: authored
              basis: wired
              records: [memory.md#mem-obj-analysis, epistemic.md#epi-rte-result-labeling]
              note: "Interpretation wording is authored in source and admitted under fixed conditions, not generated by a model explanation."
          records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, epistemic.md#epi-rte-result-labeling]
          note: "Separates compilation from the provenance of fixed textual templates within those outputs."
        - scope: "Initial/released or manually replaced records and summaries; opaque cache provenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, runtime.md#rt-cmp-engine]
          note: "Parseable files need not carry collector provenance; external cache contents and initialization are not authenticated. No imported or authored value is inferred merely from an unspecified caller."
      records: [runtime.md#rt-obj-records, runtime.md#rt-obj-summary, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-cmp-engine]
      note: "Known derivations coexist with unresolved initial-content and cache provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained correctness bits consumed by CPU arithmetic and model/configuration ranking"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-record-analysis, epistemic.md#epi-rte-statistical-check]
              note: "Bits supply measurement evidence to the statistical consumer, without authenticating gold truth or collection provenance."
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-record-analysis, epistemic.md#epi-rte-statistical-check]
              note: "Stored outcomes determine reference ranks, adjacent comparisons and subset champions under fixed formulas."
          records: [runtime.md#rt-rte-record-analysis, epistemic.md#epi-rte-statistical-check]
          note: "Actual consumed bit fields have these forces; discarded question/gold/instrumentation fields are not assigned the same authority."
        - scope: "Summary existence marker at shell scheduling"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-bap-summary-skip, runtime.md#rt-rte-sweep-driver]
              note: "A matching summary path selects skip rather than collection for the queued model."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-bap-summary-skip]
              note: "The existence predicate hard-skips collection; it does not inspect summary numerical content or certify compatibility."
          records: [runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip]
          note: "Metadata-level operational force is distinct from interpreting the summary as scientific evidence."
        - scope: "Legend permutation-count field at analysis configuration selection"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-config-legend]
              note: "The retained n_perms value selects the regenerated analysis configuration grid. Exported descriptors and reference metadata are not validated or otherwise consumed."
          records: [memory.md#mem-obj-config-legend]
          note: "Only the field that reaches the selector establishes authority."
        - scope: "Retained outcome bits at automatic production of the later-used summary marker"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, runtime.md#rt-bap-summary-skip]
              note: "Outcome experience feeds an automatic durable artifact that changes later scheduling. This update-consumer force does not establish improved model capacity or downstream instructional authority."
          records: [runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip]
          note: "The trace-fed update and the marker's later routing/enforcement are separate consumption paths."
        - scope: "Retained analysis JSON, summaries and figure exports for human reporting"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-obj-summary]
              note: "Reporting artifacts offer evidence and interpretations to readers; actual scientific reliance or subsequent decisions are not observed."
          records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-obj-summary]
          note: "Reporting affordance is not upgraded to a wired later model/collector consumer."
        - scope: "Opaque dependency-cache consumers/effects"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "Physical cache reuse alone does not establish retained content's semantic, ranking or control force."
      records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-bap-summary-skip, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-cmp-engine]
      note: "Named CPU, scheduling and reporting consumers have distinct forces; opaque cache effects remain unresolved."
    write_agency:
      assessment: partial
      units:
        - scope: "Collector record/summary and legend writes; analysis JSON and figure admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
              note: "Fixed software admits outputs without a per-content operator approval. Launching the experiment does not make these admissions manual."
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
          note: "Known subsequent software writes remain classified despite unresolved initialization."
        - scope: "Manual/released file initialization or replacement and dependency-managed cache admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-obj-records, runtime.md#rt-obj-summary, runtime.md#rt-cmp-engine]
          note: "The records leave human control over supplied/edited files unresolved and do not expose every cache admission mechanism. File presence or generic caller identity cannot establish manual agency."
      records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-cmp-engine]
      note: "Automatic inspected admissions coexist with unknown initial/replacement and cache control."
    curation_operations:
      assessment: partial
      units:
        - scope: "Retained per-item outcomes reduced into summaries and aggregate statistical reporting"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, memory.md#mem-obj-analysis]
              note: "Aggregation compresses retained outcome information into bands, counts and comparisons, without requiring removal of raw bit records."
          records: [runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, memory.md#mem-obj-analysis]
          note: "Reduction of existing measurement content is separate from new interpretive claims."
        - scope: "Analysis interpretation admitted from statistical criteria"
          assessment: known
          findings:
            - value: synthesize
              basis: wired
              records: [epistemic.md#epi-rte-result-labeling, memory.md#mem-obj-analysis]
              note: "Manufactured-gap and mental-uncertainty interpretations introduce claims not entailed by stored bits and intervals; fixed code, not a model, introduces them."
          records: [epistemic.md#epi-rte-result-labeling, memory.md#mem-obj-analysis]
          note: "The accepted non-entailment finding establishes synthesis, not warranted explanatory acceptance."
        - scope: "Matching-file replacement, initial acquisition, legend export and opaque cache maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "Overwrite/acquisition alone does not establish semantic evolution, deduplication or invalidation; cache transformations are not recorded in sufficient detail. Optional pretrained-weight purge is excluded from learned outcome-memory curation."
      records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-obj-summary, memory.md#mem-obj-analysis, epistemic.md#epi-rte-result-labeling, runtime.md#rt-cmp-engine]
      note: "Consolidation and synthesis are supported locally; the remaining maintenance inventory does not support a complete operation classification."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Later CPU invocation requests record mappings and legend metadata"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend]
              note: "Analysis invocation explicitly loads the directory's matching files and legend; fulfilling this request is not an additional push."
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend]
          note: "Covers item-ID/bit mappings and consumed permutation metadata, not all stored fields."
        - scope: "Queued-model scheduling automatically consults retained summary existence"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-sweep-driver, runtime.md#rt-bap-summary-skip]
              note: "When a model key reaches a worker, fixed code supplies retained completion state to the skip decision without a request for summary content."
          records: [runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip]
          note: "The delivered part is the existence marker, not the JSON's descriptive payload."
        - scope: "Reader inspection of retained reporting artifacts"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
              note: "Published JSON and figures afford requested human inspection; no observed read or wired return to inference is claimed."
          records: [memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
          note: "Immediate plotting of the current mapping is excluded from later read-back."
        - scope: "Opaque dependency-cache reuse routes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "Adapter-visible reuse does not resolve the request/selection/delivery operations of every retained internal part."
      records: [runtime.md#rt-rte-record-analysis, runtime.md#rt-bap-summary-skip, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, runtime.md#rt-cmp-engine]
      note: "Pull analysis/reporting and automatic scheduling push coexist; cache alternatives remain unresolved."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Summary-marker push when a worker dequeues a model key"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-sweep-driver, runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip]
              note: "The queued model key chooses that model's summary path; this identity match selects the retained completion marker used by the skip consumer."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-bap-summary-skip, runtime.md#rt-obj-summary]
              note: "Within the selected path, existence alone supplies the completion signal, independent of numerical content, request compatibility or quality."
          records: [runtime.md#rt-rte-sweep-driver, runtime.md#rt-bap-summary-skip]
          note: "Trigger is the queued-model visit, input is model key plus file availability, selected part is its existence marker; no semantic relevance selector is established."
        - scope: "Explicit CPU loads and requested human reporting inspection"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-config-legend, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures]
          note: "These named operations are pull, so their glob/ID alignment and report filenames are not classified as push signals."
        - scope: "Potential push selection inside opaque dependency caches"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-engine, runtime.md#rt-cmp-roster-model]
          note: "Unresolved cache directions prevent treating this alternative as pull-only or assigning a selector from filenames alone."
      records: [runtime.md#rt-bap-summary-skip, runtime.md#rt-rte-sweep-driver, runtime.md#rt-rte-record-analysis, runtime.md#rt-cmp-engine]
      note: "Scheduling has an identified marker-selection chain; unresolved cache alternatives prevent full signal coverage."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic inference-outcome-to-summary write and later shell skip consumer"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-generation-grid, runtime.md#rt-rte-likelihood-grid, runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip]
              note: "Model execution outcomes feed automatic summary production; its durable existence changes collection on later launches. This is a behavior-shaping artifact route without parameter training or demonstrated improvement."
          records: [runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, runtime.md#rt-bap-summary-skip]
          note: "The raw-return to bits to summary to later skip chain is wired, not observed. The marker's content-insensitive consumer still changes later behavior."
        - scope: "Other retained records, aggregate/report outputs, legend, initialization/replacement and opaque cache alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-analysis, memory.md#mem-obj-fragility-figures, memory.md#mem-obj-config-legend, runtime.md#rt-cmp-engine]
          note: "These records do not establish another complete qualifying trace-fed behavior-shaping update chain. Reporting availability, provenance uncertainty and opaque internals do not provide the evidenced-absence record required for a local no."
      records: [runtime.md#rt-obj-summary, runtime.md#rt-bap-summary-skip, runtime.md#rt-rte-record-analysis, memory.md#mem-obj-analysis, runtime.md#rt-cmp-engine]
      note: "A supported local yes establishes a system-union yes, not complete learning coverage or improved capacity; no local or system-wide no is asserted."
    trace_source:
      assessment: partial
      units:
        - scope: "Original execution feedback feeding automatic model-summary production"
          assessment: known
          findings:
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-generation-grid, runtime.md#rt-rte-likelihood-grid, epistemic.md#epi-rte-gold-comparison, runtime.md#rt-obj-summary]
              note: "Generated-answer and continuation-scoring execution feedback from Engine calls becomes correctness bits and then summary content. Tool-traces classifies this execution-feedback origin, not a claim that the harness registers agent tools."
          records: [runtime.md#rt-rte-generation-grid, runtime.md#rt-rte-likelihood-grid, runtime.md#rt-obj-summary]
          note: "Static benchmark question/gold inputs also enter scoring, but are imported content rather than an additional trace-source category. Independent single-question frames are not session logs or linked trajectories."
        - scope: "Unresolved qualifying-write alternatives in other files, initialization/replacement and dependency caches"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-record-analysis, memory.md#mem-obj-analysis, memory.md#mem-obj-config-legend, runtime.md#rt-cmp-engine]
          note: "Without a completely assessed learning inventory, other trace sources cannot be declared inapplicable or inferred from cache names and file formats."
      records: [runtime.md#rt-rte-generation-grid, runtime.md#rt-rte-likelihood-grid, runtime.md#rt-obj-summary, runtime.md#rt-rte-record-analysis, runtime.md#rt-cmp-engine]
      note: "The summary route has classified execution-feedback input; other possible qualifying writes retain unresolved source coverage."
---

# fragility-grid memory profile

## Comparison rationale

The comparison boundary is accumulated measurement and reporting state, not every byte used by inference. The unchanged model parameters and static format instructions do not become learned memory merely because later calls reuse them. Conversely, opaque dependency caches remain unresolved alternatives rather than being classified from their path names or omitted to obtain complete coverage. Explicit outputs, their admission routes and these cache limits are established by [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), [RT-CMP-engine](runtime.md#rt-cmp-engine) and [RT-CMP-roster-model](runtime.md#rt-cmp-roster-model).

Summary existence is the consequential retained part for later collection. The model key selects a matching marker, and availability alone then determines a hard skip. Identifier selection and the coarse existence predicate are separate operations in that chain. This differs from CPU analysis explicitly requesting the bit mappings and legend. Neither the CPU's item-ID intersections nor its downstream tiny-subset comparison is unsolicited model-context retrieval ([RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip), [RT-RTE-sweep-driver](runtime.md#rt-rte-sweep-driver), [RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), [MEM-OBJ-config-legend](memory.md#mem-obj-config-legend)).

The summary chain supports wired trace learning in the profile's write-route sense: model-call outcomes become bits, automatic software produces a durable summary, and later shell operation depends on its retained existence. The learning force belongs to the update consumer; routing/enforcement belong to the later marker consumer. This does not establish a model parameter update, an improved capacity, or exercised self-improvement. The original inference execution feedback supports tool-traces even though this workflow has no agent tool registry. Imported gold is a separate non-trace input. No session-log, trajectory or environmental-event source is inferred merely from repeated calls ([RT-RTE-generation-grid](runtime.md#rt-rte-generation-grid), [RT-RTE-likelihood-grid](runtime.md#rt-rte-likelihood-grid), [EPI-RTE-gold-comparison](epistemic.md#epi-rte-gold-comparison), [RT-OBJ-summary](runtime.md#rt-obj-summary), [RT-BAP-summary-skip](runtime.md#rt-bap-summary-skip)).

Aggregation reduces measurement content; the broader manufactured-gap interpretations add claims. Thus consolidation and synthesis coexist without treating all statistical arithmetic as new explanatory knowledge. The latter mapping rests on the accepted non-entailment finding, not on the presence of fluent text. Retained aggregate and figure outputs afford human reporting but have no established later model-guidance route ([MEM-OBJ-analysis](memory.md#mem-obj-analysis), [MEM-OBJ-fragility-figures](memory.md#mem-obj-fragility-figures), [EPI-RTE-result-labeling](epistemic.md#epi-rte-result-labeling)).

The reconciliation supersedes the duplicate aggregate declaration with [MEM-OBJ-analysis](memory.md#mem-obj-analysis); all aggregate classifications use that canonical identity. The legend remains a distinct durable part of [RT-OBJ-config](runtime.md#rt-obj-config), and the figures remain distinct display outputs. No parent route is superseded by its narrower statistical or labeling parts.

Unknown file initialization/manual replacement prevents complete lineage and admission classification. Cache opacity prevents complete substrate, form, authority, maintenance and read-back classification. No accepted evidenced-absence declaration supports a local trace-learning no; missing qualifying chains therefore remain unresolved rather than becoming negative findings. A wired witness is retained despite those limits, and afforded reporting is not promoted to observed use. All bases describe accepted implementation or affordance, not verified activation or benefit ([RT-RTE-record-analysis](runtime.md#rt-rte-record-analysis), [RT-OBJ-records](runtime.md#rt-obj-records), [RT-OBJ-summary](runtime.md#rt-obj-summary), [RT-CMP-engine](runtime.md#rt-cmp-engine), [MEM-OBJ-analysis](memory.md#mem-obj-analysis)).

Source-read log: no additional source files were read. This profile uses only the supplied accepted members and their canonical records; it declares no records and adds no quotations or evidence.
