---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Context Constitution runtime baseline: declared context selection, memory admission, compaction and delegation without the executing Letta harness."
run-id: AAS-2026-10-15-context-constitution-7a352d7408f6-01
reviewed-boundary: "964f30137ace9eade1aef112992ed6539b61bbb0"
---

# Context Constitution runtime report

## Runtime account

### Entry and ordinary invocation

The shipped entry is a document link, not an executable agent command. README directs readers to the Constitution and reports internal prompting and training use. Neither the consuming prompt integration nor training procedure is shipped. This account therefore traces a **declared invocation**, not an inspected runtime or supplied execution. The frozen boundary and source identity are in [boundary](boundary.md). All findings below use SRC-1, with doctrine/design evidence unless explicitly labelled reported operation. Inspection covered the complete README, Constitution and Affordances; no new source was added.

> The **[Context Constitution](constitution/CONSTITUTION.md)** is a set of principles governing how AI agents manage context to learn from experience. We use the Constitution internally as the foundation of our prompting and for training memory-native models.
> --- `README.md`

For an ordinary user interaction, the declared principal is a continuing Letta agent serving a human across inference events. The harness supplies its system preamble, tool schemas and current conversation; agent-owned identity/memory and environment-owned instructions remain distinct. System memory is described as always visible, while external memory and skills require retrieval. The foreground model decides whether the current situation warrants following an index, inspecting metadata, and loading full content. It can invoke tools, then use their returns in a subsequent inference and respond to the user. The policy does not specify model-call scheduling, a complete tool-call dispatch loop, task termination criteria or a concrete response format. These remain host responsibilities, not behavior implemented by this repository (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

The ordinary selection chain is [RT-RTE-context-disclosure](#rt-rte-context-disclosure). Durable corrections can take [RT-RTE-memory-admission](#rt-rte-memory-admission), changing the content of a later system prompt rather than model weights. The behavioral channel is [RT-BAP-system-prompt](#rt-bap-system-prompt). The distributed-parametric decision component is [RT-CMP-underlying-model](#rt-cmp-underlying-model). None of these links establishes successful compliance, learning or benefit.

### Material forcing cases and control boundaries

Four routes suffice for the document-level boundary: ordinary on-demand disclosure, a filesystem write that has not successfully pushed, context-size compaction, and isolated/background delegation. These distinguish agent choice, declared admission gating, host-triggered transformation and work isolated from the foreground window. They are source-supported cases, not executed tests.

**Failed or absent push.** A local MemFS edit is not, by the stated contract, an update to the underlying memory blocks. Successful remote push is the declared propagation gate. Its owner is the external Letta synchronization machinery; its enforcement point is the local-to-underlying-memory transition. Guarantee strength is **protocol**, and implementation conclusion status is **uninspected**; design conclusion status is **claimed**; operation conclusion status is **uninspected**. This covers changes *via the files*, not every conceivable memory write. Affordances also mentions bespoke memory tools and explicitly allows humans to edit projected memory. No common authorization gate across those paths is established. Git versioning is not evidence of implemented rollback, conflict resolution or secure isolation (SRC-1, `constitution/AFFORDANCES.md`; [RT-RTE-memory-admission](#rt-rte-memory-admission)).

**Automatic compaction versus agent-directed disclosure.** The harness is said to compact at a specified context size, independently of the foreground model's preference to release material. The summary becomes the first in-context message; raw history remains retrievable under the declared storage contract. Thus the policy's request to discard completed skills is not proof of a targeted runtime eviction primitive. No threshold, summarizer, verbatim tail length or losslessness guarantee is given ([RT-RTE-history-compaction](#rt-rte-history-compaction); SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

**Isolation versus shared memory.** Subagents isolate work context, but conversations of the same agent share memory. A self-call in a separate conversation can therefore keep intermediate messages out of the foreground window without isolating persistent writes. Background reflection and defragmentation are declared ways to change memory; scheduling, concurrent-write coordination, delegated grants and exact return payloads are not specified ([RT-RTE-subagent-context](#rt-rte-subagent-context); SRC-1, `constitution/AFFORDANCES.md`).

**Model change versus identity continuity.** The Constitution explicitly permits a user changing the underlying model. Continuity is assigned to retained context, not an invariant personality of the weights. No provider, version or model endpoint is pinned. A strong continuity claim would require evidence across those changes, not simply delivery of the same memory ([RT-CMP-underlying-model](#rt-cmp-underlying-model); SRC-1, `constitution/CONSTITUTION.md`).

The capability surface includes filesystem and arbitrary programmatic operations, shell/bash, memory tools, history search/list, self-calls and specialized subagents. These are declared affordances, not a current grant set. Tool names/schemas, approval rules, subprocess permissions, provider-native tools, remote-worker execution, direct model-call paths and manual control interfaces are not exposed. Consequently no exhaustive alternate-path security guarantee can be inferred. There is no deployed isolation envelope to inspect here; message-thread isolation is not an OS sandbox. Publication validation is limited to the whitespace workflow described in the boundary, not policy adherence or runtime reliability (SRC-1, `constitution/AFFORDANCES.md`; boundary coverage).

### Policy strength, change and recovery

The Constitution is natural-language guidance interpreted by models. Its own closing qualification defeats a reading of the principles as mandatory executable invariants:

> Ultimately, Letta agents are the owners of their own context, and can choose how to construct their own memories and identities. The specific affordances we have designed exist to assist Letta agents in their learning and formation of self, not necessarily to be used exactly as prescribed.
> --- `constitution/CONSTITUTION.md`

For relevance selection, incremental updating, conservative pruning and identity preservation, the owner is the agent, the requested enforcement point is its context-management decision, and guarantee strength is **policy**. Design conclusion status is **claimed**; implementation conclusion status is **uninspected**; operation conclusion status is **uninspected**. Coverage is whichever decisions actually receive and follow the guidance; exact deployed prompt delivery is unresolved. The required external contract is a harness exposing the declared storage and context controls. Claims of minimal inference cost are objectives, not measured performance. The instruction to preserve identity also limits an unqualified claim that the policy always minimizes tokens (SRC-1, `constitution/CONSTITUTION.md`).

Memory/instruction and agent-owned skill changes use the declared agent-driven admission route below. No distinct executable admission path for new tool capabilities or production machinery is shipped. Skills may contain scripts, but publishing a script as context does not establish permission to execute it. README welcomes issue feedback and future refinement; it does not disclose a release or approval procedure for constitutional changes, or the internal model-training admission mechanism. Do not attribute those external mechanisms to the agent. Recovery is chiefly declared retrieval of old messages, cautious updates and Git version history; no automatic retry, push-failure recovery, summary repair or memory-conflict algorithm is supplied (SRC-1, `README.md`, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

## Shared records

### Components

#### RT-CMP-underlying-model
Label: Underlying language model

The source-native underlying LLM is the inference decision component. Its parameters are distributed-parametric content stored in external model weights; location and provider internals are uninspected. The context-policy document is not that numerical component. Token-space updates are contrasted with weight updates in README; no online parameter-update route is specified. Whether a deployment changes parameters during operation is uninspected. Exact version is not pinned. Users may change models, but whether a mutable endpoint automatically resolves to a different version is uninspected (SRC-1, `README.md`, `constitution/CONSTITUTION.md`).

> The underlying model may change under the agent, for example, a user may change the model to gain different perspectives from different models.
> --- `constitution/CONSTITUTION.md`

### Operative objects

#### RT-OBJ-context-constitution
Label: Context Constitution policy

The source-native Constitution is natural-language rules, goals, explanatory claims and self-assessment questions, stored as Git-tracked Markdown in `constitution/CONSTITUTION.md`. It addresses the Letta agent. Its exact deployed prompt packaging is not supplied. This static publication is not itself a trace-fed memory update. Affordances supplies its declared host contract, not executable enforcement (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

> The Context Constitution is a set of rules and principles governing what a Letta agent places in its context window, in what order, at what level of detail, and for how long.
> --- `constitution/CONSTITUTION.md`

### Routes

#### RT-RTE-context-disclosure
Label: Indexed context disclosure

Endpoints are current system-memory/index content and external skills/files/history, then the model-visible window. The foreground agent owns the next retrieval decision: a situation matches a remembered description, metadata is inspected, and full content is loaded if useful. The policy is natural language; filesystem paths and tool interfaces are operational selectors whose implementations are external. Agent-owned and environment-owned skills are both discoverable; ownership is not interchangeable. State effects include temporary expansion of context; no required durable write follows a read (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

- Immediate return: Requested file/skill/history content becomes available for the current task under the declared affordances; exact tool payload is uninspected.
- Later read-back: Previously curated indexes, external memory and skills are intended to guide later retrieval; actual deployed selection is unobserved.
- Delegated visibility: uninspected — the document does not define automatic transmission of this loaded content to subagents.
- Selection predicate: Current situation matches an in-context cue; skill metadata suggests usefulness; task demands fuller detail.
- Invalidation or expiry: Policy says release content when done and avoid retaining completed-task skills; no concrete selective-eviction interface is specified.
- Activation or effect: Intended task guidance through content in the inference window; actual behavioral dependence is unobserved.
- Evidence limits: Doctrine/design only; selectors, retrieval results and adherence have no supplied execution evidence.
- design conclusion status: claimed
- operation conclusion status: uninspected

> Context should be surfaced at the level of detail the current moment requires. The Letta agent maintains compact summaries or indexes at all times and loads full content — skill documents, retrieved records — only when a task demands it, then releases it when done.
> --- `constitution/CONSTITUTION.md`

#### RT-RTE-memory-admission
Label: Memory and prompt admission

Endpoints are experience/current memory, agent-proposed text changes in MemFS, committed/pushed state, underlying memory blocks and subsequent context. The agent proposes and judges durable updates. Humans can also manipulate the projected files; neither universal human approval nor exclusive model authorship follows. The stated propagation rule admits file-based changes on successful remote push. The harness owns synchronization; rejection reasons and remote authorization policy are unspecified. Bespoke memory tools are an alternate write surface whose admission semantics are not described. System memory is natural-language text; external skills can include text, scripts and other assets with different consumers. This route does not assert one consumer semantics for every asset (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

- Immediate return: Local edits change the projection; successful remote push is declared necessary for propagation to underlying blocks. Exact tool acknowledgments are uninspected.
- Later read-back: `/system` memories are declared visible in future system prompts; external memory is indexed and retrieved on demand, including across environments.
- Delegated visibility: Shared memory is available across the agent's conversations; reflection/defragmentation subagents may modify it, but exact grants and synchronization timing are unspecified.
- Selection predicate: Durable corrected assumptions, user preferences, behavioral guidance and identity changes; the agent should generalize rather than merely copy events.
- Invalidation or expiry: Agent may edit, delete, compress or reorganize memory; conservative pruning should preserve identity and future retrievability. No TTL or automatic invalidation algorithm is specified.
- Activation or effect: Intended to condition subsequent inference via changed memory; installation, actual reliance and benefit are not demonstrated.
- Evidence limits: Declared interfaces and desired behavior only; no implementation of push gating, direct memory tools, approval, conflict handling or subsequent model consumption.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> The filesystem projection of memory is also tracked and versioned using git: changes to memory via the files must be tracked via commits, and are only propogated to the underlying memory blocks on a successful push to remote. The local state (MemFS) is merely a projection of the true underlying memory state (memory blocks).
> --- `constitution/AFFORDANCES.md`

Admission roles and mode: open-ended experience-driven maintenance, not a bounded curriculum or experiment. The agent selects changes; a human may edit content, but per-content human veto is not established. Failure to push prevents declared file propagation; arbitrary semantic rejection is not specified. Versioning affords history in principle, but no rollback/recovery procedure is shown. Triggering guidance is incremental, durable, generalizable learning, subsequently observed and refined. What persists is edited memory/instruction/skill content, not demonstrated changes to weights. There is no supplied expected-answer provider or reference-outcome oracle:

> Unlike traditional training processes, token-space learnings will often not have an explicit reward or verification. Instead, the effects of updates must be observed and refined over time.
> --- `constitution/CONSTITUTION.md`

Theory account: The policy gives explicit claims about how identity and learning depend on context, and recommends correcting assumptions and prompts against experience. It does not show an actual criticism/revision episode. The stored policy is [RT-OBJ-context-constitution](#rt-obj-context-constitution); retained agent content could express further theories, but its contents are not supplied. Theory-builder conditions 1–4, assessed separately: **1 localized content — claimed**, explicit policy content is published; **2 consumption — uninspected**, decisions depending on its meaning are not traced; **3 content-directed criticism — uninspected**, no identified challenged claim, outcome, blame and resulting revision episode is supplied; **4 iteration — uninspected**, no criticism result is traced into a next round. These statuses do not claim absent internal model criticism. Addressability: policy sections and individual prose rules are inspectable, but runtime revision granularity is unresolved. Persistence: intended horizon spans sessions/environments; attained runtime persistence is unobserved. Learning: improved future capacity is an objective, not established by a retained edit. Reflection: self-representation and reciprocal identity/experience influence are prescribed; both causal directions in operation remain uninspected. Reflective and autonomous theory building remain unestablished separately; model proposal authority alone establishes neither.

Self-improvement assessment: boundary is the declared agent's context-determining organization across later sessions; objective is more helpful future action, fewer repeated mistakes and better retrieval, independently stated in the Constitution. The update pathway is claimed, not exercised evidence. No trace establishes objective-bearing evidence causing a particular update, admission into the deployed organization, live behavioral authority for that exact update, or subsequent behavior causally depending on it. Thus exercised self-improvement and successful improvement cannot be attributed, without negating the explicit improvement-directed policy (SRC-1, `constitution/CONSTITUTION.md`).

#### RT-RTE-history-compaction
Label: Host history compaction

Endpoints are accumulated conversation messages and a new model-visible summary, with underlying stored messages available to active retrieval. The host owns the size trigger; the deciding summarizer and transformation details are opaque. Preferentially removed material is old conversational history; recent turns and the summary form the intended working context, but exact retained turns are unspecified (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`).

- Immediate return: A summary message becomes the first message of the in-context buffer.
- Later read-back: The summary carries prior context into later inference; all messages are declared persisted/indexed for on-demand search or listing.
- Delegated visibility: uninspected — cross-conversation history search is described, but automatic delivery of compaction summaries to delegates is not.
- Selection predicate: A specified context size is exceeded; threshold and selection algorithm are not supplied.
- Invalidation or expiry: Old in-context messages are replaced by recursive summaries; future compaction can summarize again. Underlying-history expiry is not specified.
- Activation or effect: Changes what later inference receives; preservation of all task-relevant meaning or improved task results is unobserved.
- Evidence limits: No summarizer implementation, actual before/after buffers, reference checks or recovery trace is supplied.
- design conclusion status: claimed
- operation conclusion status: uninspected

> The in-context message history of a conversation will be compacted once a specified context size is exceeded. The compaction will produce a summary message, which is the first message in the in-context message buffer. The summary message summarizes prior conversational context, and also provides references to files or previous messages that may be relevant to the current conversation.
> --- `constitution/AFFORDANCES.md`

This is host-driven working-context removal and retained-summary supply, unlike foreground requested retrieval. It admits transformed history without a disclosed human approval gate; who proposes or vetoes summary content, the oracle, semantic rejection ability and rollback are uninspected. Operating mode is ongoing conversation. Guidance requests preservation of useful facts and references, but summary correctness is not guaranteed. Raw-history retrieval provides a declared source for recovery, not proof that missing context is noticed or repaired.

#### RT-RTE-subagent-context
Label: Isolated and background subagents

Endpoints are the foreground invocation and isolated/background work; specialized roles are Recall, Reflection and Defragmentation. The agent invokes them; autonomous scheduling policy and exact context construction are unspecified. Recall concerns conversations, Reflection memory modifications, and Defragmentation memory organization. The same agent may create an isolated conversation with itself; isolated messages coexist with shared memory (SRC-1, `constitution/AFFORDANCES.md`).

- Immediate return: uninspected — no subagent result schema, completion signal or foreground handoff payload is supplied.
- Later read-back: Reflection and Defragmentation are intended to change memory for later use; Recall can surface history. No actual write/read chain is shown.
- Delegated visibility: Subagents receive isolated work contexts; which foreground messages, memory contents or tools they receive is unspecified.
- Selection predicate: Foreground choice to isolate work, run background tasks, recall conversations, revise memory or reorganize it; no mandatory trigger schedule.
- Invalidation or expiry: uninspected — delegate context disposal and background-job lifetime are not specified.
- Activation or effect: Intended to reserve foreground context for primary tasks and refine memory; actual context savings or behavior changes are unobserved.
- Evidence limits: No scheduler, delegated permission model, synchronization, return filtering, failed-job recovery or execution trace.
- design conclusion status: claimed
- operation conclusion status: uninspected

> Letta agents can invoke subagents to both isolate context and also have additional tasks run in the background. Letta agents also have access to specific subagents designed for context management:
> --- `constitution/AFFORDANCES.md`

> An individual Letta agent can have multiple concurrent conversations. Each conversation is an isolated message thread, but memory is shared across all conversations.
> --- `constitution/AFFORDANCES.md`

Context isolation resembles a separate task frame, but a return-only model is not established: shared memory can carry effects beyond the isolated thread. No pointer-like liveness or automatic reclamation of externally retained content follows. For memory-changing roles, proposal is assigned to specialized subagents; approval, veto, rejection, rollback and merge ownership remain unspecified beyond the file-admission contract in [RT-RTE-memory-admission](#rt-rte-memory-admission). Mode is open ongoing maintenance; no answer oracle is supplied. Intended persistent results are memory text and organization, not proof of successfully improved knowledge.

### Claims

#### RT-CLM-token-learning
Label: Token-space improvement claim

The Constitution attributes continual learning and self-improvement to curation and re-representation of context, while README reports internal use of the document for prompting/training. These are doctrine and reported operation respectively, not experimental evidence. Neither unchanged weights nor retained context independently settles learning capacity or benefit (SRC-1, `constitution/CONSTITUTION.md`, `README.md`).

> The primary mechanism by which Letta agents self-improve is token-based continual learning: the active curation and re-representation of what context occupies its own context window.
> --- `constitution/CONSTITUTION.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-system-prompt
Label: Persistent system-prompt guidance

Consumer: underlying LLM on later inference calls. Channel: in-context memory in the system-prompt preamble, supplemented by runtime metadata. Force: natural-language behavioral guidance and identity/background conditioning, not a mechanical invariant. Horizon: every invocation under the declared harness contract, with exact deployed prompt integration uninspected. The always-visible path differs from externally retrieved skills; successful delivery and meaning-dependent activation remain distinct. SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`.

> The system prompt is the fixed preamble prepended to every inference call. It defines the Letta agent's identity, behavioral guidelines, persistent goals, and background context that is always relevant. It sits at the front of the context window on every call, and models are trained to attend closely to any instructions or context present in the system prompt.
> --- `constitution/CONSTITUTION.md`

## Annotations

none
