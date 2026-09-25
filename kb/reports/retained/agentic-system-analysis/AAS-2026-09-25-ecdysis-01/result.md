---
type: agentic-system-analysis-result
description: "Ecdysis method-level failure aggregation, collaborative diagnosis, strict score admission and frozen-inference adapter boundaries"
run-id: AAS-2026-09-25-ecdysis-01
system: "Ecdysis"
run-date: "2026-09-25"
result-disposition: complete
target-class: "builder or improvement plane"
boundary-kind: "complete artifact, partial loop"
reviewed-boundary: "cf93866d545b0974dbb0bc83b39c31fbbdeeecb8"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Whole method-level retained-memory boundary: extracted failure evidence, FDCR transcript/specification/checkpoint and continuation, accepted generic HarnessT through training and later inference, decision records, and skill-artifact authoring/storage utilities. Includes opaque harness payloads; excludes internals of external adapters, providers, and task environments. Skill storage has no established task-consumer route."
  axes:
    storage_substrate:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-3, OBJ-4, OBJ-6, OBJ-7]
      note: "Known local stores are in-memory objects and JSON files. HarnessT can carry an opaque external-backed payload; the whole scoped substrate set cannot be completed from its reference container."
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-3, OBJ-4, OBJ-6, OBJ-7]
      note: "Readable diagnostics and skills combine natural-language content with symbolic records. The generic retained harness is consumed alongside these and has no constrained representation."
    lineage:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-3, OBJ-4, OBJ-6, RTE-1, RTE-9]
      note: "Trace extraction and generated diagnosis are wired; skill authoring is afforded. Initial harness provenance and editor transformations are unspecified, preventing a complete whole-boundary set."
    behavioral_authority:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-3, OBJ-4, RTE-1, RTE-2, RTE-3, RTE-9]
      note: "Review history is advisory knowledge; specifications direct the editor; checkpoint metadata controls resumption. The external executor determines the retained harness's actual authority."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic, manual]
      records: [OBJ-6, RTE-1, RTE-2, RTE-4, RTE-9]
      note: "FDCR and training automatically derive and retain material; callers can manually construct and save skills. The manual branch is an API affordance, not observed operation."
    curation_operations:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-4, OBJ-6, RTE-1, RTE-2, RTE-4]
      note: "Prompts afford consolidation of disputes, revision of proposals, and synthesis of diagnoses; accepted candidates replace prior harness references. Opaque editor behavior prevents completing the operation union. Skill identifier collision suppression is not semantic dedup."
    read_back_direction:
      assessment: known
      basis: wired
      values: [push]
      records: [RTE-2, RTE-3, RTE-9]
      note: "The controller supplies retained review history to later roles, cached specifications to the editor, and the retained harness to executors. Skill loading APIs do not establish a named consumer pull route. External adapter-internal retrieval is excluded."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse]
      records: [RTE-2, RTE-3, RTE-9]
      note: "Automatic supply uses the active review's last twelve turns, the current compatible checkpoint, or the entire retained harness. Context-hash checking is cache validation, not semantic targeting; no content-targeted recall selector is implemented."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-1, RTE-2, RTE-9]
      note: "Failure-derived review proposals/specifications can be checkpointed and automatically reused as guidance. Accepted harness references additionally survive to later task execution through generic adapters; skill-file wiring is not needed to establish the checkpoint route."
    trace_source:
      assessment: known
      basis: wired
      values: [trajectories]
      records: [OBJ-1, RTE-1, RTE-2, RTE-9]
      note: "Scored task simulations feed compacted failure records and FDCR summaries. Review dialogue is intermediate derived material in this same route; optional tool-call fields do not establish a separate tool-trace learning route."
    learning_scope:
      assessment: known
      basis: afforded
      values: [per-task, cross-task]
      records: [RTE-1, RTE-2, RTE-3, RTE-9]
      note: "Checkpoint advice continues the same diagnosis task; the retained harness is intended for distinct later execution tasks. Cross-task use is afforded at the external executor interface, while actual generalization is unobserved. No project horizon is established by a scope string."
    learning_timing:
      assessment: known
      basis: wired
      values: [staged]
      records: [RTE-1, RTE-2, RTE-3, RTE-9]
      note: "Failure collection, diagnosis/editing and candidate evaluation are explicit training stages before final inference. Checkpoint continuation occurs inside that diagnosis stage; no task-execution-time learning path is wired in the inference runner."
    distilled_form:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-3, OBJ-4, OBJ-7, RTE-9]
      note: "Checkpointed guidance is natural-language diagnosis in symbolic JSON, but the accepted behavior-shaping HarnessT has opaque form. A symbolic toy revision counter cannot establish the complete learned-form set."
    faithfulness_tested:
      assessment: known
      basis: wired
      values: ["no"]
      records: [CLM-3, ABS-1]
      note: "Within the frozen repository there is no retained execution evidence testing dependence on recalled content. Synthetic tests and reported aggregate gains do not establish recall faithfulness."
---

# Ecdysis agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/ecdysis.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/memory-report.md`
**Memory analysis report SHA-256:** `0596dfa068e1a3a135fd6238da8e8661e8046caac350bd1a9b798c71aef1fb5e`

## Boundary and evidence

Independent characterization of Ecdysis's complete shipped method-level Python library and two CLI interfaces at cf93866d545b0974dbb0bc83b39c31fbbdeeecb8, cutoff 2026-09-25. Target class builder or improvement plane; boundary-kind complete artifact, partial loop. Includes failure extraction/grouping, FDCR diagnosis/specification, generic trainer/admission, retained-harness inference, artifact/checkpoint utilities and benchmark adapter interface. Intended use: distinguish the method's executable controls and epistemic/memory routes from obligations left to external participants.

Collector, candidate editor, scorer, executor, actual task model/environment, benchmark installation and remote review-model internals are supplied externally. The interface and calling code are inspected; their implementations are not. Therefore candidate isolation, actual task permissions, fixed evaluation population, immutable parameters, held-out generalization and deployment safety cannot be assigned to Ecdysis from its adapters' names. Repository docs describe these contracts. Synthetic example/test code is implementation evidence, not an observed training run or causal experiment. Only this pinned repository is allowed evidence; no paper, previous reviews, ingests or other systems are used. No target execution occurs.

## Source register

| ID | Kind and identity/location | Revision | Evidence layer | Inspected scope and anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|
| SRC-1 | Git `https://github.com/cuiyu-ai/Ecdysis`; access root `/home/zby/llm/commonplace/related-systems/cuiyu-ai--Ecdysis` | cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 | Implementation | `src/ecdysis/training.py`, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`, `src/ecdysis/llm_client.py`, artifact/inference/benchmark/CLI code and synthetic example cited below | External adapters and provider internals excluded; wiring is not execution evidence |
| SRC-2 | Git `https://github.com/cuiyu-ai/Ecdysis` | cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 | Doctrine/design | `README.md:1-143`, `src/ecdysis/README.md` and clearly marked docstring claims | Contract compliance and actual freezing/candidate isolation need adapter evidence |
| SRC-3 | Git `https://github.com/cuiyu-ai/Ecdysis` | cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 | Reported operation | `README.md:6` aggregate paper-result claims | No raw trials, fixed-evaluation audit or intervention design inspected; cannot upgrade to observed/causal |

All source reads use commit-addressed blobs at the full revision; worktree/current HEAD is not evidence. No probe capsule is registered because no dynamic check ran.

## Shared records

### Components

CMP-1 — EcdysisTrainer/controller and inference interfaces. Python 3.12/3.13 library; configurable round count, threshold, refinement passes, scope and checkpoint directory. Config enforces positive round/pass count and finite failure threshold. It owns sequence and numeric admission, not task execution or candidate implementation. Conclusion status **wired**, SRC-1 `src/ecdysis/training.py:22-46,95-185`, `pyproject.toml:5-17`.

CMP-2 — FDCR review-model client. Distributed-parametric processing is remote/opaque; local client builds role messages and OpenAI-compatible calls, stores usage events in memory, and selects an arbitrary normalized model string/base URL. Exact immutable model-weight identity **uninspected**; parameter changes during operation **uninspected**; model-name selection **wired**. Prompt changes and retained harness changes are distinct from parameter training. The same supplied client handles Analyst, Critic, Engineer and Moderator; role separation is prompt separation, not independent model evidence. SRC-1 `src/ecdysis/llm_client.py:105-173`, `src/ecdysis/fdcr/review.py:149-305`.

>             "model": self.model,
>             "messages": messages,
>             "temperature": temp,
>         }
>         disable_kwargs = _build_disable_kwargs(self.disable_reasoning, self.base_url)
>         for key, value in disable_kwargs.items():
>             kwargs.setdefault(key, value)
>         for key, value in overrides.items():
>             if value is not None:
>                 kwargs[key] = value
>         return kwargs
> 
>     def usage_event_count(self) -> int:
> --- `src/ecdysis/llm_client.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


CMP-3 — External collector/editor/scorer/executor and task-model/environment adapters. Generic Python callables can run arbitrary supplied code with caller authority. The contract asks collector to keep task model/environment fixed, editor to create an isolated candidate without mutating retained harness, and scorer to compute a fixed training score. Enforcement of those semantic obligations **uninspected**; calling interface **wired**. Any distributed-parametric task model has externally supplied identity/weights; both pinning and parameter changes **uninspected**. SRC-1 `src/ecdysis/training.py:22-28,101-111,116-184`; SRC-2 `README.md:66-82`.

> 
> - `collector(harness)` executes the fixed task model and environment, returning
>   scored trajectory records.
> - `editor(harness, specification, failures, groups)` creates an isolated candidate
>   without mutating the retained harness.
> - `scorer(results)` computes the fixed aggregate training score. The default is
>   the arithmetic mean of available trajectory rewards.
> 
> This separation keeps FDCR responsible for diagnosis and specification, while the
> editor remains responsible for implementation.
> --- `README.md` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


### Operative objects

OBJ-1 — Scored task trajectories and extracted failures. Dictionaries or JSON files have tasks/simulations, scalar rewards/breakdowns, termination reasons, trial/task IDs and messages. Collector supplies facts and scoring provenance. Extraction includes only reward below threshold, skips missing rewards, defaults to last 80 messages and first 2,000 characters of each content field; tool-call arguments are retained separately. Thus content caps do not bound full payload/tool-argument size. Form is mixed natural-language trace and symbolic fields; runtime list state is in memory, optional upstream files external. SRC-1 `src/ecdysis/evolution.py:14-138`. Conclusion status **wired** for extraction; recorded reward truth **uninspected**.

>             continue
>         reward = _reward(simulation)
>         if failures_only and (reward is None or reward >= failure_threshold):
>             continue
> 
>         task_id = str(simulation.get("task_id"))
>         raw_reward_info = simulation.get("reward_info")
>         reward_info = raw_reward_info if isinstance(raw_reward_info, dict) else {}
>         raw_messages = simulation.get("messages")
>         messages = raw_messages if isinstance(raw_messages, list) else []
>         selected_messages = messages[-max_messages:] if max_messages else []
>         item = {
>             "task_id": task_id,
>             "trial": simulation.get("trial"),
>             "reward": reward,
>             "termination_reason": simulation.get("termination_reason"),
>             "reward_breakdown": reward_info.get("reward_breakdown"),
>             "task": tasks.get(task_id, {}),
>             "messages": [
>                 _compact_message(message, max_content_chars)
>                 for message in selected_messages
>                 if isinstance(message, dict)
>             ],
> --- `src/ecdysis/evolution.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


OBJ-2 — Grouped recurring/singleton evidence. Key is termination reason plus sorted reward-breakdown components whose values are below 1.0. Groups sort by distinct task count, then failures/key. This is a syntactic grouping predicate, not independently established causal equivalence of failures. Distinct task IDs supply the recurrence count; missing/shared IDs and repeated trials affect interpretation. SRC-1 `src/ecdysis/evolution.py:166-192`; FDCR labels >=2 distinct task IDs recurring and one auxiliary in `src/ecdysis/fdcr/review.py:31-63`.

> 
> 
> def group_failures_by_pattern(
>     failures: list[dict[str, Any]],
> ) -> dict[str, list[dict[str, Any]]]:
>     """Group failures by termination reason and failed reward components."""
>     groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
>     for failure in failures:
>         termination = str(failure.get("termination_reason") or "unknown")
>         breakdown = failure.get("reward_breakdown") or {}
>         failed_components = sorted(
>             str(key)
>             for key, value in breakdown.items()
>             if value is not None and float(value) < 1.0
>         )
>         component = "+".join(failed_components) or "no_breakdown"
>         groups[f"{termination}:{component}"].append(failure)
>     return dict(
>         sorted(
>             groups.items(),
>             key=lambda item: (
>                 -len({row.get("task_id") for row in item[1]}),
>                 -len(item[1]),
>                 item[0],
>             ),
> --- `src/ecdysis/evolution.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


OBJ-3 — FDCR role transcript and moderator modification specification. Prose turn contents plus structured dictionary fields failure_patterns/proposed_changes/skills/implementation_notes. Proposed changes are requested to include component, description and rationale. The returned object is advisory implementation guidance consumed by external editor; provenance is compact failure context and earlier role replies. Parsing normalizes fields but does not validate semantic support or deep schemas. SRC-1 `src/ecdysis/fdcr/review.py:67-133,201-305`; SRC-2 `src/ecdysis/fdcr/roles.py:12-41`.

OBJ-4 — Retained/candidate/final generic HarnessT object. Its form, persistence, contents and effects depend on the external adapter; the trainer holds and reassigns a Python reference. Do not infer all harnesses are prompt files or symbolic dicts from the synthetic example. New candidate only replaces current reference on strict score improvement; external mutation can affect that reference before the comparison. SRC-1 `src/ecdysis/training.py:113-185`, `src/ecdysis/inference.py:107-151`; detailed memory disposition follows.

OBJ-5 — RoundRecord and TrainingResult records. Frozen dataclass wrappers retain numeric baseline/candidate/retained scores, counts, accepted flag and status; result contains the generic object reference and tuple of rounds. Frozen wrappers do not recursively freeze the referenced harness. A no-failures round records status and continues to the configured next round. Source SRC-1 `src/ecdysis/training.py:49-91,116-185`.

> 
> @dataclass(frozen=True)
> class TrainingResult[HarnessT]:
>     """Frozen harness and the decisions that produced it."""
> 
>     frozen_harness: HarnessT
>     final_score: float
>     rounds: tuple[RoundRecord, ...] = field(default_factory=tuple)
> 
>     def infer(
>         self,
>         task: TaskT,
>         executor: Executor[HarnessT, TaskT, OutputT],
>     ) -> OutputT:
>         """Execute a task with the frozen harness without further adaptation."""
>         return executor(self.frozen_harness, task)
> --- `src/ecdysis/training.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


OBJ-6 — EvolvedSkill and SkillArtifact reusable-skill structures. A readable pattern/tip/title with IDs, task sources, issue type and metadata; versioned collection adds experiment/scope/round/mode/time/parents. Load/save/merge APIs are separate from the generic trainer. Artifact label learned is a claim about origin, not proof of training or later use. Source SRC-1 `src/ecdysis/artifacts.py:14-154`, `src/ecdysis/evolution.py:241-264`.

Memory annotation for OBJ-1 — Scored trajectories and extracted failures. Implementation conclusion status: wired. SRC-1, `src/ecdysis/evolution.py:14-23,26-48,67-152`. Collector-supplied dictionaries or JSON result files contain task simulations; extraction derives in-memory records with task metadata, trial, reward, breakdown, compacted message evidence and failure diagnostics. The JSON/Python envelope is symbolic; message text is natural language and tool arguments can be structured. Raw-to-derived provenance uses task and trial identifiers, without cryptographic source identity. These are evidence to the editor; only summaries reach FDCR. Successful/all-trajectory extraction is available but is not used by the trainer's failure route.

Memory annotation for OBJ-2 — Failure groups. Implementation conclusion status: wired. SRC-1, `src/ecdysis/evolution.py:168-192`, `src/ecdysis/fdcr/review.py:37-47`. Keys combine termination reason and sorted failed reward components. Groups retain member failure records and sort by distinct-task coverage and size. These are access/grouping structures plus retained evidence, not a semantic vector index. A recurring label means at least two distinct task identifiers, not a demonstrated common cause. Singleton groups are kept as auxiliary evidence; there is no enforced recurrence-only admission gate.

>         evidence_role = "recurring" if len(task_ids) >= 2 else "auxiliary"
>
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

Memory annotation for OBJ-3 — FDCR review and modification specification. Implementation conclusion status: wired. SRC-1, `src/ecdysis/fdcr/review.py:65-133,194-269,292-346`, `src/ecdysis/fdcr/roles.py:12-40`. In-memory role/content dialogue and optional JSON persistence hold generated diagnosis, objections, dispute summaries, proposed edits and skills. Moderator output requests rationale for each proposed change. Reasons survive if returned by the model; the parser preserves lists but does not enforce each change's nested schema or nonempty rationale. These artifacts advise later reviewers and direct the external editor; actual model attention is unobserved.

>         "  proposed_changes: list of {component, description, rationale}\n"
>         "  skills: list of {id, title, pattern, tip}\n"
>         "  implementation_notes: string for the coding agent\n"
>
> --- `src/ecdysis/fdcr/roles.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

Memory annotation for OBJ-4 — Retained, candidate and final generic harness. Implementation conclusion status: wired for references and delivery; external meaning is uninspected. SRC-1, `src/ecdysis/training.py:18-28,64-91,112-185`, `src/ecdysis/inference.py:106-154`. A generic object initially supplied by the caller is replaced by an editor-returned object after score admission and stored in `TrainingResult`. No serialized harness checkpoint or mandated skill conversion is implemented. Representation, external backing storage, internal provenance, rationale retention and authority at task execution cannot be inferred from `HarnessT`. The synthetic integer/dictionary harness illustrates an interface, not all permitted payloads.


Memory annotation for OBJ-5 — RoundRecord/TrainingResult decisions. Implementation conclusion status: wired. SRC-1, `src/ecdysis/training.py:50-70,167-185`. In-memory frozen dataclass records preserve baseline/candidate/retained scores, failure/group counts, acceptance and status. They omit the actual review, reason for each proposed edit, harness identity and links to checkpoint contents. TrainingResult preserves the harness reference and tuple of round records. The trainer does not use these records as a later review history or persist them automatically.

Memory annotation for OBJ-6 — EvolvedSkill/SkillArtifact. Implementation conclusion status: afforded. SRC-1, `src/ecdysis/artifacts.py:11-117,120-154`, `src/ecdysis/evolution.py:242-263`. Mutable Python dataclasses and JSON files retain readable pattern/tip text, IDs, scope, round, creation time, source task IDs and optional metadata. A helper can convert caller-supplied model dictionaries into artifacts. No automatic producer connects FDCR's `skills` list to that helper. Required strings support basic structural validity; optional source identifiers are not checked against evidence. `schema_version` is a stored integer, not a migration/history system. Parent metadata copies existing parent lists; merge does not automatically add the merged input artifact's own identity. A skill has no required rationale field, and metadata merely permits one.

OBJ-7 — FDCR checkpoint state, distinct from OBJ-3's semantic content. Implementation conclusion status: wired. SRC-1, `src/ecdysis/fdcr/review.py:24-28,165-200,202-247,275-309`. The optional JSON file contains input-context hash, model, round count, status, next turn, dialogue, final spec and usage segments. Atomic temporary-file replacement persists progression and errors. It is both derived guidance storage and resume-control metadata. Its source identity check is limited to rendered context, not raw evidence. `save_fdcr_transcript` offers another JSON export but has no corresponding automatic restore route.

The progress representation changes after a successful reviewer turn and governs later continuation through RTE-9. This supplies a narrow causal self-representation of review progress, not a validated theory about the harness.

> state["transcript"] = transcript
> state["next_turn_index"] = turn_index + 1
> state.pop("error", None)
> if checkpoint_path:
>     _write_checkpoint(checkpoint_path, state)
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

#### Retention evidence and context boundary

Ecdysis retains diagnosis and a candidate-selected harness through different routes. Failure records supply FDCR with a lossy summary of batch patterns. The controller then hands a generated specification to an external editor and retains the candidate only on a strictly higher score. The final harness object is later passed to a task executor. The implemented connection is object delivery; what that object means to the executing agent remains delegated.

Evidence from SRC-1, `src/ecdysis/training.py:152-165`:

>             specification = analysis["review"]["spec"]
>             candidate = self.editor(
>                 current_harness,
>                 specification,
>                 failures,
>                 groups,
>             )
>             candidate_score = self.scorer(self.collector(candidate))
>             baseline_score = current_score
>             accepted = candidate_score > baseline_score
>             if accepted:
>                 current_harness = candidate
>                 current_score = candidate_score
>
> --- `src/ecdysis/training.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

The FDCR checkpoint is a second real retention mechanism. It records completed role turns, next-turn position, and final specification. A compatible interrupted checkpoint resumes a diagnosis using saved dialogue. A compatible completed checkpoint returns its prior specification without fresh review. This supports retained behavior-shaping guidance independently of whether a deployed editor consumes a skill file.

Evidence from SRC-1, `src/ecdysis/fdcr/review.py:178-188`:

>     if checkpoint_path and checkpoint_path.exists():
>         state = json.loads(checkpoint_path.read_text())
>         if state.get("context_hash") != context_hash or state.get("model") != model:
>             raise RuntimeError(
>                 f"FDCR checkpoint input/model mismatch: {checkpoint_path}"
>             )
>         if state.get("status") == "completed":
>             return {
>                 "transcript": list(state.get("transcript") or []),
>                 "spec": _parse_moderator_spec(state.get("spec")),
>
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

FDCR sees less evidence than the editor. Extraction preserves compacted messages and selected tool-call fields, but the FDCR formatter emits cluster counts, up to eight task identifiers per cluster, and at most twelve failure score/termination summaries. It emits no message bodies or tool arguments. All clusters remain represented, so there is no global token budget. This is deterministic summarization of scores, not semantic retrieval from a growing knowledge store. SRC-1, `src/ecdysis/evolution.py:26-48,67-136`, `src/ecdysis/fdcr/review.py:31-62`:


Provenance is partial: task IDs, trials, scores, failure components, scope and review model are retained where the relevant record includes them. The checkpoint hash covers the rendered context and number of passes, with model string checked separately. It does not bind the complete raw trajectories, prompt definitions, editor, scorer, harness or provider configuration. Human intervention is possible through supplied harnesses, adapters and JSON files, but there is no approval queue or authenticated edit history in the package. Source guidance against evaluation changes is a prompt/adapter obligation, not a sandbox.

### Routes

RTE-1 — Collect/refine/edit/validate training. Trigger: caller invokes train(initial_harness); owner: deterministic configured loop. It collects current results each round, scores them, extracts failures, runs RTE-2 on failures, gives current harness plus specification/full failure/group records to editor, then evaluates candidate through the same collector/scorer callables. Candidate score strictly greater than this round's baseline replaces current reference and score; otherwise baseline reference remains. Return: TrainingResult and recorded per-round comparisons. Status **wired**, guarantee strength **protocol** for reference selection/numeric comparison. Source SRC-1 `src/ecdysis/training.py:113-185`.


For RTE-1, proposer of substantive change is external editor guided by FDCR specification, failures and groups; moderator/model proposes diagnostic content, fixed comparison owns admission and can reject, caller decides adapters/config and can stop by exception. No human approval step is wired in this loop. No copying, recursive freeze, sandbox, model pinning or task-population equality check is performed by the shown controller. A contract-compliant isolated editor is required for rejection to preserve the incumbent's content; there is no rollback of an editor's in-place mutation or external effects. All collected results and candidate evaluation can depend on caller state. Scorer default is mean of available rewards; missing rewards are excluded, and no scored rewards raises. Finite threshold validation does not establish finite baseline/candidate scores or held-out validity. Control-flow acceptance says nothing by itself about causal attribution or future generalization. Re-collecting the retained harness at every round can change its reported baseline/final score even without a harness change; the code does not establish a globally monotone score history across stochastic or changing evaluations.

Guidance proposes minimal changes to recurring runtime failures, asks for affected component/rationale and prohibits changing tasks/evaluation by prompt policy. Formulated proposed explanations/solutions are **afforded**; model calls to produce/criticize them are **wired**, but a particular valid theory, substantive criticism and improved capacity remain **uninspected** without content/run evidence. Operative use of the structured specification is **wired** as an editor argument; its actual interpretation is **uninspected**. Revision selection is numeric training fit, while cross-task reach is prompted preference, not independently enforced admission. Retention/later consumption of opaque harness changes is mapped by memory lens. Assertions such as rationale are not established facts merely because accepted score rises.

RTE-2 — FDCR multi-role diagnosis and moderator refinement. Trigger: failure list/groups plus client/scope/passes. Owner: deterministic turn plan Analyst→Critic→Engineer for each pass, then Moderator. Context is group counts/distinct IDs and up to twelve failure scalar summaries; earlier transcript last twelve turns is included on each model call. Although extracted OBJ-1 includes message/tool traces and tasks, `_format_failure_context` does not put their contents or actual harness code into FDCR messages. This limits the information supporting a proposed causal diagnosis. Singleton groups stay auxiliary; they are not filtered out nor barred from editing by a hard gate. Status **wired** for orchestration, **policy** for cross-task/minimality/anti-leakage advice. SRC-1 `src/ecdysis/fdcr/review.py:31-63,73-133,163-305`; SRC-2 `src/ecdysis/fdcr/roles.py:12-41`.

>     for f in failures[:12]:
>         sample.append(
>             f"  task={f.get('task_id')} trial={f.get('trial')} "
>             f"reward={f.get('reward')} term={f.get('termination_reason')} "
>             f"breakdown={f.get('reward_breakdown')}"
>         )
>     scope_line = f"Task scope: `{scope}`\n" if scope else ""
>     return (
>         f"{scope_line}"
>         f"## Failure clusters ({len(groups)})\n"
>         + "\n".join(group_lines)
>         + "\n\n## Sample failures\n"
>         + "\n".join(sample)
>     )
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


>     ROLE_CRITIC: (
>         "You are the Critic. Challenge the Analyst's proposals: overfitting "
>         "to single tasks, false-positive triggers, blocking valid actions, "
>         "violating runtime contracts, harming previously successful "
>         "trajectories, or introducing behavior that depends on incidental "
>         "conversation order. Be specific and constructive."
> --- `src/ecdysis/fdcr/roles.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


For RTE-2, Analyst proposes, Critic challenges overfit/false triggers/blocked valid actions/contracts/regressions/order dependence, Engineer records agreement/dispute, and Moderator synthesizes fields. Later Analyst turns are asked to address objections. All use the same client; final Engineer still gets a call with no-action instruction, then Moderator follows. Moderator prompt says full transcript, but actual assembly uses transcript[-12:], so larger configured pass counts can omit early review turns. JSON parsing may return none; `_parse_moderator_spec` then produces empty fields and the trainer still invokes editor. Nested change entries and evidence sufficiency are not structurally certified by that normalization. Criticism is explicitly sought about proposal content; whether a specific reply formulates useful criticism or whether the editor uses it remains uninspected. Immediate output transcript/spec/usage; optional persistence and resumed read-back are the specialist's checkpoint route.

> 
> 
> def _parse_moderator_spec(parsed: dict[str, Any] | None) -> dict[str, Any]:
>     if not isinstance(parsed, dict):
>         return {
>             "failure_patterns": [],
>             "proposed_changes": [],
>             "skills": [],
>             "implementation_notes": "",
>         }
>     return {
>         "failure_patterns": list(parsed.get("failure_patterns") or []),
>         "proposed_changes": list(parsed.get("proposed_changes") or []),
>         "skills": list(parsed.get("skills") or []),
>         "implementation_notes": str(parsed.get("implementation_notes") or ""),
>     }
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


RTE-3 — Final-harness inference and external benchmark interface. TrainingResult.infer passes the retained reference and task to caller executor; batch InferenceRunner sequentially calls the same executor and records output/error/time. It runs no trainer adaptation routine. Default retains failed tasks; fail_fast raises rather than returns completed batch. Benchmark wrapper obtains tasks/execute/encoder/name/version from external adapter, writes metadata on each JSONL line; name/version are supplied strings, not verified provenance. The CLI dynamically imports caller-selected adapter/harness factories. Status **wired**, guarantee strength **protocol** for wrapper flow; mutation-free execution is an external contract. SRC-1 `src/ecdysis/training.py:63-91`, `src/ecdysis/inference.py:107-154`, `src/ecdysis/benchmark.py:73-138`.

>         for index, task in enumerate(tasks):
>             started = perf_counter()
>             try:
>                 output = self.executor(self.harness, task)
>             except Exception as exc:
>                 record = InferenceRecord(
>                     index=index,
>                     task_id=self.task_id(task, index),
>                     task=task,
>                     output=None,
>                     elapsed_seconds=perf_counter() - started,
>                     error=f"{type(exc).__name__}: {exc}",
>                 )
>                 records.append(record)
>                 if fail_fast:
>                     raise
>             else:
>                 records.append(
>                     InferenceRecord(
> --- `src/ecdysis/inference.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


For RTE-3, the principal is invoking user/program; dynamic imports/executors own effect authority and model/environment selection. Capability surface is arbitrary Python adapters, actual grant set/isolation deployment **uninspected**. The frozen dataclass blocks field assignment, not mutation inside a generic dict/object or executor side effects. Execution result means no raised exception, not correct answer: benchmark encoding does not add an answer oracle or outcome evaluator. Optional JSONL result persistence is export, not a wired adaptation route. Stable task ID falls back to ordinal index and has no inspected uniqueness enforcement. Later return consumers and task-model context are adapter-owned; expiry/read-back in model is not inferred.

RTE-4 — Reusable artifact load/save/merge. Standalone APIs validate required fields, optional scope equality, serialize files and keep first skill per ID on load/merge. This is identity collision suppression, not demonstrated semantic consolidation. Source SRC-1 `src/ecdysis/artifacts.py:28-154`, `src/ecdysis/evolution.py:241-264`. Memory specialist traces consumer coverage separately.

Memory annotation for RTE-1 —Training collection, diagnosis, edit and score admission. Implementation conclusion status: wired at method interfaces. SRC-1, `src/ecdysis/training.py:112-185`; SRC-2, `README.md:67-79`. Each configured round collects scores with the current harness, extracts failures, invokes FDCR, supplies specification plus fuller failure/group records to the editor, evaluates the candidate and conditionally replaces the retained reference. Default rounds are three, default refinement passes two, failure threshold one. No-failure rounds continue rather than terminate; standalone convergence/regression helpers do not control this loop. Reasons can reach the editor in the specification, but their use and retention in the revised harness are uninspected. Candidate isolation and fixed scoring are adapter contracts.

Memory annotation for RTE-2 — Collaborative FDCR. Implementation conclusion status: wired for supplied context and prompts. SRC-1, `src/ecdysis/fdcr/review.py:31-133,194-269`, `src/ecdysis/fdcr/roles.py:10-40`. For every pass the controller calls Analyst, Critic and Engineer, then calls Moderator once. The generator sends a static role instruction, current failure summary and the most recent twelve role turns. The Engineer still receives a call on the last pass with a no-action instruction. Revising proposals, summarizing disputes and deriving changes are requested transformations; actual epistemic success is not demonstrated. Generated reasons can be consumed by later reviewer prompts. The bounded dialogue window may omit earlier reasons for more than four passes, despite the Moderator prompt saying to read the full transcript.

>     history = "\n\n".join(
>         f"### {t['role'].upper()}\n{t['content']}" for t in transcript[-12:]
>     )
>
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

Memory annotation for RTE-3 — Later inference and benchmark delivery. Implementation conclusion status: wired at adapter boundary; task behavior is afforded. SRC-1, `src/ecdysis/training.py:72-91`, `src/ecdysis/inference.py:106-154`, `src/ecdysis/benchmark.py:20-30,72-89,99-126`; SRC-2, `README.md:81-124`. Calling inference supplies the entire retained harness on every task with no retrieval request by the task executor and no per-task memory selector. Benchmark CLI constructs a harness through a caller-specified factory, not a built-in learned-harness loader. JSONL inference results are output records, with no wired return to training. Frozen means no adaptation call in these wrappers; it does not enforce object immutability or prevent executor mutation.


Memory annotation for RTE-4 — Skill authoring/load/save/merge capabilities. Implementation conclusion status: afforded. SRC-1, `src/ecdysis/artifacts.py:27-117,120-154`, `src/ecdysis/evolution.py:242-263`. Callers provide objects, dictionaries or file paths; helpers return records and optionally write files. Scope equality can reject incompatible artifacts; first occurrence of an ID wins during loads/merges. There is no semantic similarity comparison, conflict correction or replacement of an existing same-ID skill by a new skill. The exact artifact-symbol search in the search ledger, combined with the inspected trainer, review, inference and CLI entry points, establishes no package-wired consumer route from these helpers to the trainer, FDCR or executor within the frozen package. The only outside-definition call sites are synthetic artifact tests. External factory or executor implementations could supply a route, but they are excluded and uninspected. Thus task read-back remains unestablished at this boundary: the API is storage capability, not a supported pull route or evidence of learned skills in task prompts.

>         for skill in artifact.skills:
>             if skill.id not in seen_ids:
>                 seen_ids.add(skill.id)
>                 skills.append(skill)
>
> --- `src/ecdysis/artifacts.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

RTE-9 — automatic checkpoint continuation and completed-spec reuse. Implementation conclusion status: wired. SRC-1, `src/ecdysis/training.py:140-151`, `src/ecdysis/fdcr/review.py:165-247,292-309`. Trigger: FDCR invocation with an existing checkpoint path. Selection inputs: current rendered summary, pass count, model string and supplied path; trainer derives path from round number. A mismatch raises. A completed state returns prior spec to RTE-1; an interrupted state resumes from the saved next turn and sends the recent dialogue through RTE-2. Persistence is automatic when configured, absent by default. Selector is coarse continuation of the current diagnosis. Delivered critique/reasons may guide later diagnosis, while actual use remains unobserved. Pending/running state is updated per turn, and failure state is retained before raising. No retention expiry, invalidation history or cross-input migration is implemented.

>     context_hash = hashlib.sha256(f"{rounds}\0{context}".encode()).hexdigest()
>
> --- `src/ecdysis/fdcr/review.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

#### Memory write and rationale audit

Automatic acquisition begins with the external collector. The built-in transformation drops unscored or sufficiently rewarded trajectories on the failure branch, takes the last eighty messages by default and truncates each message's content to two thousand characters. Tool arguments are preserved without the same character cap. Full task dictionaries and optional failure metadata remain, so neither the failure object nor the eventual editor input has a strict total-size bound. RTE-1 uses the defaults; the extraction API and CLI expose some controls. This is evidence compaction, not a separately wired continuation memory: the compacted record is used in the current diagnosis/edit stage, and the standard model-review path does not receive its messages. SRC-1, `src/ecdysis/evolution.py:26-48,67-136`, `src/ecdysis/__main__.py:22-44`.

The RTE-2 path transforms scored trajectory summaries into proposals, criticism, dispute summaries and a structured modification specification. The Engineer's consolidation reduces discussion into agreements/disputes; Analyst revision can evolve prior proposals; deriving a proposed causal repair synthesizes a claim beyond score records. These are afforded by explicit model instructions; the actual returned text may fail to perform them. Ordinary grouping and same-ID suppression do not establish semantic curation. When checkpointing is configured, this generated advice is durable in OBJ-7 and later re-enters a reviewer or editor consumer through RTE-9. A saved raw transcript alone would not suffice; it is the inclusion of generated proposals/summaries and their resumed delivery that establishes the qualifying route.

For RTE-1 then asks the external editor to produce an isolated candidate, and score comparison decides retention. Code passes the current object directly and does not copy it. An editor that mutates it in place could change the retained harness even when its returned candidate loses. The final frozen dataclass prevents reassignment of its fields through ordinary dataclass assignment but does not deep-freeze the referenced object; the inference runner also keeps a mutable attribute. These are enforcement limits on the memory update boundary, not evidence that a particular adapter violated it. SRC-2, `README.md:71-79`; SRC-1, `src/ecdysis/training.py:64-78,152-165`, `src/ecdysis/inference.py:109-131`.

The concrete reason-retention chain stops at distinct boundaries. OBJ-3 can retain a change rationale; later RTE-2 turns see review reasons in the recent transcript; RTE-9 returns stored specification reasons to the editor on completed-cache reuse. RTE-1 passes the whole specification without inspecting a rationale. No package code confirms that the editor uses reasons or copies them into OBJ-4. OBJ-5 records admission scores but no rationale. OBJ-6's pattern/tip/source fields do not require an explanation of why the skill works. The optional renderer prints change rationales, but no in-package caller wires its output into a coding agent. SRC-1, `src/ecdysis/fdcr/review.py:120-133,178-192,320-346`, `src/ecdysis/artifacts.py:18-25`, `src/ecdysis/training.py:50-70,152-159`.

No automatic forgetting, expiry, rejection log for malformed skill contents, or withdrawal of previously accepted harness behavior appears in the inspected routes. Rejection leaves the retained reference in place if the editor obeys isolation. Checkpoint mismatch refuses reuse rather than migrating or marking old advice invalid. Skill merge retains the first same-ID skill and provides no semantic deduplication or overwrite-based evolution. These bounded findings do not constrain what an excluded external editor could implement.

#### Memory read-back audit

The named FDCR model roles receive recent retained dialogue automatically from the controller. The trigger is a scheduled role turn; selection is the last twelve transcript entries; delivery is a user message alongside failure summaries and a role system instruction. There is no role-issued retrieval query, embedding lookup or per-failure semantic match. Stored role identifiers label displayed turns but do not select only matching roles. This is coarse push.

The RTE-9 path reloads checkpoint state on the next matching invocation. Interrupted states supply dialogue to that same automatic assembly. Completed states deliver the cached spec into RTE-1's editor input without model re-review. A match validates the cache's summarized input identity; it does not prove all underlying evidence is unchanged. Changing omitted message contents, task details, reward basis or unsampled failure details can leave the checkpoint identity unchanged when the rendered summary stays identical. Hash coverage and path reuse therefore limit trust in stale-content detection. No source mutation or probe is required for this code-level inference.

For RTE-3 supplies the retained harness wholesale to each task executor. This is coarse push at the inspectable interface; the executor's internal prompt building, code execution or parameter use is outside scope. Calling `infer` requests task execution, not retrieval of particular memory entries. No activation guarantee follows from passing an object to an opaque executor. RTE-4 remains capability-only because there is no named consumer or documented adoption procedure connecting loaded skills to later task behavior. Benchmark factory loading similarly delegates harness construction/persistence rather than supplying a built-in learned-artifact pipeline.

Availability, delivery and benefit are thus separate: skill files are available through helpers; checkpoint advice and retained harness references are delivered through identified routes; synthetic examples illustrate value flow; reported aggregate benefits are claims without inspected causal evidence. No source in the allowlist establishes model dependence on recalled rationale or a particular memory representation.

RTE-5 — Analysis-only CLI. `ecdysis results.json` extracts/group failures and prints aggregate failure count plus groups/counts/task counts. No FDCR/model/client or candidate editor is called by this entry path. Input file/optional max_messages and deterministic helpers determine result; no persistent learned state is written by this CLI body. Status **wired**; immediate return stdout and success code; later learned-memory consumption **uninspected**, not established by printing. Source SRC-1 `src/ecdysis/__main__.py:12-46`.

RTE-6 — Review-model request/retry and response parsing. Caller passes model/base URL/key config; local code sends system/user messages with chosen temperature and provider-specific reasoning-disabled body when configured. Rate-limit/connection errors retry up to configured attempts with exponential sleep; other APIError raises RuntimeError. API key availability is required before real calls. Completed usage/model/attempt/duration/token events retained in memory; no request credential values are used as evidence here. Chat-json requests JSON object then permissively extracts braces/optional fences and removes trailing commas on parse repair; invalid JSON returns None, passed to RTE-2 defaults. Status **wired**, best-effort network/reliability guarantee; SDK retries/provider hidden state **uninspected**. SRC-1 `src/ecdysis/llm_client.py:37-100,116-173,188-247`.

>                 sleep_for = self.retry_backoff ** attempt
>                 logger.warning(
>                     "LLM transient error (attempt %d/%d): %s; retrying in %.1fs",
>                     attempt,
>                     self.max_retries,
>                     exc,
>                     sleep_for,
>                 )
>                 time.sleep(sleep_for)
>             except APIError as exc:
>                 raise RuntimeError(f"LLM API error: {exc}") from exc
>         raise RuntimeError(f"LLM call failed after retries: {last_exc}")
> 
>     def chat_json(
>         self,
> --- `src/ecdysis/llm_client.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


RTE-7 — Standalone score stability utilities. check_convergence compares score deltas in a caller-supplied window with a threshold; check_regression compares before/after drop with tolerance. They afford a returning Boolean calculation, not a wired trainer early-stop or candidate veto: the inspected trainer's acceptance and configured round loop are RTE-1. Immediate return is scalar; no retained-state write, delegated visibility or later memory read-back within these functions. Caller can use the result externally, but no stronger consumer is established. Status **afforded** for external integration; implementation **wired** for calculation. Source SRC-1 `src/ecdysis/evolution.py:267-291`, `src/ecdysis/training.py:113-185`.

RTE-8 — Standalone transcript export/specification rendering. save_fdcr_transcript writes caller-provided payload as JSON; format_update_spec returns Markdown containing failure patterns, proposed components/descriptions/rationales, skills and implementation notes, ending with a minimal/test-safe edit instruction. Status **afforded** for use as editor input, **wired** for serialization/rendering. Neither helper's body calls a coding agent, and trainer passes the dictionary directly. File export has no automatic restore consumer through this function; checkpoint restore is a separate route. SRC-1 `src/ecdysis/fdcr/review.py:312-346`. These formatting writes do not admit a new harness revision or independently warrant its rationale.

#### Route return/read-back/effect audit

| Route | Return and retention | Later consumer, selection and delegated visibility | Expiry/recovery/effect limits |
|---|---|---|---|
| Audit of RTE-1 | TrainingResult reference and round tuple; optional review checkpoint | Next round receives current harness; editor gets full selected spec/failures/groups; inference gets final reference | Rejection preserves reference only with isolated editor; new evaluations can change reported baseline; exception propagates |
| Audit of RTE-2 | Transcript/spec/usage; optional persistent state | Scheduled role gets last twelve turns plus scalar context; editor gets spec | Bounded dialogue may omit early reasons; empty normalized spec is allowed; model success unobserved |
| Audit of RTE-3 | Per-task output/error/time; optional JSONL | Caller receives batch; external executor gets entire harness on each task | No model-memory selector; external mutation/side effects uninspected; fail_fast raises |
| Audit of RTE-4 | Loaded/merged artifact objects or saved JSON | Caller receives records; no named automatic task-model consumer established | Scope mismatch rejects, first ID wins; no semantic conflict correction or automatic validity expiry |
| Audit of RTE-5 | Printed group/count summary | Invoking CLI user/program | No retained learned artifact or adaptation call in body; input errors propagate |
| Audit of RTE-6 | Reply/parsed object or exception; completed usage events in client | RTE-2 consumes text/spec; checkpoint persists selected outputs | Bounded retries cover selected API errors; credentials/provider internals external |
| Audit of RTE-7 | Boolean arithmetic result | External caller may integrate, trainer does not call it | No persistence, memory expiry or automatic operational effect in helper |
| Audit of RTE-8 | JSON export or rendered implementation text | Caller gets file/path/string; no wired coding-agent consumer | Export not resume; no independent acceptance or source-validation guarantee |
| Audit of RTE-9 | Resumed transcript/spec or input/model mismatch error | Automatic recent-history supply to role or cached spec to editor | Context hash covers summary/rounds plus model check only; no full-source identity, expiration or safe external-effect rollback |

### Claims

CLM-1 — Source says recurring failures across distinct tasks offer stronger evidence of systematic harness deficiencies than isolated model failures. Conclusion status **claimed**, SRC-2 `README.md:6,10-20`. Implementation supports grouping/prioritization and structured critique, not empirical causal diagnosis from recurrence alone. Source includes all auxiliary groups and only exposes compact scalar summaries to FDCR.

> Each training round follows the paper's acceptance loop:
> 
> 1. Collect trajectories with the currently retained harness.
> 2. Mark a trajectory as failed when its fixed score is below `failure_threshold`.
> 3. Aggregate structured failure evidence and prioritize patterns recurring across
>    distinct task instances; singleton patterns remain auxiliary evidence.
> 4. Run Failure-Driven Collaborative Refinement (FDCR) for `refinement_passes`.
> 5. Pass the structured specification to an isolated candidate editor.
> 6. Retain the candidate only when its training score strictly improves.
> 
> After the final round, the retained harness is frozen for inference.
> --- `README.md` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`


CLM-2 — Candidate retained only when training score strictly improves, then final harness frozen for inference. Numeric comparison and no additional trainer call in wrappers **wired**; deep immutability, candidate isolation and fixed evaluation semantics **claimed** as adapter contract, not supplied by frozen dataclass. SRC-1 `src/ecdysis/training.py:113-185,63-91`; SRC-2 `README.md:18-20,66-89`.

CLM-3 — README reports 18.56% reasoning accuracy improvement over existing evolution, up to 1.84x faster harness training and cross-model/data/token benefits. Conclusion status **claimed**, SRC-3 `README.md:6`; no local experiment evidence, causal design or reproduction supports upgrading those outcomes.

> Across multiple LLMs and benchmarks, \textsc{Ecdysis} improves the reasoning accuracy of evolved harnesses by 18.56\% over existing harness evolution while achieving up to 1.84$\times$ faster harness training.
> --- `README.md` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

The bounded memory evidence finding is ABS-1. It does not assess experiments outside this repository.

### Evidenced absences

ABS-1 —no inspected recall-dependence execution test. Conclusion status: absent within frozen repository evidence. SRC-1, `examples/quickstart.py:8-25,28-60`, `tests/test_training.py:36-71`, `tests/test_evolution_checkpoint.py:19-42,45-86`. The inspected synthetic editor ignores the specification and evidence; fake reviewers ignore their message input. Checkpoint tests assert continuity and call counts; they do not test task performance dependence on recalled reasons. No tests were executed for this analysis. The complete 23-file inventory and exact evidence query are retained in the search ledger. All seven test files were inspected; their only data are synthetic fixtures and assertions, with no persisted run outcomes. The README has an expected-output example and aggregate performance claims, but no recall-dependence result. Consequently the frozen source boundary contains no retained observed recall-dependence execution evidence. This bounded absence supports `faithfulness_tested: no`; it says nothing about excluded local outputs or the external paper.

> def edit(harness, _specification, _failures, _groups):
>     return {"revision": harness["revision"] + 1}
>
> --- `examples/quickstart.py` @ `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`

#### Bounded absence search

All commands below were executed against full revision `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`, with replacement objects disabled. They inspect source blobs, not the worktree or current HEAD.

The complete inventory command supporting ABS-1 was:

```bash
git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/cuiyu-ai--Ecdysis ls-tree -r --name-only cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
```

Its complete output was:

```text
.gitignore
README.md
examples/quickstart.py
pyproject.toml
src/ecdysis/README.md
src/ecdysis/__init__.py
src/ecdysis/__main__.py
src/ecdysis/artifacts.py
src/ecdysis/benchmark.py
src/ecdysis/evolution.py
src/ecdysis/fdcr/__init__.py
src/ecdysis/fdcr/review.py
src/ecdysis/fdcr/roles.py
src/ecdysis/inference.py
src/ecdysis/llm_client.py
src/ecdysis/training.py
tests/test_artifacts.py
tests/test_benchmark.py
tests/test_cli.py
tests/test_evolution.py
tests/test_evolution_checkpoint.py
tests/test_inference.py
tests/test_training.py
```

There are no tracked result datasets, run logs, measurements or experiment reports. Embedded content was also inspected: README prose is claimed performance and expected synthetic output; example/test code is generated fixture data and prospective assertions, not retained execution. This conclusion follows from inventory plus source inspection, not merely the lack of a suggestive filename. The ignored `outputs/` and `data/` entries in `.gitignore` explicitly do not let this analysis conclude anything about untracked operator outputs.

The actual evidence query used to locate embedded performance or recall-testing material was:

```bash
git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/cuiyu-ai--Ecdysis grep -n -i -e faithfulness -e ablation -e recall -e experiment -e benchmark -e accuracy -e generalization -e expected cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 -- README.md src examples tests pyproject.toml
```

Matches were confined to `README.md:6,49,102-124,133`, `pyproject.toml:17`, `src/ecdysis/README.md:8`, artifact metadata and helper parameter names in `src/ecdysis/artifacts.py` and `src/ecdysis/evolution.py`, benchmark interfaces in `src/ecdysis/benchmark.py`, and synthetic fixture/assertion code in `tests/test_artifacts.py` and `tests/test_benchmark.py`. There were no matches for `faithfulness`, `ablation` or `recall`. Keyword non-matches alone do not establish absence; the complete inventory and full reads of all seven tests and all source modules establish the bounded result above. These are SRC-1/SRC-2/SRC-3 searches, with ABS-1 carrying the resulting absence claim.

The actual artifact-use query supporting RTE-4's scoped read-back limit was:

```bash
git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/cuiyu-ai--Ecdysis grep -n -e load_evolved_skills -e load_skill_artifact -e save_skill_artifact -e artifact_from_skills -e merge_skill_artifacts -e EvolvedSkill -e SkillArtifact cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 -- README.md src examples tests pyproject.toml
```

The complete matching-file set was `README.md`, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`, and `tests/test_artifacts.py`. README names SkillArtifact as reusable learned behavior. Artifacts defines the records/helpers and calls its own loader inside `load_evolved_skills`. Evolution imports the classes solely for `artifact_from_skills`. Tests call load/save/merge to verify serialization, ID filtering and scope rejection. No match occurs in training, inference, benchmark, either CLI, FDCR, or the synthetic end-to-end example. Full reads of those modules confirm they pass generic harness/specification objects and do not resolve the skill loaders through another in-package alias. Dynamic external harness factories remain outside this finding.

The delivered full-file evidence ranges from follow-up test reads were commit-addressed `git show` with bounded line selections: `tests/test_artifacts.py:1-67`, `tests/test_benchmark.py:1-30`, `tests/test_cli.py:1-37`, `tests/test_evolution.py:1-127`, and `tests/test_inference.py:1-37`; each reached EOF. The already inspected `tests/test_training.py:1-71` and `tests/test_evolution_checkpoint.py:1-86` also reached EOF. Requested ranges could extend past EOF; the command form, executed separately, was `git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/cuiyu-ai--Ecdysis show cf93866d545b0974dbb0bc83b39c31fbbdeeecb8:<path> | nl -ba | sed -n '<range>p'`. Bounded deliveries were complete, with no truncated evidential output.

### Behavioral-authority paths

BAP-1 — Review models receive scalar failure context, scope and preceding role prose through messages; advisory/instruction force for diagnosis/specification within review call chain; RTE-2.

BAP-2 — External editor receives moderator spec, current harness, failures/groups as Python arguments; guidance force over proposed candidate depends on adapter implementation; RTE-1.

BAP-3 — Trainer comparison consumes numeric scorer outputs, enforcing candidate-reference replacement within the training round; RTE-1. It does not enforce candidate isolation or fixed scoring semantics.

BAP-4 — External executor receives retained harness reference/task at inference; operational force depends on opaque harness/adapter; RTE-3.

BAP-5 — FDCR resume controller consumes checkpoint path/hash/model/status/next-turn metadata to refuse mismatch, schedule remaining turns or return cached spec; review roles/editor then receive generated content. Force is protocol validation/routing for current review continuation, not source-truth endorsement. Source SRC-1 `src/ecdysis/fdcr/review.py:165-247,292-309`.

## Runtime account

Ordinary programmatic training configures adapters and review client, collects/scans a round, groups failed tasks, iterates role review, edits candidate, reruns collection/scoring and accepts only a strictly larger current-round score. It repeats configured rounds even after a no-failures round, then returns a frozen wrapper over the retained object and round records. Inference is a separate no-adaptation wrapper with external execution and optional output export. Direct CLI grouping is a narrower returning computation; artifact helpers are separate capability paths; external benchmark CLI is a dynamic host integration.

Roles and answer oracle: model roles propose/criticize/synthesize, editor implements, numeric comparison accepts/rejects, external evaluator provides reward/reference semantics. An answer oracle may exist in collector/environment, but this repository does not supply benchmark answers; supplied score alone does not establish oracle validity. Distinct tasks and stable settings are contractual, not certified by passing the same Python callable. Operating mode is bounded training rounds, then requested inference; no open-ended deployment learning is established. Guidance/rationale can be retained in review checkpoints while final harness contents remain generic and possibly omit reasons. Model-weight identity/updates are external; skill edits do not imply parameter change.

Forcing cases traced statically: rejected candidate retains the reference but a mutating editor can already have changed that object; empty/invalid moderator output still reaches editor as normalized empty fields; checkpoint match binds formatted context/model string rather than full trace/harness semantics; inference fail_fast propagates an error while ordinary mode retains a failed-task record. Each consequence follows inspected code and named external contracts, not a executed probe. Repeated evaluation may vary populations and scores; strict numerical admission is not causal or held-out validation.

**Execution preflight:** no dynamic check planned. Considered synthetic quickstart, checkpoint interruption and mutable-harness fixture. Static source suffices to trace reference aliasing, parsing, match predicate and error control flow. The synthetic quickstart increments a revision and assigns success from revision>=1; it would test plumbing, not substantive learning or generalization. Running target tests or real adapters was not needed or performed. This prevents observed success/failure-rate, performance and causality conclusions. Source SRC-1 `examples/quickstart.py:8-65`.

## Lens scoping

### Memory/context scope

Full depth. Trigger CLM-1, CLM-2, OBJ-1, OBJ-3, OBJ-4 and OBJ-6: failure-derived reviews, checkpoints, revised harnesses and reusable artifacts name retained behavior-changing state. Inspect full method-level write/read interfaces, with opaque external payloads and consumers explicit. Generic host memory and task-model internals are excluded, preventing complete deployed-agent classifications.

### Epistemic scope

Full depth. Trigger causal diagnosis/generalization claims CLM-1 and CLM-3 plus admission/freezing claim CLM-2. Assess all material proposed-change, critique, score, acceptance, checkpoint and reuse functions over canonical records. Separate implementation from observed candidate lifecycle and source-reported effects. No single system-wide knowledge/quality grade.

## Lens outputs

### Memory/context lens

Inventoried failure evidence, diagnosis/specification, optional checkpoint, retained generic harness, round decisions and standalone skill artifacts. Adopted source evidence is retained on shared records here, without dependence on the local report.

The profile includes the complete specified memory boundary. It does not declare a known symbolic-only or natural-language-only system from JSON containers, score records or the toy harness. OBJ-4 prevents complete substrate, form, lineage, behavioral-authority and distilled-form sets. The same uncertainty applies to curation because an unconstrained editor can transform retained material in unspecified ways. Locally visible mechanisms and their evidence remain described in the shared records instead of being erased by the aggregate unknowns.

Known write agency combines automatic RTE-1, RTE-2 and RTE-9 with caller-authored OBJ-6/RTE-4; the weakest basis is afforded. Known read-back values concern the actual interface paths RTE-2, RTE-3 and RTE-9, all push/coarse. A requested file path in RTE-4 is not sufficient to add pull. Round filenames and checkpoint identity checks are storage selection and validation, not evidence of content-specific retrieval by the eventual reviewer.

Trace learning is established by the optional but wired checkpoint branch even if the generic editor ignores all advice. Trajectory-derived proposals and summaries are automatically retained and later supplied as guidance in the same diagnosis task. Accepted harness reuse adds a cross-task learning affordance at the editor/executor boundary. The dependent axes cover both: input source is scored trajectories, horizons include the continuing diagnosis task and later execution tasks, and timing is staged training. The `per-task` value is specifically the diagnosis task, not an inference that a session ID defines a task. Neither a `scope` label nor a skill artifact's task-scope docstring establishes per-project learning. The derived checkpoint form is known locally; the complete union with the generic learned harness remains not determinable.

Faithfulness `no` is bounded to available retained evidence, not a universal claim that the authors never tested it. ABS-1 and CLM-3 keep unexecuted synthetic tests and README outcomes separate from recall-dependence evidence. The wired basis states what is inspectable in the repository, not an observed deployment result.

### Epistemic lens

#### 1. Source-and-claim boundary

SRC-1, SRC-2 and SRC-3 at the recorded commit govern the entire method-level boundary. Question: whether recurring failure summaries, model criticism and strict score admission establish warranted harness changes, and what they leave to adapters. Assessed route families are extraction/grouping, FDCR proposal/critique/specification, score acceptance, checkpoint reuse, artifact interfaces and final inference; external execution/editing/evaluation semantics and provider internals are unassessed. CLM-1 claims improved diagnosis from recurrence; CLM-2 claims strict acceptance/final freezing; CLM-3 reports gains. No current candidate-linked run or causal experiment is inspected.

#### 2. Epistemic-object inventory

| Object | Truth-apt part or none | Source/consumer and limit |
|---|---|---|
| OBJ-1 | Task outcomes, reward/breakdown and trace occurrence claims | External collector supplies; code selects/compacts. Ground-truth validity and missingness mechanisms uninspected. |
| OBJ-2 | Group membership/distinct-task counts are determinate from supplied fields; claim that recurrence identifies a harness defect is ampliative | Fixed grouping and review consumer. Shared termination/component keys do not prove a shared cause. |
| OBJ-3 | Analyst/critic reasons and proposed runtime changes may assert causes, scope and consequences; some fields prescribe action | Review model produces from summaries/prior turns; editor consumes. No actual harness code or trace-body context is supplied to these model calls by the formatter. |
| OBJ-4 | Generic harness may contain theories, rules, scripts, parameters or other content; unknown | Editor provides and collector/executor consumes opaque value. Cannot individuate truth-apt parts or criticism from type variable alone. |
| OBJ-5 | Numeric score/decision occurrence within loop | Controller derives from scorer outputs; caller receives. Proves encoded comparison only, given valid numbers/adapters. |
| OBJ-7 | Retained diagnostic content inherits OBJ-3; status/next-turn fields represent internal review progress | Controller updates after each turn and reloads on matched invocation, RTE-9; identity validation establishes reuse eligibility only. |
| OBJ-6 | Skill pattern/tip and provenance assertions, plus non-truth-apt IDs/control metadata | Standalone artifact interfaces. Stored origin labels do not establish learning or a consumer. |

Additional checkpoint records from the memory lens preserve transcripts, specifications and reuse metadata. They can establish retention/reuse wiring; without an executed candidate instance, every current candidate phase remains **no instance observed**. Synthetic example code contains predetermined outputs, not actual candidate-linked evidence.

#### 3. Authority-route ledger

All executable functions below have architectural status **implemented** within SRC-1. Their model behavior and external adapter semantics remain separate unknowns. A role prompt is implemented input delivery, not observed content criticism. Status is **doctrine only** for contractual isolation/fixed-task/no-evaluation-edit requirements without implementation enforcement in the inspected controller.

| Route/function | Content/update relation; target | Evaluator/condition, timing and disposition | Epistemic versus operational/behavioral authority | Limits |
|---|---|---|---|---|
| RTE-1 check/evidence production | acquisition/import of external scores; entailed arithmetic for default mean | Collector/scorer evaluates baseline/candidate | Numeric training result within supplied population; no verified answer oracle | Missing rewards excluded; external scorer semantics not checked |
| RTE-1 content transformation | indeterminate transformation of opaque harness | External editor given spec/failures/groups proposes candidate | BAP-2 grants guidance to editor, not certified cause or correctness | Implementation of candidate change uninspected |
| RTE-1 disposition/acceptance | no content change | candidate_score > baseline_score | BAP-3 enforces reference selection in current round; warrants numeric preference only | No deep freeze, population equality, causal attribution or generalization guarantee |
| RTE-1 retention | no content change | accepted reference becomes current/final; rejected reference stays | Later rounds/inference receive selected object | Mutation can precede rejection; external persistence/form unknown |
| RTE-2 content transformation | indeterminate from formatted failures to proposed causal diagnosis; potentially ampliative conjecture | Analyst model proposes minimal cross-task repairs | Candidate theory/procedure, advisory BAP-1 | Recurrence supports consideration, not proof of harness cause |
| RTE-2 check/evidence production | indeterminate criticism/reasoning about proposed changes | Critic model asks about overfit, false triggers, regressions and contracts | Content-directed criticism is requested; it is not a task-environment test | Same client/limited summaries; actual criticism quality uninspected |
| RTE-2 content transformation | indeterminate revision/synthesis | Later Analyst addresses objections; Engineer summarizes; Moderator forms spec | Updated proposal sent to editor; schema/JSON shape is not truth | Empty fallback remains executable input; last-12-turn limit |
| RTE-2 operational admission/selection/consumption | no content change | Parsed/normalized spec delivered to editor | Authorizes attempt at candidate construction within outer loop | No semantic-spec acceptance before execution |
| RTE-3 operational admission/selection/consumption | no content change in wrapper | Caller-selected harness/executor receives tasks | BAP-4 uses retained object; wrapper does not run training | Actual task effect and accidental adaptation are adapter-owned |
| RTE-3 check/evidence production | acquisition/import of outputs/errors and entailed counts/timing | Executor exception controls succeeded flag | Warrants completion status, not answer correctness | External benchmark encoder/name/version are supplied |
| RTE-4 retention | no content change | Artifact load/save files | Makes records available; no warranted model reliance | Static storage capacity is not later behavioral activation |
| RTE-4 content transformation | non-ampliative reshaping by ID merge | Scope equality/required-field checks and first-seen ID | Bounded structural validity, not conflict resolution or semantic truth | Omitted caller-side wiring is explicit |
| RTE-5 check/evidence production | entailed group/count output from given fields | CLI helper | Reports deterministic extraction/grouping | No model interpretation or candidate acceptance |
| RTE-6 operational admission/selection/consumption | no content change except syntax extraction/repair | Network retry, JSON parse | Delivers model response or error/empty parse result | JSON syntax repair does not improve epistemic warrant |
| RTE-8 retention/content transformation | non-ampliative export or Markdown reshaping | Caller explicitly invokes transcript save or specification formatter | Makes diagnosis inspectable and possible guidance available; does not confer truth or deploy it | No in-package coding-agent consumer established |
| RTE-9 retention | no content change to retained dialogue/spec | Optional checkpoint writes completed turns and final output | Preserves generated guidance and controller progress | No semantic endorsement from serialization |
| RTE-9 operational admission/selection/consumption | no content change on reload | Matching context hash and model; saved next turn chooses subsequent calls, completed state returns cached spec | Recovery metadata controls review progression; advice reaches later reviewer/editor | Omitted evidence and configuration changes can evade cache identity; no new semantic review |
| RTE-7 check/evidence production | entailed calculation in caller-defined score domain | Window/tolerance arithmetic | Boolean stability/regression result | No trainer consumer established |

Checkpoint functions and specialized memory read-back use the same distinctions in the overlay below: integrity/reuse conditions select a prior output without re-establishing its semantic warrant. Independent evaluator roles do not arise merely from role names on one client.

#### 4. Per-object lifecycle disposition

OBJ-1 is acquisition/import plus non-ampliative reshaping of retained message content; discovery lifecycle **not applicable** to extracting fields. Selection/truncation can omit evidence, while scalar reward validity remains an external premise. OBJ-2 count/key construction is entailed derivation within its supplied data, discovery lifecycle **not applicable**. The stronger interpretation that a repeated signature is a systematic harness defect is **indeterminate** until a concrete proposed diagnosis is inspected; it may be an ampliative causal conjecture.

OBJ-3's transformation is **indeterminate** between restating evidence, deriving an implication and proposing a non-entailed causal repair. Model prompts request reasons and criticism, but no actual new review is inspected. Therefore formulation, criticism, revision, task test, acceptance and later integration of any particular theory all have observed candidate state **no instance observed**. Architecturally the calls, argument flow and numeric selection are **implemented**; semantic adequacy, oracle access and preservation of a proposal's meaning through external editing remain uninspected. No accepted ampliative lifecycle is inferred from a greater scalar score.

OBJ-4's operative content and persistence are **not determinable** at the generic adapter boundary, so preservation/entailment/ampliation cannot be classified. The trainer exposes selection and subsequent invocation but not a truth-apt representation or theory. OBJ-5 contains bounded entailed decision/arithmetic records, discovery lifecycle **not applicable**. For its control-only indices/flags there is no candidate truth-apt output requiring a theory lifecycle; relevant route is RTE-1.

OBJ-6 pattern/tip content is **indeterminate**: API labels learned do not decide whether a record was inferred from failure, manually supplied, tested or merely serialized. Required-field/scope checks establish structural eligibility. No observed produced artifact or downstream reliance is established in this source-only pass. Identifier-only parts have no candidate truth-apt output; relevant storage/merge route is RTE-4. Retention before epistemic acceptance is not lifecycle integration.

For OBJ-7, copying retained diagnostic content is non-ampliative and preserves the uncertainty of OBJ-3. Its control metadata records review progress rather than a proposed theory requiring discovery-lifecycle acceptance. RTE-9 validates identity and restores execution; it does not test the retained claims. No instance of checkpoint-mediated candidate use is observed. The implemented update-and-resume path supports only the narrow reflection finding about controller progress.

#### 5. System claims versus routes

| Claim | Doctrine/design | Implementation | Observed/causal evidence | Bounded conclusion |
|---|---|---|---|---|
| CLM-1 | Recurrence is a stronger signal than isolated failure; critic should avoid model-specific accommodation | Key/count grouping, recurring/auxiliary labels and role prompts, RTE-1/RTE-2 | No current linked diagnosis or interventional task evidence | A diagnosis heuristic is wired; cause/generalization remains unproven |
| CLM-2 | Isolated editor, fixed task model/scorer, final frozen harness | Strict score comparison and wrappers without trainer calls; generic reference passed to callbacks | No mutation or fixed-population audit | Numeric admission is implemented; deep isolation/freezing depends on adapter behavior |
| CLM-3 | Reports bundle training/inference benefits | Method-level implementation exposes proposed workflow | README report only; raw trials/design not inspected | Attributed claims without empirical upgrade or component-level causality |

#### 6. Bounded conclusion

Ecdysis turns supplied failure scores into a prioritization, asks a review model to propose and criticize repairs, delegates implementation, and lets a numeric training comparison select a retained candidate. It exposes a criticism-and-test pathway, but the diagnosis input is a compact summary and the decisive task evaluator/editor are external. A score increase can support only the comparison actually executed under those adapters; none was executed here. Checkpoint reuse, structural artifact validation and frozen result wrappers each have narrower force than correctness, generalization or immutable learned behavior.


## Reconciliation

Report identity matches the run, full revision and frozen boundary. Input SHA-256 `1f943cb596507dc6ba44fb55dd487835d5ef90b8327665695b909c9705639c6a`; method SHA-256 `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`; worker model unknown. Final report digest is in Run identity. Generic canonical referents remain unchanged.

| Local proposal | Accepted canonical record |
|---|---|
| MEM-OBJ-1 | OBJ-7, optional FDCR checkpoint including semantic payload and resume metadata |
| MEM-RTE-1 | RTE-9, automatic checkpoint continuation/completed-spec reuse |
| MEM-CLM-1 | ABS-1, bounded absence of retained recall-dependence execution evidence |

Resolved issues: FDCR receives summaries rather than trace bodies; recurrence is prioritization rather than an exclusive gate; generic harness opacity blocks whole-boundary form/storage/authority classifications; reference selection/no-adaptation wrappers do not deep-freeze or isolate caller objects; artifact APIs establish storage without a task-consumer route; same-ID suppression is not semantic deduplication; checkpoint identity excludes omitted trace content and provider/harness/prompt details; rationale can reach later reviewers/editor but its use/retention in the harness is unknown.

A targeted specialist reconciliation retained explicit full-file inventory, actual search queries and complete test-inspection scope supporting ABS-1 and RTE-4's limited consumer finding. Faithfulness no remains repository-bounded and does not deny external author experiments. Parent accepts per-task continuation as the diagnosis task, not as a task horizon guessed from a session ID. Parent adds only the checkpoint's narrow self-representation finding; it does not upgrade retained criticism or score admission into improved capacity. No substantive conflict or scope change remains.


## Bounded synthesis

Ecdysis exposes a small training controller around a model-based diagnosis stage and externally supplied task machinery. It groups supplied failure signatures, prioritizes cross-task recurrence in review context, generates and criticizes proposed updates, delegates candidate editing, and selects the candidate only on a strictly greater score for that round. Its final inference wrappers do not invoke adaptation, but their retained object and executor remain outside any deep-freeze or sandbox enforcement.

The strongest supported learning contribution is the connected failure→review→candidate-selection→later-execution pathway and optional persistence/reuse of generated diagnostic guidance. This is **wired** at the method's interfaces. Specific conjectural learning, meaning criticism improving future capacity, remains **uninspected**: no actual candidate contents, valid critique, adapter-controlled experiment or generalization comparison is observed here. An increasing supplied score is the implemented admission condition, not an automatic causal explanation. Reported empirical benefits remain attributed claims.

Reflection is **wired** in the limited optional checkpoint representation of the controller's own review progress: completed turns update transcript/next-turn/status state, and a later invocation uses that state to determine subsequent review calls. It does not establish a self-theory of the theory-building organization or that the proposed harness diagnosis accurately represents the opaque runtime. Those stronger claims remain **uninspected**. Demonstrated self-improvement is separately **uninspected**; changed harness references and protocol-level score preference do not prove improved future capability under valid, stable external evaluation.

For an integration that needs reliable acceptance and reuse, the important boundary is the adapter contract: isolated edits, fixed tasks/model/scorer, meaningful rewards and nonmutating final execution must be provided externally. For interpreting diagnosis, the relevant limit is FDCR's actual scalar summary and bounded recent dialogue, not the richer failure records that only the editor receives. Concrete adapter code, current candidate-linked traces, replay interventions and held-out controlled comparisons would change these conclusions. Artifact helpers need an actual consumer route before they can substantiate task-agent memory use.

## Limitations

| Limitation | Records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Generic external harness/edit/execution | OBJ-4, CMP-3, RTE-1, RTE-3 | Callable interfaces and reference flow | Complete memory form/storage/authority, candidate isolation and actual behavior | Concrete pinned adapter/harness implementation and relevant runs |
| Fixed evaluation is contractual | RTE-1, OBJ-5 | Same callables invoked twice; strict scalar comparison | Same tasks/model/settings, valid answer oracle, stable score history and generalization | Recorded evaluation identity, reference semantics and held-out trials |
| FDCR sees summary rather than full trace/code | OBJ-1, OBJ-2, RTE-2 | Counts and sample scalar outcomes | Causal diagnosis from full message/tool/harness evidence | Candidate-linked richer diagnostic context and critique trace |
| Checkpoint identity is compressed | RTE-9, OBJ-7 | Formatted context/rounds/model string | Detecting changes outside summary or provider/prompt/harness identity | Broader identity contract or controlled cache-reuse tests |
| Transcript window and permissive spec parsing | OBJ-3, RTE-2, RTE-6 | Last twelve turns, list/string normalization | Full-transcript deliberation at arbitrary pass count or semantically valid patch spec | Validated nested content and actual full-history behavior |
| Artifact storage separate from consumers | OBJ-6, RTE-4 | Standalone API/reference search | Reusable skill-file activation in task models | Named consuming integration and executed dependence test |
| No observed training/benchmark execution | SRC-3, CLM-3 | Code, docs and synthetic fixtures only | Actual benefit, cost/speed, causal contribution or faithful recall | Inspectable current-pin experimental records and design |
| Provider/SDK internals excluded | CMP-2, CMP-3 | Mutable identifiers and local API client | Fixed weights, hidden learning/retries or internal model state | Immutable provider/dependency evidence or targeted probes |
| Wrapper completion is not correctness | RTE-3 | Exceptions/output/timing and supplied metadata | Correct task answers or immutable inference object | Domain evaluator and mutation contract/probe |

## Verification and blockers

### Semantic verification

Checked whole method-level scope with external adapters explicitly excluded; source pin, report/input hashes, full-token mapping and canonical referents match. Known local JSON/prose structures do not override opaque HarnessT in aggregate fields. Checked trace-fed diagnosis/checkpoint route RTE-2/RTE-9 and candidate retention RTE-1/RTE-3 with input trajectories, diagnosis/later-task horizons, staged timing and incomplete distilled-form union. Current-stage extraction alone and unwired artifact files are not inflated into later model memory.

Checked coarse automatic consumers: role receives recent twelve-turn window, editor receives cached/current specification, executor receives whole retained reference. Validation hash is a cache identity predicate, not targeted content retrieval. Rejection, prompt criticism, numeric score admission, purported fixed evaluation and actual future capacity remain distinct. Source-supplied benchmark claims and prospective synthetic tests are not observations. ABS-1 has complete retained search scope; all other unsupported claims remain scoped limitations. Quote support and occurrence, route audit, source layers and independent epistemic architectural/candidate-state fields were checked before publication.

### Deterministic validation

Exact target `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/result.md`; passed before publication. Publication additionally verifies quote occurrence and report/input identity. These artifact checks do not execute Ecdysis.

### Blockers

none
