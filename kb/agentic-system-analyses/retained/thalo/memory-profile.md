---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Thalo memory profile: file-backed knowledge, retained synthesis guidance/prose, symbolic access state and opaque provider alternatives."
run-id: "AAS-2026-10-14-thalo-86fcc3efe983-01"
source-identity: "https://github.com/rejot-dev/thalo"
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
memory-comparison:
  version: 2
  scope: "Retained/edited knowledge instances, entity schemas, synthesis source queries and prompts, generated Markdown and actualization checkpoints; reconstructed workspace/index access structures; shipped local maintenance, CLI/API request routes and action/Pi publication/read-back. Browser snapshots remain included with unresolved later-memory status; external provider parameters and retained state remain opaque included dependencies. Excludes static shipped system/skill instructions, transient command JSON/diagnostics, ordinary current-run presentation state, development workflows and unfrozen external implementations. External caller and provider alternatives remain unresolved rather than silently excluded."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Durable entry, schema, synthesis-query, retained-prompt, generated-prose and checkpoint text"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-schema-entries"
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-synthesis-prompt"
                - "memory.md#mem-obj-synthesis-prose"
                - "runtime.md#rt-obj-checkpoint"
              note: "These operative parts reside in .thalo files or Markdown files/fences; serialization is not a separate substrate."
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-schema-entries"
            - "memory.md#mem-obj-synthesis-sources"
            - "memory.md#mem-obj-synthesis-prompt"
            - "memory.md#mem-obj-synthesis-prose"
            - "runtime.md#rt-obj-checkpoint"
          note: "These operative parts reside in .thalo files or Markdown files/fences; serialization is not a separate substrate."
        - scope: "Git-retained versions of synthesis files and checkpoint changes"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-action-publication"
                - "runtime.md#rt-rte-pi-synthesis"
              note: "The shipped action commits and publishes file changes. Repository history supplements filesystem storage; actual publication is unobserved."
          records:
            - "runtime.md#rt-rte-action-publication"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "The shipped action commits and publishes file changes. Repository history supplements filesystem storage; actual publication is unobserved."
        - scope: "Reconstructed workspace documents, schema registry and access indexes"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-workspace"
                - "memory.md#mem-obj-schema-entries"
              note: "Process Maps and source copies implement access and checking; files, not these transient maps, supply cross-job persistence."
          records:
            - "memory.md#mem-cmp-workspace"
            - "memory.md#mem-obj-schema-entries"
          note: "Process Maps and source copies implement access and checking; files, not these transient maps, supply cross-job persistence."
        - scope: "Browser editable snapshots as possible later-consumed memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Browser process state is inspected, but cross-page retention and a later consumer invocation of accumulated snapshots are not established. Ordinary current-session state is not automatically memory."
        - scope: "Opaque provider parameter dependency at synthesis"
          assessment: "partial"
          findings:
            - value: "model-weights"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-gpt5-mini"
              note: "The shipped synthesis call selects a distributed-parametric model; its exact version and parameter storage internals are not inspected."
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
          note: "The selected model has external parameters; provider retention and mutable endpoint state are inaccessible. This does not classify a provider memory service."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-schema-entries"
        - "memory.md#mem-obj-synthesis-sources"
        - "memory.md#mem-obj-synthesis-prompt"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-obj-checkpoint"
        - "runtime.md#rt-rte-action-publication"
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-cmp-workspace"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "File and Git retention and reconstructed access structures are supported. Browser later-consumption and opaque provider state prevent complete memory-store coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Entry sections and rationales consumed as selected raw text; prior generated prose at later Pi model request"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-synthesis-prose"
                - "runtime.md#rt-rte-pi-synthesis"
              note: "Human/model interpretation gives natural-language sections and Markdown their effect; reasons are delivered when present, not guaranteed to survive generation."
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-synthesis-prose"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Human/model interpretation gives natural-language sections and Markdown their effect; reasons are delivered when present, not guaranteed to survive generation."
        - scope: "Retained synthesis prompt at later model invocation"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-prompt"
                - "runtime.md#rt-bap-synthesis-guidance"
              note: "Stored directions reach user-prompt text and require model interpretation; static script system guidance is excluded."
          records:
            - "memory.md#mem-obj-synthesis-prompt"
            - "runtime.md#rt-bap-synthesis-guidance"
          note: "Stored directions reach user-prompt text and require model interpretation; static script system guidance is excluded."
        - scope: "Entry headers/metadata, source queries, schema directives and checkpoints at fixed code consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-schema-entries"
                - "runtime.md#rt-obj-checkpoint"
                - "memory.md#mem-cmp-workspace"
                - "memory.md#mem-rte-schema-resolution"
                - "runtime.md#rt-rte-actualize-selection"
              note: "Localized fields determine query membership, schema constraints and cutoff selection. Parsed indexes preserve this symbolic path separately from prose."
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-synthesis-sources"
            - "memory.md#mem-obj-schema-entries"
            - "runtime.md#rt-obj-checkpoint"
            - "memory.md#mem-cmp-workspace"
            - "memory.md#mem-rte-schema-resolution"
            - "runtime.md#rt-rte-actualize-selection"
          note: "Localized fields determine query membership, schema constraints and cutoff selection. Parsed indexes preserve this symbolic path separately from prose."
        - scope: "Selected provider parameter component"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-gpt5-mini"
              note: "Distributed-parametric form is stated for the model dependency; this does not expose its learned content or update behavior."
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
          note: "Distributed-parametric form is stated for the model dependency; this does not expose its learned content or update behavior."
        - scope: "Browser accumulated payload at an unestablished later invocation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Editable text is mixed natural-language/symbolic, but no later-memory consumption path is established; display/panel state is not a proxy for consumed memory."
        - scope: "Additional provider-retained payloads or summaries"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Provider/Pi processing and retention are outside the inspected source; a readable host prompt does not classify an opaque retained payload."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-obj-synthesis-prompt"
        - "runtime.md#rt-bap-synthesis-guidance"
        - "memory.md#mem-obj-synthesis-sources"
        - "memory.md#mem-obj-schema-entries"
        - "runtime.md#rt-obj-checkpoint"
        - "memory.md#mem-cmp-workspace"
        - "memory.md#mem-rte-schema-resolution"
        - "runtime.md#rt-rte-actualize-selection"
        - "runtime.md#rt-cmp-gpt5-mini"
        - "memory.md#mem-obj-playground-state"
      note: "Known forms stay attached to actual parts and consumers. Browser later-memory status and opaque provider alternatives remain unresolved."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller authoring/editing of entry, schema, source-query and retained-prompt text"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-schema-entries"
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-synthesis-prompt"
                - "runtime.md#rt-rte-local-authoring"
              note: "The local authoring surface affords supplying/editing retained content; authored fixtures do not authenticate all operational inputs."
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-schema-entries"
            - "memory.md#mem-obj-synthesis-sources"
            - "memory.md#mem-obj-synthesis-prompt"
            - "runtime.md#rt-rte-local-authoring"
          note: "Authored fixtures and editable definitions establish an authoring path, but the initial provenance of arbitrary loaded KB content remains caller-dependent."
        - scope: "Workspace/registry access structures derived from retained source files"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-workspace"
                - "memory.md#mem-rte-schema-resolution"
              note: "Parser/rebuild and timestamp-ordered registry resolution compile file content into access structures, not a separate authoritative knowledge origin."
          records:
            - "memory.md#mem-cmp-workspace"
            - "memory.md#mem-rte-schema-resolution"
          note: "Parser/rebuild and timestamp-ordered registry resolution compile file content into access structures, not a separate authoritative knowledge origin."
        - scope: "Pi-produced Markdown and serialized selector checkpoint"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-prose"
                - "runtime.md#rt-rte-pi-synthesis"
                - "runtime.md#rt-obj-checkpoint"
              note: "Model output is generated from selected KB material and prior file; host serializes a Git/timestamp marker. Neither derivation is established as trace extraction."
          records:
            - "memory.md#mem-obj-synthesis-prose"
            - "runtime.md#rt-rte-pi-synthesis"
            - "runtime.md#rt-obj-checkpoint"
          note: "Model output is generated from selected KB material and prior file; host serializes a Git/timestamp marker. Neither derivation is established as trace extraction."
        - scope: "Initial experiential or imported provenance of arbitrary source entries"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-instance-entries"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Reference URLs and journal/reflection labels do not establish acquisition of their destinations or authentic trace origin; imported and trace-extracted lineage cannot be asserted from labels."
        - scope: "Defaults/initial browser snapshot at a later memory consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Defaults and edits are described, but initial provenance and cross-page consumption are not established."
        - scope: "Model parameters and additional provider retained state"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
          note: "Training/embedding provenance and provider update paths are not inspected."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-schema-entries"
        - "memory.md#mem-obj-synthesis-sources"
        - "memory.md#mem-obj-synthesis-prompt"
        - "runtime.md#rt-rte-local-authoring"
        - "memory.md#mem-cmp-workspace"
        - "memory.md#mem-rte-schema-resolution"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-rte-pi-synthesis"
        - "runtime.md#rt-obj-checkpoint"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Authoring affordance and known compiled derivatives coexist with unresolved initial and provider provenance. File loading alone is not a separate imported-content origin."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Raw source sections and prior generated Markdown at the later Pi request"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-synthesis-prose"
                - "runtime.md#rt-rte-pi-synthesis"
                - "epistemic.md#epi-rte-prose-retention"
              note: "These parts supply reference/context to generation. Delivery establishes knowledge force, not factual endorsement or observed reliance."
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-synthesis-prose"
            - "runtime.md#rt-rte-pi-synthesis"
            - "epistemic.md#epi-rte-prose-retention"
          note: "These parts supply reference/context to generation. Delivery establishes knowledge force, not factual endorsement or observed reliance."
        - scope: "Retained synthesis prompt at the Pi model consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-prompt"
                - "runtime.md#rt-bap-synthesis-guidance"
              note: "Stored prompt supplies repeatable directions; natural-language guidance is not an enforcement gate."
          records:
            - "memory.md#mem-obj-synthesis-prompt"
            - "runtime.md#rt-bap-synthesis-guidance"
          note: "Stored prompt supplies repeatable directions; natural-language guidance is not an enforcement gate."
        - scope: "Source queries and entry metadata at actualization/query membership consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-instance-entries"
                - "runtime.md#rt-rte-actualize-selection"
                - "memory.md#mem-rte-query-readout"
              note: "Predicates select the input scope and exclude nonmatching entries from delivery, giving routing and enforced membership rather than relevance ranking."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-instance-entries"
                - "runtime.md#rt-rte-actualize-selection"
                - "memory.md#mem-rte-query-readout"
              note: "Predicates select the input scope and exclude nonmatching entries from delivery, giving routing and enforced membership rather than relevance ranking."
          records:
            - "memory.md#mem-obj-synthesis-sources"
            - "memory.md#mem-obj-instance-entries"
            - "runtime.md#rt-rte-actualize-selection"
            - "memory.md#mem-rte-query-readout"
          note: "Predicates select the input scope and exclude nonmatching entries from delivery, giving routing and enforced membership rather than relevance ranking."
        - scope: "Checkpoint at future actualize/tracker consumer"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-checkpoint"
                - "runtime.md#rt-bap-checkpoint-selection"
                - "runtime.md#rt-rte-actualize-selection"
              note: "Retained cutoff/base state selects the next source window and excludes entries outside its predicate; it does not validate faithful incorporation."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-checkpoint"
                - "runtime.md#rt-bap-checkpoint-selection"
                - "runtime.md#rt-rte-actualize-selection"
              note: "Retained cutoff/base state selects the next source window and excludes entries outside its predicate; it does not validate faithful incorporation."
          records:
            - "runtime.md#rt-obj-checkpoint"
            - "runtime.md#rt-bap-checkpoint-selection"
            - "runtime.md#rt-rte-actualize-selection"
          note: "Retained cutoff/base state selects the next source window and excludes entries outside its predicate; it does not validate faithful incorporation."
        - scope: "Retained resolved schema directives at the checker and CLI exit consumer"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-schema-entries"
                - "memory.md#mem-rte-schema-resolution"
                - "runtime.md#rt-rte-check-feedback"
              note: "Constraints determine structural conformance. CLI errors enforce failed check completion, but cannot veto independent file writers."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-schema-entries"
                - "memory.md#mem-rte-schema-resolution"
                - "runtime.md#rt-rte-check-feedback"
              note: "Constraints determine structural conformance. CLI errors enforce failed check completion, but cannot veto independent file writers."
          records:
            - "memory.md#mem-obj-schema-entries"
            - "memory.md#mem-rte-schema-resolution"
            - "runtime.md#rt-rte-check-feedback"
          note: "Constraints determine structural conformance. CLI errors enforce failed check completion, but cannot veto independent file writers."
        - scope: "Schema descriptions and other unconsumed metadata at further consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-schema-entries"
            - "memory.md#mem-cmp-workspace"
          note: "Readable documentation and metadata without an identified consequential consumer establish no additional force."
        - scope: "Browser snapshot at a later memory consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Current-session checks/preparation are inspected; later invocation and durable behavioral force remain unestablished."
        - scope: "Provider-retained state beyond the identified parameter dependency"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Opaque host/provider processing prevents classification of additional retained controls or update consumers."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-rte-pi-synthesis"
        - "epistemic.md#epi-rte-prose-retention"
        - "memory.md#mem-obj-synthesis-prompt"
        - "runtime.md#rt-bap-synthesis-guidance"
        - "memory.md#mem-obj-synthesis-sources"
        - "runtime.md#rt-rte-actualize-selection"
        - "memory.md#mem-rte-query-readout"
        - "runtime.md#rt-obj-checkpoint"
        - "runtime.md#rt-bap-checkpoint-selection"
        - "memory.md#mem-obj-schema-entries"
        - "memory.md#mem-rte-schema-resolution"
        - "runtime.md#rt-rte-check-feedback"
        - "memory.md#mem-cmp-workspace"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Knowledge, instruction, routing, validation and enforcement have distinct local consumers. No record establishes retained relevance-ranking inputs or trace-fed learning authority; unresolved parts are not absent."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Pi admission of generated Markdown and appended checkpoint"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-synthesis"
                - "runtime.md#rt-obj-checkpoint"
                - "epistemic.md#epi-rte-prose-retention"
              note: "Software installs nonempty model output and a marker without an individual human content decision; starting CI/manual dispatch does not make this manual."
          records:
            - "runtime.md#rt-rte-pi-synthesis"
            - "runtime.md#rt-obj-checkpoint"
            - "epistemic.md#epi-rte-prose-retention"
          note: "Software installs nonempty model output and a marker without an individual human content decision; starting CI/manual dispatch does not make this manual."
        - scope: "Action branch commit/publication after configured command completion"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-action-publication"
              note: "Software stages and publishes all working-tree changes after subprocess return; PR review is downstream, not pre-publication approval."
          records:
            - "runtime.md#rt-rte-action-publication"
          note: "Software stages and publishes all working-tree changes after subprocess return; PR review is downstream, not pre-publication approval."
        - scope: "Initialization, formatting and merge-driver admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-local-authoring"
                - "epistemic.md#epi-rte-merge-disposition"
              note: "Software computes and writes starter/formatted/merged text, including conflict-bearing merge output. Caller initiation is not per-content human approval."
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "epistemic.md#epi-rte-merge-disposition"
          note: "Software computes and writes starter/formatted/merged text, including conflict-bearing merge output. Caller initiation is not per-content human approval."
        - scope: "Explicit human text supply, edit, revert or later PR-integration decision"
          assessment: "partial"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-local-authoring"
                - "runtime.md#rt-rte-action-publication"
              note: "A human genuinely supplying, replacing or approving content makes that admission manual; external review and edits are available, not observed."
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
          note: "Human content decisions are an afforded separate mechanism; actual authors and exercised PR approval are not supplied."
        - scope: "Generic external editor/agent saves and arbitrary replacement command admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
            - "memory.md#mem-obj-instance-entries"
          note: "Generic caller identity does not establish a human decision over individual content. Replacement command internals are external; their agency cannot inherit the shipped Pi classification."
        - scope: "Browser snapshot changes as later-consumed memory writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "setContent/reset are state updates, but durable/later-memory admission and per-content control remain unresolved."
        - scope: "Provider-retained state and parameter updates"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Provider admission/update mechanisms are outside the inspected source."
      records:
        - "runtime.md#rt-rte-pi-synthesis"
        - "runtime.md#rt-obj-checkpoint"
        - "epistemic.md#epi-rte-prose-retention"
        - "runtime.md#rt-rte-action-publication"
        - "runtime.md#rt-rte-local-authoring"
        - "epistemic.md#epi-rte-merge-disposition"
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Automatic shipped admission is wired; manual decisions are afforded locally. Generic external callers and opaque provider writes prevent a complete agency classification."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Timestamp tracker identity-key suppression in selected results"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-actualize-selection"
          note: "The recorded timestamp branch filters returned instances by file/timestamp/entity/link while leaving source entries retained. It can suppress distinct same-minute instances sharing that key. This access-selection operation does not merge or remove near-duplicate retained content, so no controlled curation operation applies to this bounded mechanism."
        - scope: "Schema alteration/removal applied to resolved retained constraints"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-schema-resolution"
                - "memory.md#mem-obj-schema-entries"
              note: "Timestamp-ordered alterations overwrite fields/sections and remove named constraints, evolving the resolved schema used on later checks."
          records:
            - "memory.md#mem-rte-schema-resolution"
            - "memory.md#mem-obj-schema-entries"
          note: "Timestamp-ordered alterations overwrite fields/sections and remove named constraints, evolving the resolved schema used on later checks."
        - scope: "Existing synthesis-file rewrite and model semantic transformation"
          assessment: "partial"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-synthesis"
                - "memory.md#mem-obj-synthesis-prose"
                - "epistemic.md#epi-rte-file-reconstruction"
              note: "Host installs a replacement suffix in an existing retained file; narrow-edit fidelity and semantic quality are not enforced."
          records:
            - "runtime.md#rt-rte-pi-synthesis"
            - "memory.md#mem-obj-synthesis-prose"
            - "epistemic.md#epi-rte-file-reconstruction"
          note: "Host replacement revises the retained synthesis artifact. Whether generated propositions consolidate existing claims or introduce absent claims is not established by an input/output instance."
        - scope: "Version merge, physical deletion and caller withdrawal"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-merge-disposition"
            - "runtime.md#rt-rte-local-authoring"
          note: "Existing versions are combined and entries can be physically deleted. The records do not establish semantic duplicate merging, reduced claim representation, or invalidation retaining history as a maintained reliance state; physical deletion alone is not decay."
        - scope: "External editor transformations and arbitrary configured commands"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
          note: "Complete formatter/editor semantics and replacement-command transformations are not inspected; supported local operations cannot enumerate all external curation."
        - scope: "Browser reset as memory curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Reset discards working state, but the later-memory boundary is unresolved; it is not classified as memory decay."
        - scope: "Provider-internal memory transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Compaction, training and provider maintenance are uninspected."
      records:
        - "runtime.md#rt-rte-actualize-selection"
        - "memory.md#mem-rte-schema-resolution"
        - "memory.md#mem-obj-schema-entries"
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-obj-synthesis-prose"
        - "epistemic.md#epi-rte-file-reconstruction"
        - "epistemic.md#epi-rte-merge-disposition"
        - "runtime.md#rt-rte-local-authoring"
        - "runtime.md#rt-rte-action-publication"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Evolution of schemas/prose is supported. Timestamp identity-key suppression filters access results, not retained memory content, and supplies no curation finding. A synthesis route name and candidate-generation claim do not establish consolidate or synthesize; semantic and opaque alternatives remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Standalone query and requested actualization preparation"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-readout"
                - "runtime.md#rt-rte-actualize-selection"
              note: "Previously retained files reach caller-requested CLI/API query or actualization results; automatic code fulfillment is still pull."
          records:
            - "memory.md#mem-rte-query-readout"
            - "runtime.md#rt-rte-actualize-selection"
          note: "Previously retained files reach caller-requested CLI/API query or actualization results; automatic code fulfillment is still pull."
        - scope: "Host supply of selected raw entries, retained prompt and whole prior synthesis file to a fresh Pi model"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-synthesis"
                - "memory.md#mem-obj-synthesis-prose"
                - "memory.md#mem-obj-instance-entries"
                - "memory.md#mem-obj-synthesis-prompt"
                - "epistemic.md#epi-rte-prose-retention"
              note: "The host assembles context before the model call without a model request for the retained parts. This push is distinct from the upstream requested actualize result."
          records:
            - "runtime.md#rt-rte-pi-synthesis"
            - "memory.md#mem-obj-synthesis-prose"
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-synthesis-prompt"
            - "epistemic.md#epi-rte-prose-retention"
          note: "The host assembles context before the model call without a model request for the retained parts. This push is distinct from the upstream requested actualize result."
        - scope: "Checkpoint and schema consumption during requested selection/checking"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-checkpoint"
                - "runtime.md#rt-bap-checkpoint-selection"
                - "memory.md#mem-rte-schema-resolution"
                - "runtime.md#rt-rte-check-feedback"
              note: "Callers request actualization or checking; code reads retained controls to fulfill those operations. Delivery is not counted as a second unsolicited route."
          records:
            - "runtime.md#rt-obj-checkpoint"
            - "runtime.md#rt-bap-checkpoint-selection"
            - "memory.md#mem-rte-schema-resolution"
            - "runtime.md#rt-rte-check-feedback"
          note: "Callers request actualization or checking; code reads retained controls to fulfill those operations. Delivery is not counted as a second unsolicited route."
        - scope: "Additional external API/editor consumers and replacement commands"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-query-readout"
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
          note: "Access affordances exist but no additional later model reader is identified; direction cannot inherit the shipped Pi route."
        - scope: "Browser snapshot across consumer invocations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Current-session deterministic runner access does not establish a later accumulated-memory route."
        - scope: "Provider-retained state read-back"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Provider/Pi internal consumption is uninspected."
      records:
        - "memory.md#mem-rte-query-readout"
        - "runtime.md#rt-rte-actualize-selection"
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-obj-synthesis-prose"
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-synthesis-prompt"
        - "epistemic.md#epi-rte-prose-retention"
        - "runtime.md#rt-obj-checkpoint"
        - "runtime.md#rt-bap-checkpoint-selection"
        - "memory.md#mem-rte-schema-resolution"
        - "runtime.md#rt-rte-check-feedback"
        - "runtime.md#rt-rte-local-authoring"
        - "runtime.md#rt-rte-action-publication"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Pull at explicit query/preparation and push at host-to-model context assembly coexist in one chain. Unresolved alternatives prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Pending Pi invocation: whole current target file automatically supplied to model"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pi-synthesis"
                - "memory.md#mem-obj-synthesis-prose"
                - "epistemic.md#epi-rte-prose-retention"
              note: "Trigger is pending execution; upstream file choice fixes the target and host includes all trimmed available content. There is no targeted selection within prose: coarse whole-file supply, not identifier matching merely because a path is present."
          records:
            - "runtime.md#rt-rte-pi-synthesis"
            - "memory.md#mem-obj-synthesis-prose"
            - "epistemic.md#epi-rte-prose-retention"
          note: "Trigger is pending execution; upstream file choice fixes the target and host includes all trimmed available content. There is no targeted selection within prose: coarse whole-file supply, not identifier matching merely because a path is present."
        - scope: "Pending Pi invocation: source entries selected upstream by stored entity/tag/link query and cutoff"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actualize-selection"
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-instance-entries"
                - "runtime.md#rt-rte-pi-synthesis"
              note: "Trigger is pending synthesis. Exact entity/tag/link matches select current retained instances for host delivery; cutoff/change tests further filter that set. Identity predicates and coarse freshness eligibility remain separate findings, with no inferred relevance score."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actualize-selection"
                - "memory.md#mem-obj-synthesis-sources"
                - "memory.md#mem-obj-instance-entries"
                - "runtime.md#rt-rte-pi-synthesis"
              note: "Trigger is pending synthesis. Exact entity/tag/link matches select current retained instances for host delivery; cutoff/change tests further filter that set. Identity predicates and coarse freshness eligibility remain separate findings, with no inferred relevance score."
          records:
            - "runtime.md#rt-rte-actualize-selection"
            - "memory.md#mem-obj-synthesis-sources"
            - "memory.md#mem-obj-instance-entries"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Trigger is pending synthesis. Exact entity/tag/link matches select current retained instances for host delivery; cutoff/change tests further filter that set. Identity predicates and coarse freshness eligibility remain separate findings, with no inferred relevance score."
        - scope: "Pending Pi invocation: retained prompt extracted from definition"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-synthesis-prompt"
                - "runtime.md#rt-rte-pi-synthesis"
              note: "Host includes collected prompt-header content as guidance. Header availability is coarse structural selection, not inferred lexical relevance to a consumer question."
          records:
            - "memory.md#mem-obj-synthesis-prompt"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Host includes collected prompt-header content as guidance. Header availability is coarse structural selection, not inferred lexical relevance to a consumer question."
        - scope: "Explicit requested query/preparation and requested schema/checkpoint reads"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-query-readout"
            - "runtime.md#rt-rte-actualize-selection"
            - "memory.md#mem-rte-schema-resolution"
            - "runtime.md#rt-obj-checkpoint"
          note: "This unit is pull fulfillment; push-signal classification does not apply to the requested return."
        - scope: "Additional external and provider push selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-query-readout"
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "External consumers and provider internals have no established selector/payload inventory; pull-only inapplicability cannot cover these alternatives."
        - scope: "Browser snapshot later-memory selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "A current runner snapshot is inspected, but an accumulated-memory push route and its selector are not established."
      records:
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-obj-synthesis-prose"
        - "epistemic.md#epi-rte-prose-retention"
        - "runtime.md#rt-rte-actualize-selection"
        - "memory.md#mem-obj-synthesis-sources"
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-synthesis-prompt"
        - "memory.md#mem-rte-query-readout"
        - "memory.md#mem-rte-schema-resolution"
        - "runtime.md#rt-obj-checkpoint"
        - "runtime.md#rt-rte-local-authoring"
        - "runtime.md#rt-rte-action-publication"
        - "runtime.md#rt-cmp-gpt5-mini"
        - "memory.md#mem-obj-playground-state"
      note: "Coarse full-file/prompt supply and identifier/freshness source selection are local host-push warrants. Requested returns are not extra pushes; opaque alternatives remain unresolved."
    trace_learning:
      assessment: "not-determinable"
      units:
        - scope: "Pi automatic KB-to-Markdown-to-later-model route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-instance-entries"
            - "memory.md#mem-obj-synthesis-prose"
            - "runtime.md#rt-rte-pi-synthesis"
            - "epistemic.md#epi-rte-prose-retention"
          note: "Automatic durable rewrite and later context consumption are wired, but original inputs are caller-dependent KB entries, not authenticated session/tool/event/trajectory traces. This prevents yes; no bounded absence warrant supports no."
        - scope: "Checkpoint append, workspace/schema compilation and local maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-checkpoint"
            - "memory.md#mem-cmp-workspace"
            - "memory.md#mem-rte-schema-resolution"
            - "runtime.md#rt-rte-local-authoring"
            - "epistemic.md#epi-rte-merge-disposition"
          note: "Known automatic transformations are symbolic control/content maintenance. Records neither identify a qualifying trace-fed behavior-shaping chain nor warrant complete absence across caller inputs; operational checkpoint metadata alone is not a trace source."
        - scope: "External authoring, commands and API consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
            - "memory.md#mem-rte-query-readout"
          note: "Arbitrary caller provenance and transformations remain unresolved; an external agent label does not establish automatic trace learning."
        - scope: "Browser accumulated-state update and later consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Cross-invocation retained result and qualifying trace-fed update are not established."
        - scope: "Provider parameter/state updates"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Provider update behavior and internal trace use are inaccessible."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-rte-pi-synthesis"
        - "epistemic.md#epi-rte-prose-retention"
        - "runtime.md#rt-obj-checkpoint"
        - "memory.md#mem-cmp-workspace"
        - "memory.md#mem-rte-schema-resolution"
        - "runtime.md#rt-rte-local-authoring"
        - "epistemic.md#epi-rte-merge-disposition"
        - "runtime.md#rt-rte-action-publication"
        - "memory.md#mem-rte-query-readout"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "No accepted record establishes a controlled yes or a bounded no. Durable recurrent generation is not itself evidence of trace-fed learning; unknown provenance and opaque updates prevent a system negative."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Original inputs to possible qualifying Pi trace-fed rewrite"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-instance-entries"
            - "runtime.md#rt-rte-pi-synthesis"
            - "memory.md#mem-obj-synthesis-prose"
          note: "No qualifying trace-fed route is established. Journal/reflection labels, URLs and adapter serialization do not determine original session-log, tool-trace, event-stream or trajectory content."
        - scope: "Possible external/local maintenance trace-fed updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-authoring"
            - "runtime.md#rt-rte-action-publication"
            - "memory.md#mem-rte-query-readout"
            - "runtime.md#rt-obj-checkpoint"
          note: "Caller input origins and behavior-shaping update chains remain unresolved. Host timestamps and Git markers alone do not establish original event-stream inputs."
        - scope: "Browser inputs to a possible later-memory learning route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playground-state"
          note: "Neither a qualifying durable trace-fed write nor original experiential input is established."
        - scope: "Provider training/retention input origins"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt5-mini"
            - "runtime.md#rt-rte-pi-synthesis"
          note: "Original learning inputs and update mechanisms are outside inspected evidence."
      records:
        - "memory.md#mem-obj-instance-entries"
        - "runtime.md#rt-rte-pi-synthesis"
        - "memory.md#mem-obj-synthesis-prose"
        - "runtime.md#rt-rte-local-authoring"
        - "runtime.md#rt-rte-action-publication"
        - "memory.md#mem-rte-query-readout"
        - "runtime.md#rt-obj-checkpoint"
        - "memory.md#mem-obj-playground-state"
        - "runtime.md#rt-cmp-gpt5-mini"
      note: "Trace-source coverage is unresolved, not inapplicable: there is no bounded, completely assessed absence of qualifying trace learning. No source value is inferred from a KB label or serialization."
---

# Thalo memory profile

## Comparison rationale

The profile separates retained content from access controls. Entry prose and prior generated Markdown supply knowledge context; retained synthesis prompts supply instructions. Queries, metadata and checkpoints select scope and enforce membership. Schemas validate structural conformance, with enforced CLI failure only when checking is called. None of those forces establishes semantic acceptance or observed model reliance. See [MEM-OBJ-instance-entries](memory.md#mem-obj-instance-entries), [MEM-RTE-schema-resolution](memory.md#mem-rte-schema-resolution), [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance) and [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection).

Requested query and actualization output are pull. The shipped host then supplies selected entries, stored guidance and the entire previous file to a fresh model invocation without a model retrieval request: that operation is push. An upstream file path alone does not establish identifier-targeted prose selection; full-file supply is coarse. Exact source entity/tag/link matching is a distinct identity selector; freshness filtering is a separate coarse eligibility operation. Neither is inferred relevance ranking. See [MEM-RTE-query-readout](memory.md#mem-rte-query-readout), [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) and [EPI-RTE-prose-retention](epistemic.md#epi-rte-prose-retention).

Curation values follow implemented transformations over retained memory. Timestamp selection suppresses returned instances sharing a composite key without merging or removing retained source content; key collisions can suppress distinct entries. That access filter establishes no curation value, including dedup. Schema alterations evolve resolved constraints; host replacement evolves a retained synthesis artifact. The generated content's semantic relation remains unresolved, so neither the word synthesis nor a requested guide establishes a new claim or reduced claim representation. Physical merge deletion does not establish a history-retaining invalidation mechanism or memory decay. See [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection), [MEM-RTE-schema-resolution](memory.md#mem-rte-schema-resolution), [EPI-RTE-file-reconstruction](epistemic.md#epi-rte-file-reconstruction) and [EPI-RTE-merge-disposition](epistemic.md#epi-rte-merge-disposition).

Manual and automatic agency are separate admission mechanisms. CI initiation does not turn the Pi writer or publication into human content approval. Human edits and later review are afforded decisions, while generic external caller identity leaves their control unresolved. Automatic compilation and durable recurrent prose generation do not establish trace learning: source entries have caller-dependent experiential provenance. Without bounded absence records neither a trace-learning no nor trace-source inapplicability is warranted. See [RT-RTE-local-authoring](runtime.md#rt-rte-local-authoring), [RT-RTE-action-publication](runtime.md#rt-rte-action-publication), [MEM-OBJ-instance-entries](memory.md#mem-obj-instance-entries) and [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis).

The supplied reconciliation supersedes EPI-OBJ-synthesis-prose with [MEM-OBJ-synthesis-prose](memory.md#mem-obj-synthesis-prose), and EPI-RTE-query-selection with [MEM-RTE-query-readout](memory.md#mem-rte-query-readout). All classifications use those canonical records. The Pi guard, reconstruction and retention parts remain valid alongside their runtime container; no value is strengthened by supersession.

All positive findings retain their local basis. Implementation is not observed operation or causal benefit. Partial axes retain unresolved initial provenance, external admissions/consumers, browser later-memory status and provider alternatives rather than obtaining known coverage by dropping them. The parameter component's parametric form is known, but provider retention/update routes remain uninspected. See [MEM-OBJ-playground-state](memory.md#mem-obj-playground-state) and [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini).

Source-read log: no source reads were made. Classification used only the supplied accepted members and reconciliation; no records, evidence or quotations were added.
