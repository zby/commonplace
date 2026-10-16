---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Document-grounded runtime baseline of trajectory-informed memory generation: trajectory processing, admission, alternative retrieval paths and the reported AppWorld consumer."
run-id: AAS-2026-10-14-2603-10600v1-a956324c9a82-01
reviewed-boundary: "arxiv-2603.10600v1-html-captured-2026-10-14"
---

# Trajectory-informed memory generation runtime report

## Runtime account

### Evidence and consequential work

The target is the paper's memory pipeline, not an enclosing agent runtime. The frozen HTML supplies design descriptions and reported evaluation, not inspected executable behavior. There is no shipped executable entry point to establish from this capture. The documented entry paths are completed trajectories entering extraction and a new task entering retrieval. Model-provider internals, persistence implementation, consumer code and raw runs remain outside the evidence. All source references below are SRC-1 at the sections named; the capture identity and source register are in [the boundary](boundary.md#source-register).

The consequential work is producing reusable behavioral guidance from agent experience, consolidating it, then selecting and delivering it to later agent invocations. This is not a claim that the system modifies agent weights or production machinery. The declared model and embedding components are [RT-CMP-gpt4](#rt-cmp-gpt4) and [RT-CMP-text-embedding](#rt-cmp-text-embedding). The production and admission routes are [RT-RTE-trajectory-extraction](#rt-rte-trajectory-extraction) and [RT-RTE-tip-consolidation](#rt-rte-tip-consolidation); alternative selectors are [RT-RTE-cosine-retrieval](#rt-rte-cosine-retrieval) and [RT-RTE-llm-selection](#rt-rte-llm-selection). Both feed [RT-RTE-agent-execution](#rt-rte-agent-execution), through the advisory authority channel [RT-BAP-guidelines-channel](#rt-bap-guidelines-channel).

### One documented invocation, end to end

A completed execution supplies sequential invocations, contexts, thoughts/reflections, actions and results. Evaluation reports are optional. The extraction pipeline classifies reasoning, identifies patterns, derives an outcome classification, traces decisions backward from outcomes, and proposes category-specific tips. With external outcome labels it uses those labels; without them it infers outcome from the agent's own signals. This alternate is consequential: the design does not require an independent correctness oracle for every retained lesson. SRC-1, §§3.1.1–3.1.3.

For subtask extraction, a segmentation model sees the full trajectory and emits generalized subtask descriptions, applications, source step ranges and purposes. Independent calls then produce 2–4 tips per subtask. Task-level extraction instead treats the full trajectory as one unit; both granularities can coexist. The separate calls focus input on a logical phase, rather than establishing separate agent security principals or an isolation envelope. No host-side truncation, compaction or mid-execution reload mechanism can be established from this description. SRC-1, §3.1.4.

The management phase abstracts descriptions, clusters similar descriptions and consolidates associated tips. The LLM is asked to deduplicate, resolve contradictory guidance using outcome metadata, and synthesize complementary guidance. A canonical cluster description replaces per-trajectory descriptions for retrieval. These are semantic admission decisions, not just physical writes. Vector and structured-metadata storage are described, but concrete transactions, reload implementation and rollback are not inspectable. SRC-1, §3.2.

A later user task triggers retrieval before reasoning begins. The cosine path embeds the task and compares stored descriptions, applying a threshold and optionally a top-k limit. The LLM path derives application/category filters and category priorities, retaining access to generic tips. Selected tip content, purpose, steps, priority and trigger are formatted into a guidelines section after task context and before standard instructions. The consumer therefore receives selected, transformed guidance, not the full original trajectory or every retained tip. SRC-1, §§3.3.1–3.3.3.

The reported consumer is a single simplified ReAct agent: GPT-4.1 reasons, chooses API actions, receives results and continues until completion or unrecoverable failure. The evaluation caps tasks at 30 reasoning-action steps, and AppWorld tests examine final application state. The memory system chooses guidance; the consumer chooses actions; the application APIs execute effects; AppWorld judges results. The paper does not expose runtime-client permission grants, API authorization, approval callbacks, delegation, shell/subprocess paths or deployed isolation. None of those responsibilities can be attributed to the memory pipeline merely because tips name APIs. SRC-1, §§4.1.1–4.1.5.

### Controls, forcing cases and guarantees

The two retrieval strategies, two extraction granularities and optional outcome labels are the material documented alternatives. Three forcing cases bound the account:

1. **No independent labels:** extraction still proceeds by inferred outcome. Thus externally verified success is not a universal admission condition (§3.1.1).
2. **Restrictive or uncapped cosine selection:** §4.1.4 says both strategies retrieve five tips, but §§4.2.2–4.2.3 explicitly report top-3 and no-top-k cosine variants. A universal five-tip bound would be false. The top-k control covers only configurations applying that cap.
3. **Guidance can harm:** the top-3 task-level cosine configuration scores below baseline in aggregate; train Difficulty 1 also declines with memory. Therefore delivery cannot be treated as guaranteed benefit, and the paper's broad “all configurations” language must be narrowed. See [RT-CLM-reported-results](#rt-clm-reported-results).

The selection owner is the retrieval pipeline. A threshold/top-k policy is described at filtering and ranking, not enforced in inspected code. Its guarantee strength is **policy**, design conclusion status **claimed**, implementation conclusion status **uninspected**, operation conclusion status **uninspected**. Coverage is the configured cosine branch, not LLM selection or explicitly uncapped cosine experiments. The external contract requires compatible embeddings and correct vector-store filtering/ranking. Numerical scores do not guarantee semantic relevance. SRC-1, §3.3.1 and §§4.2.2–4.2.3.

The consolidation owner is the merging LLM, with requested conflict precedence at the merge step. Guarantee strength is **best effort**, design conclusion status **claimed**, implementation conclusion status **uninspected**, operation conclusion status **uninspected**. It covers tips collected into a cluster, not contradictions missed by clustering, and depends on metadata quality and model compliance. It does not guarantee correctness of original causal attribution. SRC-1, §§3.2.2–3.2.3.

The evaluation driver owns the stated 30-step task limit, not the memory system. Guarantee strength is **protocol**, design conclusion status **claimed**, implementation conclusion status **uninspected**, operation conclusion status **uninspected**. Its described coverage is the evaluation tasks, not arbitrary deployments; enforcement requires the unavailable driver. There is no supplied execution trace establishing its operation. SRC-1, §4.1.5.

## Shared records

### Components

#### RT-CMP-gpt4
Label: GPT-4.1

Source-native identity: GPT-4.1, used for both the evaluation agent and tip extraction pipeline. Representational form: distributed-parametric model; provider-hosted parameter storage is opaque. Exact model snapshot/version is not pinned by the family label. The paper describes no parameter update in this pipeline; actual provider mutability and whether an endpoint can resolve to another snapshot are uninspected. Optional different models for segmentation and per-subtask extraction are a design alternative, not a reported deployment fact. SRC-1, §§3.1.4, 4.1.2.

> Both the agent and the tip extraction pipeline use GPT-4.1.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### RT-CMP-text-embedding
Label: Text embedding model

Source-native identity: unspecified text embedding model used for tip/description and query embeddings. Representational form: distributed-parametric model producing dense vectors; parameter substrate/provider is unspecified, while output vectors enter vector storage. Neither an exact version nor a model family is pinned. Parameter change during operation and mutable-endpoint substitution are uninspected; producing new vectors does not itself establish parameter learning. SRC-1, §§3.2.2–3.3.1.

> is a dense vector computed from the tip content and purpose using a text embedding model.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

The paper additionally describes canonical-description embeddings and query-to-description comparisons. These roles should not be collapsed into an assumption that every stored vector embeds the same text. Compatibility between tip-content and description indices is not specified in executable form.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-trajectory-extraction
Label: Trajectory analysis and tip extraction

Endpoints and progression: completed trajectory → structured reasoning/outcome representation → decision attribution → proposed memory tips. The pipeline owns progression; LLM semantic judgment supplies pattern recognition, attribution and generation. Output contains natural-language advice and explanatory purpose with structured categories, triggers, priorities and source IDs. State is the trajectory and intermediate representation, not a modified agent executable. SRC-1, §§3.1.1–3.1.4.

- Immediate return: Structured analyses and proposed strategy, recovery and optimization tips; subtask mode first emits segmentation and then per-subtask tips.
- Later read-back: Tips are passed through management and ultimately selected for later task prompts; raw thoughts are not described as the ordinary retrieved unit.
- Delegated visibility: Segmentation sees the full trajectory; per-subtask calls independently analyze scoped subtasks. Exact prompt contents and external worker principals are uninspected.
- Selection predicate: Outcome indicators and semantic pattern/decision analysis; task-level whole trajectory or subtask-level logical phases.
- Invalidation or expiry: uninspected — no executable invalidation or expiry contract is supplied for intermediate or generated material.
- Activation or effect: Claimed generation of behavioral guidance; individual attribution correctness and later behavioral activation are not observed.
- Evidence limits: Design prose and illustrative tips, not extraction prompts, raw runs or implementation.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admission account: completed task evidence triggers a proposed knowledge/instruction change. The computational proposer and initial judge are the model pipeline; no per-tip human approval or human veto is established. Category-specific prompts request concrete, generalizable guidance. Management is the subsequent admission stage. Rejection and rollback of extraction output are uninspected. The operating mode is generic completed-trajectory processing, with a reported bounded AppWorld train/dev corpus. Optional benchmark labels are an external answer oracle supplied by the evaluation harness; unlabeled mode instead uses self-reflective signals, not an independent oracle.

> Crucially, ground-truth outcome labels (success or failure) are not required: when they are available—for instance, from a benchmark evaluation harness—the system uses them directly to classify the trajectory; when they are absent, the system infers outcome from the agent’s own self-reflective signals identified in subsequent stages.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

Theory account: the declared output includes localized conditional prescriptions and explanations of why decisions produced outcomes. Such content can express a limited theory of task performance; output labels alone do not establish it in every entry. For these described units, theory-builder conditions 1–4: **1 claimed**, through content, purpose, triggers and steps; **2 claimed**, through intended downstream use, not verified content-dependent decisions; **3 uninspected**, because backward attribution to original decisions does not establish criticism of a previously retained tip; **4 uninspected**, because a proposed cycle does not show retained criticism shaping another round. Addressability is described at tip and metadata-field granularity, not as an inspectable assumption editor. Persistence is intended across tasks/sessions through storage; attained persistence is not independently observed. Under learning: the paper reports later performance differences, but no individual extraction component's capacity effect is isolated. Reflection is claimed at the design level through trajectories representing past behavior and tips feeding later behavior; both causal directions remain unobserved. Autonomous internal proposal is described, but full operational autonomy, reflective theory building and exercised self-improvement are not established. For the latter, the proposed horizon is future AppWorld tasks and objective is goal completion: evidence-responsive proposal, retained guidance and prompt delivery are described, while subsequent content-dependent behavior (causal link 4) remains unestablished by the aggregate results alone.

#### RT-RTE-tip-consolidation
Label: Tip storage and consolidation

Endpoints and progression: extracted descriptions/tips → LLM generalization → embedding similarity and hierarchical clustering → LLM deduplication, conflict resolution and synthesis → canonical description plus consolidated store entries. The pipeline owns scheduling; clustering uses a symbolic threshold over distributed vectors, while semantic transformations use model judgment. Natural-language guidance, numerical embeddings and structured metadata have different consumers. SRC-1, §§3.2.1–3.2.4.

- Immediate return: Canonical cluster descriptions and consolidated tips with vector and metadata representations.
- Later read-back: Retrieval uses canonical subtask descriptions or original task descriptions to select associated tips for later agents.
- Delegated visibility: Consolidation receives associated tips within each cluster, regardless of source trajectory or granularity; exact model prompts are uninspected.
- Selection predicate: Hierarchical agglomerative clustering over generalized-description cosine similarity, with approximately 0.85 given empirically; merge conflicts use category, priority and source success/failure.
- Invalidation or expiry: Canonical cluster descriptions replace individual per-trajectory descriptions; general tip expiry and reversible history are uninspected.
- Activation or effect: Claimed replacement/consolidation of retained guidance; no supplied stored artifact verifies a particular merge or its downstream effect.
- Evidence limits: Design description, without persistence code, observed merge decisions or transaction/reload evidence.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admission account: accumulated redundant or inconsistent tips trigger changes to retained guidance. The LLM proposes and decides the merged content, guided by deduplication, conflict-precedence and synthesis instructions. Outcome metadata is evidence for ranking, not a fresh answer oracle validating a merged prescription. The model can prefer one contradictory tip over another; no separate evaluator, human per-entry approval, rollback or failed-merge recovery is established. The generic design handles accumulated trajectories; the reported operating mode builds memory from train/dev. What persists is synthesized instruction content, provenance metadata and re-embedded canonical descriptions.

> Tips derived from successful trajectories take precedence over those from failed ones, and recovery tips that encode proven correction patterns take precedence over speculative prevention strategies.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

Theory account: existing prescriptions shape the synthesized successor, but outcome-precedence selection is not itself demonstrated content-directed criticism. Theory-builder conditions 1–4: **1 claimed** for consolidated whole tips; **2 claimed** for semantic consolidation and later advice; **3 uninspected** because no retained criticism naming a challenged claim, test and blame placement is supplied; **4 uninspected** because no criticism-to-next-round trace is supplied. Addressability and intended persistence are at consolidated tip/cluster granularity across tasks. Under learning: no separately varied consolidation treatment establishes its benefit. Reflection and autonomous revision are described computationally but not operationally verified; this does not negate the supported design-level semantic update path.

#### RT-RTE-cosine-retrieval
Label: Cosine similarity retrieval

Endpoints and owner: a new task description enters the retrieval pipeline; its embedding is compared to stored task/subtask description embeddings; selected associated tips leave for prompt integration. Decision policy is numerical similarity filtering and ranking, not an LLM decision at retrieval time. SRC-1, §§3.3.1, 4.1.4, 4.2.2–4.2.3.

- Immediate return: Selected tips for the guidelines section.
- Later read-back: This is the later read-back of accumulated tips; selection itself is not described as changing retained guidance.
- Delegated visibility: inapplicable — this selector is described as a vector lookup, not a delegated model invocation.
- Selection predicate: Similarity at or above configured threshold, followed by optional top-k ranking; reported alternatives include top-3 and no top-k restriction.
- Invalidation or expiry: uninspected — retrieval-time freshness checks and stale embedding invalidation are not specified.
- Activation or effect: Delivery is described; particular tips changing consumer behavior is not independently observed.
- Evidence limits: No vector database implementation, index artifact, query trace or latency measurement supplied.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

The selector decides which candidates enter context; no human per-selection decision or answer oracle is established. Its modes are generic task requests and the bounded benchmark variants. It changes working context by excluding unselected retained material and bringing selected content into the initial prompt. No eviction or mid-run reload follows from this initial selection.

> This strategy requires no LLM calls at retrieval time and is fast and inexpensive—a pure vector database lookup.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### RT-RTE-llm-selection
Label: LLM-guided selection

Endpoints and owner: new task → model analysis of context/category → structured query combining semantic similarity, metadata filtering and priority-weighted ranking → selected tips. The LLM proposes query criteria; the retrieval system executes them. SRC-1, §§3.3.2, 4.1.4.

- Immediate return: Selected tips for prompt integration.
- Later read-back: Retrieves accumulated guidance for a later invocation; no selector write-back is established.
- Delegated visibility: The selection model receives the task description; visibility of a full tip corpus or exact prompt is uninspected.
- Selection predicate: Application/domain filters including generic null-context tips, inferred task category and relevance of strategy/recovery categories; evaluation describes priority-weighted ranking and top five.
- Invalidation or expiry: uninspected — no concrete freshness or query invalidation contract supplied.
- Activation or effect: Claimed richer matching; reported aggregate comparisons do not expose individual selection decisions or behavioral activation.
- Evidence limits: No executable query builder, model version for this specific role, raw selected-tip trace or measured overhead.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

The decision is computational, with no established human veto or answer oracle. Generic new-task requests and benchmark selection are distinct from an experimental search over candidate successors. The additional LLM call is a declared cost, not a latency measurement. This path controls initial working context; it does not establish host compaction, delegation of task execution or a capability grant.

> LLM-guided selection is more expensive (requiring an additional LLM call per task) but can reason about nuances that pure embedding similarity misses.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

#### RT-RTE-agent-execution
Label: Prompt integration and agent execution

Endpoints and progression: selected tips → formatted guidelines in the agent prompt → GPT-4.1 reasoning/action/observation loop → final task outcome → AppWorld evaluation. The memory integration supplies natural-language advice; the consuming agent owns next-action decisions; application APIs own actual state effects. SRC-1, §§3.3.3, 4.1.1–4.1.5.

- Immediate return: Agent completion or unrecoverable failure; evaluation produces task/scenario goal scores from application state tests.
- Later read-back: Resulting trajectories may enter the extraction design cycle; the evaluation does not establish repeated online updating after every test task.
- Delegated visibility: inapplicable — the reported consumer is single-agent; cross-agent attribution is left to future work in §6.
- Selection predicate: Consumer decisions depend on task, standard instructions, available APIs, current observations and delivered guidelines; exact action policy is not inspectable.
- Invalidation or expiry: The evaluation treats tasks independently and caps each at 30 steps; exact context disposal, stop implementation and durable state reset are uninspected.
- Activation or effect: The paper reports goal-completion comparisons; no supplied trace establishes which delivered tip changed an action.
- Evidence limits: Consumer and evaluator are described, not inspected; no permission grants, sandbox configuration, retry machinery or raw execution evidence.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

AppWorld supplies the external answer oracle after execution: tests check API usage, database state and expected end states. Passing all task tests defines TGC; passing every task variant defines SGC. This oracle evaluates results, not each next-action choice or each merged tip. It is not shown as a universal runtime admission gate. Terminal textual answer shape is unspecified.

> The agent continues this loop until it determines the task is complete or encounters an unrecoverable failure.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

### Claims

#### RT-CLM-reported-results
Label: Reported AppWorld benefits and counterexamples

Claimed operation: the memory-enhanced single agent improves aggregate held-out outcomes. SRC-1, §4.2, Tables 1–7: baseline 69.6% TGC/50.0% SGC; subtask plus LLM selection 73.2%/64.3%; subtask cosine 73.8%/57.1%; task-level cosine at threshold 0.6 without top-k 72.0%/62.5%. These are attributed results, not independent observations or isolated proof of the proposed attribution mechanism.

A universal improvement claim fails within the same evidence: task-level cosine at threshold 0.5/top-3 reports 66.7%/48.2%, below baseline, and train easy tasks also decline. Furthermore §4.1.4's five-tip statement conflicts with explicit later parameter variants; use configuration-specific settings rather than projecting five onto every run. No raw repeated-run evidence, uncertainty estimates or component-isolated causal attribution is supplied by the frozen capture.

> On train Difficulty 1 tasks where the baseline already achieves 100%, the memory-enhanced agent scores slightly lower (94.4% TGC, 83.3% SGC), suggesting that for simple tasks where the agent already performs optimally, injecting additional tips can introduce minor interference.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-guidelines-channel
Label: Retrieved guidelines channel

Consumer: the simplified ReAct agent. Channel: natural-language guidelines in its initial prompt after task context and before standard instructions. Force: advisory behavioral instruction interpreted by the model, not API authorization or a hard reference monitor. Horizon: the current task invocation, with retained tips eligible for later invocations through retrieval. SRC-1, §3.3.3; related route [RT-RTE-agent-execution](#rt-rte-agent-execution).

> Regardless of retrieval strategy, the selected tips are injected into the agent’s prompt as a “guidelines” section positioned after the task context but before the standard agent instructions.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

This documents delivery and intended behavioral authority. It does not establish instruction-hierarchy precedence, reliable compliance, current tool grants or isolation. Selection, advice and execution remain different boundaries.

## Annotations

none
