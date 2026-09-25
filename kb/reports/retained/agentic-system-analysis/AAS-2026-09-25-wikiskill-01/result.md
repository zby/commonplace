---
type: types/agentic-system-analysis-result.md
description: "Complete documentary analysis of WikiSkill's described skill-evolution loop and retained knowledge."
run-id: AAS-2026-09-25-wikiskill-01
system: WikiSkill
run-date: "2026-09-25"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0"
analysis-cutoff: "2026-09-25"
evidence-tier: doc-grounded
memory-comparison:
  scope: "Paper-described retained raw training traces, wiki patterns/catalog/evolution log/impact history, SKILL.md and PURPOSE.md, and their evolution, validation, later inference and cross-model reuse routes. Include the inference-wiki-access ablation as an alternative with unspecified delivery. Include proposer outcome summaries as a delivery derivative, without assuming separate durable storage. Exclude static benchmark prompts, underlying tool/model implementations and ordinary within-task action-history assembly."
  axes:
    storage_substrate:
      assessment: known
      basis: claimed
      values: [files]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9]
      note: "All disclosed durable memory is in raw/, wiki/ and skills/ files; scores and decisions persist in the impact file. The supplied outcome summary has no separately specified durable store. No implementation inventory was inspected."
    representational_form:
      assessment: known
      basis: claimed
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8]
      note: "The described file contents combine prose, exact tool commands, executable command examples, metadata, proposal diffs and structured outcomes. This classifies the disclosed textual parts; the general definition of skills with scripts/resources does not establish extra evolved payloads beyond the two-file WikiSkill skill layout."
    lineage:
      assessment: known
      basis: claimed
      values: [trace-extracted, other-compiled]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, RTE-2, RTE-3, RTE-6]
      note: "Traces supply extracted diagnoses and procedures; catalog, rationale maps and impact history compile retained patterns, proposals and scores. Cross-model consumption reuses the evolved artifact and does not itself establish a new imported write lineage. Static human-authored prompts are outside this memory boundary."
    behavioral_authority:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-2, OBJ-3, OBJ-5, OBJ-6, OBJ-7, OBJ-8, RTE-1, RTE-3, RTE-5, RTE-7]
      note: "Default routes support knowledge, routing, instruction and validation roles. PURPOSE.md has no explicit later read route; the inference-wiki-access ablation does not specify delivery or prompt authority. Therefore a complete authority set across the commissioned alternatives is not determined."
    write_agency:
      assessment: known
      basis: claimed
      values: [automatic]
      records: [RTE-1, RTE-2, RTE-3, RTE-5, RTE-6]
      note: "Inference produces traces, models produce wiki/skill changes, and the harness applies changes and appends outcomes. The described loop supplies no manual memory-authoring step; filesystem editability alone does not add one."
    curation_operations:
      assessment: known
      basis: claimed
      values: [consolidate, evolve, synthesize]
      records: [RTE-2, RTE-3, OBJ-3, OBJ-4, ABS-1]
      note: "Brief summaries consolidate retained observations; patches evolve patterns and skills; diagnoses and proposed remedies synthesize claims. Duplicate prevention is not demonstrated merging; admission of a newly synthesized skill is not a separate promotion operation. Rollback rejects candidates. No pruning/decay route is described."
    read_back_direction:
      assessment: known
      basis: claimed
      values: [pull, push]
      records: [RTE-1, RTE-2, RTE-3, RTE-7]
      note: "The named proposer requests pages/traces through read_file; harness context supply delivers skills, wiki and initial proposer material without those requests. The ablation's unspecified delivery does not change the already established two-value union."
    read_back_signal:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-1, RTE-2, RTE-3, RTE-7]
      note: "Default automatic supply is coarse: current full skill set, full wiki, pass/fail-stratified traces, and initial catalog/history/summary. Requested path selection is pull, not identifier-based push. The inference-wiki-access ablation has no described selector, preventing a complete push-signal set."
    trace_learning:
      assessment: known
      basis: claimed
      values: ["yes"]
      records: [RTE-2, RTE-3, RTE-5, RTE-6]
      note: "Automatic trace-fed production retains behavior-shaping patterns, summaries, histories and admitted skills for later maintainer, proposer or inference consumption; rejected proposals remain useful context. This is described operation, not inspected wiring."
    trace_source:
      assessment: known
      basis: claimed
      values: [trajectories, tool-traces]
      records: [OBJ-1, OBJ-2, RTE-2, RTE-3]
      note: "Complete task trajectories supply reasoning, actions and answers; tool-using variants additionally supply exact calls and tool outputs. LiveMath's no-tool branch still qualifies through its trajectory."
    learning_scope:
      assessment: known
      basis: claimed
      values: [cross-task]
      records: [RTE-2, RTE-3, RTE-4, RTE-1]
      note: "Knowledge is extracted across training instances and iterations and skills are reused on validation and unseen test instances, including other inference models. Ordinary within-task action history is not a durable learned artifact in this scoped evolution workflow."
    learning_timing:
      assessment: known
      basis: claimed
      values: [staged]
      records: [RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, ABS-1]
      note: "Each trace-fed write occurs in the maintenance/proposal/outcome stages after rollouts and before later consumption. Final test-time reuse adds no new learning timing. Within-rollout online adaptation is identified as future work."
    distilled_form:
      assessment: known
      basis: claimed
      values: [natural-language, symbolic]
      records: [OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, RTE-2, RTE-3, RTE-6]
      note: "The qualifying routes retain prose diagnoses, summaries and procedures, including exact command syntax and compiled proposal diffs/outcome records. They do not describe model-weight learning."
    faithfulness_tested:
      assessment: known
      basis: claimed
      values: ["no"]
      records: [CLM-1, CLM-2, ABS-2]
      note: "Within this retained paper, task-performance ablations, transfer scores and simplified cases do not test execution dependence on particular recalled content. No qualifying retained recall-dependence execution evidence is supplied; this is a bounded no, not a claim about unprovided experiments."
---

# WikiSkill agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/wikiskill.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/memory-report.md`

**Memory analysis report SHA-256:** 8d9a31663c9138fcd91c82972efe0deba205a9f3d9e164816f46e7b2b75fa19b

Source-only documentary run; these are intended output paths, not declarations of publication completion.

## Boundary and evidence

Evidence basis: the WikiSkill paper captured on 2026-09-17, frozen by the digest above and analysed on 2026-09-25. This analysis characterizes the paper's complete described improvement workflow: task inference, trace compilation, wiki maintenance, skill proposal, validation, skill rollback, persistent history and subsequent inference. Target class is a builder or improvement plane; boundary kind is complete artifact, partial loop. The paper also describes inference but does not provide implementation or executable runs here.

Excluded model/provider internals prevent claims of exact parameter or endpoint identity. Excluded tool, benchmark and harness implementations prevent guarantees about sandboxing, scorer validity, enforcement, recovery or runtime wiring. External dependencies are model calls, domain tools, task data and scorers. No prior reviews, ingests, live pages or transfer findings supplied evidence. Capture frontmatter identifies the capture only. Reported experiments remain attributed claims, not independently observed or causal evidence.

## Source register

| Source ID | Kind and identity/location | Revision or capture | Evidence layer | Inspected scope / anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|
| SRC-1 | Paper capture, `https://arxiv.org/abs/2608.27454`; local `/home/zby/llm/commonplace/kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` | SHA-256 c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0; 90009 bytes | Doctrine/design | §§2–3, Appendix A algorithm, Appendix C sampling, Appendix E prompts, Limitations | No executable source; described paths cannot become wired findings |
| SRC-2 | Same frozen paper, `https://arxiv.org/abs/2608.27454` | Same capture and digest as SRC-1 | Reported operation | §§4–5, Tables 1–4, Figure 3, Appendix C statistics | No raw experimental artifacts; prevents independent observation, causal attribution or faithful-recall confirmation |

## Shared records

### Components

CMP-1 — Model instances for inference, wiki maintenance and proposal. Distributed-parametric; provider/service or local inference storage is outside the capture. SRC-1 §4.1 names Gemini-3.5-Flash, Qwen-3.5-4B/9B-Instruct, Qwen-3.6-27B and Gemma-4-31B-It, with open models deployed using vLLM. Parameter-change conclusion status: claimed (skill evolution is described without model-parameter updates). Exact-version fixation conclusion status: uninspected; model family names do not establish immutable endpoints, weights or optimizer-role assignment. Provider internals and hidden model reasoning remain uninspected.

> At its core, a skill packages instructions, scripts, and other resources into a reusable
> filesystem-based module (i.e., an organized directory)
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

### Operative objects

All following object existence/form/storage findings have conclusion status: claimed. Files are the described workspace representation, not inspected files. Source anchors use SRC-1 unless noted.

| ID | Source-native object and form | Producer → consumer; lineage, retention and limit |
|---|---|---|
| OBJ-1 | `raw/` execution traces; natural-language reasoning/output plus symbolic commands/tool interactions (§3.1) | Inference → maintainer and proposer; write-once training trajectories; physical log encoding uninspected |
| OBJ-2 | `wiki/patterns/` Markdown pages; natural-language patterns/explanations and symbolic command workarounds (§3.1, §3.2.2) | Maintainer → maintainer/proposer; trace-derived and continually patched; retention is not truth acceptance |
| OBJ-3 | `wiki/index.md` catalog; natural-language descriptions and symbolic path links (§3.2.2, Appendix E.2) | Maintainer → proposer and later maintainer; rebuilt with page updates; links route readers, not formal entailments |
| OBJ-4 | Evolution log, called `logs.md` in main text and `log.md` in Appendix E.2; natural-language history | Maintainer → later maintainer/proposer (§3.1, §3.2.2); filename disagreement unresolved; historical retention described |
| OBJ-5 | `wiki/skill-impact.md`; proposal metadata, diff, score and acceptance history (§3.2.4) | Harness → proposer and later wiki users; programmatic outcome records survive rejected proposals |
| OBJ-6 | `skills/*/SKILL.md`; procedural instructions/applicability conditions plus command examples and YAML metadata (§3.1, §3.2.1) | Proposer and gate → inference; current accepted skill set persists; candidate changes reversible |
| OBJ-7 | `skills/*/PURPOSE.md`; motivating pattern links and rationale/history (§3.1, Appendix E.3) | Proposer → unspecified later consumer; explicit creation and rationale retention, but subsequent PURPOSE reading/injection and patch maintenance uninspected |
| OBJ-8 | Validation score and accept/reject outcome; symbolic metric (§2, §3.2.4) | Benchmark scoring → strict gate and impact history; retained result licenses score-relative selection only |

> Each skill directory in WikiSkill contains
> two files: SKILL.md, which contains the full content of the skill; and PURPOSE.md, which maps
> the skill back to the motivating Wiki patterns that inspired its creation or modification.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

OBJ-9 — Concise current training-outcome summary: pass/fail, predictions and ground-truth answers supplied initially to proposer. Derived delivery view, not established as an independently retained artifact; conclusion status claimed for delivery, uninspected for separate persistence. SRC-1 §3.2.3; RTE-3.

> These traces capture the agent’s complete step-by-step interactions,
> including reasoning, tool calls, tool-call outputs, and final answers.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

> - Root cause analysis (WHY it happens, not just WHAT happens)
> - Exact command sequences from traces (what the agent did wrong / right)
> - Known solutions or workarounds (concrete action patterns with exact syntax)
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

### Routes

The following six canonical routes preserve complete operational families. All route operation conclusion statuses: claimed; implementation conclusion status: uninspected. Owners and mechanisms are described. No transaction, permission or isolation guarantee is established. Detailed functional distinctions inside each route remain separate in the epistemic overlay.

RTE-1 — Inference: a supplied training, validation or test task triggers a model/tool rollout with the current OBJ-6. Harness supplies task context and all active skills; the inference model chooses actions, domain tools execute, and a final answer or task artifact returns to scoring. Training produces OBJ-1 for later maintainer/proposer use. Default training denies wiki access; the paper does not expose an enforcement point or shell/provider bypass analysis. Immediate return: answer/trajectory; later read-back: OBJ-6 was changed by prior iterations; delegated visibility: maintainer/proposer receive traces. Selection is all active skills, with supersession on accepted skill changes. Activation is reported at bundle level through SRC-2 results, not independently observed. Recovery from tool/model failures is uninspected. SRC-1 §2, §3.2.1; BAP-1.

> In WikiSkill, the full content of active skills 𝑆𝑘 −1 is injected directly into the Inference Agent’s system
> prompt.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

RTE-2 — Wiki maintenance: after training rollouts, the harness samples up to five failures and three successes and caps each trace at 15000 characters (SRC-1 Appendix C). A model receives sampled OBJ-1 plus existing wiki and emits new/patch OBJ-2, replacement OBJ-3 and appended OBJ-4. The model proposes and decides substantive wiki changes; patch application is harness-owned. Guidance asks for root causes, success/failure contrasts, concrete workarounds and no duplicate patterns. Wiki changes survive skill rejection. Semantic veto, patch-failure recovery and pruning implementation are uninspected. Immediate return: patches/catalog/log; later consumers: maintainer/proposer. Full-context automatic supply is described; no expiry. Separate content-directed assessment is prescribed, while its actual reasoning and correctness are uninspected. BAP-2.

> 4. Check whether the agent followed any active skills, and whether the skill guidance
> was helpful or not
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

> The Wiki Maintainer agent receives the full wiki context 𝑊𝑘 −1 alongside sampled traces Tsample,𝑘 . It
> performs root cause analysis on the failing tasks, and extracts successful strategies from the passing
> tasks.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

> Whenever patterns are modified, the Wiki Maintainer revises the index.md catalog to reflect
> the current state and appends a summary of the iteration’s findings to the evolution log logs.md.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

RTE-3 — Skill proposal: the model initially receives OBJ-3, OBJ-5 and a training-outcome summary including predictions and ground-truth answers, then requests selected pages or traces through `read_file`. It must inspect at least four traces under Appendix E.3. The ReAct process terminates with `finish`: create a skill and PURPOSE, patch an existing skill, or `no_action`. The model proposes; RTE-5 decides admission. Guidance is the retained failure explanations and strategies in OBJ-2, rejected-edit evidence in OBJ-5 and current procedures in OBJ-6. Parts can be changed by exact-text patch, exposing local conditions and instructions; completeness of assumptions is uninspected. Immediate return is one atomic skill proposal; later effect only after gate acceptance. Requested file returns are pull, initial context is push. Tool alias `traces/<task_id>` maps to raw traces (Appendix E.3). No proposal grants runtime deployment authority. BAP-3.

> it is initially provided with the wiki index 𝐼 (𝑊𝑘′ ), the historical skill impact
> tracker (skill-impact.md), and a concise summary of all training task outcomes (pass/fail status,
> predictions and ground-truth answers).
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

RTE-4 — Validation check: harness applies a candidate proposal temporarily, runs RTE-1 over the disjoint validation split, and obtains OBJ-8 through domain-specific scoring against supplied expected answers/outcomes (SRC-1 §2, §3.2.4). Dataset creators supply the reference; scorer implementation/validity is uninspected. This check produces evidence, not admission. Immediate return is score/validation trajectories; the score enters RTE-5 and RTE-6. No subsequent validation-trace selection route is established. External effects belong to domain tools; isolation/recovery uninspected. BAP-4.

RTE-5 — Admission/rollback: the harness accepts candidate OBJ-6 only if validation score strictly exceeds the best previous score, otherwise restores the last accepted skill set. Initial threshold comes from empty-skill validation; maximum score ends evolution early. OBJ-2, OBJ-3, OBJ-4 and OBJ-5 are not rolled back. Model proposes via RTE-3; numeric gate decides and can veto; no human in-loop decision is specified. Retained accepted skills shape later task rollouts and proposals. Guarantee owner: harness; point: described score comparison; strength: protocol; conclusion status: claimed. It covers the described loop, not arbitrary external edits. Required contract: reliable comparable scorer/task splits. Recovery beyond skill restoration is uninspected. BAP-5.

> If rejected, the system discards the candidate skill modifications and reverts
> the skill set to the most recent successful configuration 𝑆𝑘 −1 . Notably, the wiki 𝑊𝑘 is never rolled
> back regardless of the acceptance decision;
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

RTE-6 — Outcome retention: after either RTE-5 decision, the harness appends proposal metadata, target skill, diff, score and decision to OBJ-5, so a later RTE-3 can avoid repeating failed interventions. The write is automatic and does not certify pattern explanations. Immediate return: updated wiki state; later read-back: full impact history in initial proposer context. No human curator, expiry, independent semantic check or crash-recovery protocol established. BAP-6. SRC-1 §3.2.4.

> recording the proposal metadata, target skill name, unified diff of the
> modification, validation score R (Tval,𝑘 ), and final acceptance outcome 𝑎𝑘 ∈ {Accepted, Rejected}.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

RTE-7 — Wiki-access ablation: SRC-2 §5.1 permits inference wiki access during training. Operation conclusion status claimed; implementation conclusion status uninspected. The inference agent is consumer, but automatic versus requested delivery, selected files, context placement, selector, budget, lifetime and authority are uninspected. Immediate return remains task rollout; later retained products follow the otherwise described evolution. No distinct write admission or recovery mechanism established. The branch stays separate from default RTE-1 and prevents a complete push-signal/authority profile.

### Claims

CLM-1 — Persistent wiki supports skill evolution. Conclusion status: claimed; SRC-2 §5.1 reports 48.7% to 63.7% average accuracy in the Gemini comparison with inference wiki access disabled. Removing proposer wiki access also removes the maintainer, so the reported contrast identifies a package, not the causal contribution of storage alone, a pattern type or a specific criticism.

> When the Skill Proposer has no Wiki access, we also remove the
> Wiki Maintainer, eliminating persistent knowledge accumulation across iterations.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

CLM-2 — Evolved skills transfer across models and can outperform self-evolved skills. Conclusion status: claimed; SRC-2 §4.2.2/Table 2 report cross-model skill injection. The paper also reports regressions in some model/task settings (§4.2.1); transfer is conditional, and retrieval was excluded.

CLM-3 — Prior rejection and recurring failure evidence inform later concrete rules. Conclusion status: claimed; SRC-2 §5.3/Figure 3 describes rejected `goal-directed-action`, accepted `break-repetition-loop`, then a later refinement. The displayed contents are simplified, not original run artifacts. This is evidence of the authors' process account, not independent observed criticism or causal credit for any rule.

> File contents are simplified for clarity.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

### Evidenced absences

ABS-1 — Conclusion status absent, bounded to the described paper method: no automated wiki pruning or within-rollout online skill adaptation. Searched SRC-1 method, Appendix A/E and Limitations in the frozen capture for pruning, online adaptation and maintenance routes; explicit limitation says pruning is lacking and online adaptation is future work. This is an absence in described workflow coverage, not inspected code.

> WikiSkill currently lacks an automated mechanism to prune the wiki.
> --- `kb/sources/.snapshots/wikiskill-persistent-knowledge-for-skill-evolution.md` @ `sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0`

ABS-2 — Conclusion status absent, bounded to retained execution evidence of recall dependence in this capture. Inspected SRC-2 §§4–5, Tables 1–5, Appendix B–C and case study; performance/ablation/transfer/statistical reports and simplified cases do not test dependence on particular recalled content. The search boundary is these experimental sections, using recall, faithful, ablation, transfer, case and access queries plus full relevant passages. This prevents faithfulness-tested yes, not claims about unavailable experiments.

### Behavioral-authority paths

| ID | Consumer | Channel | Force and horizon | Evidence |
|---|---|---|---|---|
| BAP-1 | Inference model | System-prompt OBJ-6 | Instruction for current rollout; claimed activation only | SRC-1 §3.2.1 |
| BAP-2 | Maintainer | Wiki plus sampled OBJ-1 | Advisory/evidential context shaping current wiki edits | SRC-1 §3.2.2 |
| BAP-3 | Proposer | Initial catalog/history, requested pages/traces | Advisory diagnosis and instruction shaping current proposal | SRC-1 §3.2.3 |
| BAP-4 | Gate | Numeric OBJ-8 | Validation evidence for current candidate | SRC-1 §3.2.4 |
| BAP-5 | Harness/current skill set | Strict score decision | Permits/rejects skill changes for subsequent rollouts | SRC-1 §3.2.4 |
| BAP-6 | Later proposer | Retained impact history | Advisory rejection/acceptance evidence across iterations | SRC-1 §3.2.4 |

## Runtime account

The benchmark operator supplies splits, tools, model configuration, scoring and iteration budget. Empty wiki and skill sets seed the loop. RTE-1 generates training experience; RTE-2 updates knowledge; RTE-3 makes one proposal; RTE-4 scores the candidate; RTE-5 selects/restores skills; RTE-6 retains the intervention history. The next iteration uses both retained wiki and active skills. Terminal output is final skills and wiki, followed by reported held-out testing. Scheduling is harness-owned; diagnosis and proposal policies are model-mediated natural language, while scoring and acceptance are described symbolic operations. No open-ended service or within-rollout skill adaptation is evaluated.

Material alternate routes: Appendix E.3 permits `no_action`; source does not settle its scoring/control path. The wiki-access ablation allows inference to read wiki, with worse average results in the tested condition; this branch is included with unknown delivery in the memory profile. Cross-model testing replaces the skill consumer while keeping the evolved skills. External shell/tools, provider calls and any direct workspace edits are uninspected alternate enforcement paths, preventing a deployed isolation guarantee.

Two documentary forcing cases suffice. First, equal or lower validation score invokes skill-only rollback but preserves the new wiki and rejection history, so a rejected procedure can still teach the proposer. Second, baseline validation already at 1.0 ends evolution before a skill is created; SRC-2 §4.2 gives Gemini/ALFWorld as a reported instance. Neither is an executed probe. No dynamic check planned: implementation, environment, benchmark assets and runtime authority are outside the supplied evidence, and documentary tracing answers this analysis boundary.

Theory-path findings: formulation conclusion status claimed (OBJ-2 explains recurring failures and proposes solutions); operative-use conclusion status claimed (RTE-3 explicitly reads those explanations to propose procedures); content-directed criticism conclusion status claimed at instruction/process-account level (RTE-2 compares behavior and guidance; CLM-3 describes changed rules); resulting revision/reliance conclusion status claimed; improved capacity attributable specifically to holding and criticizing theory conclusion status uninspected. SRC-2 supports reported bundle-level skill gains, not that more specific attribution. Addressability is claimed for named pages and local patches, separate from correctness. Retained rationales and outcome history have later described consumers, while hidden reasoning remains uninspected.

Reflection conclusion status claimed: task behavior and prior interventions update OBJ-2, OBJ-4 and OBJ-5; those representations guide changes to OBJ-6, which affects later behavior. This is reflection on the skill-using agent inside the workflow boundary, not evidence that the fixed improvement harness revises a theory of its own organization. Self-improvement conclusion status claimed at the tested skill-evolution boundary; its stronger causal confirmation remains uninspected.

## Lens scoping

### Memory/context scope

Full documentary lens. Triggers: SRC-1 §3, CLM-1. Included OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7 and their RTE-1, RTE-2, RTE-3, RTE-5, RTE-6 write/read paths. Default configuration and the wiki-access ablation are included; the latter has unknown delivery. Final test and cross-model reuse are RTE-1 branches. OBJ-9 is a delivered derivative, not independently counted as durable memory. Persistent accumulated content is central to the claimed mechanism. Exact storage implementation and model internals are excluded.

### Epistemic scope

Full documentary lens, triggered by root-cause and increasingly supported knowledge claims in SRC-1 §3 and CLM-1, CLM-3. Assessed RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, especially OBJ-2 explanations and OBJ-6 procedures. No implementation/independent run layer; only declared transformations, operational admission and reported outcomes can be characterized. Unassessed provider reasoning and domain scorer correctness prevent stronger warrant.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried all raw/wiki/skills objects and the default, held-out/transfer and wiki-access-ablation branches. Disclosed retained parts use files and combine prose with command syntax, metadata/diffs and outcomes; all known profile bases remain claimed. Wiki patterns, index summaries, evolution-log summaries, rejected-history records and accepted procedures qualify as automatic trace-fed, staged, cross-task writes. Raw logging alone and OBJ-9 do not independently establish learning. No parametric learning is described in this scoped route.

RTE-1 supplies all active skills automatically to inference, including final and cross-model testing. RTE-2 supplies full existing wiki plus outcome-stratified traces automatically to the maintainer. RTE-3 initially supplies catalog, impact history and OBJ-9, then returns pages/traces that the proposer requests. The default pushes are coarse, while requested paths remain pull; names/aliases do not prove identifier-based push. RTE-7 leaves its selector and authority unknown, preventing complete known authority and push-signal sets even though the pull/push direction union is complete.

The maintainer's per-trace cap and sample count do not bound full-wiki growth. RTE-2 consolidates summaries, synthesizes diagnoses and evolves pages; RTE-3 evolves procedures; RTE-6 compiles intervention history. Duplicate-prevention instructions are not demonstrated deduplication of existing memory. Full wiki delivery in the main text is broader than the Appendix E.2 input list, and Appendix E.3 asks to read catalog/impact even though main text initially supplies them. Both discrepancies remain implementation uncertainties. OBJ-7's rationale is retained, but its later consumer and inference injection are unresolved. Pattern/index/log/impact rationale has described later users; this does not establish rationale delivery to every executor.

Delivery is not activation: SRC-2 reports some consumers fail to follow multi-step skills. The bundled ablation, transfer results and simplified case do not test dependence on specific recalled content (ABS-2). All14 comparison axes preserve these scope and evidence limits.

### Epistemic lens

1. **Source-and-claim boundary.** SRC-1 supplies doctrine; SRC-2 supplies reported operation. Scope, excluded participants and prevented conclusions are fixed above. Question: which transformations and checks license later reliance? CLM-1 and CLM-3 concern accumulated knowledge; CLM-2 concerns transfer. No implementation or original candidate artifacts are available.

2. **Epistemic-object annotations.** OBJ-1 is acquired task/interaction evidence with unverified recording completeness. OBJ-2 contains ampliative root-cause and strategy conjectures as well as observed-event summaries; neither entailment nor truth follows from the trace. OBJ-3 and OBJ-4 reshape/register these accounts, with semantic fidelity uninspected. OBJ-5 retains measured outcomes and interventions, without granting their explanations warrant. OBJ-6 contains imperative policy plus possible truth-apt applicability claims; particular rules may be conjectures rather than derivations. OBJ-7 retains claimed motivating relations, whose completeness is uninspected. OBJ-8 is a measurement within a named task/scorer domain. OBJ-9 is a supplied outcome-summary view whose preservation fidelity and independent retention are uninspected. Identity/form/producer/consumer remain on their canonical records.

3. **Authority-route ledger.** Architectural status for each declared function below: doctrine only. Observed candidate state: no instance observed in original artifacts; SRC-2 illustrations/reports are not promoted into such artifacts. Implemented force is uninspected; described force follows the corresponding BAP. Operational admission and epistemic acceptance are distinguished.

| Canonical route | Function and content relation | Target, criterion, timing and consequence | Warrant and limit |
|---|---|---|---|
| RTE-1 | Operational consumption; no content change to skill | Inference receives active OBJ-6; BAP-1 | Procedure use, not acceptance of explanatory truth |
| RTE-1 | Check/evidence production; acquisition of observations | Task tools produce OBJ-1 during rollout | Domain-scoped observations; recording fidelity uninspected |
| RTE-2 | Content transformation; ampliative conjecture for OBJ-2, reshaping for OBJ-3, OBJ-4 | Maintainer interprets successful/failed traces after rollout; BAP-2 | Plausible explanations/workarounds, not demonstrated causes |
| RTE-2 | Retention; no additional content change | Harness applies wiki output before skill validation | Durable access; no semantic acceptance criterion established |
| RTE-3 | Operational consumption; no content change | Model reads accumulated evidence; BAP-3 | Relevance selection alone does not validate content |
| RTE-3 | Content transformation; policy update with possible ampliative applicability claims | One skill proposal from diagnosis/history | Candidate instructions, not warranted general rules |
| RTE-4 | Check/evidence production; no content change to candidate | Domain scorer compares returned answers/outcomes on validation split; BAP-4 | Candidate performance on selected tasks only |
| RTE-5 | Disposition/acceptance; no content change | Strict improvement selects candidate skill for later task use; BAP-5 | Operational performance acceptance; neither root-cause truth nor transfer certified |
| RTE-5 | Behavior/policy adaptation; accepted policy replaces active skill | Later RTE-1 consumes admitted skill | Subsequent use is described; isolated activation/benefit uninspected |
| RTE-6 | Retention; non-ampliative recording | Diff/score/outcome survives either decision; BAP-6 | Historical evidence if correctly recorded; explanation not endorsed |

RTE-7 adds an operational-consumption alternative, architectural status doctrine only, no content change to wiki; target is training inference, but delivery/authority remain not determinable and no original instance is observed. It licenses only the reported access comparison.

All rows cite their canonical SRC-1 anchors; claim associations are CLM-1 for wiki paths, CLM-2 for subsequent inference and CLM-3 for proposal/history. No mismatch with a narrower operational gate is invented; the unresolved issue is the broader knowledge language.

4. **Per-object lifecycle.** OBJ-2: observation RTE-1 → conjecture RTE-2 → possible guidance at RTE-3; each declared phase is doctrine only/no instance observed. Derived consequence, direct test of the explanation, truth acceptance and post-acceptance integration are not determinable architecturally, with no instance observed. RTE-4 tests procedures, not the explanation independently. OBJ-6 applicability claims: conjecture RTE-3, test RTE-4, performance acceptance RTE-5 and later operational use RTE-1 are doctrine only/no instance observed; derivation of a stated consequence is uninspected. Acceptance criterion is higher validation score for procedural use on this benchmark. It cannot be relabelled acceptance of all truth-apt claims or full discovery-lifecycle integration. OBJ-1 acquisition, OBJ-3 catalog reshaping, OBJ-4 summary, OBJ-5 outcome recording, OBJ-7 rationale mapping and OBJ-8 measurement have non-ampliative or indeterminate transformations rather than evidenced ampliative lifecycles. OBJ-9 is an intended non-ampliative outcome summary with acquisition/lineage through RTE-3; preservation remains uninspected. For OBJ-3, OBJ-4 and OBJ-7, exact inputs/outputs would be needed to establish semantic preservation. No candidate truth-apt output is asserted for the imperative-only parts of OBJ-6; direct-adaptation route RTE-5 applies.

5. **Claim comparison.** CLM-1 has explicit design routes and reported bundled ablation support, no inspected implementation or causal evidence here. CLM-2 has reported transfer scores, no general guarantee. CLM-3 has a simplified case account and preserved-history design, no original candidate-linked trace. None licenses upgrading a conclusion status.

6. **Bounded conclusion.** WikiSkill describes a route from task experience through editable explanations to performance-gated procedures. It grants operative force to skill-score comparisons while letting wiki explanations persist without that gate. The paper reports useful bundle-level outcomes and an illustrative revision path. It does not independently establish which explanation is true, whether its criticism caused an improvement, or whether any selected procedure remains reliable outside the tested distributions.

## Reconciliation

Specialist input/report run, capture digest, boundary, completed status and input SHA-256 matched. Proposal mappings: MEM-OBJ-1 → OBJ-9; MEM-RTE-1 → the already defined initial-supply part of RTE-3; MEM-RTE-2 → test/transfer branches of RTE-1; MEM-RTE-3 → RTE-7; MEM-ABS-1 → ABS-1; MEM-ABS-2 → ABS-2. Merged proposals do not split or redefine existing canonical identities.

All eight reported integration issues are disposed: proposed records registered; OBJ-4 filename disagreement preserved; initial supply/requested reads and full-wiki/narrow prompt list preserved; OBJ-7 consumer/injection and patch handling left uninspected; strict improvement and no_action uncertainty retained; CLM-1 remains bundled and CLM-2 conditional; CMP-1 role-specific fixation remains uninspected. The profile includes the ablation rather than silently excluding its unknowns. Memory owns its comparison judgments; epistemic annotations cite shared records and do not duplicate or strengthen them. Both passes independently distinguished skill-score admission from truth acceptance; no independent empirical confirmation is claimed.

## Bounded synthesis

WikiSkill's strongest reported contribution is repeated skill improvement with persistent diagnostic knowledge, supported by benchmark comparisons and a bundled wiki/maintainer ablation. Its distinctive separation is between immutable experience, continuously retained wiki knowledge and reversible skills. A failed candidate can therefore preserve its diagnosis and rejection evidence for a later proposal while being removed from task instructions.

This has different licenses at different points: wiki retention preserves access, the proposer produces a candidate, and the strict validation gate licenses performance-relative skill selection. Full skill injection removes retrieval from the experiment. Results should therefore be read as skill-quality findings under the specified consumer models and benchmarks, not demonstrated scalable retrieval or universal transfer.

Conjectural-learning conclusion status uninspected at the stronger attribution required here: formulated diagnoses, prescribed criticism and revision are claimed, while reported improvements concern the whole pipeline. Reflection conclusion status claimed for self-behavior representations driving later skill changes. Self-improvement conclusion status claimed for the described benchmark skill-evolution process. None is established as an independently observed or causal property by this paper-only run. Original trajectories, exact wiki/skill versions, code-enforced read/write boundaries and candidate-linked criticism tests would materially strengthen the account; a validation gate alone would not settle explanatory truth.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No implementation or original runs | SRC-1, SRC-2; all routes | Frozen paper | Wiring, enforcement, runtime observation | Pinned code and replayable artifacts |
| Fixed names are not immutable model identities | CMP-1 | §4.1 | Exact parameter/version fixation | Weight digests or endpoint version records |
| Wiki permanence without automatic pruning is reported | RTE-2, RTE-6 | Limitations | Sustainable long-run memory cost or correctness | Long-run traces and maintenance mechanism |
| Gate tests scores rather than causal explanations | OBJ-2, RTE-4, RTE-5, CLM-1 | §§3.2.4, 5.1 | Truth acceptance and criticism-specific improvement | Candidate-linked consequence tests and component comparisons |
| Full injection and bounded benchmark evolution | RTE-1, CLM-2 | §3.2.1, Limitations | Retrieval robustness and within-rollout learning | Retrieval experiments and long-horizon runs |
| Filename and context specifications differ | OBJ-4, RTE-2, RTE-3 | Main text versus Appendix E | Exact implementation path and context completeness | Pinned workspace and assembly code |

## Verification and blockers

### Semantic verification

Source digest and destination metadata checked before analysis. Every canonical source-dependent record stays documentary. Ordinary progression, equal/lower score rollback, perfect-baseline termination, no-action and wiki-access alternate branches inspected. Theory formulation, operation, criticism, revision, improvement and reflection are separately scoped; score admission never stands for explanation acceptance. Specialist profile scope checked against OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9 and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7. Every trace-fed durable write, including catalog/log/history summaries, enters the dependent learning axes; OBJ-9 does not. All push consumers and coarse default selectors identified; ablation unknowns prevent unsupported aggregate classifications. Complete ID mapping and minimum quote support checked; no stronger evidence status inferred.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md`; `commonplace-validate --full` passed with no failures or warnings.

### Blockers

None.
