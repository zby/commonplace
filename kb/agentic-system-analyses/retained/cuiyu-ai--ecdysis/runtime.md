---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Ecdysis runtime baseline: failure review, adapter-mediated harness editing, score admission and retained-harness inference at the frozen commit."
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
---

# Ecdysis runtime report

## Runtime account

### Work and shipped entry paths

Ecdysis implements a harness-improvement plane, not the task agent whose harness it improves. A caller supplies a collector, editor and review client; the trainer collects scored outcomes, groups failures, asks review roles for a specification, delegates implementation and selects a candidate by aggregate score. Task execution and editing can perform effects outside Ecdysis, through those callbacks. The frozen scope and sole source are in [boundary](boundary.md); all source findings below use SRC-1 at its registered commit. Inspected source and synthetic test assertions establish implementation or design, not successful execution, reliable model compliance or benefit.

The ordinary complete shipped driver is `examples/quickstart.py`. Public Python paths include `EcdysisTrainer.train`, `analyze_failures_fdcr`, `run_harness_fdcr`, `TrainingResult.infer`/`infer_many`, `InferenceRunner` and `run_benchmark`. The two installed CLIs are different partial routes: `ecdysis` extracts and prints failure-group counts without FDCR or editing; `ecdysis-run` imports caller-named adapter and harness factories, executes tasks and emits JSONL plus a printed summary. Neither CLI trains a harness. Artifact APIs separately construct, save, load and merge skills; training does not automatically use those persistence utilities. These entry distinctions follow SRC-1, `pyproject.toml`, `src/ecdysis/__main__.py`, `src/ecdysis/benchmark.py`, `src/ecdysis/evolution.py`, `src/ecdysis/artifacts.py` and `examples/quickstart.py`.

> [project.scripts]
> ecdysis = "ecdysis.__main__:main"
> ecdysis-run = "ecdysis.benchmark:main"
> --- `pyproject.toml`

### Ordinary invocation, end to end

In the quickstart, the Python caller is the principal and next-step owner until `train` takes control. It passes a dictionary harness with revision zero, a deterministic collector, an editor returning a new dictionary and a synthetic review client. Two configured training rounds and two review passes bound the work. The collector emits two task IDs with rewards determined by whether the revision is at least one; the editor increments the revision regardless of the specification. This is a demonstration of orchestration, not model-responsive editing or a causal test of FDCR quality (SRC-1, `examples/quickstart.py`).

The trainer recollects and rescores the retained harness every round. Failure extraction selects rewards below the configurable threshold; missing rewards are not failures. It keeps up to 80 final messages and 2,000 characters per message by default. Grouping uses termination reason and sorted reward components below 1.0; it orders groups by distinct-task recurrence and count. The review receives a further transformed representation: all cluster summaries, up to eight displayed task IDs per group and the first twelve failure metadata samples. It does not receive the compacted trajectory messages, task descriptions or current harness code. The editor, by contrast, receives the full extracted failures, groups, current harness and moderator specification. This difference bounds diagnosis: the model sees structured failure signatures, not the alleged faulty actions themselves (SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`; [RT-RTE-failure-review](#rt-rte-failure-review)).

Code serially schedules Analyst, Critic and Engineer for each review pass, then Moderator. These are role identities in separate two-message requests, not separate workers or access-control principals. Each request contains a shipped system prompt plus freshly constructed user context and at most the last twelve transcript turns. Model replies escape as stripped text in a shared transcript. The final Engineer still receives a call, with the instruction “No action — moderator follows.” The Moderator is asked for JSON; parsing normalizes four fields into a specification. At two passes, the ordinary nonempty review entails six text calls and one JSON call (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`).

The trainer calls the editor once, executes the candidate through the collector, scores it and replaces the retained harness reference only if its score strictly exceeds that round's baseline. It records acceptance, both scores and failure/group counts. In quickstart source, revision one supplies reward one; the second round then records `no_failures` rather than invoking review or editing. The terminal product is `TrainingResult`, containing a retained harness reference, final score and immutable tuple of round records. Quickstart later invokes `infer_many` with two new task dictionaries and an executor that renders their IDs and retained revision. No code here injects reusable skills into inference (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`; [RT-RTE-candidate-admission](#rt-rte-candidate-admission), [RT-RTE-harness-inference](#rt-rte-harness-inference)).

### Control paths and guarantees

| Guarantee or requested constraint | Owner and enforcement | Strength and scope | Alternate paths and required external contract | Conclusions |
|---|---|---|---|---|
| Candidate reference replacement requires strict score improvement | Trainer's `candidate_score > baseline_score` branch | invariant for this replacement operation, not for arbitrary mutation or real performance | Direct inference, direct FDCR, artifact APIs and caller edits bypass it. Editor/collector must not mutate retained state; scorer must compare the intended fixed task/model/environment. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Isolated candidate, fixed task model/environment and fixed scorer | Adapter implementers; trainer passes live references without copying or sandboxing | protocol from README, not deployment guarantee | Callback code can mutate input or evaluation; generic types impose no effect restrictions. True isolation and score comparability require external implementation. | implementation conclusion status: claimed; operation conclusion status: uninspected |
| Inference does not adapt harness | No trainer/review invoked inside `infer` or `InferenceRunner.run` | invariant about Ecdysis's own scheduling, protocol about the harness's unchanged contents | Executor receives the live harness and can mutate it; the frozen dataclass does not deep-freeze payloads. Direct runner accepts any harness, including one never trained. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Cross-task repairs, no task/evaluation edits, conservative dispute resolution | Role prompts interpreted by review model | policy, not an invariant | Singleton evidence is still delivered; editor can disregard the spec. No minimum recurring-task admission predicate or evaluator-integrity check is imposed by the trainer. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Checkpoint belongs to review input/model | Review's hash/model comparison and exception | invariant for equality check on the formatted context, rounds and model string | Raw omitted messages, role-prompt versions and provider endpoint are not in the hash. Completed reuse can skip all calls despite changes in those omitted inputs. | implementation conclusion status: wired; operation conclusion status: uninspected |

Source support: SRC-1, `README.md`, `src/ecdysis/training.py`, `src/ecdysis/inference.py`, `src/ecdysis/fdcr/roles.py`, `src/ecdysis/fdcr/review.py`. The table's statuses describe implementation inspection only. There is no supplied run or deployed isolation evidence. References, normalization and prompt delivery do not prove evaluator integrity, semantic correctness or provider compliance.

> - `editor(harness, specification, failures, groups)` creates an isolated candidate
>   without mutating the retained harness.
> --- `README.md`

The capability surface includes arbitrary Python callback execution, dynamic module import in the benchmark CLI, provider calls and caller-selected filesystem output paths. The current grant set is whatever callbacks, credentials and paths the caller supplies; no actual invocation grant set was supplied here. The deployed isolation envelope is uninspected. The selected source paths implement no distinct task-tool permission manager or approval gate; this does not describe permissions inside an external executor. Provider-native tools, shell operations, subprocesses or remote workers could occur inside callbacks, but none of those external implementations is available. `LLMClient.chat` allows arbitrary SDK overrides; FDCR itself supplies no tools and consumes only response content. A caller using `LLMClient` directly can issue requests outside the review schedule. Neither such requests nor callback effects are governed by trainer admission (SRC-1, `src/ecdysis/llm_client.py`, `src/ecdysis/training.py`, `src/ecdysis/benchmark.py`).

### Selected forcing cases and recovery

Four source-supported cases constrain the broad product claims:

1. **Non-improving or no-failure round.** Equal/lower candidate scores retain the previous reference; an empty failure list skips proposal generation but continues remaining training rounds. Test source checks rejection and a later no-failure round. This challenges “each round evolves” and does not prove rollback of adapter mutation (SRC-1, `src/ecdysis/training.py`, `tests/test_training.py`).
2. **In-place mutation despite rejection or freezing.** The trainer passes the retained object directly to editor/collector and inference passes it directly to executor. No copied snapshot is restored on rejection. The callbacks' externally required nonmutation, not `@dataclass(frozen=True)`, protects mutable harness contents. This challenges deep isolation and physical freezing (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/inference.py`).
3. **Interrupted/completed checkpoint.** Successful turns advance an index; interruption records the exception and rethrows. Reentry resumes the unfinished role, while completed state returns cached transcript/spec without calls. Hash/model mismatch raises. Test source explicitly constructs interrupted and completed consumers. A failed provider request can be repeated; this is not exactly-once provider execution, and the trainer itself has no persisted harness/candidate round restart protocol (SRC-1, `src/ecdysis/fdcr/review.py`, `tests/test_evolution_checkpoint.py`).
4. **Direct external execution and malformed review output.** `ecdysis-run` imports factories and inference executes their adapters without training admission. Separately, unparseable moderator output produces empty spec fields rather than a semantic rejection, and editor still runs after nonempty failures. Exceptions in training callbacks propagate; batch inference instead captures executor exceptions unless `fail_fast` is set. These are distinct result/error policies, not one system-wide success guarantee (SRC-1, `src/ecdysis/benchmark.py`, `src/ecdysis/inference.py`, `src/ecdysis/llm_client.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`).

Provider retries cover rate-limit and connection errors, with bounded attempts and exponential sleeps; other SDK API errors become `RuntimeError`. Usage events record only completed calls, including attempt counts and token/duration fields. Interrupted checkpoints keep successful transcript segments and error text; there is no concurrent review coordination or locking in the inspected synchronous schedule. Temp-file replacement reduces partially written checkpoint exposure but does not make multiple writers safe. Full failure-message evidence, role compliance, real task performance, live provider behavior, actual recovery and costs remain unobserved. No target code, example, tests or provider calls were executed (SRC-1, `src/ecdysis/llm_client.py`, `src/ecdysis/fdcr/review.py`).

## Shared records

### Components

#### RT-CMP-review-model
Label: Review model behind LLMClient

Source-native identity: `LLMClient.model` resolves at a caller-selected OpenAI-compatible `base_url`. Distributed-parametric model weights reside at the provider; Python stores a normalized model-name string, credentials-backed SDK client and usage events. Parameter updates are not requested by inspected FDCR/client routes. Provider internals and any provider-side training/state remain uninspected. No immutable model version is required; a mutable endpoint/name can resolve to a different model. Checkpoint equality tests the model string, not weights or endpoint. Synthetic example/test clients are deterministic stand-ins, not evidence of real model operation (SRC-1, `src/ecdysis/llm_client.py`, `src/ecdysis/fdcr/review.py`, `examples/quickstart.py`).

> kwargs: dict[str, Any] = {
>     "model": self.model,
>     "messages": messages,
>     "temperature": temp,
> }
> --- `src/ecdysis/llm_client.py`

### Operative objects

#### RT-OBJ-frozen-harness
Label: Retained harness in TrainingResult

Identity: `TrainingResult.frozen_harness`, an unconstrained generic Python value held in process memory; persistence and encoding depend on the caller. In quickstart it is symbolic dictionary state interpreted by fixed collector/executor rules. A real harness could contain instructions, code or numerical components; its form and substrate are uninspected rather than inferred from the API's field name. Round records are symbolic dataclasses/tuple in memory. The result dataclass freezes assignment to its fields, not the transitive contents of the harness. Later authority is described in [RT-BAP-retained-harness](#rt-bap-retained-harness) (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`).

> frozen_harness: HarnessT
> final_score: float
> rounds: tuple[RoundRecord, ...] = field(default_factory=tuple)
> --- `src/ecdysis/training.py`

#### RT-OBJ-review-spec
Label: Moderator patch specification

Identity: `review["spec"]`, a Python dictionary returned by `run_harness_fdcr` and passed to editor. Symbolic keys select fields; their patterns, descriptions, rationales, tips and implementation notes are natural-language instructions for an interpreting consumer. It resides in process memory, optionally also checkpoint JSON. The trainer does not execute specification fields as code. Editor interpretation and actual changed organization are external except for the synthetic editor, which ignores them. Skill persistence is a separate route, not an automatic effect of this object (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`, `examples/quickstart.py`).

> specification = analysis["review"]["spec"]
> candidate = self.editor(
>     current_harness,
>     specification,
>     failures,
>     groups,
> )
> --- `src/ecdysis/training.py`

### Routes

#### RT-RTE-failure-review
Label: Scored failures to FDCR specification

Endpoints and owner: collector results enter extraction/grouping code, then `run_harness_fdcr` owns the deterministic sequential role schedule. Model replies supply diagnoses/proposals and criticism; Moderator proposes the final specification. The code neither adjudicates each dispute nor vetoes semantic changes. A human selects initial adapters/configuration; no per-spec human approval is wired. Operation is a bounded training review over caller-supplied tasks, not an open-ended autonomous task agent. Improvement trigger is a nonempty below-threshold failure set. Reward labels are evaluator outcomes, not necessarily expected-answer oracles. Real answer/reference providers and their use are uninspected because the collector is external. The synthetic collector's reference outcome is the fixed predicate `revision >= 1`, independent of model answers (SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`, `examples/quickstart.py`).

- Immediate return: Group map plus review transcript, normalized spec, configured passes and optional usage/checkpoint metadata.
- Later read-back: With a checkpoint path, later invocation reloads transcript/progress or completed spec; trainer hands the resulting spec to editor. Cached reuse is under [RT-RTE-checkpoint-recovery](#rt-rte-checkpoint-recovery).
- Delegated visibility: Each review request sees its role system prompt, formatted cluster/sample metadata and last twelve transcript turns; editor receives extracted failures including compacted messages and the groups/spec/harness.
- Selection predicate: Failure reward below threshold; groups prioritized by distinct task count; recurring label requires at least two displayed task identities, but singleton groups remain input and admission does not require recurrence.
- Invalidation or expiry: Checkpoint hash/model mismatch raises; otherwise transcript context is sliced per request without deleting stored turns. No checkpoint expiry is wired.
- Activation or effect: Calls are wired; resulting spec is delivered to editor. Semantic review compliance or behavior changed by the spec is unobserved; quickstart editor ignores it.
- Evidence limits: Source reveals requests and transformations, not actual criticism quality, model compliance, full trajectory diagnosis or benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Working context is reconstructed, not an accumulating provider conversation: each role request has two messages. Code excludes raw trajectory messages, limits metadata samples, and removes all but twelve transcript turns from the window. Full transcript remains in memory/checkpoint, but there is no special on-demand reload of omitted turns into a role's window. The Moderator prompt asks to read the full transcript even though the same twelve-turn slice applies; reviews longer than four passes can omit earlier turns. This resembles isolated call frames with text returns, not pointer-following storage. All roles share one review-client identity and selected transcript; there is no process-level delegation isolation (SRC-1, `src/ecdysis/fdcr/review.py`).

> history = "\n\n".join(
>     f"### {t['role'].upper()}\n{t['content']}" for t in transcript[-12:]
> )
> --- `src/ecdysis/fdcr/review.py`

> "You are the Critic. Challenge the Analyst's proposals: overfitting "
> "to single tasks, false-positive triggers, blocking valid actions, "
> "violating runtime contracts, harming previously successful "
> "trajectories, or introducing behavior that depends on incidental "
> "conversation order. Be specific and constructive."
> --- `src/ecdysis/fdcr/roles.py`

Theory account: The shipped guidance treats cross-task recurrence as evidence of harness deficiencies and directs minimal conservative repairs without changing evaluation. Proposed component/description/rationale units could state localized explanatory hypotheses, but the parser does not require such content. The Critic is explicitly asked to challenge proposals; later Analyst requests address objections, and the transcript passes the result to subsequent roles. What persists is transcript/spec and optionally checkpoint JSON, not revised role-method texts. These are inspectable requests for a criticism/revision process, not observed formulated criticism (SRC-1, `README.md`, `src/ecdysis/fdcr/roles.py`, `src/ecdysis/fdcr/review.py`).

- theory-builder conditions 1–4: Condition 1 conclusion status: afforded — component/description/rationale fields permit whole localized proposals; actual theory content is unobserved. Condition 2 conclusion status: wired — prior text is supplied with content-sensitive revision instructions; resulting dependence on its meaning remains unobserved. Condition 3 conclusion status: claimed — challenge/revision is requested, but no supplied transcript establishes challenged claim, outcome and placement of blame. Condition 4 conclusion status: wired — replies are carried into later revision turns and optional resume state; retention of an actual criticism result remains unobserved.
- Addressability: Proposal fields and transcript role turns are inspectable/replacable text units; no assumption-level addressing or editing mechanism is enforced.
- Persistence: In-memory review passes; optional checkpoint across invocations; no demonstrated cross-problem use.
- learning: Future improved capacity from FDCR is unestablished; synthetic score changes do not attribute improvement to review content.
- Reflection: Failure-signature representation of the target harness reaches an editor that can modify it; the architecture affords both directions through adapters, but the review's access is coarse and actual representation-mediated modification is unobserved. Revision of Ecdysis's own review method is not wired here.
- Reflective theory builder: Method-text criticism and revision against its own operation are unestablished; the review targets supplied harnesses, not shipped role prompts.
- Autonomous theory builder: Computation schedules review and can perform editing through supplied callbacks without a per-update human gate. Full theory-builder operation is unestablished because criticism content and real editor behavior are unobserved.

#### RT-RTE-candidate-admission
Label: Editor candidate to retained harness

Endpoints and owner: trainer sends [RT-OBJ-review-spec](#rt-obj-review-spec) and evidence/current harness to the caller's editor, then collector/scorer produce candidate score. Editor proposes; trainer's scalar comparison decides reference retention and vetoes non-improvement. No per-candidate human approval is required or excluded by callback internals. Mode is fixed-count training rounds with configurable threshold/passes/scope, not held-out validation enforced by the package. Answer oracle, task-model fixity and evaluator integrity depend on collector/scorer; default scorer averages available rewards and raises if none exist. Candidate rejection keeps the old reference but cannot undo in-place mutation. Callback exceptions propagate; no trainer checkpoint/rollback restores candidate or harness state (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/evolution.py`, `README.md`).

- Immediate return: Ultimately TrainingResult with retained harness, final score and round decisions; each round records candidate and baseline scores/status.
- Later read-back: Retained object feeds the next round's collector and later infer/infer_many; no automatic durable harness save/load is wired.
- Delegated visibility: Editor receives current harness, spec, failures and groups; collector receives harness; scorer receives results. Effects of external callbacks are not isolated by this route.
- Selection predicate: candidate_score strictly greater than this round's baseline_score.
- Invalidation or expiry: Replaced on a later accepted candidate; rejected proposals are not retained as harness. No horizon/expiry for the final reference is enforced.
- Activation or effect: Accepted reference is passed to subsequent collection/inference. Semantic patch implementation and actual later dependence on it require adapter evidence.
- Evidence limits: Comparison supports admission wiring, not comparable sampling, nonmutation, held-out generalization or successful improvement; no runs supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> accepted = candidate_score > baseline_score
> if accepted:
>     current_harness = candidate
>     current_score = candidate_score
> --- `src/ecdysis/training.py`

Admission guidance is the review spec shaped by shipped role policy; it may propose product/capability/instruction changes to the caller's harness. Only retained reference and round decisions persist in trainer memory. Whether it changes production machinery depends on harness/editor. This is an improvement-directed dispositional self-change path if the assessment boundary includes the supplied task runtime/harness, with horizon successive rounds and inference and objective aggregate reward specified before editing. For Ecdysis's shipped improvement machinery alone, those products are external harnesses; no package self-rewrite follows. Evidence can shape spec and editor input (link 1), editor can change a harness (link 2) and retained harness reaches collector/executor (link 3). An exercised content-responsive change and subsequent behavioral dependence (link 4), and successful improvement attribution, are unestablished. The quickstart's predetermined revision predicate does not close that attribution (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`).

#### RT-RTE-checkpoint-recovery
Label: FDCR checkpoint write and reentry

Endpoints and owner: review code serializes state to caller path via temporary JSON file and replacement, then reads it on a later review call. State includes version/status, formatted-context hash, model string, transcript, next turn and usage segments; final state adds spec. Running and interrupted records permit retries; completed records bypass review calls. This is recovery/reuse, not independent semantic admission of a new patch. Caller controls path and can replace contents; no signature or comprehensive schema validation is enforced (SRC-1, `src/ecdysis/fdcr/review.py`).

- Immediate return: On success, review result; on interruption, saved error/progress and rethrown exception.
- Later read-back: Existing path loads transcript and next index, or completed spec/usage into a later review invocation.
- Delegated visibility: Resumed roles see only the last twelve stored turns plus reconstructed context; editor receives the resulting spec, not checkpoint state directly.
- Selection predicate: Existing explicitly supplied checkpoint path; context hash and model string must match. Completed status selects cached return.
- Invalidation or expiry: Mismatch raises RuntimeError; no expiry. Hash covers formatted context and review-pass count, not all source failures, role prompts or provider endpoint.
- Activation or effect: Stored index controls which calls are skipped; cached spec may feed editing without another review call. Actual resumed execution is unobserved.
- Evidence limits: Test assertions describe designed interruption/reuse, not an observed run; concurrency safety, exactly-once external calls and semantic freshness are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> context_hash = hashlib.sha256(f"{rounds}\0{context}".encode()).hexdigest()
> model = str(getattr(client, "model", ""))
> --- `src/ecdysis/fdcr/review.py`

> if state.get("context_hash") != context_hash or state.get("model") != model:
>     raise RuntimeError(
>         f"FDCR checkpoint input/model mismatch: {checkpoint_path}"
>     )
> --- `src/ecdysis/fdcr/review.py`

#### RT-RTE-harness-inference
Label: Retained or caller-loaded harness to task outcomes

Endpoints and owner: `TrainingResult.infer` directly invokes executor; `infer_many` constructs `InferenceRunner`; direct runner and benchmark API accept arbitrary caller harnesses. Benchmark CLI dynamically imports factories, calls adapter.load_tasks(split), then sequential adapter.execute(harness, task). Caller controls task source, factories, split, encoder/output path and fail-fast. There is no FDCR scheduler or admission during inference; arbitrary executor/factory effects remain external. No parallel tasks or separate task model context is created by Ecdysis itself (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`).

- Immediate return: Single executor output, or tuple of records with task identity/output/error/elapsed time; benchmark adds name/version/split and optional JSONL/printed output.
- Later read-back: Same in-memory harness can be reused; benchmark factory may load retained state, but its implementation is external. Emitted JSONL has no automatic package reload/evolution path.
- Delegated visibility: Executor receives harness and one task; benchmark factory/import and encoder run in caller process. Model-visible context inside executor is uninspected.
- Selection predicate: Supplied tasks in iteration order; default ID uses task_id/id or index, benchmark split delegated to adapter.
- Invalidation or expiry: inapplicable — inference imposes no harness expiry or adaptation schedule; caller controls replacement/lifetime.
- Activation or effect: Live harness reaches task executor; the synthetic executor reads its revision. Real task effects and semantic activation are unobserved.
- Evidence limits: Success counter means no caught executor exception, not correct task answer; unchanged harness contents and benchmark quality require external contracts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> output = self.executor(self.harness, task)
> --- `src/ecdysis/inference.py`

> module_name, separator, symbol_name = specification.partition(":")
> if not separator or not module_name or not symbol_name:
>     raise ValueError("expected import path in the form module:callable")
> return getattr(importlib.import_module(module_name), symbol_name)
> --- `src/ecdysis/benchmark.py`

Batch runner catches executor exceptions into records and continues unless fail_fast; direct `infer` propagates them. Task-ID calculation, iterable failures and output encoding are outside the executor catch's protection. JSONL is explicit result persistence, not a guarantee of semantic correctness or automatically imported training feedback (SRC-1, `src/ecdysis/inference.py`, `src/ecdysis/training.py`, `src/ecdysis/benchmark.py`).

#### RT-RTE-artifact-utilities
Label: Skill construction, persistence and merge APIs

Endpoints and owner: callers invoke `artifact_from_skills`, save/load APIs, `load_evolved_skills` or `merge_skill_artifacts`. Dictionary conversion checks required fields; optional load scope checking and mandatory merge scope checking restrict combination. Deduplication keeps the first identifier, not the best-supported content. Caller can supply manual or model-produced content; no automatic trainer score gate or per-item human approval operates here. Whether a caller is human-directed and whether skills later control an agent are unresolved outside the shipped consumers (SRC-1, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`).

- Immediate return: Structured artifact, saved path or loaded/merged skills.
- Later read-back: Explicit artifact-path loading returns skills to caller; no automatic inference injection is implemented in trainer/runner.
- Delegated visibility: API caller sees skill text and metadata; downstream prompt/editor visibility depends on caller integration.
- Selection predicate: Explicit path lists/artifact inputs, optional scope equality, first occurrence of each skill ID. IDs deduplicate; they do not semantically select relevant skills.
- Invalidation or expiry: Scope mismatch raises where scope checking applies; no semantic expiry/version invalidation. Saves overwrite caller-selected paths without admission comparison.
- Activation or effect: JSON filesystem writes and in-memory content delivery are wired; downstream behavior change is unestablished.
- Evidence limits: Required-field checks establish structure, not correctness, learned benefit or observed skill consumption by an agent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission trigger is an explicit API call with supplied content. Software checks required fields for dictionary conversion and scope for selected consumers, but typed objects can be directly constructed; there is no comprehensive semantic approval or rejection gate. Rejected scope mismatch raises, and no versioned rollback is provided. Guidance content is each skill's natural-language pattern/tip within symbolic metadata; saved artifact JSON persists it for later caller loads. Memory revision analysis is left to the memory member (SRC-1, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`).

> if skill.id not in seen_ids:
>     seen_ids.add(skill.id)
>     skills.append(skill)
> --- `src/ecdysis/artifacts.py`

### Claims

#### RT-CLM-harness-training
Label: Generalizing and efficient harness training

Claimed operation: README says recurring cross-task failure evidence plus collaborative refinement produces better-generalizing harness repairs and reports 18.56% accuracy improvement and up to 1.84× faster training over existing harness evolution. The inspected implementation prioritizes recurrence and requests conservative review; it does not hard-gate recurrence or establish those numerical results. Evidence layer is reported operation/doctrine, not observed run or causal experiment. External paper/benchmarks are not registered evidence. No attribution of gains, real costs or cross-model generalization is supported here (SRC-1, `README.md`, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/roles.py`).

> 3. Aggregate structured failure evidence and prioritize patterns recurring across
>    distinct task instances; singleton patterns remain auxiliary evidence.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-retained-harness
Label: Retained harness reaches collection and task execution

Consumer: trainer collector in a later round, and supplied executor/benchmark adapter during inference. Channel: live Python harness argument. Force: program-level delivery with effects determined by callback interpretation; in quickstart the revision field determines synthetic reward and rendered output. Horizon: rounds of one training call and later in-process inference calls; cross-process factory persistence is external. Retention does not by itself demonstrate meaningful behavior change or improvement (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `examples/quickstart.py`; [RT-OBJ-frozen-harness](#rt-obj-frozen-harness)).

> return executor(self.frozen_harness, task)
> --- `src/ecdysis/training.py`

#### RT-BAP-review-editor
Label: Review specification reaches candidate editor

Consumer: caller-supplied editor. Channel: specification dictionary argument containing model-produced natural-language descriptions/rationales and optional skills/notes. Force: advisory content supplied by the trainer, not code-enforced compliance; editor owns actual implementation. Horizon: current candidate generation, potentially later through cached checkpoint spec. The synthetic editor disregards specification content, so source wiring is not evidence of activation. Later retained-harness authority is a separate path (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`, `examples/quickstart.py`; [RT-OBJ-review-spec](#rt-obj-review-spec)).

> def edit(harness, _specification, _failures, _groups):
>     return {"revision": harness["revision"] + 1}
> --- `examples/quickstart.py`

## Annotations

none
