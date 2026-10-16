---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Context Constitution memory: declared memory blocks, discovery metadata, raw history, compaction summaries and isolated maintenance without a shipped harness."
run-id: AAS-2026-10-15-context-constitution-7a352d7408f6-01
source-identity: "https://github.com/letta-ai/context-constitution"
reviewed-boundary: "964f30137ace9eade1aef112992ed6539b61bbb0"
---

# Context Constitution memory report

## Boundary and evidence

This report covers the published context-management policy, not an executing Letta installation. The frozen boundary and source register are [boundary](boundary.md). Direct reads covered all of `constitution/CONSTITUTION.md` and `constitution/AFFORDANCES.md` in SRC-1. Their evidence layer is doctrine/design. Supplied runtime findings organize the analysis but do not establish implementation or operation. Git HEAD matched the reviewed commit and the checkout was clean. The tracked-path inventory was rechecked; it exposes no CLI dispatch, hooks, tool registration or library/service implementation to trace. Tool descriptions here are declared interfaces, not inspected registrations.

Included are system memory, external memory and skills, their local projection, automatic and curated indexes, raw message storage, recursive compaction, retrieval, pruning and delegated memory maintenance. Environment context is included as an alternate input, not as agent-owned persistent memory. Model weights and internal training are outside this memory mechanism account; [RT-CMP-underlying-model](runtime.md#rt-cmp-underlying-model) retains their separate uncertainty. Runtime storage, synchronization, authorization, search, summarizers and evaluator implementations are not shipped. No observed runs or causal experiments support actual retention, activation or benefit.

| Entry point or operation | Directly inspected source in SRC-1 | Coverage and limit |
|---|---|---|
| Always-visible memory; file-based editing and push | `constitution/AFFORDANCES.md`, Storage and management of context | [MEM-OBJ-memory-blocks](#mem-obj-memory-blocks), [MEM-OBJ-mem-fs](#mem-obj-mem-fs); annotation on [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). No deployed prompt or synchronization code. |
| Bespoke memory tools; human edits | `constitution/AFFORDANCES.md`, MemFS | Same admission annotation. Alternate tool gate unresolved; successful push applies specifically to file changes. |
| External memory and skill discovery | Both documents, progressive disclosure and MemFS layout | [MEM-OBJ-external-memory](#mem-obj-external-memory), [MEM-OBJ-skill-assets](#mem-obj-skill-assets), [MEM-OBJ-context-metadata](#mem-obj-context-metadata); annotation on [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure). No schemas or execution grants. |
| Automatic indexing and system-prompt metadata supply | `constitution/AFFORDANCES.md`, Indexing context and Message History | Metadata/history objects and disclosure annotation distinguish automatic supply from requested full-content delivery. No ranking or budget implementation. |
| History search/list within or across conversations | `constitution/AFFORDANCES.md`, Message History and Conversations | [MEM-OBJ-message-history](#mem-obj-message-history); disclosure and subagent annotations. No deployed search scope or permissions. |
| Threshold compaction; recursive summary; fact extraction | Both documents, Messages, Compaction and Ideal Context | [MEM-OBJ-summary-message](#mem-obj-summary-message); annotation on [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction). Fact extraction is prescribed, not shown as a separate automatic checkpoint. |
| Recall, Reflection, Defragmentation and self-conversation | `constitution/AFFORDANCES.md`, Conversations and Subagents | Annotation on [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context). Inputs, outputs, admission and concurrent merge details unresolved. |
| Evaluation, correction, removal and conservative pruning | `constitution/CONSTITUTION.md`, Context as Memory, System Prompt Learning, Efficiency, Ideal Context | Write-side analysis and admission annotation. Questions and desired outcomes are not an evaluator implementation or evidence of semantic rejection. |
| Environment instructions, skills and curated files | `constitution/AFFORDANCES.md`, Environment-scoped versus agent-scoped context | External-memory and metadata objects. Ownership distinguished; ingestion/trust policy and cross-environment reconciliation unresolved. |

## Core ideas

The policy separates durable raw experience from curated behavioral guidance. Automatic message retention is the recovery substrate; durable prompt changes should generalize rather than repeat every event. The significance of a retained item depends on its delivery: `/system` content is declared always visible; external memory needs an in-context discovery cue and an explicit read. These are different behavioral-authority paths, not interchangeable storage labels (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`; [RT-BAP-system-prompt](runtime.md#rt-bap-system-prompt)).

> Learning should be done in a **general way**. Letta agents should not expect future situations to only repeat exact past circumstances.
> --- `constitution/CONSTITUTION.md`

Navigation itself is a retained product. A temporal reference that identifies useful interactions adds a future retrieval path even where copying an event description would add redundant content. Automatic skill/file-tree metadata and agent-authored links have different producers. Neither establishes that a later agent notices the cue or loads the right item ([MEM-OBJ-context-metadata](#mem-obj-context-metadata)).

Budgeting is qualitative: minimize baseline tokens, load relevant detail, reserve reasoning headroom and remove stale content. No per-item quota, relevance score, numerical compaction threshold or guaranteed eviction primitive is supplied. Identity-preserving conservatism is a counterexample to reading efficiency as unconditional token minimization (SRC-1, `constitution/CONSTITUTION.md`; [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)).

> Efficiency should not come at the cost of losing the Letta agent’s identity, as this breaks the continuity of Letta agents and their experiential nature that is core to Letta agents.
> --- `constitution/CONSTITUTION.md`

Source ownership is explicit but trust enforcement is not. The documents distinguish user/system inputs, tool returns, agent outputs, agent-owned memory and environment-owned context. They do not supply a provenance-validation or instruction-sanitization mechanism before these reach inference. A skill label does not establish executable permission, and a Git push does not establish semantic truth (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-blocks
Label: Memory blocks

The underlying memory blocks are the declared authoritative persistent memory substrate; the local filesystem is a projection, not the canonical state. `/system` files project the natural-language identity, preferences, goals and behavioral guidance delivered in the system prompt. These contents are interpreted by the underlying model, not enforced as fixed symbolic rules. Initial block population and backend representation are unspecified. Subsequent agent/human edits are described; external memory is treated separately below. The closest supplied records are the write route [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) and consumer path [RT-BAP-system-prompt](runtime.md#rt-bap-system-prompt), not duplicate objects. Source: SRC-1, `constitution/AFFORDANCES.md`.

> - **In-context memory**: Memory files contained in `/system` represent in-context memories stored inside in the Letta agent’s system prompt (visible at all times)
> --- `constitution/AFFORDANCES.md`

#### MEM-OBJ-mem-fs
Label: Memory Filesystem (MemFS)

MemFS is the local-device projection of agent-owned memory and skills. Storage is files, with declared Git tracking/versioning; content form depends on the projected part. Paths and commit/push operations have symbolic addressing/protocol roles, while prose memories remain natural language. This is a distinct working copy with a separate propagation gate, not an additional authoritative memory store. Human and agent filesystem manipulation are both allowed by the description. Git history does not establish an implemented restore procedure. Source: SRC-1, `constitution/AFFORDANCES.md`; the closest supplied referent is its update route [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), whose quoted push rule supplies the evidence passage.

#### MEM-OBJ-external-memory
Label: External memory

Agent-owned external memory is projected to non-`/system` files, with procedural skills in `/skills`. Its text and Markdown documents provide natural-language knowledge or guidance when read. Full contents are not always in the prompt; an index is. Persistence is declared to span environments, unlike environment-owned AGENTS.md/CLAUDE.md, project skills and curated files. Initial content acquisition and validation are unspecified; later curation can create, delete, compress, expand and reorganize content. At inference the text is interpreted guidance or background knowledge, not necessarily system-prompt authority. Source: SRC-1, `constitution/AFFORDANCES.md`, `constitution/CONSTITUTION.md`.

> - **External memory**: External memory files (contained in non-`/system` directories) follow the principle of progressive disclosure: an index of the memories is kept in the system prompt, but the full contents of the memories must be retrieved on-demand (e.g. by reading the full file contents in the MemFS projection). Skills are a special type of external memory for procedural knowledge stored in the `/skills` top-level folder.
> --- `constitution/AFFORDANCES.md`

The closest supplied record, [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure), is the consumption route rather than this retained collection. Skill non-prose assets are separated below because they can have different consumers.

#### MEM-OBJ-skill-assets
Label: Skill scripts and other assets

Skills may retain scripts, data, configuration, templates and example code alongside prose. Their substrate is a skill folder; initial provenance and actual payloads are not supplied. A script/configuration used by an interpreter has symbolic consumer rules; a displayed example interpreted by the model has a different consumption path. No payload, interpreter, invocation gate or downstream execution is shown, so this is an explicitly opaque mixed-asset surface, not a claim that every skill asset runs. It differs from the textual knowledge in [MEM-OBJ-external-memory](#mem-obj-external-memory). The closest supplied record [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) already flags asset heterogeneity, but declares no asset object. Source: SRC-1, `constitution/CONSTITUTION.md`.

> Skills are folders of reusable, on-demand context — not just text files, but structured collections of markdown documents, scripts, data, and other assets that the Letta agent can discover, explore, and manipulate.
> --- `constitution/CONSTITUTION.md`

#### MEM-OBJ-context-metadata
Label: Context metadata and indexes

Two producers contribute to the model-visible discovery layer. The system automatically includes available agent/environment skills and information about message counts and the MemFS tree. The agent maintains additional descriptions, indexes and links in its system prompt. Descriptions are natural-language relevance cues; paths/references identify retrievable objects. Counts and tree metadata describe access, not the memories' substantive content or an embedding index. Metadata generation internals, persistence of automatic metadata and exact refresh timing are unspecified. Curated links persist as edited memory text. Later foreground inference uses cues to decide whether to retrieve full content. Source: SRC-1, `constitution/AFFORDANCES.md`, `constitution/CONSTITUTION.md`.

> The Letta agent is responsible for maintaining additional metadata in its system prompt for additional indexing of context outside of the current context window.
> --- `constitution/AFFORDANCES.md`

> * **Skills metadata:** The system prompt automatically contains available skills (both the Letta agent's own skills, as well as skills in the current environment)
> --- `constitution/AFFORDANCES.md`

This is distinct from the route [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure), and from its full-content endpoints. No dense vector store or embedding provenance can be inferred from the word “indexed.”

#### MEM-OBJ-message-history
Label: Message history

This is raw retained conversational experience, not already-generalized memory: user/system inputs, reasoning traces, assistant outputs, tool calls and returns. The Constitution describes a database; Affordances says automatic storage/indexing permits search/list across or within conversations. Textual messages have natural-language consumption paths, while tool-call structure and search identifiers can have symbolic roles; no backend schema, raw serialization or reasoning-payload visibility policy is supplied. The readable message description is not proof of access to all opaque provider state. Same-agent conversations have isolated message threads but shared memory. Source: SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`.

> The Letta agent can see the current in-context messages, which include user messages, assistant messages, system messages, and tool calls and tool returns. All messages are automatically stored and indexed, so are always accessible to the Letta agent, but may not be currently in the context window.
> --- `constitution/AFFORDANCES.md`

Closest supplied records are [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) and [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure); this declares their retained raw input/retrieval object, not duplicate routes. “All” and unbounded storage are design claims, not verified capacity, retention or retrieval guarantees.

#### MEM-OBJ-summary-message
Label: Summary message

The compaction product is derived natural-language conversation context plus references to files or prior messages. Its declared substrate is the first message in the in-context buffer. Old messages are periodically replaced by recursive summaries; the raw messages remain separately retrievable. The summarizer, storage of prior summary versions, exact verbatim tail and semantic preservation checks are unspecified. It carries prior material to a later inference even within one conversation, and therefore is retained memory rather than mere transient accumulation. Source: SRC-1, `constitution/AFFORDANCES.md`, `constitution/CONSTITUTION.md`. Closest supplied record [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction) declares the transformation and quotes the summary/reference contract, not this object.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Memory-specific lineage is experience or current memory → model/human-selected edits → local MemFS files → committed and successfully pushed state → underlying memory blocks → future prompt or on-demand retrieval. Known subsequent transformations coexist with unknown initialization. Physical editing and pushing do not identify the semantic approver: agents judge their own incremental updates; humans can edit; no universal per-content human approval is specified. Direct bespoke memory tools are an alternative, not evidence that every update traverses the file gate (SRC-1, `constitution/AFFORDANCES.md`; supplied route's push quotation).

Stored results can be generalized corrections, preferences, behavior rules, identity text, procedural text or discovery links. These are derived memory, unlike the automatically retained raw transcript. They influence later inference as prompt guidance or retrieved content, not parametric updates. The source instructs observation/refinement of effects, but does not establish that reasons, challenged assumptions, rejected candidates or outcome evidence accompany each saved rule. Raw history can retain circumstances; neither a mandatory rationale link nor a later rationale-reading route is prescribed (SRC-1, `constitution/CONSTITUTION.md`; supplied route's verification quotation).

#### On [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)

The retained inputs are curated cue text, skill descriptions, file tree and message-history information, plus the full external/history material to which they lead. Automatic inclusion of skills metadata, tree and message count is a declared host-to-prompt supply path, independent of an agent's specific file request. Curated links and descriptions are agent-maintained; their later interpretation supplies relevance targeting. A requested file address identifies the object to return but does not prove that relevance selection succeeded (SRC-1, `constitution/AFFORDANCES.md`, `constitution/CONSTITUTION.md`; [MEM-OBJ-context-metadata](#mem-obj-context-metadata)).

The foreground model is the later consumer. A current situation can trigger examination of skill metadata and then full content; history may instead be searched/listed, including across conversations. Detail is loaded on demand via the declared tools/filesystem and interpreted in subsequent inference. Exact result formatting and retrieval limits are uninspected. No numerical budget or scoring algorithm is given; “minimal baseline” and release-after-use are policy objectives. In contrast, `/system` content reaches every invocation without a content-specific request. Delivery does not establish compliance, correct retrieval or benefit. Loaded skill release is prescribed but no precise removal primitive or expiration policy is exposed (SRC-1, both documents; supplied disclosure quotation and [RT-BAP-system-prompt](runtime.md#rt-bap-system-prompt)).

#### On [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)

Trace lineage is mixed user/system/assistant/tool experience → accumulated messages (and prior summaries under recursive compaction) → host-triggered summary with references → later inference. The host triggers at a specified size; selector inputs, threshold, summarizer and quality checks are not supplied. Older history is preferentially removed from the window; the first-message summary remains, while raw messages remain declared reachable through active tools. The exact verbatim tail is unknown. This is an automatic trace-fed transformation, but no inspected implementation or observed successful write exists (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`; [MEM-OBJ-message-history](#mem-obj-message-history), [MEM-OBJ-summary-message](#mem-obj-summary-message)).

The alternative desired form is recent turns plus summary with key facts extracted to external memory. The Constitution prescribes it; it does not identify an automatic extraction producer, admission gate, checkpoint schema or later read of a particular extracted fact. Summary references can support later reconstruction of reasons, but required rationale retention and actual reason retrieval are unestablished. No human approval, semantic rejection, before/after test, summary rollback or repair loop is described. These are unknowns, not absent runtime capabilities (SRC-1, `constitution/CONSTITUTION.md`).

> A well-managed context window has a stable, compressed system prompt that changes only when a learning is truly durable. Conversation history beyond the most recent turns is summarized, with key facts extracted to external memory.
> --- `constitution/CONSTITUTION.md`

#### On [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context)

Recall is a history-retrieval role; Reflection reviews conversations to modify memory; Defragmentation reviews memory to improve organization. Reflection is a declared raw-trace-to-derived-memory pathway, while Defragmentation need not originate from new traces. Their retained products feed the same future memory consumers, but exact output, access grants, admission, rationale retention and merge semantics are unspecified. Names do not establish successful reflection or semantic improvement (SRC-1, `constitution/AFFORDANCES.md`).

> * Recall: Specialized in recalling past conversations
> * Reflection: Specialized in reviewing conversations to make modifications to memory
> * Defragmentation: Specializes in reviewing memory and improving its structure and organization
> --- `constitution/AFFORDANCES.md`

The agent invokes isolation/background work; exact trigger scheduling and chosen inputs are not defined. Intermediate conversation context stays outside the foreground thread, reserving its window. A self-conversation nevertheless shares memory: persistent changes can cross the boundary even without a disclosed return payload. Thus a separate-context/task-frame analogy describes message isolation only; return-only effects, automatic frame disposal and reclamation of external memory do not follow. Loaded context is received by value, while discovery paths enable later explicit reads, not automatic pointer following. No supplied execution establishes context savings or write/read activation (SRC-1, `constitution/AFFORDANCES.md`; supplied route's shared-memory quotation).

## Write side

The durable-update policy asks agents to incorporate corrected assumptions, user preferences and refined behavior/identity guidance incrementally. The proposed selector is the agent's judgment of future value, not an explicit reward or reference-answer oracle. The operating mode is ongoing experience, not a bounded experiment. Human filesystem authorship is allowed; human semantic approval is not required by the published contract. Model-selected curation, physical writes and harness synchronization are separate stages ([RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) and its annotation).

There are three other write mechanisms with distinct admission uncertainty: automatic raw-message storage, automatic compaction and specialized delegated maintenance. Raw storage is not by itself a learned rule. Compaction transforms trace content into a later inference input; Reflection proposes or makes memory changes from conversations; Defragmentation reorganizes existing memory. The source does not state whether delegated writes use MemFS, bespoke memory tools or another path, or who can veto them. Automatic metadata is additional derived access information, not evidence of semantic generalization ([MEM-OBJ-message-history](#mem-obj-message-history), [MEM-OBJ-context-metadata](#mem-obj-context-metadata), annotations above).

Evaluation consists of self-assessment questions, prompts to examine prior conversations and a request to observe/refine updates. No shipped memory-quality evaluator, rejection log or retained comparison result establishes that a bad memory was identified, rejected or withdrawn. Lack of explicit reward is not proof that evaluation never occurs; the source itself asks for continuing observation (SRC-1, `constitution/CONSTITUTION.md`; supplied admission route).

Removal can mean deleting a retained memory, compressing/reorganizing it, moving guidance out of `/system`, or releasing task-specific loaded content. These have different consequences. Removing `/system` text withdraws automatic future delivery; relocation with an index preserves conditional access. The policy requires confidence in future retrieval before such relocation and warns against erasing identity. Historical copies may remain in Git or raw messages, but no global deletion propagation, rollback, revocation or cache-invalidation implementation is supplied. A failed/absent push does not admit local file changes into canonical blocks; neither conflict recovery nor semantic rejection follows from Git versioning (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

> Context should only be removed from the in-context memory and placed externally if the Letta agent is confident that it has laid the groundwork (e.g. through updating its index) to retrieve the context reliably when necessary in the future.
> --- `constitution/CONSTITUTION.md`

## Read-back

Four consumer chains distinguish retention from availability. System memory and curated discovery cues are supplied in the later prompt; automatic skill/tree/history metadata is also supplied without a specific retrieval request. An agent then requests full skills, files or historical messages using current task relevance and the retained cues. Host compaction independently replaces old context with a summary that later inference receives. Delegates can recall history or modify shared memory, but their foreground return channel is unspecified. The route annotations retain triggers, selectors, persistence and delivery limits rather than inferring an unspecified API caller ([RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure), [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction), [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context)).

At the update consumer, historical experience is intended to shape edits. At the downstream inference consumer, edited text is guidance/knowledge; compaction text reconstructs prior conversational context. No exact saved item is traced into an actual subsequent decision. The policies therefore support a declared retention-and-consumption design, not exercised learning, reflection, self-improvement or benefit. The independent theory and self-improvement assessments in [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) remain bounded accordingly. A stored reason would need its own delivered-content and use evidence; availability of raw history alone does not supply it.

## Integration issues

- No correction to a supplied fact is required. The added objects distinguish endpoints and material parts of supplied routes; none duplicates a supplied operative-object record. [RT-OBJ-context-constitution](runtime.md#rt-obj-context-constitution) is the published policy, not the runtime memories described here. Route annotations reuse supplied identities rather than redeclare them.
- Automatic metadata supply must not be collapsed into agent-requested full-content retrieval. Both occur in [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure), but have different selectors, content and channels; [MEM-OBJ-context-metadata](#mem-obj-context-metadata) preserves those facts. Host generation/refresh details remain unknown, preventing implementation-level completeness claims.
- File push gating is only one admission mechanism. Direct memory tools and delegated writes have unresolved gates; see [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context), [MEM-OBJ-mem-fs](#mem-obj-mem-fs). No universal human veto, semantic validation or push requirement across all writes is established.
- Summary/reference delivery is declared, but exact retained tail, rationale preservation, prior-summary storage and automatic fact extraction are unresolved. See [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction), [MEM-OBJ-message-history](#mem-obj-message-history), [MEM-OBJ-summary-message](#mem-obj-summary-message). This prevents claims of losslessness or a fully wired raw-to-extracted-memory checkpoint route.
- Skill assets have consumer-dependent forms and unresolved execution gates; [MEM-OBJ-skill-assets](#mem-obj-skill-assets) must not inherit the natural-language semantics of all external prose. The declared assets do not establish execution or authority to execute.
- Shared memory can carry delegated effects despite isolated conversations. Exact handoff payload, concurrency, failed-job recovery and authorization remain unknown in [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context). Isolation must not be summarized as return-only or a security boundary.

## Limitations and checks

Only the published policy and affordance descriptions were directly inspected as memory evidence. No deployed prompt contents, persisted memory instance, search result, compaction output, retained criticism/revision episode or later consumer trace is available in SRC-1. Those gaps prevent implementation, exercised behavior, correctness and benefit claims; they do not negate the explicit design. The strong claims of infinite storage and context-based improvement were treated as claims, and counterexamples within the source qualified unconditional minimization, push gating and isolation readings.

Input contracts were read completely; the registered revision and clean source checkout were rechecked. No target code, services, tests or examples were executed. This member preserves the boundary's source identity and uses no additional source or source ID. Deterministic validation is recorded below after checking this candidate; a form/quotation pass does not establish analytical acceptance.

Validation: passed (`commonplace-run validate-output` on the supplied prompt); no content or relation findings.
