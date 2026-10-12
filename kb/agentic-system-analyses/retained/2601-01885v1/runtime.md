---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AgeMem runtime baseline: the paper-specified memory action loop, curriculum, control limits and policy updates at the frozen arXiv v1 capture."
run-id: AAS-2026-10-12-2601-01885v1-32274e5bddc1-01
reviewed-boundary: "arxiv-2601.01885v1-html-2026-10-12"
---

# AgeMem runtime report

## Runtime account

### Evidence and entry paths

AgeMem's consequential claimed work is to let one agent policy choose both long-term memory operations and active-context operations while solving long-horizon tasks. This is a documentary runtime baseline, not a trace of shipped executable software. The [boundary](boundary.md#boundary-and-evidence) supplies one captured paper, SRC-1, and no executable entry points, raw runs or reproduced experiments. The inspected additions to its initial coverage are Appendix A.1's full prompts and textual schemas, Appendix A.2's reward formulas, Algorithms 1–5, Appendix B.2–B.3's illustrative cases, and Appendix C.2–C.4's evaluator and configuration descriptions. All remain doctrine/design or reported operation, not implementation or observed-run evidence.

The paper specifies two related entry paths: a task-solving invocation using a policy plus the memory-tool interface, and a generate-then-optimize training driver that constructs three-stage episodes. It reports Agentscope for agent construction and Trinity for optimization, but supplies neither their callers nor AgeMem packaging, deployment configuration or CLI/API entry points (SRC-1, `2601.01885v1.html#S4.SS1`, `2601.01885v1.html#A3.SS4`). [RT-RTE-task-rollout](#rt-rte-task-rollout) describes the ordinary episode; [RT-RTE-policy-update](#rt-rte-policy-update) describes the builder loop. Inference-time weight updates are not established merely because training changes weights.

### Ordinary invocation, end to end

In the declared training mode, the driver selects a task and its supporting context, generates distractors, and initializes an empty long-term memory store for each independent rollout. Stage 1 starts an empty message context and samples messages from the task's contextual information. Before each policy decision, Algorithm 3 retrieves memories using the sampled message, then inserts the retrieved content and that message into context. The policy generates language or structured memory calls. The driver appends the response, collects a state/action/zero-reward/old-log-probability tuple, dispatches memory calls, and either continues or breaks on an output answer. The repeated retrieval is a driver-specified route, not solely a decision to call a tool: [RT-RTE-stage-retrieval](#rt-rte-stage-retrieval).

Stage 2 resets the message context while retaining the store. It injects distractors, samples policy actions, appends responses, records experience and dispatches memory calls. Stage 3 appends the formal query to the context left by Stage 2. It repeats the same action cycle until an answer is emitted or the turn bound is reached. Its immediate terminal output is a stage trajectory and an answer, initially NULL if no answer is produced. The surrounding account assigns the composite trajectory reward after completion, and the optimizer broadcasts the group-normalized terminal advantage to earlier actions. These are symbolic orchestration decisions around a distributed-parametric policy; the messages that the policy interprets are natural-language content (SRC-1, `2601.01885v1.html#alg1`, `2601.01885v1.html#alg3`, `2601.01885v1.html#alg4`, `2601.01885v1.html#alg5`, `2601.01885v1.html#A1.SS3`).

Identity in this specification means task q, rollout k, timestep t and memory identifiers returned by retrieval. No authenticated caller identity or tenant boundary is specified in the inspected interface. The next-step owner is the driver for staging, message supply and bounded iteration, and the policy for choosing its generated response or explicit calls. State is represented abstractly as context, memory and query. That notation does not establish exactly what memory or query text reaches the model: the prose says the query has not been revealed in Stage 1, but Algorithm 3 includes q in its state tuple despite not listing q among its inputs. Therefore the intended withheld-query curriculum is clear, while the actual model-visible input construction and leak prevention remain unverified; see [RT-CLM-context-reset](#rt-clm-context-reset).

The executor boundary comprises the described memory/context functions and the benchmark environment. Add takes content with optional metadata/type; Update takes a previously retrieved memory identifier and replacement content; Delete takes a previously retrieved identifier and a boolean confirmation. Their semantics change the external store. Retrieve supplies selected entries to context. Summary replaces selected context with generated prose. Filter removes messages by similarity. The six-tool capability surface is explicit; the current per-stage grant set is not. The stage procedures say to dispatch memory calls without a visible per-stage allowlist. Their curricular emphasis on LTM or STM does not prove that other operations are denied. Memory-content lineage, curation and revisions are left to the memory analyst rather than recast here as runtime guarantees (SRC-1, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#A1.F7`, Algorithms 3–5).

The caller-facing controls shown are tool arguments, prompt guidance, maximum context/response lengths and bounded turns. Deployment isolation, approval callbacks, concurrency, transaction boundaries, error retries and process-restart recovery cannot be inspected in this capture. Stage persistence is explicitly described, but disk/database durability and cross-process reload are not established. Independent rollouts are grouped for reward normalization, not described as delegated agents with shared writable state. The paper's environment benchmarks extend the task-effect boundary to simulated actions, but do not show the exact environment action adapter or its permissions (SRC-1, `2601.01885v1.html#A3.SS1`).

### Forcing cases and alternate routes

Three documentary forcing cases materially qualify the broad claims:

1. **Driver retrieval before policy choice.** Algorithm 3 prescribes retrieval every exploratory turn. This is an alternate route to model-requested Retrieve_memory and prevents interpreting every memory delivery as agent-selected timing. The selected content can shape the very decision whether to store or update: [RT-RTE-stage-retrieval](#rt-rte-stage-retrieval).
2. **Context deletion versus preservation.** The Filter equation retains messages with similarity below the threshold, and its schema calls the criterion a removal description. Nearby prose offers a description of “what to keep.” These are not interchangeable criterion semantics. Summary also replaces originals using an LLM, without an inspectable fidelity check. Consequently neither operation supplies a proven essential-information-preservation invariant: [RT-RTE-context-filter](#rt-rte-context-filter), [RT-RTE-context-summary](#rt-rte-context-summary).
3. **Exit and malformed requests.** Algorithms 3–5 break on an answer and bound turns. The system prompt requests mutually exclusive tool-call/answer blocks, including arrays of calls. The illustrative Summary call in Appendix B.2 uses `span: "full"`, whereas the operational description specifies `"all"` or a numeric span. The schema accepts a string but no dispatcher is supplied to settle `full`, mixed blocks, malformed JSON, invalid IDs or partial multi-call execution. A prompt plus schemas establishes the requested protocol, not guaranteed parsing or atomic effects: [RT-CLM-tool-protocol](#rt-clm-tool-protocol).

The inspected alternate paths include language-only final answers, one or multiple explicit memory calls, driver-triggered retrieval, the summarizer's model call, and the external judge/optimizer path. Appendix C.3 additionally describes comparison variants: AgeMem-noRL retains the interface without RL; RAG variants replace STM tools with retrieval at every step. Those variants are comparisons, not evidence that the trained target uses that RAG route in ordinary execution (SRC-1, `2601.01885v1.html#A3.SS3`). Direct provider-native tools, shell access, host callbacks, extensions, subprocess workers, manual control and durable deployment variants remain unobserved rather than ruled out. No universal isolation guarantee can be inferred from this small action-space description.

### Load-bearing controls and guarantee coverage

| Control or claimed guarantee | Owner and enforcement point | Strength and status | Covered paths, external contract and limits |
|---|---|---|---|
| Consistent tool-call/answer format | Prompt author requests it; model emits blocks; executable parser owner is unresolved | guarantee strength: policy; design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected | Explicit response path only. Requires model compliance and a parser matching the documented tags/JSON. Does not establish multi-call ordering, rejection or atomicity. [RT-CLM-tool-protocol](#rt-clm-tool-protocol). |
| Remove Stage 1 residual context | Training driver at reset before Stage 2 | guarantee strength: protocol; design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected | Removes the named message context while retaining memory; not a general no-leakage guarantee for query/state, provider state or other host channels. [RT-CLM-context-reset](#rt-clm-context-reset). |
| Keep within context budget | Model chooses Summary/Filter; reward calculation penalizes overflow; external runtime supplies token accounting | guarantee strength: best effort; design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected | Reported 8,192-token context and 2,048-token response limits. Penalty is a training signal, not demonstrated pre-action admission or lossless compaction. [RT-RTE-policy-update](#rt-rte-policy-update). |
| Obtain identifiers before modification and confirm deletion | Tool schema requests retrieved IDs and a confirmation boolean; dispatcher enforcement is unresolved | guarantee strength: protocol; design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected | Update/Delete request path. Boolean confirmation is a model-supplied argument, not evidence of human approval. Requires identifier validation and deletion semantics from the uninspected executor. [RT-OBJ-ltm-tools](#rt-obj-ltm-tools). |

Distributed-parametric dependencies are separately recorded below. Training changes the policy; no operation-time parameter update is specified for the encoder, summarizer or judge. Exact checkpoint digests are not pinned for any of them. Named models do not establish stable provider-endpoint identity. The framework learns a policy through scalar reward and parameter updates; the inspected algorithm does not supply a content-directed criticism/revision loop over formulated method theories. This limits such an interpretation without deciding what opaque model processing might contain.

## Shared records

### Components

#### RT-CMP-agent-policy
Label: Agent policy

Source-native identity: parameterized policy πθ, with Qwen2.5-7B-Instruct and Qwen3-4B-Instruct as reported backbones. Representational form: distributed-parametric weights, consuming natural-language context and emitting language plus symbolic call envelopes. Storage substrate: model parameters, checkpoint/serving substrate uninspected. Parameters change in the specified GRPO training loop; inference-time changes are uninspected. Exact trained version is not pinned. Mutable endpoint resolution is uninspected; naming a backbone does not freeze a deployed model. Provider internals are outside the capture. Evidence: SRC-1, `2601.01885v1.html#S3.SS1`, `2601.01885v1.html#S4.SS1`, [RT-RTE-policy-update](#rt-rte-policy-update).

#### RT-CMP-text-encoder
Label: Text encoder

Source-native identity: enc(·), the dense text encoder used for cosine matching. Representational form: distributed-parametric encoder and dense numerical outputs. Storage substrate: encoder parameters and embedding vectors; actual backend uninspected. Parameter changes during operation are uninspected, not established absent. Exact model/version is unspecified; whether a mutable endpoint can resolve to another encoder is uninspected. This dependency affects both retrieval and filtering, so its opacity prevents reproduction of selection decisions. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px1`, `2601.01885v1.html#A1.E9`.

> We use cosine similarity for semantic matching throughout the framework.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-CMP-summarize-model
Label: Summarize model

Source-native identity: LLM implementing Summarize(·) under the conversation summarization prompt. Representational form: distributed-parametric component producing natural-language summaries. Storage substrate: model weights/endpoint uninspected. Parameters changing during operation, exact version pinning and mutable endpoint resolution are all uninspected. The paper does not settle whether this is the task policy or a distinct model instance; it establishes a distinct consumption role, not a proven distinct checkpoint. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5`, [RT-RTE-context-summary](#rt-rte-context-summary).

#### RT-CMP-qwen-max
Label: Qwen-Max evaluator

Source-native identity: Qwen-Max for reported HotpotQA answer and memory-quality evaluation. Representational form: distributed-parametric judgment model; prompts and expected facts/answers are natural-language inputs, scores are symbolic outputs. Storage substrate: external model service or weights, not specified. Exact version is not pinned; operation-time parameter changes and mutable endpoint resolution are uninspected. Provider internals remain uninspected. Qwen-Max is named for the reported evaluation; the paper's generic reward-judge notation alone does not establish that this precise model supplies every training subscore. Evidence: SRC-1, `2601.01885v1.html#A3.SS2`.

> We use Qwen-Max as the evaluator model, and each evaluation is performed independently to ensure consistency.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Operative objects

#### RT-OBJ-tool-prompt
Label: Tool-calling system prompt

Source-native identity: AgeMem's tool-calling system prompt in Appendix A.1. Representational form: natural-language behavioral guidance with embedded symbolic tag and JSON examples; the guidance is interpreted by the model, while an external parser would consume the emitted envelopes. Storage substrate: literal prompt in the captured paper; runtime installation/storage uninspected. It includes a tool-list placeholder, a reasoning block, one tool-call block or answer block after each reasoning block, and iterative tool use. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px7`, [RT-CLM-tool-protocol](#rt-clm-tool-protocol). No executable validator is supplied by this object.

#### RT-OBJ-ltm-tools
Label: LTM tool schemas

Source-native identity: LTM_TOOLS, containing Add_memory, Update_memory and Delete_memory. Representational form: symbolic function/argument descriptions, with natural-language descriptions interpreted by the policy. Storage substrate: textual schemas in Figure 7; installed registry and executor storage uninspected. The schemas require content for Add, memory_id plus content for Update, and memory_id plus boolean confirmation for Delete. Update/Delete descriptions require identifiers from prior retrieval. This describes the request protocol, not proof that arbitrary IDs are rejected or confirmation is enforced. Evidence: SRC-1, `2601.01885v1.html#A1.F7`.

> Requires<span id="lstnumberx135.5.4" class="ltx_text ltx_lst_space"> </span>memory_id<span id="lstnumberx135.5.5" class="ltx_text ltx_lst_space"> </span>from<span id="lstnumberx135.5.6" class="ltx_text ltx_lst_space"> </span>prior<span id="lstnumberx135.5.7" class="ltx_text ltx_lst_space"> </span>retrieval.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> Requires<span id="lstnumberx156.5.5" class="ltx_text ltx_lst_space"> </span>confirmation.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Routes

#### RT-RTE-task-rollout
Label: Three-stage task rollout

Endpoints and progression: task/context and distractor inputs → fresh per-rollout store → Stage 1 → reset context → Stage 2 → query appended to retained Stage 2 context → Stage 3 trajectory and answer. Driver owns staging, response insertion, experience collection, tool dispatch and exits; [RT-CMP-agent-policy](#rt-cmp-agent-policy) selects generated actions. Source: SRC-1, `2601.01885v1.html#alg1`, `2601.01885v1.html#alg3`, `2601.01885v1.html#alg4`, `2601.01885v1.html#alg5`, `2601.01885v1.html#A1.SS3`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: Stage 3 trajectory and predicted answer, with NULL initialized for the no-answer path; earlier stages return their experience sequences.
- Later read-back: constructed memory reaches later stages through retrieval; transformed Stage 2 context reaches Stage 3; experiences feed optimization. Cross-process persistence is uninspected.
- Delegated visibility: inapplicable — no delegated worker is specified in Algorithms 1–5; parallel rollouts are independent trajectory samples.
- Selection predicate: driver selects task/context/distractors and turn progression; policy samples actions from the presented state; explicit Retrieve selects cosine top-k content.
- Invalidation or expiry: store initialized empty per rollout; context reset before Stage 2; Update/Delete and Summary/Filter can replace or remove information; TTL and cross-run expiry are uninspected.
- Activation or effect: specified actions mutate the store/context or return an answer; delivered information is intended to shape later reasoning, but actual activation is not inspectable as a run.
- Evidence limits: algorithmic and prose specification only; model-visible q in early stages, executable action parsing, tool-result formatting, errors and benchmark adapters are unresolved.

Operating mode: bounded training curriculum; user-facing task solving is also described but its exact enclosing driver is uninspected. Computational contributions: driver supplies stages and policy proposes/chooses calls and answers. Human contribution: researchers define data, prompts, tools and curriculum; no per-action human veto is specified by these algorithms, and a production veto mechanism remains uninspected. Answer oracle: during training, a reference answer and an LLM judge contribute terminal reward; during benchmark evaluation, environment outcomes supply SR/PR and HotpotQA ground truth is judged by Qwen-Max. This is evaluation supervision, not a live guarantee of answer correctness. Memory admission uses model-generated requests and described tool execution, shaped by the prompt and learned rewards; failure rejection and rollback are uninspected. Detailed memory revision findings belong to the memory member.

> Once the answer is produced or the maximum steps are reached, a composite reward function
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-RTE-stage-retrieval
Label: Stage 1 driver retrieval

Endpoints: sampled contextual message and current store → Retrieve → selected memories plus message inserted into C → next policy action. Owner: Stage 1 driver, with cosine matching implemented by the described retrieval function. Unlike explicit Retrieve_memory, this occurs before the policy action in Algorithm 3. Evidence: SRC-1, `2601.01885v1.html#alg3`, `2601.01885v1.html#A1.SS3.SSS0.Px2`, `2601.01885v1.html#A1.SS1.SSS0.Px2`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: top-k memories, combined with the sampled input message and appended to active context.
- Later read-back: store entries written earlier may reach a later turn's policy through this driver-triggered retrieval.
- Delegated visibility: inapplicable — recipient is the same policy's next invocation, not a specified delegate.
- Selection predicate: sampled message is the query; cosine similarity over dense encodings ranks current entries; k is supplied by the driver notation, with typical experimental retrieval count described as 3–5.
- Invalidation or expiry: subsequent store updates/deletes change candidates; context reset removes these deliveries before Stage 2, while the store persists.
- Activation or effect: creates model input for storage/maintenance choices; neither full-store visibility nor actual behavior change is established by top-k delivery alone.
- Evidence limits: encoder identity, ties, empty-store behavior and output rendering are uninspected; prose's “awareness” claim exceeds proof of complete inspection.

> To support informed memory decisions, the agent proactively performs memory retrieval at every step.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-RTE-context-summary
Label: Summary context replacement

Endpoints: policy-selected context span → LLM summarizer with its system prompt → generated summary replaces originals in C → later policy invocation. Owner: policy for invocation/span, summarizer for proposed text and context tool for installation. Guidance asks for concise preservation of important information, intentions, decisions and unresolved questions. What persists is replacement prose, not a specified criticism history. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5`, `2601.01885v1.html#A1.F6`, `2601.01885v1.html#A2.SS2`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: updated context with selected original messages replaced by an LLM summary; exact tool response envelope is uninspected.
- Later read-back: replacement summary becomes input to subsequent policy invocations within the episode; restart/session persistence is uninspected.
- Delegated visibility: summarizer receives the selected conversation span; whether it shares policy weights or service state is unresolved.
- Selection predicate: policy supplies `span`; prose permits all non-system messages or the last N messages; schema describes rounds, leaving message-versus-round counting unresolved.
- Invalidation or expiry: original selected content is replaced; later reset, filtering or compaction can remove the summary; versioning and rollback are uninspected.
- Activation or effect: changes the language available for subsequent reasoning; lossless preservation and successful overflow avoidance are requested/reported, not independently observed.
- Evidence limits: Appendix B.2 illustrates `full` despite the operational all/numeric description; no executor settles that input or checks summary fidelity.

Admission: model selects compaction and summarizer proposes replacement; described tool installs it. Per-content human approval, rejection based on preservation tests and rollback are uninspected. Operating mode: context management inside task/curriculum; trigger is policy judgment about accumulated context. Answer oracle: inapplicable — no reference summary or per-summary acceptance oracle is specified; terminal preservation reward is a separate training signal.

> operation compresses conversation history in the short-term context to prevent context overflow while preserving essential information.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-RTE-context-filter
Label: Filter context removal

Endpoints: current messages and criterion → similarity threshold filter → reduced message context → later policy invocation. Owner: policy supplies criterion or it is derived from current task context; the described tool applies cosine thresholding. Equation 15 retains messages with similarity strictly below θ; the prose describes removing messages exceeding the threshold, leaving equality handling imprecise across surfaces. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px6`, `2601.01885v1.html#A1.E15`, `2601.01885v1.html#A1.F6`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: filtered context; exact tool response message is uninspected.
- Later read-back: retained messages, with omitted messages no longer present, reach the next policy invocation; cross-session retention is uninspected.
- Delegated visibility: inapplicable — no delegated recipient is specified; the encoder consumes criterion/message text for matching.
- Selection predicate: similarity to criterion compared with default threshold 0.6; schema describes removal criteria, while nearby prose also suggests descriptions of what to keep.
- Invalidation or expiry: filtering removes messages from C; reset can remove remaining context; restoration/undo is uninspected.
- Activation or effect: deletes model-input messages; relevance preservation is an intended outcome, not entailed by the threshold.
- Evidence limits: criterion polarity inconsistency, encoder opacity and message-level removal prevent inferring reliable separation of relevant facts from distractors, especially in mixed messages.

Admission: computational criterion proposal and threshold execution, with no specified per-removal human approval or veto. Trigger: noise/redundancy under the curriculum or task. Proposed change: omit matching messages. Guidance: Filter_context schema says criterion describes content to remove. Rejection and recovery are uninspected. Operating mode: context-maintenance action, not a bounded comparison between candidate filters. Answer oracle: inapplicable — no per-filter expected retained-context oracle is specified; terminal rewards are later training feedback.

> criteria<span id="lstnumberx82.5.2" class="ltx_text ltx_lst_space"> </span>for<span id="lstnumberx82.5.3" class="ltx_text ltx_lst_space"> </span>content<span id="lstnumberx82.5.4" class="ltx_text ltx_lst_space"> </span>removal.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-RTE-policy-update
Label: Step-wise GRPO policy update

Endpoints: grouped three-stage trajectories and terminal rewards → group-normalized advantages broadcast across timesteps → KL-regularized objective → gradient update of θ → returned policy. Owner: training driver/Trinity optimizer, described but not inspected. Parameters, rather than a localized text rule set, are the behavior-shaping retained result. Evidence: SRC-1, `2601.01885v1.html#S3.SS4`, `2601.01885v1.html#A1.SS2`, `2601.01885v1.html#alg2`, `2601.01885v1.html#A3.SS4`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: updated policy after gradient ascent, with old-policy parameters refreshed.
- Later read-back: changed parameters govern subsequent training decisions and the reported trained agent's evaluation; actual checkpoint lineage and deployment read-back are uninspected.
- Delegated visibility: optimizer receives experience and advantages; LLM scoring consumes answers/memories/reference inputs. External framework and provider data boundaries are uninspected.
- Selection predicate: each task's rollout rewards are normalized relative to its group; the same terminal advantage is assigned to every preceding timestep; no independently estimated causal value for each memory action is supplied.
- Invalidation or expiry: θ is updated and θold refreshed; buffer is initialized in the training loop; checkpoint retention, optimizer rollback and serving replacement are uninspected.
- Activation or effect: specified parameter changes alter the future action distribution; operation and benefit are author-reported, not supported by inspectable execution evidence.
- Evidence limits: pseudocode only; exact checkpoint, scorer identities for all training components, hyperparameter consistency and executable scheduling remain unresolved.

Trigger and proposed change: after generating grouped trajectories, optimize weights for task completion, context economy/preservation and memory quality. Admission: gradient ascent applies the computed update; researchers set curriculum and objective, while software computes rollout actions, scores/advantages and updates. No human per-update approval, candidate checkpoint veto or validation-set rejection gate is specified by Algorithm 2. Recovery: KL regularization constrains departure from a reference distribution but is not rollback; checkpoint recovery remains uninspected. Operating mode: bounded experimental training on HotpotQA, then reported evaluation on five benchmarks, not continuous production self-training.

Answer oracle: ground-truth answer Aq for the task-completion judge; supporting facts for reported memory-quality evaluation; environment outcomes for simulation benchmarks. LLM judgment is not itself ground truth. Reward guidance includes compression, pre-overflow tool use, preservation, storage quality, maintenance and retrieved-memory relevance. Appendix A.2's maintenance formula is an indicator that an update or delete occurred, narrower than the prose's claim to reward “meaningful” maintenance. Likewise penalties encourage rather than prevent overflow. Appendix C.4 names K=8 and KL coefficient 0.1. The exact top-level reward scale is unresolved: §4.1 says coefficients 1.0, Appendix C.4 says 1/3. Equal relative weights are consistent, but numerical equivalence cannot be assumed given fixed penalties and KL regularization.

> These terminal advantages are then broadcast uniformly to all timesteps within the same trajectory, establishing a consistent learning signal that connects early-stage memory decisions to final task outcomes.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> When the context exceeds this limit, the agent receives a penalty, encouraging proactive use of STM management tools.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> For all reward weights in the reward function, we use uniform coefficients of 1.0 without manual tuning.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> All reward weights are set to 1/3:
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

This is an explicit policy-improvement design, but a shared terminal score does not independently identify which individual memory action caused an outcome. A theory-builder interpretation is not established by scalar ranking and distributed parameter updates; no claim of autonomous theory building or exercised production self-improvement is made here.

### Claims

#### RT-CLM-tool-protocol
Label: Consistent tool protocol claim

Claimed operation: prompt structure ensures consistent reasoning/tool/final-answer format and supports multiple calls per step. Source: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px7`. Assessed scope: declared model response protocol. Guarantee owner is prompt author/model compliance, with executable parser enforcement uninspected; guarantee strength: policy. Design conclusion status: claimed. Implementation and operation conclusion status: uninspected. Figure 6 accepts a string span, but Appendix B.2's `full` versus the all/numeric operational description prevents treating the illustrative case as proof of strict semantic argument validation. No malformed-output handling or multi-call transaction contract is inspectable.

> This prompt structure ensures that the agent follows a consistent format for reasoning, tool invocation, and final answers, which is essential for reliable parsing and reward computation during RL training.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-CLM-context-reset
Label: Context reset leakage claim

Claimed operation: resetting context before Stage 2 forces later reliance on LTM rather than residual Stage 1 context. Source: SRC-1, `2601.01885v1.html#S3.SS1`, `2601.01885v1.html#A1.SS3.SSS0.Px2`, Algorithms 1, 3–5. Owner/enforcement point: training driver reset of C. Guarantee strength: protocol. Design conclusion status: claimed. Implementation and operation conclusion status: uninspected. The reset covers the named short-term message context, not all host/model state. Stage 3 deliberately retains Stage 2 context. Algorithm 3/4 state tuples include q despite prose withholding it until Stage 3, so actual query visibility is unresolved. This is a local inconsistency and evidence limit, not grounds to assert the implemented curriculum leaks.

> Since the task query has not yet been revealed in Stage 1, the agent must rely on general cues about which information may become useful later.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### RT-CLM-evaluation-oracles
Label: Evaluation oracle account

Claimed operation: HotpotQA memory quality compares stored predicted facts against expected supporting facts; answer judgment compares the agent answer against the ground-truth answer using Qwen-Max. Sources: SRC-1, `2601.01885v1.html#A3.SS2`, `2601.01885v1.html#S4.SS1`. Reported experiments do not provide independently inspectable runs or causal identification of each memory mechanism. The oracle is a dataset reference interpreted by an LLM, not the agent's confidence or self-assessment. Simulation benchmarks instead use success/progress metrics. This distinction bounds what the scalar scores supervise.

> The evaluator compares the stored memory entries (predicted supporting facts) with the ground-truth supporting facts provided in the HotpotQA dataset.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-policy
Label: System prompt to policy

Consumer: task agent policy. Channel: tool-calling system prompt plus available-tools descriptions. Force: natural-language instruction requesting a reasoning/action/answer protocol; no demonstrated compliance guarantee. Horizon: each invocation receiving the static supplied prompt, not acquired memory read-back. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px7`, [RT-OBJ-tool-prompt](#rt-obj-tool-prompt), [RT-CLM-tool-protocol](#rt-clm-tool-protocol). Model-generated symbolic call envelopes then request executor effects, whose validation remains uninspected.

#### RT-BAP-trained-policy
Label: Training update to later decisions

Consumer: subsequent rollout/evaluation policy invocation. Channel: learned model parameters from [RT-RTE-policy-update](#rt-rte-policy-update). Force: distributed-parametric influence over the action distribution, not a symbolic veto. Horizon: training iterations and reported evaluation after RL; persistence across deployed processes/sessions is uninspected. Source: SRC-1, `2601.01885v1.html#alg2`, `2601.01885v1.html#S4.SS1`, [RT-CMP-agent-policy](#rt-cmp-agent-policy). The design places outcome-responsive parameter updates on a behavior-shaping path; this paper capture does not independently establish subsequent causal dependence or production activation.

## Annotations

none
