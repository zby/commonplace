---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Nimbalyst Wiki memory comparison for retained wiki content, access metadata and prescribed session-to-page recall at the frozen plugin boundary."
run-id: AAS-2026-11-08-nimbalyst-wiki-d9ff54186a76-01
source-identity: https://github.com/nimbalyst/nimbalyst-wiki
reviewed-boundary: "97c1ba1594d6e3d466a23d33c1bda084026b01b8"
memory-comparison:
  version: 2
  scope: "Accumulated local/team wiki prose, installed editable guide, page fields, tables/types, editor payloads and attachments, recovery/cache and destination metadata; their capture, maintenance, migration, direct-edit, component and later-read routes. Includes unresolved external hook, server, editor and caller behavior at this partial loop. Excludes static shipped skills/base guide before installation, release machinery and enclosing host/provider state not established as wiki memory."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Local pages, installed guide, YAML metadata/types, CSV rows, editor files/sidecars/assets, activity/trash and destination files"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [runtime.md#rt-obj-wiki-pages, memory.md#mem-obj-table-types, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-obj-destination-metadata]
              note: "The file contract names these retained objects; external writers are not inspected."
          records: [runtime.md#rt-obj-wiki-pages, memory.md#mem-obj-writing-guide, memory.md#mem-obj-table-types, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-obj-destination-metadata]
          note: "Complete classification of the named local format objects, not proof of writes."
        - scope: "Team collaborative page bodies and tool-managed type schemas"
          assessment: partial
          findings:
            - value: service-object
              basis: claimed
              records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-table-types, runtime.md#rt-rte-team-transition]
              note: "The documented team service retains collaborative content; no backing database is inferred."
          records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-table-types, runtime.md#rt-rte-team-transition]
          note: "Service-level retention is specified; internal persistence and history substrates remain unknown."
        - scope: "Search/backlink/read-state caches and external session-input payload retention"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-recovery-records, epistemic.md#epi-obj-citation-inputs]
          note: "Cache locations and upstream payload storage are not established; transient returned citations are not presumed durable stores."
      records: [runtime.md#rt-obj-wiki-pages, memory.md#mem-obj-page-prose, memory.md#mem-obj-table-types, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-obj-destination-metadata, epistemic.md#epi-obj-citation-inputs]
      note: "The local format and hosted object contract classify storage, but opaque cache/service internals prevent complete coverage; historical graph input is not a current graph substrate."
    representational_form:
      assessment: partial
      units:
        - scope: "Page decisions/context/reasons, copied citations, installed guide and retained component prompts/templates"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-writing-guide, memory.md#mem-rte-component-consumption]
              note: "People and models interpret prose, writing rules and prompts."
          records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-writing-guide, memory.md#mem-rte-component-consumption]
          note: "This unit covers interpreted text, not its symbolic selectors."
        - scope: "Page identity/globs/mark attributes, type definitions and typed cells, destination/recovery records, component keys, formulas/assertions"
          assessment: known
          findings:
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, memory.md#mem-obj-destination-metadata, memory.md#mem-obj-recovery-records, memory.md#mem-rte-component-consumption, epistemic.md#epi-obj-sheet-expressions]
              note: "External tools use localized keys, schema fields, selectors and arithmetic/check rules."
          records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, memory.md#mem-obj-destination-metadata, memory.md#mem-obj-recovery-records, memory.md#mem-rte-component-consumption, epistemic.md#epi-obj-sheet-expressions]
          note: "Text-cell meaning and formula comments remain in the interpreted-text branch, not validated by encoding."
        - scope: "Other editor payloads/assets and any external extracted representation delivered to models"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-editor-pages, runtime.md#rt-rte-host-entry]
          note: "Extension-specific bodies and hook payloads are not fully classified; a readable summary cannot classify an opaque payload."
      records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-writing-guide, memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-obj-destination-metadata, memory.md#mem-rte-component-consumption, epistemic.md#epi-obj-sheet-expressions, runtime.md#rt-rte-host-entry]
      note: "Text and fixed-rule parts are supported at design level; no parametric wiki-memory representation is established, and host model weights are outside this inventory."
    lineage:
      assessment: partial
      units:
        - scope: "Documented direct person/agent edits and newly authored page/component content"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption]
              note: "People and agents can supply retained bodies, prompts and templates."
          records: [memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption]
          note: "An authoring affordance does not identify the origin of an unavailable initial corpus."
        - scope: "Setup source/base-guide acquisition and migration of legacy or local wiki material"
          assessment: known
          findings:
            - value: imported
              basis: claimed
              records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-writing-guide, memory.md#mem-rte-legacy-migration, runtime.md#rt-rte-team-transition]
              note: "Existing repository material, shipped guide text and retained old content enter the chosen wiki destination."
          records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-writing-guide, memory.md#mem-rte-legacy-migration, runtime.md#rt-rte-team-transition]
          note: "Migration does not establish original authorship or faithful preservation."
        - scope: "Session capture's selected decisions/questions/context and attached session words"
          assessment: known
          findings:
            - value: trace-extracted
              basis: claimed
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-page-prose]
              note: "Conversation/session inputs feed selected persistent prose rather than raw transcript replay."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-page-prose]
          note: "Classifies the prescribed derivation route, not fidelity of an observed output."
        - scope: "Initial corpus, detailed editor/cache derivations and undocumented external transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-page-prose, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records]
          note: "No initial corpus or complete external derivation account supports a complete lineage inventory."
      records: [runtime.md#rt-rte-wiki-setup, runtime.md#rt-rte-session-capture, runtime.md#rt-rte-team-transition, memory.md#mem-obj-writing-guide, memory.md#mem-obj-page-prose, memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption, memory.md#mem-rte-legacy-migration, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records]
      note: "Supported import, authoring and session extraction paths coexist; no other-compiled value follows merely from file conversion or uninspected calculations."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained prose and surrounding reasons delivered to answering/coding agents and page readers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose]
              note: "Pages provide reference and contextual evidence, not truth enforcement."
          records: [runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose]
          note: "This is intended consumption, not demonstrated reliance."
        - scope: "Installed guide at later writing and retained action prompts at new-session consumers"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [runtime.md#rt-bap-guide-writing, memory.md#mem-obj-writing-guide]
              note: "The retained guide explicitly overrides base writing advice."
            - value: instruction
              basis: afforded
              records: [memory.md#mem-rte-component-consumption]
              note: "A clicked action supplies its retained prompt to an agent session."
          records: [runtime.md#rt-bap-guide-writing, memory.md#mem-obj-writing-guide, memory.md#mem-rte-component-consumption]
          note: "Separate consumer paths and evidence layers; neither establishes obedience."
        - scope: "Retained destination pins/migration markers, coverage globs and component selectors at external selection consumers"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-destination-metadata, memory.md#mem-obj-page-metadata]
              note: "Metadata chooses destination or covering pages, not access permission."
            - value: routing
              basis: afforded
              records: [memory.md#mem-rte-component-consumption]
              note: "Retained view/transclusion/template keys select displayed fields, pages or creation inputs."
          records: [memory.md#mem-obj-destination-metadata, memory.md#mem-obj-page-metadata, memory.md#mem-rte-component-consumption]
          note: "The declared selectors have operational force distinct from prose knowledge."
        - scope: "Retained IDs, versions and type criteria at cooperating local writers"
          assessment: partial
          findings:
            - value: validation
              basis: claimed
              records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, memory.md#mem-rte-wiki-maintenance, runtime.md#rt-rte-session-capture]
              note: "Identity/schema/version criteria constrain admissible tool writes."
            - value: enforcement
              basis: claimed
              records: [memory.md#mem-obj-page-metadata, runtime.md#rt-rte-session-capture]
              note: "Unsafe identity can make content read-only and stale versions are specified to refuse cooperating writes."
          records: [memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, runtime.md#rt-rte-session-capture, memory.md#mem-rte-cli-file]
          note: "External enforcement and direct-editor alternatives remain unresolved; no universal veto follows."
        - scope: "Retained criteria at calc assertion consumer"
          assessment: known
          findings:
            - value: validation
              basis: claimed
              records: [epistemic.md#epi-obj-sheet-expressions, epistemic.md#epi-rte-sheet-check]
              note: "Stored assertion defines a predicate checked over expressions; no enforcing admission consequence is established."
          records: [epistemic.md#epi-obj-sheet-expressions, epistemic.md#epi-rte-sheet-check]
          note: "Validation criterion is distinct from a demonstrated evaluator or downstream veto."
        - scope: "Search priority, external caches/editor effects and experience-driven revision of standing guidance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-recovery-records, memory.md#mem-obj-editor-pages, memory.md#mem-obj-writing-guide]
          note: "Search ranking and complete consumer effects are uninspected. Trace capture alone does not establish retained examples feeding a guidance-update consumer with learning authority."
      records: [runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose, runtime.md#rt-bap-guide-writing, memory.md#mem-obj-writing-guide, memory.md#mem-rte-component-consumption, memory.md#mem-obj-destination-metadata, memory.md#mem-obj-page-metadata, memory.md#mem-obj-table-types, runtime.md#rt-rte-session-capture, memory.md#mem-rte-cli-file, epistemic.md#epi-obj-sheet-expressions, epistemic.md#epi-rte-sheet-check, memory.md#mem-obj-recovery-records, memory.md#mem-obj-editor-pages]
      note: "Knowledge, instruction, routing and criteria/veto paths are distinct. No ranking or learning-authority value is inferred from a tool name or persistence alone."
    write_agency:
      assessment: partial
      units:
        - scope: "Ordinary session additions, setup page creation after agreed direction and routine agent/library repairs"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-setup, memory.md#mem-rte-wiki-maintenance, memory.md#mem-obj-page-metadata]
              note: "Agent/software admission does not wait for a human decision about each retained edit; workflow initiation is not content approval."
          records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-setup, memory.md#mem-rte-wiki-maintenance, memory.md#mem-obj-page-metadata]
          note: "Only the prescribed ordinary-write mechanisms are covered."
        - scope: "Existing-guide replacement, destructive schema changes, others' text retirement, destination/move choice and direct human editing/decision answers"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-rte-wiki-maintenance, memory.md#mem-rte-legacy-migration, runtime.md#rt-rte-team-transition, epistemic.md#epi-rte-block-choice]
              note: "These paths require an explicit human content, approval, replacement or destination decision."
            - value: manual
              basis: afforded
              records: [memory.md#mem-rte-cli-file]
              note: "People may directly edit the retained files."
          records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-rte-wiki-maintenance, memory.md#mem-rte-legacy-migration, runtime.md#rt-rte-team-transition, epistemic.md#epi-rte-block-choice, memory.md#mem-rte-cli-file]
          note: "Approval is scoped; it does not make subsequent additive migration sentences manually admitted."
        - scope: "Generic CLI/script/browser callers, initial corpus and complete hosted/editor admission behavior"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages, memory.md#mem-obj-page-prose, memory.md#mem-rte-component-consumption]
          note: "Caller identity and physical I/O do not determine per-content human control; initial content and external admission code are unavailable."
      records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-setup, memory.md#mem-rte-wiki-maintenance, memory.md#mem-obj-page-metadata, memory.md#mem-rte-legacy-migration, runtime.md#rt-rte-team-transition, epistemic.md#epi-rte-block-choice, memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages, memory.md#mem-obj-page-prose, memory.md#mem-rte-component-consumption]
      note: "Manual and automatic are supported for different admission mechanisms, without classifying every external writer."
    curation_operations:
      assessment: partial
      units:
        - scope: "Prescribed session-to-page selection and legacy-to-subject-page reshaping"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-rte-legacy-migration]
              note: "Selects decisions/context, excludes routine progress and compresses existing retained meanings into subject prose."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-rte-legacy-migration]
          note: "Classifies the requested transformation, not semantic fidelity of an actual output."
        - scope: "Prescribed duplicate merging, decision revision and outdated/archive withdrawal"
          assessment: known
          findings:
            - value: dedup
              basis: claimed
              records: [epistemic.md#epi-rte-doctor-repair]
              note: "Duplicate titles are directed to be merged into one page, beyond a collision check alone."
            - value: evolve
              basis: claimed
              records: [epistemic.md#epi-obj-decision-prose, epistemic.md#epi-rte-doctor-repair]
              note: "Changed decisions and affected page meaning are revised."
            - value: invalidate
              basis: claimed
              records: [memory.md#mem-rte-wiki-maintenance, runtime.md#rt-rte-team-transition]
              note: "Outdated marking and migrated archives withdraw current reliance without requiring physical erasure."
          records: [epistemic.md#epi-rte-doctor-repair, epistemic.md#epi-obj-decision-prose, memory.md#mem-rte-wiki-maintenance, runtime.md#rt-rte-team-transition]
          note: "These are prompt/format prescriptions, not inspected executed curation."
        - scope: "Novel-claim production, detailed editor/cache transformations and opaque external maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-rte-table-conversion]
          note: "No concrete output establishes a new claim rather than reshaping. Index rebuild, table conversion and purge alone do not establish an additional controlled curation operation."
      records: [runtime.md#rt-rte-session-capture, memory.md#mem-rte-legacy-migration, epistemic.md#epi-rte-doctor-repair, epistemic.md#epi-obj-decision-prose, memory.md#mem-rte-wiki-maintenance, runtime.md#rt-rte-team-transition, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records, memory.md#mem-rte-table-conversion]
      note: "Consolidation, deduplication, revision and withdrawal have claimed warrants; no wired implementation, synthesis, decay or promotion is inferred."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Foreground recall and guide reads"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-wiki-recall, runtime.md#rt-bap-guide-writing]
              note: "The consumer agent requests marks/pages or the guide, even when recall precedes code changes proactively."
          records: [runtime.md#rt-rte-wiki-recall, runtime.md#rt-bap-guide-writing]
          note: "Requested return is not a second push operation."
        - scope: "CLI/direct-file/browser reads and clicked retained prompts/templates"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption]
              note: "Documented people/callers request files, views or button-supplied retained content; no independent automatic selection is established for those clicks."
          records: [memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption]
          note: "Afforded consumers are not observed deployed callers."
        - scope: "SessionStart injection of retained local coverage/changed-file matches"
          assessment: partial
          findings:
            - value: push
              basis: claimed
              records: [runtime.md#rt-rte-host-entry]
              note: "Host event initiates unsolicited context supply; only command declarations are wired, not inspected retained-content selection."
          records: [runtime.md#rt-rte-host-entry]
          note: "Payload, budget and implementation remain unknown; Codex lacks this hook path."
        - scope: "Complete editor/transclusion model delivery and external alternative consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-editor-pages, memory.md#mem-rte-component-consumption, memory.md#mem-obj-recovery-records]
          note: "Renderer consumption is named, but complete payload selection/delivery and cache consumers are not established."
      records: [runtime.md#rt-rte-wiki-recall, runtime.md#rt-bap-guide-writing, memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption, runtime.md#rt-rte-host-entry, memory.md#mem-obj-editor-pages, memory.md#mem-obj-recovery-records]
      note: "Pull and claimed SessionStart push coexist with unresolved external delivery; Stop is a capture reminder, not retained-memory read-back."
    read_back_signal:
      assessment: partial
      units:
        - scope: "SessionStart supply of local wiki coverage"
          assessment: partial
          findings:
            - value: coarse
              basis: claimed
              records: [runtime.md#rt-rte-host-entry]
              note: "SessionStart triggers general coverage context from the local wiki without a topical consumer query."
          records: [runtime.md#rt-rte-host-entry]
          note: "The general coverage description is supported; actual selected fields, truncation and budget are not."
        - scope: "SessionStart changed-file-to-page targeting"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-host-entry, memory.md#mem-obj-page-metadata]
          note: "Changed-file matches are described, but the external hook selector and delivered parts are unknown. Globs or page IDs on a requested route do not prove identifier-based push."
        - scope: "Requested recall/guide/CLI reads and human-clicked components"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-wiki-recall, runtime.md#rt-bap-guide-writing, memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption]
          note: "These classified operations fulfill consumer requests rather than select unsolicited retained material; their keywords and IDs are not push signals."
        - scope: "Unresolved editor and external consumer delivery"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-editor-pages, memory.md#mem-rte-component-consumption]
          note: "No complete directional account permits declaring this alternative pull-only or choosing a push signal."
      records: [runtime.md#rt-rte-host-entry, memory.md#mem-obj-page-metadata, runtime.md#rt-rte-wiki-recall, runtime.md#rt-bap-guide-writing, memory.md#mem-rte-cli-file, memory.md#mem-rte-component-consumption, memory.md#mem-obj-editor-pages]
      note: "Only the general coverage push supports coarse selection. Unknown targeted hook selection prevents a complete signal assessment."
    trace_learning:
      assessment: partial
      units:
        - scope: "Ordinary session capture into retained subject-page prose for later recall/code context"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose]
              note: "Session traces feed agent-admitted durable prose that later invocations receive as context; per-edit human approval is not required."
          records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose]
          note: "The definition requires a trace-fed durable behavioral context path, not new knowledge or measured improvement. This path is prescribed, not wired or observed."
        - scope: "Direct CLI/script, initial/editor/hosted writes and possible host-generated continuation material"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages, runtime.md#rt-rte-host-entry, runtime.md#rt-rte-wiki-recall]
          note: "Admission, trace inputs and later shaping paths are not completely inspected. Host compaction is not established wiki memory and supplies no additional positive or negative."
      records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-wiki-recall, memory.md#mem-obj-page-prose, memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages, runtime.md#rt-rte-host-entry]
      note: "Claimed yes survives incomplete coverage. No evidenced-absence record supports a local or system-wide no; improved capacity and self-improvement remain unestablished."
    trace_source:
      assessment: partial
      units:
        - scope: "Conversation/current-session inputs consumed by ordinary capture"
          assessment: known
          findings:
            - value: session-logs
              basis: claimed
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-page-prose, epistemic.md#epi-obj-citation-inputs]
              note: "The original content is recorded coding-session conversation, including human decisions and available transcript quotes."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-page-prose, epistemic.md#epi-obj-citation-inputs]
          note: "Transcript citation availability differs by host; selection of session content does not require a quote on every write."
        - scope: "Mixed capture inputs from team comments/changed-file context and unresolved alternative write routes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-obj-citation-inputs, memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages]
          note: "Comment origin and complete raw content consumed by alternatives are not classified. Code files/Git diffs or tool-returned text alone do not prove tool-traces, event-streams or linked trajectories."
      records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-page-prose, epistemic.md#epi-obj-citation-inputs, memory.md#mem-rte-cli-file, memory.md#mem-obj-editor-pages]
      note: "Session-log origin is supported for the prescribed qualifying capture write; opaque mixed/alternative inputs prevent complete trace-source enumeration."
---

# Nimbalyst Wiki memory profile

## Comparison rationale

This profile classifies accepted records, not fresh source facts. Every positive retains its design or affordance basis. The wired manifests do not upgrade the external selectors, storage controls or prompt-directed transformations to wired memory behavior. No supplied run supports observation or causal benefit. No source files were read for this mapping.

The accumulated memory boundary includes page prose and the installed editable guide, not the static shipped skills. Local files and hosted collaborative objects are separate substrate units. Detailed editor representations, upstream citation storage and cache internals remain unresolved rather than inheriting the readable page body's classification. The local file contract is supplied by [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages); the material alternatives are recorded in [MEM-OBJ-editor-pages](memory.md#mem-obj-editor-pages), [MEM-OBJ-table-types](memory.md#mem-obj-table-types) and [MEM-OBJ-recovery-records](memory.md#mem-obj-recovery-records).

Reconciliation supersedes the epistemic writing-guide object with [MEM-OBJ-writing-guide](memory.md#mem-obj-writing-guide), and its legacy-reshape route with [MEM-RTE-legacy-migration](memory.md#mem-rte-legacy-migration). Those canonical records carry the classifications here. The guide's authority path, [RT-BAP-guide-writing](runtime.md#rt-bap-guide-writing), remains distinct. The page container and its prose, fields, guide and editor parts are not superseded by one another.

Ordinary capture is automatic admission at claimed basis because the agent selects wording and placement without per-edit approval. Approval for replacing an existing guide or retiring someone else's content is a separate manual mechanism. CLI invocation alone leaves the deciding principal unresolved. These distinctions follow [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup) and [MEM-RTE-cli-file](memory.md#mem-rte-cli-file).

Session-to-page selection supports claimed consolidation and trace learning: session material becomes durable prose intended for later agent context. This is not a finding of improved capacity, accepted novel knowledge or learning authority at a separate policy-update consumer. The downstream page consumer has knowledge authority; guide consumption separately has instruction authority. The semantic relation of a particular generated claim remains indeterminate, so the profile does not turn the word synthesis into a controlled synthesize finding. See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall) and [MEM-OBJ-page-prose](memory.md#mem-obj-page-prose).

Requested page reads and clicked component actions remain pull operations. The claimed SessionStart coverage delivery is a separate push stage. General coverage supports coarse selection, but the unknown changed-file selector does not establish an identity-match signal. In particular, symbolic coverage globs on the inspected pull route cannot classify the opaque hook. Neither the five-page advice nor manifest wiring establishes an enforced memory budget. See [RT-RTE-host-entry](runtime.md#rt-rte-host-entry), [RT-RTE-wiki-recall](runtime.md#rt-rte-wiki-recall) and [MEM-RTE-component-consumption](memory.md#mem-rte-component-consumption).

All ten inventories retain unresolved included alternatives. Their partial assessments indicate incomplete classification, not absence and not merely lack of execution evidence. The claimed trace-learning yes is retained; no bounded absence record supports no. Likewise, unknown search ranking, editor delivery and hosted enforcement prevent stronger authority or complete-value conclusions without suppressing the supported local paths.
