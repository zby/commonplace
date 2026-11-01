---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Ultimate memory comparison: root project memory, retained work/context derivatives and chapter carry, with opaque alternatives retained."
run-id: "AAS-2026-11-01-ultimate-f5179584de71-01"
source-identity: "https://github.com/HazAT/ultimate"
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
memory-comparison:
  version: 2
  scope: "Included: accumulated root memory and metadata; raw work history and derived tally/continuation summaries; Store and display summaries; Todos/Goals; saved automation state; cross-chapter seed and afforded adopted code/instruction artifacts. External default checkpoint/provider state and less-inspected script/extension consumers remain unresolved alternatives. Excluded: unchanged shipped static instructions, ordinary transient current-run values and model weights merely used for inference. No complete inventory of all persistent bytes or context injections is claimed."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Root memory and addresses; tally/raw entries and abstracts; Store; call summaries; Todos; Goals; task/seed receipts; saved automation state"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-memory-addresses"
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-obj-store"
                - "memory.md#mem-obj-call-summaries"
                - "memory.md#mem-obj-todos"
                - "memory.md#mem-obj-goals"
                - "memory.md#mem-obj-seed"
                - "runtime.md#rt-rte-automation-run"
              note: "Logical documents and entry/task state use active-chapter SQLite through the external harness. JSON is encoding, not an extra substrate."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-memory-addresses"
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-obj-store"
            - "memory.md#mem-obj-call-summaries"
            - "memory.md#mem-obj-todos"
            - "memory.md#mem-obj-goals"
            - "memory.md#mem-obj-seed"
            - "runtime.md#rt-rte-automation-run"
          note: "Logical documents and entry/task state use active-chapter SQLite through the external harness. JSON is encoding, not an extra substrate."
        -
          scope: "Cross-chapter seed snapshot"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-seed"
              note: "seed.json is a filesystem snapshot, distinct from destination application receipts."
          records:
            - "memory.md#mem-obj-seed"
          note: "seed.json is a filesystem snapshot, distinct from destination application receipts."
        -
          scope: "Adopted memory-review code/instruction artifacts"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
                - "runtime.md#rt-rte-change-admission"
              note: "The procedure affords codifying memories in durable source/instruction files through normal change branches."
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
                - "runtime.md#rt-rte-change-admission"
              note: "The procedure affords codifying memories in durable source/instruction files through normal change branches."
          records:
            - "memory.md#mem-rte-review-memory"
            - "runtime.md#rt-rte-change-admission"
          note: "The procedure affords codifying memories in durable source/instruction files through normal change branches."
        -
          scope: "External default compaction and provider-held continuation/update state"
          assessment: "uninspected"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "runtime.md#rt-cmp-provider-models"
            - "memory.md#mem-cmp-jev"
          note: "Local integration does not expose default checkpoint payload, provider retention or update internals; no complete classification of this alternative."
      records:
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-memory-addresses"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-obj-call-summaries"
        - "memory.md#mem-obj-todos"
        - "memory.md#mem-obj-goals"
        - "memory.md#mem-obj-seed"
        - "runtime.md#rt-rte-automation-run"
        - "memory.md#mem-rte-review-memory"
        - "runtime.md#rt-rte-change-admission"
        - "runtime.md#rt-rte-context-return"
        - "runtime.md#rt-cmp-provider-models"
        - "memory.md#mem-cmp-jev"
      note: "Known local documents/files and afforded codification do not classify opaque external retained state or the unaudited archive lifecycle."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Memory lines/bodies, work transcripts, abstracts, continuation summaries, seed handoff, to-do text and goal text/reasons at model/human consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory"
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
                - "memory.md#mem-obj-seed"
                - "memory.md#mem-obj-todos"
                - "memory.md#mem-obj-goals"
              note: "Text receives consequences through model or human interpretation; stored JSON wrappers do not change that form."
          records:
            - "memory.md#mem-obj-memory"
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
            - "memory.md#mem-obj-seed"
            - "memory.md#mem-obj-todos"
            - "memory.md#mem-obj-goals"
          note: "Text receives consequences through model or human interpretation; stored JSON wrappers do not change that form."
        -
          scope: "Memory addresses; tally visibility/watermarks; Store JSON in scripts; call effect flags; task/goal status; seed and automation settings at fixed-rule consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-addresses"
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-obj-store"
                - "memory.md#mem-obj-call-summaries"
                - "memory.md#mem-obj-todos"
                - "memory.md#mem-obj-goals"
                - "memory.md#mem-obj-seed"
                - "runtime.md#rt-rte-automation-run"
              note: "Localized keys, kinds, flags, counters and structured values are read by code. Store strings emitted to a model can instead carry natural-language content."
          records:
            - "memory.md#mem-obj-memory-addresses"
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-obj-store"
            - "memory.md#mem-obj-call-summaries"
            - "memory.md#mem-obj-todos"
            - "memory.md#mem-obj-goals"
            - "memory.md#mem-obj-seed"
            - "runtime.md#rt-rte-automation-run"
          note: "Localized keys, kinds, flags, counters and structured values are read by code. Store strings emitted to a model can instead carry natural-language content."
        -
          scope: "Natural-language call display lines at the display consumer"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-call-summaries"]
              note: "Model-derived prose lines serve human display; they are not established foreground guidance or full execution payloads."
          records: ["memory.md#mem-obj-call-summaries"]
          note: "The record establishes the prose display part separately from the symbolic effect flags already inventoried."
        -
          scope: "External default compaction and provider-held continuation/update state"
          assessment: "uninspected"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "runtime.md#rt-cmp-provider-models"
            - "memory.md#mem-cmp-jev"
          note: "Local integration does not expose default checkpoint payload, provider retention or update internals; no complete classification of this alternative."
      records:
        - "memory.md#mem-obj-memory"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-obj-seed"
        - "memory.md#mem-obj-todos"
        - "memory.md#mem-obj-goals"
        - "memory.md#mem-obj-memory-addresses"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-obj-call-summaries"
        - "runtime.md#rt-rte-automation-run"
        - "runtime.md#rt-cmp-provider-models"
        - "memory.md#mem-cmp-jev"
      note: "Local prose and fixed-rule parts are separated; opaque external payloads cannot be classified from display summaries. Inference weights are not asserted to be accumulated memory merely because a provider is called."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Explicit root memory, to-do/goal text, saved prompts and prepared handoff/learned lines"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-edit"
                - "memory.md#mem-obj-todos"
                - "memory.md#mem-obj-goals"
                - "memory.md#mem-rte-chapter-seed"
                - "runtime.md#rt-rte-automation-run"
              note: "Models/users supply these texts. Seed construction copies authored handoff rather than generating it."
          records:
            - "memory.md#mem-rte-memory-edit"
            - "memory.md#mem-obj-todos"
            - "memory.md#mem-obj-goals"
            - "memory.md#mem-rte-chapter-seed"
            - "runtime.md#rt-rte-automation-run"
          note: "Models/users supply these texts. Seed construction copies authored handoff rather than generating it."
        -
          scope: "Landing-derived memories; branch abstracts; local compaction, side-chat and optional rewind summaries"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
              note: "Selected activity/history feeds retained derivatives; this does not establish faithful preservation or novelty."
          records:
            - "memory.md#mem-rte-landing-distil"
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
          note: "Selected activity/history feeds retained derivatives; this does not establish faithful preservation or novelty."
        -
          scope: "Deterministic catch-up notes and cross-chapter seed metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tally-catchup"
                - "memory.md#mem-rte-chapter-seed"
              note: "Code selects/formats already retained parts; compilation/copy does not create factual warrant."
          records:
            - "memory.md#mem-rte-tally-catchup"
            - "memory.md#mem-rte-chapter-seed"
          note: "Code selects/formats already retained parts; compilation/copy does not create factual warrant."
        -
          scope: "Call-summary model-derived display lines, symbolic effect flags and script-header fallback"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-summaries"
          note: "The record distinguishes model-derived lines and memoized receipts from effect flags and the fallback header, but does not establish their complete derivation paths or original inputs. No single deterministic lineage is assigned to this mixed branch; catch-up and seed evidence cannot resolve it."
        -
          scope: "External web content retained in conversation tool results"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-web-acquisition"
              note: "Imported excerpts/pages keep URL labels but extraction and truncation can degrade fidelity."
          records:
            - "epistemic.md#epi-rte-web-acquisition"
          note: "Imported excerpts/pages keep URL labels but extraction and truncation can degrade fidelity."
        -
          scope: "Arbitrary Store values and actual initial/deployed memory provenance"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-store"
            - "memory.md#mem-obj-memory"
          note: "Script-supplied values and absent deployed corpus do not reveal every original derivation; known subsequent paths do not settle initialization."
        -
          scope: "External default compaction and provider-held continuation/update state"
          assessment: "uninspected"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "runtime.md#rt-cmp-provider-models"
            - "memory.md#mem-cmp-jev"
          note: "Local integration does not expose default checkpoint payload, provider retention or update internals; no complete classification of this alternative."
      records:
        - "memory.md#mem-rte-memory-edit"
        - "memory.md#mem-obj-todos"
        - "memory.md#mem-obj-goals"
        - "memory.md#mem-rte-chapter-seed"
        - "runtime.md#rt-rte-automation-run"
        - "memory.md#mem-rte-landing-distil"
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-rte-tally-catchup"
        - "memory.md#mem-obj-call-summaries"
        - "epistemic.md#epi-rte-web-acquisition"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-obj-memory"
        - "runtime.md#rt-cmp-provider-models"
        - "memory.md#mem-cmp-jev"
      note: "Supported derivations coexist with unknown initialization, arbitrary script values, mixed call-summary derivations and external provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Project memory and derived history at branch, standing, summary and continuation model consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-memory-guidance"
                - "memory.md#mem-rte-memory-read"
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-tally-catchup"
              note: "Delivered content supplies context/reference; delivery alone is not obedience."
          records:
            - "memory.md#mem-bap-memory-guidance"
            - "memory.md#mem-rte-memory-read"
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-tally-catchup"
          note: "Delivered content supplies context/reference; delivery alone is not obedience."
        -
          scope: "Retained memory directions and open-goal authorization/criteria at standing Ultimate"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-bap-memory-guidance"
                - "memory.md#mem-rte-operational-notes"
                - "epistemic.md#epi-rte-goal-authority"
              note: "Recalled applicable guidance and goal policy direct future work through natural-language interpretation, not a compulsory action gate."
          records:
            - "memory.md#mem-bap-memory-guidance"
            - "memory.md#mem-rte-operational-notes"
            - "epistemic.md#epi-rte-goal-authority"
          note: "Recalled applicable guidance and goal policy direct future work through natural-language interpretation, not a compulsory action gate."
        -
          scope: "Retained memory lines at relevance classifier and subsequent ranking selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recall-message"
                - "epistemic.md#epi-rte-recall-selection"
                - "epistemic.md#epi-rte-recall-injection"
              note: "Memory-line text affects relative relevance probabilities; fixed threshold/top-three code uses the result. No retained ranking policy or truth probability is inferred."
          records:
            - "memory.md#mem-rte-recall-message"
            - "epistemic.md#epi-rte-recall-selection"
            - "epistemic.md#epi-rte-recall-injection"
          note: "Memory-line text affects relative relevance probabilities; fixed threshold/top-three code uses the result. No retained ranking policy or truth probability is inferred."
        -
          scope: "Retained traces/abstracts and current memory at automatic durable-update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
              note: "Experience supplies a retained behavior-shaping derivative. Learning authority here does not mean measured capacity improvement."
          records:
            - "memory.md#mem-rte-landing-distil"
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
          note: "Experience supplies a retained behavior-shaping derivative. Learning authority here does not mean measured capacity improvement."
        -
          scope: "Seen baselines, entry kinds/anchors, goal states and saved automation configurations at code consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-rte-tally-catchup"
                - "memory.md#mem-obj-goals"
                - "runtime.md#rt-rte-automation-run"
                - "memory.md#mem-obj-seed"
              note: "Retained state selects new input windows, eligible work and later scheduler operations."
          records:
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-rte-tally-catchup"
            - "memory.md#mem-obj-goals"
            - "runtime.md#rt-rte-automation-run"
            - "memory.md#mem-obj-seed"
          note: "Retained state selects new input windows, eligible work and later scheduler operations."
        -
          scope: "Existing slug membership/capacity and stored goal/status constraints at admission code"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-checks"
                - "memory.md#mem-rte-memory-edit"
                - "epistemic.md#epi-rte-goal-authority"
              note: "Current retained map/state supplies applicability criteria and an enforced veto on invalid operations; static schema code itself is not classified as acquired memory."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-checks"
                - "memory.md#mem-rte-memory-edit"
                - "epistemic.md#epi-rte-goal-authority"
              note: "Current retained map/state supplies applicability criteria and an enforced veto on invalid operations; static schema code itself is not classified as acquired memory."
          records:
            - "epistemic.md#epi-rte-memory-checks"
            - "memory.md#mem-rte-memory-edit"
            - "epistemic.md#epi-rte-goal-authority"
          note: "Current retained map/state supplies applicability criteria and an enforced veto on invalid operations; static schema code itself is not classified as acquired memory."
        -
          scope: "Arbitrary Store payload effects and untraced external consumers"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-store"
            - "memory.md#mem-cmp-jev"
            - "runtime.md#rt-cmp-provider-models"
          note: "Loading JSON into a script does not establish every later effect; opaque provider state is not resolved by local guidance."
      records:
        - "memory.md#mem-bap-memory-guidance"
        - "memory.md#mem-rte-memory-read"
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-tally-catchup"
        - "memory.md#mem-rte-operational-notes"
        - "epistemic.md#epi-rte-goal-authority"
        - "memory.md#mem-rte-recall-message"
        - "epistemic.md#epi-rte-recall-selection"
        - "epistemic.md#epi-rte-recall-injection"
        - "memory.md#mem-rte-landing-distil"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-obj-goals"
        - "runtime.md#rt-rte-automation-run"
        - "memory.md#mem-obj-seed"
        - "epistemic.md#epi-rte-memory-checks"
        - "memory.md#mem-rte-memory-edit"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-cmp-jev"
        - "runtime.md#rt-cmp-provider-models"
      note: "Actual consumers establish distinct forces. Display-only call lines are not silently promoted to agent guidance; external and arbitrary-script effects remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model remember, landing distillation, abstracts, local compaction, catch-up, script Store commits and model task/goal updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-edit"
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-tally-catchup"
                - "memory.md#mem-obj-store"
                - "memory.md#mem-rte-operational-notes"
              note: "Software/model admission does not require a per-content operator decision; launching work or choosing summary injection does not manually approve each generated sentence."
          records:
            - "memory.md#mem-rte-memory-edit"
            - "memory.md#mem-rte-landing-distil"
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-tally-catchup"
            - "memory.md#mem-obj-store"
            - "memory.md#mem-rte-operational-notes"
          note: "Software/model admission does not require a per-content operator decision; launching work or choosing summary injection does not manually approve each generated sentence."
        -
          scope: "User forget, direct user task edits and user goal start"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-edit"
                - "memory.md#mem-rte-operational-notes"
                - "epistemic.md#epi-rte-goal-authority"
              note: "Explicit human actions choose deletion, task content or the retained goal authorization."
          records:
            - "memory.md#mem-rte-memory-edit"
            - "memory.md#mem-rte-operational-notes"
            - "epistemic.md#epi-rte-goal-authority"
          note: "Explicit human actions choose deletion, task content or the retained goal authorization."
        -
          scope: "Ordinary review adoption with user-chosen operations"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
              note: "Instructions call for user choice before Ultimate applies chosen operations."
          records:
            - "memory.md#mem-rte-review-memory"
          note: "Instructions call for user choice before Ultimate applies chosen operations."
        -
          scope: "Hands-off review adoption"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
                - "epistemic.md#epi-rte-goal-authority"
              note: "Goal policy affords Ultimate making proposal decisions instead of the user."
          records:
            - "memory.md#mem-rte-review-memory"
            - "epistemic.md#epi-rte-goal-authority"
          note: "Goal policy affords Ultimate making proposal decisions instead of the user."
        -
          scope: "Seed construction/application following user transition"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chapter-seed"
              note: "Code selects and directly installs carried content; a human transition gate is not independent per-memory approval."
          records:
            - "memory.md#mem-rte-chapter-seed"
          note: "Code selects and directly installs carried content; a human transition gate is not independent per-memory approval."
        -
          scope: "Generic extension API content admission and external/default compactor"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-rte-memory-edit"
            - "runtime.md#rt-rte-context-return"
          note: "API caller identity does not establish human control; external default content admission is not inspected."
      records:
        - "memory.md#mem-rte-memory-edit"
        - "memory.md#mem-rte-landing-distil"
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-tally-catchup"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-rte-operational-notes"
        - "epistemic.md#epi-rte-goal-authority"
        - "memory.md#mem-rte-review-memory"
        - "memory.md#mem-rte-chapter-seed"
      note: "Multiple admission mechanisms coexist; neither standing caller checks nor a user chapter transition establish universal manual admission."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Conversation abstracts, local compaction, side-chat and optional rewind summaries"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
              note: "Selected retained history is compressed into a smaller continuation/coordination representation; raw history can remain."
          records:
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
          note: "Selected retained history is compressed into a smaller continuation/coordination representation; raw history can remain."
        -
          scope: "Existing memory overwrite through explicit edits and landing operations"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-edit"
                - "memory.md#mem-rte-landing-distil"
                - "epistemic.md#epi-rte-memory-retention"
              note: "Implemented update operations revise existing retained entries; generated content remains unwarranted by structure alone."
          records:
            - "memory.md#mem-rte-memory-edit"
            - "memory.md#mem-rte-landing-distil"
            - "epistemic.md#epi-rte-memory-retention"
          note: "Implemented update operations revise existing retained entries; generated content remains unwarranted by structure alone."
        -
          scope: "Cross-root seed collision resolution"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-chapter-seed"
          note: "Timestamp selection resolves same-slug collisions and directly installs one survivor. The record does not establish duplicate or near-duplicate content; differing root-specific claims can share a key. This mechanism establishes no controlled curation operation."
        -
          scope: "Bounded completed Todos and call display history"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todos"
                - "memory.md#mem-obj-call-summaries"
              note: "Old completed/display entries are dropped beyond explicit retention caps; this does not erase full raw call transcripts."
          records:
            - "memory.md#mem-obj-todos"
            - "memory.md#mem-obj-call-summaries"
          note: "Old completed/display entries are dropped beyond explicit retention caps; this does not erase full raw call transcripts."
        -
          scope: "Review proposals for duplicate cleanup and revision"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
              note: "Procedure affords evidence-directed cleanup; requested transformations are not observed executed operations."
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-review-memory"
              note: "Procedure affords evidence-directed cleanup; requested transformations are not observed executed operations."
          records:
            - "memory.md#mem-rte-review-memory"
          note: "Procedure affords evidence-directed cleanup; requested transformations are not observed executed operations."
        -
          scope: "Landing model semantic transformation and arbitrary Store scripts/default compactor"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "epistemic.md#epi-rte-landing-candidates"
            - "memory.md#mem-obj-store"
            - "runtime.md#rt-rte-context-return"
          note: "Landing may copy, compress or infer; no candidate identifies entailment or a new claim, so synthesis is not established. Arbitrary scripts and default compaction cannot complete the operation inventory."
      records:
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-rte-memory-edit"
        - "memory.md#mem-rte-landing-distil"
        - "epistemic.md#epi-rte-memory-retention"
        - "memory.md#mem-rte-chapter-seed"
        - "memory.md#mem-obj-todos"
        - "memory.md#mem-obj-call-summaries"
        - "memory.md#mem-rte-review-memory"
        - "epistemic.md#epi-rte-landing-candidates"
        - "memory.md#mem-obj-store"
      note: "Implemented transformations are classified separately from requested cleanup. Deleting latest memory is not asserted to be history-preserving invalidation, nor is a receipt check semantic deduplication."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested memory lookup, entries/search/history and Store load"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-read"
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-obj-store"
                - "runtime.md#rt-rte-browser-input"
                - "runtime.md#rt-rte-codemode-tools"
              note: "Consumer requests retained material; exact-slug/file identity does not turn requested delivery into push."
          records:
            - "memory.md#mem-rte-memory-read"
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-obj-store"
            - "runtime.md#rt-rte-browser-input"
            - "runtime.md#rt-rte-codemode-tools"
          note: "Consumer requests retained material; exact-slug/file identity does not turn requested delivery into push."
        -
          scope: "Root branch brief, message recall, catch-up and operational notes"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-read"
                - "memory.md#mem-rte-recall-message"
                - "memory.md#mem-rte-tally-catchup"
                - "memory.md#mem-rte-operational-notes"
              note: "Automatic selectors supply retained material without the receiving model asking for those particular parts."
          records:
            - "memory.md#mem-rte-memory-read"
            - "memory.md#mem-rte-recall-message"
            - "memory.md#mem-rte-tally-catchup"
            - "memory.md#mem-rte-operational-notes"
          note: "Automatic selectors supply retained material without the receiving model asking for those particular parts."
        -
          scope: "Continuation summaries and chapter waking/installed memory"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
                - "memory.md#mem-rte-chapter-seed"
              note: "User may trigger the operation, but software supplies the selected derivative to the later invocation."
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
            - "memory.md#mem-rte-chapter-seed"
          note: "User may trigger the operation, but software supplies the selected derivative to the later invocation."
        -
          scope: "Additional external/default and untraced extension deliveries"
          assessment: "uninspected"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-obj-store"
            - "runtime.md#rt-rte-automation-run"
          note: "Local routes do not exhaust opaque context assembly or every later script/extension consumer."
      records:
        - "memory.md#mem-rte-memory-read"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-obj-store"
        - "runtime.md#rt-rte-browser-input"
        - "runtime.md#rt-rte-codemode-tools"
        - "memory.md#mem-rte-recall-message"
        - "memory.md#mem-rte-tally-catchup"
        - "memory.md#mem-rte-operational-notes"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-rte-chapter-seed"
        - "runtime.md#rt-rte-automation-run"
      note: "Both requested retrieval and unsolicited context supply are established; incomplete alternative coverage is retained."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Root-branch brief, summary replacement, open-work notes and chapter carry"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-read"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-operational-notes"
                - "memory.md#mem-rte-chapter-seed"
                - "memory.md#mem-rte-rewind-context"
              note: "Branch/reset/transition/input triggers select available root index, recent landings, summary or eligible/open state by presence/status/recency; no semantic task targeting is inferred."
          records:
            - "memory.md#mem-rte-memory-read"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-operational-notes"
            - "memory.md#mem-rte-chapter-seed"
            - "memory.md#mem-rte-rewind-context"
          note: "Branch/reset/transition/input triggers select available root index, recent landings, summary or eligible/open state by presence/status/recency; no semantic task targeting is inferred."
        -
          scope: "Message-triggered recall of root memory bodies"
          assessment: "known"
          findings:
            -
              value: "inferred-judgment"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recall-message"
                - "epistemic.md#epi-rte-recall-selection"
              note: "Incoming message prefix plus all memory lines feed probabilistic relevance judgment; threshold/top-three selects bodies. Slug response keys label judged choices, not an independent identifier-match signal."
          records:
            - "memory.md#mem-rte-recall-message"
            - "epistemic.md#epi-rte-recall-selection"
          note: "Incoming message prefix plus all memory lines feed probabilistic relevance judgment; threshold/top-three selects bodies. Slug response keys label judged choices, not an independent identifier-match signal."
        -
          scope: "Idle catch-up by changed tally and Git state"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tally-catchup"
              note: "New-entry/budget/recency selection is coarse. Workspace diff or recorded edit/write paths provide identity-based overlap targeting for commit/activity priority; this is not semantic conflict detection."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tally-catchup"
              note: "New-entry/budget/recency selection is coarse. Workspace diff or recorded edit/write paths provide identity-based overlap targeting for commit/activity priority; this is not semantic conflict detection."
          records:
            - "memory.md#mem-rte-tally-catchup"
          note: "New-entry/budget/recency selection is coarse. Workspace diff or recorded edit/write paths provide identity-based overlap targeting for commit/activity priority; this is not semantic conflict detection."
        -
          scope: "Opaque default compactor and other unaudited selectors"
          assessment: "uninspected"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-cmp-jev"
            - "memory.md#mem-obj-store"
          note: "No internal embedding selector is established by use of a remote classifier; unknown selectors cannot be made inapplicable by known pull routes."
      records:
        - "memory.md#mem-rte-memory-read"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-operational-notes"
        - "memory.md#mem-rte-chapter-seed"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-rte-recall-message"
        - "epistemic.md#epi-rte-recall-selection"
        - "memory.md#mem-rte-tally-catchup"
        - "memory.md#mem-cmp-jev"
        - "memory.md#mem-obj-store"
      note: "Signals belong to actual automatic selections. Explicit slug lookup and substring search remain pull; they do not establish identifier or lexical push by themselves."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Landing event/abstract to durable root memory and later brief/lookup/recall"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-bap-memory-guidance"
              note: "Automatic trace-fed memory writes have later behavior-shaping consumers; successful improvement is not required for wiring."
          records:
            - "memory.md#mem-rte-landing-distil"
            - "memory.md#mem-bap-memory-guidance"
          note: "Automatic trace-fed memory writes have later behavior-shaping consumers; successful improvement is not required for wiring."
        -
          scope: "Branch transcript to retained abstract and later tally/catch-up/distillation"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-tally"
                - "memory.md#mem-obj-tally"
                - "memory.md#mem-rte-tally-catchup"
              note: "Automatic extraction supplies future coordination context."
          records:
            - "memory.md#mem-rte-summary-tally"
            - "memory.md#mem-obj-tally"
            - "memory.md#mem-rte-tally-catchup"
          note: "Automatic extraction supplies future coordination context."
        -
          scope: "Local compaction, side-chat and optional rewind trace summaries to later context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
              note: "Automatically produced retained continuation summaries qualify even when a user initiates injection or rewind. Local compaction annotation separates inspected producer from external default."
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
          note: "Automatically produced retained continuation summaries qualify even when a user initiates injection or rewind. Local compaction annotation separates inspected producer from external default."
        -
          scope: "External default compaction/provider updates, arbitrary Store transformations and actual review enactment"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "runtime.md#rt-cmp-provider-models"
            - "memory.md#mem-cmp-jev"
            - "memory.md#mem-obj-store"
            - "memory.md#mem-rte-review-memory"
          note: "Unknown alternatives and doctrine-only enactment prevent a complete learning inventory. No local or system-wide no is asserted without an absence record."
      records:
        - "memory.md#mem-rte-landing-distil"
        - "memory.md#mem-bap-memory-guidance"
        - "memory.md#mem-rte-summary-tally"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-rte-tally-catchup"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "runtime.md#rt-cmp-provider-models"
        - "memory.md#mem-cmp-jev"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-rte-review-memory"
      note: "Supported yes survives incomplete coverage; no measured capacity improvement, exercised self-improvement or system-complete conclusion follows."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Abstract, side-chat and rewind summaries from recorded conversational turns"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-tally"
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-rte-rewind-context"
              note: "Recorded user/assistant work turns feed durable summaries later delivered as context."
          records:
            - "memory.md#mem-rte-summary-tally"
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-rte-rewind-context"
          note: "Recorded user/assistant work turns feed durable summaries later delivered as context."
        -
          scope: "Landing-derived project memory"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-rte-summary-tally"
              note: "SubmissionLanded supplies the discrete runtime landing/note; its submitter abstract derives from conversational work history. Wrapping that abstract in an event does not erase its session origin."
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-landing-distil"
                - "memory.md#mem-rte-summary-tally"
              note: "SubmissionLanded supplies the discrete runtime landing/note; its submitter abstract derives from conversational work history. Wrapping that abstract in an event does not erase its session origin."
          records:
            - "memory.md#mem-rte-landing-distil"
            - "memory.md#mem-rte-summary-tally"
          note: "SubmissionLanded supplies the discrete runtime landing/note; its submitter abstract derives from conversational work history. Wrapping that abstract in an event does not erase its session origin."
        -
          scope: "Local compaction selected edited model view"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-return"
                - "memory.md#mem-obj-tally"
              note: "Conversation history supplies the local summary; this finding does not resolve every selected entry's original source type."
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-obj-tally"
          note: "Conversation history supplies the local summary; this finding does not resolve every selected entry's original source type."
        -
          scope: "Tool-content inclusion, external default compactor/provider inputs and arbitrary Store/review inputs"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "runtime.md#rt-rte-context-return"
            - "memory.md#mem-obj-store"
            - "memory.md#mem-rte-review-memory"
            - "runtime.md#rt-cmp-provider-models"
          note: "Accepted records do not enumerate original qualifying tool payloads or linked state/action/outcome sequences for every automatic update. Neither tool-traces nor trajectories is inferred from generic execution labels."
      records:
        - "memory.md#mem-rte-summary-tally"
        - "runtime.md#rt-rte-context-return"
        - "memory.md#mem-rte-rewind-context"
        - "memory.md#mem-rte-landing-distil"
        - "memory.md#mem-obj-tally"
        - "memory.md#mem-obj-store"
        - "memory.md#mem-rte-review-memory"
        - "runtime.md#rt-cmp-provider-models"
      note: "Session and landing-event origins are supported locally; mixed/opaque inputs prevent exhaustive source classification."
---

# Ultimate memory profile

## Comparison rationale

### Boundary and coverage

This profile classifies accepted records, not a new source inspection. Known units describe the named local mechanisms, not all external implementations or deployed content. Every axis remains partial because the records retain material opaque or less-inspected alternatives. Provider inference alone does not make model weights accumulated memory; provider retention/update internals remain unresolved rather than becoming a positive parametric-memory finding. The local SQLite integration does not certify external transactional correctness ([RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc), [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models), [MEM-CMP-jev](memory.md#mem-cmp-jev)).

### Canonical identities

Reconciliation supersedes the epistemic memory object with [MEM-OBJ-memory](memory.md#mem-obj-memory), the goal object with [MEM-OBJ-goals](memory.md#mem-obj-goals), memory consumption with [MEM-RTE-memory-read](memory.md#mem-rte-memory-read), review with [MEM-RTE-review-memory](memory.md#mem-rte-review-memory), chapter carry with [MEM-RTE-chapter-seed](memory.md#mem-rte-chapter-seed), and the tuning claim with [MEM-CLM-recall-tuning](memory.md#mem-clm-recall-tuning). Those identities govern the citations above. The separate epistemic candidate-generation, normalization, checks, retention and relevance records remain distinct functions, not superseded whole routes. No disagreement requires choosing a strongest status.

### Force, admission and transformations

Retained memory can supply knowledge to a work model, instructions when its content directs behavior, ranking input to recall, and learning input to a durable update. These are separate consumers, not blanket properties of all text. Existing map membership supplies validation and an enforced admission veto, without turning structural checks into truth acceptance ([MEM-BAP-memory-guidance](memory.md#mem-bap-memory-guidance), [EPI-RTE-memory-checks](epistemic.md#epi-rte-memory-checks)). Goal authorization is interpretive instruction; state/counters have separate code effects ([EPI-RTE-goal-authority](epistemic.md#epi-rte-goal-authority)).

Automatic admission is not manual because a user began a task or selected a chapter transition. Human deletion, direct editing and goal authorization are manual paths. Ordinary review affords human choice, while hands-off policy affords computational substitution. Generic extension callers remain unresolved. Seed application is a separate automatic installation route and bypasses ordinary batch validation ([MEM-RTE-memory-edit](memory.md#mem-rte-memory-edit), [MEM-RTE-review-memory](memory.md#mem-rte-review-memory), [MEM-RTE-chapter-seed](memory.md#mem-rte-chapter-seed)).

Summary compression supports consolidation without requiring raw-history deletion. Memory overwrite supports evolution. Same-slug seed selection resolves key collisions, not established duplicate content, so it emits no curation value. The separate afforded review-cleanup finding does not establish wired seed deduplication. Bounded display/completed-task retention supports decay. Landing generation remains semantically indeterminate: a model request for lessons neither proves synthesis nor licenses classifying every landing as faithful consolidation. The explicitly inspected summaries still support consolidation independently ([MEM-RTE-summary-tally](memory.md#mem-rte-summary-tally), [EPI-RTE-landing-candidates](epistemic.md#epi-rte-landing-candidates), [MEM-OBJ-call-summaries](memory.md#mem-obj-call-summaries)).

### Selection and trace-fed writes

Requested memory/history reads are pull; automatic brief, recall, catch-up, operational-note and continuation delivery are push. Recall uses inferred judgment over memory lines; merely returning slugs does not establish a separate identity-match selector. Catch-up combines coarse recency/budget selection with path-overlap targeting. A requested substring history search is not lexical push ([MEM-RTE-memory-read](memory.md#mem-rte-memory-read), [MEM-RTE-recall-message](memory.md#mem-rte-recall-message), [MEM-RTE-tally-catchup](memory.md#mem-rte-tally-catchup), [RT-RTE-codemode-tools](runtime.md#rt-rte-codemode-tools)).

Landing-derived memory, abstracts and retained continuation summaries support wired trace-learning yes. This classification concerns automatic trace-fed durable guidance, not measured improvement. Session-derived abstracts keep their session origin even inside a landing event; the discrete landing record separately supports event-stream origin. The records do not establish every original tool payload or a trajectory-learning route. No bounded absence record supports a local no, and no opaque alternative is dropped to obtain complete coverage ([MEM-RTE-landing-distil](memory.md#mem-rte-landing-distil), [MEM-RTE-summary-tally](memory.md#mem-rte-summary-tally), [RT-RTE-context-return](runtime.md#rt-rte-context-return), [MEM-RTE-rewind-context](memory.md#mem-rte-rewind-context)).

Call-summary display lines, effect flags, receipts and header fallback retain unresolved lineage as a separate unit; they are not covered by the deterministic catch-up/seed finding. Their prose form at the display consumer is known without asserting a foreground memory route ([MEM-OBJ-call-summaries](memory.md#mem-obj-call-summaries)).

### Source-read log

No frozen-source reads were made. All classifications use the supplied accepted records and annotations; no new evidence or record is declared.
