---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "WikiSkill runtime baseline: documented task execution, wiki maintenance, skill proposal and validation rollback at the frozen arXiv v1 capture."
run-id: AAS-2026-10-15-2608-27454-65116a9d0de7-01
reviewed-boundary: arxiv-2608.27454v1-text-2026-10-15
---

# WikiSkill runtime report

## Runtime account

WikiSkill's documented work is to turn task execution experience into persistent wiki knowledge and validation-selected procedural skills. The boundary is a complete paper capture, not a shipped executable distribution. No CLI, library entry point, parser, tool implementation or harness checkout is supplied. The entry paths below are therefore the paper's specified invocation paths, not verified shipped APIs. SRC-1, §2–3, Appendix A and E, provide doctrine/design; §5 provides reported operation. The [boundary](boundary.md) fixes the capture and its limits. No target execution was performed or supplied as an inspectable trace bundle. Implementation, activation and causal benefit remain uninspected even where the paper reports results.

### Ordinary evolution invocation

A caller supplies training tasks, validation tasks, a scoring metric and an iteration budget to the outer-loop harness (SRC-1, Appendix A.1). Caller identity and any interactive human control are unspecified. The declared initial state is empty skills and wiki. The harness evaluates the empty skill set on validation tasks to initialize the best score. Each subsequent iteration has four ownership transfers:

1. **Harness to Inference Agent.** For each training task the model gets task context and the full active skill contents in its system prompt. It chooses reasoning steps and permitted task-tool actions; tools or the simulator execute effects. It returns a prediction or task artifact, and the harness retains execution traces. [RT-RTE-task-execution](#rt-rte-task-execution) gives the task-specific return and answer-oracle boundaries.
2. **Harness to Wiki Maintainer.** Code-described stratification supplies at most eight training traces, with at most five failures and three successes. Each log is capped at 15,000 characters. The model also receives the current wiki. It returns JSON containing pattern creations/patches, a complete replacement index and a log append. The surrounding system applies these edits. No validation acceptance gate is described for these wiki changes. [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance) separates this authority from skill admission.
3. **Harness to Skill Proposer.** The proposer receives the wiki index, impact history and a summary of all training outcomes including predictions and ground truth. A multi-turn ReAct model chooses which pattern pages and traces to inspect through `read_file`, then submits `create`, `patch` or `no_action` through `finish`. The stated output targets one skill. [RT-RTE-skill-proposal](#rt-rte-skill-proposal) describes this selective context and proposal-only authority.
4. **Harness to evaluator and back.** The harness applies the proposal provisionally and rolls out the candidate skills on validation tasks. A strict score increase over the incumbent best admits the candidate; a tie or lower score restores the last accepted skills. In either case the wiki remains and the harness appends the proposal diff, score and decision to its impact tracker. [RT-RTE-validation-gate](#rt-rte-validation-gate) owns the admission decision. There is no described per-candidate human approval.

The loop stops at its iteration budget or a best validation score of 1.0, returning skills and wiki. Appendix A uses a final `S_K, W_K` return even with early termination; actual variable handling is not inspectable. Training and validation invocation state is distinct from retained files. Cross-iteration coordination is serial in the algorithm, through filesystem workspace state and the best-score variable. Task rollout scheduling/concurrency, locking, crash recovery and atomic application of multiple filesystem edits are uninspected. Rejection rollback is a specified recovery path, not evidence of crash-safe transactions.

The model substrate is distributed-parametric; the evolving skill and wiki content is primarily natural language, while JSON action fields, patch operations and score comparisons have symbolic consumers. [RT-CMP-model-backends](#rt-cmp-model-backends) records model fixity limits. [RT-BAP-skill-injection](#rt-bap-skill-injection) identifies how an accepted instruction artifact can reach later task behavior without a model-weight update.

### Material forcing and alternate routes

The following three source-supported checks qualify the ordinary path. These are inspected descriptions, not executed forcing tests.

**1. A rejected or neutral skill is not a rejected wiki update.** SRC-1, §3.2.4 and Appendix A, specify rollback of skills only. §5.3 reports a rejected initial `goal-directed-action` proposal whose retained history informs a later `break-repetition-loop` proposal. Thus the validation gate cannot be generalized to all retained behavior-shaping content. A neutral immediate proposal is also rejected by the strict comparison, even if it could enable later gains (§7 Limitations). The score gate covers the ordinary candidate-skill path, not wiki pattern admission or all future influence from rejected proposals. Details and quotes are in [RT-RTE-validation-gate](#rt-rte-validation-gate).

**2. Tool-free inference, shell inference and simulator inference have different effect boundaries.** SRC-1, Appendix B and E.1, specify LiveMath as single-step direct reasoning with no external tools, SpreadSheet as Python manipulation through a bash tool, and ALFWorld as actions against an interactive simulator. SealQA adds remote web search and file reading; OfficeQA uses local document search/read tools and initially supplied oracle reference pages. A uniform multi-turn tool loop is therefore not the universal inference path. The spreadsheet prompt claims path confinement while also advertising arbitrary shell commands; no shell wrapper or isolation implementation establishes that confinement. ALFWorld's prompt supplies recent observations/actions and an admissible-action list at each step, but enforcement of action membership and the history-window selection rule are uninspected. These paths are included in [RT-RTE-task-execution](#rt-rte-task-execution).

**3. Restricted wiki access is a default experimental mode, not a universal capability limit.** SRC-1, §3.2, restricts the default Inference Agent from the wiki, while §5.1 explicitly describes an experimental mode that grants it wiki access. The maintainer prompt's index rule even refers to inference agents reading patterns, although default inference is described as isolated from wiki. This wording does not establish such access in the default mode. Full skill injection also differs from the progressive-disclosure capability discussed generally in the introduction: the studied route injects all active skills, without task-relevance retrieval (§3.2.1, §7). No provider-native tool path, extension callback, remote worker, direct bypass of admission, manual graph-control surface or durable workflow variant is specified in the inspected method and prompts. That limits assessment; it is not an absence claim about an unavailable implementation.

### Guarantees and enforcement boundaries

| Claimed guarantee | Owner and enforcement point | Strength and coverage | External contract and conclusion limits |
|---|---|---|---|
| Only strict validation improvements enter active skills | Outer harness, score comparison and restore step; [RT-RTE-validation-gate](#rt-rte-validation-gate) | protocol; covers normal single-skill candidate application, not wiki maintenance | Requires faithful evaluator, saved incumbent and correct application/restore. Design conclusion status: claimed. Implementation conclusion status: uninspected. Operation conclusion status: uninspected. Finite validation improvement is not a guarantee of unseen-task improvement. |
| Wiki survives skill rejection; raw history is immutable | Workspace/harness and raw storage policy, §3.1–3.2.4 | policy; wiki retention and raw immutability are described, not filesystem protections | Requires persistence and write boundaries in unavailable host code. Design conclusion status: claimed. Implementation conclusion status: uninspected. Operation conclusion status: uninspected. |
| Default inference cannot access wiki | Harness/environment at inference construction, §3.2 | policy; default mode only, not the wiki-enabled ablation | Requires tool/path restrictions beyond withholding prompt context, especially with bash. Enforcement mechanism is unspecified. Design conclusion status: claimed. Implementation conclusion status: uninspected. Operation conclusion status: uninspected. |
| Spreadsheet reads/writes confined to task directory | Claimed task environment; exact check point unavailable, Appendix E.1 | policy; spreadsheet prompt only, not a demonstrated deployment guarantee | Requires shell/filesystem isolation covering subprocesses and all shell commands. Design conclusion status: claimed. Implementation conclusion status: uninspected. Operation conclusion status: uninspected. |

The capability surface includes arbitrary-command bash for the spreadsheet task; the current grant set is the task-specific tool configuration, not every tool for every role. The deployed isolation envelope is unknown. Prompt restrictions, model compliance and operating-system confinement are distinct. No permission/approval system or security assurance can be derived solely from these prompts. The relevant source passages are retained in the route records below.

## Shared records

### Components

#### RT-CMP-model-backends
Label: Model backends

SRC-1, §4.1, names Gemini-3.5-Flash, Qwen-3.5-4B/9B-Instruct, Qwen-3.6-27B and Gemma-4-31B-It, with vLLM deployment for open-weight models. Identity is the named model families/variants used across the documented experiments, not one proven immutable endpoint. Representational form: distributed-parametric. Storage substrate: model weights behind the closed service or open-weight serving deployment; provider internals and deployment artifacts are uninspected. The inference, maintainer and proposer roles use LLM computation (§2–3, Appendix D.2); exact per-role backend configuration is not established by the capture.

> For closed models, we use Gemini-3.5-Flash (Google DeepMind, 2026). For open-weight models, we evaluate Qwen-3.5-4B/9B-Instruct (Qwen Team, 2026a), Qwen-3.6-27B (Qwen Team, 2026b), and Gemma-4-31B-It (Gemma Team, 2026), which we deploy using the vLLM framework (Kwon et al., 2023).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Parameter changes during operation: no parameter update is specified in the evolution algorithm; its explicit mutable state is skills/wiki and the validation threshold. Exact weight snapshots are not pinned by the paper's model names. Whether a mutable endpoint can resolve to another model is uninspected, including the closed service and serving configuration. This does not negate learning through retained textual artifacts.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-task-execution
Label: Task execution with active skills

Endpoints and progression: harness-supplied task plus active skills → task model → tools/environment where available → prediction or artifact and execution trajectory. The task model owns next-action decisions; the harness owns task selection, skill injection, evaluation and trace retention. The model's policy is natural-language task instructions and skill contents interpreted through distributed parameters. The environment executor supplies tool results; effect boundaries differ by task.

SRC-1, §3.2.1 and Appendix B/E.1:

> In WikiSkill, the full content of active skills Sk−1S_{k-1} is injected directly into the Inference Agent’s system prompt.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> You can ONLY read and write files within the **working_directory**. Any attempt to access files outside this directory will fail.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> You have access to a bash tool that can execute any shell command.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

- Immediate return: LiveMath/SealQA/OfficeQA request final answers in answer tags; SpreadSheet requests an output spreadsheet at the supplied path; ALFWorld requests a tagged admissible action for the current simulator step. Training trajectories include reasoning, calls, outputs and final answers (§3.1).
- Later read-back: Active skill text is supplied to later task invocations; retained training traces reach maintainer and proposer through their separate routes. A task agent is not described as reading prior raw traces by default.
- Delegated visibility: Maintainer gets sampled/capped traces; proposer gets outcome summaries and on-demand trace access, not an established verbatim transfer of every task context.
- Selection predicate: Harness selects the benchmark task/split and injects the entire active skill set; no skill relevance retrieval is evaluated. Task model selects tool actions subject to the described tool surface.
- Invalidation or expiry: Rejected skills revert to incumbent; accepted skills remain until later accepted changes. Current task context lifetime is unspecified. ALFWorld receives a recent history slice with unspecified window length/selection implementation.
- Activation or effect: Design intends skill-conditioned reasoning and tool/environment actions. Delivery alone does not establish obedience or actual behavioral change; supplied execution artifacts are unavailable.
- Evidence limits: SRC-1 §2–3.2.1, Appendix B/E.1 describe the route, not implementation or observed calls. Shell confinement, wiki denial and tool-action validation are uninspected.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Operating modes: training, candidate validation and final held-out testing, plus the explicitly wiki-enabled training ablation (§5.1). The harness/evaluator decides scores, not the task model. The answer oracle is the benchmark's ground-truth outcome and domain scoring function (§2); exact scoring code is unavailable. OfficeQA's initial oracle reference pages are evidence delivery, not proof of an expected-answer oracle supplied to every inference agent. Human contribution is dataset/setup provision as described, with per-task or per-candidate intervention unspecified. Model reasoning/action changes within a task are not online skill revisions; §7 describes online single-rollout skill adaptation as future work.

#### RT-RTE-wiki-maintenance
Label: Trace consolidation into wiki

Endpoints and progression: harness samples training traces and supplies current wiki → maintainer model diagnoses patterns → JSON edit response → system-applied wiki updates. Trigger: completion of training rollouts each iteration. The model proposes knowledge text and edit operations; the surrounding system is the filesystem executor. Natural-language claims and workarounds have model consumers; JSON keys and exact-substring edits have symbolic consumers. SRC-1 §3.2.2, Appendix C/E.2:

> Specifically, the system samples up to 8 traces per iteration, stratified into a maximum of 5 failing traces (to perform root-cause analysis of errors) and up to 3 passing traces (to identify effective strategies and prevent regressions in working behaviors). Each individual execution log is capped at 15,000 characters prior to injection into the prompt.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> "update_index" and "append_log" are REQUIRED. Always provide them, even if there are no new patterns. For "update_index", always provide the complete updated index content including all existing entries plus any new ones.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

- Immediate return: JSON create_patterns, update_patterns, update_index and append_log, intended for the intermediate wiki state.
- Later read-back: Patterns, index and chronological log persist across iterations for later maintainer/proposer consumption; the proposer initially receives a smaller context than the maintainer.
- Delegated visibility: Maintainer gets the current wiki and sampled/capped logs, not all training trajectories in full. Its edited index guides the proposer's further reads.
- Selection predicate: Harness stratifies by success/failure; model decides which meaningful patterns merit creation/refinement. Pattern prompt requests root cause, exact command evidence and concrete solutions, with 10–30-line pages and no duplicates.
- Invalidation or expiry: Wiki is retained despite rejected skills. Pattern content can be replaced/refined; index is fully regenerated. No bounded expiry is specified; §7 explicitly states lack of automated wiki pruning.
- Activation or effect: Intended durable knowledge changes shape subsequent proposals. Whether edits apply correctly and whether later decisions depend on their content is uninspected.
- Evidence limits: No edit parser, patch failure policy, content-review gate or persisted wiki bundle is available. The body uses logs.md while E.2 uses wiki/log.md; runtime filename resolution is unresolved, not evidence of two distinct logs.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Admission and decision roles: the model authors the content and selects edits; the system applies them without a described validation/human veto for wiki content. Format/substring constraints are prompt instructions, not verified rejection rules. Recovery from malformed JSON, missing targets or partial application is uninspected. No content rollback is described on skill rejection. Guidance is the maintainer's deep-analysis and pattern-documentation prompt. What persists is pattern explanations, proposed fixes, index and log, not model weights. Operating mode is a bounded training/evolution experiment; the upstream scorer identifies passing/failing tasks, not the maintainer's unsupported judgment alone.

Theory account: the prompt requests explanations of why failures happen and how to avoid them. This supports a claimed route for formulating localized natural-language explanations, not proof of correct explanations. Theory-builder conditions 1–4: 1, claimed — pattern pages are requested to carry description, cause and solution; 2, claimed — later proposal is specified to use patterns; 3, uninspected — requests for root-cause analysis do not establish a particular claim/result/blame/revision chain; 4, claimed — revised pages are retained for subsequent iterations, but criticism-specific iteration is uninspected. Addressability: page-level identity and exact-span patches expose parts for inspection/revision in the design. Persistence: rounds of one evolution run. Learning: improved future capacity is author-reported in §5, not independently established for this route. Reflection: the design requests representations of the task agent's own actions and skill adherence that can influence later instructions; exercised two-way dependence is uninspected. Reflective theory builder and autonomous theory builder: uninspected — no trace establishes all four conditions or every internal operation, although computational role ownership is specified.

#### RT-RTE-skill-proposal
Label: Wiki-guided skill proposal

Endpoints and progression: updated wiki/active skills/training outcomes → proposer ReAct context → selected read_file results → finish JSON proposal. The proposer model owns diagnostic reads and candidate content; the harness owns supplying context, resolving trace aliases and receiving the proposal. The available tools are reads and submission, not a documented arbitrary-write tool for this role. SRC-1 §3.2.3, Appendix E.3:

> The Proposer ℳP\mathcal{M}_{\text{P}} is an LLM-based agent responsible for skill discovery and refinement.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> You MUST read at least 4 execution traces before proposing a skill change. Target your exploration based on the trace summary.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> If no action is needed, call finish with: {"action": "no_action"}
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

- Immediate return: Atomic single-skill create or patch proposal, or no_action. Creation supplies SKILL.md with applicability/instructions and PURPOSE.md with origin, patterns and evolution history.
- Later read-back: Candidate contents enter later inference only if admitted; rejected proposal diffs remain in the impact history for later proposer invocations.
- Delegated visibility: Initial index, skill-impact history and all-task outcome summary; selected pattern/trace contents via reads. The traces/ alias resolves to raw/traces/. The maintainer's complete context is not automatically transferred.
- Selection predicate: Model chooses relevant patterns/traces using current failure summaries and historical interventions; prompt requests wiki-first inspection, no repeated rejected approaches, and at least four trace reads.
- Invalidation or expiry: Pending proposals are subject to admission/rejection; earlier history persists. ReAct context eviction/compaction and turn-exhaustion handling are uninspected.
- Activation or effect: Submission requests a candidate change, not admission. Requested adherence to trace-count and no-repeat rules is not verified.
- Evidence limits: Tool schemas, parser validation, no_action handling in the outer algorithm and replacement semantics of create on an existing name are not inspectable. E.3 permits create when changing most of a file; this is not enough to infer safe replacement behavior.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Decision roles and oracle: model proposes and may select no_action; software gate can veto installation. Ground-truth training answers, predictions and pass/fail outcomes are explicitly supplied (§3.2.3), unlike open-ended model judgment alone. Operating mode is bounded benchmark optimization, not an unrestricted user-request service. Guidance is wiki explanations, rejection history and the fixed proposer prompt; instruction/script/production-harness mutation beyond skill creation/patching is not specified. The described experimental skills consist of SKILL.md and PURPOSE.md, despite a broader generic skill format that can package scripts (§2–3.1).

Theory account: wiki patterns supply proposed explanations and concrete action rules; candidate skills encode procedures with applicability conditions. §5.3 reports a rejected rule followed by an accepted anti-loop rule and later refinement. This is attributed narrative, not a supplied full criticism transcript. Theory-builder conditions 1–4: 1, claimed — localized skill and pattern text; 2, claimed — content-guided synthesis; 3, uninspected — reported score rejection and rule refinement alone do not establish articulated blame on a theory versus test/data/auxiliaries; 4, claimed — retained histories guide further proposals, with criticism-specific iteration uninspected. Addressability: skill, pattern and span-edit granularity in design. Persistence: evolution rounds and a final reusable skill product. Learning: capacity gains are reported, but route-specific attribution and execution remain uninspected. Reflection: proposed instructions concern task-agent behavior and can return to it through injection; exercised causal closure is uninspected. Reflective/autonomous theory-builder attribution is uninspected for lack of condition-3 and full operation evidence, not disproved by that lack.

#### RT-RTE-validation-gate
Label: Validation admission and skill rollback

Endpoints and progression: proposal → harness applies candidate → inference on validation split → scorer computes mean performance → harness compares incumbent threshold → accepts or restores skills and records outcome. Trigger is proposal generation. Proposed change is a single skill creation or patch; executor and veto owner are the outer-loop harness, not proposer self-approval. SRC-1 §3.2.4, Appendix A and §7:

> If rejected, the system discards the candidate skill modifications and reverts the skill set to the most recent successful configuration Sk−1S_{k-1}.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> Notably, the wiki WkW_{k} is never rolled back regardless of the acceptance decision; accumulated patterns and logs persist across all iterations to ensure long-term knowledge retention.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> Second, our validation gating requires each accepted proposal to improve the validation score, which excludes neutral proposals that preserve immediate performance but could enable gains in subsequent iterations.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

- Immediate return: Accept/reject decision, updated active skills and best score on acceptance, restored incumbent on rejection, plus harness-written impact entry.
- Later read-back: Active skills reach later task prompts; diff, metadata, validation score and acceptance result reach later proposer/maintainer history contexts.
- Delegated visibility: Candidate is delivered to validation inference through skill injection; proposer receives subsequent history rather than ownership of the final comparison.
- Selection predicate: Strict greater-than comparison with best validation score initialized from empty-skill baseline; equality is rejection. Early stop at score 1.0.
- Invalidation or expiry: Rejection discards candidate skill changes only. Accepted skills persist until superseded. Wiki and failed-proposal evidence remain; crash-time recovery and file transactionality are uninspected.
- Activation or effect: Acceptance changes intended active instruction state; later injection can influence behavior. No frozen trace proves exercised dependence or successful improvement.
- Evidence limits: Capture supplies algorithm and reported results, not executable evaluator, restore code, raw score records or independently verifiable run artifacts. Small validation splits can introduce gating noise (Appendix B).
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Answer oracle: benchmark ground truth/domain scoring (§2), used to evaluate candidate task outcomes on validation examples; harness comparison is symbolic, not an LLM preference judge. Human computation split: dataset/setup provision is external to the internal loop; no per-proposal human admission is described. A starting caller is not evidence of per-content human approval. Guidance shaping proposals belongs to [RT-RTE-skill-proposal](#rt-rte-skill-proposal); the gate selects by score, not by an independently assessed explanation. Score selection alone establishes no content-directed theory criticism.

Self-improvement assessment: boundary is the documented inference/skill/wiki evolution system over rounds of a benchmark optimization run; objective is independently defined held-out task performance, with validation accuracy as admission proxy. A dispositional design path links task evidence to proposal determination, accepted skills to the system's instruction organization, and those instructions to later inference through [RT-BAP-skill-injection](#rt-bap-skill-injection). All are claimed, not implementation-verified. Link 4, subsequent operation causally depending on the changed instructions, is uninspected in this capture. The paper's narrative and results are attributed evidence of claimed improvement, not independently established exercised self-improvement. Success and pathway membership are distinct; validation acceptance alone establishes neither unseen-task gain nor causal attribution.

### Claims

#### RT-CLM-wiki-benefit
Label: Reported persistent-wiki benefit

Claimed operation: SRC-1 §5.1 reports that, with inference wiki access disabled, providing the proposer a persistent wiki raises average benchmark performance from 48.7% to 63.7%. The reported treatment also removes the Wiki Maintainer when proposer wiki access is removed. Therefore the contrast concerns the knowledge-maintenance/access bundle, not an independently isolated retrieval, pattern-format or individual file effect.

> When the Skill Proposer has no wiki access, we also remove the Wiki Maintainer, eliminating persistent knowledge accumulation across iterations.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

> As shown in Table 3, when wiki access for the Inference Agent is disabled, providing the Skill Proposer with access to the persistent wiki increases average benchmark performance from 48.7% to 63.7% (+15.0%), with substantial gains on LiveMath (51.3% to 72.6%) and SpreadsheetBench (49.9% to 76.6%).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Evidence layer: reported operation. No raw runs or independently inspectable intervention evidence are frozen. The capture's table omits some configuration-symbol rendering; the explicit prose establishes this particular contrast. It does not independently demonstrate a component-specific causal benefit.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-injection
Label: Active skill instruction authority

Consumer: task Inference Agent. Channel: full active skill text in the system prompt. Force: interpreted natural-language procedural guidance, capable of shaping reasoning and tool choices, not an executable guarantee or verified compliance. Horizon: later tasks/iterations within evolution and the paper's final skill evaluation; persistence beyond the supplied experimental setup is uninspected. SRC-1 §3.1–3.2.1; the injection passage is retained in [RT-RTE-task-execution](#rt-rte-task-execution). This path differs from proposal authority: the proposer submits JSON; the harness gate determines which skill text becomes active. The wiki's default downstream authority is mediated by proposal and admission, not direct task injection.

## Annotations

none
