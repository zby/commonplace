---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Meta-Harness memory: classification checkpoints, proposer experience files, KIRA handoffs and pilot evaluation history."
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
source-identity: "https://github.com/stanford-iris-lab/meta-harness"
reviewed-boundary: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
---

# Meta-Harness memory report

## Boundary and evidence

This report covers retained classification state and response caches, reference-search experience, task-local KIRA compaction, pilot source snapshots and scoring history, and the onboarding handoff. The frozen source is SRC-1 in [boundary](boundary.md). Direct reads established the memory-specific findings below; supplied [runtime](runtime.md) findings establish broader invocation, code admission, model identity and external-host limits. Evidence is implementation or doctrine/design, not observed operation. No target was executed.

The important distinction is between state used by a task solver and evidence offered to a harness proposer. Classification examples enter solver prompts through implemented selection. Search summaries and traces are requested proposer inputs, not automatically loaded in full. Candidate Python subsequently has executable authority, independently of whether its author followed the history-reading instructions. See [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution).

| Entry point or operation | Source path; inspection basis | Covering records or local limit |
|---|---|---|
| Classification `predict`, `learn_from_batch`, state save/load | Direct: `reference_examples/text_classification/agents/fewshot_memory.py`, `agents/fewshot_all.py`, `agents/no_memory.py` under the same classification root; `reference_examples/text_classification/memory_system.py`, `reference_examples/text_classification/inner_loop.py` | [MEM-OBJ-examples](#mem-obj-examples), [MEM-RTE-classification-memory](#mem-rte-classification-memory). Generated candidates are not frozen; their internal state formats cannot be enumerated. |
| Benchmark validation/test dispatch and checkpoint alternatives | Direct: `reference_examples/text_classification/benchmark.py` build-val/test ranges, `reference_examples/text_classification/inner_loop.py` logger, offline/online and main save/load ranges | [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-classification-log](#mem-obj-classification-log), [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize). Arbitrary direct `set_state` callers have no established principal or approval policy. |
| Reference history generation, selection and reset | Direct: both reference `meta_harness.py` summary/frontier/reset ranges; classification benchmark frontier range is supplied runtime evidence | [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary), its separately assessed [MEM-OBJ-summary-results](#mem-obj-summary-results) and [MEM-OBJ-summary-rationale](#mem-obj-summary-rationale), [MEM-OBJ-frontier-val](#mem-obj-frontier-val), [MEM-OBJ-reports](#mem-obj-reports), annotations on search routes. |
| Reference proposer skill loading, interactive skill and child contexts | Direct: both shipped `.claude/skills/*/SKILL.md`; supplied wrapper/runtime findings | [RT-BAP-proposer-instructions](runtime.md#rt-bap-proposer-instructions), search annotations. Host compaction and actual child visibility remain external and uninspected. |
| Classification response replay and prompt trimming | Direct: `reference_examples/text_classification/llm.py` provider cache and truncation ranges | [MEM-OBJ-completion-cache](#mem-obj-completion-cache), [MEM-RTE-completion-replay](#mem-rte-completion-replay). |
| KIRA proactive/overflow handoff, trajectory recording, tools and image frame | Direct: `reference_examples/terminal_bench_2/agents/baseline_kira.py` handoff ranges; supplied runtime for command/image paths | [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution) annotation. Inherited selector, eviction and summarizer implementation are outside the frozen repository. |
| Provider-side ephemeral prompt cache | Direct: `reference_examples/terminal_bench_2/anthropic_caching.py` | KIRA annotation. Opaque provider storage, lifetime and actual reuse prevent a local durable-memory classification. |
| Pilot evaluate tool, history projection, terminal tails and final verifier | Direct: `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py` evaluate-source/CLI range, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`; supplied runtime for controller admission and shell counterpaths | [MEM-OBJ-evaluation-history](#mem-obj-evaluation-history), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) annotation. |
| Pilot child terminal harness | Supplied runtime: `experimental/harbor_meta_harness/agents/terminal_harness.py` | Current conversation accumulation and output tails, not established cross-task memory. Internal candidate alternatives unknown; no next-run history loader established. |
| Domain onboarding and implementation handoff | Supplied runtime: `ONBOARDING.md` | [RT-RTE-domain-onboarding](runtime.md#rt-rte-domain-onboarding) annotation. |

Static datasets, seed prompts, tool schemas, verifiers and suite configuration are inputs/control surfaces rather than use-derived memory. They remain in the whole-system boundary. Downloaded task payloads, actual search histories and provider state are unavailable in the frozen source; this prevents empirical provenance, activation, quality and performance conclusions. Available supporting tests and full loader/verifier internals not directly reread here are not access gaps.

## Core ideas

1. The shipped classification memory is supervised example retention, not model-weight learning or an error-only lesson generator. Offline batches substitute ground truth for prediction; online batches carry real predictions and evaluator feedback. The few-shot implementation keeps only input/target/raw-question pairs. Prediction metadata and reasons do not survive into that store. [MEM-RTE-classification-memory](#mem-rte-classification-memory).
2. Search retains multiple representations of experience: raw/partial traces, numeric frontiers, model-authored hypotheses and requested reports. Numeric selection is implemented; interpretation and subsequent candidate design are model-facing procedure. Scores alone neither supply causal explanations nor establish improvement. [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary), [MEM-OBJ-reports](#mem-obj-reports).
3. Persistence is route-specific. Classification saves and reloads training state across processes. KIRA carries a transformed task context across inference calls. Pilot history affects later turns and the final reward consumer, but final code is not automatically restored to the best historical snapshot. [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize), [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search).
4. Labels overstate budgets if read literally: the few-shot headers mention 50,000 characters or a 50k token limit, but executable `MAX_CHARS` is 30,000 and `FewShotAll` sets 9,999 examples. The implementation selects/shuffles examples and stops formatting at its character heuristic; it does not deliver every stored example. SRC-1, `reference_examples/text_classification/agents/fewshot_memory.py`, `reference_examples/text_classification/agents/fewshot_all.py`.

> MAX_CHARS = 30000
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

> super().__init__(llm, max_examples=9999)
> --- `reference_examples/text_classification/agents/fewshot_all.py`

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-examples
Label: FewShotMemory examples

The `examples` list is source-native in-memory state; JSON serialization preserves its fields on disk. JSON keys/list ordering are symbolic; question/answer strings become natural-language demonstrations at the model consumer. Lineage is training examples plus supplied ground truth, not accumulated model reasoning. `learn_from_batch` appends every received example without correctness filtering, deduplication or per-content human approval. `set_state` replaces the list from JSON; arbitrary callers' initial-content control is unresolved. Prediction derives Q/A text, using raw question when supplied and full input otherwise. Stored examples have advisory force through model interpretation, not executable label rules. No counterpart object exists in supplied runtime; this is retained data consumed inside [RT-RTE-classification-search](runtime.md#rt-rte-classification-search) and [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize), not candidate Python. SRC-1, `reference_examples/text_classification/agents/fewshot_memory.py`.

> ex = {"input": r["input"], "target": r["ground_truth"]}
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

> self.examples.append(ex)
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

#### MEM-OBJ-memory
Label: Classification memory checkpoint

`memory.json` is the benchmark's file checkpoint, produced from candidate `get_state`, later read by `set_state`. The file extension does not enforce JSON or a uniform schema: the interface returns a string. For few-shot it serializes [MEM-OBJ-examples](#mem-obj-examples); for NoMemory it is inert `_state`, which prediction does not use. Unknown generated candidates may serialize other content. Distinct from the live examples list and raw log: this is a save/reload transport object spanning processes. No supplied counterpart object; closest route is [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize). Substrate is local run-directory disk, keyed by dataset/candidate/model/seed; no content-digest binding to candidate code is shown. SRC-1, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/agents/no_memory.py`.

> Path(args.save_memory).write_text(memory.get_state())
> --- `reference_examples/text_classification/inner_loop.py`

> self._state = state
> --- `reference_examples/text_classification/agents/no_memory.py`

Checkpoint alternatives include JSONL `checkpoint` events embedding `memory_state`, and in-memory `best_state` captured after epoch validation. The offline loop restores the best epoch if it precedes the final epoch. This is validation-driven state replacement by software, not necessarily criticism of state content. Direct loading accepts a caller-supplied path without the benchmark's run-key selection; automatic restoration from JSONL is not established. SRC-1, `reference_examples/text_classification/inner_loop.py`.

> self.log("checkpoint", step=step, memory_state=memory_state)
> --- `reference_examples/text_classification/inner_loop.py`

> if best_state is not None and best_epoch < num_epochs - 1:
> --- `reference_examples/text_classification/inner_loop.py`

#### MEM-OBJ-classification-log
Label: Classification JSONL trace

`log.jsonl` is software-authored disk JSONL, initialized by truncating its path. Symbolic events hold step, predictions, targets, correctness, lengths/hashes, timings and optional serialized checkpoints; text previews are natural-language material. Online `step` and offline `eval_step` events retain only the first 200 input characters, not full examples. Offline `train_batch` events retain counts/timing rather than equivalent prediction traces. The separate returned trajectory can hold full input and metadata, but must not be conflated with what the log consumer receives. Prompt hash/length are access/measurement metadata, not the prompt itself. Proposer instructions afford later reading/prototyping; no automatic transformation of this log into the few-shot store occurs. The latter receives batches directly. No supplied counterpart object; closest is history read-back in [RT-RTE-classification-search](runtime.md#rt-rte-classification-search). SRC-1, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`.

> input_preview=inp[:200],
> --- `reference_examples/text_classification/inner_loop.py`

> self.path.write_text("")
> --- `reference_examples/text_classification/inner_loop.py`

#### MEM-OBJ-frontier-val
Label: Reference validation frontier

Each reference experiment maintains its own `frontier_val.json` on disk. These are symbolic summaries with candidate identities and measured evaluation aggregates, not candidate code or explanatory theory. Classification stores per-dataset winners and aggregate accuracy/context-size Pareto entries; terminal stores per-task winners and overall best, replacing on strict improvement. Software controls admission to frontier entries; initiating the search is not human approval of each entry. Later consumers are driver resume/status/final-selection code and instructed proposer reads. At the driver the fields have fixed selection force; at the proposer their displayed scores are evidence interpreted by a model. No supplied object counterpart; these are results of [RT-RTE-classification-search](runtime.md#rt-rte-classification-search) and [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search), not duplicated routes. SRC-1, `reference_examples/text_classification/benchmark.py`, `reference_examples/terminal_bench_2/meta_harness.py`; classification selection evidence is also retained in the supplied runtime route.

> current_best_avg = frontier.get("_best", {}).get("avg_pass_rate", -1)
> if avg > current_best_avg:
> --- `reference_examples/terminal_bench_2/meta_harness.py`

#### MEM-OBJ-evolution-summary
Label: Reference evolution summary parts

The separate reference `evolution_summary.jsonl` files form a valid mixed container with two separately declared operative parts: [MEM-OBJ-summary-results](#mem-obj-summary-results) and [MEM-OBJ-summary-rationale](#mem-obj-summary-rationale). Symbolic iteration/candidate/score/delta/outcome/timing fields are software-derived from manifests and evaluation aggregates and support iteration resume and displayed comparison. Natural-language hypothesis fields (plus terminal `changes`) are model-authored manifest content copied by software, and are later offered as design rationale. Terminal additionally retains rollout metrics; classification optionally retains component tags. Stored on run-local disk and appended rather than rewritten, these summaries are distinct from [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval): the pending handoff is transient, whereas summaries join hypotheses to later outcomes. The mixed parts do not share identical authority: counters drive deterministic resume, hypotheses inform the next model. The driver does not verify the truth of the rationale. SRC-1, both `reference_examples/text_classification/meta_harness.py` and `reference_examples/terminal_bench_2/meta_harness.py`.

> "hypothesis": c.get("hypothesis", ""),
> "changes": c.get("changes", ""),
> --- `reference_examples/terminal_bench_2/meta_harness.py`

> if name in metrics:
>     row["rollout_metrics"] = metrics[name]
> --- `reference_examples/terminal_bench_2/meta_harness.py`

The quoted classification delta is relative to the frontier read at summary time, not necessarily a pre-update incumbent. That distinction prevents interpreting every positive/negative delta as an independent before/after improvement estimate. SRC-1, `reference_examples/text_classification/meta_harness.py`.

> "delta": round(avg_val - best_val, 1) if best_val else None,
> --- `reference_examples/text_classification/meta_harness.py`

#### MEM-OBJ-summary-results
Label: Evolution summary result and control fields

Part of: [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary)

This part is the symbolic result/control projection in each run-local disk JSONL row: driver iteration, candidate identity, score aggregates, delta, formatted outcome, optional timing and terminal rollout metrics. Candidate identifiers/import paths are copied manifest metadata; iteration and measured/derived fields are supplied or calculated by software, not model-authored explanation. The classification driver rounds `avg_val` and calculates delta from the frontier at summary time; terminal rounds aggregate/per-task pass rates and copies collected rollout metrics. A zero/missing result can become `failed`, so that label is not a diagnosis of the failure mechanism. These fields are derived evidence and control state rather than raw trajectories or retained causal reasons. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`, implementation.

Software automatically appends these fields without per-row human approval or a score-improvement admission threshold. Resume code reads the maximum iteration to choose the next iteration; proposer/analysis models are instructed to read result history for comparison. Counters have deterministic control authority at resume; metrics have advisory evidential authority at the model reader. Summary fields do not themselves select frontier winners or execute candidate code. Writes and resume consumption are wired; actual model reading, reliance and measurement validity in a deployed run are uninspected. Fresh-start deletes the container rather than selectively retracting a result field; no independent field-expiry or source-digest invalidation is shown. Both reference drivers implement the following resume expression. SRC-1, the same two driver paths and both proposer skills: `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

> max_iter = max(max_iter, json.loads(line).get("iteration", 0))
> --- `reference_examples/text_classification/meta_harness.py`

> "avg_pass_rate": round(avg, 3),
> "per_task": {k: round(v, 3) for k, v in per_task.items()},
> --- `reference_examples/terminal_bench_2/meta_harness.py`

This is a material part of the summary container, not a duplicate of [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval), whose manifest precedes measurements. It overlaps the summary-field subset of the broader [EPI-OBJ-val-results](epistemic.md#epi-obj-val-results), supplied in the refusal, but does not denote that record's result files or frontier identities. Reconciliation should retain that overlap, not infer exact cross-artifact identity.

#### MEM-OBJ-summary-rationale
Label: Evolution summary hypothesis and change fields

Part of: [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary)

This part is model-authored natural-language `hypothesis` and terminal `changes`, copied from the pending manifest into run-local disk JSONL. Classification `axis` and optional `components` are copied symbolic design labels, not measured results. JSON field names provide addressability, but hypothesis/change text receives consequences through model interpretation. The retained reasons are proposed mechanism claims and change descriptions, not necessarily post-evaluation criticism or a complete rationale. Missing fields become empty strings or default labels; drivers do not validate the truth of the copied explanation. Authorship is model work; physical copying and automatic admission are software operations, without per-content human approval. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`, implementation; manifest authorship is also described in [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval).

The classification proposer and terminal analysis child are intended later readers through instructed file reads, not automatic full-content injection. Their skills ask them to interpret prior attempts alongside scores and traces. No separate hypothesis-only selector or context budget is wired. The resume parser uses iteration, not hypothesis meaning. At the actual model consumer this part has advisory design authority; it neither warrants a numerical result nor directly gives code execution authority. Retention is wired; later model use is afforded by shipped procedure, and exercised reliance is uninspected. Fresh-start withdraws the summary container, while copied candidate files or other residual artifacts can remain subject to the cleanup limits already recorded. SRC-1, both drivers and `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`, doctrine/design for requested reading.

> Check `evolution_summary.jsonl` for what's been tried — parameter sweeps (pool sizes, retrieval counts, context budgets, similarity metrics) almost always regress or tie.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

> `evolution_summary.jsonl` - what's been tried, what worked/didn't, plus `rollout_metrics` (path given in task prompt)
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

The hypothesis/change-copy passage is retained in the parent. This is the later retained copy, not a re-declaration of the transient [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval). It is distinct from [MEM-OBJ-summary-results](#mem-obj-summary-results) in producer, form and authority. The supplied [EPI-OBJ-val-results](epistemic.md#epi-obj-val-results) explicitly excludes these hypotheses and cannot supply this part's lineage or consumer assessment. Proposed explanations are not software-derived warrant; no exercised criticism-mediated revision or learning gain follows from preserving them.

#### MEM-OBJ-reports
Label: Requested post-evaluation reports

Reference run prompts name a reports directory. Classification skill requests missing post-evaluation reports of at most 30 lines, including changes, improvements/regressions, why, and a takeaway. They are afforded model-authored natural-language files on disk, not established produced reports. Interpretation of traces/scores can transform experience into prospective guidance; no deterministic fact-check or approval gate is wired for their content. The classification proposer is the intended later reader, but its explicit Step 1 read-all list names summary/frontier/config/traces rather than reports. Terminal prompt names the directory without an equivalent enforced report-writing step in its supplied skill. No counterpart object in runtime; related affordance is [RT-RTE-classification-search](runtime.md#rt-rte-classification-search). SRC-1, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/terminal_bench_2/meta_harness.py`.

> Each report should be **<=30 lines** covering: what changed, which datasets improved/regressed and why, and a takeaway for future iterations.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

#### MEM-OBJ-completion-cache
Label: Classification completion cache

`llm.py` stores symbolic keyed JSON files containing natural-language `content` plus symbolic token/cost fields. Provider completion is the original producer; software admits it automatically and returns cached content on later identical-key calls. Lineage preserves an extracted response rather than full provider payload or model weights. Exact selection uses cache version, normalized model, API base, system prompt, prompt and kwargs. It does not include exact backend weights. These are retained outputs, distinct from task memory or raw traces and from [RT-CMP-classification-llm](runtime.md#rt-cmp-classification-llm), whose cache mention refers to this subsidiary store. Substrate is `CACHE_DIR` on local disk; provider-native caches are different. SRC-1, `reference_examples/text_classification/llm.py`.

> return CACHE_DIR / f"{digest}.json"
> --- `reference_examples/text_classification/llm.py`

#### MEM-OBJ-evaluation-history
Label: Pilot evaluation history and snapshots

Part of: [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search)

This object is the retained-output part of the pilot route, not another declaration of its progression. Source snapshots `harness-N.py` and full `evaluation-N.json` remain on host logs; controller results hold source hash, acceptance, reason, reward and task results. `EvaluationState.history` is an in-memory tuple of result dictionaries serialized to `evaluation_history.json`, then uploaded to the outer task. Source is symbolic executable material; hash/acceptance/rewards/budget are symbolic data; reason/verifier summaries are natural-language explanations nested in JSON. Source snapshots are separate from readable feedback. The outer model receives only reward, tasks, reason under `verifier_summary`, and remaining budget: source hash and acceptance are not explicitly delivered in that projection. The final verifier reads full history and acceptance flags, not those model messages. Software writes the report automatically; shell-access implications and budget counterpaths remain those in the supplied route. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`.

> "reward": result.get("reward", 0.0) or 0.0,
> "tasks": result.get("tasks") or [],
> "verifier_summary": result.get("reason"),
> "remaining_budget": next_state.remaining,
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

> if entry.get("accepted") and entry.get("reward") is not None
> --- `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`

### Routes

#### MEM-RTE-classification-memory
Label: Classification batch memory update and reuse

Operator-selected candidate is instantiated → offline labelled batch or online evaluated batch → candidate `learn_from_batch` → state/optional best-epoch restore → save → subsequent prediction or benchmark-selected reload. The driver/inner loop decides batch ordering, mode, evaluation and persistence; the candidate owns transformation. This spans memory operations inside [RT-RTE-classification-search](runtime.md#rt-rte-classification-search) and [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize), distinct from their outer code-admission/selection routes. SRC-1, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/agents/fewshot_memory.py`, `reference_examples/text_classification/benchmark.py`.

- Immediate return: Candidate state changes and prediction/metadata; inner loop returns target-backed evaluation metrics.
- Later read-back: Few-shot formats stored examples for subsequent solver calls; test child reloads `memory.json` before prediction. JSONL checkpoints are inspectable but an automatic replay loader is not established.
- Delegated visibility: Child process receives candidate, dataset/model/seed configuration and state path, not outer proposer transcript; each solver call receives current task plus selected demonstrations.
- Selection predicate: Stable SHA-256-derived input seed controls sampling/shuffling; sample max_examples when list exceeds that count, otherwise shuffle recent slice. Formatter stops when the next example would exceed MAX_CHARS. Test checkpoint selected by dataset/candidate/model/seed path.
- Invalidation or expiry: List grows on batch update, replacement occurs through `set_state`; offline best-epoch restore can undo later epochs. Usable result files skip reruns, not source-digest invalidation. NoMemory's restored state does not affect its prompt.
- Activation or effect: Implemented demonstration delivery asks model to follow patterns. State loading alone does not establish dependence for every candidate; no exercised solver effect or benefit was observed.
- Evidence limits: Generated candidate transformations, caller-supplied checkpoint provenance and candidate mutation during `predict` are not universally controlled by this interface. Character budgets are not strict token guarantees.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software/model transformation, not per-example human acceptance. The operator chooses workflow/configuration. Few-shot admits all batches; arbitrary candidates can accept/reject/transform feedback. Offline checkpoint comparison uses dataset evaluator accuracy and software restores the best captured state, whereas online updates use evaluator correctness and labels. These are bounded training/evaluation modes. Stored demonstrations retain correct answers but not criticism/reasons. Learning as improved future capacity is uninspected; example retention alone does not establish benefit. This route makes no independent theory-builder or self-improvement attribution. SRC-1, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/agents/fewshot_memory.py`.

> "prediction": ex["target"],  # Ground truth visible
> "ground_truth": ex["target"],
> "was_correct": True,
> --- `reference_examples/text_classification/inner_loop.py`

> to_use = rng.sample(self.examples, self.max_examples)
> --- `reference_examples/text_classification/agents/fewshot_memory.py`

#### MEM-RTE-completion-replay
Label: Classification completion replay

LLM callable truncates prompt → provider wrapper derives key → hit returns stored content; miss calls provider, extracts content/usage, saves JSON and returns content. Software selects and writes; consumer is the candidate prediction/learning call requesting that response. Distinct from [RT-CMP-classification-llm](runtime.md#rt-cmp-classification-llm) model identity and [MEM-RTE-classification-memory](#mem-rte-classification-memory) supervised memory. SRC-1, `reference_examples/text_classification/llm.py`.

- Immediate return: Extracted model content, replayed or freshly generated.
- Later read-back: A later same-key request receives cached content from disk in place of a fresh provider call.
- Delegated visibility: Provider receives system/user messages on miss; on hit no new provider request is made by this wrapper.
- Selection predicate: Exact digest of version/model/API base/system prompt/truncated prompt/kwargs; not semantic relevance or a model-chosen retrieval query.
- Invalidation or expiry: Missing/unreadable JSON falls back to generation; version/key changes separate entries. No expiry or backend-weight invalidation appears in the inspected cache methods.
- Activation or effect: Cached content becomes the returned LLM response with answer-producing force at downstream extraction. Actual hits and answer changes were not observed.
- Evidence limits: Cache payload integrity and exact backend model identity are not verified; `cached["content"]` assumes an appropriate field. Opaque provider reuse is outside this local route.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Cache admission is automatic after provider success, without human review or candidate-quality comparison; writing failures are ignored. It is response reuse, not trace-derived lesson synthesis. The trimming rule preserves head/tail with a marker and discards the middle from provider-visible context; no reload operation is wired there. The saved/thread-local original prompt and logged length cannot establish what the provider saw after truncation. Supplied [runtime](runtime.md) retains the truncation passage. SRC-1, `reference_examples/text_classification/llm.py`.

> cached = self._load_cache(cache_path)
> if cached is not None:
>     return cached["content"]
> --- `reference_examples/text_classification/llm.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-classification-search](runtime.md#rt-rte-classification-search)

Memory-specific read-back is path-directed but model-selected: driver starts a fresh proposer with state paths; skill requests reads of all summary/frontier state and recent logs. It does not push those files' full contents, implement semantic retrieval or enforce read completion. No numerical aggregate context budget is established for these reads; reports have a requested 30-line cap. Symbolic scores support software selection, while natural-language hypothesis/report content has advisory model authority. Trace-fed summary writes join manifest rationale with scores; direct batch writes, not JSONL consumption, produce classification examples. Summary rationale survives into the next-round affordance, but compliance and criticism-mediated revision remain unobserved. SRC-1, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/text_classification/meta_harness.py`.

> Treat `evolution_summary.jsonl`, `frontier_val.json`, and recent training traces as the only shipped history sources in this trimmed repo.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

Reset deletes nonbaseline agent files, summary/frontier/pending files and validation results, but does not delete every checkpoint, training log, report, test result or completion cache. Thus withdrawal of code/frontier is not complete erasure of experience. Residual files can remain reachable via shell; no guarantee of consistent cross-object cleanup follows from the `fresh_start` label. SRC-1, `reference_examples/text_classification/meta_harness.py`.

> val_files = list(LOGS_DIR.rglob("val.json"))
> for f in val_files:
>     f.unlink()
> --- `reference_examples/text_classification/meta_harness.py`

#### On [RT-RTE-classification-finalize](runtime.md#rt-rte-classification-finalize)

Saved state is a requested file load, not unsolicited memory push. The benchmark selects a run-keyed memory path and skips jobs missing it; the inner-loop `--load-memory` alternative accepts an explicit caller path and skips training. State arrives in a new candidate instance; the candidate decides whether and how prediction uses it. The reference NoMemory counterexample prevents inferring behavioral activation merely from successful loading. Supplied runtime contains the load passage. SRC-1, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/agents/no_memory.py`.

#### On [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search)

Terminal summary fields retain hypothesis, changes, per-task scores and optional rollout metrics; software frontier summarizes winners, while trajectories remain separate evidence artifacts. Skill requests analysis-child reads of both successful and failed trajectories, state files and code, then a short STATE/HYPOTHESIS/CANDIDATE return. Implementation child receives selected changes, class/name and directory, returns file/status, and edits shared disk. This is an afforded selected-input frame: returned prose can escape while files are shared effects, not frame-local memory. The host decides actual isolation and any compaction; the repository specifies no complete context-size budget. Reports directory naming does not demonstrate reports exist or are read. SRC-1, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`, `reference_examples/terminal_bench_2/meta_harness.py`.

> Use the current run outputs under `jobs/` and `logs/` as the primary source of truth.
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

Reset deletes generated agents and summary/frontier/pending files, but its inspected body does not clear every Harbor job or new prompt template. This preserves residual evidence but does not provide transactional rollback. Raw trajectory-to-hypothesis-to-code transformation is requested model work, not a demonstrated automatic learning process. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`.

#### On [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution)

Raw task conversation/screens feed an inherited summarizer when proactive check triggers or a context-overflow exception occurs with summarization enabled. Derived natural-language `summary_prompt` is appended to a retry request and chat history; pending handoff text and subagent references are also recorded in trajectory structures. These are separate consumers: model-visible handoff text shapes subsequent inference, while references index execution evidence. Storage begins in in-memory chat/trajectory; broader Harbor persistence is external. The inherited summarizer's exact selected inputs, retained reasons, overwrite behavior and proactive budget remain uninspected. It cannot be treated as merely raw trace accumulation or as proven faithful semantic curation. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`.

> messages = chat.messages.copy()
> messages.append({"role": "user", "content": summary_prompt})
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

Fallback is another checkpoint form: after unwinding to free 4,000 tokens and failed summarization, it adds original instruction and last 1,000 screen characters to whatever chat messages remain. It does not prove all prior messages were discarded. The supplied runtime's fallback description needs this qualification. The fallback reconstructs current observable state, not prior decision reasons; no automatic reload of evicted turns is established. Proactive handoffs can split linear trajectory or append a handoff step, preserving evidence for later search analysis without proving complete retained reasoning. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`; supplied runtime retains unwind/fallback passages.

Prompt-cache decoration is access metadata, not a new semantic store: Anthropic/Claude model-name detection marks content in the last three messages `ephemeral` on a deep copy. Provider substrate, expiry and actual hits remain opaque. The full request still includes other messages; last-three decoration is not a last-three context-selection rule. Image frames exclude full chat and return textual analysis; output-limiting preferential retention is inherited, while the 30,000-byte requested limit is local. SRC-1, `reference_examples/terminal_bench_2/anthropic_caching.py`; image/output evidence in the supplied runtime route.

> if n >= len(cached_messages) - 3:
> --- `reference_examples/terminal_bench_2/anthropic_caching.py`

#### On [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search)

Full controller results and source snapshots remain on host logs; projected feedback goes directly into ordinary tool-message accumulation, not a demonstrated cross-run memory loader. The projection in [MEM-OBJ-evaluation-history](#mem-obj-evaluation-history) omits source hash and acceptance but includes task summaries, reward and reason. Rejected source still produces a history entry on a normally completed evaluation; outer exceptions may return errors without history/budget update. Controller temporary candidate code is withdrawn after evaluation, while snapshots/results persist. Final report is automatically uploaded; verifier filters accepted reward-bearing entries and chooses max if arithmetic is valid. That consumer gives fixed scoring authority to historical data, not policy authority to the final edited harness. No automatic restore-best path is established. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`; supplied runtime retains rejection/budget/max-reward passages.

Outer shell stdout and stderr tails are selected by code at 12,000 characters each. Removed heads are not stored in model messages by this mechanism; shell filesystem/log reads can recover files when available, not arbitrary lost stdout. Child receives staged candidate source and selected task/model inputs, not outer conversation/history. These are isolated invocation inputs with shared artifact effects; they are not a trace-fed child memory update. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`, supplied runtime child route.

> "stdout": (execution.stdout or "")[-12000:],
> "stderr": (execution.stderr or "")[-12000:],
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

#### On [RT-RTE-domain-onboarding](runtime.md#rt-rte-domain-onboarding)

The intended retained result is model-authored `domain_spec.md`, natural-language decisions/defaults/unknowns on disk with later implementation-agent readership. Operator decisions supply consequential content; the specification must not silently convert suggested budgets into spend authorization. This handoff selects relevant decisions rather than requiring transcript replay. It affords cross-session context through a document; actual creation/load and exact downstream reliance are unobserved. SRC-1, `ONBOARDING.md`; evidence and the no-implementation restriction are retained in the supplied runtime record.

## Write side

Classification admission has three distinct layers: code admission by outer import checks; supervised batch transformation by candidate code; and checkpoint selection by software. No layer implies per-content human approval. Offline data uses ground truth even in its `prediction` field, so this pathway is not exclusively learning from solver failures. Online batches include genuine evaluator feedback, but few-shot discards predictions, correctness and reasons. Best-epoch restore is software curation of whole state by validation score. [MEM-RTE-classification-memory](#mem-rte-classification-memory).

Reference summaries join separately admitted parts: [MEM-OBJ-summary-results](#mem-obj-summary-results) is automatic result/control projection, while [MEM-OBJ-summary-rationale](#mem-obj-summary-rationale) preserves copied model-authored claims and design labels. Copying rationale beside measured scores is not an automatic causal inference or verification of those claims. Requested reports can derive guidance from outcomes and explanations, but their contents, truth and future use are unobserved. Candidate code can embody a resulting rule and later gain execution authority, independently of frontier selection. The supplied runtime theory accounts remain bounded claims about requested criticism and iteration; this report does not infer successful learning from retention. [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary), [MEM-OBJ-reports](#mem-obj-reports), [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution).

Cleanup/rejection have different retention consequences. Manifest deletion removes the immediate proposal handoff, not code/history. Failed imports or smoke/evaluation failures can remain summary outcomes; frontier can retain previous winners. Fresh-start deletes selected code/index/result files but leaves some raw artifacts and caches. Pilot syntax/reference rejection becomes retained feedback without child execution, while temporary staging is cleaned after accepted evaluation. A history rejection does not undo outer source edits. These limits are retained in the search annotations and [MEM-OBJ-evaluation-history](#mem-obj-evaluation-history).

Cache writes automatically retain provider response content. They synthesize no general lesson, and stale backend identity is not invalidated by a model-name key alone. KIRA compaction is the other trace-fed derived route: raw task history becomes a handoff for later inference, with selection/rationale fidelity dependent on uninspected inherited implementation. [MEM-RTE-completion-replay](#mem-rte-completion-replay), [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution).

## Read-back

There is no single universal retrieval algorithm. Few-shot requests demonstrations by stable per-input sampling/shuffling plus a formatting cap; checkpoint loading requests a run-keyed file; completion replay requests an exact digest; proposer file reads are instructed but chosen by the coding model. KIRA pushes a derived handoff on context pressure; the selector and derivation inside Harbor are opaque. Pilot feedback is direct current-conversation return, while its final verifier rereads the durable report. Onboarding affords later document loading by an external implementation agent. The covering route records/annotations retain each consumer's actual delivery, authority and limits.

Summary read-back separates consumers: [MEM-OBJ-summary-results](#mem-obj-summary-results) supplies the iteration field to deterministic resume and comparisons to instructed model readers; [MEM-OBJ-summary-rationale](#mem-obj-summary-rationale) offers hypotheses/changes to those model readers, with no demonstrated reliance or direct execution force. Their shared JSONL substrate does not make their lineage, warrant or authority uniform.

Selection evidence must not be overread. Few-shot input affects random seed, not semantic matching to stored questions. A path in a prompt establishes addressability and requested reading, not targeted semantic retrieval or complete delivery. Frontier identities drive deterministic final selection but do not inject the frontier's full rationale into task solvers. Caches return content while token/cost metadata remains software accounting. Trajectory references and hashes locate/describe material; they are not themselves model-readable reasoning. SRC-1, `reference_examples/text_classification/agents/fewshot_memory.py`, `reference_examples/text_classification/llm.py`, `reference_examples/terminal_bench_2/agents/baseline_kira.py`; see [MEM-RTE-classification-memory](#mem-rte-classification-memory), [MEM-RTE-completion-replay](#mem-rte-completion-replay).

The context-control frame lens is partial. Fresh proposer sessions and requested child roles keep prior transcript out while passing paths or selected instructions; child returns and shared files escape. KIRA eviction is unlike popping a whole frame because an inherited subset of messages can remain alongside derived text. Pilot child source and model configuration are selected inputs, with externally executed file effects. No local pointer/liveness model makes omitted context automatically reachable. Reload requires a distinct file/tool operation, and neither prompt-middle truncation nor tool-tail trimming wires one automatically. Supplied runtime and annotations above bound these conclusions.

## Integration issues

- Qualification of supplied KIRA fallback wording: [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution) says fallback keeps original instruction plus last 1,000 screen characters. The inspected retry also copies remaining `chat.messages`; those two items are the fallback text, not necessarily the entire next context. This prevents a total-history-discard conclusion. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`; quoted retry above.
- Qualification of classification trace consumption: [RT-RTE-classification-search](runtime.md#rt-rte-classification-search) describes training traces as history inputs. [MEM-OBJ-classification-log](#mem-obj-classification-log) shows partial input previews and mode-dependent events, not necessarily full examples. Skill instructions to prototype using real logged examples are an affordance whose fidelity is not guaranteed by those log fields. SRC-1, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`.
- The correction preserves [MEM-OBJ-evolution-summary](#mem-obj-evolution-summary) as a valid container and separately declares [MEM-OBJ-summary-results](#mem-obj-summary-results) and [MEM-OBJ-summary-rationale](#mem-obj-summary-rationale). Driver summary writes and resume parsers, plus both proposer skills, were directly rechecked at SRC-1. The result/control part overlaps the summary subset of [EPI-OBJ-val-results](epistemic.md#epi-obj-val-results), but not its complete cross-artifact referent; the rationale part is explicitly excluded there. Neither part duplicates [RT-OBJ-pending-eval](runtime.md#rt-obj-pending-eval): they are retained post-evaluation projections/copies, not the transient input manifest. This resolves the missing-part defect without transferring software-derived warrant to model-authored explanation.
- No new record re-declares a supplied referent. New data objects are parts/results or subsidiary stores described by supplied routes; the pending manifest comparison and pilot `Part of` relation are explicit. The new batch-memory and replay routes name different operations from outer search/finalization routes, with overlap noted beside each.
- Unresolved generated-candidate state: [MEM-OBJ-memory](#mem-obj-memory) cannot enumerate formats or downstream effects for code not present at the pin. The interface leaves transformation and mutation control to candidates; this prevents universal memory, invariance or provenance conclusions. SRC-1, `reference_examples/text_classification/memory_system.py`.
- Unresolved KIRA/host internals: exact proactive selection, eviction, summarizer inputs/output rationale and provider-cache retention are uninspected outside the frozen source. This prevents complete curation/fidelity/reload claims while preserving wired handoff delivery. [RT-RTE-kira-execution](runtime.md#rt-rte-kira-execution), [RT-BAP-proposer-instructions](runtime.md#rt-bap-proposer-instructions).
- Requested reports and child analyses have no supplied run artifacts. [MEM-OBJ-reports](#mem-obj-reports), [RT-RTE-terminal-search](runtime.md#rt-rte-terminal-search) establish intended guidance/return channels, not produced criticism or exercised cross-round improvement.
- Pilot history is more complete than model-visible feedback and does not bind final code to historical max reward. [MEM-OBJ-evaluation-history](#mem-obj-evaluation-history), [RT-RTE-pilot-search](runtime.md#rt-rte-pilot-search) preserve that distinction. Controller source hashes support lineage recording, not cryptographic verification by the final reward consumer.

## Limitations and checks

Frozen source HEAD was rechecked as `8123ccabe2b19fa1123090b2e5f1bacc20963ce8`; source checkout status was clean. The supplied run/source identity and member/record contracts were reread. This correction directly rechecked both drivers' summary construction and resume parsing, and both proposer skills, against the frozen checkout; other findings and their limits are carried from the supplied previous report rather than re-analysed. Direct additions to inspected coverage are identified in the table; source layers remain implementation and doctrine/design. No additional source identity was introduced, target tests executed or provider called.

No observed search, cached response hit, successful checkpoint use, faithful summary or measured benefit was supplied. Source inspection supports wiring and bounded affordances, not reliance, causal gains, secrecy or complete cleanup. Unknown checkpoint initialization, inherited compaction and unproduced criticism remain local limits rather than unsupported absences.

Validation: deterministic output validation passed; this checks structure, references and quotation occurrence, not semantic acceptance or performance.
