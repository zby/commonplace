---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SkillLift runtime baseline: task-portfolio evolution, verifier calibration, durable recovery and distinct category/domain drivers at the frozen main-repository revision."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
---

# SkillLift runtime report

## Runtime account

SkillLift is an improvement plane, not the agent executing the benchmark task. Its consequential work is to propose skill changes, score their visible instructions, run candidate portfolios against benchmark reward, select a successor and calibrate the scoring receipt against reward rankings. The frozen [boundary](boundary.md#boundary-and-evidence) excludes unavailable benchmark and host implementations from end-to-end conclusions. All evidence below is SRC-1 implementation or explicitly identified prompt doctrine at that commit. No program, test, provider or benchmark was executed. Wiring is not observed activation or demonstrated benefit.

### Ordinary task invocation

The shipped evaluation CLI dispatches the `skilllift` WildClaw path to `SkillLiftWildClawRunner`. The runner resolves one task, constructs a portfolio store and adapter, configures thresholds and creates rubricator, generator and verifier clients from an endpoint profile. These clients receive separate system/user request bodies rather than a shared accumulating conversation. The runner uses a bounded-edit generator by default; constructor-injected planners, generators, verifiers and benchmark runners are alternate capability surfaces. SRC-1: `skilllift_eval/cli.py`, `skilllift_eval/runners/skilllift_wildclaw.py`, `skilllift/skilllift/llm_client.py`. See [RT-CMP-llm-client](#rt-cmp-llm-client).

The coordinator owns the next step. It checks task/seed identity, fingerprints algorithm configuration and reward policy, initializes or reconstructs the accepted parent, then evaluates an anchor. An invalid anchor returns an indeterminate frozen seed; an already-terminal unadapted anchor returns without final trials. Otherwise the coordinator generates or reloads a plan, prepares candidate branches, refines them with the verifier, evaluates valid branches through the adapter and accepts an oracle improvement or an oracle tie with a higher verifier score. Mode B then revises the receipt against the *pre-round* champion and evaluated candidates. The receipt change does not retroactively choose that round's winner. Stop predicates include invalid candidates, terminal reward, two no-improvement rounds and round budget. Ordinary completion freezes the chosen portfolio, requests two final logical trials and reports the maximum valid final reward, or null if none is valid. SRC-1: `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/coordinator/modes.py`; [RT-RTE-task-evolution](#rt-rte-task-evolution), [RT-RTE-branch-refinement](#rt-rte-branch-refinement), [RT-RTE-receipt-revision](#rt-rte-receipt-revision).

The executor boundary is an adapter call, not an optimizer tool permission. WildClaw submits the candidate root/hash to the runner under an adapter lock, so the coordinator's candidate thread pool does not imply simultaneous WildClaw execution. The local engine starts an OpenClaw gateway and agent in the task container, waits with a timeout, kills an overrun process and grades in a finally path. It performs Docker/shell effects with caller/container credentials. The enclosing host's tool grants, approvals and model behavior remain uninspected. SRC-1: `skilllift/skilllift/adapters/wildclawbench.py`, `skilllift_eval/runners/wildclaw_engine/run_batch.py`.

> bash_cmd=f"openclaw agent --session-id chat --timeout {timeout_seconds} --message '{safe_prompt}'",
> --- `skilllift_eval/runners/wildclaw_engine/run_batch.py`

Terminal outputs are a frozen portfolio, task evolution result, cell summary, task-run records and usage/attempt artifacts. Optimizer model text reaches code as proposals or scores; benchmark agents receive skill content through a loader. Neither channel establishes compliance. [RT-BAP-skill-delivery](#rt-bap-skill-delivery) separates downstream instruction authority from [RT-BAP-receipt-scoring](#rt-bap-receipt-scoring).

### Controls and forcing cases

Three control points carry different guarantees. First, `apply_portfolio_patch` stages a copy, checks and applies a unified diff, validates actual changed paths against planner scopes, rejects forbidden environment/dependency changes, preserves curated identities, validates skill structure and atomically moves the staged tree. Its owner is portfolio code; its strength is an **invariant** over accepted calls to that function, not semantic safety of the new instructions. Required external contracts are filesystem and Git behavior. Initial drafts, refinements and replay all call this gate; a custom generator can bypass bounded-edit request validation but not this gate when used by the inspected task coordinator. Separate category/tau2 skill generation does not traverse this portfolio gate. SRC-1: `skilllift/skilllift/portfolio/ref.py`, `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/coordinator/modes.py`; implementation conclusion status: wired; operation conclusion status: uninspected.

> _validate_changed_paths(changed_paths, scopes)
> _validate_forbidden_paths(changed_paths)
> --- `skilllift/skilllift/portfolio/ref.py`

Second, adapter/store fingerprints establish artifact association, not grader correctness. WildClaw checks task identity, portfolio hash, successful result status, configuration fields, contained artifact paths and loader-manifest hash. SkillsBench's task adapter additionally checks deployed files and loaded-skill receipts before committing reward or recovering an uncommitted trial. Owner: each adapter; strength: **protocol**, conditional on honest/accurate receipt producers and external benchmark results. Covered paths are task-adapter evaluation/recovery; direct subprocess calls and category drivers are not thereby covered. Source receipt checks cannot prove actual model-visible behavior or Docker isolation. SRC-1: `skilllift/skilllift/adapters/wildclawbench.py`, `skilllift_eval/runners/skillsbench_portfolio_adapter.py`; implementation conclusion status: wired; operation conclusion status: uninspected.

> if deployed.get("tree_hash") != portfolio.tree_hash or deployed.get("files") != expected_manifest:
>     raise ValueError("SkillsBench deployed-tree receipt does not match the candidate Portfolio")
> --- `skilllift_eval/runners/skillsbench_portfolio_adapter.py`

Third, recovery fingerprints and durable attempt markers distinguish logical evaluations from physical calls. Owner: coordinator/store; strength: **protocol**, not exactly-once remote execution. A started trial is offered to adapter recovery before a new attempt; outages leave audit markers and an indeterminate return rather than a permanent logical-cell result. Required external contract: adapter recovery must locate/authenticate completed effects. [RT-RTE-cell-recovery](#rt-rte-cell-recovery) states the scope. Implementation conclusion status: wired; operation conclusion status: uninspected.

The selected forcing cases are:

1. **Oracle tie and verifier failure.** Acceptance is not strictly increasing reward: a verifier advantage can promote a tied branch. Verifier errors can produce empty scores; Mode B skips when fewer than two scores survive. Therefore oracle improvement and complete rubric calibration are not universal completion guarantees. SRC-1: `skilllift/skilllift/coordinator/modes.py`.
2. **A genuinely changed Mode A refinement followed by resume.** `_refine_branch` replaces the branch portfolio but keeps the original candidate record. Accepted state stores round/candidate IDs; store replay uses that record's original patch. The inspected code does not persist a replacement candidate record in the refinement path. This yields a source-visible risk: the replayed parent can differ from the refined portfolio evaluated/promoted in memory, and later parent-hash checks or final-freeze checks can reject continuation. This is not an observed failure, and it only applies when refinement actually changes the tree and reaches acceptance. SRC-1: `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/portfolio/store.py`; [RT-CLM-refinement-replay](#rt-clm-refinement-replay).
3. **Alternate maintenance/consumption drivers.** SkillsBench category training and tau2 domain training/fusion have separate state machines, selectors and recovery conventions. Their final-skill/master-skill consumers are material routes, not equivalent evidence for task-portfolio guarantees. [RT-RTE-category-training](#rt-rte-category-training), [RT-RTE-domain-fusion](#rt-rte-domain-fusion).

The smallest inspection supports these cases, not an exhaustive security or performance audit. Added coverage beyond the boundary's initial reads includes the task coordinator's candidate/evaluation/recovery paths; mode coordinator's refinement and calibration paths; portfolio patch/replay; model request construction; planner and rubric-revision prompts; category training/test selection; tau2 domain training and master loader; and local WildClaw host launch. These are all SRC-1 at the frozen revision. Baseline algorithms, every batch launcher, all low-level bounded-edit internals, all injection-patch branches and provider/host internals remain uninspected here. Their omission prevents universal claims about every shipped command, approval mechanism, model grant or deployed isolation envelope.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LLMClient-backed model roles

Source-native identity: `LLMClient` for rubricator, skill generator and verifier. Representational form: distributed-parametric model behind a text/JSON transport. Storage substrate: remote provider machinery, uninspected; local client stores endpoint, model string, counters and API configuration, not weights. SRC-1: `skilllift/skilllift/llm_client.py`, `skilllift_eval/runners/skilllift_wildclaw.py`.

Parameters changing during operation: uninspected provider internals; inspected callers send inference requests and do not supply weight-update operations. Exact model version pinned: not established by a configured model ID; endpoint profiles identify the requested name, not a frozen weight revision. Mutable endpoint resolving to another model: possible under the external provider contract; target code does not authenticate model weights. Planner/generator/verifier role separation need not imply different underlying models. tau2 permits role-specific model IDs through its driver. No inference about absence of adaptation through retained text follows from weight opacity.

> payload = {
>     "model": self.model,
>     "messages": [
>         {"role": "system", "content": system_prompt},
>         {"role": "user", "content": user_prompt},
>     ],
>     "temperature": temperature,
> }
> --- `skilllift/skilllift/llm_client.py`

### Operative objects

#### RT-OBJ-portfolio-ref
Label: PortfolioRef candidate and frozen skill tree

Source-native identity: `PortfolioRef`, including task ID, root, tree/seed/config hashes and skill origins. Symbolic metadata is consumed by identity and validation rules; skill Markdown bodies are natural-language instruction content consumed by models. Substrate: filesystem tree, temporary branch workspaces and durable seed/final trees. This record identifies the runtime container, not every retained-content part or memory revision. SRC-1: `skilllift/skilllift/portfolio/ref.py`, `skilllift/skilllift/portfolio/store.py`.

> if portfolio_tree_hash(parent.root) != parent.tree_hash:
>     raise PortfolioError("parent portfolio hash no longer matches its directory")
> --- `skilllift/skilllift/portfolio/ref.py`

#### RT-OBJ-receipt
Label: Receipt binary scoring criteria

Source-native identity: `Receipt`, its version and signed-point rubrics. Natural-language rule text guides verifier interpretation; symbolic IDs/points/version and validation reports govern score calculation and admission. Substrate: Python schema objects, JSON receipts and experiment/state files. Runtime revision persists the selected receipt for later rounds. SRC-1: `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/baselines/prompts.py`.

> state.setdefault("receipt", receipt.to_dict())
> --- `skilllift/skilllift/coordinator/modes.py`

### Routes

#### RT-RTE-task-evolution
Label: Task portfolio successor selection

Endpoints/progression: CLI/runner → coordinator → anchor → planner/drafts/refinement → candidate benchmark evaluations → successor → receipt calibration → frozen portfolio/final trials. Owner: coordinator code, with model proposals and adapter-supplied reward. Context: public task, current portfolio, earlier plan/directions, scalar history and champion verifier feedback. State effects: accepted IDs, parent reward, prohibited novelty keys, receipt and next-round checkpoint. Action effects: local tree edits and delegated benchmark execution. SRC-1: `skilllift_eval/runners/skilllift_wildclaw.py`, `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/coordinator/modes.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TaskEvolutionResult with frozen portfolio, history, final rewards/score and metrics; runner emits summary and task records.
- Later read-back: store reconstructs accepted parent and reloads plans/receipt/history on re-entry; final portfolio is consumed by final trials.
- Delegated visibility: generator sees scoped task/portfolio guidance; adapter receives candidate root/hash and trial identity; benchmark host receives loader-produced skills, not necessarily optimizer history.
- Selection predicate: valid winner improves reward, or ties validated parent reward with strictly higher available verifier score.
- Invalidation or expiry: configuration/seed fingerprints reject incompatible reuse; stop predicates and configured budgets bound search, not durable artifact lifetime.
- Activation or effect: code selects a successor and submits portfolios for execution; model compliance and useful task behavior are unobserved.
- Evidence limits: unavailable tasks/graders/hosts prevent end-to-end reward and loading verification; refinements have the replay qualification in RT-CLM-refinement-replay.

Proposer: planner and generator models. Decider/veto: parse/patch validators, adapter validity, reward policy and coordinator selector. Human contribution: caller supplies task/configuration; this inspected path contains no per-candidate human approval step. Answer oracle: adapter-provided benchmark outcome, not the verifier model. Operating mode: bounded candidate experiment with verifier-only inner refinement and benchmark-backed outer selection. Trigger: nonterminal valid anchor or continued checkpoint. Proposed change: skill package content/new declared skills within scopes. Admission/rejection: staged validation plus successor predicate; failed proposals leave the parent. Recovery: durable evaluation cells and original candidate patches; rejected branches are not promoted. Guidance: public requirements, hypotheses, verifier criterion hits and scalar outcome history; what persists includes plans, patches, acceptance IDs and receipt, not model weights.

> if reward_spec.improves(winner.evaluation.reward, parent_reward):
>     accept_reason = "oracle_improved"
> elif (
>     reward_spec.validate(winner.evaluation.reward) == parent_reward
>     and winner_verifier is not None
>     and champion_verifier is not None
>     and winner_verifier > champion_verifier
> ):
> --- `skilllift/skilllift/coordinator/modes.py`

#### RT-RTE-branch-refinement
Label: Mode A bounded branch refinement

Endpoints: prepared branch → verifier → bounded-edit generator → portfolio patch gate → verifier → branch returned to outer evaluator. Owner: coordinator. Context/state: receipt and branch-local criterion hits shape the refined direction; separate calls supply explicit inputs rather than a retained agent conversation. SRC-1: `skilllift/skilllift/coordinator/modes.py`, `skilllift_eval/runners/bounded_edits_skill_generator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: branch with current portfolio, score/hits and refinement count, or unchanged branch on failures/decline.
- Later read-back: initial candidate record persists, but refined branch tree is not substituted into it in this path; see RT-CLM-refinement-replay.
- Delegated visibility: bounded editor receives selected snapshot files, task and direction; verifier receives converted skills and receipt.
- Selection predicate: below configured score threshold, within iteration budget; accept a refined tree only when its verifier score is at least current score.
- Invalidation or expiry: temporary round workspaces expire after evolve; patch/context errors terminate refinement locally.
- Activation or effect: a refined portfolio can reach outer benchmark evaluation; actual instruction activation remains unobserved.
- Evidence limits: zero oracle calls describes this inner method, not the surrounding round; verifier score improvement is not benchmark benefit.

Proposer: generator model, guided by missed positive and present negative criteria. Decider/veto: patch validator and verifier-score comparison in code. No human per-edit gate in the inspected method. Answer oracle: inapplicable — local rubric judgment is not a reference outcome. Mode: bounded verifier-only optimization. Trigger: valid branch with insufficient score. Admission: scope-preserving patch and nondecreasing verifier score; recovery/rollback: keep previous branch on rejected/error paths. Persisted guidance/result: original direction/draft record and diagnostics; refinement persistence is qualified above.

Working-context control: generator attempts the full scoped file set, but uses model-selected file IDs when there are more than 20 files, snapshot incompatibilities or overflow. Mandatory files remain; selected snapshot plus metadata replaces an overlarge evidence pack. Context-character checks can stop before editor or repair calls. Each call is an isolated explicit request; repair calls carry invalid output/error, not an entire benchmark trajectory. This resembles selected inputs in a frame with returned edits, not heap references that the model can dereference. SRC-1: `skilllift_eval/runners/bounded_edits_skill_generator.py`.

> if not self._fits_context(request[2], request[3]):
>     raise PortfolioContextLimitError(
>         "selected bounded edit files exceed the configured model context"
>     )
> --- `skilllift_eval/runners/bounded_edits_skill_generator.py`

#### RT-RTE-receipt-revision
Label: Mode B rank alignment and receipt admission

Endpoints: pre-round champion/candidate reward and verifier scores → tie-aware rank/criterion contrast → rubricator proposal → receipt validation → best tested alignment receipt. Owner: coordinator/rubricator code. Changes scoring instructions rather than benchmark task answers. SRC-1: `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/rubricator.py`, `skilllift/skilllift/baselines/prompts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected receipt and alignment, or old receipt/no alignment on insufficient evidence.
- Later read-back: state receipt is supplied to next-round scoring/refinement; experiment store retains scores, receipt versions and revision attempts.
- Delegated visibility: rubricator receives evidence package, public scalar/rank contrast, current criteria and validation feedback; prompt explicitly marks trajectory exclusion and forbids guessing hidden answers.
- Selection predicate: at least two valid portfolios and two common scores; revise below alignment threshold with available rubricator and remaining iterations; retain best measured alignment.
- Invalidation or expiry: validator rejects invalid revision; no sufficient score signal or model/output failure can preserve existing receipt.
- Activation or effect: admitted receipt changes later scoring input; interpretation fidelity and benefit are unobserved.
- Evidence limits: score/rank disagreement does not by itself prove a particular causal defect in a criterion, grader or data.

Proposer: rubricator model. Decider/veto: receipt validator, retry/keep-old policy and coordinator's best-alignment selection. Caller launch is not per-receipt human admission. Answer oracle: reused adapter benchmark reward; Mode B does not need a new benchmark call for each receipt trial. Trigger/objective: verifier/oracle rank misalignment; proposed change: whole receipt with declared rubric removals and version increment. Recovery: two validation attempts, old receipt on rejection, best-tested receipt on revision failure. Guidance requests evidence-bounded diagnosis and reusable binary rules; persisted result is receipt text/points plus attempt/diff/diagnostic artifacts.

> if attempt.accepted:
>     return candidate
> previous_payload = payload
> previous_report = report
> --- `skilllift/skilllift/rubricator.py`

> - A scalar score gap alone is never enough to create a criterion; when visible evidence cannot explain it, preserve the receipt and record no_visible_explanation.
> --- `skilllift/skilllift/baselines/prompts.py`

Theory account: receipts expose localized scoring rules and assumptions about what visible skill content predicts benchmark reward. Their rules are supplied to verifier decisions; the revision prompt requests criticism of weak/missing criteria against score contrast and a changed receipt. That request is not proof of faithful model diagnosis. `theory-builder conditions 1–4`: condition 1 implementation conclusion status: wired — whole criteria are inspectable/replacable; condition 2 implementation conclusion status: wired — scoring uses receipt content; condition 3 doctrine conclusion status: claimed — prompt requests content-directed diagnosis, but actual blame placement and justified revision are unobserved; condition 4 implementation conclusion status: wired — selected revisions feed further scoring/rounds, while criticism quality remains unestablished. All four operation conclusion statuses: uninspected. Addressability: IDs, text, signed points and removals localize revision below whole-receipt granularity. Persistence: rounds and task-run re-entry through state/experiment files; later consumption of diagnostic rationale is uninspected. Learning: useful future capacity change and attribution unestablished; selection/alignment alone do not prove it. Reflection: wired feedback about the optimizer's own verifier-ranking policy can change its later policy, but accurate self-representation is unobserved. Reflective theory builder: not established because condition 3's actual criticism remains unobserved. Autonomous theory builder: computational proposal/admission/iteration is wired, but every internal theory-building operation is not established given that same criticism gap. No exercised self-improvement claim follows without observed downstream causal dependence and independently assessed objective outcomes.

#### RT-RTE-cell-recovery
Label: Logical cell recovery and infrastructure retries

Endpoints: logical evaluation fingerprint → result/attempt lookup → adapter recovery → retry → durable result or indeterminate return. Owner: coordinator/store. Effects: attempts and benchmark execution may repeat; valid reward closes the cell. SRC-1: `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/portfolio/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: cached/recovered/valid new CandidateEvaluation, or infrastructure failure after consecutive-failure fuse.
- Later read-back: valid cell results and physical-attempt markers are reloaded on future evolve; indeterminate fuse result does not permanently close a cell.
- Delegated visibility: adapter gets task/portfolio/trial ID, phase and attempt; recovery visibility depends on adapter artifacts.
- Selection predicate: matching fingerprint and valid reward; recover started attempts before creating fresh physical calls.
- Invalidation or expiry: incompatible fingerprints reject reuse; fresh invocation can retry an indeterminate cell.
- Activation or effect: recovery can avoid execution or reissue a benchmark trial; exactly-once external effects are not guaranteed.
- Evidence limits: inspected adapter contracts cannot establish live remote completion, infrastructure availability or atomicity across crashes.

> # Fuse tripped. The indeterminate outcome is deliberately NOT
> # persisted as the cell's final result: once the outage is fixed, a
> # later resume retries this cell with a fresh fuse. The attempt
> # markers remain as the audit trail of every physical oracle call.
> --- `skilllift/skilllift/coordinator/task.py`

#### RT-RTE-category-training
Label: SkillsBench category training and final-skill testing

Endpoints: category CLI → batch training → verifier-guided skill updates → task-by-skill oracle matrix → selected batch winner → optional fusion → final_skills → held-out testing. Owner: SkillLiftSkillsBenchRunner, a separate driver. Context/state: category batches, skills/receipt objects, round markers and config/skill hashes. SRC-1: `skilllift_eval/skillsbench_cli.py`, `skilllift_eval/runners/skilllift_skillsbench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: train/test summaries and final category skill files.
- Later read-back: resume reloads completed round skills/receipt; testing reads final_skills and compatible score markers.
- Delegated visibility: updater sees skill/receipt/score; subprocess benchmark receives materialized candidate per task; test receives final category tree.
- Selection predicate: inner update requires changed key and nondecreasing verifier score; outer selector uses aggregate oracle evidence, verifier values and hashes; best completed round supplies final batch winner.
- Invalidation or expiry: resume predicates check config and skill fingerprints; outer-round/threshold bounds stop training.
- Activation or effect: final trees are submitted to later tests; execution and benefit remain unobserved.
- Evidence limits: task-portfolio patch and receipt-loading guarantees must not be projected onto this separate path; detailed fusion admission and every test reuse branch remain uninspected here.

Proposal/decision: models initialize/update skills and revise receipts; code validates receipt proposals, selects winners and writes final content. Human role: category/config selection, not demonstrated per-content approval. Answer oracle: per-task benchmark reward matrix aggregated per skill. Mode: bounded batch curriculum, followed by separate held-out test. Trigger: configured batches/rounds; proposed changes: skill bodies and receipts. Rejection/rollback: Mode A keeps old skill on decline; round markers enable recovery. Final fusion has a distinct model consumer whose detailed correctness gate is uninspected, preventing a universal verified-final-content claim.

> best_round = min(completed_rounds, key=_round_winner_sort_key)
> winner_id = best_round["winner_skill_id"]
> --- `skilllift_eval/runners/skilllift_skillsbench.py`

#### RT-RTE-domain-fusion
Label: tau2 domain training, master fusion and held-out read-back

Endpoints: domain driver → train clusters → verifier/oracle contrast and updates → cluster skill artifacts → fusion model → MASTER_SKILL bundle → held-out loader/task runner. Owner: shipped domain driver and tau2 runner. Context/state: public domain policy, task-suite overview, role-specific models, skill/receipt checkpoints and round metrics. SRC-1: `scripts/skilllift_tau2_run_domain.py`, `skilllift_eval/runners/skilllift_tau2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: cluster/fusion/test artifacts and domain summary.
- Later read-back: checkpoints restore skills/receipt; the domain driver supplies each cluster's final training artifact, whose writer exports every current skill; fusion loads every skill metadata entry and its SKILL.md body, not only the oracle-ranked winner; held-out evaluation loads MASTER_SKILL and matching bundle.
- Delegated visibility: fusion sees train cluster skill material and domain/action guidance; held-out task runner gets policy/skill prompt context, model controls, seed and max steps.
- Selection predicate: training tests best oracle reward against threshold and revises receipt on misalignment; cluster-to-fusion loading iterates all skill metadata entries without consulting the separately saved aggregate oracle rank, so lower-ranked current skills can enter the fusion prompt; fusion parse/validation accepts a nonempty fenced skill body; held-out loader checks domain/single-skill identity, exact body equality and hashes.
- Invalidation or expiry: master content/hash mismatch rejects loading; separate resume shortcuts reuse existing artifacts/scores and are not the task coordinator's logical-cell protocol.
- Activation or effect: retained MASTER_SKILL becomes held-out prompt-context input; actual behavior and generalization are unobserved.
- Evidence limits: sibling tau2 implementation is unavailable; whole domain resumption is not proven hash-complete by inspecting the master loader alone; detailed markdown-update helper admission is uninspected here.

Proposal/decision: computational role-specific models propose initial/update/receipt/fusion content; Python chooses rounds, rejects malformed fusion and validates master identity. Human contribution: domain/config/problem supply; no inferred human approval of each revision. Answer oracle: tau2 simulation reward aggregated across cluster tasks, with external grader correctness unresolved. Mode: bounded train clusters, fusion, held-out consumption. Trigger/change: scheduled training and low alignment drive receipt/skill revisions; fusion builds domain instructions from retained train products. Recovery: cluster checkpoints and artifact/score reuse; fusion parse failures retain prompt/raw-output failure artifacts and raise. Guidance persists as cluster/master skill text and receipts; it is not a production-code modification. Detailed theory properties of generated domain rules remain for specialist inspection rather than inferred from their output name.

The final-artifact handoff and all-skill export/loading are SRC-1 implementation evidence: `scripts/skilllift_tau2_run_domain.py`, `skilllift_eval/runners/skilllift_tau2.py`. The training score can stop the cluster loop, but it is not a winner-only quality gate on fusion inputs. This corrects the earlier winner-only lineage characterization; it leaves structural fusion admission and held-out delivery intact.

> cluster_artifact_paths.append(cluster_result["cluster_artifact_path"])
> --- `scripts/skilllift_tau2_run_domain.py`

> "cluster_level_skill_contents": {
>             key.token(): {
>                 "files": {"SKILL.md": skill.files.get("SKILL.md", "")},
>                 "entrypoint": skill.entrypoint,
>             }
>             for key, skill in sorted(skills.items())
> --- `skilllift_eval/runners/skilllift_tau2.py`

> for skill_key, metadata in metadata_by_key.items():
>             files = (content_by_key.get(skill_key) or {}).get("files") or {}
>             skill_text = str(files.get("SKILL.md") or "")
> --- `skilllift_eval/runners/skilllift_tau2.py`

> if str(skill.get("content") or "") != master_skill_content:
>     raise ValueError("MASTER_SKILL.md and best_skill_bundle content disagree")
> --- `skilllift_eval/runners/skilllift_tau2.py`

### Claims

#### RT-CLM-mode-a
Label: Claimed verifier-only inner mode

Claimed operation: Mode A performs branch-local refinement without benchmark oracle calls. Source doctrine and inspected method agree at this inner scope; outer rounds still evaluate candidates. SRC-1: `skilllift/skilllift/coordinator/modes.py`.

> """Mode A: verifier-guided branch-local refinement, zero oracle calls."""
> --- `skilllift/skilllift/coordinator/modes.py`

#### RT-CLM-refinement-replay
Label: Refinement record and durable replay mismatch risk

Implementation finding, not reported execution: accepted refined branch retains original candidate record, while parent reconstruction applies the recorded patch. This qualifies resume-stable successor identity. The affected boundary is task Mode A with actual accepted refinement, not category/tau2 paths or unchanged drafts. SRC-1: `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/portfolio/store.py`.

> current = _Branch(
>     record=current.record,
>     portfolio=refined,
>     verifier_score=refined_score.normalized_score,
>     criterion_hits=refined_score.criterion_hits,
>     refinement_attempts=current.refinement_attempts + 1,
> )
> --- `skilllift/skilllift/coordinator/modes.py`

> result = apply_portfolio_patch(
>     parent,
>     record.patch,
>     destination,
>     target_scope=record.direction.target_scope,
>     new_skill_names=record.new_skill_names,
> )
> --- `skilllift/skilllift/portfolio/store.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-delivery
Label: Candidate and retained skill instruction delivery

Consumer: external benchmark agent. Channel: portfolio loader/materialized skill tree, or tau2 skill/policy prompt context. Force: natural-language guidance interpreted by host/model, not an enforced capability restriction. Horizon: candidate/final trials, and retained category/master skill reuse in later tests. SRC-1: `skilllift/skilllift/adapters/wildclawbench.py`, `skilllift_eval/runners/skillsbench_portfolio_adapter.py`, `skilllift_eval/runners/skilllift_tau2.py`. Delivery is wired; actual instruction activation and causal task benefit are unobserved. This does not certify the external host's tool grants or sandbox envelope.

> context = Tau2SkillLoader(
>     artifact_root=config.run_root / "tau2_prompt_context" / "test_eval" / domain / task_id
> ).prepare(
>     bundle=bundle,
>     domain=domain,
>     task_ids=[task_id],
>     domain_policy=domain_policy,
> )
> --- `skilllift_eval/runners/skilllift_tau2.py`

#### RT-BAP-receipt-scoring
Label: Receipt-mediated verifier and update guidance

Consumer: verifier model, then generator and coordinator through interpreted criterion hits/scores. Channel: receipt rules in explicitly constructed model requests and symbolic score comparisons. Force: requested model judgment plus enforced code thresholds; no semantic correctness guarantee. Horizon: inner refinement, subsequent outer rounds and task checkpoint re-entry. SRC-1: `skilllift/skilllift/baselines/prompts.py`, `skilllift/skilllift/coordinator/modes.py`.

> "You will receive a task description, a candidate skill, and a receipt containing binary rubrics. "
> "You must not invent hidden assumptions beyond the provided task, skill and rubrics. "
> "Evaluate the candidate skill against each rubric criterion in the given order. "
> --- `skilllift/skilllift/baselines/prompts.py`

## Annotations

none
