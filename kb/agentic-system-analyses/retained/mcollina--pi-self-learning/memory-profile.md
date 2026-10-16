---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "pi-self-learning memory comparison: trace-derived journals, canonical rules and ranking state, rendered views, process notes and later-consumer routes."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
source-identity: https://github.com/mcollina/pi-self-learning
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
memory-comparison:
  version: 2
  scope: "Accumulated daily reflections, canonical index text and ranking metadata, core and long-term renders, monthly summaries and process-local reflection notes; their initialization/migration, automatic updates, maintenance and later model/code consumers. Existing file content is included with unresolved original provenance and admission control. Branch conversations and tool results are original learning inputs, not extension-owned durable stores. Optional Git history is included as conditional retention, not a shipped read-back route. Excludes static boilerplates and consultation policy, ordinary settings and branch controls, enclosing-host transcript persistence and provider parameters: these are dependencies or configuration, not accumulated memory maintained by this extension."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Daily journal, canonical index text and ranking metadata, core, long-term and monthly current files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly]
              note: "UTF-8 Markdown and JSON files under the resolved project/global root; JSON encoding is not a separate database substrate."
          records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly]
          note: "Records enumerate both canonical parts and all rendered/summary file alternatives; unavailable contents do not obscure their implemented substrate."
        - scope: "Optional version history of accumulated memory files"
          assessment: known
          findings:
            - value: repo
              basis: wired
              records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
              note: "Configured Git initialization and commits retain file versions if successful; wiring is best effort, not observed durability."
          records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
          note: "Covers commit paths for reflection and both maintenance producers; no shipped history consumer is implied."
        - scope: "Process-local recent reflection notes"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-obj-runtime-notes]
              note: "Module array retains at most 30 shortened notes for later hooks in the same process."
          records: [runtime.md#rt-obj-runtime-notes]
          note: "This alternative is volatile and has no durable reload or branch/root key."
      records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
      note: "Inventory covers every extension-maintained accumulated object in scope. External model state and host transcript storage are not asserted as extension memory substrates."
    representational_form:
      assessment: known
      units:
        - scope: "Journal, rule, render, summary and note prose at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes]
              note: "Mistakes, fixes, rules, summaries and shortened notes receive their content effects through model interpretation."
          records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes]
          note: "Actual prose is unavailable, but the retained string and Markdown consumption paths are inspected; no opaque numerical payload occurs on these paths."
        - scope: "Index keys/kinds, numerical ranking metadata and file/date/note ordering at fixed-code consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, epistemic.md#epi-rte-index-migration]
              note: "Localized keys, counters, timestamps, kinds, paths and array order have fixed parse, merge, rank and selection rules; numbers here are not distributed parameters."
          records: [memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, epistemic.md#epi-rte-index-migration]
          note: "Separates access structure from model-interpreted text even when both occupy the same file."
      records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-context-injection, epistemic.md#epi-rte-index-migration]
      note: "All operative retained parts and consumption paths are represented; using a parametric completion model does not make its textual output parametric memory."
    lineage:
      assessment: partial
      units:
        - scope: "New reflection-derived daily prose and canonical rule candidates"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-rte-task-reflection, memory.md#mem-obj-branch-messages, memory.md#mem-obj-daily, memory.md#mem-obj-index-text]
              note: "Selected conversational turns and execution signals feed model reflection, optional repair, and admission into daily/index content."
          records: [runtime.md#rt-rte-task-reflection, memory.md#mem-obj-branch-messages, memory.md#mem-obj-daily, memory.md#mem-obj-index-text]
          note: "Covers the inspected new-content derivation, not all pre-existing file provenance or fidelity of generated statements."
        - scope: "Ranking metadata, normalized keys, rendered views, process fragments, monthly derivation and redistill rewrites"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-watchout-conversion]
              note: "Code computes metadata/views/fragments; models transform already retained daily/index content. This identifies derivation paths, not independent corroboration or known initial authorship."
          records: [memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-watchout-conversion]
          note: "Known subsequent compilation remains classifiable even when its input's original provenance is unknown."
        - scope: "Existing-index load and CORE fallback migration"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration]
              note: "Previously present index items or Markdown bullets enter active canonical state without an origin check."
          records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration, memory.md#mem-obj-daily]
          note: "Import mechanism is inspected; initial author, human/model control and derivation of legacy/handwritten content are unknown. Authored versus trace-derived initial lineage cannot be completed."
      records: [runtime.md#rt-rte-task-reflection, memory.md#mem-obj-branch-messages, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-index-migration, epistemic.md#epi-rte-watchout-conversion]
      note: "New extraction and subsequent transformations are supported; included existing-content provenance prevents complete lineage coverage."
    behavioral_authority:
      assessment: known
      units:
        - scope: "Retained prose and notes supplied to later foreground agents as historical evidence"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-memory-policy, runtime.md#rt-rte-context-injection, memory.md#mem-obj-daily, memory.md#mem-obj-core, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes]
              note: "Selected text is returned as historical context in a hidden custom message; knowledge authority here is not verified truth or demonstrated reliance."
          records: [runtime.md#rt-bap-memory-policy, runtime.md#rt-rte-context-injection, memory.md#mem-obj-daily, memory.md#mem-obj-core, memory.md#mem-obj-monthly, runtime.md#rt-obj-runtime-notes]
          note: "Covers automatic delivery; host application and changed answers remain unobserved."
        - scope: "Retained core, daily, monthly and long-term prose on requested external-agent consultation paths"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [runtime.md#rt-bap-memory-policy, memory.md#mem-obj-core, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-long-term-memory]
              note: "Policy names files for historical evidence or prior fixes; external file reading is afforded, not an extension-executed or observed retrieval."
          records: [runtime.md#rt-bap-memory-policy, memory.md#mem-obj-core, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-long-term-memory]
          note: "Long-term content belongs to this channel rather than the automatic bundle."
        - scope: "Retained prevention rules and watch-outs at later foreground interpretation"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [epistemic.md#epi-rte-watchout-conversion, memory.md#mem-obj-index-text, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, runtime.md#rt-rte-core-redistill]
              note: "Retained avoidance advice and imperative prevention rules can direct later conduct through rendered text. Actual output wording and adherence are unobserved; this is not enforcement."
          records: [epistemic.md#epi-rte-watchout-conversion, memory.md#mem-obj-index-text, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, runtime.md#rt-rte-core-redistill]
          note: "This is the retained advice's potential standing force, separate from the excluded static system-prompt consultation instructions."
        - scope: "Retained experience at reflection, monthly-summary and canonical-rule rewrite consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, runtime.md#rt-rte-month-summary, memory.md#mem-obj-index-text, runtime.md#rt-rte-core-redistill]
              note: "Session experience and retained derived prose feed updates to durable behavior-shaping memory. Authority at these update consumers is separate from downstream knowledge/instruction and does not establish improved capacity."
          records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, runtime.md#rt-rte-month-summary, memory.md#mem-obj-index-text, runtime.md#rt-rte-core-redistill]
          note: "Names the actual update consumers rather than inferring authority from storage alone."
        - scope: "Index content identity/kind and ranking metadata at rendering and redistill targeting"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, epistemic.md#epi-rte-core-ranking, runtime.md#rt-rte-core-redistill]
              note: "Scores, hits, age and kind balancing determine priority/membership; text keys determine repetition buckets and corresponding score updates."
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-index-text, memory.md#mem-obj-core, epistemic.md#epi-rte-index-migration]
              note: "Retained kind and parsed text select learning/watch-out rendering classes, and fallback CORE bullets determine reconstructed canonical input."
          records: [memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-index-migration, runtime.md#rt-rte-core-redistill]
          note: "Symbolic consumer effects are classified separately from prose interpretation; recurrence metadata is not a correctness criterion."
      records: [runtime.md#rt-bap-memory-policy, runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, memory.md#mem-obj-branch-messages, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, memory.md#mem-obj-long-term-memory, memory.md#mem-obj-monthly, epistemic.md#epi-rte-watchout-conversion, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-index-migration]
      note: "Coverage is of implemented or afforded consumers/effects, not actual use. Structural parsers and static policy are not accumulated validation criteria; no retained-memory enforcement authority is inferred from strict-mode wording."
    write_agency:
      assessment: partial
      units:
        - scope: "Reflection/repair admission, daily append, index/ranking updates, rendering and process-note admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-obj-runtime-notes, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-watchout-conversion]
              note: "Model proposal and software parse/normalization decide admission; no per-content operator decision. Manual reflection calls the same mechanism."
          records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-obj-runtime-notes, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-watchout-conversion]
          note: "Starting or enabling reflection does not make its generated content manually admitted."
        - scope: "Monthly summary admission, redistill replacement and migration/default admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-index-migration]
              note: "Code accepts nonempty summaries/mappings or parsed bullets; month/limit selection, preview and coarse batch confirmation are not approval of retained content."
          records: [runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-index-migration]
          note: "Known automatic import/admission remains distinct from unknown original creation of its inputs."
        - scope: "Original admission and replacement of pre-existing or externally edited memory files"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-index-text, memory.md#mem-obj-daily]
          note: "Files can be externally edited, but no actual operator content decision or initial control is recorded. Physical editability alone does not establish manual admission."
      records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-watchout-conversion, epistemic.md#epi-rte-index-migration, memory.md#mem-obj-index-text, memory.md#mem-obj-daily]
      note: "All shipped write mechanisms are classifiable; included initial/external content control remains unresolved, so the axis is not wholly known."
    curation_operations:
      assessment: partial
      units:
        - scope: "Reflection extraction, monthly summary production and shortened/runtime/rendered descendants"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-core, memory.md#mem-obj-monthly, runtime.md#rt-rte-month-summary]
              note: "Session material becomes selected mistakes/fixes; retained daily material feeds a bounded summary; first-item prefixes and selected core views reduce existing content. Wiring does not establish semantic faithfulness."
          records: [runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-core, memory.md#mem-obj-monthly, runtime.md#rt-rte-month-summary]
          note: "Classifies the extraction/reduction paths, not a claim that every generated statement is entailed by its input."
        - scope: "Normalized-key maintenance, recency-weighted core selection and redistill replacement"
          assessment: known
          findings:
            - value: dedup
              basis: wired
              records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-core-ranking, runtime.md#rt-rte-core-redistill]
              note: "Normalized equal keys merge entries and rewrite collisions; equivalence is lexical normalization, not semantic duplicate judgment."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-index-text, runtime.md#rt-rte-core-redistill, runtime.md#rt-rte-month-summary]
              note: "Matching canonical entries can be updated; redistill replaces selected rule text/keys, and regenerating a month overwrites its summary."
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-index-ranking, epistemic.md#epi-rte-core-ranking, runtime.md#rt-obj-runtime-notes]
              note: "Age lowers effective rank when selection runs; process FIFO removes old notes. Index content is not deleted by exclusion from core."
            - value: promote
              basis: wired
              records: [memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, epistemic.md#epi-rte-core-ranking]
              note: "Repetition increases scores and ranked/kind-balanced selection raises items into the default-delivered core view."
          records: [memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, epistemic.md#epi-rte-core-ranking, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-core-redistill, runtime.md#rt-rte-month-summary]
          note: "Implemented maintenance operations are independent of whether model rewrites preserve meaning."
        - scope: "Semantic novelty or withdrawal in model-generated reflection, monthly and redistill content"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-watchout-conversion]
          note: "Input/output proposition comparisons are unavailable. Synthesize cannot be established from a generation call, and requested preservation does not resolve semantic changes. A deterministic Avoid prefix is a policy conversion, not evidence of a novel truth-apt claim."
      records: [runtime.md#rt-rte-task-reflection, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-index-text, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, epistemic.md#epi-rte-core-ranking, epistemic.md#epi-rte-watchout-conversion]
      note: "Positive code-supported transformations coexist with unresolved semantic operations. No complete operation list or synthesis/semantic-invalidation negative is asserted."
    read_back_direction:
      assessment: known
      units:
        - scope: "Unrequested future-turn notes/file supply and selected retained content supplied to maintenance completions"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
              note: "Hook supplies notes/files without a foreground request; maintenance code selects retained journal/rule inputs for separate models rather than waiting for those models to retrieve them."
          records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
          note: "Operator-started maintenance still includes a distinct automatic selection and delivery operation to its model."
        - scope: "Update-code requests for existing canonical state and explicit month/redistill requests for retained input"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
              note: "Update code loads the current index/fallback; commands request a month or rule scope. Requested acquisition is distinct from subsequent unsolicited model-input supply."
          records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
          note: "Files are actual later update inputs, not merely storage capabilities."
        - scope: "Foreground on-demand consultation of core, daily, monthly and long-term paths"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [runtime.md#rt-bap-memory-policy, memory.md#mem-obj-core, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-long-term-memory]
              note: "Host agent is instructed to consult files when relevant or stuck; no extension tool performs or verifies those reads."
          records: [runtime.md#rt-bap-memory-policy, memory.md#mem-obj-core, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-long-term-memory]
          note: "Affordance remains weaker than wired delivery and is not upgraded by the automatic bundle witness."
      records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, runtime.md#rt-bap-memory-policy, memory.md#mem-obj-index-text, memory.md#mem-obj-core, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-long-term-memory, epistemic.md#epi-rte-index-migration]
      note: "The inventory separates request, automatic selection and delivery within each chain. Git history has no shipped later consumer; current-file and note paths cover the recorded alternatives."
    read_back_signal:
      assessment: known
      units:
        - scope: "Before-agent-start note and file push"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core]
              note: "Enabled hook uses include flags, available files, note-tail counts, latest dated filenames and prefix budgets; core membership was previously rank/kind selected. No query-content matching occurs."
          records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core]
          note: "Selected parts are note fragments and configured core/daily/monthly prefixes; a fixed path or chronological filename ordering is not inferred lexical relevance."
        - scope: "Monthly command's selected daily-file push to summary model"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-month-summary, memory.md#mem-obj-monthly]
              note: "Requested/default YYYY-MM is matched against daily filename prefixes to select that month's retained files for model input. This is an actual identity filter, not merely a path printed to the operator."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-month-summary, memory.md#mem-obj-monthly]
              note: "Matching files are sorted, concatenated and prefix-limited to 180000 characters before supply."
          records: [runtime.md#rt-rte-month-summary, memory.md#mem-obj-monthly]
          note: "The upstream month request supplies the selector input; the downstream model receives selected retained prose automatically."
        - scope: "Redistill command's selected canonical-rule push to rewrite model"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-core-redistill, memory.md#mem-obj-index-ranking]
              note: "Invocation selects score-ranked targets under an optional positive limit, then supplies chunks of eight. Transient IDs map returned rewrites, not semantic or identity targeting of the push."
          records: [runtime.md#rt-rte-core-redistill, memory.md#mem-obj-index-ranking]
          note: "Selected retained part is rule text/kind; ranking metadata chooses targets but is not supplied as model evidence."
      records: [runtime.md#rt-rte-context-injection, runtime.md#rt-obj-runtime-notes, memory.md#mem-obj-index-ranking, memory.md#mem-obj-core, runtime.md#rt-rte-month-summary, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill]
      note: "All recorded push operations have named triggers, selectors and delivered parts. Pull path identifiers alone add no signal finding."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic or manually initiated reflection over branch activity, including repair and durable daily/index/render descendants"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, runtime.md#rt-rte-context-injection]
              note: "Software/model admission transforms activity traces into durable mistake/fix memory with later context/update consumers. Manual invocation does not make admission manual."
          records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, runtime.md#rt-rte-context-injection]
          note: "A wired trace-learning route does not establish observed use, improved performance or parameter training."
        - scope: "Monthly summary and redistill over reflection-derived retained material"
          assessment: partial
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-index-text, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, runtime.md#rt-rte-context-injection]
              note: "When supplied retained inputs are reflection-derived, automatic summaries/replacements carry that experience into durable artifacts for later consumers."
          records: [memory.md#mem-obj-daily, memory.md#mem-obj-monthly, memory.md#mem-obj-index-text, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
          note: "Inputs may instead include legacy/externally edited prose of unknown origin; the records cannot classify every maintenance input as trace-derived."
        - scope: "Existing-content initialization and CORE fallback with unresolved original source"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration]
          note: "Automatic import is known, but original activity provenance is not. Neither a qualifying trace-fed write nor a local no can be established for all imported content."
        - scope: "Process-local note as a standalone output"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-obj-runtime-notes, runtime.md#rt-rte-task-reflection]
          note: "The note has later consumers but no durable persistence/reload. The encompassing reflection route qualifies through its durable siblings, not through this volatile fragment alone."
      records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-monthly, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, runtime.md#rt-rte-context-injection, epistemic.md#epi-rte-index-migration, runtime.md#rt-obj-runtime-notes]
      note: "Positive trace-fed routes coexist with unresolved legacy inputs. No system-wide no or observed-learning claim follows from missing execution evidence."
    trace_source:
      assessment: partial
      units:
        - scope: "Original inputs to new reflection writes and their trace-derived maintenance descendants"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill]
              note: "Recorded user/assistant conversational turns enter reflection; daily/index descendants carry that source into monthly and redistill transformations."
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill]
              note: "Recorded tool messages and separately extracted permission/blocking error feedback feed the same durable reflection path and derived maintenance inputs."
          records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-monthly, runtime.md#rt-rte-core-redistill]
          note: "Classifies original trace content, not JSON/Markdown wrappers. A lifecycle callback triggering extraction does not add event-streams, and conversational ordering alone does not establish state/action/outcome trajectories."
        - scope: "Original source of imported/legacy daily and canonical content used in maintenance"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-daily, memory.md#mem-obj-index-text, epistemic.md#epi-rte-index-migration, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill]
          note: "No original files/provenance are supplied. Unknown material may or may not be trace-derived, preventing a complete source union for all included maintenance writes."
      records: [memory.md#mem-obj-branch-messages, runtime.md#rt-rte-task-reflection, memory.md#mem-obj-daily, memory.md#mem-obj-index-text, memory.md#mem-obj-monthly, runtime.md#rt-rte-month-summary, runtime.md#rt-rte-core-redistill, epistemic.md#epi-rte-index-migration]
      note: "Session and tool sources are supported on the inspected reflection branch; unresolved initial provenance stays local rather than being made inapplicable by that witness."
---

# pi-self-learning memory profile

## Comparison rationale

The profile classifies extension-maintained memory, not the entire host or completion provider. The retained-object inventory is the daily journal, canonical text and ranking parts, core and long-term views, monthly summaries and process-local notes. These records distinguish raw branch input from derived memory and distinguish canonical content from its lossy displays ([MEM-OBJ-branch-messages](memory.md#mem-obj-branch-messages), [MEM-OBJ-daily](memory.md#mem-obj-daily), [MEM-OBJ-index-text](memory.md#mem-obj-index-text), [MEM-OBJ-index-ranking](memory.md#mem-obj-index-ranking), [MEM-OBJ-core](memory.md#mem-obj-core), [MEM-OBJ-long-term-memory](memory.md#mem-obj-long-term-memory), [MEM-OBJ-monthly](memory.md#mem-obj-monthly), [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes)). Optional Git attempts support a conditional repository substrate, not an observed backup or read-back from commit history ([RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)).

Reconciliation supersedes the epistemic conversation-signals object with the memory branch-messages object, the epistemic monthly-text object with the memory monthly object, and the epistemic full-history claim with the memory complete-history claim. Citations use those canonical memory records. The parsed-reflection and aggregate-index containers remain valid, but classification uses their finer durable parts where consumers differ. These supersessions change citation identity, not evidence strength. The unresolved registration-count conflict does not change any classified memory route; this profile asserts no command count ([MEM-CLM-complete-history](memory.md#mem-clm-complete-history), [RT-RTE-runtime-controls](runtime.md#rt-rte-runtime-controls)).

Knowledge, instruction and learning describe different consumers. Historical prose is supplied to a foreground model; prevention advice can direct its conduct; retained experience also feeds further durable updates. None establishes truth, adherence or improved capacity. Static consultation instructions are excluded as shipped policy, and strict-mode wording supplies no retained-memory enforcement finding ([RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy), [EPI-RTE-watchout-conversion](epistemic.md#epi-rte-watchout-conversion), [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)). Symbolic kind and ranking state act earlier at code consumers, so they retain routing/ranking findings independently of downstream prose authority ([MEM-OBJ-index-text](memory.md#mem-obj-index-text), [MEM-OBJ-index-ranking](memory.md#mem-obj-index-ranking)).

Extraction, summarization, prefix retention, normalized-key merging, age downweighting and core promotion support curation findings. They do not resolve whether model text introduces new propositions or preserves every input claim. In particular, an Avoid prefix is an implemented policy conversion, not a semantic check; redistill's preservation request does not establish successful preservation. That unresolved semantic branch keeps curation partial without suppressing implemented operations ([EPI-RTE-watchout-conversion](epistemic.md#epi-rte-watchout-conversion), [EPI-RTE-core-ranking](epistemic.md#epi-rte-core-ranking), [RT-RTE-month-summary](runtime.md#rt-rte-month-summary), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill)).

Requested acquisition and unsolicited model-input delivery can occur in one chain. A requested month supplies an identity selector that actually filters daily filenames before the summary model receives their content. Recency, rank, include flags and prefix budgets remain coarse signals; printing a file path or assigning rewrite IDs does not itself establish identifier-targeted push. Foreground consultation is an afforded pull route rather than another wired retrieval tool ([RT-RTE-month-summary](runtime.md#rt-rte-month-summary), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill), [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy)).

Trace learning is supported by automatic admission into durable reflection artifacts and later consumers, including when a human starts reflection. Original inputs include conversational turns and tool feedback. Later summaries and rewrites can inherit those sources through retained reflections, but legacy/imported inputs have unknown origin and admission control. This prevents complete lineage, write-agency and trace-source coverage. No model-weight learning or observed improvement is inferred ([MEM-OBJ-branch-messages](memory.md#mem-obj-branch-messages), [MEM-OBJ-daily](memory.md#mem-obj-daily), [MEM-OBJ-index-text](memory.md#mem-obj-index-text), [EPI-RTE-index-migration](epistemic.md#epi-rte-index-migration), [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model)).

Source-read log: no frozen-source files were read for this mapping. All classifications use the supplied accepted records and their annotations; no records, quotations or new evidence were added.
