---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AgeMem's paper-specified store editing, semantic read-back, context replacement and trace-fed policy training at arXiv v1."
run-id: AAS-2026-10-12-2601-01885v1-32274e5bddc1-01
source-identity: https://arxiv.org/html/2601.01885v1
reviewed-boundary: "arxiv-2601.01885v1-html-2026-10-12"
---

# AgeMem memory report

## Boundary and evidence

AgeMem retains selected conversational knowledge in an external long-term memory store, replaces or filters active context, and trains its action policy from scored trajectories. This report includes all six declared operations and both explicit and driver-triggered retrieval. It includes evaluation and optimization as consumers of memory and traces, not as additional storage tools. The frozen evidence is SRC-1, the HTML capture identified in [boundary](boundary.md#source-register). All architectural findings are documentary claims; examples and experiments are author-reported operation. No executable registry, CLI dispatcher, hook, library/service implementation or raw execution artifact is supplied. Their conformance, hidden alternatives, malformed-call rejection and restart durability cannot be checked.

Direct source inspection covered Appendix A.1's definitions, prompts and Figures 6–7; Appendix A.2's rewards; Algorithms 1–5 and surrounding Appendix A.3 prose; Appendix B.1–B.3's cases; Appendix C.1–C.4's evaluation and settings. HTML was locally rendered to text for inspection, without fetching linked resources or executing the target. Supplied runtime records also establish quoted support where cited. Available portions of the paper outside these inspected sections are not access gaps. External provider internals, executable benchmark adapters, separately hosted images and repositories remain outside the frozen contents.

| Operation or entry | Frozen source anchor | Coverage and evidence basis | Missing fact and prevented conclusion |
|---|---|---|---|
| Add, Update, Delete | `2601.01885v1.html#A1.SS1.SSS0.Px3`, `2601.01885v1.html#A1.SS1.SSS0.Px4`, `2601.01885v1.html#A1.F7` | Direct read; [MEM-RTE-store-maintenance](#mem-rte-store-maintenance); supplied [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools) | Executor, ID validation, embeddings after replacement and rollback uninspected; cannot establish reliable withdrawal. |
| Explicit Retrieve_memory | `2601.01885v1.html#A1.SS1.SSS0.Px2`, `2601.01885v1.html#A1.F6` | Direct read; [MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval) | Metadata-filter order and precise output rendering unspecified; cannot reproduce candidate selection or complete model-visible record. |
| Stage 1 automatic retrieval | `2601.01885v1.html#alg3` | Direct read plus [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval) | Top-k delivery is not a full-store inspection; state tuple is not a specified prompt serialization. |
| Summary_context and summarizer prompt | `2601.01885v1.html#A1.SS1.SSS0.Px5`, `2601.01885v1.html#A1.F6` | Direct read; [MEM-OBJ-summary](#mem-obj-summary); annotation on [RT-RTE-context-summary](runtime.md#rt-rte-context-summary) | Counting and accepted span values conflict across examples/specification; fidelity and executable replacement unknown. |
| Filter_context, agent or automatic criterion | `2601.01885v1.html#A1.SS1.SSS0.Px6`, `2601.01885v1.html#A1.E15`, `2601.01885v1.html#A1.F6` | Direct read plus [RT-RTE-context-filter](runtime.md#rt-rte-context-filter) | Automatic criterion derivation unspecified; keep/remove polarity conflicts; cannot promise fact-level preservation. |
| Initialize store, reset context, pass Stage 2 context onward | `2601.01885v1.html#alg1`, `2601.01885v1.html#alg3`, `2601.01885v1.html#alg4`, `2601.01885v1.html#alg5` | Direct read plus [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout) | Stage persistence specified, cross-session reload not inspected; early query visibility unresolved. |
| Evaluate stored facts and answer | `2601.01885v1.html#A3.SS2`, `2601.01885v1.html#A1.SS2` | Direct read plus [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) and training annotation | Evaluation produces scores, not a specified per-write admission or repair gate. |
| Collect trajectories, score, optimize and reuse policy | `2601.01885v1.html#A1.SS3`, `2601.01885v1.html#alg2` | Direct read; [MEM-OBJ-experience](#mem-obj-experience); annotation on [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | No alternative checkpoint format, saved optimizer state or deployment loader specified; cannot trace disk artifacts into production. |
| Case cleanup, filtering, summary and later preference use | `2601.01885v1.html#A2.SS1`, `2601.01885v1.html#A2.SS2`, `2601.01885v1.html#A2.SS3` | Direct read; store/retrieval records and [MEM-CLM-case-protocol](#mem-clm-case-protocol) | Illustrations omit tool results and include inconsistent arguments; not authenticated executions. |

## Core ideas

Three retained results have different consumers. Stored text supplies knowledge to later task-policy invocations; a summary supplies derived conversational state to later invocations; scored experience changes policy parameters through optimization. Parameters shape the action distribution rather than presenting readable advice. These mechanisms are not interchangeable kinds of memory ([MEM-OBJ-content](#mem-obj-content), [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-experience](#mem-obj-experience), [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy)).

The policy authors store changes, but delivery is not always policy-requested. Algorithm 3 retrieves against each sampled Stage 1 message before the next policy decision. Explicit Retrieve_memory instead takes a model-selected query, count and optional metadata filter. Neither route establishes complete awareness of the store; a count budget is not a token budget ([RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval), [MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval)).

The source names metadata containing source information, but supplies no authenticated provenance or consumer trust hierarchy. Retrieved material enters active context for interpretation, not a specified higher-priority instruction channel. Semantic similarity selects candidates; it does not certify their truth. Update/Delete and Summary/Filter permit correction or removal, but also remove evidence and historical context. Preserving important information is requested behavior, not a proven invariant ([MEM-OBJ-access-metadata](#mem-obj-access-metadata), [MEM-BAP-retained-context](#mem-bap-retained-context), [RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-context-filter](runtime.md#rt-rte-context-filter)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-content
Label: Long-term memory content

Source-native identity: the content string c in memory entry m_i of M_t. Representational form: natural-language content interpreted by the task policy; it is not the dense embedding or metadata. Storage substrate: abstract external memory store; database, files and reload implementation uninspected. Lineage: model selects and rewrites information from presented context, including supporting facts and illustrative user preferences; exact copying versus derivation depends on its emitted string. Subsequent Update replaces content; Delete removes the entry. Consumer: task policy after selected retrieval, and memory-quality/relevance evaluators. At the policy, force is knowledge/context influence, not a symbolic instruction veto. Persistence is specified across curriculum stages, not independently established across sessions. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px1`, `2601.01885v1.html#A1.SS1.SSS0.Px3`, `2601.01885v1.html#A2.SS1`, `2601.01885v1.html#A3.SS2`.

Closest supplied record: [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools) describes request schemas, not retained payloads; distinct identity. [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout) carries the store across stages but is not its content object.

> operation allows the agent to store new information in long-term memory for future use.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### MEM-OBJ-embedding
Label: Memory content embedding

Source-native identity: enc(c) in the new memory tuple; enc(c') in Update. Representational form: dense numerical, distributed-parametric representation of text. Storage substrate: abstract tuple in external memory, numerical index/backend uninspected. Lineage: text encoder output from content; encoder training provenance and exact version unresolved in [RT-CMP-text-encoder](runtime.md#rt-cmp-text-encoder). Consumer: cosine selector, not a readable task-policy instruction. Updating content is specified to regenerate its representation; stale-index prevention is not implementation-grounded. Delete removes the tuple from the candidate set in the specified set semantics. Evidence: SRC-1, `2601.01885v1.html#A1.E9`, `2601.01885v1.html#A1.E10`, `2601.01885v1.html#A1.E12`. Distinct from the encoder component in the supplied record: this is its retained output, not its weights. Textual definition support is shared with [MEM-OBJ-access-metadata](#mem-obj-access-metadata).

#### MEM-OBJ-access-metadata
Label: Memory access metadata

Source-native identity: metadata in m_new, metadata' in updated entry, memory_id and optional memory_type in schemas. Representational form: symbolic fields for addressing/filtering; free-form values may carry natural-language source descriptions. Storage substrate: store tuple and textual request/result protocol; exact backend and returned field layout unspecified. Lineage: Add accepts optional caller/model metadata and type; prose names timestamp, source information and tags, Update names modification timestamp. Which fields the executor generates or verifies is uninspected. Consumer: metadata filtering narrows search; retrieved ID targets replacement/deletion. Source labels are not shown to confer epistemic or instruction authority. Field names do not prove access control or authenticated provenance. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px3`, `2601.01885v1.html#A1.SS1.SSS0.Px4`, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#A1.F7`.

Closest supplied referent [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools) is schema text; this object is operational addressing/selection data, not a duplicate schema declaration. Returned identifiers are required by the schema descriptions, but actual result rendering is unknown.

> includes timestamp, source information, and optional tags. The memory store is then updated:
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### MEM-OBJ-summary
Label: Replacement conversation summary

Source-native identity: Summarize output replacing selected u_i in C. Representational form: natural-language derived conversation summary. Storage substrate: active message context; durable transcript/version storage uninspected. Lineage: selected conversation messages → prompted LLM → replacement prose. This is derived memory, not an unchanged raw log. Consumer: later task-policy invocation; content supplies interpretive context, not an enforced policy. The summarizer is asked to preserve intentions, decisions and unresolved questions; retained reasons depend on output fidelity, not a separate reason/criticism ledger. Evidence: SRC-1, `2601.01885v1.html#A1.E14`, `2601.01885v1.html#A1.SS1.SSS0.Px5`.

Part of: [RT-RTE-context-summary](runtime.md#rt-rte-context-summary)

This object is the route's generated replacement artifact, not a second declaration of that route or the summarizer model. Later reset/filter/re-summarization may remove it. The horizon established by the specification is later invocations within the episode.

> is implemented by LLM with a summarization system prompt. The agent can specify which messages to summarize using the
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### MEM-OBJ-experience
Label: Training experience buffer

Source-native identity: E, collecting stage trajectories of state/action/initial-zero-reward/old-log-probability tuples; terminal rewards and group advantages subsequently supervise optimization. Representational form: symbolic tuple structure containing conversation/action text and numerical scoring/log-probability data; it is not itself learned weights. Storage substrate: abstract training buffer, reinitialized by Algorithm 1; serialized logs, replay retention and checkpoint substrate unspecified. Lineage: sampled supporting context plus synthetic distractors, generated policy responses/calls, and final task outcomes. Original trace origin is mixed environment/data input and agent-generated interaction, not merely human-authored notes. Consumer: optimizer uses traces and terminal advantages to update policy weights. Authority at that consumer is training supervision; downstream weights influence later policy decisions. Evidence: SRC-1, `2601.01885v1.html#alg1`, `2601.01885v1.html#alg2`, `2601.01885v1.html#alg3`, `2601.01885v1.html#alg4`, `2601.01885v1.html#alg5`.

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

This is the route's retained input object, not a duplicate of its progression or [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy). The supplied update route's verbatim terminal-advantage passage supports this raw-to-derived-to-policy chain. Buffer retention alone is not learned capacity; the behavior-shaping result is updated parameters.

### Routes

#### MEM-RTE-store-maintenance
Label: Store authoring and maintenance

Endpoints and progression: presented context plus selected retrieved entries → policy-generated Add/Update/Delete request → described store mutation → later candidate set for retrieval or evaluation. Owner: policy proposes content/target; described executor installs it. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px3`, `2601.01885v1.html#A1.SS1.SSS0.Px4`, `2601.01885v1.html#A1.F7`, `2601.01885v1.html#A2.SS1`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: changed abstract memory store; call result envelope and acknowledgment contents are uninspected.
- Later read-back: surviving content becomes eligible for explicit or Stage 1 retrieval and for memory-quality scoring; Update changes later candidate text/embedding, Delete removes its tuple.
- Delegated visibility: inapplicable — the described editor is the same task policy; no delegated worker is specified.
- Selection predicate: policy judges what to retain, replace or remove; Update/Delete require a retrieved memory_id; Add supplies content and optional metadata/type.
- Invalidation or expiry: replacement regenerates embedding and modification metadata; deletion removes the entry; independent rollouts initialize empty stores. TTL, tombstones and undo are uninspected.
- Activation or effect: specified changes alter the external candidate store; later retrieval can alter policy input. Actual behavioral dependence or benefit is not independently inspected.
- Evidence limits: documentary semantics and illustrative cleanup, without executor, authenticated run, version history or multi-call transaction contract.

Trigger: salient new context, superseding/refining information, or perceived obsolete/incorrect entries. Proposed change: create a tuple, replace its text/embedding/metadata, or remove it. Computational admission: model generates the request and tool applies the described transformation. Human contribution: researchers choose tools, prompt and reward; illustrative users supply preferences, not formal per-write approval. Delete's model-supplied boolean is not a human veto. Schema enforcement, failure rejection and rollback are uninspected. Guidance requests active memory management and high-quality reusable storage; the retained result is selected content, not necessarily the rationale that selected it. Operating mode: bounded curriculum/task interaction. Answer oracle: no per-edit oracle is specified; later LLM scores against query/reference material are training/evaluation signals, not write gates.

This route is distinct from [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools), which declares schemas, and refines an operative subchain of [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout).

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

Its supportive replacement wording is supplied by [MEM-OBJ-content](#mem-obj-content) and the prior-ID/confirmation quotations in [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools). Appendix B.1's later Delete-plus-Add case is a counterexample to mandatory retention of historical rationale: the agent explicitly strips the old preference reference.

#### MEM-RTE-requested-retrieval
Label: Policy-requested memory retrieval

Endpoints and progression: policy query/count/optional metadata filter plus current store → cosine top-k retrieval → insertion of selected memories into C → later policy invocation. Owner: policy requests and targets retrieval; described retrieval function selects/delivers it. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px2`, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#A2.SS3`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: selected memories inserted into active short-term context; schema's prior-retrieval ID requirement implies usable IDs, but complete response envelope is unspecified.
- Later read-back: entries accumulated or edited earlier supply selected knowledge to the next task-policy invocation for reasoning or further maintenance.
- Delegated visibility: inapplicable — no worker handoff is specified; text encoder consumes text and task policy consumes retrieved material.
- Selection predicate: cosine matching of query and memory representations, optional metadata filter to narrow search, top_k default 3 and typical experimental count 3–5. Filter/ranking order, ties and bounds validation are uninspected.
- Invalidation or expiry: Update/Delete change candidates; delivered copies may remain in C until reset, Summary or Filter. The paper specifies no propagation of store deletion into already delivered context.
- Activation or effect: selection/insertion is specified; Appendix B.3 attributes use of preferences in a later schedule, but supplies no independently inspectable activation trace or causal comparison.
- Evidence limits: unspecified encoder/version, field rendering, token truncation, exact message role and external durability prevent complete reproduction or trust claims.

Distinct identity from [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval): the driver initiates that route every exploratory turn using sampled m_t, whereas this route begins with an explicit model-selected tool call. Both share store and selector semantics, not trigger ownership.

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

> The retrieved memories are then inserted into the short-term context
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Claims

#### MEM-CLM-case-protocol
Label: Case illustration protocol limits

Claimed operation: Appendix B.1 portrays Update followed later by Delete-plus-Add as successful cleanup, retaining current preference but discarding its old historical reference. Source: SRC-1, `2601.01885v1.html#A2.SS1`, compared against `2601.01885v1.html#A1.F7`. The example uses argument `confirmed`, while the schema requires `confirmation`; its first Update also does not display a preceding retrieval yielding the ID. This is not evidence of executor acceptance of either deviation. It prevents using the illustrative success narration to prove ID/confirmation enforcement, transaction success, or preserved lineage. This extends, but is not identical to, [RT-CLM-tool-protocol](runtime.md#rt-clm-tool-protocol), whose counterexample concerned Summary span values.

> After training with AgeMem, the agent demonstrates strategic memory management by selectively storing user preferences, recognizing when updates are needed, and maintaining clean, consistent memory.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Retained text to policy

Consumer: later task-policy invocation. Channel: active context containing selected stored text, replacement summary or surviving filtered messages. Force: natural-language interpretation can inform answers and later memory calls; no specified instruction-priority elevation or mandatory compliance. Horizon: later turns and stages of the same episode; cross-session deployment is uninspected. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px2`, `2601.01885v1.html#A1.SS1.SSS0.Px5`, `2601.01885v1.html#alg5`; [MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval), [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval), [RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-context-filter](runtime.md#rt-rte-context-filter). Distinct from [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy): static prompt guidance is not acquired memory. Distinct from [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy): that channel is updated weights, not text supply. Delivery supports a declared influence path, not proof of actual activation.

## Annotations

#### On [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval)

Memory-specific scope: this is independently initiated supply relative to the next policy action, but not an unsolicited cross-agent notification. Selector input is the sampled message and existing store; retained part is only selected top-k memory content, not guaranteed full-store state. Count k budgets entries, not tokens. Store lineage and access metadata are described in [MEM-OBJ-content](#mem-obj-content) and [MEM-OBJ-access-metadata](#mem-obj-access-metadata). Evidence: SRC-1, `2601.01885v1.html#alg3`, `2601.01885v1.html#A1.SS1.SSS0.Px2`. The supplied route's quote supports the paper's claimed awareness, while its top-k limit bounds that claim. Model-visible serialization of M in s_t remains unknown; the state tuple is not proof of another whole-store read channel.

#### On [RT-RTE-context-summary](runtime.md#rt-rte-context-summary)

Raw-to-derived chain: prior conversational inputs, policy responses and tool-related conversation → selected span → LLM summary → replacement active context → next policy invocation. The generated object is [MEM-OBJ-summary](#mem-obj-summary). Computational admission installs the summarizer's text under policy-selected span; no per-summary human approval or independent fidelity rejection gate is specified. Initial context supply remains driver-defined; that does not make known automatic replacement indeterminate. Prompt asks for important information, intentions, decisions and unresolved questions, but no separate reason ledger is specified. Source: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5`, `2601.01885v1.html#A1.F6`. Preserve the supplied all/N versus full and message-versus-round limits. The schema additionally counts a system/user/assistant/tool bundle as one round, whereas prose's all excludes system messages; actual system-message treatment remains unverified.

#### On [RT-RTE-context-filter](runtime.md#rt-rte-context-filter)

Retained result is the surviving message list, not a new summary or a curated fact collection. Lineage remains raw conversation or earlier summaries minus omitted whole messages. Mixed relevant/distractor messages in Appendix B.2 challenge any assertion of reliable fact-level removal: the specified selector operates on message similarity, while the illustration narrates selective removal of topics without displaying resulting context. Agent-supplied criterion and automatically task-derived criterion are both included documentary alternatives; the automatic derivation rule is missing. Admission is computational threshold execution, not human review. Store entries remain separate; removing a contextual copy does not specify deleting its original from M. Source: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px6`, `2601.01885v1.html#A1.E15`, `2601.01885v1.html#A2.SS2`. The supplied route provides the minimum verbatim criterion-removal passage and polarity limitation.

#### On [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Trace-fed result: [MEM-OBJ-experience](#mem-obj-experience) supplies states/actions/outcomes, terminal scoring and group advantage produce numerical supervision, and optimization changes [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy). Later rollout and reported evaluation use the policy; [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy) identifies its authority path. This is trace-fed parameter adaptation, not textual method editing. Readable reasons need not survive in the parameter output. Checkpoints, optimizer-state retention, rejected candidate updates and deployment loading remain uninspected. Evidence: SRC-1, `2601.01885v1.html#alg1`, `2601.01885v1.html#alg2`, `2601.01885v1.html#A1.SS2`.

Storage-quality scoring classifies Stage 1 entries using query and expected answer; preservation scoring tests key query tokens/phrases at answer generation, directly or via summary. Neither entails accurate preservation of all supporting reasoning. Memory maintenance reward is an update/delete occurrence indicator, not an inspected test that the edit was warranted. The supplied route already retains its reward and terminal-advantage quotations; no correction to it is proposed. MQ separately compares stored facts to HotpotQA supporting facts under Qwen-Max ([RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles)). It produces a score, with no specified feedback repair route into store content. Shared scalar advantage does not localize action-level causal credit or retain a formulated criticism history.

## Write side

Acquisition and admission are separate. Driver-selected supporting context and distractors enter C; the model authors Add/Update content and selects Delete targets; described tool semantics install the mutations. Researchers starting training or users supplying a preference do not establish per-content approval. Identifiers and confirmation are requested protocol constraints, with rejection ability and rollback unknown. The resulting text is selected knowledge, its embedding is access machinery, and its metadata supports addressing/search rather than trust certification ([MEM-RTE-store-maintenance](#mem-rte-store-maintenance), [MEM-OBJ-embedding](#mem-obj-embedding), [MEM-OBJ-access-metadata](#mem-obj-access-metadata)).

Summary is an automatic derived write after policy selection; Filter is automatic omission of messages after criterion selection. Their consumers receive replacements or survivors, not necessarily the original evidence. The preservation reward is later feedback, not an installation-time check. B.1's Delete-plus-Add cleanup deliberately removes the old preference reference, so a stronger claim that AgeMem always retains reasons would be false. No specified read-back route reconstructs that discarded history. B.2's simulated context growth and narrated success cannot settle executor details ([MEM-OBJ-summary](#mem-obj-summary), [MEM-CLM-case-protocol](#mem-clm-case-protocol), summary/filter annotations; SRC-1, `2601.01885v1.html#A1.SS2`, `2601.01885v1.html#A2.SS1`, `2601.01885v1.html#A2.SS2`).

Store initialization is explicitly empty per independent rollout; context resets before Stage 2 but memory persists, and Stage 3 retains Stage 2 context. This gives two concurrent within-episode horizons, not a demonstrated disk-backed lifelong store. Withdrawals are local: Delete changes store candidates, Filter changes C, reset changes C, and weight updates change a different retained artifact. No specified mechanism retracts information from already delivered context, an already formed summary, evaluation output or trained weights ([RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout), [MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval); SRC-1, `2601.01885v1.html#alg1`, `2601.01885v1.html#alg4`, `2601.01885v1.html#alg5`). This is a specification limit, not an evidenced universal absence.

Training transforms mixed traces into updated weights. Raw buffer retention is not the behavior-shaping endpoint; later optimizer and policy consumers must be distinguished. The bounded generate-then-optimize design specifies computational admission of gradient updates without a human per-update veto or candidate-rejection gate. Alternative checkpoint forms and recovery remain unknown, so no deployment persistence claim follows from the returned trained policy ([MEM-OBJ-experience](#mem-obj-experience), training annotation, [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

## Read-back

1. **Policy request:** model-selected query → optional metadata restriction/cosine top-k → selected entries inserted into C → next task-policy invocation. It can support task reasoning or another edit, not merely return bytes to an unspecified caller ([MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval)).
2. **Driver supply:** each sampled Stage 1 message triggers retrieval before policy choice → selected stored entries plus message → C → policy maintenance decision. Independent initiation is established by Algorithm 3, not by the paper calling it agent introspection ([RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval)).
3. **Derived context:** policy-selected Summary produces replacement text; criterion-based Filter leaves surviving messages; next invocation consumes that reduced context. Stage 3 receives Stage 2 survivors/summaries. Replacements count as retained memory when used on the later invocation; unchanged current state alone does not establish a memory transformation ([MEM-OBJ-summary](#mem-obj-summary), summary/filter annotations, [MEM-BAP-retained-context](#mem-bap-retained-context)).
4. **Trace learning:** optimizer consumes buffered experience and reward-derived advantages, returns changed weights; subsequent policy invocation uses those parameters. This is not an entry-retrieval request, and no readable checkpoint explanation is specified ([MEM-OBJ-experience](#mem-obj-experience), training annotation, [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy)).
5. **Evaluation:** evaluator consumes stored predicted facts and expected supporting facts, or final answer and ground truth. Numerical output supports measurement and, in the reward design, optimization. It does not establish a store-edit admission gate or a later content repair consumer ([RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles), training annotation; SRC-1, `2601.01885v1.html#A3.SS2`, `2601.01885v1.html#A1.SS2`).

The documented context limit is 8,192 tokens and response limit 2,048 tokens. Retrieval count 3–5 does not itself guarantee fitting the context budget; penalty and proactive compaction encourage rather than enforce successful preservation. Actual message-role rendering, overflow handling and per-stage grants remain unverified ([RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval); SRC-1, `2601.01885v1.html#A3.SS4`).

## Integration issues

- **Corrections to supplied facts:** none. The runtime's strong-claim qualifications are retained, not replaced.
- **Possible duplication:** none after comparison. Payload, embedding and metadata are distinct from schema/encoder records; generated summary and experience are declared parts of supplied routes. Store-maintenance and explicit-retrieval routes are subchains of the rollout, not duplicates of its end-to-end referent. [MEM-CLM-case-protocol](#mem-clm-case-protocol) extends the supplied protocol limits to a different illustrative mismatch. Parent and closest-record comparisons are retained at every declaration.
- **Protocol discrepancy:** B.1's `confirmed` versus schema `confirmation`, and unshown retrieval before its first Update, prevent inferring successful enforcement from narrated cleanup. Reconciliation should preserve this alongside [RT-CLM-tool-protocol](runtime.md#rt-clm-tool-protocol), not infer executable acceptance ([MEM-CLM-case-protocol](#mem-clm-case-protocol); SRC-1, `2601.01885v1.html#A2.SS1`, `2601.01885v1.html#A1.F7`).
- **Selection visibility:** explicit metadata_filter is a documented alternative narrowing input; filter ordering, returned metadata and ID rendering are unresolved. Algorithm state tuples also leave whole-store/query serialization unresolved. These limits prevent classifying complete model-visible provenance or full-store awareness ([MEM-RTE-requested-retrieval](#mem-rte-requested-retrieval), [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval), [RT-CLM-context-reset](runtime.md#rt-clm-context-reset); SRC-1, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#alg3`).
- **Context preservation:** all/N/full, rounds/messages/system handling, automatic Filter criterion derivation and keep/remove polarity remain unresolved. Mixed-message examples do not demonstrate safe topical removal. These prevent a reliable essential-information-preservation conclusion ([RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-context-filter](runtime.md#rt-rte-context-filter), [MEM-OBJ-summary](#mem-obj-summary); SRC-1, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#A1.SS1.SSS0.Px6`, `2601.01885v1.html#A2.SS2`).
- **Lifecycle and trust:** store backend, external reload, metadata authentication, deletion propagation and reason/version retention are not supplied; stage-local retention is the supported horizon. No durable withdrawal or trust-elevation guarantee follows ([MEM-OBJ-access-metadata](#mem-obj-access-metadata), [MEM-RTE-store-maintenance](#mem-rte-store-maintenance), [MEM-BAP-retained-context](#mem-bap-retained-context)).
- **Training persistence and scoring:** checkpoint/recovery formats and exact training scorers remain unknown; scalar supervision does not localize causal credit. The runtime's 1.0 versus 1/3 reward-scale discrepancy remains unresolved. MQ evaluation is not an edit gate, and query-token preservation is narrower than full supporting-information preservation ([MEM-OBJ-experience](#mem-obj-experience), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles); SRC-1, `2601.01885v1.html#A1.SS2`, `2601.01885v1.html#A3.SS2`, `2601.01885v1.html#A3.SS4`).

## Limitations and checks

Source identity and capture label were rechecked against supplied boundary/runtime, and all new evidence stays within SRC-1. The source digest is checked separately against the boundary's SHA-256. Governing identity, record and quotation requirements were read completely. The analysis inspected source text, not target execution or model services. Paper specifications and illustrative successes do not establish implementation wiring, authenticated exercise, action-level causal benefit, restart persistence or reliable rejection. Opaque model processing cannot establish either presence or absence of a formulated criticism loop.

Validation: deterministic member validation passed for this candidate using the supplied command and artifact/role context. Form and quotation occurrence checks do not establish analytical acceptance or independently validate operation.
