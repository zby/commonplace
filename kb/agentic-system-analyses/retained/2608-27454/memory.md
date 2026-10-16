---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "WikiSkill's documented trace consolidation, persistent intervention history and validation-selected skill memory at the frozen arXiv v1 capture."
run-id: AAS-2026-10-15-2608-27454-65116a9d0de7-01
source-identity: "https://arxiv.org/abs/2608.27454"
reviewed-boundary: arxiv-2608.27454v1-text-2026-10-15
---

# WikiSkill memory report

## Boundary and evidence

WikiSkill retains task experience in three filesystem layers: raw trajectories, a maintained wiki, and active procedural skills. This report covers the described write and later-consumption paths, including rejected interventions, context selection and the wiki-enabled inference ablation. The [boundary](boundary.md) registers SRC-1 and fixes a complete text artifact but a partial operational loop. All mechanisms below are doctrine/design unless labelled reported operation. No implementation, persisted workspace or inspectable execution bundle is available.

Direct source inspection covered SRC-1, §3.1–3.2.4, §5.3, Appendix A.1, Appendix C and E.2–E.3. Scoped source searches also examined §2 initialization, §5.1 alternative access, §7 pruning/retrieval limits, and E.1's ALFWorld history placeholder. Source anchors below name sections in the registered capture; quoted evidence uses its absolute path. The runtime member was read in full as a provisional route inventory, not as independent verification.

| Entry point or memory operation | Source scope | Coverage and limits |
|---|---|---|
| Training rollout retention | SRC-1 §3.1, A.1 | [MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); completeness and immutability are declared, not checked. |
| Maintainer acquisition and edits | SRC-1 §3.2.2, C, E.2 | [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), annotated below; [MEM-OBJ-patterns](#mem-obj-patterns), [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-log](#mem-obj-log). No executable edit dispatcher or error policy. |
| Proposer reads and submissions | SRC-1 §3.2.3, E.3 | [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal), annotated below; `read_file` and `finish` are described tools, not inspected implementations. Trace alias routing is specified. |
| Validation, rollback and outcome retention | SRC-1 §3.2.4, A.1, E.3 | [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate), [MEM-OBJ-skill-impact](#mem-obj-skill-impact); actual restore snapshots, validation-trace persistence and rejected-content serialization are unresolved. |
| Active skill and rationale production | SRC-1 §3.1, E.3 | [MEM-OBJ-skill](#mem-obj-skill), [MEM-OBJ-purpose](#mem-obj-purpose); rationale is retained by design, but separate later delivery of PURPOSE.md is unspecified. |
| Full active-skill injection | SRC-1 §3.2.1, §7; supplied runtime | [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection); all active skills, not relevance retrieval. Activation unobserved. |
| Wiki-enabled inference alternative | SRC-1 §5.1; supplied runtime forcing account | [MEM-BAP-wiki-guidance](#mem-bap-wiki-guidance); access described, selector and delivery details unspecified. Cannot infer default direct wiki authority. |
| Context restriction and history window | SRC-1 C, E.1–E.3; supplied runtime task account | Trace sampling/capping, role-specific inputs and on-demand reads are specified. ALFWorld recent-history placeholder is described; eviction/compaction implementation and window length unknown. |
| Cleanup, withdrawal and initialization | SRC-1 §2, §7, A.1 | Empty skills/wiki and skill-only rejection rollback are specified. Automated wiki pruning is explicitly said to be lacking. Manual deletion, expiry and cross-run reload are unspecified. |
| CLI, hooks, library/service dispatch | No executable distribution in SRC-1 | Not inspectable in this capture. The named prompt tools and algorithm are the available interfaces, not a complete inventory of deployed entry points. |
| Provider state and task documents | SRC-1 §4.1, E.1; supplied runtime | [RT-CMP-model-backends](runtime.md#rt-cmp-model-backends) covers model fixity limits. Opaque provider caches are unknown; task documents and current environment feedback are inputs, not established execution-derived memory. |

## Core ideas

The wiki preserves proposed explanations independently of skill admission. The validation gate selects active procedures, not all knowledge that can influence future procedures. Rejected skill changes stop being active instructions but their diffs and outcomes remain available to the next proposer. The reported ALFWorld example explicitly attributes a later rule to that history ([MEM-CLM-rejection-history](#mem-clm-rejection-history)).

Raw traces, explanations and access summaries are different operative parts. Pattern pages are intended to retain causes, evidence and remedies. The index summarizes those pages to guide selective reading. The evolution log summarizes rounds. The impact tracker retains interventions and validation outcomes; calling it an objective audit trail does not validate the explanations in pattern pages or prove a diff caused a score change.

Read-back uses both automatic supply and model-selected pulls. The maintainer gets sampled/capped traces plus the current wiki; the proposer gets index/history/outcome summaries and requests detailed files; default task inference gets all active skills, not the wiki. These arrangements bound visibility differently. They do not establish model obedience, context-fit over indefinitely growing runs or successful learning. See the annotations on the supplied routes and [RT-CLM-wiki-benefit](runtime.md#rt-clm-wiki-benefit) for the reported bundled ablation.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw Layer

Identity: `raw/`, with execution logs under `raw/traces/`. Storage substrate: workspace filesystem. Representational form: textual/natural-language reasoning and answers, with symbolic tool-call fields and task actions where their downstream executors interpret them. Log serialization is unspecified. Lineage: training task rollouts, including tool/environment outputs, not wiki-derived summaries. Later consumers are the maintainer and proposer; their diagnostic interpretation can influence edits but does not make every trace an instruction.

SRC-1 §3.1:

> These traces capture the agent’s complete step-by-step interactions, including reasoning, tool calls, tool-call outputs, and final answers. In our setup, the Wiki Maintainer and Skill Proposer agents can access these raw traces to analyze agent behavior. To preserve the raw history, this layer is immutable.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object is declared in runtime. Closest route: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), which produces this retained material; the object is not the route. Retention is claimed across evolution rounds. Immutable storage enforcement, raw-log truncation versus prompt-only truncation, and retention of validation traces are uninspected.

#### MEM-OBJ-patterns
Label: Wiki patterns

Identity: individual Markdown pages under `wiki/patterns/`. Storage substrate: filesystem. Representational form: natural-language descriptions, causes and solutions, including exact command examples as evidence or interpreted procedural guidance. Lineage: maintainer interpretation of sampled successes/failures plus existing wiki. Later consumers: subsequent maintainer calls and proposer-selected reads. Pages can shape proposal content without directly entering default inference. Curation is requested root-cause analysis and minimal refinement, not verified truth-preserving compilation.

SRC-1 E.2:

> - What the pattern is (description)
> - Root cause analysis (WHY it happens, not just WHAT happens)
> - Exact command sequences from traces (what the agent did wrong / right)
> - Known solutions or workarounds (concrete action patterns with exact syntax)
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime; closest transformation is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Prompt requests 10–30-line, meaningful, nonduplicate pages. Physical application and content admission are distinct: the model selects text and edits; the surrounding system applies them, with no described performance veto for wiki edits. Rejection of a skill does not withdraw these pages. File/span addressability is claimed; correct causal diagnosis is not established.

#### MEM-OBJ-index
Label: Wiki index

Identity: `wiki/index.md`. Storage substrate: filesystem. Representational form: natural-language relevance summaries plus symbolic Markdown paths used to name accessible pages. Lineage: maintainer-generated complete index replacement after wiki analysis. Consumers: subsequent maintainer context and initial proposer context. This is a derived access aid with substantive summaries, not the full underlying pattern evidence.

SRC-1 E.2:

> The description must be specific enough that an agent can judge relevance without reading the full page. Include the problem, root cause, AND solution.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime; closest routes are [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) and [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal). It is not contained in either route alone. Maintainer authoring governs content; inclusion of all existing entries is a prompt requirement, not checked preservation. Index text can bias which evidence gets read. E.2 mentions inference agents as readers, but §3.2 restricts default inference from wiki; that wording does not prove default inference delivery.

#### MEM-OBJ-log
Label: Wiki evolution log

Identity: maintainer evolution log, called `logs.md` in §3.1–3.2.2 and `wiki/log.md` in E.2. Storage substrate: filesystem; exact resolved filename unknown. Representational form: natural-language chronological findings/actions, with iteration/score/decision metadata described in its prompt label. Lineage: maintainer summary of each round, distinct from raw traces and harness-written impact entries. Later maintainer input explicitly includes the log; §3.1 names maintainer/proposer historical awareness, but the proposer default initial context does not explicitly include this log.

SRC-1 E.2:

> - "append_log": "brief summary of this iteration’s findings and actions"
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime. Closest route [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) already identifies the naming ambiguity; this record retains that uncertainty rather than inventing two stores. Appending is mandatory in the prompt even without new patterns. Wiki-level persistence is claimed; complete preservation of reasoning in these brief summaries is not.

#### MEM-OBJ-skill-impact
Label: Skill impact tracker

Identity: `wiki/skill-impact.md`. Storage substrate: filesystem. Representational form: natural-language proposal/diff content for model interpretation, plus symbolic scores, target identity and Accepted/Rejected metadata recording harness decisions. Lineage: automatic post-validation append from proposal and evaluator outcome, not maintainer-authored causal interpretation. Later consumers: proposer initial history and later reads; §3.1 also describes maintainer awareness, while E.2's explicit input list omits the tracker.

SRC-1 E.3:

> 2. Read ‘wiki/skill-impact.md‘ to see what was tried before (includes full content of rejected proposals -- DO NOT repeat rejected approaches)
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime; closest route [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate). §3.2.4 specifies metadata, unified diff, score and outcome. Full rejected-content retention is stronger wording in E.3; exact serialization and reconstructability of full rejected files from patches are uninspected. Append admission follows the harness outcome regardless of acceptance, with no per-entry human approval described. Its later advisory authority can discourage repeating an intervention, not certify that intervention can never work.

#### MEM-OBJ-skill
Label: SKILL.md

Identity: procedural file in each directory under `skills/`. Storage substrate: filesystem. Representational form: natural-language applicability and instructions; YAML names/descriptions provide structured metadata. No executable skill scripts are established for the studied workspace. Lineage: proposer synthesis from wiki explanations, selected traces, training outcome oracle and existing skills. Consumers: validation task inference provisionally and later task inference when admitted. Authority is the interpreted system-prompt channel in [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection).

SRC-1 E.3:

> - "skill_md": full SKILL.md content with YAML frontmatter + When to Apply + When NOT to Apply + Instructions
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime. Closest routes [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal) and [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) span production and admission; this file is distinct from both. Strict score improvement admits the changed active set; ties/lower scores revert to the incumbent. File/span edits are addressable in the design. Exact file snapshots and restore mechanics are unknown. The score gate selects behavior instructions without separately validating their explanations.

#### MEM-OBJ-purpose
Label: PURPOSE.md

Identity: companion rationale file in each skill directory. Storage substrate: filesystem. Representational form: natural-language origin and evolution history with links/mappings to motivating patterns. Lineage: proposer supplies it at skill creation. Later consumer delivery is unresolved: §3.1 says it maps skills to patterns; §3.2.1 says full active skill content is injected, without separately enumerating this file. Retention of reasons therefore does not establish that task inference reads them.

SRC-1 E.3:

> - "purpose_md": full PURPOSE.md content with Origin + Patterns Addressed + Evolution History
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

No counterpart object in runtime; closest [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal). Its separate consumer uncertainty warrants separation from SKILL.md. The patch proposal schema does not specify which companion file receives edits or require synchronized rationale updates. Skill-set rollback is described globally; companion-file coverage is uninspected. No authority is inferred merely from the filename.

### Routes

none declared in this member

### Claims

#### MEM-CLM-rejection-history
Label: Rejection history reuse

Claimed operation: SRC-1 §5.3 reports retention and later use of a rejected skill intervention. This is reported operation, not an independently inspectable trajectory. Closest supplied [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) describes the admission route and mentions this case; this claim isolates its attributed later history dependence rather than duplicating the route.

> At Iteration 0, the Wiki Maintainer identifies a basic looping behavior (take-examine-move-loop.md), while the Skill Proposer proposes goal-directed-action, which fails to improve performance on the validation set and is rejected. Crucially, skill-impact.md preserves the proposal diff and rejection outcome, allowing subsequent skill updates to account for this failed attempt.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

The next paragraph reports accepted `break-repetition-loop` and later refinement with another wiki pattern. The simplified narrative supports the attributed mechanism; it does not supply all contexts, criticism steps or a causal intervention isolating history reuse. Outcome rejection is not by itself articulated blame on a particular explanatory claim.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-guidance
Label: Wiki guidance authority

Consumers: maintainer and proposer by default; task inference in the explicitly wiki-enabled ablation. Channel: maintainer current-wiki prompt, proposer initial index/impact history plus selected file-read results, and unspecified wiki-access channel for alternative inference. Force: interpreted explanatory and procedural advice; proposer can convert it into proposed instructions, while the harness gate controls active skill admission. Horizon: subsequent calls and evolution rounds; cross-run workspace restoration is uninspected. Evidence: SRC-1 §3.2.2–3.2.3, E.2–E.3 and §5.1, with read-selection passages in [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal).

> Our default WikiSkill configuration gives wiki access to the Skill Proposer but not the Inference Agent.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

Closest supplied [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection) has a distinct consumer-channel referent: accepted active instructions in task prompts. Wiki advice can remain influential after a failed skill proposal; it does not have that default direct task instruction path. Alternative inference access is claimed, but its selector, budget, implementation and actual activation are uninspected.

## Annotations

#### On [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Retained output is raw training interaction material in [MEM-OBJ-raw](#mem-obj-raw). Full skill injection automatically supplies all active retained procedures at each task invocation; the selection input is active-set membership, not task relevance. Rejected candidates nevertheless reach validation inference provisionally before rollback, so admission is not a prerequisite for every task-model exposure. No later default inference read of old raw traces is established. Task-specific frames keep wiki work out of default task context; the return is prediction/artifact plus retained trajectory, not a transferred maintainer context. Actual separate context lifetime and pop/discard mechanics are unspecified. E.1's ALFWorld `{history_length}` and `{action_history}` specify recent-history input, not a known compaction or reload algorithm. Static prompts and current task documents are working context, not automatically retained learning.

#### On [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Memory transformation: sampled raw trajectories → requested causal diagnoses and command evidence → editable patterns, replacement index and appended iteration summary → later maintainer/proposer consumption. Prompt-only trace capping bounds each delivered log, not established deletion of stored raw material. The automatic selector is the harness's success/failure stratification: up to five failures and three successes, each capped at 15,000 characters (SRC-1 C; quote retained in the supplied record). Which characters survive the cap and tie-breaking among eligible traces are unspecified. The full current wiki is supplied according to §3.2.2; no wiki token budget is given. Model authorship and edit choice do not establish a human admission decision. Initial filesystem setup control is unknown even though the declared initial content is empty. New pages/full index and incremental page patches are distinct physical operations under the same requested wiki-content authority.

#### On [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal)

The first context is a deliberately reduced view: index, impact history and all-task outcomes including expected answers, rather than the maintainer's full wiki plus sampled logs. Index and failed-outcome details target the model's further selection of pages/traces; the `traces/<task_id>` name is an address after selection, not a separate relevance algorithm. Read requests pull selected file content; initial supply is automatic. At least four trace reads is a prompt rule, not a maximum or verified enforcement. No turn/token/file-read limit or host compaction policy is specified. Model interpretation of reasons can inform procedures; PURPOSE.md retains stated origin/history, but later separate rationale delivery and patch synchronization remain unknown. `no_action` is a prompt-supported alternative with unresolved outer-loop handling. Exact-target patches and create-as-large-rewrite are exposed adoption surfaces, not proven safe overwrite semantics.

#### On [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)

Active procedures and intervention history have different withdrawal rules. Restoration removes candidate skill changes from active state; it does not remove patterns, log summaries or failed proposal evidence. The harness appends [MEM-OBJ-skill-impact](#mem-obj-skill-impact) irrespective of acceptance, supplying later proposer history and preventing a simplistic inference that rejected material has no future authority. The scalar incumbent best score is symbolic admission state across rounds, not a model-consumed explanation; durable checkpoint storage is unspecified. Validation produces traces, but §3.1's retained raw layer specifically describes training examples: no later read route for persisted validation trajectories is established. Score/outcome retention is established as design, not full validation-context retention. The report's source narrative of rejection-history reuse is [MEM-CLM-rejection-history](#mem-clm-rejection-history).

## Write side

The declared initial wiki and skill set are empty (SRC-1 §2, A.1). Who creates workspace scaffolding and whether a human can seed/replace content are unspecified; a caller starting the experiment does not establish per-content approval. Subsequent content ownership is clearer: task agents generate trajectories, the surrounding harness retains them, a maintainer model chooses wiki edits, a proposer model authors a single-skill candidate, and the evaluator/harness admits or rejects active skill changes. These are bounded benchmark-evolution modes. Ground-truth training outcomes guide diagnosis; validation ground truth/domain scoring supplies the gate, not a model preference judge.

Acquisition and curation separate raw experience from claims. Tool outputs and task-agent reasoning enter raw traces without becoming warranted diagnoses. Maintainer sampling preferentially delivers failures while retaining some successes. Requested root causes, concrete commands and refined solutions become patterns; index replacement and log appends derive smaller views. Requested no-duplicate and concision rules do not prove semantic deduplication or accuracy. Guidance and theory assessments remain in the supplied maintenance/proposal records: localized text and specified later interpretation are claimed, content-directed criticism and exercised criticism-specific iteration remain uninspected. This report adds no stronger theory-builder, reflective, autonomous or learning attribution.

Proposer synthesis produces behavior-shaping instructions with a separate rationale file. Reasons also remain in pattern pages and are explicitly available for proposer reads. That establishes a designed reasons-to-procedure path, not certainty that each accepted rule retains all reasons or that inference receives PURPOSE.md. Rejection preserves the intermediate wiki and records the failed intervention. Acceptance changes active skills. Transactional patch application, malformed-response recovery and companion-file rollback are unknown. See [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) for veto and score rules.

Cleanup is limited in the inspected design. Maintainers can refine or replace spans; proposers can patch or request substantial replacement. Neither exposed proposal format lists skill deletion, and their omission is not proof that an unavailable implementation cannot delete. SRC-1 §7 explicitly says automated wiki pruning is lacking:

> Third, the Wiki Layer continuously accumulates pattern pages, evolution logs, and proposal diffs across iterations, but WikiSkill currently lacks an automated mechanism to prune the wiki.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/wikiskill-65116a9d0de7/kb/agentic-system-analyses/state/AAS-2026-10-15-2608-27454-65116a9d0de7-01/sources/arxiv-2608.27454v1-text.txt`

This is a declared design limitation, not an implementation-wide evidenced absence. No expiry, manual withdrawal or cross-run checkpoint/reload policy is established.

## Read-back

| Later consumer | Selection and delivered material | Persistence and authority |
|---|---|---|
| Maintainer next round | Harness supplies current wiki and stratified/capped training traces | Patterns/index/log persist across rounds; requested interpretation can revise the wiki. Tracker inclusion has prose/prompt ambiguity. |
| Proposer next invocation | Initial index, intervention tracker and outcome summary; model chooses pattern/trace reads | Failed and successful interventions remain available. Model-requested pulls supplement automatic supply; both may shape candidates, not admit them. |
| Validation inference | All candidate active skills supplied provisionally | Candidate can affect scored tasks even if later rejected; no verified activation. |
| Later default training/test inference | All accepted active skill content supplied in system prompt | Procedure authority is interpreted guidance; no evaluated relevance retrieval or guarantee of compliance. Companion rationale inclusion is unspecified. |
| Wiki-enabled training inference | Experimental wiki access described in §5.1 | Alternative authority only; read-back selection and delivery mechanics unresolved. |

The wiki and raw filesystem are reachable through described file reads rather than through provider memory. Separate role contexts resemble selected-input frames, but the source does not specify disposal implementation. Retained files escape the role invocation and can be read later; a model's window contains delivered text by value, not traversable filesystem references. An index/path enables a future tool read, not automatic access to all referenced evidence. There is no described host summarization checkpoint replacing a role's whole context; sampling, capped trace delivery and the small proposer initial view are the source-supported context controls. Unspecified provider state cannot be classified as absent memory.

## Integration issues

1. **No supplied fact requires correction; several existing limits remain.** [MEM-OBJ-log](#mem-obj-log) preserves `logs.md` versus `wiki/log.md`, already noted in [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Filename resolution prevents an exact filesystem claim, not the documented log-retention account.
2. **Impact-history delivery ambiguity.** §3.1 describes maintainer and proposer awareness of acceptance history; E.2's explicit current-wiki inputs list index/log/patterns, omitting the tracker. [MEM-OBJ-skill-impact](#mem-obj-skill-impact) and the maintenance annotation preserve that distinction. Do not infer identical history completeness for both roles.
3. **Diff versus full rejected content.** §3.2.4 describes unified diffs; E.3 calls them full rejected proposals. [MEM-OBJ-skill-impact](#mem-obj-skill-impact) preserves both source statements. Reconciliation must not silently equate patch history with reconstructable whole files. Actual serialization would resolve this, but is outside the capture.
4. **Rationale consumer and patch target.** [MEM-OBJ-purpose](#mem-obj-purpose) separates retained reasons from operative instructions in [MEM-OBJ-skill](#mem-obj-skill). No separately specified later PURPOSE.md delivery, synchronized edit path or companion-file restore mechanism is available. This prevents a claim that every downstream task sees a maintained rationale.
5. **Validation traces and checkpoints.** [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) produces validation trajectories and restores incumbent skills; [MEM-OBJ-raw](#mem-obj-raw) is explicitly training-derived. Validation raw retention, durable incumbent snapshots, crash recovery and `no_action` handling remain unknown. Score/diff history should not be expanded into a full replay archive.
6. **Potential overlap, not duplicate identity.** [MEM-CLM-rejection-history](#mem-clm-rejection-history) elaborates the example already discussed in [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate), but is an attributed claim rather than that route. [MEM-BAP-wiki-guidance](#mem-bap-wiki-guidance) contrasts with [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection): wiki adviser channels versus active task instructions. The seven new objects have no supplied object counterparts; their closest routes are cited in each declaration.
7. **Scope of alternate wiki authority and context control.** [MEM-BAP-wiki-guidance](#mem-bap-wiki-guidance) retains the §5.1 wiki-enabled mode without inventing default inference access or a retrieval budget. Trace-cap preservation policy, ALFWorld window length, role context disposal and provider caches remain unresolved; these prevent implementation/isolation and long-run context-fit guarantees.

## Limitations and checks

This is a source-grounded description of a documented memory mechanism, not evidence of executed storage, correct diagnoses, successful restore, instruction compliance or causal benefit. The paper's reported history example and bundled ablation do not establish per-file causal effects. Persistence is specified across evolution rounds with a final skills/wiki return; cross-session restoration is not established. No target execution or external source acquisition was performed.

The supplied invocation, job, member and input types, worker rules, collection contract and records contract were read completely, including bounded continuation reads. Runtime identity and capture label were checked against the boundary. Source inspection stayed within the registered text capture; source-byte identity is rechecked by SHA-256. Deterministic validation: passed using the invocation's `commonplace-run validate-output` command. This check establishes structure and quotation occurrence, not semantic acceptance.
