---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AIDE2 runtime baseline: documented nested harness search, private-grade admission and forcing routes in the frozen paper capture."
run-id: AAS-2026-10-14-2609-26457-6b3bcd4791cf-01
reviewed-boundary: arxiv-2609.26457v1-2026-10-14
---

# AIDE2 runtime report

## Runtime account

### Evidence and consequential work

AIDE2 searches for research-agent harnesses that produce better task solutions at a fixed evaluation budget. It edits the code controlling search, context and verification, not the underlying model weights. The target is the documented improvement plane, with a complete paper but a partial executable loop, as fixed in [the boundary](boundary.md). SRC-1 supplies design and author-reported operation, not inspected implementation or raw execution evidence. In particular, the paper's algorithm is not evidence of a shipped CLI or API entry point. Packaging, entry-point arguments, full generated agents and evaluator implementations are unavailable in this capture.

> Our experiments target the harness layer, the code that surrounds a model and controls an agent’s search, context, and verification.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

The ordinary documented entry is Algorithm 1, supplied with an initial agent, outer-loop agent, tasks, per-task budgets and trajectory length. AIDE0 is the initial inner agent; AIDEhuman drives the principal outer-loop experiment. Model calls use Gemini 3 Flash inside and Claude Opus 4.7 outside ([RT-CMP-gemini3-flash](#rt-cmp-gemini3-flash), [RT-CMP-claude-opus4](#rt-cmp-claude-opus4)). The initiator's runtime identity, authentication and launch procedure are not stated. Experimental designers choose tasks, models and constraints; that human setup is distinct from per-rewrite admission.

### One documented invocation end to end

1. Grade the initial harness. For each selection task, start from its codebase and run that harness until the task's dollar budget is spent. Its draft, debug and improve operators generate runnable solution candidates. AIDE0 chooses the highest-scoring parent greedily. Solution execution yields public feedback; a reviewer extracts a score and relevant feedback. The harness chooses its own final solution. This is [RT-RTE-inner-search](#rt-rte-inner-search).
2. The grading procedure evaluates those returned solutions on private held-out data, averages private scores over tasks and repeated independent runs, and returns a grade. The outer driver reads previous harness proposals and their grades, reviews evaluation artifacts over several steps, and proposes a rewrite of the current incumbent. This is [RT-RTE-harness-admission](#rt-rte-harness-admission).
3. Grade the rewrite under the same task budgets. The fixed outer selection policy keeps the best graded agent; a rejected proposal does not displace the incumbent. An accepted rewrite becomes the codebase edited next and the harness used in subsequent evaluations. At the trajectory limit, return the highest-grade agent. Storage format, checkpoints, process restart and exact installation/loading are not documented.

SRC-1 §2.1, Algorithm 1 and §2.2 describe this sequence. The model-driven operators own candidate construction and, through the editable inner policy, task-level next-step and return choices. The fixed outer policy owns incumbent selection. Execution of candidate scripts and private grading belongs to the experimental infrastructure; the capture does not identify exact executor APIs, process isolation, filesystem grants or callback interfaces. Coordination is nested search with task/run score aggregation, not evidence of a particular distributed-worker protocol.

### Material alternate and forcing routes

Four forcing cases bound the ordinary account.

- **AIDE85 changes the inner selector without changing the outer selector.** It chooses among five strategy labels using UCB1, with 30% of steps sampling by softmax over best arm scores, then expands the highest-scoring node carrying the selected label. Every five steps it forks the global best under a different arm. Greedy parent selection is therefore a baseline property, not an AIDE2-wide invariant. Details and role-specific context inputs remain in [RT-RTE-inner-search](#rt-rte-inner-search), SRC-1 §3.5.
- **A candidate can change evaluation machinery.** The accepted agent includes a patch preventing one failing test from crashing all cases in one held-out scorer. Thus the documented effect boundary is not exclusively search/prompts. It reaches a scoring-script repair. The paper calls the intervention narrow, but does not expose a permission boundary proving that evaluator changes are generally restricted. See [RT-RTE-robustness-controls](#rt-rte-robustness-controls), SRC-1 §3.5.
- **A run can end before its primary cap.** Appendix A scores the best available candidate after a secondary limit or context-window error. AIDE0's context errors terminated five FML-Bench runs and 48 larger-budget ALE-Bench runs. Successful exhaustion of the intended primary budget is not guaranteed; fallback scoring is part of the reported protocol. See [RT-RTE-terminal-fallback](#rt-rte-terminal-fallback).
- **An evolved agent can drive the outer loop.** The ignition test substitutes AIDE47 for AIDEhuman while keeping the same AIDE47 initial inner agent. Its three-seed comparison does not establish superior self-improver efficiency or automatic production promotion. See [RT-RTE-ignition-test](#rt-rte-ignition-test), SRC-1 §3.6.

### Controls, authority and persistence

The capability surface includes model-generated edits to task code and harness code, solution execution, reviewer interpretation of outputs and exploration of evaluation artifacts. The scorer patch is a positive witness of evaluation-machinery reach. The current grant set and deployed isolation envelope remain uninspected: no allowlist, sandbox configuration, approval interface or provider-native-tool contract is supplied. The paper cannot support a conclusion that all direct model calls, shell/subprocess paths, host callbacks, extensions or remote workers are mediated by a particular guard. These paths are unobserved, not established absent.

AIDE85 bounds draft/improve context using summaries of the root and recent candidates and conditionally adds deduplicated error signatures when the bug rate reaches 15%. This identifies a documented context-selection boundary, not full memory lifecycle verification. Debug and reviewer prompts, summary production rules and reload routes are not fully specified. This report leaves retained-memory objects and revisions to the memory member. The immediate loop consumes current candidate state; later outer rounds consume accepted harness code through [RT-BAP-incumbent-code](#rt-bap-incumbent-code).

> Which candidate to edit next, which to return, and how to structure the agent’s memory are all part of the agent’s code and are editable by the outer loop.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

The reported benchmark execution substrates are large CPU machines for ALE-Bench, CPU-only Modal containers for MLE-Bench and A100 GPUs for WeatherBench 2, FML-Bench and KernelBench (SRC-1 appendix A). Those resources are not evidence of filesystem/network isolation. Prompts instruct models; symbolic selection rules determine choices when executed; provider parameters supply model behavior. These are different authority channels, recorded below rather than treated as one guarantee.

### Load-bearing guarantees and their limits

| Claimed guarantee | Owner and enforcement point | Strength and coverage | External contract and alternate-path limit | Conclusion statuses |
|---|---|---|---|---|
| Only the best private-grade harness becomes incumbent | Fixed outer selector at candidate admission, [RT-RTE-harness-admission](#rt-rte-harness-admission) | protocol; all graded candidates in the described outer loop | Requires comparable, faithfully computed grades. Buggy proposals receive no grade; noise can admit a worse true performer. No inspectable bypass/rollback enforcement is supplied. | design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: claimed |
| Inner optimization does not directly observe private selection outcomes | Task feedback/scoring split, [RT-CLM-private-signal](#rt-clm-private-signal) | protocol; documented selection-task inner runs | Requires private data and scoring to remain isolated. Outer driver does see grades; repeated outer selection can adapt to them. The scorer patch demonstrates machinery reach, not private-data access. Sandbox and alternate access paths are uninspected. | design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: claimed |
| Comparable evaluation constrains compute spending | Budget accounting in Grade; held-out benchmark caps, [RT-RTE-terminal-fallback](#rt-rte-terminal-fallback) | protocol; per-task selection dollar caps and per-benchmark comparison protocols | Requires accounting of tokens and solution execution. Held-out modes include step caps, secondary caps and different models. Cost accounting and overshoot handling cannot be verified. | design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: claimed |
| Robust, nonempty solutions | Code-generation prompts and short-output re-prompt guard, [RT-RTE-robustness-controls](#rt-rte-robustness-controls) | best effort; prompts and generated-code length check described for AIDE85 | Relies on model compliance and a length proxy; neither establishes correctness or generalization. The selection penalty reportedly never changes the selected candidate. | design conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: claimed |

These guarantees concern the paper's protocols. None is certified here as an executable invariant or deployment guarantee. The strongest counterevidence is local to each guarantee: noisy incumbent admission, outer exposure to aggregate grades, premature task termination, and an ineffectual ranking penalty. SRC-1 §5 explicitly warns that a falsely accepted rewrite can redirect subsequent search.

## Shared records

### Components

#### RT-CMP-gemini3-flash
Label: Gemini 3 Flash inner-loop model

Source-native identity: gemini 3 flash, used for every inner-loop agent evaluation during the principal recursive run. Representational form: distributed-parametric. Storage substrate: provider-hosted model parameters; physical storage and provider internals uninspected. Parameters changing during operation: the paper says the model is held fixed within each loop; no model-weight update is part of the documented harness search. Exact version pinned: no immutable model revision or weight digest is supplied. Mutable endpoint resolving to another model: uninspected; model naming alone does not fix provider routing. Evidence: SRC-1 §2.2, doctrine/design and reported operation. Held-out protocols also use Gemini 3.1 Pro, GPT-5.4, GPT-5.6-Sol and Fable 5; those evaluation-only dependencies do not establish model mutability within the selection run.

> During the recursive self-improvement run, we hold the model fixed within each loop. The outer-loop agent runs on claude opus 4.7 (Anthropic, 2026b), while every inner-loop agent is evaluated with gemini 3 flash (Google DeepMind, 2025).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-CMP-claude-opus4
Label: Claude Opus 4.7 outer-loop model

Source-native identity: claude opus 4.7, used by the outer driver in the principal run. Representational form: distributed-parametric. Storage substrate: provider-hosted parameters; provider internals uninspected. Parameters changing during operation: held fixed according to SRC-1 §2.2. Exact version pinned: no immutable revision/digest supplied. Mutable endpoint resolving to another model: uninspected. Evidence: the passage in [RT-CMP-gemini3-flash](#rt-cmp-gemini3-flash). The paper says the outer reviewer explores evaluation artifacts over several steps, unlike the inner reviewer's one call; it does not reveal every call's provider request or hidden provider state.

### Operative objects

#### RT-OBJ-agent-code
Label: Candidate and incumbent agent code

Source-native identity: complete research-agent code at each outer tree node. Representational form: symbolic executable harness rules; embedded instructions have natural-language consumption and are separated as [RT-OBJ-robustness-instruction](#rt-obj-robustness-instruction). Storage substrate: codebase, with backing filesystem/version/archive format uninspected. Lineage: AIDE0 starts as a pared-down AIDE refactor; proposed successors edit the incumbent. Accepted code persists across outer rounds and later benchmark evaluation. The code determines parent selection, returned solution and context policy. Exact generated code is not in the capture, so complete instruction/code decomposition remains unresolved. Evidence: SRC-1 §2.1 and §2.2; the editable-code quote above and [RT-RTE-harness-admission](#rt-rte-harness-admission).

#### RT-OBJ-robustness-instruction
Label: Private-split robustness reminder

Source-native identity: fixed instruction in every AIDE85 code-generation prompt reminding the model of unseen private scoring and preferring robust, generalizable approaches. Representational form: natural language. Storage substrate: prompt-bearing harness; actual text and template serialization uninspected. The instruction persists with the harness and is delivered to code generation. The private-split reminder is not a proof of compliance. Evidence: SRC-1 §3.5; minimum passage in [RT-RTE-robustness-controls](#rt-rte-robustness-controls).

### Routes

#### RT-RTE-inner-search
Label: Budgeted task solution search

Endpoints and progression: task codebase → draft/debug/improve calls → execution → reviewer score/feedback → parent choice → chosen terminal solution. Owner: inner harness policy and model operators, with experimental executor supplying feedback. Operating mode: bounded code-optimization experiment, not open-ended arbitrary requests. Improvement trigger: public objective feedback; debug targets errors. Proposer: generation model; decider: editable harness selector and final-return policy. Human contribution: task/objective/budget setup; per-candidate human veto is not described. Answer oracle: task-specific public metric/evaluator supplies measurable outcomes, not the reviewer model alone; exact evaluator implementations uninspected.

- Immediate return: chosen task solution, after iterative solution execution and feedback.
- Later read-back: accepted harness code governs later task runs; current-run candidate history is repeatedly supplied or summarized for later operator invocations, with memory revisions left to the memory member.
- Delegated visibility: reviewer receives execution output; AIDE0 generation receives full candidate/output history; AIDE85 draft/improve receive root/recent summaries and gated error signatures. Full debug/reviewer context is uninspected.
- Selection predicate: AIDE0 greedily selects the highest-scoring parent; AIDE85 selects a strategy arm with UCB1 or 30% softmax sampling, expands its best node, and forks the global best every five steps.
- Invalidation or expiry: fixed task budget ends ordinary search; candidate state lifetime across task/process boundaries is uninspected.
- Activation or effect: documented policy chooses which task code to edit and which solution private grading receives; prompt compaction changes delivered context. Raw operator traces are unavailable.
- Evidence limits: SRC-1 §§2.1–2.2 and §3.5 describe operators and policies; full executable rules, complete prompts and concrete task traces are not supplied.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

> The agent consists of several operators designed for different purposes: draft to explore broad sets of new ideas, debug to repair a solution with a bug or execution error, and improve to refine a promising direction.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> At each step a strategy arm is chosen by UCB1, with 30% of steps instead sampling an arm by a softmax over the arms’ best scores. The highest-scoring node carrying the chosen arm’s label is then expanded with a new node.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-RTE-harness-admission
Label: Private-grade harness successor admission

Endpoints: previous harnesses/grades → outer model-driven rewrite → independent task runs → private grade → incumbent code. Owner: AIDEhuman proposes; fixed outer selector decides. Trigger: each outer step. Proposed change: inner-agent harness, including search, prompts, context and feedback machinery. Operating mode: bounded curriculum across ML, heuristic algorithm and harness engineering task families. Answer oracle: private task evaluators produce reference outcomes through scores; the grade aggregates returned-solution private scores over tasks and repeated runs. No expected harness text is an oracle.

Admission and rejection: best-grade selection can reject any lower-grade proposal; buggy proposals receive no grade. A human chooses the experiment but per-content approval/veto is not described. Rollback/recovery: failed/rejected candidates leave the incumbent available; recovery after false noisy acceptance, restart and checkpoint semantics are uninspected. Guidance: prior proposed agents, grades and evaluation artifacts shape the rewrite. The full outer prompts and proposal rationales are not supplied. What persists: accepted code and proposal/grade history for future rounds; storage mechanics unresolved. This is evidence-responsive code selection, not by itself a record of formulated theoretical criticism.

- Immediate return: a candidate grade and incumbent decision; after the trajectory, the best graded agent.
- Later read-back: accepted code becomes the next edit base and later task optimizer; previous proposals and grades reach the outer driver.
- Delegated visibility: inner agents receive public feedback; the outer reviewer explores evaluation artifacts over several steps, and the outer agent receives aggregate private grades. Artifact contents beyond that description are uninspected.
- Selection predicate: fixed argmax over graded agents; incumbent improves only with a better grade, subject to evaluator noise.
- Invalidation or expiry: rejected proposals do not replace the incumbent; trajectory length terminates search. Grade expiry and re-evaluation policy are uninspected.
- Activation or effect: accepted rewrites change later research-agent organization. The paper reports seven incumbent changes, not inspectable installation/load traces.
- Evidence limits: SRC-1 §2.1, Algorithm 1, §§2.2–3.2, appendix D and §5. No executable admission gate, raw rewrite archive or independent causal identification is available.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

> In practice, the outer-loop agent edits the current incumbent, so each accepted rewrite becomes the codebase that is edited at the next step. At step kk, the incumbent is the best agent graded so far.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> Out of the graded rewrites that were rejected, about a quarter scored higher than the incumbent on the agent-visible public signal and were rejected on the private grade.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-RTE-robustness-controls
Label: AIDE85 robustness interventions

Owner: generated harness supplies reminders, re-prompt guard and selection penalty; it also includes a held-out scoring-script patch. These interventions share outer admission through [RT-RTE-harness-admission](#rt-rte-harness-admission), but have different downstream consumers. Code generation consumes the reminder through model interpretation. The short-code guard triggers another generation call below 40 characters. A symbolic penalty is intended to avoid lucky scores, but preserves ordering. A scorer repair contains single-case failure rather than aborting all cases. No broader evaluator-edit permission guarantee follows from this witness.

Admission context: outer model proposes; private-grade selector accepts/rejects. The source reports the patch's stated guidance as a narrow repair of a verified failure, but provides neither full rationale nor executable diff. Recovery: re-prompting for stub-like output and per-case scoring continuation; rollback of the scorer patch is uninspected. Operating mode: research/evaluation runs of the accepted agent. Answer oracle: existing private scoring machinery, whose crash behavior is changed; reminder and code length are not answer oracles.

- Immediate return: regenerated code after a short output, chosen solution after ranking, and score after per-case evaluator failure handling.
- Later read-back: robustness mechanisms recur with the accepted harness; retained error-memory contents are outside this route's revision account.
- Delegated visibility: code-generation model receives a private-split reminder, not the hidden split itself; scorer consumes test-case outcomes. Exact scorer/model data access remains uninspected.
- Selection predicate: re-prompt below 40 characters; penalize distance from the median of top candidates. The latter reportedly preserves all candidate ordering.
- Invalidation or expiry: inapplicable — the described fixed mechanisms have no stated expiry; code replacement can change them, but no specific invalidation protocol is provided.
- Activation or effect: source-reported replay says the ranking penalty never changes the selected candidate; the scorer patch avoids whole-evaluation failure. Independent component benefit is not established.
- Evidence limits: SRC-1 §3.5; no raw replay outputs, exact templates, patch or external enforcement audit.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

> The first is a pair of prompt-level safeguards: a fixed instruction in every code-generation prompt reminding the model that solutions are scored on a private split it cannot see and that it should prefer robust, generalizable approaches, and a guard that re-prompts when generated code is nearly empty (under 40 characters, e.g. a stub or placeholder).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> Because the penalty preserves the ordering of the candidates, replaying the rule over the held-out runs shows that it never changed which candidate the agent selected.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> One task’s held-out scoring script crashed on all of its test cases whenever any single test case failed, and AIDE85\mathrm{AIDE}_{85} adds a small patch, which the agent described as “a narrow, low-risk intervention targeting a verified failure mode … without altering search dynamics”, that stops a single failed test case from taking down the whole evaluation.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-RTE-terminal-fallback
Label: Held-out run termination and fallback scoring

Owner: benchmark protocol terminates a run at primary/secondary caps or an error, then scores its best available candidate. Context-window failure is a forcing case, not a successful operator return. Operating mode: held-out evaluation; benchmark designers choose constraints. Selection: best available candidate, with exact fallback selector implementation uninspected. Human per-result veto is not specified. Answer oracle: benchmark private outcomes; terminal errors alone are not answers.

- Immediate return: private score for the best available candidate at termination.
- Later read-back: uninspected — results inform paper comparisons, but the capture does not show automatic re-entry of held-out results into the selection run.
- Delegated visibility: benchmark evaluators receive the terminal candidate; exact orchestration of failed workers and reviewer visibility is uninspected.
- Selection predicate: primary cost caps for ALE-Bench, MLE-Bench and WeatherBench 2; primary step caps for FML-Bench and KernelBench; secondary constraints or context errors can terminate earlier.
- Invalidation or expiry: termination ends further search in that run; no resume policy supplied.
- Activation or effect: preserves a score after early termination rather than discarding the run; reported AIDE0 failures include five FML-Bench and 48 larger-budget ALE-Bench runs.
- Evidence limits: SRC-1 appendix A and appendix E report the protocol and errors, not raw terminal artifacts or executor recovery code.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

> A run that reaches a non-primary constraint, for example, the 12 hour time limit for ALE-Bench which uses cost as the primary constraint, is scored on the best candidate available at that point.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-RTE-ignition-test
Label: Evolved agent as outer-loop driver

Endpoints: AIDE47 initial harness plus either AIDE47 or AIDEhuman outer driver → three independent 50-step runs per arm → incumbent-grade comparison. Owner: experimental setup chooses driver; each outer driver proposes rewrites and the same fixed grade policy selects incumbents. Trigger: test whether a discovered agent is a better self-improver. Operating mode: bounded paired-arm experiment. Answer oracle: aggregate private grade, not an expected code output. Human contribution: treatment/reference design; automatic promotion or human approval of production promotion is not established. Rejection/recovery of individual rewrites follows [RT-RTE-harness-admission](#rt-rte-harness-admission). Guidance and persistence are the same proposal/grade history and accepted-code chain; no new persistent guidance object is documented.

- Immediate return: final incumbents and grade trajectories for each arm.
- Later read-back: evolved AIDE47 code is consumed as an outer driver in this test; subsequent production promotion is uninspected.
- Delegated visibility: driver receives previous agents/grades; its inner evaluations retain the public/private distinction.
- Selection predicate: per-run private-grade incumbent selection; the proposed criterion for promotion is better loop-driving performance, not demonstrated here.
- Invalidation or expiry: each arm terminates after 50 steps; no ongoing promotion/resume policy supplied.
- Activation or effect: AIDE47 reportedly produces accepted improvements as outer driver; endpoint means 0.780 and 0.782 do not establish driver superiority.
- Evidence limits: SRC-1 §3.6, three seeds per arm and substantial variance; no raw traces, and no decisive sample-efficiency or acceleration conclusion.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

> However, with only three seeds per outer-loop agent, we find these results to be inconclusive; they do not establish that AIDE47\mathrm{AIDE}_{47} is more sample-efficient as a self-improver than AIDEhuman\mathrm{AIDE}_{\mathrm{human}}.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

### Claims

#### RT-CLM-private-signal
Label: Separated optimization and selection signals

Claimed operation: inner runs optimize public task feedback, while private held-out outcomes grade their selected solutions for outer admission. Owner: task/grading protocol. Guarantee strength: protocol, not a verified information-flow invariant. Evidence: SRC-1 §2.1. Covered path: documented selection-task evaluation. Alternate-path limits: the outer driver sees grades; code/evaluator access paths and private-data isolation are not inspected. The claim does not rule out adaptation to the fixed selection benchmark or prove resistance to proxy exploitation.

> First, separating the inner loop’s optimization signal rtpubr^{\mathrm{pub}}_{t} from the outer loop’s selection signal gg (driven by rtprivr^{\mathrm{priv}}_{t}) prevents the inner-loop agent from directly optimizing the criterion used for outer-loop selection.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### RT-CLM-harness-improvement
Label: Reported recursive harness improvement

Claimed operation: seven accepted rewrites improve the research-agent harness over an eight-day, 100-node run; private incumbent grade rises from 0.703 to 0.778. Source: SRC-1 §3.2; held-out transfer is reported in §3.3 and appendix A. Boundary: the improvement plane plus the inner agents whose organization it rewrites. Horizon: outer rounds and subsequent held-out task evaluations. Independently specified objective: better task optimization at fixed evaluation budgets. This does not mean that the unchanged outer driver itself improves during the principal run.

Self-improvement links: (1) prior grades and artifacts reportedly shape rewrite proposals and admission; (2) accepted harness code replaces the inner agent's search/context organization; (3) that code enters [RT-BAP-incumbent-code](#rt-bap-incumbent-code); (4) subsequent grading and held-out evaluations reportedly execute changed agents. All four are supported as attributed design/operation, not independently verified causal execution. The missing inspectable code/load/run chain prevents an independently established exercised attribution. Successful improvement is separately author-reported at the full-harness level. Component-specific causal benefit is unestablished; §5 says the contributing versus unused components remain unclear. Learning through harness retention is therefore reported, not evidence of model-weight learning. Better self-improver efficiency remains inconclusive in [RT-RTE-ignition-test](#rt-rte-ignition-test). No theory-builder classification is inferred merely from code selection or numerical scores.

> We ran AIDE2\mathrm{AIDE}^{2} over 8 days of wall-clock time, producing a 100-node trajectory, containing the initial agent and 99 rewrite proposals. As shown in fig. 2, we observe seven accepted improvements at steps 2, 6, 28, 39, 47, 63, and 85, with the incumbent grade rising from 0.703 to 0.778, evidence of a sustained trend.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> It is unclear which components drive performance and which, if any, are unused artifacts of earlier recursive self-improvement steps.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-incumbent-code
Label: Accepted harness controls later search

Consumer: next-round editing driver and inner-agent executions. Channel: incumbent codebase becomes the next rewrite base and task optimizer. Force: symbolic runtime rules determine search/control when executed; embedded prompt instructions separately receive model interpretation. Horizon: successive outer rounds, then held-out problems. Evidence: SRC-1 §2.1, §3.3 and [RT-RTE-harness-admission](#rt-rte-harness-admission). Delivery/loading and actual behavioral dependence remain attributed rather than inspected.

#### RT-BAP-robustness-prompt
Label: Robustness reminder reaches code generation

Consumer: AIDE85 code-generation model. Channel: fixed reminder in every generation prompt, [RT-OBJ-robustness-instruction](#rt-obj-robustness-instruction). Force: advisory model-interpreted guidance, not executable enforcement of robust solutions. Horizon: generation calls made by the retained harness. Evidence: SRC-1 §3.5 and [RT-RTE-robustness-controls](#rt-rte-robustness-controls). No independent reminder ablation establishes compliance or benefit; full-agent reduction in reward hacking cannot be attributed to this instruction alone.

## Annotations

none
