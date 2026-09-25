---
type: types/agentic-system-analysis-result.md
description: "SkillLift flagship portfolio improvement plane: rubric-guided edits, oracle promotion, memory read-back and bounded recovery findings"
run-id: AAS-2026-09-25-skilllift-01
system: SkillLift
run-date: "2026-09-25"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: subsystem-only
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Retained task-local portfolio content, rubric versions, plans, scalar evaluation history, candidate patches and resume state accumulated by the flagship portfolio coordinator, including its superproject-owned WildClawBench and SkillsBench delivery paths. Static seed authoring, excluded benchmark internals, remote model internals and reuse after final export are outside."
  axes:
    storage_substrate: {assessment: known, basis: wired, values: [files, in-memory], records: [OBJ-2, OBJ-3, OBJ-4, OBJ-5], note: "Directory trees and JSON/diff files back live Python objects and branch-local refinements; Git is source provenance, not an operative memory store."}
    representational_form: {assessment: not-determinable, basis: null, values: [], records: [OBJ-2, OBJ-3, OBJ-4], note: "Natural-language and symbolic forms are established. Arbitrary UTF-8 portfolio assets imported from excluded benchmark trees prevent a complete payload classification; a text container alone does not classify every consumed asset."}
    lineage: {assessment: known, basis: wired, values: [imported, other-compiled, trace-extracted], records: [OBJ-2, OBJ-3, OBJ-4, RTE-2, RTE-3], note: "Native seed imports, deterministic patch/history compilation, and automatic derivation from verifier/evaluation events. Manual source authoring predates the memory boundary."}
    behavioral_authority: {assessment: known, basis: afforded, values: [instruction, knowledge, learning, ranking, routing, validation], records: [OBJ-2, OBJ-3, OBJ-4, OBJ-5, RTE-2, RTE-3, RTE-4, RTE-5], note: "Rubrics validate and rank; plans and outcomes guide learning and routing; state validates replay identity. Skill instructions reach the owned context hook or an afforded external read route. Executable auxiliary files are available, but their invocation is not established here."}
    write_agency: {assessment: known, basis: wired, values: [automatic], records: [RTE-2, RTE-3, RTE-5], note: "Model and deterministic code write task memory. Operator task/configuration choices are not a manual memory-edit workflow."}
    curation_operations: {assessment: known, basis: wired, values: [evolve, invalidate, promote, synthesize], records: [RTE-2, RTE-3, OBJ-4], note: "Revise portfolio/rubric content; withdraw removed criteria while retaining history; promote winners; synthesize hypotheses and criteria. Admission-time duplicate rejection is not deduplication of retained entries."}
    read_back_direction: {assessment: known, basis: afforded, values: [pull, push], records: [RTE-1, RTE-2, RTE-3, RTE-4, RTE-5], note: "Controllers request saved state and results; prompt assemblers automatically supply selected memory. WildClaw explicitly affords the external task agent a read-tool pull, whose execution is unobserved."}
    read_back_signal: {assessment: known, basis: wired, values: [coarse, identifier, inferred-judgment], records: [RTE-2, RTE-3, RTE-4], note: "Whole history/portfolio supply, path and criterion-ID matching, and an LLM optional-file selector. Requested state lookup is not counted as identifier-based push."}
    trace_learning: {assessment: known, basis: wired, values: ["yes"], records: [RTE-2, RTE-3], note: "Evaluation and verifier events feed retained plans, patches and rubric revisions consumed in later rounds; task execution trajectories themselves are excluded from revision evidence."}
    trace_source: {assessment: known, basis: wired, values: [event-streams], records: [OBJ-4, RTE-2, RTE-3], note: "The qualifying signal is scalar evaluation outcomes and verifier scoring events; it is not the retained benchmark trajectory or arbitrary execution logs."}
    learning_scope: {assessment: known, basis: wired, values: [per-task], records: [RTE-1, RTE-2, RTE-3, RTE-5], note: "Each evolve(task_id) has its own seed, plans, history, accepted chain and state. Batch iteration does not import another task's evolved content."}
    learning_timing: {assessment: known, basis: wired, values: [staged], records: [RTE-2, RTE-3], note: "Framework scoring/evaluation stages alternate with plan, patch and receipt revision stages before another trial or round; no in-rollout memory update is established."}
    distilled_form: {assessment: known, basis: wired, values: [natural-language, symbolic], records: [OBJ-2, OBJ-3, OBJ-4, RTE-2, RTE-3], note: "The inspected transformation outputs are textual skill/criterion/hypothesis content and executable text patches plus structured criteria, path scopes and outcomes. No parameter-training transformation is present on these routes."}
    faithfulness_tested: {assessment: not-determinable, basis: null, values: [], records: [RTE-4], note: "Receipt checks establish supplied content identity, and evaluation returns reward. No retained execution experiment testing dependence on recalled content was commissioned or inspected."}
---

# SkillLift agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-skilllift-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/skilllift.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-skilllift-01/memory-report.md`

**Memory analysis report SHA-256:** `3d87bb3c117c5a2c8302de03cfd6c70d37fc9d4b9147bd1a4c819c7f3e94fef1`

## Boundary and evidence

Evidence basis: implementation and source claims in SkillLift commit `599358b4d4c4a27c0e004df8228ab93026600653`, frozen on 2026-09-25; no target execution, observed rollout or causal experiment. This analysis characterizes the flagship portfolio improvement plane, not every algorithm in the repository. It includes SkillLiftPortfolioCoordinator, inherited task coordination, rubric and verifier calls, bounded candidate edits, PortfolioStore, and superproject-owned WildClawBench/SkillsBench adapters and their native callers. This is a subsystem-only builder or improvement plane operating bounded benchmark experiments.

Excluded comparison algorithms, legacy non-portfolio training, tau2 routes and human-skill baselines prevent conclusions about all repository modes. External Gitlinks WildClawBench and skillsbench, container images, OpenClaw/OpenHands/BenchFlow internals, task datasets and remote provider internals are outside the source allowlist; this prevents certifying benchmark correctness, full tool grants, deployed isolation, model parameter identity or real task success. The inspected superproject implementation of rollout launch and result admission remains in scope. No paper, prior review, ingest prose or cross-system analysis supplies evidence. The purpose is source-grounded characterization and a reusable exact record, without adoption or transfer advice.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/WalteR-MittY-pro/SkillLift`; access root `/home/zby/llm/commonplace/related-systems/WalteR-MittY-pro--SkillLift` | `599358b4d4c4a27c0e004df8228ab93026600653` | Implementation: coordinator, portfolio, rubric/verifier/model clients, native runners, adapters and superproject rollout/grading glue. Doctrine/design and reported operation: README, separately treated. | Commit-addressed blobs only, selected ranges below; no worktree evidence | `skilllift/skilllift/coordinator/modes.py:87-307,357-443,533-755`; `skilllift/skilllift/coordinator/task.py:260-344,476-727`; `README.md:14-33,100-118`; further anchors on canonical records | External Gitlinks and services excluded; no retained candidate-linked execution or intervention inspected. Prevents upgrading wiring or README figures to observed operation or causal improvement. |

## Shared records

### Components

CMP-1 — SkillLiftPortfolioCoordinator with TaskPortfolioCoordinator. Symbolic Python control over finite per-task search, adapter evaluation and persisted state. Implementation conclusion status: wired. Defaults cap three rounds and three branches, with two final trials; native callers configure selected thresholds/concurrency but inherit these round/final constraints. Source: SRC-1 `skilllift/skilllift/coordinator/task.py:35-67,260-344`; `skilllift_eval/runners/skilllift_wildclaw.py:198-212`; `skilllift_eval/runners/skilllift_skillsbench_tasks.py:137-173`.

>     def __post_init__(self) -> None:
>         if not 1 <= self.max_rounds <= 3:
>             raise ValueError("max_rounds must be between 1 and 3")
>         if not 1 <= self.max_candidates_per_round <= 3:
>             raise ValueError("max_candidates_per_round must be between 1 and 3")
>         if self.candidate_concurrency < 1:
>             raise ValueError("candidate_concurrency must be positive")
>         if not 1 <= self.max_consecutive_infra_failures <= 5:
>             raise ValueError("max_consecutive_infra_failures must be between 1 and 5")
>         if self.final_trials != 2:
>             raise ValueError("the locked protocol requires exactly two final trials")
> --- `skilllift/skilllift/coordinator/task.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

CMP-2 — Framework rubricator/planner, verifier and skill-generator model roles, including bounded-editor file selection. Distributed-parametric processing behind LLMClient; their prompts, parsers and callers are symbolic/natural-language. Parameter-change finding: wired inference requests expose model/messages/temperature, not training; provider-internal changes: uninspected. Identity finding: wired mutable endpoint plus configured model identifier, not an exact weight digest. WildClaw's roles share the endpoint profile; SkillsBench can supply a separate framework_model. Role separation is computational responsibility, not independent model evidence. Source: SRC-1 `skilllift/skilllift/llm_client.py:42-177`; `skilllift_eval/runners/skilllift_wildclaw.py:165-196`; `skilllift_eval/runners/skilllift_skillsbench_tasks.py:99-133`.

>         payload = {
>             "model": self.model,
>             "messages": [
>                 {"role": "system", "content": system_prompt},
>                 {"role": "user", "content": user_prompt},
>             ],
>             "temperature": temperature,
>         }
> --- `skilllift/skilllift/llm_client.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

CMP-3 — Benchmark adapter and external rollout/grading interface. Superproject Python adapters copy/deploy candidate portfolios, invoke a runner or subprocess and admit a fingerprinted finite reward. Actual external agent scheduling/tool decisions and task graders remain delegated. Source: SRC-1 `skilllift/skilllift/adapters/wildclawbench.py:276-404`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py:97-169,245-298`. Implementation conclusion status: wired.

CMP-4 — External OpenClaw/OpenHands rollout models and possible benchmark judge model. The inspected WildClaw runner configures the image model from the same model argument, resolves judge environment, starts OpenClaw gateway and agent; SkillsBench passes model/agent/sandbox arguments. Parameter changes and exact resolved versions: uninspected at provider/host internals. Configured identifier routing: wired. The source cannot establish that all grading is deterministic: WildClaw executes task-supplied grading Python and passes judge configuration. Source: SRC-1 `skilllift_eval/runners/wildclaw_engine/run_batch.py:561-627`; `skilllift_eval/runners/skillsbench_adapter.py:16-58`; `skilllift_eval/runners/wildclaw_engine/grading.py:17-47`.

### Operative objects

OBJ-1 — PublicTask and task identity. Imported task text, evidence_ref and task_id; natural-language text with symbolic identifiers. Sources: SRC-1 `skilllift/skilllift/portfolio/prompts.py:23-26`; `skilllift/skilllift/adapters/wildclawbench.py:221-228`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py:63-90`. Public task delivery is wired; source truth and hidden benchmark answer correctness are uninspected. The task itself is static input, not accumulated memory.

OBJ-2 — Skill portfolio files and PortfolioRef. A task-specific directory tree containing SKILL.md, scripts, references and permitted inherited assets, with tree/seed/config hashes and curated/generated identities. Natural-language instructions and symbolic code/metadata can coexist; opaque inherited assets require the specialist's scoped uncertainty. Source: SRC-1 `skilllift/skilllift/portfolio/ref.py:42-89,113-145,164-256`; `skilllift/skilllift/portfolio/prompts.py:291-297,345-357`. Content is copied, edited and passed to later model/harness consumers; correct application and benefit remain uninspected.

OBJ-3 — Receipt rubric criteria and versions. Individually identified binary criteria, signed integer points, bounds, metadata and explicit removals. This is a revisable assessment representation, not a benchmark answer. Source: SRC-1 `skilllift/skilllift/rubricator.py:114-163,481-535`; `skilllift/skilllift/baselines/prompts.py:28-59,90-188`. Formulation of proposed requirements is afforded; JSON production/validation and scoring consumption are wired. Semantic relevance, binary evaluability and criticism quality are not guaranteed by parser acceptance.

>     if candidate.version != old_receipt.version + 1:
>         errors.append("receipt_version_must_increment_by_one")
>     old_ids = {rubric.rubric_id for rubric in old_receipt.rubrics}
>     new_ids = {rubric.rubric_id for rubric in candidate.rubrics}
>     removed_ids = old_ids - new_ids
>     declarations = candidate.removed_rubrics
>     declared_ids = {item.get("rubric_id") for item in declarations if isinstance(item, dict)}
>     if removed_ids != declared_ids:
>         errors.append("removed_rubric_declaration_missing")
>         messages.append(
>             f"declared removed rubrics {sorted(declared_ids)} do not match actual removals {sorted(removed_ids)}"
> --- `skilllift/skilllift/rubricator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

OBJ-4 — Candidate evaluation, scalar history, SearchPlan and diagnostics container. It retains outcome/candidate/direction identifiers, rewards, acceptance and model-proposed hypotheses/reasons. Its constituent epistemic parts receive separate overlay treatment below. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:30-119,280-331`; `skilllift/skilllift/coordinator/modes.py:239-303`. Status: wired retention and subsequent prompt supply; this does not establish that a hypothesis explains an outcome.

OBJ-5 — PortfolioStore checkpoint and final-reference state. Files encode seed/config identity, candidate patches, round plans/results, accepted-candidate IDs, receipt, trial attempts and frozen final portfolio. It controls resume and cached evaluation return as well as audit. Source: SRC-1 `skilllift/skilllift/portfolio/store.py:73-156,158-192,218-267,355-402`; `skilllift/skilllift/coordinator/task.py:573-727`. Status: wired; persisted initial patches do not by themselves preserve later branch refinement.

OBJ-6 — SearchPlan requirements, directional hypotheses and cross-skill rationale, an individually addressable part of OBJ-4. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:30-81,280-331`. Natural-language claims in structured JSON; model-produced and parsed, saved in plans/directions, supplied to future planner and editor. Intended to say which behavior/skill change addresses the task and why. Hypothesis validity remains uninspected; delivery and persistence are wired.

OBJ-7 — Verifier criterion hits, evidence and rationale, an individually addressable part of OBJ-4. Source: SRC-1 `skilllift/skilllift/verifier.py:62-86,126-155`; `skilllift/skilllift/baselines/prompts.py:191-230`. Model assertions or lexical estimates that a named criterion is met; symbolic Boolean/numeric results and natural-language reasons. Parsing checks keys/types; it does not independently validate their truth. Numeric score/rank derivation is wired within declared scoring semantics.

OBJ-8 — Benchmark reward/result identity and scalar outcomes, an individually addressable part of OBJ-4. Source: SRC-1 `skilllift/skilllift/coordinator/task.py:117-174,592-705`; `skilllift/skilllift/portfolio/prompts.py:85-119`; `skilllift/skilllift/adapters/wildclawbench.py:333-404`; `skilllift_eval/runners/skillsbench_adapter.py:334-374`. Imported symbolic result of external task execution/checks, reduced to reward/delta/rank/validity/acceptance for later history. Claims about this evaluation are limited by external check validity; identifiers/hashes protect association, not truth.

OBJ-9 — Receipt criterion requirements and signed-point structure, an individually addressable part of OBJ-3. Source: SRC-1 `skilllift/skilllift/rubricator.py:114-163,481-535`; `skilllift/skilllift/baselines/prompts.py:28-59`. Requirements function as evaluation policy; any claim that a criterion predicts useful task behavior is a proposed assessment hypothesis, not an established general law. IDs expose parts to revision and explicit removal.

OBJ-10 — Receipt diagnosis metadata and removed-criterion reasons, an individually addressable part of OBJ-3. Source: SRC-1 `skilllift/skilllift/baselines/prompts.py:153-184`; `skilllift/skilllift/rubricator.py:139-163,501-535`. Natural-language explanations and references in JSON; diagnosis is requested but optional, while a declared removal requires a nonempty reason and evidence list. Whole-receipt prompts can later deliver these reasons. They are candidate assertions, not validated explanations.

### Routes

RTE-1 — Flagship initialization, baseline and rounds. Trigger/principal: operator CLI or native batch calls evolve(task_id), selecting model, task and configuration. Next-step owner: symbolic coordinator, with model-owned proposal content. It imports public task and seed, checks task identities, hashes algorithm/config/reward specification, loads state, reconstructs parent and evaluates an anchor if no reward is saved. An indeterminate anchor freezes the seed and ends; a terminal untouched anchor ends without final trials. Otherwise it invokes the remaining routes, freezes a final portfolio, runs exactly two final cells and reports the maximum valid reward. Effects stay in local run files and delegated benchmark execution. Source: SRC-1 `skilllift_eval/cli.py:590-624`; `skilllift_eval/runners/skilllift_wildclaw_tasks.py:62-125,128-152`; `skilllift/skilllift/coordinator/task.py:260-344,707-727`. Implementation conclusion status: wired; deployed operation: uninspected. The result's best-of-two value is a protocol statistic, not an unbiased expected success estimate.

>             frozen = self.store.freeze_final(task_id, parent)
>             final_rewards = []
>             for final_index in range(self.config.final_trials):
>                 evaluation = self._evaluate_cell(
>                     task_id,
>                     frozen,
>                     reward_spec,
>                     algorithm_hash,
>                     phase="final",
>                     final_index=final_index,
>                 )
>                 if evaluation.is_valid:
>                     final_rewards.append(reward_spec.validate(evaluation.reward))
>             final_score = max(final_rewards) if final_rewards else None
>             state.update(
>                 status="completed",
>                 cohort=state.get("cohort") or "adapted_budget",
>                 final_rewards=final_rewards,
>                 final_score=final_score,
>             )
> --- `skilllift/skilllift/coordinator/task.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

RTE-2 — Candidate generation and Mode A verifier-guided refinement. Trigger: a nonterminal round; planner receives current portfolio, prior plans/directions/outcomes and current verifier feedback. Generator receives selected direction and scoped current files, produces structured bounded edits transformed into a unified diff, and the portfolio code checks scope, hashes, layout and forbidden paths before staging the changed tree. Invalid edits can be rejected; parent stays intact. Each branch is scored under the current frozen receipt, refined until threshold/budget, and only a nondecreasing normalized verifier score replaces that branch's working portfolio. Model output and optional selector determine proposal content; deterministic checks and score predicates veto. A missing verifier client or malformed non-agent_skill verifier output uses lexical fallback, while other verifier errors can leave scores unavailable. Direct callback generators/planners are alternate proposal paths through the coordinator's portfolio validator; they need not use the native bounded-editor contract. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:125-175,309-443,445-531`; `skilllift/skilllift/coordinator/task.py:476-544`; `skilllift/skilllift/verifier.py:13-59,89-123,162-170`; `skilllift_eval/runners/bounded_edits_skill_generator.py:68-150`; `skilllift/skilllift/portfolio/ref.py:164-256`. Implementation conclusion status: wired. Guarantee owner is the local validator/score branch, strength invariant only over checked file edits and numeric comparisons; no semantic or sandbox guarantee follows.

>             refined_score = self._branch_score(
>                 task_spec, refined, receipt, mode="mode_a", stage="mode_a_refinement"
>             )
>             if refined_score is None:
>                 break
>             if refined_score.normalized_score >= (current.verifier_score or 0.0):
>                 current = _Branch(
>                     record=current.record,
>                     portfolio=refined,
>                     verifier_score=refined_score.normalized_score,
>                     criterion_hits=refined_score.criterion_hits,
>                     refinement_attempts=current.refinement_attempts + 1,
>                 )
>             else:
>                 break
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>     try:
>         payload = llm_client.call_json(system, user, temperature=0.0)
>         return parse_verifier_output(payload, receipt, skill.key)
>     except (LLMOutputError, VerifierError) as exc:
>         if skill_format == "agent_skill":
>             raise
>         return fallback_score_skill(skill, receipt, f"fallback_invalid_verifier_output: {exc}")
> --- `skilllift/skilllift/verifier.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

> def _fallback_hit(skill_text: str, criterion: str, points: int) -> bool:
>     tokens = [token for token in _words(criterion) if len(token) >= 4]
>     if not tokens:
>         return points > 0
>     matches = sum(1 for token in tokens if token in skill_text)
>     ratio = matches / max(1, len(tokens))
>     if points > 0:
>         return ratio >= 0.2 or any(word in skill_text for word in ["verify", "validate", "check", "deadline"])
>     return ratio >= 0.35 and not any(word in skill_text for word in ["avoid", "never", "do not", "must not"])
> --- `skilllift/skilllift/verifier.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>         if not changed_paths:
>             raise PortfolioError("candidate patch does not change the portfolio")
>         _validate_changed_paths(changed_paths, scopes)
>         _validate_forbidden_paths(changed_paths)
> 
>         previous_names = _portfolio_skill_names(parent.root)
>         candidate_names = _portfolio_skill_names(work_root)
>         candidate_assets = _portfolio_shared_paths(work_root)
>         if candidate_assets != parent.curated_asset_paths:
>             raise PortfolioError(
>                 "curated shared asset identities cannot be deleted, renamed, or added: "
>                 f"actual={sorted(candidate_assets)}, expected={sorted(parent.curated_asset_paths)}"
>             )
>         added_names = candidate_names - previous_names
>         if added_names != declared_new:
>             raise PortfolioError(
>                 f"new skill directories {sorted(added_names)} do not match declaration {sorted(declared_new)}"
>             )
>         missing_curated = parent.curated_skill_names - candidate_names
>         if missing_curated:
>             raise PortfolioError(f"curated skill identities cannot be deleted or renamed: {sorted(missing_curated)}")
> --- `skilllift/skilllift/portfolio/ref.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

Guidance on this route consists of task requirements, portfolio text/code, directional hypotheses, reasons and rubric hits. Directions claim that changing a specified capability will improve the task solution; receipt criteria claim a useful skill should exhibit named behavior. Formulation: afforded by explicit hypothesis/requirement fields and prompts. Operative delivery and numeric use: wired; faithful semantic application: uninspected. Content-directed criticism: afforded by falsifiable directions and missing/forbidden behavior feedback, not established by mere score selection. Resulting edits/changed reliance: wired conditionally. Improved capacity attributable to holding and criticizing a theory: uninspected. Addressability: wired file/path/criterion/direction granularity; quality and completeness of assumptions are uninspected. Reasons persist in plans and directions and are supplied to later planning/generation; this is not evidence that the model uses them soundly.

>         user = "\n\n".join([
>             f"[Public Task: {task.evidence_ref}]\n{task.text}",
>             f"[Portfolio Manifest]\n{_json(_manifest_with_origins(portfolio))}",
>             f"[Current Portfolio Files]\n{evidence}",
>             f"[Previous SearchPlan]\n{_json(previous_plan.to_dict() if previous_plan else None)}",
>             f"[Prior Direction History]\n{_json([item.to_dict() for item in direction_history])}",
>             f"[Scalar SearchHistory]\n{_json(serialize_search_history(history))}",
>             feedback_section,
>             "[Output Contract]\n"
>             '{"receipt_version": int, "rubrics": [{"rubric_id": str, "requirement": str, '
>             '"evidence_refs": [str]}], "directions": [{"direction_id": str, "rubric_id": str, '
>             '"hypothesis": str, "capability": str, "target_scope": [str], '
>             '"cross_skill_rationale": str|null, "evidence_refs": [str], "novelty_key": str}]}.',
> --- `skilllift/skilllift/portfolio/prompts.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

RTE-3 — Mode B rubric revision and candidate promotion. Trigger: branch benchmark rewards and verifier scores; owner: coordinator plus model rubricator. Candidate promotion is chosen before rubric alignment: maximal valid benchmark reward wins, verifier breaks candidate ties, and a reward strictly above parent or equal parent reward with a higher verifier score permits replacing parent. Mode B freezes the pre-round champion and valid candidates, reuses their rewards, scores them under candidate receipts, computes tie-aware alignment and supplies rank/criterion contrasts to the rubricator. It does not rerun the champion each round. Revision JSON undergoes count/weight/version/removal checks; the best measured alignment is kept. Iteration bounds, missing scores/client, or errors may end below threshold; the threshold is not a guaranteed postcondition. The final branch promotion does not wait for aligned receipt success. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:177-235,533-755`; `skilllift/skilllift/rubricator.py:177-248,481-535,611-613`. Implementation conclusion status: wired; improvement observation: uninspected.

>             if winner is not None:
>                 winner_verifier = branch_verifier.get(winner.record.candidate_id)
>                 if reward_spec.improves(winner.evaluation.reward, parent_reward):
>                     accept_reason = "oracle_improved"
>                 elif (
>                     reward_spec.validate(winner.evaluation.reward) == parent_reward
>                     and winner_verifier is not None
>                     and champion_verifier is not None
>                     and winner_verifier > champion_verifier
>                 ):
>                     # Oracle tie: promote the branch whose verifier score is higher
>                     # instead of discarding otherwise-good evolution work.
>                     accept_reason = "verifier_tiebreak"
>             if accept_reason is not None:
>                 accepted_id = winner.record.candidate_id
>                 parent = winner.portfolio
>                 parent_reward = reward_spec.validate(winner.evaluation.reward)
>                 state["accepted_candidates"].append(
>                     {"round_index": round_index, "candidate_id": accepted_id}
>                 )
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>             if alignment is not None and (
>                 best_alignment is None or alignment > best_alignment
>             ):
>                 best_alignment = alignment
>                 best_receipt = current_receipt
>             if (
>                 alignment is None
>                 or alignment >= self.config.rank_alignment_threshold
>                 or rubricator_client is None
>             ):
>                 break
>             if mode_iter == self.config.mode_b_iters - 1:
>                 break
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>         selected_alignment = best_alignment if best_alignment is not None else alignment
>         if best_alignment is not None:
>             current_receipt = best_receipt
>         experiment_store.save_receipt(
>             current_receipt, f"outer_{round_index:03d}_mode_b_final"
>         )
>         return current_receipt, selected_alignment
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

Guidance proposes which visible skill properties explain a benchmark ordering mismatch. The revision prompt explicitly forbids inventing hidden labels and asks for no_visible_explanation when the visible text cannot explain the gap. Formulation and content-directed criticism of the rubric: afforded, with wired prompts and contrast delivery; actual sound criticism: uninspected. Criterion replacement/removal and altered future ranking: wired. Reasons/evidence_refs in removals and diagnosis metadata can persist in receipt and reach future receipt prompts, but string-presence validation is not semantic support. The hidden-answer check is a two-substring filter, not a provenance or nonleakage proof. Stronger inference that criticism improved future capacity remains uninspected. Selection prefers observed alignment on this candidate set; the prompt's reusable-behavior instruction is a policy preference for generality, not a test of explanatory reach among evidence-fitting alternatives.

>         "[Oracle Contrast Diagnosis]",
>         "- For each pairwise difference, compare only visible task requirements, skill files, criterion_hits, and criterion_evidence.",
>         "- If the oracle-preferred skill contains a reusable observable behavior that the receipt does not reward, add or strengthen a positive criterion for that behavior.",
>         "- If the lower-scoring skill contains an explicit unsafe or forbidden behavior that the receipt does not penalize, add or strengthen a negative criterion for that behavior.",
>         "- A scalar score gap alone is never enough to create a criterion; when visible evidence cannot explain it, preserve the receipt and record no_visible_explanation.",
>         "- If oracle_scores separate skills but verifier_scores are tied or full-credit, the current receipt is too weak.",
>         "- In receipt.metadata.oracle_contrast_diagnosis, write only an evidence-bounded hypothesis from visible skill text and public scores.",
>         "- Do not infer expected answers, missing task-specific actions, hidden labels, or private oracle rules from logs, chat, artifacts, filenames, or output paths.",
>         "- If visible skill text does not explain the oracle gap, write no_visible_explanation instead of guessing.",
> --- `skilllift/skilllift/baselines/prompts.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

> def _contains_hidden_answer(receipt: Receipt) -> bool:
>     text = json.dumps(receipt.to_dict(), ensure_ascii=False).lower()
>     return "hidden_answer" in text or "ground_truth" in text
> --- `skilllift/skilllift/rubricator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

RTE-4 — Benchmark portfolio evaluation and feedback. Trigger: anchor/candidate/final logical cell. The coordinator fingerprints task, portfolio, algorithm, phase and candidate; cached valid cells return immediately. New attempts call the injected adapter. WildClaw loads the portfolio, launches OpenClaw in a Docker container, runs task-supplied grading Python and reads score.json after checking task/skill/config identity and artifact paths. SkillsBench stages the portfolio plus host patch, launches its BenchFlow wrapper, checks unchanged deployment bytes, exact result task and deployment/loaded-skill receipts, then accepts a finite reward in [0,1]. Valid numeric reward may be admitted even when SkillsBench result carries timeout/partial-trajectory metadata. Next-step owner: external runtime and benchmark evaluator during rollout, coordinator on return. Effects: model/provider calls, subprocess/container/tool execution, local benchmark artifacts. Persistence: attempt markers, result hashes and raw outputs. Recovery: adapter can reconstruct completed attempts; repeated infrastructure failures trip a per-invocation fuse without committing a valid logical cell. Source: SRC-1 `skilllift/skilllift/coordinator/task.py:546-705`; `skilllift/skilllift/adapters/wildclawbench.py:276-404`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py:97-169,171-298`; `skilllift_eval/runners/skillsbench_adapter.py:98-156,334-374`; `skilllift_eval/runners/wildclaw_engine/run_batch.py:384-410,484-532,561-674`. Implementation conclusion status: wired. Receipt matching checks delivery identity, not activation or usefulness.

>     def _validate_receipts(self, receipt_root: Path, portfolio: PortfolioRef) -> None:
>         deployed = _read_json(receipt_root / "deployed_tree_receipt.json")
>         loaded = _read_json(receipt_root / "loaded_skill_receipt.json")
>         expected_manifest = list(portfolio_manifest(portfolio.root))
>         if deployed.get("tree_hash") != portfolio.tree_hash or deployed.get("files") != expected_manifest:
>             raise ValueError("SkillsBench deployed-tree receipt does not match the candidate Portfolio")
> --- `skilllift_eval/runners/skillsbench_portfolio_adapter.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>     # The reward is computed by the verifier from the agent's final artifacts, so it
>     # stays authoritative even when the run was cut short by a wall-clock/agent
>     # timeout or carries a partial trajectory. Accept any result with a valid
>     # reward and only reject results where the reward is absent or malformed,
>     # which signals a genuinely unusable run (e.g. verifier never executed).
>     rewards = payload.get("rewards")
>     if not isinstance(rewards, dict) or not isinstance(rewards.get("reward"), (int, float)):
> --- `skilllift_eval/runners/skillsbench_adapter.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>     runner_code = "\n".join([
>         "import json, sys",
>         automated_checks,
>         "",
>         f'result = grade(transcript=[], workspace_path="{TMP_WORKSPACE}")',
>         "print(json.dumps(result))",
>     ]) + "\n"
> --- `skilllift_eval/runners/wildclaw_engine/grading.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

Answer-oracle distinction: the source-native “oracle” means a full rollout plus benchmark reward, not necessarily an expected-answer lookup. WildClaw's superproject copies a gt directory when present and runs task-provided checks; thus access to reference material is wired conditionally at the grader, provided by the external benchmark task. The exact references, grading truth and whether a given grader uses model judgment are uninspected. SkillsBench consumes an external verifier reward; expected-answer availability is uninspected within this boundary. Framework proposal prompts receive public requirements, visible skill text and scalar/rank evidence rather than established hidden answers. Operators supply tasks/configuration and launch the bounded experiment; no per-candidate human approval is in the inspected coordinator path. This is descriptive scope, not an autonomy grade.

RTE-5 — Persistence, recovery, resume and final portfolio export. Trigger: state/plan/candidate/evaluation saves and later evolve of the same task. PortfolioStore writes immutable plans/candidate records and mutable state, reconstructs accepted parents from seed plus recorded patches, verifies hashes and freezes the final tree by atomic copy. Admission of state is governed by fingerprint, task and hash checks; changed seed/config or conflicting immutable marker can reject reuse. No automatic expiry was established by these methods; user file deletion/replacement is outside the recorded recovery protocol. Source: SRC-1 `skilllift/skilllift/portfolio/store.py:73-156,158-192,218-267,355-402`; `skilllift/skilllift/coordinator/task.py:274-344,592-690`; `skilllift/skilllift/coordinator/modes.py:392-399,203-209,252-303`. Implementation conclusion status: wired. Conditional recovery mismatch: Mode A changes branch.portfolio while keeping its initial CandidateRecord; acceptance retains only candidate ID. On resume the saved initial patch is replayed, not the later refinement. A later accepted patch can fail its parent-hash check; an already frozen refined final portfolio can disagree with the reconstructed tree. This is a static path inference, not an observed incident. In uninterrupted operation the current refined portfolio still reaches evaluation and final copy.

>     def materialize_parent(self, task_id: str, state: dict[str, Any], workspace: Path) -> PortfolioRef:
>         current = self.load_seed(task_id)
>         for index, accepted in enumerate(state.get("accepted_candidates", [])):
>             record = self.load_candidate(task_id, int(accepted["round_index"]), accepted["candidate_id"])
>             if record is None:
>                 raise PersistenceError(f"accepted candidate record is missing: {accepted}")
>             current = self.materialize_candidate(current, record, workspace / f"accepted-{index:03d}")
>         return current
> --- `skilllift/skilllift/portfolio/store.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

>     def freeze_final(self, task_id: str, portfolio: PortfolioRef) -> PortfolioRef:
>         destination = self.task_root(task_id) / "final_portfolio"
>         if destination.exists():
>             if portfolio_tree_hash(destination) != portfolio.tree_hash:
>                 raise PersistenceError("existing final portfolio has the wrong tree hash")
>         else:
>             destination.parent.mkdir(parents=True, exist_ok=True)
>             with tempfile.TemporaryDirectory(prefix=".final-", dir=destination.parent) as temporary:
>                 staged = Path(temporary) / "portfolio"
>                 shutil.copytree(portfolio.root, staged, copy_function=shutil.copy2)
>                 os.replace(staged, destination)
> --- `skilllift/skilllift/portfolio/store.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-3 and OBJ-5, round-boundary state persists the receipt and search history. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:252-303`.

>             state.update(
>                 parent_reward=parent_reward,
>                 next_round=round_index + 1,
>                 history=serialize_search_history(history),
>                 direction_history=[item.to_dict() for item in direction_history],
>                 prohibited_novelty_keys=sorted(prohibited),
>                 previous_plan=plan.to_dict(),
>                 receipt=receipt.to_dict(),
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For OBJ-2, arbitrary imported UTF-8 assets leave the complete representational union uncertain. Source: SRC-1 `skilllift/skilllift/portfolio/ref.py:275-303`.

>             data = path.read_bytes()
>             if b"\x00" in data:
>                 raise PortfolioError(f"binary file is forbidden: {rel}")
>             try:
>                 data.decode("utf-8")
>             except UnicodeDecodeError as exc:
>                 raise PortfolioError(f"file must be UTF-8: {rel}") from exc
> --- `skilllift/skilllift/portfolio/ref.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-5 and OBJ-4, persisted initial patch/direction bytes retain provenance. Source: SRC-1 `skilllift/skilllift/portfolio/store.py:158-237`.

>             self._write_text_atomic(temp_root / "patch.diff", patch)
>             self._write_json_atomic(temp_root / "direction.json", direction.to_dict())
>             validation = {
>                 "candidate_id": candidate_id,
>                 "round_index": round_index,
>                 "parent_hash": parent_hash,
>                 "candidate_hash": result.portfolio.tree_hash if result else None,
>                 "patch_hash": result.patch_hash if result else hashlib.sha256(patch.encode("utf-8")).hexdigest(),
> --- `skilllift/skilllift/portfolio/store.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-3, current receipt, candidates and both score sets enter revision. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:679-697`.

>             revision_input = ReceiptRevisionInput(
>                 task=task_spec,
>                 receipt=current_receipt,
>                 skills=skills,
>                 verifier_scores=verifier_scores,
>                 oracle_scores=oracle_scores,
>                 verifier_rank=verifier_rank,
>                 oracle_rank=oracle_rank,
>                 rank_alignment=alignment if alignment is not None else 0.0,
>                 oracle_contrast=contrast,
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-3, qualifying trace-fed input is evaluation/verifier events; full rollout trajectories and private evaluator material are excluded from the evidence package. Source: SRC-1 `skilllift/skilllift/rubricator.py:304-376`.

>         "evidence_scope": {
>             "task": "public_task_spec",
>             "seed": "complete_portfolio" if budget is None else "manifest_plus_SKILL.md_plus_budgeted_auxiliary_files",
>             "trajectory": "excluded",
>             "private_evaluator_material": "excluded",
>         },
> --- `skilllift/skilllift/rubricator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-2, duplicate/prohibited direction rejection is admission control, not retained-memory deduplication. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:212-268`.

>         if (
>             direction.direction_id in direction_ids
>             or direction.novelty_key in novelty_keys
>             or direction.novelty_key in prohibited
>             or direction.semantic_key() in semantic_keys
>         ):
>             continue
> --- `skilllift/skilllift/portfolio/prompts.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For OBJ-6 and BAP-1, directions retain a hypothesis and rationale supplied again in later history. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:43-64`.

>             "hypothesis": self.hypothesis,
>             "capability": self.capability,
>             "target_scope": list(self.target_scope),
>             "cross_skill_rationale": self.cross_skill_rationale,
>             "evidence_refs": list(self.evidence_refs),
>             "novelty_key": self.novelty_key,
> --- `skilllift/skilllift/portfolio/prompts.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-2, branch-local criterion feedback is added to the next generator hypothesis without updating its persisted original direction. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:884-903`.

>         direction_id=direction.direction_id,
>         rubric_id=direction.rubric_id,
>         hypothesis=f"{direction.hypothesis}\nVerifier feedback to address: " + "; ".join(targets),
>         capability=direction.capability,
>         target_scope=direction.target_scope,
>         cross_skill_rationale=direction.cross_skill_rationale,
>         evidence_refs=direction.evidence_refs,
>         novelty_key=direction.novelty_key,
> --- `skilllift/skilllift/coordinator/modes.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For OBJ-10 and RTE-3, a removal reason is required syntactically, without semantic proof. Source: SRC-1 `skilllift/skilllift/rubricator.py:501-535`.

>         rubric_id = item.get("rubric_id")
>         reason = item.get("reason")
>         evidence_refs = item.get("evidence_refs")
>         if rubric_id not in removed_ids:
>             errors.append("removed_rubric_entry_invalid")
>         if not isinstance(reason, str) or not reason.strip():
>             errors.append("removed_rubric_reason_missing")
> --- `skilllift/skilllift/rubricator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-3, failed candidate/validation data feeds the immediate retry. Source: SRC-1 `skilllift/skilllift/rubricator.py:177-257`.

>         if attempt.accepted:
>             return candidate
>         previous_payload = payload
>         previous_report = report
> --- `skilllift/skilllift/rubricator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-5, parent reconstruction occurs before completion checks. Source: SRC-1 `skilllift/skilllift/coordinator/task.py:276-280`.

>         with tempfile.TemporaryDirectory(prefix=f"skilllift-{task_id}-") as temporary:
>             workspace = Path(temporary)
>             parent = self.store.materialize_parent(task_id, state, workspace / "accepted")
>             history = _history_from_state(state)
>             parent_reward = state.get("parent_reward")
> --- `skilllift/skilllift/coordinator/task.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-2, SkillsBench planner overflow can select core files; this is selection, not history compaction. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:280-331`.

>     prompt = prompt_with(_complete_evidence_pack(portfolio))
>     if (
>         core_evidence_on_overflow
>         and max_input_chars is not None
>         and len(prompt.system) + len(prompt.user) > max_input_chars
>     ):
>         prompt = prompt_with(_core_evidence_pack(portfolio))
>     return _preflight(prompt, max_input_chars)
> --- `skilllift/skilllift/portfolio/prompts.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For CMP-2 and RTE-2, the native optional-file selector uses model judgment. Source: SRC-1 `skilllift_eval/runners/bounded_edits_skill_generator.py:171-290`.

>         system = (
>             "You are the Skill Generator file selector. Select the smallest set of optional "
>             "files needed to implement the direction. Return only file_ids with "
>             "selectable=true."
> --- `skilllift_eval/runners/bounded_edits_skill_generator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-2, selected IDs map to optional paths and budget checks constrain delivery. Source: SRC-1 `skilllift_eval/runners/bounded_edits_skill_generator.py:171-290`.

>         selected_ids = _parse_selected_ids(raw, optional_by_id, max_optional)
>         if optional_file_bytes_budget is not None and sum(
>             (parent.root / optional_by_id[file_id]).stat().st_size
>             for file_id in selected_ids
>         ) > optional_file_bytes_budget:
>             raise PortfolioContextLimitError(
>                 "selected bounded edit files exceed the configured model context"
>             )
>         optional_paths = tuple(optional_by_id[file_id] for file_id in selected_ids)
>         selected_paths = tuple(sorted((*mandatory_paths, *optional_paths)))
> --- `skilllift_eval/runners/bounded_edits_skill_generator.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-4 and BAP-4, the owned SkillsBench hook injects all skill documents with always-active trigger semantics; external host behavior remains uninspected. Source: SRC-1 `scripts/oh_skill_patch.py:42-108,183-202`.

>         runtime_root = RUNTIME_SKILLS_ROOT / name
>         runtime_note = (
>             f"[Runtime Skill Root]\nThis skill's scripts and references are available under `{runtime_root}`. "
>             "Resolve relative file paths from that directory.\n\n"
>         )
>         # trigger=None => always active (Repository Skill semantics)
>         injected = runtime_note + content
>         skills.append(Skill(name=name, content=injected, trigger=None))
> --- `scripts/oh_skill_patch.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-4, loaded-skill hashes and character counts verify delivery identity only. Source: SRC-1 `skilllift_eval/runners/skillsbench_portfolio_adapter.py:245-270`.

>         for name, values in expected.items():
>             actual = actual_by_name[name]
>             if any(actual.get(key) != value for key, value in values.items()):
>                 raise ValueError(f"SkillsBench loaded-skill receipt hash mismatch: {name}")
>             if not isinstance(actual.get("injected_chars"), int) or actual["injected_chars"] < values["source_chars"]:
>                 raise ValueError(f"SkillsBench loaded-skill receipt token context is invalid: {name}")
> --- `skilllift_eval/runners/skillsbench_portfolio_adapter.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

For RTE-4 and BAP-4, WildClaw supplies locators and instructs the named external agent to request files through its read tool; actual reading is afforded, not observed. Source: SRC-1 `skilllift_eval/skills/wildclaw_loader.py:148-210`.

>         for skill_name in skill_names:
>             skill_path = f"{CONTAINER_SKILL_DIR}/{skill_name}/SKILL.md"
>             lines.append(f"- Read the skill at `{skill_path}` using the read tool")
>             lines.append("- Follow ALL instructions in that skill document")
>             lines.append("- The skill contains critical information you must use")
> --- `skilllift_eval/skills/wildclaw_loader.py` @ `599358b4d4c4a27c0e004df8228ab93026600653`

### Claims

CLM-1 — README claims cheaper rubric ranking supervision gives dense feedback with no oracle cost in inner refinement, and frozen agent adaptation without weight updates. Claim conclusion status: claimed. Source: SRC-1 `README.md:24-33`. The coordinator wires separate refinement and rollout evaluation; framework inference adds cost and per-skill scoring can require multiple calls for a multi-skill portfolio. Fixed remote parameter identity is uninspected.

> SkillLift breaks this supervision bottleneck with one idea: **ranking is a cheaper supervision
> target than score regression.** Instead of chasing oracle scores directly, SkillLift first learns a
> *rubric* — a set of binary criteria with signed weights — that reproduces the oracle's *preference
> order* over skills. Once aligned, the rubric scores any candidate with a **single LLM call**, giving
> the skill generator dense, criterion-level feedback at zero oracle cost.
> --- `README.md` @ `599358b4d4c4a27c0e004df8228ab93026600653`

CLM-2 — README says nondecreasing rubric score never degrades a candidate, Mode B revises until alignment ≥0.9, and misalignment never degrades final output because oracle chooses the champion. Claim conclusion status: claimed. Source: SRC-1 `README.md:106-118`. RTE-2 enforces only a local numeric surrogate comparison, possibly lexical fallback; RTE-3 has bounded iterations, reuses champion reward and admits verifier-based reward ties. The strong task-quality and guaranteed-alignment readings exceed inspected enforcement.

> - **Inner loop (Mode A):** the frozen rubric guides skill revision. Each branch is refined only
>   while its rubric score is non-decreasing, so local refinement can never degrade a candidate.
> - **Outer loop (Mode B):** K+1 oracle rollouts rank the champion and the refined branches; a
>   *rubricator* revises the rubric until its ranking agrees with the oracle's (Kendall's τ ≥ 0.9).
>   A misaligned rubric degrades guidance quality, never the final output — the champion is always
>   selected by oracle score.
> --- `README.md` @ `599358b4d4c4a27c0e004df8228ab93026600653`

CLM-3 — README reports six winning model/benchmark combinations, +8.8–11.5 percentage points on WildClawBench, +16.7–24.2 on SkillsBench and 2.1–2.7× token ratios for baselines. Claim conclusion status: claimed. Source: SRC-1 `README.md:14-16,45-51,94-96`. No candidate-linked raw experiment or intervention is in this analysis; these reported aggregates neither establish a component's causal effect nor verify the reviewed implementation's deployed results.

> **SkillLift wins all six model × benchmark combinations**, lifting the one-shot skill ceiling by
> **+8.8–11.5 pp** on WildClawBench and **+16.7–24.2 pp** on SkillsBench, while baselines need
> **2.1–2.7× more tokens** to reach the same accuracy.
> --- `README.md` @ `599358b4d4c4a27c0e004df8228ab93026600653`

CLM-4 — Conditional static finding: persisted accepted-candidate replay can lose a content-changing Mode A refinement, reuse its reward against the initial draft, reject a later refined-parent patch, or disagree with an existing final tree. Implementation conclusion status: wired. This is an inference from RTE-2 and RTE-5, not an author claim or observed incident. Source: SRC-1 `skilllift/skilllift/coordinator/modes.py:203-209,392-399`; `skilllift/skilllift/portfolio/store.py:239-267,355-365`; `skilllift/skilllift/coordinator/task.py:276-280,311-344`. It does not apply when no changed refinement was promoted; uninterrupted export copies the live refined tree.

### Evidenced absences

None asserted. Uninspected provider state, external benchmark internals and missing observed runs are limitations, not bounded absence records.

### Behavioral-authority paths

BAP-1 — Planner/generator consumes task, evolving portfolio, prior hypotheses/reasons/outcomes and verifier hits in model prompt context. Force: instruction plus advisory evidence; horizon next proposal and later rounds of this task. Structural file scopes become enforcement in patch application; semantic compliance remains uninspected. Source: SRC-1 `skilllift/skilllift/portfolio/prompts.py:280-360`; `skilllift_eval/runners/bounded_edits_skill_generator.py:68-150`; RTE-2.

BAP-2 — Verifier consumes Receipt and skill text through model messages, or lexical fallback evaluates text. Criterion hits become normalized ranking values controlling local refinement and equal-reward promotion. Force: model instruction followed by numeric ranking/enforcement; horizon current scoring/round. Epistemic authority is only modeled or heuristic criterion satisfaction, not task success. Source: SRC-1 `skilllift/skilllift/verifier.py:13-86,162-170`; RTE-2, RTE-3.

BAP-3 — Coordinator consumes valid benchmark rewards and fingerprints through adapter return values. Force: promotion, rejection, termination and cache selection; horizon task adaptation/final reporting. Its epistemic authority inherits the benchmark check's unknown external validity. Source: SRC-1 `skilllift/skilllift/coordinator/task.py:89-103,573-690`; `skilllift/skilllift/coordinator/modes.py:186-209`; RTE-3, RTE-4.

BAP-4 — External rollout agent receives deployed skills and a read/follow instruction or host injection. Force: instruction; actual tools and execution are host-owned. Horizon fresh trial. File/loaded-skill receipt matching warrants delivery identity only, not actual reading or changed behavior. Source: SRC-1 `skilllift_eval/runners/wildclaw_engine/run_batch.py:484-532`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py:245-270`; RTE-4.

BAP-5 — Coordinator consumes persisted task/accepted-candidate/receipt/evaluation identifiers and matching hashes. Force: routing, validation and reuse; horizon same-task resumed and later rounds. Stored acceptance is operational lineage, not fresh evidence of fitness; refinement recovery has the RTE-5 limitation. Source: SRC-1 `skilllift/skilllift/portfolio/store.py:89-156,239-267`; `skilllift/skilllift/coordinator/task.py:592-605`; RTE-5.

## Runtime account

The ordinary WildClaw invocation is the README's `python -m skilllift_eval.cli run skilllift --benchmark wildclawbench ... --tasks.mode single --tasks.filter ...`. The CLI supplies endpoint/task/config hashes to the native runner, which creates clients, adapter and PortfolioStore, then calls CMP-1. RTE-1 anchors the declared seed, RTE-2 generates and refines branches, RTE-4 obtains benchmark rewards, RTE-3 promotes a parent and revises the rubric, and RTE-5 records state for later rounds/resume. Terminal or budget conditions freeze the winner; two valid-or-indeterminate final cells are attempted and the maximum valid score is returned with the portfolio, history, physical attempts and logical-cell counts. All source anchors and role ownership are on those routes.

Native SkillsBench batches invoke the same coordinator per selected task with their own adapter, deployment receipts and optional planner evidence-overflow fallback. Native WildClaw batch launching is sequential task subprocess invocation; candidate scheduling uses a ThreadPoolExecutor but the WildClaw adapter's runner lock serializes its actual runner calls. Framework model calls are direct LLMClient requests, not subagents with independent task authority. Injected planner/generator/verifier/adapter callbacks can replace native roles; guarantees depend on each callback's contract and do not certify arbitrary implementations. Legacy algorithms and tau2 are excluded, so README statements about identical budgets across every baseline are not established here.

The capability surface includes local portfolio writes, provider requests, host subprocesses, Docker launch/copy/exec/build, task-supplied warmup/grading code and host agent tools. The current grant set is selected by endpoint credentials, task environment names, model configuration, adapter and sandbox settings; no deployed grant set was inspected. WildClaw mounts its task exec directory read-only at /app, copies temporary files and passes task/judge environment values. This code is an execution envelope, not proof of network denial, sandbox completeness or tool safety. Patch scope and forbidden dependency filenames constrain generated portfolio edits only; they do not govern all host subprocesses or model-provider effects. Source: SRC-1 `skilllift_eval/runners/wildclaw_engine/docker_utils.py:26-98`; `skilllift_eval/runners/wildclaw_engine/run_batch.py:561-674`; `skilllift_eval/runners/skillsbench_portfolio_adapter.py:199-243`.

Forcing cases selected by static trace:

| Case | Inspected transition | Supported result and limit |
|---|---|---|
| Bad verifier output or unavailable scoring | RTE-2, SRC-1 `skilllift/skilllift/verifier.py:21-32,162-170`; `skilllift/skilllift/coordinator/modes.py:445-483` | Non-agent_skill output can become lexical fallback; other caught errors yield missing scores. A nondecreasing score is not a semantic guarantee. No failure observed. |
| Equal benchmark reward or unresolved alignment | RTE-3, SRC-1 `skilllift/skilllift/coordinator/modes.py:190-209,666-728` | Higher verifier value may promote a reward tie; best receipt survives even below alignment target. Future/general improvement remains uninspected. |
| Infrastructure failure and task resume | RTE-4, RTE-5, SRC-1 `skilllift/skilllift/coordinator/task.py:603-690`; `skilllift/skilllift/portfolio/store.py:239-267,355-365` | Valid cells can recover without re-evaluation; fuse failure is indeterminate. Initial-patch replay can diverge from refined acceptance. Static inference only. |
| Oversized context or invalid portfolio edit | RTE-2, SRC-1 `skilllift_eval/runners/bounded_edits_skill_generator.py:68-101`; `skilllift/skilllift/coordinator/modes.py:108-115,140-147,227-235`; `skilllift/skilllift/portfolio/ref.py:164-256` | File selection or bounded failure/skip prevents unchecked candidate admission; it does not prove selected evidence is sufficient. |

Execution preflight: **no dynamic check planned**. Considered a refinement/resume fixture, malformed-verifier fixture and real benchmark smoke run. Static branch inspection is sufficient for the conditional implementation findings. No framework packages, Docker, external Gitlinks, services or credentials were used to execute SkillLift; real rollouts would require those dependencies and paid provider calls. No command attempt is counted as an observed target check.

Every route's consumer audit:

| Route | Immediate return | Later read-back and delegated visibility | Selection predicate | Invalidation/expiry | Activation/effect and evidence limit |
|---|---|---|---|---|---|
| RTE-1 | TaskEvolutionResult | Reconstructed parent/history/state to later calls; task and portfolios to adapter/model roles | Task ID, algorithm/config identity and terminal/status predicates | Fingerprint mismatch refuses reuse; no automatic time expiry shown in inspected methods | Control and delivery wired; task benefit uninspected |
| RTE-2 | Valid/refined branch or failure | Candidate files, directions, prior histories and receipt supplied to subsequent model scoring/proposals; direct callbacks vary | Declared paths, optional model selection, context budget and verifier threshold | Rejected edits remain outside parent; losing branch stops influencing chosen parent except retained history | File edits/score admission wired; instruction activation uninspected |
| RTE-3 | New parent and selected receipt/alignment | Receipt/history/accepted IDs persist and feed subsequent rounds | Valid benchmark rewards, verifier tie rule, measured alignment and finite iteration budget | Nonwinning receipt discarded from current reliance; audit artifacts may persist; no time expiry | Operational replacement wired; valid criticism and capacity gain uninspected |
| RTE-4 | Valid reward/hash or infrastructure error | Cached cells and recoverable attempt artifacts avoid later rollout; portfolio goes to external harness | Full cell fingerprint, task/result identity and numeric validity | Mismatch rejects; indeterminate attempts do not become valid cells | Deployment/return wired, receipt identity only; external tool execution validity and behavior change uninspected |
| RTE-5 | Materialized parent/final ref/state | Same task's accepted patches/state/results re-enter control and model contexts | IDs/hashes and recorded accepted-candidate order | Conflict/hash mismatch rejects; filesystem lifetime not scheduled here | Reuse wired with refinement replay limitation; no faithful-recall intervention |

## Lens scoping

### Memory/context scope

Full depth triggered by OBJ-2, OBJ-3, OBJ-4, OBJ-5 and RTE-2, RTE-3, RTE-5. Scope is changed/accumulated portfolios, rubric and history/plan state, write admission, later model/harness consumers and task resume on the two native flagship adapters. Static task/seed initialization is lineage context, not itself read-back. External post-export use and legacy algorithms excluded. Fresh specialist input frozen at SHA-256 `067be3011aec50750220ebe2b6c14a35c58cd6aa5e8c4fd8b243d5fd46834a98`.

### Epistemic scope

Full depth triggered by explicit hypotheses/criteria, verifier evidence, benchmark ranking and rubric-revision claims (OBJ-2, OBJ-3, OBJ-4; RTE-2, RTE-3, RTE-4; CLM-1, CLM-2, CLM-3). The standalone epistemic procedure was executed locally over SRC-1, assessing candidate content, checks, disposition, retention, recovery and later force. External task truth, graders, model internals and reported experiments remain uninspected; they cannot supply whole-system warrant.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried OBJ-2, OBJ-3, OBJ-4, OBJ-5 and all five routes, checking core mechanisms, artifacts, writes, later consumers and misleading claims. Its fourteen-axis profile is integrated above without changing values or confidence. Retained state is task-local files plus live Python objects. Imported seeds and deterministic patch/history compilation join automatic event-fed revisions; source Git is provenance, not a memory database. Evolved skills, receipt versions, plans and scalar outcomes affect later rounds. Raw benchmark artifacts are retained behind references, but the flagship rubric evidence excludes trajectories/private evaluator material (RTE-3).

Read-back is consumer-specific. The planner receives coarse automatic current-portfolio/prior-plan/direction-history/scalar-history supply on a new plan. SkillsBench enables core-file fallback on overflow; WildClaw does not. Native bounded editors select scoped files, enforce mandatory skill documents/exact-file scopes, and may ask a model to select optional file IDs under a 20-file and size/context bound. Mapping those IDs to paths is identifier selection; the model's choice is inferred judgment. Mode A matches criterion IDs and hit flags to missing/forbidden criterion text supplied to the generator. Verifiers receive whole current receipt and skill payload. These are push routes. The coordinator's explicit requests for saved task state/plan/candidate/result are pull; requested lookup IDs are not counted again as identifier push. These selectors and their exact evidence are retained on RTE-2, RTE-3, RTE-5.

Adapter delivery differs materially. SkillsBench's owned hook supplies whole skill documents with trigger=None, named runtime locations for scripts/references and custom-skill precedence over same-name built-ins. This is coarse push into an external context hook. WildClaw installs the portfolio and automatically supplies document locators plus a read-tool instruction; subsequent external-agent content reading is afforded pull. Both pass provenance/delivery checks; neither establishes instruction activation or script invocation. Consequently behavioral-authority and direction unions use the weaker afforded basis, while internal selectors are wired. Source: SRC-1 `scripts/oh_skill_patch.py:42-108,183-202`; `skilllift_eval/skills/wildclaw_loader.py:59-110,148-210`; RTE-4 and BAP-4.

Automatic trace learning in the comparison's narrow write-route sense is wired: evaluation/verifier event streams feed saved plans, portfolio patches and rubric revisions before subsequent trials/rounds. Scope is per-task; timing is staged; distilled outputs include natural-language hypotheses/criteria/skill instructions and symbolic patches, executable text and structured rules. Batch iteration does not import another task's evolved history. This classification does not establish conjectural learning or measured improvement. Curation comprises evolve, synthesize, promote and invalidate; duplicate proposal rejection is not memory deduplication. Reasons persist in directions and optional rubric diagnosis, but branch-refinement feedback need not persist in the initial candidate record and final files need not explain each adopted edit.

Two axes remain not-determinable. The complete representational union includes opaque imported UTF-8 assets; known prose/code lower bounds cannot classify every such payload. Faithfulness has no commissioned recalled-content dependence experiment; deployed/load receipts establish identity rather than dependence. Context limits also differ: planner/generator guards can be absent or branch-specific, and the verifier call does not receive the coordinator's receipt context limit. The specialist's resume finding is incorporated as CLM-4, with conditional consequences and no invented observed failure.

### Epistemic lens

#### 1. Source-and-claim boundary

SkillLift at the frozen revision uses canonical SRC-1 and the declared flagship boundary. Question: what do hypotheses, rubric criteria, benchmark results and accepted edits warrant, and how do they affect later behavior? Assessed families are RTE-1, RTE-2, RTE-3, RTE-4, RTE-5; unassessed families are external benchmark/host/provider internals, legacy algorithms and cross-task deployment. Source layer is implementation plus separately attributed README claims CLM-1, CLM-2, CLM-3. No candidate-linked generated run artifact or causal experiment was inspected; claim CLM-4 is static inference. Thus an implemented transition is not an observed candidate disposition.

#### 2. Epistemic-object inventory

Generic identities, forms, storage, source/input lineage and endpoints remain on canonical records. The following overlays name only operative epistemic parts; container OBJ-4 has been made addressable through OBJ-6, OBJ-7, OBJ-8, and OBJ-3 through OBJ-9, OBJ-10 without changing the containers' referents.

| Part | Candidate content/role | Producer/consumer and warrant limit | Evidence |
|---|---|---|---|
| See OBJ-1 | Imported public task assertions and requirements | Benchmark to planner/agent; import preserves supplied wording, not independently established truth | SRC-1, OBJ-1 anchors |
| See OBJ-2 | Procedural instructions/code, potentially factual claims inside arbitrary text | Generator to validator, verifier and host agent; policy edits are not automatically truth-apt, while factual additions can be ampliative | SRC-1, OBJ-2 and RTE-2 anchors |
| See OBJ-6 | Proposed requirement/hypothesis that a scoped capability change addresses this task | Model planner to generator/future planner; explicit candidate hypothesis, not entailed by observed score | SRC-1 `skilllift/skilllift/portfolio/prompts.py:30-81,280-331` |
| See OBJ-7 | Criterion satisfaction plus explanation, and numeric score/rank | Model/lexical scorer to coordinator/reviser; assertion and arithmetic must be separated | SRC-1 `skilllift/skilllift/verifier.py:62-86,162-170` |
| See OBJ-8 | External reward and its associated task/trial identity; history delta and rank | Benchmark evaluator to coordinator/planner; external validity unknown, association checked locally | SRC-1 `skilllift/skilllift/coordinator/task.py:117-174,592-705` |
| See OBJ-9 | Normative skill criteria and implied predictive assessment hypotheses | Rubricator to verifier/reviser; syntactic validity and sampled ranking agreement do not warrant universal necessity or predictive validity | SRC-1 `skilllift/skilllift/rubricator.py:114-163,481-535` |
| See OBJ-10 | Explanation of ranking mismatch or why a criterion should be removed | Rubricator to later whole-receipt contexts; mandatory nonempty removal explanation is not validated content | SRC-1 `skilllift/skilllift/baselines/prompts.py:153-184` |
| See OBJ-5 | Provenance/checkpoint assertions about selected task/candidate/result | Store to coordinator; supports operational identity, with CLM-4's fidelity exception | SRC-1 `skilllift/skilllift/portfolio/store.py:239-267,355-365` |

#### 3. Authority-route ledger

Each row is one function of its canonical route. Architectural status is **implemented** for every row below; activation is conditional as specified. No row asserts observed activation. Behavioral authority follows BAP-1, BAP-2, BAP-3, BAP-4, BAP-5 at their declared horizons. “Epistemic license” is limited to the named target/check and does not certify its broader content.

| Route and function | Object and content/update relation | Activation, evaluator domain and possible result | Implemented force; epistemic license; operational authority and path | Evidence; claims; mismatch/limit |
|---|---|---|---|---|
| For RTE-1 — content transformation | OBJ-1, OBJ-2; truth-apt transformation: acquisition/import for factual content, non-truth-apt policy import for instructions | Task initialization; adapter imports public view and declared seed | Allows task setup; no new truth warrant; BAP-1, BAP-4 | SRC-1, OBJ-1 and RTE-1; CLM-1; external origin validity unknown |
| For RTE-2 — content transformation | OBJ-6, proposed factual parts of OBJ-2; truth-apt transformation: ampliative conjecture; instruction/code edits can instead be non-truth-apt policy/content update | Missing plan or branch refinement; model proposes requirements, hypotheses and edits | Creates proposals, not epistemic acceptance; BAP-1 | SRC-1 `skilllift/skilllift/portfolio/prompts.py:280-360`; CLM-1; actual generated content unobserved |
| For RTE-2 — check/evidence production | OBJ-2; no content change | Every patch; scope/layout/hash/dependency checks | Formal admission evidence over file-change contract only; no task fitness; BAP-1 | SRC-1 `skilllift/skilllift/portfolio/ref.py:164-256`; CLM-2; callback generator still crosses validator |
| For RTE-2 — disposition/acceptance | OBJ-2; no content change | Valid patch then nondecreasing verifier score in refinement | Replaces working branch; accepts local surrogate fit for another trial, not truth of instruction rationale; BAP-2 | SRC-1 `skilllift/skilllift/coordinator/modes.py:357-443`; CLM-2; lexical fallback and missing-score branches |
| For RTE-2 — check/evidence production | OBJ-7; model criterion judgment is truth-apt transformation: ampliative conjecture; numeric weighted score is entailed derivation under supplied hits/weights | Scoring call; model or lexical heuristic, then deterministic arithmetic | Criterion assertions become ranking; arithmetic warrants only consistency with supplied values; BAP-2 | SRC-1 `skilllift/skilllift/verifier.py:13-86,162-170`; CLM-1, CLM-2; no independent semantic test |
| For RTE-4 — check/evidence production | OBJ-8; truth-apt transformation: acquisition/import of reward and association metadata | Fresh trial; external task grader and local fingerprint/numeric checks | Benchmark-specific evidence permits return; BAP-3 | SRC-1 RTE-4 anchors; CLM-3; exact reference answers/check validity excluded |
| For RTE-3 — content transformation | OBJ-9, OBJ-10; criterion policy update and truth-apt transformation: ampliative conjecture for new explanatory hypotheses | Ranking mismatch with enough scores/client/budget; rubricator compares visible skill content | Proposes criteria/reasons; no warranted explanation merely from scalar gap; BAP-1, BAP-2 | SRC-1 `skilllift/skilllift/baselines/prompts.py:153-184`; CLM-1, CLM-2; prompt requests content-directed diagnosis, response unobserved |
| For RTE-3 — check/evidence production | OBJ-9, OBJ-10; no content change plus entailed rank-alignment calculation under supplied numbers | Each revision; structural/version/removal validation then rescoring | Checks receipt contract and empirical agreement on this set; no proof of explanation or transfer; BAP-2 | SRC-1 `skilllift/skilllift/rubricator.py:177-248,481-535`; `skilllift/skilllift/coordinator/modes.py:618-678`; CLM-2 |
| For RTE-3 — disposition/acceptance | OBJ-9, OBJ-10; no content change | Best measured alignment or fallback old receipt | Permits current rubric use; reasons are carried without a separate truth gate; BAP-2 | SRC-1 `skilllift/skilllift/coordinator/modes.py:666-728`; CLM-2; may end below threshold |
| For RTE-3 — disposition/acceptance | OBJ-2; no content change | Valid branch reward strictly higher, or equal with higher verifier score | Promotes parent for same-task search; warrant is measured outcome/heuristic tie, not general superiority; BAP-3 | SRC-1 `skilllift/skilllift/coordinator/modes.py:186-209,731-755`; CLM-2 |
| For RTE-3 — lifecycle integration | Accepted operational OBJ-2, OBJ-9; no content change | Next round consumes promoted parent/receipt | Changes search/scoring after operational acceptance; epistemic integration of a particular claim requires missing candidate-linked evidence; BAP-1, BAP-2 | SRC-1 `skilllift/skilllift/coordinator/modes.py:239-307`; CLM-1; content truth not separately accepted |
| For RTE-5 — retention | OBJ-2, OBJ-3, OBJ-4, OBJ-5; non-ampliative reshaping of declared retained fields | State/plan/candidate writes and final copy | Makes artifacts available to later consumers; storage adds no warrant; BAP-5 | SRC-1 RTE-5 anchors; CLM-4; refinements not fully encoded by initial patch |
| For RTE-5 — lineage/freshness/recovery | OBJ-5 and reconstructed OBJ-2; no intended content change | Same task resume/cached cell request; hashes/fingerprints/patch replay | Reuses operational state or rejects mismatch; no reevaluation of validity; BAP-5 | SRC-1 `skilllift/skilllift/portfolio/store.py:239-267,355-365`; CLM-4; conditional reconstruction divergence |
| For RTE-4 — operational admission/selection/consumption | OBJ-2; no content change | Trial starts; owned adapter/hook installs/injects skills or read locators | Instructions supplied to host; no warrant that followed; BAP-4 | SRC-1 `scripts/oh_skill_patch.py:42-108,183-202`; `skilllift_eval/skills/wildclaw_loader.py:148-210`; CLM-1; external read remains afforded |

#### 4. Per-object lifecycle disposition

For OBJ-6 and OBJ-10, the proposed hypotheses/explanations are ampliative candidates. No generated candidate instance or candidate-linked execution was inspected. All observed candidate states below are therefore **no instance observed**, separately from architectural status. This is not a claim that the project has never generated one.

| Candidate and phase | Relevant route, architectural status | Observed candidate state | Criterion/intended use and scope; evidence limit |
|---|---|---|---|
| For OBJ-6 — observation/anomaly | RTE-2; implemented | no instance observed | Prior scalar outcomes and verifier feedback enter planner, SRC-1 `skilllift/skilllift/portfolio/prompts.py:280-331` |
| For OBJ-6 — conjecture | RTE-2; implemented | no instance observed | Explicit requirement/hypothesis fields; no generated instance inspected |
| For OBJ-6 — derived consequence | RTE-2; not determinable | no instance observed | Edit direction proposes an intervention; no enforced derivation of a separately stated test consequence |
| For OBJ-6 — test/evidence | RTE-2, RTE-4; implemented | no instance observed | Patch, verifier and benchmark evaluate a bundle; no enforced proposition-specific test |
| For OBJ-6 — acceptance | RTE-3; not determinable | no instance observed | Skill promotion can consume reward without accepting the named hypothesis as true; no separate hypothesis criterion established |
| For OBJ-6 — lifecycle integration | RTE-2, RTE-3; not determinable | no instance observed | Later plan/direction read-back is wired, but post-epistemic-acceptance integration is not established |
| For OBJ-10 — observation/anomaly | RTE-3; implemented | no instance observed | Rank/criterion contrasts identify candidate mismatches, SRC-1 `skilllift/skilllift/coordinator/modes.py:618-634` |
| For OBJ-10 — conjecture | RTE-3; implemented | no instance observed | Prompt requests evidence-bounded diagnosis/removal reasons; semantic output unobserved |
| For OBJ-10 — derived consequence | RTE-3; not determinable | no instance observed | Changed criteria imply a new scoring behavior, but no general claim-to-consequence derivation is enforced |
| For OBJ-10 — test/evidence | RTE-3; implemented | no instance observed | Revised receipt is rescored for alignment; explanation itself is not independently tested |
| For OBJ-10 — acceptance | RTE-3; not determinable | no instance observed | Receipt contract and alignment grant scoring authority, not truth acceptance to diagnosis; intended use is next scoring round |
| For OBJ-10 — lifecycle integration | RTE-3; not determinable | no instance observed | Whole-receipt delivery can carry reasons after receipt promotion; candidate-linked accepted-claim integration absent from inspected evidence |

For OBJ-7, the criterion-satisfaction assertion is an ampliative model/heuristic judgment. Its observation input (skill/receipt) and judgment generation have architectural status **implemented** at RTE-2; observed candidate state **no instance observed**. A separate derived-consequence or independent semantic-test route is **not determinable**; state **no instance observed**. Type/key validation is implemented but tests syntax. Its ranking consumption is **implemented** under BAP-2, while epistemic acceptance/integration of the asserted satisfaction is **not determinable**; state **no instance observed** throughout. Numeric score/rank is instead an entailed derivation only within the supplied-hit/weight arithmetic; discovery lifecycle is not applicable to that arithmetic output.

For OBJ-1 and OBJ-8, transformation is acquisition/import; discovery lifecycle is not applicable. Public task text and external reward enter through RTE-1 and RTE-4; local identity/range checks protect association, not source truth. Scalar-history reshaping is non-ampliative over the fields actually retained; it does not preserve the full causal trajectory. For OBJ-5, intended reconstruction is non-ampliative; the CLM-4 path prevents a general fidelity claim.

For OBJ-2, transformation is **indeterminate** for factual prose in arbitrary generated/imported files: preservation, derivation and ampliation are all possible without candidate content. Its direct instruction/code policy updates are evidenced operationally, with structural and outcome checks; evidence needed to classify truth-apt additions is actual before/after content and linked criticism/test history. For OBJ-9, requirements as normative scoring policy have no candidate truth-apt output; their implicit predictive interpretation remains indeterminate without a concrete stated claim. No lifecycle record for the non-truth-apt policy part of OBJ-9: relevant direct-adaptation routes are RTE-2 and RTE-3. OBJ-3 and OBJ-4 are containers disposed through their parts, not additional undifferentiated truth claims.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design support and implemented routes | Observed-run support | Causal support | Supported conclusion and mismatch/unknown |
|---|---|---|---|---|
| See CLM-1 | Separate inner scoring and outer rollout RTE-2, RTE-3, RTE-4 | None inspected; README report only | None inspected | Wired cost-shifting mechanism; no oracle calls in Mode A's own code. Multi-skill scoring iterates per skill; savings depend on costs and outcome |
| See CLM-2 | Numeric nondecrease and reward-led promotion with finite alignment loop | None inspected | None inspected | Local surrogate nondecrease only; lexical fallback, verifier ties, cached champion reward and below-threshold exits limit broad guarantees |
| See CLM-3 | README numerical report; shipped benchmark interfaces | None inspected at candidate-linked level | None inspected | Attributed reported aggregate only; not evidence that criticism or a particular component caused benefit |
| See CLM-4 | Initial record retained through refinement, ID-only accepted chain and replay | No failure observed | No intervention performed | Conditional implementation mismatch; uninterrupted live final copy remains supported |

#### 6. Bounded conclusion

The system imports tasks/seeds, reshapes scalar result evidence, conjectures directional hypotheses and rubric explanations, structurally validates edits/criteria, and grants operational reliance from verifier and benchmark comparisons. It retains accepted operational state and supplies it to later planning/scoring/trials. Its explicit reasons and criterion IDs afford content-directed criticism, but scalar fit and parser validity cannot certify that criticism or its explanatory reach. Framework rank arithmetic is warranted only relative to supplied scores; benchmark correctness belongs to excluded evaluator sources. Reflection and a standing self-improvement pathway are distinguishable from observed successful learning; see the bounded synthesis. None of these findings supplies a system-wide epistemic grade.

## Reconciliation

The frozen specialist input and report identify this run, SRC-1 revision and declared boundary exactly. Input SHA-256 is `067be3011aec50750220ebe2b6c14a35c58cd6aa5e8c4fd8b243d5fd46834a98`; method SHA-256 is `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`; actual specialist model identity is unknown. Complete report SHA-256 is recorded in Run identity. Its full validation, source anchors and unchanged input identity were checked before integration.

The sole proposal mapping is MEM-CLM-1 → CLM-4, a static inferred qualification of RTE-5. Existing CMP-1, CMP-2, CMP-3, OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5 and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 keep their original referents. New OBJ-6, OBJ-7, OBJ-8 identify parts of OBJ-4 and OBJ-9, OBJ-10 parts of OBJ-3 for epistemic heterogeneity; no original ID was reassigned or superseded.

All six integration issues are disposed: (1) refined replay limitation retained with its condition and uninterrupted-export exception; (2) native bounded editor and judgment-based file selector included on CMP-2/RTE-2; (3) representational union remains not-determinable because inherited asset bodies are excluded; (4) SkillsBench coarse hook injection and WildClaw afforded file pull are separate RTE-4 branches; (5) trace learning is event-stream, per-task and staged, without claiming rollout-trajectory extraction; (6) all seed referents unchanged, both uncertainty axes retained and no substantive conflict remains. The coordinator's recovery question was explicitly sent to the specialist, so convergence on that finding is not claimed as blind independent discovery. The epistemic lens independently supplies its own route-level warrant assessment, not a second memory classification.

The specialist's twenty-three quote blocks are integrated once where distinct evidence is needed; overlapping excerpts already retained on the same canonical records are not repeated. Every adopted conclusion is self-contained here; the local report is provenance, not an additional required evidence file. Source-only independence was preserved: no previous target review, prior audit finding or ingest prose was read.

## Bounded synthesis

SkillLift wires a per-task improvement process in which dense rubric feedback guides local portfolio edits and sparse benchmark rewards determine parent succession, with a verifier-based rule for reward ties. Its strongest established contribution is this inspectable, evidence-responsive edit-and-evaluate route with versioned criteria, reasons and file-scoped validation. Separate gates answer different questions: a patch can apply within its allowed scope, a verifier can predict criterion satisfaction, and an external benchmark can return a task reward. None alone establishes the others.

A standing self-improvement pathway at the declared improvement-plane boundary has implementation conclusion status **wired**: benchmark-responsive rubric revision changes the plane's own later scoring/refinement rules, while promoted portfolios change the material supplied to later task trials. This is dispositional wiring, not an assertion that an observed subsequent action depended on the change. Demonstrated improved capacity is **claimed** in README aggregates and **uninspected** as candidate-linked outcome or causal evidence here. Conjectural learning has conclusion status **uninspected**: hypotheses and content-directed rubric-criticism prompts are afforded and their data routes wired, but valid criticism and an attributable improvement in future capacity were not observed.

Reflection has conclusion status **wired** at the narrow assessment-mechanism boundary: the system represents its own current receipt, criterion-level judgments and disagreements; changed criteria update the representation consumed by rubricator/verifier, and receipt revision affects later scoring and refinement. This does not establish a reflective theory builder revising a self-theory of its whole theory-building organization; that stronger property is uninspected. Addressable criteria/files and retained reasons are separate structural findings, not proof of learning.

For a bounded same-task experiment, the most consequential limits are surrogate ties, bounded alignment, lexical verifier fallback, and the refined-winner replay mismatch. For exported skills in new tasks, transfer remains uninspected. Candidate-linked transcripts tracing hypotheses, criticisms, edits and later tests, interventions isolating the rubric revision effect, and a corrected tested refinement-persistence route would change these conclusions. There is no product ranking or Commonplace transfer recommendation.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| External harnesses, task datasets and reference answers excluded | CMP-3, CMP-4, RTE-4, BAP-4 | Superproject interfaces and launch/grading glue | Benchmark correctness, complete grants/isolation, answer provenance and task-level agent behavior | Frozen task/host/image sources and candidate-linked execution |
| No observed rollout or causal comparison | CLM-1, CLM-2, CLM-3, RTE-2, RTE-3 | Static code and README reports | Activation, faithful semantic criticism and attributable capacity gain | Exact traces and suitable interventions |
| Provider weights/version resolution opaque | CMP-2, CMP-4 | Configured inference client and model strings | Exact fixed parameter identity or absence of provider-side changes | Pinned model artifacts or provider version guarantees |
| Scope excludes alternate algorithms and later human deployment | SRC-1, RTE-1 | Flagship portfolio paths only | Repository-wide budget guarantees and cross-task export benefit | Separate frozen analyses of those paths and deployment outcomes |
| Refined winner not represented by persisted initial CandidateRecord | RTE-2, RTE-5, OBJ-5 | Coordinator/refinement and accepted-patch replay | General faithful resume of refined acceptance | Corrected persistence and candidate-linked recovery checks |
| Scalar outcome fit and rank alignment differ from explanatory warrant | OBJ-3, OBJ-4, RTE-3 | Prompt, structural validation and ranking code | Truth of criterion rationale or transfer beyond sampled candidates | Independent tests of named consequences and held-out behavior |

## Verification and blockers

### Semantic verification

Checked canonical seed referents, evidence-layer separation and no observed/causal upgrades. Traced both native flagship adapters and callback alternatives; external responsibilities remain outside their internal implementation boundary. Verified conditional promotion, fixed inner receipt, finite Mode B exit, lexical fallback, context failure, valid reward return, task/fingerprint recovery and initial-patch reconstruction. The recovery mismatch is labelled static inference and does not claim an executed failure. Every material route has return/read-back/selection/invalidation/effect limits and separate behavioral authority. Answer-oracle access is conditional/unknown per benchmark rather than inferred from the word oracle. Theory formulation, operative delivery, criticism, revision and capacity improvement remain separate claims. Memory integration checked all scoped write/consumer branches of RTE-1, RTE-2, RTE-3, RTE-4, RTE-5: event-fed plan/patch/receipt writes qualify separately; no trace compaction was inferred from core-file selection; push selections identify their consumer, trigger, input and retained part; requested state lookup remains pull. Known axis sets aggregate the two adapters and native model selector at the weakest applicable basis; imported payload form and faithful-use evidence remain uncertain. Distilled-form classification concerns inspected outputs, not every opaque imported asset. Receipt/hypothesis rationale delivery does not upgrade semantic use or criticism. Epistemic architectural statuses and candidate states remain independent. No unresolved semantic blocker was found.

### Deterministic validation

Target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-skilllift-01/result.md`. Full structural validation passed cleanly with no warnings or failures. Source quotation occurrence, anchor bounds and workflow byte identities are also checked by the publication preparation step; semantic support was checked above.

### Blockers

None.
