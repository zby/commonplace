---
type: types/agentic-system-analysis-result.md
description: "OpenRSI's released OpenMLE search, task construction and training routes, with complete source-bounded analysis"
run-id: AAS-2026-09-26-openrsi-01
system: OpenRSI
run-date: "2026-09-26"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
analysis-cutoff: "2026-09-26"
evidence-tier: code-grounded
memory-comparison:
  scope: "Released Evo and ERL accumulated program archives and access metadata, trace-derived experience cards and rich summaries, training-trace selection and SFT learning, plus RL learning and checkpoint reuse at the shipped external interfaces. Includes optional and legacy memory branches; excludes external training engine internals, unknown external corpus contents, static skills, Gym task packages as environment definitions, and transient builder dialogue including Gym prepare retry history."
  axes:
    storage_substrate:
      assessment: known
      basis: afforded
      values: [files, in-memory, sqlite, model-weights]
      records: [OBJ-3, OBJ-5, OBJ-6, OBJ-13, OBJ-14, RTE-4, RTE-5]
      note: "Journal/node state and caches, SQLite RL archive, JSONL/Parquet training tables, and parameter checkpoints. RL learned parameters are covered at the external training interface; no graph database inferred from parent links."
    representational_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic, parametric]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-5, OBJ-6, OBJ-13, OBJ-14]
      note: "Code, identifiers and numeric selection state are symbolic; plans, execution text and summaries carry language; trained weights are parametric. Checkpoint runtime-state containers do not turn weights into symbolic knowledge."
    lineage:
      assessment: known
      basis: afforded
      values: [trace-extracted, imported]
      records: [RTE-10, RTE-4, RTE-5, RTE-11]
      note: "Automatic extraction from executions and trajectories plus supplied annotation/checkpoint/data interfaces. External authorship and pretraining histories are outside this boundary."
    behavioral_authority:
      assessment: known
      basis: afforded
      values: [knowledge, ranking, routing, learning]
      records: [RTE-3, RTE-4, RTE-5, RTE-10, RTE-11]
      note: "Summaries and prior code inform model generation; metrics rank parents and route operator fallback; selected messages/rewards train parameters; checkpoints supply learned behavior. Static instructions and test evaluators are excluded from this memory authority union."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic]
      records: [RTE-3, RTE-4, RTE-5, RTE-10]
      note: "Inspected in-boundary writes are automatic, including operator-triggered selection/training. Configuration editing and unknown production of imported annotations are not manual memory-writing routes established here."
    curation_operations:
      assessment: known
      basis: wired
      values: [decay, dedup, synthesize]
      records: [OBJ-3, OBJ-13, OBJ-14, RTE-4, RTE-10]
      note: "Retained rich summaries request new comparative experience; program pruning/cooling forgets or downweights; SFT message hashing removes duplicates. New candidate generation is acquisition, metadata recomputation is ranking, and neither is counted as evolve or promote. No retained withdrawal history establishes invalidate."
    read_back_direction:
      assessment: known
      basis: afforded
      values: [pull, push]
      records: [RTE-3, RTE-4, RTE-5, RTE-10, RTE-11]
      note: "Automatic selected context goes to generation models; trainers request batches and configured loaders request checkpoints. These are distinct consumption operations, not double-counting the return from one API request."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse, identifier, inferred-lexical]
      records: [RTE-3, RTE-10]
      note: "Task/operator/score/recency filtering is coarse; parent, ancestor, sibling and node matching targets identities; inferred error-signature extraction and matching target related failures. SFT annotation judgment is admission to the dataset, not an additional context-push signal. Numeric ranking is not LLM judgment."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-10, RTE-4, RTE-5]
      note: "The wired retained-summary route alone establishes yes; SFT parameter training supplies a second wired route. RL is afforded through the external engine. This does not establish theory criticism or demonstrated benefit."
    trace_source:
      assessment: known
      basis: afforded
      values: [tool-traces, trajectories]
      records: [RTE-10, RTE-4, RTE-5]
      note: "Execution output and scored experiment trajectories feed summaries, message datasets, and learning interfaces. No separate event-stream or general session-log learner was established."
    learning_scope:
      assessment: known
      basis: afforded
      values: [per-task, cross-task]
      records: [RTE-10, RTE-4, RTE-5]
      note: "Experiment memory is task-keyed; selected multi-task messages and task-prompt streams train a shared parameter set. No project-specific learning horizon is inferred from an output directory."
    learning_timing:
      assessment: known
      basis: afforded
      values: [online, offline]
      records: [RTE-10, RTE-4, RTE-5]
      note: "Cards/summaries arise during search; RL interfaces consume live rollouts. SFT selects completed traces and trains offline. A pipeline having stages does not add staged as a third learning schedule."
    distilled_form:
      assessment: known
      basis: afforded
      values: [natural-language, symbolic, parametric]
      records: [OBJ-13, OBJ-14, OBJ-5, OBJ-6, RTE-10, RTE-4, RTE-5]
      note: "Derived cards retain symbolic selection/error features; summaries and selected training messages retain language and code; SFT/RL produce parameters. Covers the same routes as trace_learning."
    faithfulness_tested:
      assessment: known
      basis: claimed
      values: ["no"]
      records: [ABS-1]
      note: "No retained execution test of dependence on recalled content was found within inspected release claims and memory tests. Source test definitions and training smoke prose do not supply a qualifying memory intervention result."
---

# OpenRSI agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-openrsi-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/openrsi.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-openrsi-01/memory-report.md`

**Memory analysis report SHA-256:** 64b3a2914bc1dfe922618c99107624c272c1adec0d45cf7c75d00e52dd3a0c0f

## Boundary and evidence

Evidence basis: static inspection of released source code and repository documents at commit `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`, frozen on 2026-09-26. Repository performance tables are reported operation, not independently inspected executions or causal experiments.

The question is what Frontis's publicly inspectable system actually connects: executable task construction, program evolution, retained experience, and training of the program-generating model. The source-native name is OpenRSI; its released executable stack is OpenMLE, comprising Gym, Evo and ERL (the source directory for OpenMLE-RL). This is a builder or improvement plane, with an enclosing evolutionary runtime inside it. The whole-system boundary covers the released stack and its material interfaces, not every dependency's internals.

Included: MLE-Bench search adapter, shared synchronous/asynchronous evolutionary controller, NatureBench adapter interface, task-package construction and quality checks, sandbox execution/scoring interface and worker mount configuration, SFT selection/training interfaces, RL rollout/reward/database interfaces, and their memory routes. Excluded: Horizon; external model weights and training datasets; independently installed SLIME RL optimizer internals; external NatureBench task/evaluator checkout; deployed model servers, worker images and infrastructure. These exclusions prevent conclusions about the enterprise platform, actual parameter identity, data disjointness, end-to-end deployment isolation, evaluator fidelity, and independently reproduced improvement. Vendored SFT training code is part of the repository; external RL training dependencies are not silently treated as inspected source.

The operator supplies task packages, model endpoint/checkpoint, evaluator, budgets and stage launch configuration. OpenRSI documents independently runnable stages, not a single automatic release-to-release scheduler. Dynamic model or infrastructure execution was not needed to establish these wiring boundaries.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | Git | `https://github.com/FrontisAI/OpenRSI` | `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa` | implementation | Evo controller/operators/configuration, shared archive and memory; ERL selection/training interfaces; Gym graph, metric/quality checks and sandbox mounts | `OpenMLE-Evo/scripts/evaluate_airaevo.py:295-466`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:750-2075`; `OpenMLE-Gym/builder_core/design.py:26-147`; additional full paths on records below | Absolute access root `/home/zby/llm/commonplace/related-systems/FrontisAI--OpenRSI`; worktree never used. External dependency/deployment internals uninspected; implementation supports wiring, not execution outcomes. |
| SRC-2 | Git | `https://github.com/FrontisAI/OpenRSI` | `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa` | doctrine/design | release boundary, shared operators, runtime profiles, external dependencies | `README.md:36-170`; `OpenMLE-Evo/docs/overview.md:1-104`; `OpenMLE-ERL/RL/README.md:1-46`; `OpenMLE-Gym/openmle-sandbox/README.md:1-119` | Declared purpose and operational contracts do not establish deployment. |
| SRC-3 | Git | `https://github.com/FrontisAI/OpenRSI` | `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa` | reported operation | benchmark tables, transfer comparisons, training counts and reported RL smoke | `docs/results.md:1-96`; `docs/training.md:1-31`; `OpenMLE-ERL/RL/README.md:43-46`; `OpenMLE-Evo/benchmarks/naturebench_local_quick/RESULTS.md:1-115` | Raw benchmark traces/checkpoints and independent interventions not inspected. Reported effects remain claimed at the stated comparison grain. |

No probe source was produced. Repository example artifacts were not used as independent execution evidence; the local NatureBench narrative changes both model and harness and does not isolate either contribution.

## Shared records

### Components

| ID | Source-native component | Form, state and responsibilities | Parameter change / identity evidence |
| --- | --- | --- | --- |
| CMP-1 | OpenMLE-Evo / vendored AIRA-Evo | Symbolic Python controller plus natural-language operator templates; task/sample workers, island population, journal and checkpoint state. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:750-850,1910-2062`. | Parameter changes: inapplicable to this symbolic controller. Configuration chooses synchronous generations or asynchronous workers; no inference that controller source is rewritten. |
| CMP-2 | Generation, analysis and rich-summary LLMs; trainable Frontis-MA1/base model | Distributed-parametric models invoked through GenericLLM/LiteLLM; SFT and RL consume generated samples. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:811-850`; `OpenMLE-Evo/tts_search/configs/litellm/sglang_qwen3_30b_a3b_thinking_2507.yaml:1-19`. | Inference weight update: uninspected at provider; inspected Evo client only sends generation requests. Training weight updates: wired for vendored SFT training; afforded at the external RL engine interface on RTE-5. Exact served identity: uninspected; configurable model name and base URL do not pin weight bytes. Provider internals remain uninspected. |
| CMP-3 | OpenMLE-Gym and OpenMLE Sandbox | Symbolic task graph, filesystem packages, controller/worker execution and scoring; LLM-assisted construction/quality assessment. SRC-1 `OpenMLE-Gym/builder_core/design.py:26-147`; `OpenMLE-Gym/openmle_gym/local_evaluator.py:887-934`; SRC-2 `OpenMLE-Gym/openmle-sandbox/README.md:1-119`. | Gym generator/evaluator models are separately configured distributed-parametric consumers. No parameter-update route is established for those calls; exact endpoint weights and provider processing uninspected. |

Configurable endpoint evidence for CMP-2 supports endpoint resolution, not an immutable model pin:

> model_name: ${oc.env:OPENMLE_MODEL_ID,Qwen/Qwen3-30B-A3B-Thinking-2507}
> --- `OpenMLE-Evo/tts_search/configs/litellm/sglang_qwen3_30b_a3b_thinking_2507.yaml` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> base_url: ${oc.env:SGLANG_BASE_URL,http://127.0.0.1:30010/v1}
> --- `OpenMLE-Evo/tts_search/configs/litellm/sglang_qwen3_30b_a3b_thinking_2507.yaml` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

### Operative objects

| ID | Source-native identity | Form / substrate / producer → consumer | Evidence and limit |
| --- | --- | --- | --- |
| OBJ-1 | Candidate program code | Symbolic Python, journal and files; model → executor and later Improve/Debug/Crossover calls. It states an executable proposed solution, not necessarily an explanation of why it works. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/core.py:12-33`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1945-2062`; wired. |
| OBJ-2 | Execution/evaluation feedback | Natural-language logs plus symbolic exit/validity/score fields; executor and evaluator → controller, diagnosis, memory and rewards. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py:168-245`; wired. A score warrants only its configured test contract. |
| OBJ-3 | Program database/archive and lineage metadata | Composite journal/population/database container for retained program attempts and lineage; component content and access metadata are distinguished in memory records below. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:784-809,1206-1215,1310-1339`; wired. Container identity does not decide form of every payload. |
| OBJ-4 | Operator prompts and static task guidance | Natural-language templates and symbolic configuration in repository/files; authors/operator → generation calls. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml:1-89`; wired. Static shipping does not itself establish accumulated memory. |
| OBJ-5 | Training samples and trajectories | Messages, code, execution results and selection metadata in files; rollout/selection → SFT or RL consumers. | SRC-1 training anchors and branch limits on RTE-4, RTE-5 and specialist integration. |
| OBJ-6 | Trained parameters/checkpoints | Distributed-parametric weights serialized to files; optimizer → later generation service after configured load/sync. | Training interfaces on RTE-4 and RTE-5; weight payloads and historical runs not inspected. |
| OBJ-7 | Operator plan | Natural-language text extracted before code; model → retained node and subsequent context. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/core.py:12-33`; wired extraction, plan semantics and presence not invariant. |
| OBJ-8 | Execution analysis / diagnosis | Natural-language summary and structured bug/metric values; deterministic feedback or fallback analyzer → node and later memory/revision. | SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1830-1895`; wired. Model explanation is not automatically a checked causal explanation. |
| OBJ-9 | Gym task description | Natural-language task specification derived from source data/metadata; builder → preparation/metric generators and future task solvers. | SRC-1 `OpenMLE-Gym/builder_core/design.py:99-137`; `OpenMLE-Gym/builder_core/utils/nodes.py:884-1049`; wired. Source fidelity not proved by generation. |
| OBJ-10 | Gym generated prepare script | Symbolic Python in task files; generator → compilation and execution, retry context. | SRC-1 `OpenMLE-Gym/builder_core/utils/nodes.py:884-986`; wired. Passing execution checks is narrower than correct task construction. |
| OBJ-11 | Gym generated metric program | Symbolic Python in `utils/metric.py`; generator → dynamic metric loader and scoring. | SRC-1 `OpenMLE-Gym/builder_core/utils/nodes.py:988-1060`; `OpenMLE-Gym/openmle_gym/metric_validation.py:42-92`; wired. The evaluator is also a generated artifact. |
| OBJ-12 | Gym quality evaluation | Structured numeric dimensions, reasons and recommendation; deterministic checks/model judge → persisted report. | SRC-1 `OpenMLE-Gym/openmle_gym/local_evaluator.py:553-572,727-742,887-932`; wired. Recommendation is a report disposition; training admission is not inferred from its label. |

Plan extraction for OBJ-7 has a retained representation, but the parser's default does not require one:

> operator_fn: Callable, *operator_args, max_operator_tries: int, requires_plan: bool = False
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/core.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> plan = extract_text_up_to_code(text_without_thinking)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/core.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

#### Archive detail for OBJ-3

Evo uses a task journal of node objects with parent/child links, code, plans, metrics and outputs, plus JSONL checkpoints and per-step exports. RL uses SQLite program rows with task and parent identity, code, execution payload, raw response, metadata and changing sampling fitness. These are files, in-memory structures and SQLite, not an inferred graph database. Metadata carries ranking/routing force; code and feedback carry advisory evidence to the generator. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:784-809`; `OpenMLE-ERL/RL/program_database.py:445-472,565-621,757-779`. Implementation conclusion status: wired.

>         self.logger.info(f"Found journal at {journal_path}. Loading...")
>         # Load the journal
>         with open(journal_path, "r") as f:
>             journal_export = [json.loads(line) for line in f]
>         self.journal = Journal.from_export_data({"nodes": journal_export})
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Conditional top-k pruning deletes archive entries. The RL archive also recomputes cooling from how often each program has been selected as a parent. This is downweighting by use, not forgetting by age, and it does not establish retained invalidation history.

>             if self.max_per_task > 0 and count > self.max_per_task:
>                 # Delete programs beyond top k
>                 cursor.execute(
>                     """
>                     DELETE FROM programs
>                     WHERE task_name = ? AND id NOT IN (
>                         SELECT id FROM programs
>                         WHERE task_name = ?
>                         ORDER BY fitness DESC
>                         LIMIT ?
>                     )
> --- `OpenMLE-ERL/RL/program_database.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

#### OBJ-13 — Experience cards and strategy-board features

Cards extract method family, parent delta, error signature, plan/analysis and usage from completed experiments; strategy boards derive ranking and novelty/failure summaries. They mix symbolic features and language, retained in per-step JSON, aggregate JSONL and a strategy-board JSON file; RL stores analogous metadata in SQLite. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py:379-447`; `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py:1556-1617`; `OpenMLE-ERL/RL/generate_mle.py:911-958`. These features influence parent selection and displayed operator context, so they are derived memory, not only diagnostic exports. Implementation conclusion status: wired.

>             node.experience_card = card
>             step_stat_payload["experience_card_path"] = str(
>                 step_dir / "experience_card.json"
>             )
>             step_stat_payload["strategy_board_path"] = str(
>                 output_dir / "strategy_board.json"
>             )
>             (step_dir / "experience_card.json").write_text(
>                 json.dumps(card, indent=2),
>                 encoding="utf-8",
>             )
>             (output_dir / "experience_cards.jsonl").write_text(
>                 "\n".join(json.dumps(item) for item in experience_cards) + "\n",
>                 encoding="utf-8",
>             )
>             (output_dir / "strategy_board.json").write_text(
>                 json.dumps(board, indent=2),
>                 encoding="utf-8",
>             )
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

#### OBJ-14 — Retained rich experiment summaries

`method_overview` and `parent_comparison_experience`. Natural-language payload inside JSON/metadata wrappers; derived from current and parent code, plans, execution output, score/delta/status, and task description. Evo stores per-node cache files and attaches the payload to cards. RL optionally generates equivalent summaries after archive insertion. These are advisory knowledge to later generation; their schema is not evidence that the proposed causal explanation is true. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py:53-128`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:867-968`; `OpenMLE-ERL/RL/generate_mle.py:911-958`. Implementation conclusion status: wired.

>         "parent_comparison_experience": {
>             "type": "string",
>             "minLength": 1,
>             "description": "2-5 concise sentences comparing the current node against its parent and extracting reusable success or failure experience."
>         }
>     },
>     "required": ["method_overview", "parent_comparison_experience"],
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

>     def _store_rich_summary(self, node: Node, summary: dict[str, str]) -> None:
>         node.rich_summary = summary
>         card = getattr(node, "experience_card", None)
>         if isinstance(card, dict):
>             card["rich_summary"] = summary
>         cache_path = self._rich_memory_cache_path(node)
>         try:
>             cache_path.parent.mkdir(parents=True, exist_ok=True)
>             cache_path.write_text(
>                 json.dumps(
>                     {
>                         "node_id": node.id,
>                         "parent_node_ids": [parent.id for parent in list(node.parents or [])],
>                         "rich_summary": summary,
>                     },
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

#### Training and checkpoint detail for OBJ-5 and OBJ-6

Separate raw per-step execution/generation outputs, selected-step manifests, materialized `messages` examples, token/loss-mask batches and rewarded RL samples. A manifest's path to a trace is access metadata, not the trace payload. SFT collector examples can include reasoning, code and full response; selection reasons are separate metadata and are not automatically a training target. SRC-1: `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py:358-480`; `OpenMLE-ERL/SFT/scripts/sft_data_selection/select_evolutionary.py:283-361`; `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py:42-56`. Implementation conclusion status: wired for these producer/consumer pieces; end-to-end evolutionary materialization is limited under RTE-4.

Parametric memory may be active on accelerators or persisted in checkpoint files. Checkpoint containers can additionally hold optimizer and RNG state; those are symbolic training-control state, not readable explanations of learned behavior. SFT launchers deliberately omit optimizer/RNG saves. RL launchers expose separate checkpoint, optimizer/RNG, and database-continuation controls. SRC-1: `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh:148-170`; `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh:347-394`. Persistence implementation conclusion status: wired for SFT; external RL engine consumer conclusion status: afforded. No actual weight payload or retained model-behavior probe was inspected.

> CKPT_ARGS=(
>   --hf-checkpoint "${MODEL_PATH}"
>   --ref-load "${REF_LOAD_PATH}"
>   --save "${OUTPUT_DIR}"
>   --save-interval "${SAVE_INTERVAL}"
>   --no-save-optim
>   --no-save-rng
> )
> --- `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

### Routes

#### RTE-1 — Evo invocation and model proposal

Implementation conclusion status: wired. The operator launches `scripts/evaluate_airaevo.py` with Hydra config; it builds task-specific configs then invokes the vendored runner in subprocesses. The controller chooses Draft initially and later Improve, Crossover or fresh Draft from population state. GenericLLM renders task/data description, parent code, execution feedback, selected memory and remaining budget. The chosen model produces plan/code, extracted with bounded retries. Model output becomes an executable candidate; no human approval is interposed on each proposal. Principal: configuring operator; runtime identities: task, sample, node and parent IDs. Decision owner: symbolic scheduler for operator/parent choice, model for proposed content. Effects: model request and candidate files; candidate execution belongs to RTE-2. SRC-1 `OpenMLE-Evo/scripts/evaluate_airaevo.py:295-466`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1945-2002`.

> child_node = create_node_fn(*in_context_nodes)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Return is a candidate node; later read-back goes through RTE-3, not guaranteed activation by mere delivery. Delegated workers see task-scoped configs and selected parents; configuration/step/time limits control continuation. Invalid extraction retries; final extraction fallback can still yield unusable code, handled at execution. No expiry of static prompts is established. Guarantee strength: protocol, enforced only over configured controller calls; operator-selected alternate configs and endpoints remain material.

#### RTE-2 — Candidate execution and evaluation

Implementation conclusion status: wired. A candidate is sent to the configured task adapter/sandbox; execution produces submission, logs, exit state and score. For OpenMLE task packages, a scorer loads dataset-specific metric code and compares the submission with supplied answer CSV. Answer-oracle provider: task-package curator/builder; authority: executable metric over the supplied expected answers, not universal truth. The controller uses protocol-specific selection scores. Under `self_valid`, model-reported scores require explicit trust opt-in; default uses sandbox validation score or sandbox score. `legacy`, `method1` and `method2` use distinct score fields. SRC-1 `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py:168-245`; `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py:105-142`.

> score = metrics_calculator.evaluate(y_true=ground_truth_df, y_pred=submission_df)
> --- `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> trust_model_score = bool(
>     self.cfg["sandbox"].get(
>         "trust_model_validation_score",
>         False,
>     )
> )
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> selection_score = (
>     sandbox_valid_score
>     if sandbox_valid_score is not None
>     else sandbox_score
> )
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The immediate result is feedback/fitness; later consumers are archive ranking, diagnosis and training rewards. Execution feedback is visible to the model after prompt sanitization, but score sanitization does not hide files from executed code. Candidate effects are arbitrary submitted Python within the selected executor's granted filesystem/network/device envelope. The published worker launcher mounts the shared task tree read-only with writable scratch/cache subtrees. Read-only is not unreadable; private answers under that tree are not isolated from candidate code by that mount. This is a deployment-contract limit, not evidence of actual benchmark cheating. SRC-1 `OpenMLE-Gym/openmle-sandbox/node_workers/sandbox_builder/start_sandboxes.sh:145-191`; SRC-2 `OpenMLE-Gym/openmle-sandbox/README.md:105-119`.

> -v "$NFS_MOUNT:$CONTAINER_WORKSPACE:ro" \
> --- `OpenMLE-Gym/openmle-sandbox/node_workers/sandbox_builder/start_sandboxes.sh` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Guarantee strength: protocol for score selection; configured deployment guarantee for isolation, not established across all adapters. The evaluator owns the score; operators can choose evaluator and trust override. Remote failures/timeouts yield feedback and buggy candidates; model and sandbox concurrency controls do not establish exactly-once external effects. NatureBench uses its external evaluator contract; no claim that this worker mount describes that separate deployment.

#### RTE-3 — Program archive admission and parent read-back

The task controller automatically selects eligible prior programs and an operator, then supplies selected code/feedback and lineage context to the next generation model. The generator does not request this history, making delivery push. Selection uses task/operator eligibility, metric/rank/novelty and parent identities. Evo's experience selector uses the node metric and keeps its separately read official-score field diagnostic. The source comment calls that metric self-validation, but the selector does not establish its upstream provenance. In the `self_valid` validation phase, `base_task.py` defaults `trust_model_validation_score` to false and chooses `sandbox_valid_score`, falling back to `sandbox_score`; the true opt-in instead chooses `model_final_validation_score`. Thus the selector guard does not independently guarantee exclusion of held-out feedback: that depends on normalization, configuration, and the sandbox score's meaning. RL's adapted selector defines its score from training reward metadata, a separate route. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py:1152-1249`; `OpenMLE-ERL/RL/airaevo_experience.py:54-70`; `OpenMLE-ERL/RL/program_database.py:1393-1495`. Implementation conclusion status: wired.

>     metric_scores = [_metric_value(node) for node in nodes]
>     # Parent selection must follow the same self-validation metric used by the
>     # journal and final node selection.  The sandbox/raw score is kept in the
>     # trace for diagnostics only; using it here would leak test feedback into
>     # the search controller.
>     official_scores = [
>         _official_score_value(node) if _has_official_score(node) else None
>         for node in nodes
>     ]
>     selection_scores = metric_scores
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The upstream normalization evidence is retained once on RTE-2; the same limit applies here.

> def program_selection_score(program: Any) -> float | None:
>     """Return the test-reward fitness signal used by RL AIRA-Evo selection."""
>     metadata = _metadata(program)
>     for key in (
>         "metric_static_base_reward",
>         "static_base_reward",
>         "base_reward",
>         "dynamic_base_reward",
>         "reward",
> --- `OpenMLE-ERL/RL/airaevo_experience.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

RL stores successful execution responses and selected invalid-code categories; connection/runtime failures and empty code are excluded by the admission expression. Retained invalid examples are not thereby trusted parents: success/debug eligibility and operator fallback remain separate. Evaluation calls explicitly choose the raw Draft prompt and bypass archived parent context. Thus a reported evaluation score need not test archive recall.

>     # Store successful executions plus explicitly categorized invalid code we want to keep for analysis.
>     # Connection/runtime failures and empty code are still skipped.
>     should_store_program = status_code == 200 or code_category in {"hack", "no_verify", "hack_verify"}
>     if should_store_program:
>         program_id = db.add(program)
> --- `OpenMLE-ERL/RL/generate_mle.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

>         if evaluation:
>             self.last_selection_metadata = {"airaevo_policy": self.policy, "airaevo_operator": "draft", "airaevo_generation_id": generation_id}
>             return (public_system_prompt, public_user_prompt), None, "draft", None
> 
>         programs = self._all_programs(database, task_key)
>         active = self._active_success_programs(programs)
> --- `OpenMLE-ERL/RL/program_database.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Admission/revision audit: candidate and execution producers append immutable attempt records; successful/eligible programs can enter ranked populations while invalid attempts can remain diagnostic history. The selection policy, not a human reviewer, admits parents. Existing code and feedback guide the next proposal. Program versions persist across rounds; task checkpoints and configured archive continuation support later same-task consumers. Pruning/cooling can remove or downweight material; no universal expiry or semantic withdrawal mechanism is inferred. Immediate return is an admitted record/selected context. Delegate visibility is the task-local journal or configured database, not cross-task conversational memory. Crash recovery is bounded by committed checkpoints, and delivered context has no observed activation evidence. Guarantee strength: policy over covered selection branches; upstream score provenance and external evaluator contract still govern what rank means.


#### RTE-4 — SFT selection and training

Offline producer path: collect successful evaluated parallel responses with prompt provenance, select per-task candidates, deduplicate complete messages, token-filter, optionally exclude reserved task descriptions, and supply `messages` to the vendored trainer. The collector reads source prompt tables plus retained generation/evaluation artifacts and builds assistant content from reasoning/code/response. The loss-mask generator turns messages into token targets; the launcher selects SFT loss; training invokes actor updates and saves parameters. SRC-1: `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py:383-480`; `OpenMLE-ERL/SFT/scripts/sft_data_selection/finalize_messages.py:81-102`; `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py:42-56`; `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh:157-170`; `OpenMLE-ERL/SFT/slime/train_async.py:36-78`. Implementation conclusion status: wired for materialized-message training and parallel collection, with operator-selected file boundaries.

>         reasoning = read_text(step_dir / "reasoning.md")
>         code = read_text(step_dir / "valid_code.py")
>         response = read_text(step_dir / "response.md")
>         assistant = build_assistant_content(reasoning, code, response)
> 
>         rows.append(
>             {
>                 "id": f"{id_prefix}-{len(rows)}",
>                 "messages": [
>                     {"role": "system", "content": system_prompt},
>                     {"role": "user", "content": stored_user},
>                     {"role": "assistant", "content": assistant},
>                 ],
> --- `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

>     samples = data_buffer.get_samples(args.rollout_batch_size)
> 
>     for i, sample in enumerate(samples):
>         (sample,) = sample
>         messages = sample.prompt
>         tools = sample.metadata.get("tools", None)
> 
>         token_ids, loss_mask = MASK_GENERATOR.get_loss_mask(messages, tools=tools)
> 
>         response_length = MASK_GENERATOR.get_response_lengths([loss_mask])[0]
> 
>         sample.tokens = token_ids
>         sample.response_length = response_length
>         sample.reward = 0
>         sample.loss_mask = loss_mask[-response_length:]
> --- `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The evolutionary branch first identifies successful medal-reaching segments and selects steps by supplied causal-inheritance annotation for multi-step segments. The selector reads `keep_indices` or `keep_for_sft`; its output contains step identity, path, segment metadata and selection source. It neither generates the annotations nor exports `messages`. Scoped search of ERL for `selected_steps`, `keep_indices`, and `causal_inheritance_annotation`, and inspection of the separate `data_produce` collector, found no direct consumer materializing that selected evolutionary manifest into training messages. The collector explicitly expects Pass@k generation/evaluation files. Therefore the release affords this workflow but the claim of an automatically closed evolutionary trace-to-SFT chain is unsupported within the inspected boundary. SRC-1: `OpenMLE-ERL/SFT/scripts/sft_data_selection/select_evolutionary.py:283-361,387-407`; SRC-2: `OpenMLE-ERL/SFT/docs/usage.md:197-240`.

>             selected.append(
>                 {
>                     "id": f"aira::{segment['task_name']}::step_{step_index}",
>                     "task_name": segment["task_name"],
>                     "step_index": step_index,
>                     "step_dir": relative_step_dir,
>                     "segment_id": segment["segment_id"],
>                     "segment_type": segment["segment_type"],
>                     "segment_length": segment["segment_length"],
>                     "selection_source": source,
>                 }
> --- `OpenMLE-ERL/SFT/scripts/sft_data_selection/select_evolutionary.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Causal-inheritance annotations request a `usefulness_reason`, but the parser reduces them to indices. That reason is not passed through this selector to training. Kept generation reasoning may remain in assistant text; parameter learning does not retain an addressable guarantee that a particular justification controls future behavior.

> For each step, return:
> 
> {
>   "step_index": 0,
>   "operator": "Draft | Improve | Crossover | Debug",
>   "keep_for_sft": true,
>   "usefulness_reason": "A concise English explanation of the causal contribution."
> }
> --- `OpenMLE-ERL/SFT/scripts/sft_data_selection/causal_inheritance_prompt.txt` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

>         indices = parse_index_list(row.get("keep_indices"))
>         if not indices and isinstance(row.get("steps"), list):
>             indices = [
>                 int(step["step_index"])
>                 for step in row["steps"]
>                 if isinstance(step, dict)
>                 and step.get("keep_for_sft") is True
>                 and isinstance(step.get("step_index"), int)
>             ]
>         if isinstance(segment_id, str):
>             result[segment_id] = indices
> --- `OpenMLE-ERL/SFT/scripts/sft_data_selection/select_evolutionary.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Message deduplication is an actual operation over retained training examples:

>     for index, row in enumerate(rows):
>         if "messages" not in row:
>             raise ValueError(f"row {index} has no messages field")
>         digest = message_hash(row["messages"])
>         if digest in seen:
>             dropped.append(
>                 {
>                     "row_index": index,
>                     "id": row.get("id"),
>                     "first_row_index": seen[digest],
>                     "message_hash": digest,
>                     "drop_reason": "duplicate_normalized_messages",
> --- `OpenMLE-ERL/SFT/scripts/sft_data_selection/finalize_messages.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The retained SFT implementation makes actual actor-training calls:

> ray.get(actor_model.async_train(rollout_id, rollout_data_curr_ref))
> --- `OpenMLE-ERL/SFT/slime/train_async.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Admission/revision audit: operator-selected sources and paths trigger collection/selection; success criteria, annotation-selected indices, complete-message hashes and token limits reject examples before training. Dataset guidance includes task prompts and generated reasoning/code, but gradient fitting is not criticism of stated theory content. Changed parameters persist in model checkpoints for later generation. Immediate return is selected files/checkpoints; named trainers pull batches and model loaders pull checkpoints. Withdrawals/rollback beyond operator-selected previous files/checkpoints are uninspected; no automatic validation-based deployment gate is established. Training adjusts parameters; it does not preserve addressable theory content in those parameters. Theory-builder conditions 1–4 for weight adaptation alone are inapplicable to its non-localized representation; criticism on generated program routes remains separately assessed at RTE-7. Learning through criticism is uninspected. Execution benefits are claimed only at CLM-2's coarser comparison grain.


#### RTE-5 — Online RL rollouts and updates

Shipped generation code returns rewarded sample groups and writes program records; the fully asynchronous adapter supplies complete groups to the separately installed SLIME trainer. The launcher selects the task prompt table, custom rollout function, response cap and checkpoint destinations. Parameter update/synchronization inside that external engine is an afforded consumer route here, with repository prose claiming an executed smoke. SRC-1: `OpenMLE-ERL/RL/fully_async_rollout.py:346-363`; `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh:362-394`; `OpenMLE-ERL/RL/train_async_with_patch.py:73-90`; SRC-3: `OpenMLE-ERL/RL/docs/usage.md:169-185`. Consumer conclusion status: afforded. Reported-operation conclusion status: claimed.

>     completed_samples = run(generate_rollout_async(args, rollout_id, data_buffer))
>     return completed_samples
> --- `OpenMLE-ERL/RL/fully_async_rollout.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The reported smoke used a 128-token response cap and two optimizer steps, and excludes checkpoint save/reload and exact paper reproduction. It cannot establish memory faithfulness or generalized learning quality. Reward changes model parameters across tasks; no retained, separately addressable reason is required by this update interface.

Admission/revision audit: task prompts trigger generated operator candidates; execution-derived rewards and admitted program history feed samples. The external training engine decides parameter changes under configured objective; humans configure resources/checkpoints/stages, not every gradient update. The supplied expected outcomes are evaluator labels/metrics, distinct from model opinions. Reward gates and database admission can reject usable training material, but no inspected gate certifies a new model before deployment. Immediate return is completed sample groups; later consumer is the named external trainer and its rollout generator, afforded at this interface. Checkpoint continuation is RTE-11. Profile-dependent summary generation is RTE-10. Parameter persistence spans tasks via a shared learner; actual effects and safe recovery in the external engine remain uninspected. Theory-builder conditions 1–4 are not inferred from parameter updates; any task-level criticism is confined to the explicit candidate routes. Guarantee strength: interface contract, requiring the pinned external SLIME engine and configured evaluator. Learning attributable to theory criticism remains uninspected.


#### RTE-6 — Gym task construction

Implementation conclusion status: wired. A user-supplied task/slugs batch enters a graph: download, copy, scrape, perceive/tools, describe, prepare/retry, metric, next/end. Available data-inspection tools are explicitly listed. Generator calls propose task descriptions, preparation and metric code; compilation rejects malformed code, preparation execution can fail and feed the last attempts into the next generation. The builder persists task-package files. The graph routes failures to termination or bounded preparation retry; it does not supply an independently authored answer oracle for the semantic correctness of generated metric code. SRC-1 `OpenMLE-Gym/builder_core/design.py:26-147`; `OpenMLE-Gym/builder_core/utils/nodes.py:884-1060`.

> response = self.llm_provider.query(
>     [query[0]] + self.todo["prepares"][-2:] + [query[1]]
> )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> compile(metric_code, str(metric_file), "exec")
> atomic_write_text(metric_file, metric_code)
> --- `OpenMLE-Gym/builder_core/utils/nodes.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Proposal guidance is static sample code and task description; feedback criticizes execution of the preparation proposal. Localized code and consumption are wired; explicit content-directed interpretation of failures is afforded by the model call, not established for all generated tasks. Iteration of changed code plus error feedback is wired within bounded retries. Addressability is script-level with editable functions; persistence of the package extends beyond construction, while this retry route establishes only within-run revision. Learning from criticism is uninspected. Historical rationale is not required by successful compilation. Rollback is retry/failed-task disposition, not a transaction over arbitrary code effects. Default `process` execution uses a disposable process; optional `isolated` mode requires Docker/Podman and an image, mounts selected paths and disables network. This local Gym isolation is distinct from distributed worker deployment. SRC-1 `OpenMLE-Gym/openmle_gym/process_runner.py:72-160`. Return: package/build results; later consumption is independently launched checking/training/search. Automatic promotion to a training corpus is not established here.

#### RTE-7 — Diagnosis, Debug and Improve revision

Implementation conclusion status: wired. Execution errors and previous candidates prompt Debug; valid parents can prompt Improve. These calls explicitly request reasons directed at the previous program: diagnose its failure or explain what worked and did not, then revise. This supplies a content-directed criticism route beyond numeric selection. It is a model-mediated protocol, not an invariant that every output formulates an adequate criticism. Under experience mode, deterministic metric/error feedback normally populates node analysis; the separate analyzer is a fallback. Its successful-run description need not propose improvements. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/debug_experience.yaml:39-55`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml:39-58`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1830-1895`.

> Based on the previous attempt, its score, and execution output, please identify the root cause of the failure and fix the code so it runs successfully and follows the output requirements. After it runs, improve the solution if possible.
> Preserve the current core idea unless the feedback shows that it cannot be made valid.
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/debug_experience.yaml` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> Based on the previous attempt, its score, and execution output, please analyze what worked well and what didn't, then improve the solution.
> Propose exactly one improvement idea that is different from the previously explored improvement ideas.
> Keep the evaluation method consistent across iterations.
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> node.analysis = response["summary"]
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Guidance: task requirements, proposed algorithm/code, failed execution and related retained attempts. Proposed change: replacement candidate program and optional plan. Model proposes and assigns explanatory blame; executor tests; controller may reject as buggy or fail population admission. A failure can reflect code, resource exhaustion, dependency or input contract; the route does not prove the model assigned blame correctly. Old journal nodes remain available; recovery stops at debug depth/time and can request a fresh Draft after repeated failure classes. Immediate return is a revised candidate; next debugging round tests it and retains its outcome. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1227-1310,1991-2023`.

> current_debug_node = fixed_node_attempt  # Update the node for the next iteration
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

**Theory-builder conditions 1–4:** (1) localized content — wired for candidate code as a formal proposed solution, and optional plan as explicit natural-language proposal; (2) consumption — wired, since execution follows code and revision prompts include it; (3) content-directed criticism — wired as an explicit diagnostic/revision procedure over previous code and outcome, with actual adequacy and realized criticism uninspected; numeric fitness alone does not establish this; (4) iteration — wired, revised code and feedback are consumed by subsequent tests/revisions, with persistence across rounds and checkpoint resume on the same task through RTE-3. Thus the implementation supports a bounded program-theory-builder route; no observed candidate instance establishes how reliably it meets the requested criticism protocol. Rationale: optional plans/diagnoses and derived memory can retain it, but no invariant requires historical rationale. Addressability: code functions and plan parts can be inspected and replaced, while archive identity/admission is chiefly whole-program. **Learning:** uninspected for improved future capacity attributable specifically to this criticism; CLM-2 reports coarser model/harness comparisons.

#### RTE-8 — Final selection, evaluation and return

Implementation conclusion status: wired. At search termination the runner selects the best available node, writes `valid_code_final.py` and `submit_code.py`, optionally reruns final test evaluation, and persists result/feedback files. `StopSearch` saves checkpoints and still attempts best-available selection. Test reruns are configurable; NatureBench may use recorded search-stage aggregate improvement when final submission is disabled. SRC-1 `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py:1670-1760`.

> best_code = best_node.code if best_node is not None else ""
> (output_dir / "valid_code_final.py").write_text(best_code, encoding="utf-8")
> submit_code = task.build_submit_code(best_code)
> (output_dir / "submit_code.py").write_text(submit_code, encoding="utf-8")
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Admission authority: metric and validity ranking within the configured task; final code is a selected product, not a proved algorithm. Caller receives files/statistics. Later reuse outside the archive/training interfaces is uninspected; delegated visibility is output-directory access, not guaranteed shared knowledge. Expiry is operator-managed. The route freezes the task product; deploying it elsewhere does not extend this builder episode. Guarantee strength: protocol, conditional on external evaluator and budget/termination behavior.

#### RTE-9 — Gym metric and quality checks

Implementation conclusion status: wired. Explicit metric-check loads generated metric class, validates sample-submission format where supported, evaluates against private answer and requires a finite numeric score. The separate quality evaluator inspects task structure, applies deterministic failure gates, or calls an LLM for dimension scores/reasons. It computes recommendation thresholds itself; skipped LLM evaluation remains explicitly skipped. SRC-1 `OpenMLE-Gym/openmle_gym/metric_validation.py:42-92`; `OpenMLE-Gym/openmle_gym/local_evaluator.py:553-572,727-742,887-932`.

> or not math.isfinite(float(score))
> --- `OpenMLE-Gym/openmle_gym/metric_validation.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> elif validation["status"] == "failed":
>     result["quality_scores"] = _hard_gate_quality(validation)
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> if overall >= 4:
>     recommendation = "recommended"
> elif overall >= 2.5:
>     recommendation = "conditional"
> else:
>     recommendation = "not_recommended"
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The numeric check warrants callable, finite scoring on that sample; it does not independently establish metric semantics, leakage freedom or adequacy of target labels. The quality recommendation grants a report-level disposition for task suitability. Automatic downstream corpus admission from it is uninspected, so it is not counted as lifecycle integration. The operator can choose task artifacts, metric and whether to run model assessment; the deterministic failure branch can veto a positive report in that call. Return: persisted quality result/errors; no observed quality improvement or revision is inferred. Guarantee strength: codified check over covered entry path; calls that bypass quality evaluation remain outside it.

#### RTE-10 — Trace extraction, retained summaries and targeted context

Trigger: completed execution creates a card; an impending Evo operator call selects related nodes and lazily ensures rich summaries exist. Producer: deterministic feature extraction plus summary LLM. Persistence: node/card attachment and cache files; the RL alternative merges metadata into SQLite after completion when enabled. Consumer: Improve, Crossover or Debug generator. Evo selects ancestry/sibling identities; Debug prioritizes inferred error-signature matches then recency. Delivery is automatic prompt supply. Failure: malformed/missing summary fields or generation exceptions leave the existing path usable without a new summary. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:905-1021`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py:704-855`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py:64-85,115-124`. Implementation conclusion status: wired.

>     if normalized_operator == "debug":
>         focus_node = current_node or (parent_nodes[0] if parent_nodes else None)
>         sections["primary"] = [focus_node] if focus_node is not None else []
>         signature = _current_error_signature(focus_node)
>         related = []
>         recent = []
>         for candidate in reversed(_journal_nodes(journal)):
>             if focus_node is not None and _node_id(candidate) == _node_id(focus_node):
>                 continue
>             card = _card_for_node(candidate, cards)
>             if signature and str(card.get("error_signature") or "") == signature:
>                 related.append(candidate)
>             else:
>                 recent.append(candidate)
>         cap = max(1, int(max_related_cards or 8))
>         sections["debug_related"] = _dedupe_nodes(related + recent)[:cap]
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> def _rich_summary_lines(prefix: str, card: dict[str, Any]) -> list[str]:
>     rich_summary = card.get("rich_summary")
>     if isinstance(rich_summary, dict):
>         method_overview = _compact_text(rich_summary.get("method_overview"), max_chars=420)
>         parent_experience = _compact_text(
>             rich_summary.get("parent_comparison_experience"),
>             max_chars=420,
>         )
>         lines = []
>         if method_overview:
>             lines.append(f"- {prefix}_method_overview: {method_overview}")
>         if parent_experience:
>             lines.append(f"- {prefix}_parent_comparison_experience: {parent_experience}")
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

>     if memory:
>         improve_data["memory"] = memory
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Error signatures are inferred from lexical patterns in status and execution text, rather than embeddings or model judgments. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py:305-331`.

>     combined = " ".join([str(status or ""), str(raw_run_log or ""), str(clear_run_log or "")]).lower()
>     if "timeout" in combined or "timed out" in combined:
>         return "timeout"
>     if "submission.csv" in combined and any(token in combined for token in ["missing", "not found", "no such file"]):
>         return "submission_missing"
>     if any(token in combined for token in ["modulenotfounderror", "importerror", "no module named"]):
>         return "import_error"
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The retained rationale is explicitly read: the renderer emits `parent_comparison_experience`. This establishes reason-bearing delivery, not its use by the model or the truth of the explanation. Node/cache identity and parent IDs preserve provenance; no inspected semantic validator independently checks the summary against execution. The optional RL summary feature is enabled in three supplied templates, but the asynchronous single-node launcher supplies a default of zero when its configuration omits the flag. SRC-1: `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh:562`; SRC-2: `OpenMLE-ERL/RL/configs/sync_single_node.env.example:103`, `OpenMLE-ERL/RL/configs/sync_multi_node.env.example:99`, `OpenMLE-ERL/RL/configs/async_multi_node.env.example:97`.

Revision admission: completed traces supply features; selected nodes trigger LLM summaries. Proposed new comparative explanations are admitted by parseability/nonempty-field normalization, attached to node/card/cache and reused; exceptions fall back without a new summary. The model proposes the explanation, code admits its shape, and no semantic reviewer veto is established. Cached content can persist across rounds/resume; freshness follows cache/node identity, not evidence of ongoing truth. Summaries retain rationale, and the renderer demonstrably reads that rationale. Their explanation is an ampliative conjecture, not a validated causal lesson. Theory-builder conditions 1–4 on the summary itself: localized content wired; contextual consumption wired at delivery, behavioral activation uninspected; criticism of summary content uninspected; criticism-driven summary revision/iteration uninspected. This is separate from program revision on RTE-7. Learning through criticism of summaries is uninspected. Guarantee strength: best effort summarization and policy-based selection; no observed benefit.


#### RTE-11 — Checkpoint and archive continuation

Named later consumers: the configured training model loader, serving/rollout models, and resumed search controller. Operator-selected checkpoint paths request prior learned parameters; Evo requests its journal checkpoint, and RL can copy a prior database into a new run. SFT code explicitly calls `actor_model.update_weights()` after initialization and at update intervals, and saves checkpoints periodically. RL documents SFT-to-RL and weight-only continuation, with independent optimizer/RNG choices. These are pull by named loader/controller roles, not merely hypothetical storage APIs. SRC-1: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:795-809`; `OpenMLE-ERL/SFT/slime/train_async.py:24-28,55-78`; `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh:347-379`; SRC-2: `OpenMLE-ERL/RL/docs/usage.md:155`. Implementation conclusion status: wired for Evo/SFT; external RL loader conclusion status: afforded.

>     # create the actor and critic models
>     actor_model, critic_model = create_training_models(args, pgs, rollout_manager)
> 
>     # always update weight first so that sglang has the loaded weights from training.
>     actor_model.update_weights()
> --- `OpenMLE-ERL/SFT/slime/train_async.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> if [ -n "${RESUME_MODEL_PATH}" ]; then
>    CKPT_ARGS+=(--load "${RESUME_MODEL_PATH}" --ckpt-step "${RESUME_CKPT_STEP}")
> fi
> if [ "${LOAD_OPTIMIZER}" = "0" ]; then
>    CKPT_ARGS+=(--no-load-optim)
> fi
> if [ "${LOAD_RNG}" = "0" ]; then
>    CKPT_ARGS+=(--no-load-rng)
> --- `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Return/visibility audit: loaders restore weights or task archive state for the next generation/training/search consumer; persistence is explicit beyond the producing call. Selection is requested path/checkpoint identity. No additional automatic context push is inferred from satisfying that request. Recovery depends on usable checkpoint and compatible configuration; unsupported freshness/corruption guarantees remain uninspected. This route restores admitted state rather than proposing new semantic revisions. Operator choice can return to an earlier snapshot; no automatic evidence-based rollback of model capability is established.


### Claims

#### CLM-1 — Search, experience and training form an improvement loop

Conclusion status: claimed. SRC-2 `README.md:36-52,101-127` positions OpenRSI as an executable engineering program, beginning with meta-evolution in MLE rather than claiming solved general recursive self-improvement.

> Search produces experience, experience enters training, and trained models return to search and evaluation.
> --- `README.md` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

The canonical routes and integrated memory records support concrete stage interfaces. End-to-end unattended scheduling and exact published-weight provenance remain uninspected. The source states the orchestration limit directly:

> OpenRSI contains several independently runnable stages rather than one synthetic top-level command.
> --- `README.md` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

#### CLM-2 — Reported post-training and harness gains

Conclusion status: claimed, evidence layer reported operation. SRC-3 `docs/results.md:15-39,86-96` reports MLE-Bench Lite Medal Average 39.39% → 60.61% for base versus Frontis-MA1-35B with Evo fixed; Evo-Max reaches 71.21% with priors plus asynchronous search. NatureBench Lite's ten-task table reports Match-SOTA 50% → 70% with adapter fixed, and 20% → 50% with base model fixed. These are strongest as model-plus-harness comparisons at the stated task budget. They do not isolate memory, formulated criticism, or any single operator, and no underlying executions/interventions were examined here.

> These are **model–harness results**, not standalone one-shot model scores. The OpenMLE-Evo-Max rows are end-to-end system results and must not be presented as pure model gains.
> --- `docs/results.md` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

### Evidenced absences

#### ABS-1 — No retained recall-dependence test within the inspected release boundary

Within the inspected memory-route source tests and release operation descriptions, no retained execution result intervenes on recalled content and measures the resulting consumer behavior. Test source can assert construction and selection semantics; repository training smoke prose asserts completion. Neither supplies the observed dependence required for `faithfulness_tested: yes`. This is an evidence-bound negative, not a claim that no private experiments exist. SRC-1: `OpenMLE-Evo/third_party/aira-evo/tests/test_experience_memory.py:344-515`; SRC-3: `OpenMLE-ERL/RL/docs/usage.md:169-185`. Conclusion status: absent.

The exact scoped search was `git --no-replace-objects -C related-systems/FrontisAI--OpenRSI grep -n -i -E 'faithful|recall|ablation|interven|memory|validation|smoke' 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa -- OpenMLE-Evo/third_party/aira-evo/tests/test_experience_memory.py OpenMLE-ERL/RL/docs/usage.md OpenMLE-ERL/RL/README.md OpenMLE-ERL/SFT/docs/usage.md`. It returned construction/selection test assertions and training-validation/smoke descriptions, with no qualifying recall-intervention execution result. The full-commit source reads covered `OpenMLE-Evo/third_party/aira-evo/tests/test_experience_memory.py:344-515`, `OpenMLE-ERL/RL/docs/usage.md:1-189`, `OpenMLE-ERL/RL/README.md:1-48`, and `OpenMLE-ERL/SFT/docs/usage.md:1-317`. The test-function-name query `^def test_` was also inspected for the same memory-test file. This is a bounded finding over those sources, not an exhaustive search of every repository artifact or private experiment.

>     assert "Targeted Memory Context for IMPROVE" in memory
>     assert f"parent_node_id: {parent.id}" in memory
>     assert "score=0.78" in memory
>     assert "delta_vs_parent=0.04" in memory
>     assert "runtime_seconds=12" in memory
>     assert "LightGBM with target encoding and 5-fold validation." in memory
> --- `OpenMLE-Evo/third_party/aira-evo/tests/test_experience_memory.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

These assertions concern rendered strings; they are not an execution result establishing model reliance.

Other uninspected deployment, criticism and dependency findings are limitations, not absence claims.

### Behavioral-authority paths

| ID | Consumer | Channel | Force | Horizon / evidence |
| --- | --- | --- | --- | --- |
| BAP-1 | Evo generation model | Rendered operator prompt: task, parent, feedback and selected memory | Instruction/advisory knowledge | Current candidate and later task rounds; RTE-1, RTE-3, RTE-7; SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py:90-124`. Delivery wired, activation uninspected. |
| BAP-2 | Search controller | Validity/fitness fields and island policy | Enforcing buggy exclusion, ranking/selection | Population admission and final task product; RTE-2, RTE-3, RTE-8. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1830-1895,1945-2062`. |
| BAP-3 | SFT/RL learner and generation service | Samples/rewards/checkpoint interfaces | Learning/update and later generated behavior | Training stage and later model use; RTE-4, RTE-5. Actual trained bytes and benefit uninspected beyond reported claims. |
| BAP-4 | Gym graph and quality report consumer | Generated scripts, exception feedback, metric and quality result | Execution/retry control, validation and advisory recommendation | Task construction/checking; RTE-6, RTE-9. SRC-1 `OpenMLE-Gym/builder_core/utils/nodes.py:884-1060`; `OpenMLE-Gym/openmle_gym/local_evaluator.py:887-932`. |

## Runtime account

An ordinary MLE-Bench invocation begins with an operator-configured task list and model endpoint. The launcher resolves prompts/guidance and emits task and runner configuration. A runner starts per-task/sample subprocesses; each solver owns a journal and population. It drafts code, submits it to the selected executor, parses objective fitness or failure, records the attempt, and either repairs it or considers it for the population. Later rounds select a parent or pair, construct context from code/feedback/retained experience, and invoke Improve or Crossover. Time, step and generation bounds stop search. The runner saves the best available code, optional final test reruns and statistics. This progression is wired by RTE-1, RTE-2, RTE-3, RTE-7 and RTE-8, not observed in this analysis.

Decision roles are split explicitly. The operator chooses tasks, model, executable evaluator, launch profiles and budgets, and launches SFT/RL stages. Computation chooses operators/parents, proposes candidate content, executes tests, ranks/rejects and checkpoints within a search run. The model supplies diagnostic blame; deterministic error/validity checks and fitness can overrule candidate continuation. No inspected approval gate asks a human to accept each program. Replacing production checkpoints or redesigning the task/evaluator/search procedure remains a configured stage/operator responsibility; automatic source-level method revision is not established. Operating modes are bounded search experiments/curricula and separately launched training, not an open-ended user-request assistant. Answer-oracle use is limited to configured reference labels/benchmark evaluator in RTE-2 and RTE-9; a model quality judgment is not an expected-answer oracle.

Material alternate paths: standard synchronous generations versus asynchronous steady-state workers; MLE-Bench sandbox versus NatureBench Docker/SCM/local adapter; model-analysis fallback versus deterministic execution metadata; default sandbox-derived versus explicit trusted model score; local Gym process versus optional isolated execution; separate SFT, synchronous RL and asynchronous RL launch profiles. The main runtime is not a generic arbitrary tool-calling assistant: generated program execution supplies its broad capability surface. Gym's perception loop does have a bounded declared tool list. Current deployed grants, keys, images and accessible data are uninspected; task paths and model/tool capability are not themselves evidence of deployed isolation.

Asynchronous workers share sample/commit locks. Completed node admission and checkpoints occur inside a commit lock; finalization cancels workers and saves a checkpoint. This provides local coordination, not proof of exactly-once remote code effects or cluster fault tolerance. SRC-1 `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py:1476-1510,1685-1745`.

> async with commit_lock:
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

> await asyncio.gather(*workers, return_exceptions=True)
> self.save_checkpoint()
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` @ `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`

Static forcing cases:

| Case | Inspected branch | Consequence and limit |
| --- | --- | --- |
| Model prints an attractive validation score | RTE-2 trust switch and protocol branches | Default selection uses sandbox score; explicit opt-in changes authority. This does not prevent code from reading mounted private labels. |
| Candidate fails or lacks valid metric | RTE-7 debug loop and `node.is_buggy` | Invalid candidates receive worst fitness; bounded repairs consume code/feedback; repeated failure can request a fresh Draft. It does not prove the diagnosis is correct. |
| Several candidates finish while budget expires | Async commit/stop checks above | Serialized admission can reject late commits; workers are cancelled and checkpoint saved. Remote process cleanup depends on backend. |
| Task preparation or metric generation is wrong | RTE-6, RTE-9 | Syntax/execution/finite-score and quality checks have distinct rejection points. Metric validity on one sample is narrower than semantic correctness. |

Execution-preflight disposition: **no dynamic check planned**. Considered a real model/search smoke, RL optimizer run, and sandbox execution check. They require external model services/weights, datasets, evaluators, images and possibly GPU infrastructure; they would add operational evidence but are unnecessary to distinguish the inspected branches. No target test was attempted or reported as failing. Static source inspection and Commonplace artifact validation are not target execution probes.

## Lens scoping

### Memory/context scope

Full depth. Triggers: OBJ-3, OBJ-5, OBJ-6 and RTE-3, RTE-4, RTE-5; program reuse, derived summaries and trace-to-parameter pathways are central to CLM-1. The fresh specialist inspects the pinned released source, including material context alternatives; normalized scope and exclusions are recorded in `memory-comparison` and below. Static prompts alone do not qualify as accumulated memory. Endpoint weights and actual activation are uninspected.

### Epistemic scope

Full depth. Triggers: candidate programs/plans (OBJ-1, OBJ-7), execution/diagnosis (OBJ-2, OBJ-8), Gym task/evaluator construction (OBJ-9, OBJ-10, OBJ-11, OBJ-12), and training claim CLM-1. Assessed families: proposal, execution, criticism/revision, score admission, memory retention/derivation, task quality and parameter adaptation. External evaluator/optimizer internals and raw benchmark runs are unassessed, preventing a system-complete causal or correctness conclusion.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried experiment archives, lineage/selection metadata, cards, retained rich summaries, training examples and checkpoint reuse. Its comparison scope includes optional/legacy Evo and ERL memory branches at shipped interfaces. It excludes static task skills, Gym task/environment definitions and transient builder retry dialogue; the latter still appears in the runtime account. External corpus/weight contents and RL engine internals are explicit exclusions, not unknown payloads silently omitted from a known aggregate.

The decisive memory distinction is between raw attempts (OBJ-3), derived features (OBJ-13), reason-bearing rich summaries (OBJ-14), training samples (OBJ-5) and parameters (OBJ-6). The generator receives selected history without requesting it: RTE-3 and RTE-10 are push. Task/operator/fitness/recency filters are coarse; node/parent/ancestor/sibling matches are identifier signals; lexically inferred error signatures add inferred-lexical selection. The trainer and checkpoint controller make requested reads on RTE-4 and RTE-11, giving separate pull paths. Neither an identifier on a requested path nor an ordinary function return is counted as push.

Trace learning is wired through retained comparative summaries and materialized SFT training. RTE-10 transforms execution/tool traces and trajectories into online per-task symbolic cards and natural-language summaries; subsequent model calls receive them. RTE-4 converts completed multi-task trajectories into offline messages and parametric changes. RTE-5 adds cross-task online RL at an afforded external engine interface. The profile's dependent source/scope/timing/form unions cover all three and use afforded where the RL boundary weakens the union. This trace-learning classification does not establish theory criticism or measured improvement.

Curation includes deletion/downweighting of stored programs (decay), exact normalized-message deduplication, and model synthesis of comparative explanations. New candidates do not themselves establish evolving a standing memory entry. Summary rendering bounds fields/related-node counts, not all prompt tokens or total selection cost. Plans/analyses can preserve reasons; rich summaries explicitly deliver comparison reasons; evolutionary SFT annotation reasons are dropped by the index-only selector. No recall-dependence execution test was found within ABS-1's boundary. Delivery and training interfaces therefore remain distinct from observed activation and benefit.

The specialists' material uncertainty is retained: an evolutionary selected-step manifest is not a training message corpus, and the inspected source does not close that materialization boundary. SFT training for supplied/materialized messages is wired. RL internals are external, and the reported short training smoke does not establish summary activation or checkpoint save/reload. Optional rich summaries are profile-dependent.


### Epistemic lens

The invoked procedure is `analyse-external-system-epistemic-architecture.md`. The following six blocks are a sparse overlay; shared records retain identities, storage/forms and route progression.

#### Source-and-claim boundary

See SRC-1, SRC-2 and SRC-3 and the Epistemic scope. Question: which proposals become operationally selected solutions, and what evidence licenses stronger claims about knowledge or improvement? CLM-1 claims an improvement loop; CLM-2 claims performance gains. All assessed route implementations are distinct from reported benchmark operation; no observed candidate instances or causal experiments were inspected for these program/training routes.

#### Epistemic-object inventory

| Object | Epistemic annotation |
| --- | --- |
| OBJ-1, OBJ-7 | A program/plan proposes how to solve the task. Program behavior is formally localized; performance and explanatory adequacy are conjectural until tested. Code can be directly operational without a separately stated explanatory claim. |
| OBJ-2 | Acquired execution/measurement evidence; numeric derivation inherits only the task metric and input contract. Logs are not automatically truthful explanations. |
| OBJ-3 | Retention/access container; no additional truth-apt content follows from retention. |
| OBJ-4 | Authored operational guidance; shipping/delivery does not validate its claims. |
| OBJ-5 | Selected/reformatted training examples; suitability derives from their selection criterion, not a new truth certificate. |
| OBJ-6 | Parameter adaptation with no individuated truth-apt proposition established in this boundary. |
| OBJ-8 | Deterministic feedback can be acquired/reshaped; model diagnosis adds an ampliative causal claim. Its correctness is not established by a repaired program's score alone. |
| OBJ-9 | Imported facts plus generated task description: semantic preservation versus added conjecture is indeterminate without comparing each output to source data. |
| OBJ-10, OBJ-11 | Executable proposals for preparation and evaluation; their intended data/metric semantics require separate checking beyond compilation. |
| OBJ-12 | Ampliative task-quality judgment over evidence plus codified threshold disposition; report recommendation is narrower than external adoption. |

Derived-memory objects receive the same limit through the accepted memory records: compression can mix faithful reshaping with inferred explanation; source occurrence and later use do not validate truth.

#### Authority-route ledger

All rows below have architectural status **implemented** at the inspected interface, except where explicitly bounded. Observed candidate state is **no instance observed** for these assessed candidate routes; source code and reported tables do not establish an instance's traversal. Content/update relation and force are per function, not a system grade.

| Route / function | Content/update relation | Target, evaluator and timing | Epistemic license | Operational / behavioral authority |
| --- | --- | --- | --- | --- |
| RTE-1 — content transformation | Ampliative conjecture for proposed plan; executable candidate construction | Task proposal, model at each generation | Candidate only; no correctness acceptance | Produces executable OBJ-1; BAP-1. |
| RTE-2 — check/evidence production | Acquisition/import of execution output; metric derivation under configured semantics | Submission, runtime plus metric/reference labels after execution | Score for that input/split/metric; no mechanism or transfer warrant | Feedback and fitness enter BAP-2; source-native checker may fail. |
| RTE-3 — disposition/acceptance | No content change | Validity and population fitness policy after evaluation | Relative acceptance for continued task search, not truth of explanation | Candidate can become later parent; BAP-2. |
| RTE-3 — retention | No content change | Journal/database writes | Preserves lineage and results, not acceptance by itself | Later contextual availability; BAP-1. |
| RTE-3 — operational admission/selection/consumption | No content change | Parent/history selectors before model call | Context selection licenses no extra truth | Selected prior candidates and feedback supplied to later proposals; BAP-1. |
| RTE-7 — content transformation | Ampliative diagnosis/revision | Previous program and feedback, model during Debug/Improve | Stated criticism requested; explanation not independently accepted | Revised candidate and optional retained reason; BAP-1. |
| RTE-8 — disposition/acceptance | No content change | Best-available/validity selection for task product | Best under configured search selection; general optimality unestablished | Final product written; BAP-2. |
| RTE-8 — check/evidence production | Acquisition/metric derivation | Optional final test rerun against selected evaluator | Test result for that final execution | Statistics/reporting, not guaranteed deployment acceptance. |
| RTE-4 — content transformation | Non-ampliative selection/formatting where implemented; parameter update is non-truth-apt adaptation | Training examples and configured training objective | Selection preserves only source-level evidence; no proposition becomes true by gradient update | BAP-3 with branch and materialization limits below. |
| RTE-5 — behavior/policy adaptation | Non-truth-apt parameter update | Rollout rewards and external optimizer interface | Objective optimization, not criticism of what a parameter says | Future generator changes; BAP-3, dependency boundary applies. |
| RTE-6 — content transformation | Task description indeterminate; program conjecture for scripts | Data/specification, generator during construction | Proposed task/metric, not independent correctness | Files executed and checked; BAP-4. |
| RTE-9 — check/evidence production | Derivation/acquisition for structural checks; ampliative model quality judgment | Metric/sample and task structure before report | Finite result and bounded quality opinion, not scientific task fidelity | Hard gate can veto positive quality result; BAP-4. |
| RTE-9 — disposition/acceptance | No content change | Codified average thresholds over quality dimensions | Report recommendation for task suitability | No inspected automatic promotion to training; BAP-4. |

Every row's source/endpoint/progression is the named canonical route. No mismatch is inferred from intentionally operational selection; mismatch would arise only by presenting its score as validated explanation or universal improvement.

#### Per-object lifecycle disposition

For OBJ-1 and OBJ-7, RTE-1 proposes a task solution; RTE-2 tests executable consequences; RTE-7 can state a criticism and revise; RTE-3 accepts candidates for relative population fitness and supplies accepted parents to later rounds; RTE-8 selects the task product. Observation/anomaly, conjecture, consequence execution, testing and criterion-bound acceptance have architectural status implemented. Observed candidate state for each is no instance observed. Post-acceptance reuse of a selected parent is implemented operational integration into further search, with no instance observed; unaccepted journal retention is not lifecycle integration. Missing evidence: an actual candidate-linked plan, criticism, test and selection trace.

OBJ-8 model explanations are ampliative conjectures. Production and use are implemented on the fallback/model-summary branch; a separate check that accepts a root-cause explanation as true is not determinable within the inspected code. Observed candidate state: no instance observed throughout. A successful repair tests the revised program and need not confirm its explanation.

OBJ-2 is acquired output plus metric derivation; discovery lifecycle not applicable to the raw result. Warrant is conditional on test data/evaluator/execution integrity. OBJ-9 is indeterminate between faithful restatement and ampliative task specification; source lineage is preserved in builder inputs, but semantic comparison was not inspected. OBJ-10 and OBJ-11 are executable proposals with implemented construction and compilation/execution checks; observed candidate state no instance observed. Acceptance establishes bounded script/metric operability, not semantics. Subsequent scoring use of OBJ-11 need not follow semantic acceptance, so that use is not semantic lifecycle integration.

OBJ-12 quality judgments have implemented evidence collection, model conjecture, syntactic/range validation and codified recommendation. Observed candidate state: no instance observed. Acceptance scope is the report's threshold criterion for task suitability; downstream corpus integration is not determinable. An LLM quality score is not an oracle answer.

No lifecycle record for OBJ-3: no candidate truth-apt output for this container; relevant retention/read-back route RTE-3. No lifecycle record for OBJ-4: no generated truth-apt output in the inspected static-guidance route RTE-1. OBJ-5 selection/formatting is non-ampliative over source samples where established, with discovery lifecycle not applicable; opaque/materialization branches retain their limits. No lifecycle record for OBJ-6: no individuated candidate truth-apt output; relevant direct-adaptation routes RTE-4, RTE-5. For OBJ-13, feature extraction is non-ampliative where it copies status/lineage, and inferred family/error features retain heuristic limits; discovery lifecycle does not apply to raw metadata. For OBJ-14, comparative explanations are ampliative conjectures: RTE-10 production and retention/context use are implemented, observed candidate state no instance observed, independent semantic acceptance and post-acceptance lifecycle integration not determinable. Pre-acceptance prompt use is not lifecycle integration.

#### System-claim versus route comparison

CLM-1 has design support and implementation for search, retention, selection and training interfaces. This supports a concrete improvement plane; it does not establish autonomous orchestration of successive released models. CLM-2 has reported controlled comparisons at model/harness grain. No observed-run or causal evidence was independently inspected, so its improvements remain claimed; neither the mixed Evo-Max intervention nor the local single-run example isolates memory or criticism. An implemented feedback loop is not itself evidence of improved future capacity.

#### Bounded conclusion

OpenMLE creates and tests executable proposals, grants criterion-bound search authority to evaluated candidates, and uses prior attempts to generate replacements. The diagnostic prompts establish a route for criticism of program content; score ranking and gradient updates have separate roles. Generated task/evaluator code creates an additional warrant dependency: checking that a metric runs cannot make its target semantics true. Parametric post-training and reported transfer gains are meaningful parts of the system's contribution, but do not show that formulated criticism caused the reported gains.

## Reconciliation

The frozen memory input hash is `75de9f54b6259d99c213062ec549d32de727e3189d179ea6fd9f8bc9be1b1bbb`; report identity, complete status, method hash, source/reviewed boundary and final byte hash were checked. The report was independently source-read in a fresh worker. Its complete comparison mapping was retained after exact-token remapping:

| Specialist proposal | Canonical record | Disposition |
| --- | --- | --- |
| MEM-OBJ-1 | OBJ-13 | Register derived experience cards/board features; OBJ-3 keeps archive referent. |
| MEM-OBJ-2 | OBJ-14 | Register retained rich-summary language separately from access metadata. |
| MEM-RTE-1 | RTE-10 | Register extraction, persistence and selected contextual supply. |
| MEM-RTE-2 | RTE-11 | Register requested archive/checkpoint continuation. |
| MEM-ABS-1 | ABS-1 | Register bounded lack of retained recall-dependence evidence with exact search scope. |

Eight material integration issues are disposed. Archive heterogeneity is preserved on OBJ-3, OBJ-13 and OBJ-14. The evolutionary manifest-to-messages gap and externally supplied annotations qualify RTE-4; no fully closed branch is claimed. Discarded annotation rationale is distinct from retained/delivered comparative rationale on RTE-10. RL's external optimizer and claimed short smoke qualify RTE-5; vendored SFT code is not used as evidence of RL internals. Configurable rich summaries and the asynchronous single-node default remain explicit. Deterministic `node.analysis` is not automatically model criticism; RTE-7 separately reads diagnostic prompts. Scope exclusions are explicit and do not block a complete bounded report.

The coordinator challenged the original shorthand that Evo parent selection was necessarily self-validation-only. The specialist re-read upstream normalization and amended the same RTE-3 finding: selection uses the normalized node metric, whose provenance depends on protocol/trust configuration on RTE-2. The selector's avoidance of a separate raw score does not alone establish withheld-test secrecy. This supersedes the overly broad shorthand without changing the route's referent or comparison classification. The corrected quote is retained once on RTE-2.

The two passes independently found that execution feedback may be deterministic and that memory presence does not prove model reliance; the diagnostic-branch clarification was later exchanged, so it is not counted as independent convergence on the final wording. Parent owns epistemic judgment and IDs; specialist owns memory source analysis/profile. No unresolved substantive conflict remains.


## Bounded synthesis

OpenRSI's released contribution is an executable MLE improvement plane: OpenMLE constructs task packages, searches over model-generated programs, retains reusable attempt information, and provides training interfaces for improving the generator. The code-grounded result establishes connected local routes; repository documents report substantial post-training and harness-level gains. The unresolved question is which parts of that improvement are attributable to specific memory or criticism mechanisms, and how reliably the released stages reproduce the reported results under independently pinned external artifacts.

The system has two distinct improvement horizons. Within a search run, candidate code and selected experience change subsequent proposals while the model endpoint is fixed by configuration. Across training stages, filtered traces and rewarded rollouts can change model parameters, which later generation consumes. Those stages share Draft/Improve/Debug/Crossover semantics but remain independently launched. Treating the entire repository as one autonomous recursive agent would conceal this scheduling boundary.

For [theory-builder](../../../../notes/definitions/theory-builder.md) conditions 1–4, RTE-7 supports a wired bounded route: localized proposed programs, content-based execution and revision, explicit requested diagnosis, and next-round reuse of revisions. The request for criticism is model-mediated and not guaranteed by parser checks; actual criticism content and observed membership remain uninspected. Whole-program selection and optional plans give some addressability; journal/checkpoint reuse gives persistence across task rounds/resumption. Neither property establishes learning.

**Learning:** the strongest supported contribution is claimed improved MLE capacity in reported fixed-harness model comparisons and fixed-model harness comparisons (CLM-2). Improved capacity attributable specifically to holding and criticizing stated theories remains uninspected; no inspected intervention isolates that cause. The memory profile's trace-learning classification concerns its defined trace-fed artifact/parameter pathway and does not settle this stronger learning claim.

**Reflection:** wired in the limited sense that retained representations of the search's own attempts and outcomes can change later search behavior through RTE-3 and derived-memory routes. The representation concerns selected prior search behavior; it does not prove a method-text theory builder that criticizes and revises its own search rules. That reflective qualifier remains uninspected in this boundary. **Autonomy:** wired computational proposal, testing, diagnosis, candidate selection and revision inside a configured search run; whole-plane autonomous stage scheduling, evaluator redesign and production-model replacement remain uninspected. **Self-improvement:** wired feedback-responsive revision of task solutions and training interfaces; claimed improvements to generator/harness capability at CLM-2's comparison grain. Sustained recursively accelerating improvement is neither observed nor inferred.

This design is discriminating where executable performance supplies usable feedback and expensive candidate runs make selective reuse worthwhile. Its evidential limits are equally specific: changing task metric, data split, trust override, mounted private data or model endpoint changes what the score and comparison mean. Evidence that would alter the assessment includes pinned runnable external artifacts, complete candidate-linked criticism/admission traces, an intervention on derived memory or criticism with other settings fixed, and inspected automation for subsequent-stage model admission.

## Limitations

| limitation | affected records | inspected boundary | conclusion prevented | resolving evidence |
| --- | --- | --- | --- | --- |
| External weights, datasets, evaluator and deployment images | CMP-2, CMP-3, RTE-2, RTE-5, CLM-2 | Repo code/config and documents | Exact identity, benchmark reproduction, data disjointness and deployed isolation | Immutable artifacts and reproducible deployment/run records |
| Model outputs are unobserved for assessed candidate routes | OBJ-7, OBJ-8, RTE-7 | Prompts/parser/control wiring | Reliable realized criticism, correct blame and observed theory-builder operation | Candidate-linked outputs, feedback, revisions and next consumers |
| Benchmark effect attribution | SRC-3, CLM-2 | Reported tables and local example narrative | Independent causal claims, memory/critic/operator component effects | Matched run data and interventions at named component grain |
| Private-label separation depends on deployment | RTE-2 | Shipped shared mount and evaluator interface | Enforced answer secrecy or leakage-free assessment | Verified per-worker grants and evaluator separation |
| Generated task/evaluator semantics | OBJ-9, OBJ-10, OBJ-11, OBJ-12, RTE-9 | Compilation, finite-score and task-quality checks | Metric truth, unbiased task construction and downstream admission | Independent semantic tests and documented corpus admission |
| Stage transition and full autonomy | CLM-1, RTE-4, RTE-5 | Independently launched training/search interfaces | One unattended recursive production loop | Inspectable scheduler/admission/rollback with retained run evidence |
| Memory branch and opaque payload limits | OBJ-3, OBJ-5, OBJ-6 | Normalized specialist scope below | Claims beyond specified forms, tasks, stages or observed activation | Materialized samples/checkpoints and consumer-linked execution evidence |

## Verification and blockers

### Semantic verification

Source pin, identities and paths were checked against the repository commit; no worktree or prior review supplied evidence. Quotes retain exact short passages and keep inferred mechanism separate from source claims. Canonical references and theory-builder conditions are separated from comparison assessments and epistemic architectural/candidate states. RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 and RTE-9 were audited for immediate return, later consumer, selection, expiry/recovery and limits; additional memory routes are checked in the integrated account. No delivered context was promoted to observed activation, no model judgment was promoted to an expected answer, and no reported table was promoted to independently observed or causal evidence.

Integrated comparison check: RTE-3, RTE-4, RTE-5, RTE-10 and RTE-11 cover the profile's accumulated-memory boundary, including legacy/optional branches and explicit external-interface limits. Online per-task summaries/cards, offline cross-task SFT and afforded online cross-task RL are each carried into source, scope, timing and form axes. RTE-10 names the consumer, impending-call trigger, selected node relations/error signature and retained parts for every push signal; requested training/checkpoint reads remain pull. OBJ-3's heterogeneous container has separate natural-language/symbolic/parametric payload records rather than a display-derived form claim. Faithfulness remains known no within ABS-1's bounded release evidence, not a claim about all private experiments. Every mapped ID is declared once; no local proposal token remains outside Reconciliation. Report and input hashes were rechecked; all material report limits and supporting quotes needed by the exact result are integrated.


### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-openrsi-01/result.md`. `commonplace-validate --full` completed with PASS (clean): no failures or warnings. Source quote occurrence is additionally checked by publication against full-commit blobs; structural validation does not establish semantic truth.

### Blockers

None; external evidence gaps limit conclusions but do not block this bounded source analysis.
