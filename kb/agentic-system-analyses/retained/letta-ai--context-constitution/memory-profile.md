---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Context Constitution memory comparison: declared persistent blocks, MemFS, discovery metadata, history and summaries without the executing harness."
run-id: AAS-2026-10-15-context-constitution-7a352d7408f6-01
source-identity: "https://github.com/letta-ai/context-constitution"
reviewed-boundary: "964f30137ace9eade1aef112992ed6539b61bbb0"
memory-comparison:
  version: 2
  scope: >-
    Agent memory accumulated or revised through use: system and external memory
    blocks, their Git-tracked MemFS projection, prose and opaque skill assets,
    curated discovery cues and automatic access metadata, retained conversation
    history, recursive compaction summaries, foreground and delegated maintenance,
    and later prompt or requested retrieval consumers. Automatic metadata is
    included as an access structure although its own persistence is unspecified.
    Environment context is included only as an alternate discovery/input surface,
    not attributed to agent-owned memory. Excluded are the static published
    Constitution, unmodified environment instructions, model weights and internal
    training, and publication-hygiene state. This is the declared policy artifact's
    memory loop, not a classification of an inspected Letta implementation.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Authoritative memory blocks underlying system and external memory"
          assessment: partial
          findings:
            - value: service-object
              basis: claimed
              records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory]
              note: "The declared underlying blocks are persistent host objects, distinct from their local file projection."
          records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory]
          note: "Logical block storage is described; backend substrate and initial representation are unspecified."
        - scope: "Local MemFS projection, external files and skill folders"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-mem-fs, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets]
              note: "The working projection and skill folders are files, not the canonical block store."
            - value: repo
              basis: claimed
              records: [memory.md#mem-obj-mem-fs, runtime.md#rt-rte-memory-admission]
              note: "Memory-file changes are declared Git-tracked and versioned, with remote push before propagation."
          records: [memory.md#mem-obj-mem-fs, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, runtime.md#rt-rte-memory-admission]
          note: "The local file/versioning boundary is classifiable without inferring synchronization implementation."
        - scope: "Compaction summary in the later inference buffer"
          assessment: partial
          findings:
            - value: in-memory
              basis: claimed
              records: [memory.md#mem-obj-summary-message, runtime.md#rt-rte-history-compaction]
              note: "The retained summary occupies the first message of the in-context buffer across later inference calls."
          records: [memory.md#mem-obj-summary-message, runtime.md#rt-rte-history-compaction]
          note: "Buffer placement is specified; backing persistence and prior-summary storage are not."
        - scope: "Raw message database and automatic metadata backing state"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata]
          note: "A database and automatic indexing are named without relational, vector or other backend facts; metadata persistence is unresolved."
      records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-mem-fs, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, memory.md#mem-obj-context-metadata, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message]
      note: "Inventory covers declared retained objects and access structures; opaque backend and summary persistence prevent complete substrate classification."
    representational_form:
      assessment: partial
      units:
        - scope: "System/external prose memories, durable learnings, textual history, summaries and descriptive discovery cues at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, memory.md#mem-obj-context-metadata, epistemic.md#epi-obj-durable-learnings]
              note: "The model interprets memories, conversation text, summaries and relevance descriptions as language."
          records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, memory.md#mem-obj-context-metadata, epistemic.md#epi-obj-durable-learnings]
          note: "This unit is limited to the explicitly described textual consumption paths, not every asset or provider payload."
        - scope: "MemFS addressing/protocol and history tool-call/search structure"
          assessment: partial
          findings:
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-mem-fs, memory.md#mem-obj-message-history]
              note: "File paths, commit/push protocol and structured tool/search identifiers have fixed addressing or protocol roles."
          records: [memory.md#mem-obj-mem-fs, memory.md#mem-obj-message-history]
          note: "These roles are distinguished from prose; raw serialization and provider-internal history forms are unspecified."
        - scope: "Non-prose skill payloads and their downstream consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill-assets]
          note: "Scripts/configuration could have symbolic interpreter semantics or be model-readable examples; no actual payload or consumer resolves the alternatives."
      records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-mem-fs, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, memory.md#mem-obj-context-metadata, memory.md#mem-obj-skill-assets, epistemic.md#epi-obj-durable-learnings]
      note: "Text and fixed addressing roles are positive findings; mixed skill assets and opaque raw payloads prevent a complete form union. No parametric memory update is established."
    lineage:
      assessment: partial
      units:
        - scope: "Subsequent foreground memory edits and curated discovery text"
          assessment: partial
          findings:
            - value: authored
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-context-metadata, epistemic.md#epi-obj-durable-learnings]
              note: "Agents compose guidance and indexes; humans may also edit memory files."
            - value: trace-extracted
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings]
              note: "Durable corrections and guidance are prescribed as products of accumulated experience."
          records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-context-metadata, epistemic.md#epi-obj-durable-learnings]
          note: "Known subsequent authorship/experience paths do not resolve initial content acquisition or every edit's derivation."
        - scope: "Recursive conversation summary"
          assessment: known
          findings:
            - value: trace-extracted
              basis: claimed
              records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
              note: "The declared summary is derived from prior conversation messages and, recursively, prior summaries."
          records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
          note: "The origin path is specified even though summarizer internals and semantic fidelity are not."
        - scope: "Automatically supplied skill/tree/count metadata"
          assessment: partial
          findings:
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-context-metadata]
              note: "The host automatically assembles access information from available skills, the memory tree and message counts."
          records: [memory.md#mem-obj-context-metadata]
          note: "The compilation role is declared; producer details, source-description provenance and refresh timing remain unresolved."
        - scope: "Initial block/external/skill contents, raw-history capture derivation and delegated maintenance outputs"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, memory.md#mem-obj-message-history, runtime.md#rt-rte-subagent-context]
          note: "Content initialization and asset provenance are unspecified; automatic raw logging alone does not identify a controlled derivation path, and delegate output transformations are opaque."
      records: [runtime.md#rt-rte-memory-admission, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata, memory.md#mem-obj-summary-message, epistemic.md#epi-obj-durable-learnings]
      note: "Authorship, experience extraction and automatic metadata compilation coexist; no imported lineage is inferred merely from the availability of environment-owned context."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "System memory at later model inference"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [memory.md#mem-obj-memory-blocks, runtime.md#rt-bap-system-prompt]
              note: "Retained preferences, goals and behavioral guidance supply standing model directions in the system preamble."
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-memory-blocks, runtime.md#rt-bap-system-prompt]
              note: "Retained identity and background context supply information to later inference."
          records: [memory.md#mem-obj-memory-blocks, runtime.md#rt-bap-system-prompt]
          note: "Both described content effects are model-interpreted, not enforced invariants; actual activation remains unobserved."
        - scope: "External prose and raw history at requested model consumption; summary at subsequent inference"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, runtime.md#rt-rte-context-disclosure, runtime.md#rt-rte-history-compaction]
              note: "Retrieved procedures, records and summarized past conversation provide context or advice to the model."
          records: [memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, runtime.md#rt-rte-context-disclosure, runtime.md#rt-rte-history-compaction]
          note: "Procedural advice here is not automatically standing system guidance or executable enforcement."
        - scope: "Curated and automatic discovery cues at foreground retrieval decisions"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
              note: "Retained descriptions and references guide the agent's choice of skill/file/history input to retrieve."
          records: [memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
          note: "Cue-based input selection is described, but no relative scoring or retained veto criterion is established."
        - scope: "Retained conversational experience at compaction and Reflection update consumers"
          assessment: known
          findings:
            - value: learning
              basis: claimed
              records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-subagent-context]
              note: "Conversation records feed durable summary production and conversation-based memory modification, separately from downstream context authority."
          records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-subagent-context]
          note: "Learning authority denotes the update input's role, not demonstrated improved capacity or accepted knowledge."
        - scope: "Opaque skill-asset consumers and particular delegated memory outputs"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill-assets, runtime.md#rt-rte-subagent-context]
          note: "No actual asset interpreter or delegate payload determines its force; capability names do not establish execution or enforcement."
      records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-context-metadata, memory.md#mem-obj-message-history, memory.md#mem-obj-summary-message, memory.md#mem-obj-skill-assets, runtime.md#rt-bap-system-prompt, runtime.md#rt-rte-context-disclosure, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-subagent-context]
      note: "Inventory separates inference guidance, routing and update-input authority. Opaque consumers remain unresolved; the file push gate is not itself retained memory with enforcement authority."
    write_agency:
      assessment: partial
      units:
        - scope: "Agent-selected foreground memory and index edits"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-context-metadata]
              note: "The model judges and admits its own durable text updates; no per-content operator approval is required by this route."
          records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-context-metadata]
          note: "File I/O and push are propagation stages, not evidence of human semantic approval."
        - scope: "Explicit human edits of projected memory files"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-mem-fs]
              note: "Humans can directly manipulate retained content through the projected files."
          records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-mem-fs]
          note: "This separately allowed operator-content decision does not make all other writes manual."
        - scope: "Automatic raw-message storage, metadata assembly and size-triggered compaction"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-history-compaction]
              note: "The host stores messages, supplies access metadata and produces the summary on a size trigger without a described per-content human decision."
          records: [memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-history-compaction]
          note: "Host automation is explicit at design level; summary quality and implementation are separate unknowns."
        - scope: "Initial content, direct bespoke memory tools, delegated write admission and desired external fact checkpoint"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, runtime.md#rt-rte-memory-admission, runtime.md#rt-rte-subagent-context, runtime.md#rt-rte-history-compaction]
          note: "Initial admission, alternate-tool control, delegate veto/merge ownership and fact-extraction producer are unspecified; agent proposal or workflow launch cannot resolve per-content approval."
      records: [runtime.md#rt-rte-memory-admission, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-memory-blocks, memory.md#mem-obj-external-memory, memory.md#mem-obj-skill-assets, memory.md#mem-obj-mem-fs, memory.md#mem-obj-context-metadata, memory.md#mem-obj-message-history]
      note: "Manual and automatic mechanisms are both declared; unresolved initial, direct-tool and delegated gates prevent a universal admission classification."
    curation_operations:
      assessment: partial
      units:
        - scope: "Host recursive history-to-summary transformation"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
              note: "The declared transformation reduces accumulated messages into summarized prior context; retaining the raw history does not negate consolidation."
          records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
          note: "The specified operation is consolidation at doctrine level, not inspected execution or guaranteed faithfulness."
        - scope: "Foreground maintenance of existing memories"
          assessment: partial
          findings:
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings]
              note: "The policy's edit/refinement route revises existing assumptions and behavioral guidance."
            - value: consolidate
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-external-memory]
              note: "Compression of existing retained content is a declared maintenance option."
            - value: decay
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission]
              note: "Deleting retained memory is a declared forgetting operation, distinct from merely releasing loaded context."
          records: [runtime.md#rt-rte-memory-admission, memory.md#mem-obj-external-memory, epistemic.md#epi-obj-durable-learnings, epistemic.md#epi-rte-pruning-assessment]
          note: "These are described maintenance actions only; unspecified concrete updates do not establish synthesis, deduplication, promotion or history-preserving invalidation."
        - scope: "Reflection, Defragmentation, desired fact extraction and opaque skill-asset transformations"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-subagent-context, runtime.md#rt-rte-history-compaction, memory.md#mem-obj-skill-assets]
          note: "Memory modification/organization role names and a desired extracted-fact checkpoint do not identify particular controlled transformations or implementation."
      records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, runtime.md#rt-rte-memory-admission, memory.md#mem-obj-external-memory, epistemic.md#epi-obj-durable-learnings, epistemic.md#epi-rte-pruning-assessment, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets]
      note: "Only the specified transformations receive claimed findings; none is wired or observed. Opaque maintenance branches remain unresolved rather than inheriting the compaction classification."
    read_back_direction:
      assessment: partial
      units:
        - scope: "System memory and discovery metadata supplied in later prompts"
          assessment: known
          findings:
            - value: push
              basis: claimed
              records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
              note: "The host supplies system memory and available skill/tree/count metadata without a content-specific retrieval request."
          records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
          note: "Unsolicited baseline supply is distinct from subsequent agent-requested expansion."
        - scope: "External files/skills and stored history requested by the foreground agent"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-context-disclosure, memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history]
              note: "The agent requests full retained content through file reads or history search/list; returning that request is not an additional push."
          records: [runtime.md#rt-rte-context-disclosure, memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history]
          note: "Relevance reasoning precedes an explicit request in the disclosed workflow."
        - scope: "Compaction summary carried into later inference"
          assessment: known
          findings:
            - value: push
              basis: claimed
              records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
              note: "The host installs a summary as the first buffer message after the size trigger, independently of a request for that retained summary."
          records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
          note: "This within-conversation continuation is read-back because a later inference receives retained derived context."
        - scope: "Delegate retained inputs/returns, non-prose skill consumers and desired extracted-fact checkpoint"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets, runtime.md#rt-rte-history-compaction]
          note: "Exact delegated context construction and returns, asset consumption and a particular fact checkpoint's later delivery are unspecified. Shared memory alone does not resolve these operations."
      records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure, memory.md#mem-obj-external-memory, memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets]
      note: "Both requested content and unsolicited prompt/summary supply are declared. Unresolved delegate and asset paths prevent complete direction coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Baseline system memory and automatic discovery-metadata push"
          assessment: known
          findings:
            - value: coarse
              basis: claimed
              records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
              note: "Each inference triggers system-memory supply; available agent/environment skills and the current tree/history counts determine broad metadata inclusion, not a targeted content identity match."
          records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure]
          note: "The described push selects baseline classes by placement/availability. Agent relevance judgments subsequently request full files and do not classify this push as inferred-judgment."
        - scope: "Size-triggered summary push"
          assessment: partial
          findings:
            - value: coarse
              basis: claimed
              records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
              note: "Exceeding the host's context-size threshold triggers replacement of old history by a supplied summary; old conversational context is the broadly selected retained input."
          records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message]
          note: "Threshold/age selection is described; internal summarizer content selection, retained tail and exact thresholds are not, preventing a complete signal classification."
        - scope: "Agent-requested file/skill/history delivery"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-context-disclosure]
          note: "This unit is explicit pull, not automatic push. Paths identify requested objects but establish no identifier-based push."
        - scope: "Delegated/opaque asset supply and desired fact-checkpoint delivery"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets, runtime.md#rt-rte-history-compaction]
          note: "Unresolved delivery direction and selectors prevent signal findings; a known pull route cannot make these alternatives inapplicable."
      records: [runtime.md#rt-bap-system-prompt, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-context-disclosure, runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets]
      note: "Coarse automatic supply is supported at design level; no targeted identity, lexical, embedding or judgment push selector is established for full retained content. Opaque alternatives remain included."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic conversation compaction to retained continuation summary"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, memory.md#mem-obj-message-history]
              note: "The host automatically derives a retained summary from conversational traces and supplies it to later inference as context."
          records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, memory.md#mem-obj-message-history]
          note: "This meets the trace-fed write definition by doctrine; no novelty, observed operation or demonstrated improvement is implied."
        - scope: "Model-selected durable experience-based foreground edits"
          assessment: partial
          findings:
            - value: "yes"
              basis: claimed
              records: [runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings, runtime.md#rt-bap-system-prompt]
              note: "The policy directs the model to turn accumulated experience into durable corrections and guidance for future prompt or retrieval consumption without mandatory per-content human approval."
          records: [runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings, runtime.md#rt-bap-system-prompt]
          note: "The prescribed trace-fed branch qualifies; concrete inputs and actual writes are unspecified, and this does not classify every edit as trace-fed."
        - scope: "Reflection admission, other delegated maintenance, initial/alternate-tool writes, non-prose assets and desired extracted-fact checkpoint"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-subagent-context, runtime.md#rt-rte-memory-admission, memory.md#mem-obj-skill-assets, runtime.md#rt-rte-history-compaction]
          note: "Reflection reviews conversations to change memory, but final admission control and outputs are unspecified; other branches lack a complete automatic trace-to-artifact-to-consumer chain."
        - scope: "Raw history storage, automatic access metadata and explicit human content edits considered alone"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-memory-admission]
          note: "Plain trace retention is not a derived behavior-shaping update; counts/tree metadata alone establish no such artifact, and explicit human edits are not automatic admission. These local exclusions do not negate qualifying routes."
      records: [runtime.md#rt-rte-history-compaction, memory.md#mem-obj-summary-message, memory.md#mem-obj-message-history, runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings, runtime.md#rt-bap-system-prompt, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets, memory.md#mem-obj-context-metadata]
      note: "Positive design routes coexist with unresolved admissions and transformations. No system-wide negative or exercised learning conclusion is inferred."
    trace_source:
      assessment: partial
      units:
        - scope: "Original trace inputs to automatic conversation compaction"
          assessment: known
          findings:
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction]
              note: "Recorded user/system/assistant conversation turns feed the summary, including recursively summarized prior conversational context."
            - value: tool-traces
              basis: claimed
              records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction]
              note: "The described message history also contains recorded tool calls and returns consumed as conversational context by compaction."
          records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction]
          note: "Classification follows the specified mixed message contents, not a journal label; recursive summaries do not change their original trace origins."
        - scope: "General experience feeding foreground durable edits"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings]
          note: "The policy names accumulated experience but does not identify the original inputs of a particular durable edit, preventing a controlled trace-source inventory for this route."
        - scope: "Reflection and other unresolved automatic-write alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-subagent-context, runtime.md#rt-rte-memory-admission, runtime.md#rt-rte-history-compaction, memory.md#mem-obj-skill-assets]
          note: "Conversation review is a candidate origin for Reflection, but qualifying automatic admission is unresolved; alternate-tool writes, asset transformations and desired extraction lack complete qualifying chains and source inventories."
        - scope: "Plain raw storage/access metadata and explicit human edits alone"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-message-history, memory.md#mem-obj-context-metadata, runtime.md#rt-rte-memory-admission]
          note: "These isolated mechanisms are not qualifying automatic trace-fed behavior-shaping writes; the same raw messages remain a source for the separately qualifying compaction route."
      records: [memory.md#mem-obj-message-history, runtime.md#rt-rte-history-compaction, runtime.md#rt-rte-memory-admission, epistemic.md#epi-obj-durable-learnings, runtime.md#rt-rte-subagent-context, memory.md#mem-obj-skill-assets, memory.md#mem-obj-context-metadata]
      note: "Session and tool traces are declared inputs to compaction; generic experience and unresolved admission routes prevent complete source coverage. No event-stream or multi-step-trajectory input is established."
---

# Context Constitution memory profile

## Comparison rationale

All positive findings have **claimed** basis. The accepted records describe a
policy and external host affordances, not inspected memory implementation or
execution. A unit can therefore have known classification at a declared path
without wired or observed evidence. Partial axes retain opaque initial content,
provider storage, mixed skill assets, alternate write gates and delegated
consumers rather than excluding them to obtain completeness. The inventory and
those limits come from the memory objects and annotations on
[RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission),
[RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure),
[RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) and
[RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context).

The summary identity supersession affects every summary-related axis: citations
use canonical [MEM-OBJ-summary-message](memory.md#mem-obj-summary-message), not
the superseded epistemic summary declaration. The amendment changes identity
resolution, not evidence strength or fidelity. No other supersession changes a
value. [EPI-OBJ-durable-learnings](epistemic.md#epi-obj-durable-learnings) remains
a content class within the update route, not a replacement for the block,
external-memory or projection objects.

Logical memory blocks map to service objects, while their working projection
maps separately to files and a repository. A named message database does not
establish relational storage, SQLite or vectors. Summary buffer placement does
not establish durable backend storage or a history of summary versions. These
limits are retained in [MEM-OBJ-memory-blocks](memory.md#mem-obj-memory-blocks),
[MEM-OBJ-mem-fs](memory.md#mem-obj-mem-fs),
[MEM-OBJ-message-history](memory.md#mem-obj-message-history) and
[MEM-OBJ-summary-message](memory.md#mem-obj-summary-message).

Automatic baseline supply is coarse push; requested full-content delivery is
pull. The foreground relevance judgment in
[RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure) selects what to
request, not an additional unsolicited delivery. References and paths therefore
do not establish identifier-based push. Curated discovery material has routing
force at that decision, while retrieved content supplies advice or context;
standing system memory separately supplies instructions. No ranking,
validation or enforcement value follows from a catalog, relevance judgment or
file-propagation gate alone. Opaque skill consumers remain unresolved under
[MEM-OBJ-skill-assets](memory.md#mem-obj-skill-assets).

Compaction qualifies as consolidation and trace learning because an automatic
trace-fed summary becomes context for later inference. This mapping does not
assert semantic preservation: the epistemic account's indeterminate content
relation and missing fidelity checks remain compatible with a declared
summarization operation in
[RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction). Its mixed
session/tool origins come from
[MEM-OBJ-message-history](memory.md#mem-obj-message-history). Retained traces
have learning authority at that update consumer, separately from the summary's
knowledge authority at later inference. Neither authority nor the trace-learning
value establishes improved capacity.

Foreground text revision, compression and deletion support claimed evolve,
consolidate and decay operations on the described maintenance branch. Merely
moving material out of the active window is not forgetting it, and pruning
confidence is not semantic rejection or history-preserving invalidation. The
unresolved transformations of Reflection and Defragmentation receive no
operation by role name. The relevant boundaries are
[RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission),
[EPI-RTE-pruning-assessment](epistemic.md#epi-rte-pruning-assessment) and
[RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context).

Source-read log: none. Classification used only the supplied accepted members
and their reconciliation; no frozen source file, incumbent profile or reference
profile was read.
