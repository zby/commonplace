---
type: agentic-system-analysis-result
description: Complete code-grounded analysis of Meta^n as an evolutionary code-injection improvement plane, with
  bounded memory and epistemic findings
run-id: AAS-2026-09-24-meta-n-01
system: Meta^n
run-date: '2026-09-24'
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
analysis-cutoff: '2026-09-24'
evidence-tier: code-grounded
memory-comparison:
  scope: Meta^n-owned use-accumulated task traces, candidate code/rationale and frozen solutions, archive selection/checkpoint
    state, optional imported seeds, and built-in per-task conversation summaries; includes repository external-agent
    injection/Trace conversion, excludes SDK-internal memory, provider weights, static prompts/configs, datasets
    and diagnostic-only opaque log payloads.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - in-memory
      records:
      - OBJ-4
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      note: JSON/text files retain candidates, traces and generated code; process objects retain indexes and continuation
        summaries. External SDK state and diagnostic-only opaque logs are excluded.
    representational_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - symbolic
      records:
      - OBJ-4
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      note: Code and structured selection metadata coexist with rationales, feedback and continuation prose; helper
        descriptions do not replace executable source in this union.
    lineage:
      assessment: known
      basis: wired
      values:
      - imported
      - other-compiled
      - trace-extracted
      records:
      - RTE-6
      - RTE-11
      - RTE-13
      - RTE-14
      note: Trace-fed generated code and summaries; mechanically assembled maps/indexes; imported optional helper
        seeds. The system does not establish who authored an imported seed.
    behavioral_authority:
      assessment: known
      basis: wired
      values:
      - enforcement
      - instruction
      - knowledge
      - learning
      - ranking
      - routing
      - validation
      records:
      - BAP-3
      - BAP-4
      - BAP-5
      note: Runtime code binds execution; emitted guidance instructs solvers; traces/rationales inform generation;
        scores and retained verification metadata govern selection and eligibility. These forces belong to separate
        consumers.
    write_agency:
      assessment: known
      basis: wired
      values:
      - automatic
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-13
      - RTE-14
      - RTE-15
      note: Inspected in-system writes are automatic. Selecting a seed file is operator configuration; seed authoring
        outside this system is not assigned a write agency.
    curation_operations:
      assessment: known
      basis: wired
      values:
      - consolidate
      - evolve
      - promote
      - synthesize
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-13
      - OBJ-6
      note: Summaries consolidate history; repairs and name overrides evolve versions; best/elite indexes promote
        salience; Omega can synthesize new code/strategy. Archive identity checks are not dedup; prompt truncation
        does not delete archived memory.
    read_back_direction:
      assessment: known
      basis: afforded
      values:
      - pull
      - push
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-11
      - RTE-13
      note: Automatic context/code supply is wired push. External helper files afford explicit reads/imports/calls
        by the named task agent; activation is not established.
    read_back_signal:
      assessment: known
      basis: wired
      values:
      - coarse
      - identifier
      - inferred-lexical
      records:
      - RTE-6
      - RTE-7
      - RTE-11
      - RTE-13
      note: Coarse outcome/fitness/depth/budget/recency selection, exact task/ancestor/helper identity selection,
        and error-keyword classification feeding representative-trace selection. No embedding or model-judged retrieval
        route was found in the inspected infrastructure.
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-13
      - RTE-15
      note: Automatic trace-fed writes retain code, frozen solutions or continuation summaries and feed later consumers;
        observed improvement is not required for this wired classification.
    trace_source:
      assessment: known
      basis: wired
      values:
      - session-logs
      - tool-traces
      - trajectories
      records:
      - OBJ-4
      - RTE-6
      - RTE-11
      - RTE-15
      note: Task execution records and iterative agent/environment message histories feed the routes; external transcript
        text may enter a Trace when no extracted solution exists. Opaque diagnostic event-stream copies are not
        assigned an additional learning route.
    learning_scope:
      assessment: known
      basis: wired
      values:
      - cross-task
      - per-task
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-13
      - RTE-15
      note: Candidate code is reused across the run task set; focus recursion, solution maps, self-debug and continuation
        summaries also have explicit single-task consumers. No project-spanning route is inferred from a run ID.
    learning_timing:
      assessment: known
      basis: wired
      values:
      - online
      - staged
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-13
      - RTE-15
      note: Outer search alternates build/evaluate stages; continuation summarization and task repair occur during
        an active solve. Resume restores stages and does not by itself create an offline learning route.
    distilled_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - symbolic
      records:
      - OBJ-5
      - OBJ-7
      - OBJ-8
      - RTE-11
      note: Generated executable hooks/helpers/frozen solution maps plus generated rationales and retained continuation
        summaries; no weight update is exposed.
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - CLM-4
      note: No qualifying retained execution evidence was inspected. Source tests, adoption heuristics and README
        claims do not establish an observed dependence test, nor establish that no such test occurred outside the
        frozen boundary.
---

# Meta^n agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-meta-n-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/meta-n.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-meta-n-01/memory-report.md`

**Memory analysis report SHA-256:** ff2961d6b190b25acf1c00705ade6c1217d983abab365edc73d2468231dab8f1

Run AAS-2026-09-24-meta-n-01 opened on 2026-09-24 before local midnight. System name: Meta^n. The run state declares publication completion.

## Boundary and evidence

The purpose is to characterize the inspectable improvement machinery behind Meta^n's recursive-self-improvement claim. Target class: builder or improvement plane. Boundary kind: whole-system, covering this repository's implemented responsibilities. Evidence tier: code-grounded. Frozen repository: `https://github.com/minnesotanlp/meta-n` at `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`, cutoff 2026-09-24.

Included: CLI/configuration, archive-based evolutionary orchestration, Omega code generation and repair, retained candidate/trace/code state, native single-shot and agentic solvers, code injection, task evaluation interfaces, local executor, external-agent lifecycle and source-visible persistence/compaction. The benchmark adapter interface and representative classification evaluator are inspected for oracle and split semantics; other benchmark-specific evaluators are interface boundaries, not independently audited answer oracles. Excluded: provider weights/transport internals, OpenHands/Terminus SDK internals, upstream benchmark datasets and service implementations, and the paper's experiment artifacts. These exclusions prevent an exact deployed isolation claim, complete external-context representation, independent benchmark-validity judgment, and observed or causal improvement claims. No prior target review, ingest prose or sibling analysis supplied evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/minnesotanlp/meta-n`; access root `/home/zby/llm/commonplace/related-systems/minnesotanlp--meta-n` | `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8` | implementation and test source | `meta_n/main.py`, `meta_n/core/`, `meta_n/utils/`, relevant adapter interfaces, selected tests/fixtures | full commit-relative citations and retained quotations | no live provider/benchmark execution; upstream SDK/evaluator internals excluded |
| SRC-2 | same Git repository | `https://github.com/minnesotanlp/meta-n` | `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8` | doctrine/design; separately attributed reported operation | `README.md`, `meta_n/configs/benchmark_features.yaml`, source comments describing intended or historical results | CLM records and configuration anchors | reports and source comments do not supply candidate-linked experimental records |

## Shared records

### Components

CMP-1 — Python evolutionary orchestrator and Omega engine. The orchestrator drives a bounded experiment over supplied tasks; Omega proposes executable injections from prior candidate evidence. The symbolic loop selects parents, evaluates children, retains candidates and stops by iteration, patience, depth or applicable budget conditions. It is not an open-ended service accepting arbitrary new user goals during a run. Implementation conclusion status: wired. SRC-1 `meta_n/core/evolutionary_orchestrator.py:636-1754`; `meta_n/core/omega.py:51-190`.

CMP-2 — Outer completion model serving Omega, the native solver and built-in summary calls. Distributed-parametric component exposed through `LLMClient`; default config names `anthropic/claude-sonnet-4-20250514` at an OpenAI-compatible endpoint, while Azure treats the name as a deployment. Model routing conclusion status: wired. Immutable parameter identity conclusion status: uninspected. Runtime parameter updates conclusion status: uninspected at the provider; the inspected product issues completions and changes code/context, not an inspected training operation. A dated model label does not by itself establish immutable weights. SRC-1 `meta_n/core/llm_client.py:1-16,149-210`; `meta_n/core/omega.py:148-156`; `meta_n/core/solver.py:180-186`.

> model: str = "anthropic/claude-sonnet-4-20250514"
> --- `meta_n/core/llm_client.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

CMP-3 — Models called inside generated solution programs or external agents. Classification and some other adapters supply an inner LLM helper; external backends have their own SDK/model call stack. Meta^n distinguishes inner usage from its outer code-generation usage and forwards model configuration at those interfaces. Call-boundary conclusion status: wired; complete model identities, hidden context transforms and parameter behavior conclusion statuses: uninspected. Post-hoc analysis utilities are outside the operational runtime under review, so their optional embeddings are not runtime-memory components. SRC-1 `meta_n/main.py:1680-1810`; `meta_n/integrations/benchmark.py:18-45`; `meta_n/core/external_agents/solver.py:411-556`.

CMP-4 — Executors, validators and adapter evaluators. LocalExecutor runs generated Bash on the host; adapters own benchmark-specific evaluation; external backends use provisioned environments and child runners. Static Python filtering and host callback timeouts are distinct from sandbox execution. Capability surface includes host `exec`, task subprocesses, filesystem writes, model network calls and optionally Docker; current grants and effective deployed isolation conclusion statuses: uninspected. SRC-1 `meta_n/core/base_executor.py:70-159`; `meta_n/utils/safety.py:1-9`; `meta_n/core/meta_layer.py:203-331`; `meta_n/core/external_agents/solver.py:273-556`.

> Host-exec reality: ``smoke_test_function`` (and the pre_process pipeline in
> meta_layer.py) exec model-emitted code in the meta-n HOST process, gated only
> by this static validation plus a wall-clock bound — not by the Docker sandbox.
> --- `meta_n/utils/safety.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> _worker = threading.Thread(target=_exec_block, daemon=True)
> _worker.start()
> _worker.join(pre_process_timeout)
> if _worker.is_alive():
> --- `meta_n/core/meta_layer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

### Operative objects

OBJ-1 — Task and run configuration. Authored/imported task descriptions, metadata, optional verification scripts, benchmark choice, model route and control flags. Form: natural-language task content and symbolic configuration. These are current run inputs; static supplied values are not use-accumulated memory. The operator selects tasks, evaluation domain and run budget. Conclusion status: wired. SRC-1 `meta_n/core/meta_layer.py:80-87`; `meta_n/main.py:1515-1680`.

OBJ-2 — Generated task solution. Model-produced Bash/Python program or classification output, returned by the selected solver and executed/evaluated. Candidate truth-apt parts depend on the task: predictions assert labels; a program prescribes computation and may implement a conjectured solution. Its execution score does not verify every explanation in the model's reasoning. Code becomes retained memory only through the later archive/reuse routes. Conclusion status: wired. SRC-1 `meta_n/core/solver.py:125-211`; `meta_n/core/agentic_solver.py:241-680`; `meta_n/integrations/text_classification.py:887-984`.

OBJ-3 — Shipped Omega guidance. Authored natural-language instructions embedded in code ask for score-improving executable intervention, rationale, task-structural generalization and simple helpers. The generator accepts optional rationale, preprocessing and library blocks; it does not require a formal explanatory theory or a criticism object. Higher-depth inputs select a different template when previous scores exist; the engine's fixed operation does not imply identical prompt bytes at every depth. Static guidance is retained in source and read on each applicable generation, but is excluded from accumulated-memory classifications. Conclusion status: wired. SRC-1 `meta_n/core/prompts.py:140-220`; `meta_n/core/omega.py:385-412,1201-1215`.

> - GENERALIZE: condition your intervention on task STRUCTURE (problem size, presence of hard constraints, metadata fields) — NEVER branch on specific task_id string literals. Code that keys off task_id values cannot transfer to unseen tasks and is wasted effort.
> --- `meta_n/core/prompts.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> elif depth >= 3 and previous_scores is not None:
> --- `meta_n/core/omega.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-4 — task execution traces and active solve history

Implementation conclusion status: wired within the declared object boundary. Raw/normalized evidence. `Trace` stores task ID, code, standard streams, success, score, reasoning, error summary, evaluator feedback, termination and adoption fields. Candidate traces live in memory and are written as JSON plus code files. Active built-in messages retain assistant code and user-role execution observations within one task. External `Trace.script` is best-effort solution text or transcript, so the field name does not guarantee executable Python. Consumer authority: evidence for Omega, task repair and selection, with specific frozen scripts later executable through OBJ-8. SRC-1 `meta_n/core/meta_layer.py:89-141`, `meta_n/core/run_persistence.py:377-385`, `meta_n/core/agentic_solver.py:603-635`, `meta_n/core/external_agents/telemetry/writer.py:427-461`.

>         # Traces
>         traces_dir = cand_dir / "traces"
>         traces_dir.mkdir(exist_ok=True)
>         for trace in candidate.traces:
>             with open(traces_dir / f"{trace.task_id}.json", "w") as f:
>                 json.dump(trace.model_dump(), f, indent=2)
>             ext = ".py" if detect_script_language(trace.script) == "python" else ".sh"
>             with open(traces_dir / f"{trace.task_id}{ext}", "w") as f:
>                 f.write(trace.script)
> --- `meta_n/core/run_persistence.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>         """Best-effort solution text for ``Trace.script`` (diff / solve.py / transcript).
> 
>         The env provider's ``extract_solution`` result (the T2 diff / CO-Bench
>         ``solve.py``) is the authoritative ``script`` and the spine stamps it onto
>         the run as a ``solution`` attribute when available; absent that, fall back
>         to the transcript so the Trace still carries something inspectable.
>         """
>         return str(getattr(run, "solution", "") or run.transcript or "")
> --- `meta_n/core/external_agents/telemetry/writer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-5 — injected code, rationale and generation provenance

Implementation conclusion status: wired within the declared object boundary. Derived memory. `InjectedCode` carries Python `pre_process`, named Python/Bash libraries, optional rationale, source depth, frozen solution map and verified-name metadata. Code is symbolic; rationale is natural language. The full prompt/response is inspection provenance, saved separately from the compact JSON. Retained rationale is actually read by later Omega context assembly, including a preview in the structured effectiveness section. The task solver normally sees emitted hook guidance and signatures/docstrings, not a dedicated copy of the rationale field. Rationale is optional and is not certified true. SRC-1 `meta_n/core/meta_layer.py:148-171`, `meta_n/core/omega.py:950-966,1069-1086,1201-1215`, `meta_n/core/run_persistence.py:387-414`.

>             if code.code_library_bash:
>                 for name, src in code.code_library_bash.items():
>                     part += f"solver_lib_bash:{name}:\n```bash\n{src}\n```\n"
>             if code.rationale:
>                 part += f"Rationale: {code.rationale}\n"
>             parts.append(part)
>         return "\n".join(parts) if parts else "(none — you are the first meta-layer)"
> --- `meta_n/core/omega.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> injected.raw_omega_prompt = prompt
> --- `meta_n/core/omega.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-6 — candidate archive and access structures

Implementation conclusion status: wired within the declared object boundary. Each candidate retains chain, parent ID, evaluation traces, per-task scores and search metadata. In-memory lists/dictionaries plus JSON files implement storage; parent edges alone do not constitute a graph database. Best-candidate and per-task-best indexes, parent weights, elite selection and breedable pools are access/control metadata. Ranking uses finite mean scores, exploration from child counts, optional depth/headroom bonus, and per-task `(success, score)` ordering. A retained task-best exclusion restricts index admission while preserving the candidate. SRC-1 `meta_n/core/archive.py:21-70,129-238,358-431,476-598`.

>     def _selection_weights(self, candidates: list[Candidate]) -> list[float]:
>         """Scale-invariant parent-selection weights (roadmap v2 2.1 / N4b).
> 
>         ``weight = rank_norm(mean_score) + alpha * sqrt(ln N / (1 + num_children))``
> 
>         ``rank_norm`` is the fraction of candidates with a strictly smaller
>         FINITE mean_score (in [0,1]) — invariant to any positive affine rescale
>         of the score, so the exploration term never vanishes against a large
>         score magnitude the way the old additive ``alpha/(1+children)`` bonus did
>         on continuous scales. Non-finite means rank at the bottom. The UCB term
>         favors under-explored candidates. Deterministic given the inputs.
> --- `meta_n/core/archive.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> Candidates are never removed. The archive tracks per-task best scores
> and supports weighted parent selection (fitness + exploration bonus).
> --- `meta_n/core/archive.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-7 — built-in continuation summary

Implementation conclusion status: wired within the declared object boundary. Natural-language, trace-extracted memory retained in the active message list. It replaces an older message span while keeping the initial message and the last four messages. The summarizer is asked to preserve task, attempts, scores/errors/outcomes and latest code. This can retain reasons and negative evidence, but preservation is prompt-directed rather than mechanically checked. The next LLM call reads the summary as user-role context. Its horizon is the concrete task passed into the solve loop; no session-ID inference is needed. SRC-1 `meta_n/core/agentic_solver.py:252-258,355-395,880-940`, `meta_n/core/agentic_prompts.py` (SUMMARIZE_PROMPT).

> SUMMARIZE_PROMPT = """Summarize the following conversation between a solver agent and an
> execution environment. Preserve:
> 1. The original task description (verbatim if short, summarized if long)
> 2. Key observations from each execution attempt (scores, errors, what worked)
> 3. What approaches were tried and their outcomes
> 4. The most recent code that was generated
> 
> Be concise but preserve all information needed to continue solving.
> 
> Conversation:
> --- `meta_n/core/agentic_prompts.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-8 — frozen per-task winning solution map

Implementation conclusion status: wired within the declared object boundary. Derived symbolic routing map from task IDs to previously evaluated script strings, bundled in `InjectedCode`. The merger assembles per-task winners without another LLM call or evaluation. The native MetaLayer consumer returns a matching script verbatim, bypassing the solver and library prepend. Its fixed rationale `SYNTHESIZED:Ω_merge` is a provenance label, not an explanation of why the script works. No map consumption was found in the native AgenticSolver or external InjectionMapper; capability must not be generalized to those branches. SRC-1 `meta_n/core/evolutionary_orchestrator.py:3735-3806`, `meta_n/core/meta_layer.py:494-523`; bounded search in ABS-2.

>         # follow-up.
>         frozen = self.injected_code.task_solution_map.get(task.task_id)
>         if frozen:
> --- `meta_n/core/meta_layer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-9 — checkpoint and reconstruction state

Implementation conclusion status: wired within the declared object boundary. JSON checkpoint plus candidate directories restore archive content, exclusions, RNG and progress. Candidate JSON retains code/rationale but excludes raw Omega prompt/response fields; readable sidecars keep those for inspection. Rebuild checks that the number of code sidecars matches declared depth, skips malformed/partial candidates, merges persisted task-best bars and recomputes child counts from lineage. This is mechanical reconstruction, not a fresh learned conclusion. SRC-1 `meta_n/core/run_persistence.py:60-102,126-234,387-414`, `meta_n/core/archive.py:796-918`.

>             archive_dir = out_dir / "archive"
>             self._orch.archive = Archive.rebuild_from_disk(
>                 archive_dir,
>                 barred_from_best=checkpoint.get("barred_from_best"),
>                 **self._orch._archive_kwargs(),
>             )
> --- `meta_n/core/run_persistence.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>         # Injected codes (full chain — always save JSON for consistent rebuild).
>         # raw_omega_prompt + raw_omega_response are excluded from JSON to keep
>         # injected_code_d{N}.json compact; they're persisted as paired sidecar
>         # .txt files instead so a reviewer can diff prompt ↔ response easily.
>         for i, ic in enumerate(candidate.injected_codes):
>             with open(cand_dir / f"injected_code_d{i+2}.json", "w") as f:
>                 json.dump(
>                     ic.model_dump(exclude={"raw_omega_prompt", "raw_omega_response"}),
>                     f, indent=2,
>                 )
>             if not ic.is_empty:
> --- `meta_n/core/run_persistence.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-10 — optional imported helper seed

Implementation conclusion status: wired within the declared object boundary. A caller-selected JSON mapping supplies helper source before Omega authors a layer. It becomes a source-depth-zero contribution in the candidate chain. The loader requires string names/sources and uses static code validation. Its upstream author and acquisition history are not established; classify the in-system lineage as imported and the loader's write agency as automatic. This is the concrete human editing/adoption surface: a person can supply a known helper file and choose the feature flags, but no in-repository manual memory editor is established. SRC-1 `meta_n/main.py:463-477,964-998`, `meta_n/core/evolutionary_orchestrator.py:925-937,2000-2051`.

>     from meta_n.utils.safety import validate_code
> 
>     with open(path, "r", encoding="utf-8") as fh:
>         raw = json.load(fh)
>     if not isinstance(raw, dict):
>         raise ValueError(
>             f"--seed-code-library {path}: expected a JSON object "
>             f"{{name: source}}, got {type(raw).__name__}"
> --- `meta_n/main.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

OBJ-11 — external log copies and diagnostic sidecars, boundary record

Implementation conclusion status: wired within the declared object boundary. Repository telemetry can copy external logs to `archive/<candidate_id>/agent_logs/<run_id>/` before scratch cleanup and retain pointers. These payloads are external-format diagnostics; no active replay consumer is established by the pointers. Only the separately normalized text in OBJ-4 enters the scoped learning chain. Likewise repair events and full Omega prompt/response sidecars support audit, not an independently established memory retrieval loop. SRC-1 `meta_n/core/external_agents/solver.py:528-548`, `meta_n/core/external_agents/telemetry/writer.py:906-976`, `meta_n/core/archive.py:833-850`. This record is excluded from the operative memory form union beyond its readable Trace conversion.

>                 root
>                 / "archive"
>                 / str(candidate_id or "")
>                 / "agent_logs"
>                 / str(run_id or "")
>             )
>             shutil.copytree(src, dest, dirs_exist_ok=True)
> 
>             # Repoint at the durable copy with an output_dir-relative pointer
> --- `meta_n/core/external_agents/telemetry/writer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

### Routes

RTE-1 — CLI/configuration admission and run dispatch. Trigger/principal: an operator invokes `meta-n` or its module with a benchmark or task file. Owner: CLI and orchestrator. Explicit CLI values override benchmark-specific YAML, then YAML defaults, then code defaults; custom task runs keep bare defaults. Missing selected config refuses startup; malformed YAML is reported and skipped, while wrong-typed recognized values refuse startup. The archive orchestrator is required. Benchmark defaults enable consolidation, regression guard and within-task recursion; they deliberately leave gate-dependent refinement off because consolidation bypasses that gate. External-run routes require a positive daily cap. Terminal output is the run summary and persisted result. SRC-1 `meta_n/main.py:1515-1680,1810-1850,1935-2007`; SRC-2 `meta_n/configs/benchmark_features.yaml`.

Implementation conclusion status: wired. Immediate return is startup refusal or completion after the bounded search; later memory effects belong to integrated archive routes. Delegated visibility: config and selected tasks shape solver/provider requests, not every CLI setting. Expiry: run lifecycle; resume re-derives config and warns about drift while new values win. Operator proposes config, parser and startup checks can veto invalid combinations; reverting settings starts or resumes under changed config rather than transactionally rolling back executed task effects. Guidance is authored experimental policy, not an outcome-validated theory. Configuration admission itself has no answer oracle or content-directed criticism. SRC-1 `meta_n/core/evolutionary_orchestrator.py:850-913`.

> consolidate: true            # per-task oracle (>= single chain by construction)
> --- `meta_n/configs/benchmark_features.yaml` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> if not getattr(args, "use_archive", False):
> --- `meta_n/main.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

RTE-2 — Native single-shot solve and execution. Trigger: candidate evaluation on a task. Model receives task/language-selected prompt plus any accepted injection context and returns OBJ-2. At depth one, orchestration calls `solve` then executor. A MetaLayer chain can first run retained preprocessing, advertise/prepend helpers or directly replay a frozen winner; its outermost execute path may self-debug a low score by asking its inner solver again and keeping the better trace. Generic memory details belong to the integrated injection/retry records. SRC-1 `meta_n/core/solver.py:125-211`; `meta_n/core/meta_layer.py:494-680`; `meta_n/core/evolutionary_orchestrator.py:2274-2433`.

Implementation conclusion status: wired. LocalExecutor writes a temporary Bash file, starts a new process session, captures stdout/stderr and returns a scored trace. Nonzero exit fails; after zero exit, a supplied verification script may veto. Timeout kills the process group and bounds pipe draining; the temporary file is removed, but arbitrary task side effects are not rolled back. Local execution is host execution, not a sandbox. Immediate return is trace/token accounting to evaluation; later read-back occurs only if the trace/solution is retained by archive routes. No independent delegated worker receives a memory payload on the native path. Selection: task/language/current candidate. Source truth beyond exit/verification domain is uninspected. SRC-1 `meta_n/core/base_executor.py:70-159`.

The model proposes task changes, executable/parser constraints can reject malformed material, and the executor/evaluator supplies operational outcomes. Current task instructions and injected guidance shape the proposal. Task-specific formulation and criticism are afforded through model calls and execution feedback, but no instance-linked formulated theory, content-directed criticism, resulting theory revision or capacity gain was observed. Optional verification script is an operator-supplied success predicate; an exit-only task has no independently supplied answer oracle.

> success = exit_code == 0
> if success and task.verification_script:
>     success = await self._verify(task.verification_script, timeout=10)
> --- `meta_n/core/base_executor.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

RTE-3 — Native agentic task loop. Trigger: evaluation selects `use_agentic`. Owner: AgenticSolver. It generates, parses, prepends the available library, executes, observes and repeats. Finite score determines the best retained trace within the task. Two consecutive completion signals terminate only after an executed finite-scored trace exists; confirmation is not itself a high-score or correctness test. No-code/parse errors become feedback. Context estimates above 85% trigger summary; above 95% stop before a model call. Optional accumulated spend and turn limits also stop. The summary's later-use path is integrated from the specialist. SRC-1 `meta_n/core/agentic_solver.py:241-680`.

Implementation conclusion status: wired. Immediate return is the best trace plus aggregate reasoning/usage/termination state; evaluation may archive it for later generations. Available helpers are visible in the current task context, not a separate delegated model. State expires with the invocation except what archive/log routes retain. Rejected model status or script does not undo executed effects. A fixed early exit uses score at least 1.0; benchmark scores can be continuous with no upper bound, so the code's `perfect_score` label is not a universal benchmark-optimality guarantee. RTE-5 supplies the domain-specific meaning of scores. Model proposes new scripts; finite-score selection and bounds decide continuation. Guidance combines task, retained code and feedback; a score comparison alone does not establish content-directed criticism or a general solution theory.

> if math.isfinite(trace.score) and trace.score >= 1.0:
> --- `meta_n/core/agentic_solver.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

RTE-4 — External-agent lifecycle and control boundary. Trigger: an adapter-supported OpenHands/Terminus backend, or advertised built-in external route. The orchestrator builds one solver per candidate. The wrapper starts telemetry, creates injection plan, checks available daily headroom, leases a bounded private environment, stages helpers, starts backend, extracts solution, scores, records spend and returns a trace. Its task execution happens in a child runner/SDK rather than importing the external SDK into the orchestrator. Memory payloads and staging are integrated separately. SRC-1 `meta_n/core/external_agents/solver.py:95-140,273-556`; `meta_n/core/external_agents/concurrency.py:132-240`; SRC-2 `README.md`.

Implementation conclusion status: wired at the inspected wrapper; external SDK execution and deployed permission envelope conclusion statuses: uninspected. The shared guard uses a semaphore, a private scratch directory, teardown/hard-kill callbacks and final cleanup. Backend hard timeout precedes a larger outer timeout; with no time limit that outer wall is absent. Most guarded faults become degraded traces, while cancellation propagates. Durable transcript copying is best effort before scratch removal. Immediate return is trace and accounting; later archive consumers may read the retained trace. SDK-visible task/injection context is known at handoff; internal history selection is excluded. No universal rollback of external task effects is established.

The daily cap is admission control, not a per-run spending kill. Concurrent admitted work can overshoot; missing metrics on killed/degraded runners undercount actual spend. Enforced owner/predicate: Meta^n admission and generation-boundary checks over recorded spend; guarantee strength: policy with external metering and cleanup contracts, not an exact deployed dollar bound. The wrapper admits model-driven task effects under operator-selected backends; no per-action human approval protocol is established within this wrapper. SRC-1 `meta_n/core/external_agents/budget.py:31-74,241-276`; `meta_n/core/external_agents/solver.py:411-556`.

> if self.cost_guard is not None and self.cost_guard.precheck(self.max_budget_usd):
>     rec.terminated_by = TerminatedBy.BUDGET_DENIED.value
>     return self.telemetry.finish_budget_denied(task, rec, self.depth), 0
> --- `meta_n/core/external_agents/solver.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

RTE-5 — Benchmark evaluation, repeated comparison and reporting. Trigger: native/external solve output. Owner: adapter evaluator and orchestrator. AdapterExecutor translates EvalResult into Trace; adapter-specific timeout and score semantics are authoritative. Classification compares predicted labels with dataset gold labels using normalized accuracy or per-example F1; validation and test are separate inputs. Those are supplied answer oracles for this benchmark mode, not knowledge inferred from model judgment. Other adapters expose domain-specific objectives/checkers at the declared boundary; their upstream answer validity is uninspected. SRC-1 `meta_n/integrations/benchmark.py:18-158,256-315`; `meta_n/integrations/text_classification.py:795-815,887-984`.

Implementation conclusion status: wired. Immediate return is score, feedback and trace to candidate selection. Evaluation writes operational judgments; later archive use can change parent choice and Omega proposals. Repetition may choose a median-scoring trace, while gate/frozen-consolidation traces can be reused. Exceptions become failed traces except cancellation. Finite candidate scores are averaged over finite traces; nonfinite traces remain in evidence but are excluded from that mean, so its denominator can differ from the full task set. Per-task oracle reporting separately uses the full task count with missing scores as zero. Optional common-random-number seeds reach only native depth-one solves on the configured supported backend; deep, agentic and external execute paths are unseeded. Thus no generic paired-causal experiment is implied. SRC-1 `meta_n/core/evolutionary_orchestrator.py:2364-2433,2463-2766,1515-1645`; `meta_n/core/llm_client.py:86-111`.

End-of-run held-out evaluation runs only where an adapter supports it; per-task winners are re-executed, while best-chain testing may re-solve when the adapter exposes a test-task route. The stored-solution selection, new solution generation and test evaluator are distinct operations. Test-set reporting does not retroactively make development-score admission a generalization proof. Guidance is task/evaluator specification; the evaluator can reject outputs under its metric, not certify a causal explanation of why an injection worked. No actual run of these tests is retained in this analysis. SRC-1 `meta_n/core/evolutionary_orchestrator.py:3824-3938`.

> gold = _normalize(ex["label"])
> if pred == gold:
>     correct += 1
> --- `meta_n/integrations/text_classification.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

> finite_traces = [t for t in traces if math.isfinite(t.score)]
> if finite_traces:
>     candidate.mean_score = (
>         sum(t.score for t in finite_traces) / len(finite_traces)
>     )
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

RTE-6 — archive evidence to a new Omega layer

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: breeding an archive-selected parent. Producer/selector: orchestrator and Omega. Retained inputs: parent traces/code/rationale, seed/grandparent scores, archive-best values, optional better same-task traces from other candidates. Output: parsed code/rationale attached to a new candidate and persisted after admission/evaluation. Later consumers: task solvers and subsequent Omega calls. Source status wired. SRC-1 `meta_n/core/evolutionary_orchestrator.py:1096-1188,1270-1290`, `meta_n/core/omega.py:68-189,305-490`, `meta_n/core/archive.py:648-709`.

Selection is automatic push to Omega, even though the implementation calls archive methods: the LLM consumer did not request a particular memory read. At most 20 traces are sampled with nominal 0.75 failure ratio. Default budget is 100,000 estimated tokens less 2,000 overhead, allocated 65% to traces and 35% to the code stack. CLI can override the maximum. Budget estimates use characters/4, not a tokenizer. Default trace eviction can preferentially lose successes; symmetric mode changes this. Oldest layers are hidden first but at least the newest layer is kept even when it exceeds its allocation. Entire old code remains live at the solver. Thus this is not a strict full-prompt bound: task text, inspiration and other appended sections may add volume beyond the two allocations. SRC-1 `meta_n/utils/context_manager.py:21-49,77-257`, `meta_n/main.py:1921-1934`.

>         # C2.1: dropped layers stay LIVE in the solver (MetaLayer merges the full
>         # stack) but vanish from the Omega prompt view -> re-synthesis /
>         # name-collision risk with no operator-visible signal. Emit ONE WARNING
>         # naming the dropped layers' source_depths. Only fires when truncation
>         # actually drops a layer, so the byte-identical (no-truncation) path is
>         # untouched.
> --- `meta_n/utils/context_manager.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

At depth three or above with prior scores, Omega renders category/failure statistics and up to three representative traces, selecting by focus ID, common error class, regression and success. Error class has structured precedence and a keyword fallback, so this selection includes `inferred-lexical`. Inspiration uses exact task matches and score gaps, capped at five. Task IDs are real selection inputs here, not merely labels. SRC-1 `meta_n/core/omega.py:1003-1167`, `meta_n/core/adoption.py:26-77`, `meta_n/core/archive.py:648-709`.

>         if focus_task:
>             focus_trace = current_traces.get(focus_task)
>             if focus_trace is not None:
>                 selected.append(focus_trace)
> 
>         # 1. Failure with most common error type
>         failures = [t for t in current_traces.values() if not t.success]
>         if failures:
>             error_counts = Counter(self._classify_error(t) for t in failures)
>             most_common_type = error_counts.most_common(1)[0][0]
>             rep = next(t for t in failures if self._classify_error(t) == most_common_type)
>             if rep not in selected:
> --- `meta_n/core/omega.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>     # Text fallback, reached only when terminated_by carried no structured signal.
>     if "max_turns" in text or "max turns" in text:
>         return "Turn starvation"
>     if not text.strip():
>         return "Unknown error"
>     if "timeout" in text or "timed out" in text:
>         return "Timeout"
>     # Numeric instability — precise tokens (avoid 'inf' matching 'infeasible').
>     if any(w in text for w in ("nan", "zerodivision", "divide by zero",
>                                 "overflowerror", "-1e9", "-1e+09", "not finite")):
>         return "Numeric instability"
>     if "import" in text or "modulenotfounderror" in text or "no module" in text:
> --- `meta_n/core/adoption.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

Admission and selection: the orchestrator samples parents from the depth-eligible/breedable pool using archive weights. The model proposes another layer; an empty result is skipped unless the consolidation focus branch permits a plain resample. RTE-16 applies optional helper checks. For a nonfocus child with gate tasks enabled, at least one successful task within the relative margin clears the gate unless the configured floor vetoes; absent the floor it returns on first success. Without a parent baseline, the relative test falls back to success. Gate-failed children may enter RTE-9; successful/focus/full-evaluated children enter the growing archive, while task-best eligibility and later breeding can impose further restrictions. Existing parents survive, providing a retained alternative rather than undoing side effects. SRC-1 `meta_n/core/evolutionary_orchestrator.py:1019-1440,2870-2995`.

Guidance: OBJ-3 asks for interventions from failures, higher-level patterns and prior effects. Retained OBJ-5 rationale/code is also guidance for later calls. Models propose and interpret; symbolic parsing, optional verification and quality policy can veto particular proposals. Benchmark/task evaluators supply the outcome interface on RTE-5; archive-best is a selection target, not an independent ground-truth oracle. Rationale is optional and unvalidated. Theory formulation is afforded by the code/rationale interface; actual formulated theoretical content, its operative semantic use, content-directed criticism, resulting theory revision and attributable capacity improvement all have conclusion status uninspected without a candidate-linked instance. Executable rule installation and subsequent source-wired consumers remain wired independently.

RTE-7 — retained layer to native solver guidance and execution

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: building/running a candidate solver. Selector: candidate chain, helper-name override merge, adapter library-liveness policy, validation. Retained inputs: OBJ-5 and optional OBJ-10. `pre_process` runs deepest-first, with task and accumulated outer text, producing `additional_context`; library signatures/docstrings enter the solver prompt, executable source is prepended to generated code. Runtime execution binds actual behavior; advertised availability alone does not prove a call. Later layers override earlier helper names. Hooks that fail static validation, raise, time out or emit non-string context are skipped. Deep-copy failure can fall back to sharing the live task, and a timed-out daemon thread is abandoned rather than forcibly stopped: this is not a complete isolation guarantee. SRC-1 `meta_n/core/meta_layer.py:180-194,203-329,494-572`, `meta_n/core/code_library.py:42-97,125-185,300-347`.

> def merge_code_libraries(
>     injected_codes: list[InjectedCode],
> ) -> tuple[dict[str, str], dict[str, str]]:
>     """Merge code libraries across layers. Returns (python_libs, bash_libs).
> 
>     Later layers override earlier by name within each library type.
>     """
>     merged_py: dict[str, str] = {}
>     merged_bash: dict[str, str] = {}
>     for ic in injected_codes:
>         merged_py.update(ic.code_library)
>         merged_bash.update(ic.code_library_bash)
>     return merged_py, merged_bash
> 
> --- `meta_n/core/meta_layer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>         # (single-sourced tail; deploy is a no-op + identical object when the
>         # flag is OFF, prepend of an empty library returns the input unchanged)
>         script, reasoning, tokens = await self.inner_solver.solve(task, context)
>         script = self._prepend_library(self._maybe_deploy_verified_helper(script))
>         return script, reasoning, tokens, context, False
> --- `meta_n/core/meta_layer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The native CO-Bench/SWE policy demotes generated Python helpers unless forced live; seed contributions are exempt when the relevant flags are active. Bash helpers use a separate channel. `foster_adoption` requests calls in prose; optional deploy fallback can generate a direct helper wrapper when the authored solve body is empty or re-derives the solution inline without calling a staged helper. Neither name implies measured voluntary adoption. SRC-1 `meta_n/core/evolutionary_orchestrator.py:1983-2051,2273-2362`, `meta_n/core/meta_layer.py:423-492`.

RTE-8 — retained layer to external agent prompt and helper files

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: an external-agent task run. InjectionMapper automatically merges code, executes hooks, creates a prompt suffix and stages readable helper files under `helpers/`. It guards unsafe helper names and Python importability; advertisement is a subset of staged helpers. The solver passes the plan to a named backend, with a workspace handle, and stages files before calling the agent. This is wired push delivery. A task agent can then request/read/import/invoke those helpers using the documented Python imports or Bash CLI interface: an afforded pull route, without an observed activation claim. SRC-1 `meta_n/core/external_agents/injection.py:1-44,252-340`, `meta_n/core/external_agents/solver.py:464-488`.

> * The ``pre_process`` channel + library *descriptions* become the
>   :class:`~meta_n.core.external_agents.backend.Prompt`'s ``system_suffix`` (OpenHands
>   maps it to ``AgentContext.system_message_suffix``; Terminus 2 folds it into the
>   leading instruction). The inter-layer ``additional_context`` becomes the ``prefix``.
> * The ``code_library`` / ``code_library_bash`` channels become *staged files* under
>   ``helpers/`` in the agent's workspace, with a Python re-export ``helpers/__init__.py``
>   so the agent can ``from helpers import <name>``.
> --- `meta_n/core/external_agents/injection.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>             await self.env_provider.stage_files(env, plan.staged_files)
> 
>             ctx = AgentRunContext(
>                 instruction=getattr(task, "description", "") or "",
>                 prompt=plan.prompt,
>                 # The env yields an opaque handle; the backend receives the
>                 # provider's ``workspace_handle`` (plan §2.3 L98).
>                 workspace=getattr(env, "workspace_handle", env),
> --- `meta_n/core/external_agents/solver.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The suffix channel is instruction/guidance, while files are symbolic code consumed on demand. The formatters' readable descriptions are not the complete payload. External SDK context policy, file-use decisions, summarization and replay are outside this source boundary and do not silently enlarge any comparison union.

RTE-9 — within-layer repair after quality-gate failure

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: a nonempty generated child fails the quality gate, with `within_layer_refine` enabled and no consolidation focus. Omega receives the rejected code, gate failure traces and previous layers with a repair directive. The orchestrator constructs a new candidate, re-gates it, and only retains/evaluates it if it clears the gate. The failed candidate is not mutated. Retained code carries rationale; the next Omega call can consume it through RTE-6. This is staged evolution of a program version from content-bearing errors, not proof that the reason was correctly diagnosed. SRC-1 `meta_n/core/omega.py:191-273`, `meta_n/core/evolutionary_orchestrator.py:1346-1382,2996-3184`.

>         """Stage 2 WITHIN-LAYER REFINE: one extra Ω call to fix ``buggy_injection``.
> 
>         Called ONLY from the gate-fail branch when ``within_layer_refine`` is ON
>         and the injection is non-empty (so gen0 / depth-1 / empty / focus
>         resamples can never reach here). Makes one ``OmegaEngine.refine`` call,
>         builds a NEW candidate from the corrected injection (monotonic — the
>         rejected ``buggy_child`` is never mutated or archived), re-gates it, and
>         KEEPS IT iff it now clears the gate. On success it is fully evaluated,
>         gets a ``within_layer`` :class:`SelfRepairEvent`, and is archived + saved.
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The repaired candidate is kept because it re-clears the gate; a later SelfRepairEvent `accepted` flag compares before/after scores on the earlier gate subset. That flag is distinct from `archived=True`. Guidance explicitly says to keep the approach/helper names and make the smallest correction; it can direct error repair without establishing that the diagnosis or broader approach is correct. Rationale remains available to later Omega consumers. Theory formulation is afforded; actual theory use, formulated criticism of its content, revision of that theory and capacity gain are uninspected. Local syntax/runtime/constraint error feedback may identify a concrete code error, while aggregate score change alone is not a formulated explanatory criticism. SRC-1 `meta_n/core/omega.py:274-300`; `meta_n/core/evolutionary_orchestrator.py:2996-3213`.

RTE-10 — downward repair of an intermediate layer

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: opted-in repropagation on an eligible archived depth-three-or-greater chain. Selector chooses an intermediate layer; Omega receives full-chain failure traces, layers below as context and layers above as downstream feedback. A new version replaces one injection in a newly constructed candidate; the old candidate remains. Unlike within-layer gate repair, the new evaluated result is archived even when its mean does not improve. The acceptance/provenance record must not be read as universal adoption. Retained rationale is consumed by later generation in the ordinary route. SRC-1 `meta_n/core/evolutionary_orchestrator.py:3240-3459`, `meta_n/core/omega.py:968-998`.

> 
>         Called ONLY from the post-archive.add depth>=3 branch when
>         ``repropagation`` is ON and :meth:`_should_repropagate` fired. Picks
>         ``d_t`` via :meth:`_pick_repropagation_depth`, rebuilds the context as the
>         layers BELOW ``d_t``, feeds ``omega.generate`` the FULL-CHAIN failure
>         traces (``child.traces``, contaminated by the layers above ``d_t``) plus
>         the above-layer injections as ``downstream_injections`` (so the call is
>         scoped to error-correction), REPLACES ``child.injected_codes[d_t-2]``, and
>         evaluates the new chain. The result is ALWAYS archived (monotonic — the
>         old ``child`` is retained); a ``downstream`` :class:`SelfRepairEvent` is
>         logged + classified. ``accepted`` records whether the mean improved.
> 
>         Returns ``(reprop_candidate | None, tokens_spent)`` — ``tokens_spent`` is
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

Admission has no better-score veto on archival here: `accepted` is a finite nonworse-mean provenance judgment; selection later determines whether the version becomes useful. Score means inherit RTE-5's finite-denominator limits. Guidance supplies prior code and full-chain errors plus higher-layer compatibility instructions, while RTE-16 handles optional helper filtering. The original candidate is retained for recovery. Theory formulation is afforded; actual theoretical content/use, its content-directed criticism, resulting revision and improved capacity are uninspected. Replacing source code is wired and does not by itself resolve those theory claims. SRC-1 `meta_n/core/evolutionary_orchestrator.py:3284-3462`; `meta_n/core/omega.py:968-998`.

RTE-11 — conversation history to retained continuation summary

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: estimated active context exceeds 85% of the built-in solver's token budget; an earlier check stops the loop above 95%. With fewer than six messages the summarizer returns unchanged history. Otherwise it summarizes all but the first and last four messages at temperature 0.3 and requested maximum 2,000 output tokens. It places the result in `messages` and the next LLM call consumes it; repeated triggers can fold earlier summaries into new ones. Summary failure logs a warning and preserves history. This is automatic push with coarse recency/budget selection. Source status wired. SRC-1 `meta_n/core/agentic_solver.py:355-395,880-940`.

>         """
>         if len(messages) < 6:
>             return messages, 0
>         first = messages[0]
>         keep_n = min(4, len(messages) - 2)
>         keep = messages[-keep_n:]
>         # Non-empty by construction: len >= 6 ⇒ keep_n == 4 ⇒ slice has
>         # len - 5 >= 1 elements.
>         to_summarize = messages[1:-keep_n]
>         conversation_text = "\n\n".join(
>             f"[{m['role']}]\n{m['content']}" for m in to_summarize
>         )
> --- `meta_n/core/agentic_solver.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The summary's durable scope is across later turns of one active solve, not a restart checkpoint. It may preserve reasons/outcomes because the prompt asks for them, but no exactness check is wired. It contributes `per-task`, `online`, `natural-language` to the trace-learning profile even if every outer Omega artifact is symbolic. Its retained message context is not a learned parameter update.

> return [
>     first,
>     {
>         "role": "user",
>         "content": f"## Prior work summary\n{summary}",
>     },
>     *keep,
> ], summ_tokens
> --- `meta_n/core/agentic_solver.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

Admission/recovery: the summarizer proposes text under static preservation instructions; no semantic coverage gate is shown, and failure keeps the prior messages. The next model call receives the replacement. This preserves a reasoning affordance but is not a theory-acceptance transition. Actual theory formulation/criticism inside the summarizer and resulting capacity improvement are uninspected; inapplicable to the mechanical slice/placement operation itself. The summary loses its active role at task termination unless separately retained in diagnostic logging, which has no established summary-restore route.

RTE-12 — persisted archive to resumed evolutionary search

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Trigger: caller chooses resume for a run with a valid checkpoint. RunPersistence reads checkpoint and candidate directories, restores indexes and RNG, and subsequent search uses the rebuilt objects. Named later consumer is the evolutionary orchestrator, with Omega/solver consumers reached by existing routes. This is automatic restoration of the selected run's state, not a retrieval service for unspecified future clients. Integrity mismatches skip candidates; an empty rebuilt archive starts fresh. No manual repair/adoption is inferred from JSON editability. SRC-1 `meta_n/core/run_persistence.py:60-124`, `meta_n/core/archive.py:739-918`.

RTE-13 — winning task traces to inherited evaluations and frozen dispatch

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. Two consumers share selected per-task winners. During consolidation, all nonfocus task results are copied from archive bests and reused without solving; only the focus task is fresh. Optional within-task recursion preserves the same unsaturated focus down the chain. At merge, archived winning scripts are assembled into OBJ-8 and the native MetaLayer matches `task.task_id` to return the stored program. This is automatic identifier-based push to the executor, with ranking selecting which program is retained. It is not cross-task generalization merely because the map covers many tasks. The producer's word “synthesize” describes mechanical assembly here; it does not establish a new explanatory claim. SRC-1 `meta_n/core/evolutionary_orchestrator.py:3548-3605,3689-3810`, `meta_n/core/meta_layer.py:515-523,588-594`.

>             # Deep-copy so the merged candidate never aliases the archive's
>             # _best_per_task entries (in-place tagging, e.g. failure_class,
>             # must not leak into the per-task-best index) — same discipline
>             # as the consolidation-inherit path above.
>             frozen = tr.model_copy(deep=True)
>             task_solution_map[t.task_id] = frozen.script
>             merged_traces.append(frozen)
>         if not task_solution_map:
>             return None
> 
>         merge_ic = InjectedCode(
>             task_solution_map=task_solution_map,
>             rationale="SYNTHESIZED:Ω_merge",
>             source_depth=2,
>         )
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The profile counts this as trace-fed symbolic retention because the later consumer actually executes the winning output; ordinary task files with no later consumer remain excluded. Its task horizon is per-task keyed reuse even when selected alongside a benchmark-wide set.

Admission/recovery: symbolic winner selection and deep-copy assembly create the map; there is no new model proposal or new evaluator call at merge. Existing archives remain. Objective is retained task-set performance, with RTE-5 supplying prior scores; there is no new answer oracle. Guidance is winner identity and measured task outcomes, not a newly formulated theory. Theory formulation/criticism and theory revision are inapplicable to mechanical selection/assembly; transfer or improved future problem-solving capacity is uninspected. Backend dispatch limits in ABS-2 prevent extrapolating native frozen replay to external or iterative backends.

RTE-14 — operator-selected seed file to retained candidate library

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. The loader reads and validates a JSON helper mapping; generation zero receives a copied library with `source_depth=0`. It is then persisted and delivered through the ordinary library routes. Operator intent selects the supplied file; the inspected transformation/writes are automatic. This is an import path, not evidence of automatic trace extraction from the seed's unknown upstream history. SRC-1 `meta_n/main.py:964-998`, `meta_n/core/evolutionary_orchestrator.py:925-937`.

Admission/recovery: operator selects a file, loader checks mapping/source shape and static code rules, and invalid input can be rejected before running. Imported helper meaning/rationale and upstream criticism are uninspected; importing source is not an in-system theory-learning process. Existing run artifacts remain unless the caller starts a different run. The retained code reaches the same downstream checks/consumers as generated code.

RTE-15 — trace-fed within-task solution repair and later archive consumption

Implementation conclusion status: wired; requested external helper consumption on RTE-8 is afforded. A native MetaLayer below the retry threshold constructs a debug prompt from the retained best attempt's code, errors and evaluator feedback; it keeps only score-improving retry traces as the winner. The built-in iterative solver similarly appends execution observations, generates later code, and retains a best trace. When that trace reaches candidate persistence, Omega can read the resulting solution and the frozen-map route can reuse it. This supplies an online/per-task/symbolic route alongside RTE-11, not merely raw logging. Rationale/reasoning fields can be retained, but the debug prompt emphasizes code and execution outcomes and does not separately consume the prior rationale field. SRC-1 `meta_n/core/meta_layer.py:602-650,738-773`, `meta_n/core/agentic_solver.py:288-326,603-635`.

>                 debug_context = self._build_debug_context(
>                     additional_context, best_trace, retry + 1,
>                 )
>                 retry_script, retry_reasoning, retry_tokens = (
>                     await self.inner_solver.solve(task, debug_context)
>                 )
> --- `meta_n/core/meta_layer.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

This record annotates the trace-fed repair subpaths of RTE-2 and RTE-3, rather than introducing a second task executor. Models propose revised task code; the retained best trace and evaluator feedback shape the proposal; finite/better-score rules choose a winner. Original execution side effects are not reversed. Actual explanatory formulation, content-directed theory criticism/revision and improved capacity are uninspected; the error-responsive code proposal and later archive delivery are wired.

RTE-16 — Optional Python helper verification and retained admission metadata. Trigger: enabled `verified_code` after fresh Omega generation, within-layer refinement or downward replacement. Owner: orchestrator with adapter-supplied verifier. Model proposes source; verifier evaluates an entry point with lower/sibling helper context; passed source is kept, failed source initially dropped. Dependency closure can re-add a failed sibling required by kept code without adding it to the verified-name set. Preprocessing and Bash helpers pass through this particular gate. BAP-5 carries the retained metadata's later authority. SRC-1 `meta_n/core/evolutionary_orchestrator.py:2057-2185`; `meta_n/core/verified_code.py:40-96,190-249`.

Implementation conclusion status: wired. Immediate return: filtered injection and verified-name set to construction. Later consumer: candidate library delivery and verified nonadoption eligibility; selection is exact helper/dependency name. Invalid/failed candidates can be dropped while existing archives remain; enabled gate without a real harness keeps source marked unverified. The real sandbox verifier uses network-disabled/read-only Docker with resource bounds and a supplied runner/predicate. That predicate is the helper answer oracle, with family-specific scope; the stub has none. The adapter interface identifies CO-Bench crew as the implemented real harness; other upstream oracle validity is uninspected here. Guarantee strength: protocol/invariant for this branch's checks, not a guarantee that every delivered helper passed an independent test. RTE-7/RTE-8 may apply additional runtime validation/staging rules.

Guidance is proposed helper specification/code plus a supplied executable check. Formal/syntactic or held-out checks can find errors in that target domain; they do not validate an optional explanation of why the helper generalizes. Actual theory formulation/use, content-directed criticism of its explanatory content, resulting theory revision and attributable capacity improvement remain uninspected. This filtering route modifies a candidate library, not the fixed Omega or validator implementation. SRC-1 `meta_n/integrations/benchmark.py:231-254`.

> return VerifyResult(
>     passed=True,
>     evidence="no held-out harness (stub) — kept UNVERIFIED",
>     ran_in_sandbox=False,
> )
> --- `meta_n/core/verified_code.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

### Claims

CLM-1 — Recursive self-improvement through emergent depth. README says Omega reads lower-layer traces and writes executable preprocessing/helpers, and its fixed operation is repeatedly applied. Claim conclusion status: claimed; the generation/injection/search path is wired. Higher-depth prompt selection supplies explicit structural guidance, so “emergent roles” does not mean the shipped generator has no depth-dependent instructions. Actual role emergence and net improvement are uninspected here. SRC-2 `README.md`; SRC-1 `meta_n/core/omega.py:385-412`; `meta_n/core/prompts.py:208-220`.

> Meta^n instead keeps a single universal meta-operation **Ω** fixed and recurses on its **input**: Ω reads execution traces from the layers below and writes *executable code* (a `pre_process` hook plus a `code_library` of utilities) that is injected into the layer beneath it, changing its behavior.
> --- `README.md` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

CLM-2 — Monotone archive and constructive code channel. README explicitly calls the project a research prototype and limits empirical claims. Claim conclusion status: claimed for reported efficacy; archive/injection wiring is supported in the memory records. Retaining the maximum of more draws differs from proving a better generating procedure. Source comments reporting helper gains or historical regressions are author reports, not observed/causal capsules in this analysis. SRC-2 `README.md`; SRC-1 `meta_n/core/evolutionary_orchestrator.py:920-980,1440-1645`.

> Empirical results are exploratory and should not be read as headline wins — see the paper for the full analysis.
> --- `README.md` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

CLM-3 — Verified helper and adoption terminology. Verification means a particular configured check, with a keep-unverified stub when no checker is supplied; dependency closure can retain unverified siblings. Helper-call attribution scans script text using word/path patterns and shadowing checks. That is an implemented proxy, not a dynamic proof that the helper executed or caused a score change. Claim-level labels must be read through these mechanisms. Conclusion status: wired for the checks/proxy; actual helper-dependent improvement conclusion status: uninspected. SRC-1 `meta_n/core/verified_code.py:40-97`; `meta_n/core/evolutionary_orchestrator.py:2057-2185`; `meta_n/core/adoption.py:79-131,214-282`.

> word_hit = bool(pat.search(script)) and not def_pat.search(script)
> file_hits = file_pat.findall(script)
> if word_hit or file_hits:
>     called.append(name)
> --- `meta_n/core/adoption.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

CLM-4 — memory-faithfulness evidence limitation

Conclusion status: uninspected. This is a limitation, not an evidenced absence. The full `ls-tree -r --name-only` inventory at the frozen commit supplies source/tests/fixtures, not an inspected experiment run proving dependence on recalled content. Searches for adoption/verified/recall/faithfulness-related tests located source assertions in `tests/test_foster_adoption.py`, `tests/test_verified_code.py`, context and repair tests. They were not executed; names and mock tests cannot certify field performance. SRC-2 `README.md` calls the project a research prototype and claims a working correct-helper channel, while pointing to an excluded paper. This prevents a `yes` faithfulness classification; it does not justify universal `no`. No claim of observed improvement is made.

### Evidenced absences

ABS-1 — no separate embedding memory store in the inspected owned routes

Conclusion status: absent for that bounded separate-store finding. At the frozen commit, complete path inventory plus commit `grep -n -E 'vector|embedding|sqlite|retriev'` over `meta_n/core`, `meta_n/utils`, `meta_n/integrations` returns only algorithm categories, a sample SQLite installation, dataset download, model listing and safety comments. The active memory definitions/writers/readers inspected above are files and process objects. This bounded search supports no separate vector/SQLite retrieval store within the owned memory routes; it does not establish absence from external SDKs or arbitrary generated programs. Model selection uses a configured client/backend (`meta_n/main.py:1007-1019,1628-1656,1921-1934`); no model-parameter write is exposed in these routes. The fixed Omega method in README is a claim about the operation, not a verified immutable provider model version.

The model-parameter observation is a boundary limitation, not an evidenced absence of provider-side updates; see CMP-2 and CMP-3. Search revision: `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`.

ABS-2 — frozen-map and external-log replay boundaries

Conclusion status: absent for the named consumers within the searched implementation. Search revision: `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`. Commit-wide `grep -l 'task_solution_map'` over `meta_n/core`, `meta_n/utils`, `meta_n/integrations` finds only `archive.py`, `evolutionary_orchestrator.py`, and `meta_layer.py`. Inspection of the builder's early external/agentic branches (`meta_n/core/evolutionary_orchestrator.py:2273-2346`) and native map consumer establishes that `AgenticSolver` and external InjectionMapper do not dispatch OBJ-8 in the inspected implementation. Do not report the native route as backend-universal. Similarly `grep -l -E 'transcript_ptr|agent_logs_ptr'` in those roots finds only external solver and telemetry modules; pointers do not establish an Omega replay of archived opaque logs. The separately wired `Trace.script` transcript fallback remains included.

### Behavioral-authority paths

BAP-1 — Operator configuration to CLI/orchestrator: symbolic flags/task inputs choose capabilities, budgets and experimental scope for a run. Force: routing and instruction. Conclusion status: wired. SRC-1 `meta_n/main.py:1515-1680,1935-2007`.

BAP-2 — Generated task script to executor/evaluator: code has operational execution force under the selected host/environment grants; scores and feedback acquire later selection force only through archive/admission consumers. Horizon: task evaluation and subsequent retained candidate use. Conclusion status: wired. SRC-1 `meta_n/core/base_executor.py:70-159`; `meta_n/integrations/benchmark.py:282-311`; `meta_n/core/evolutionary_orchestrator.py:2383-2433`.

BAP-3 — code and emitted instruction authority

Implementation conclusion status: wired for automatic delivery/control; external requested consumption is afforded. OBJ-5 and OBJ-8 bind native execution through prepended code or frozen dispatch (`enforcement`, `routing`); hook-emitted text and helper-use requests have `instruction` authority at the solver. Helper source may simply be available without activation. Evidence is the actual consumption in RTE-7, RTE-8 and RTE-13, not the word “injection.” This does not attribute every possible enforcement operation to every generated helper.

BAP-4 — evidence, learning and ranking authority

Implementation conclusion status: wired for automatic delivery/control; external requested consumption is afforded. OBJ-4 traces and OBJ-5 rationale provide `knowledge` to Omega; automatic trace-fed generation/summary/repair has `learning` authority at later tasks or turns. OBJ-6 scores/child counts control `ranking` and selection, and OBJ-8 controls task routing. Error-aware refinement can criticize code content using feedback; score-based winner retention alone does not establish criticism of a claim. See RTE-6, RTE-9, RTE-10, RTE-11 and RTE-15.

BAP-5 — retained verification and admission authority

Implementation conclusion status: wired for automatic delivery/control; external requested consumption is afforded. Optional `verified_code` invokes a held-out verifier for Python helper entries; absent a family harness, a keep-all stub returns `ran_in_sandbox=False`. Kept helpers that depend on another helper cause a transitive dependency closure to re-add that dependency even if it failed its own check. Such a dependency is not added to `sandbox_verified_names`. This retained per-layer set survives persistence and is read to restrict the verified-helper nonadoption bar on per-task-best. Thus “kept,” “sandbox checked,” “advertised,” “called,” and “task best eligible” are different states. `validation` belongs to this retained evidence at its admission consumer, rather than importing all runtime guards into memory authority. SRC-1 `meta_n/core/evolutionary_orchestrator.py:2059-2259`, `meta_n/core/verified_code.py:41-96`, `meta_n/core/archive.py:185-198,884-897`.

>                 )
>         # Dependency-aware keep: deploy prepends every KEPT helper together, so a
>         # kept helper that name-calls a sibling needs that sibling present or it
>         # NameErrors at runtime. Add back the transitive closure of injection
>         # helpers name-called by any kept helper — even ones that individually
>         # failed the single-entry-point oracle. A depended-upon sibling was never
>         # verified AS an entry point, so it is NOT added to sandbox_verified (the
>         # T3.2 penalty still bars per-task-best only on genuinely-verified names);
>         # genuinely-dead helpers (called by nothing kept) stay dropped.
>         from meta_n.core.adoption import scan_helper_calls
> 
>         all_names = list(injected.code_library)
>         frontier = list(kept)
>         while frontier:
>             src = injected.code_library[frontier.pop()]
>             called, _ = scan_helper_calls(src, all_names)
>             for dep in called:
>                 if dep not in kept:
>                     kept[dep] = injected.code_library[dep]
>                     frontier.append(dep)
>         # Stamp the sandbox-verified set onto the returned injection so the newest
>         # layer carries its own genuinely-verified names into the child chain (the
>         # override-aware penalty aggregation reads this per layer). Only reached on
>         # the ON path with a non-empty library — the default-OFF early-returns above
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

>         ``None`` ``utilities_called`` means UNMEASURABLE (demoted/no live helpers)
>         and is never penalized.
> 
>         T3.2 (audit): ``sandbox_verified_names`` is the set of helper names that
>         ACTUALLY ran in the sandbox (``ran_in_sandbox==True``). When supplied for a
>         layer, its verified set is restricted to ``code_library ∩
>         sandbox_verified_names`` so a STUB-KEPT (``ran_in_sandbox==False``)
>         UNVERIFIED helper never bars per-task-best — a helper we never actually
>         verified must not gate a real win. ``None`` (legacy callers / existing
>         tests) ⇒ that layer treats every code_library key as verified.
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

The ordinary quality gate is a separate branch. Bundled benchmark defaults enable `consolidate`; focus children skip that gate, so its failure-triggered within-layer repair is dormant under that profile. Code defaults, custom task runs and explicit overrides differ. A configurable gate is not evidence that all retained candidates passed it. SRC-2 `meta_n/configs/benchmark_features.yaml:1-48`; SRC-1 `meta_n/core/evolutionary_orchestrator.py:1285-1305`.

>                         # Gate check. G9: skipped in consolidate mode — only the
>                         # focus task is solved and inherited tasks cannot regress,
>                         # so the gate is moot, and gate re-solves would re-roll the
>                         # frozen tasks.
>                         gate_traces: dict[str, Trace] = {}
>                         if self.config.gate_tasks > 0 and not focus_task:
> --- `meta_n/core/evolutionary_orchestrator.py` @ `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`

## Runtime account

An operator chooses a bounded benchmark/task set and run configuration. RTE-1 builds model, adapter, executor and archive orchestrator. A seed candidate runs through the same selected solver family as later candidates. The outer search selects breedable parents, asks Omega for a new injection from parent traces and the prior code stack, constructs a new chain, applies configured admission/evaluation, and retains the resulting candidate. The model proposes improvements; symbolic policy chooses parents, filters permitted code, applies score conditions and terminates. Humans supply experiment/task definitions and can choose seed helpers or flags; there is no requirement for human review of each generated injection.

Native single-shot RTE-2, iterative RTE-3 and external RTE-4 are distinct solver families beneath the same search. Task evaluators on RTE-5 provide outcome signals. The memory specialist's records trace generation, repair, selection, persisted artifact and later-consumer transitions without collapsing those families. The ordinary operation is bounded experimental optimization, with custom task mode as another fixed supplied task set. No open curriculum generator or arbitrary production deployment service is inferred.

Material alternatives: bare task runs versus bundled benchmark profile; native versus external solver; direct generation versus iterative execution; live versus demoted helper library; real held-out verifier versus keep-all stub; gate-based candidates versus consolidation/frozen-result reuse; continued child extension versus same-layer repair or downward replacement; static context truncation versus agentic model summarization; fresh run versus resume. A guarantee at one admission point does not cover all these paths.

Four static forcing cases delimit the main claims:

1. A generated preprocessing block fails static validation, raises, produces non-string context or times out: it is skipped. Its daemon thread is abandoned on timeout, not killed. Task deep-copy failure falls back to the live task reference. Docker claims for task execution therefore do not cover all generated-code effects in the host. SRC-1 `meta_n/core/meta_layer.py:203-331`; `meta_n/utils/safety.py:1-9`.
2. A child clears one sampled quality-gate task: absent the optional floor, this is enough to pass. With the floor, later sampled hard regression can veto. Consolidation bypasses the gate entirely and evaluates only the focus task while reusing other results. The quality gate cannot be described as complete nonregression testing. SRC-1 `meta_n/core/evolutionary_orchestrator.py:1285-1430,2870-2995`.
3. `verified_code` is enabled without a real adapter verifier: helper retention is marked unverified, while adoption-related policy can remain active. A real verifier can reject a helper, but dependency closure can retain it as a required sibling without promoting its verification status. This is not “every deployed helper passed its own check.” SRC-1 `meta_n/core/evolutionary_orchestrator.py:2057-2185`.
4. An external run loses metrics or exceeds remaining headroom after admission: accounting can understate spend, and no per-run USD kill is guaranteed. Stop/cleanup wrappers bound selected lifecycle failures but do not prove every external side effect was reversed. SRC-1 `meta_n/core/external_agents/budget.py:31-74`; `meta_n/core/external_agents/solver.py:273-556`.

No dynamic check planned. Considered unit/mock gate checks, local toy execution and live benchmark runs. Static inspection establishes the declared predicates and branch distinctions; mocked scores would not establish generalization, semantic criticism or actual model use of helpers. Live provider/SDK/benchmark services and credentials were not provisioned. No attempted command is misreported as execution evidence.

## Lens scoping

### Memory/context scope

Full lens: SRC-1 and SRC-2 show retained candidates, injections, traces, summaries, checkpoints and code read-back. The frozen input commissions all use-accumulated writes, maintenance and later consumers, including native summarization and external payload boundaries. Static prompts/config and ordinary task products without later memory consumers are excluded. Source-visible external contracts are included with opaque internals preserved as uncertainty. This requires a full specialist pass because the improvement loop operates through retained code and evidence.

### Epistemic scope

Full lens under `kb/instructions/analyse-external-system-epistemic-architecture.md`, applied locally as a sparse overlay on the canonical records. CLM-1, CLM-2 and CLM-3 require distinguishing model-proposed interventions, executable checking, benchmark outcomes, candidate admission, archive selection, retained rationale and causal explanation. Assessed: native and wrapper operational paths plus integrated memory routes. Upstream oracle validity, provider reasoning and paper experiment artifacts are excluded, preventing actual candidate lifecycle and causal efficacy conclusions.

## Lens outputs

### Memory/context lens

The specialist inventoried OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, OBJ-10 and boundary object OBJ-11 through RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12, RTE-13, RTE-14 and RTE-15. RTE-16 registers the materially distinct helper admission described in its authority proposal. Its profile excludes opaque diagnostic-only OBJ-11 and external SDK-internal memory, while including normalized text converted into OBJ-4.

#### Write side

The write chain is execution/feedback → candidate trace → Omega-selected context → generated hook/library/rationale → candidate evaluation/admission → archive persistence. RTE-6, RTE-9 and RTE-10 share this reason-bearing derived artifact but have different triggers and acceptance rules. Layer rationale is retained in ordinary JSON, survives resume and reaches later Omega prompts. Full raw prompts/responses are paired audit sidecars, excluded from the restored injection object. A repair event can describe an attempted replacement without establishing that a better theory was adopted.

Retention is monotone at the candidate archive level. “Evolve” refers to constructing a revised layer/program version and name-based overrides, not erasing the parent. “Promote” is best/elite salience. “Consolidate” applies to continuation compression and assembled selected views; the application's `--consolidate` mode primarily freezes nonfocus outputs and must not be mistaken for semantic deduplication. Identity collision checks prevent duplicate IDs, not near-duplicate memory. Prompt truncation hides material from one consumer while preserving it for another; it is not archive decay. No automatic withdrawal of existing candidate content was established; failing fresh admission is rejection rather than invalidation.

Trace-fed derived-memory alternatives are all included in the dependent axes: multi-task Omega synthesis; per-task focus/deepening; within-layer/downward repair; online solution repair followed by archive consumption; frozen winning-script reuse; and online continuation summaries. Deterministic Omega rendering and debug excerpting do not independently become persistent learned summaries merely because their text is shortened. They support the later generated artifacts. Manual seed-file authorship lies upstream of the inspected system; the supported local interface is import and automatic persistence.

#### Read-back

The named downstream consumers are Omega, native single-shot/iterative task solvers, the native MetaLayer executor path, external task agents, and the resumed orchestrator. Omega is automatically supplied selected memories; it is not implementing a memory tool request. Exact task identity selects inspiration/focus/frozen outputs, ancestry selects baseline scores, and helper identity controls override. Broad candidate fitness, failure ratio, recency/depth and budgets are coarse signals; keyword-derived error classes influence representative trace selection and add `inferred-lexical`. There is no need to call object IDs a retrieval signal when they merely label an archived item.

External staged helpers establish an explicit pull affordance for a named consumer role with a supported interface (`from helpers import <name>` or the advertised script invocation). File delivery is wired, reading/calling is afforded, and effectiveness is unobserved here. Native helper descriptions similarly expose callable code, but the automatic prepend itself is push. Source inspection can show the binding executable route without proving that a model-generated solution uses a helper. Adoption tracking includes text/regex heuristics in `meta_n/core/adoption.py:80-124`, which do not by themselves prove causal dependence on the helper's retained content.

Context limits are approximate. Omega may omit still-active low-depth code, reducing its visibility into the program it is revising. The source warns about re-synthesis/name collisions. Agentic summaries trade older observations for a generated account; repeated replacement can accumulate omissions. The code retains the newest messages and original task context, but neither budget handling nor the summary prompt guarantees faithful preservation. These are material information-selection limits, not evidence of an observed failure in this run.

#### Comparison rationale

The profile's union is limited to owned memory surfaces. Files/in-memory cover operative code, rationale, traces, access state and continuation history; JSON does not turn natural-language fields into wholly symbolic content. Executable helper payloads remain symbolic even when the prompt shows only descriptions. External opaque logs and SDK state are boundary records, not silently classified payloads.

Automatic trace-fed code generation and continuation summaries establish `trace_learning: yes` at wired strength. The qualifying inputs include execution/tool traces and task trajectories, with conversation history classified as session logs even though held in process rather than first serialized as a log file. No event-stream learning is inferred from copying OpenHands log directories. Outer multi-task generation contributes cross-task/staged; explicit focus recursion, frozen scripts and active solve repair/summary contribute per-task, with online timing from the last two. Both symbolic and natural-language distilled forms are necessary. No separate offline or per-project route is established.

The lineage union is trace-extracted generation/summary, other-compiled maps and indexes, and imported seed source. It deliberately omits authored: an unknown seed file could have been authored manually, but its provenance is not fixed by this source. The write-agency union is automatic for these same in-system write routes. The external task-agent pull is afforded while push is wired; the combined direction axis therefore uses the weaker afforded basis, without weakening each route's implementation status.

Curation classifications do not promote a source label into proof. “SYNTHESIZED:Ω_merge” is selection/assembly; novel model-written code/strategy in RTE-6 supplies synthesis. The archive itself grows, while derived summary/code versions consolidate or evolve and index salience promotes winners. Curation admission filters, import and duplicate-ID guards alone supply none of those operations. Faithfulness remains not determinable because no qualifying retained execution result was inspected.

#### Route return and horizon audit

All effects below are wired or explicitly afforded, not observed activation. Canonical records supply trigger/selector/owner and source anchors. No process boundary itself creates a new task horizon.

| route | immediate return and later consumer | delegated visibility | invalidation/expiry and evidence limit |
|---|---|---|---|
| RTE-6 | proposed injection to evaluation, later solver and Omega | selected traces, earlier code/rationale and comparisons | bounded prompt hides still-live code; rejected empty/gate-failed proposal need not enter archive |
| RTE-7 | text/code to native solver/executor | hooks see task/outer context, model sees guidance and library descriptions | later same-name override; validation/timeout skip; execution may ignore advertised helper |
| RTE-8 | staged files/suffix to backend, requested helper access afforded | source-visible task, prompt and files; SDK policy excluded | scratch teardown after run; persistent candidate source remains |
| RTE-9 | replacement version after re-gating, then archive | rejected code plus gate traces to Omega | failed repair discarded; prior archive parent persists; accepted flag differs from retention |
| RTE-10 | evaluated replacement chain then archive regardless of score rise | full-chain evidence plus above/below code | old version persists; subsequent selection determines reuse |
| RTE-11 | new message list to next model call | selected old messages to summarizer | later summary may replace it; task end ends active retention; fidelity unchecked |
| RTE-12 | reconstructed archive/state to search | saved candidate code/rationale and indexes, not full opaque SDK logs | invalid/partial candidates skipped, empty archive fresh-starts; config drift warns |
| RTE-13 | copied nonfocus results or frozen task-keyed program | selected stored winner, no new model at merge | no native-map dispatch in early agentic/external branches; no novel transfer claim |
| RTE-14 | validated imported library to seed construction | selected source file, upstream provenance unknown | loader rejects invalid input; later name overrides can supersede content |
| RTE-15 | winner task attempt to archive/next Omega | current-task execution feedback to model | losing attempt not selected as winner; logs may survive separately; effects not rolled back |
| RTE-16 | kept library plus verification metadata | supplied checker sees helper/context; stub performs no check | rejected fresh entries may survive dependencies without verified status; no universal gate |

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 and SRC-2, CLM-1, CLM-2 and CLM-3. Question: what Meta^n proposes, checks, admits and retains, and which kinds of later reliance those transitions warrant. Whole repository responsibilities are assessed; opaque external models/SDKs and unaudited upstream evaluators are bounded interfaces. No source-code test or reported score is promoted to an observed run.

#### 2. Epistemic-object overlay

OBJ-1 supplies task/evaluation scope and normative run settings. OBJ-2 contains a prescribed computation and may contain task claims or model explanations; these parts have different warrant. OBJ-3 is procedural guidance to generate interventions, not an automatically accepted theory of the task. Memory objects distinguish imported traces, generated rationale/code, selection metadata and transformed continuation context. Executable code is individually inspectable, but symbolic form does not establish that its mechanism or rationale is correct.

#### 3. Authority-route ledger

| route/function | architectural status | target/content relation | check or evaluator | epistemic license | operational authority and limits |
|---|---|---|---|---|---|
| RTE-1: operational admission/selection/consumption | implemented | OBJ-1; no content change | CLI/config checks at run start | valid selected configuration, not effective improvement | BAP-1 determines enabled machinery and task domain |
| RTE-2: content transformation | implemented | OBJ-2; indeterminate task-specific proposal | solver model | candidate code/prediction, no general warrant | executor may run it under configured grants |
| RTE-2: check/evidence production | implemented | OBJ-2; no content change | exit status and optional verification predicate | operational result under that predicate only | BAP-2 returns trace to evaluation |
| RTE-3: content transformation | implemented | OBJ-2; indeterminate revised task solution | model reads task/injections/feedback | candidate revision, not accepted explanation | another execution may follow |
| RTE-3: disposition/acceptance | implemented | OBJ-2; no content change | finite-score best selection, completion handshake and caps | selected task outcome, no universal proof of completion | BAP-2 returns current best and stops |
| RTE-4: operational admission/selection/consumption | implemented | OBJ-1 and OBJ-2; no content change | budget/lease/backend wrapper | no epistemic license from admission | starts or blocks external task execution |
| RTE-4: lineage/freshness/recovery | implemented | output trace/log; no content change | timeout/fault/cleanup machinery | recorded termination and recoverable metrics only | degraded return or cancellation; external effects uninspected |
| RTE-5: check/evidence production | implemented | OBJ-2; no content change | adapter-specific evaluator; classification gold labels | label accuracy/F1 or named task metric on supplied cases | feeds selection; upstream labels/objectives not validated here |
| RTE-5: content transformation | implemented | score aggregation; entailed derivation | finite-filter, median/mean arithmetic | arithmetic under its actual denominator and inputs | candidate scores and reports; no component attribution |

| RTE-6: operational admission/selection/consumption | implemented | OBJ-4, OBJ-5, OBJ-6; no content change | archive rank, ancestry/task IDs, failure-class and budget selectors | relevance/availability view, not truth endorsement | BAP-4 supplies chosen evidence and prior rationale to Omega |
| RTE-6: content transformation | implemented | OBJ-5; indeterminate proposed code/rationale | model under OBJ-3 | new intervention candidate; preservation/entailment/ampliation depend on actual content | prospective later solver organization |
| RTE-6: check/evidence production | implemented | proposed child; no content change | configured sampled gate and RTE-5 outcomes | sampled success/relative score within that domain | controls next admission; default consolidation omits gate |
| RTE-6: disposition/acceptance | implemented | candidate chain; no content change | nonempty/focus rules, optional gates, full evaluation | operational eligibility, not explanatory acceptance | admitted chain enters archive; later selection is separate |
| RTE-6: retention | implemented | OBJ-4, OBJ-5, OBJ-6; no content change | candidate persistence | source/outcome/rationale lineage | BAP-4 later generation; retention is not lifecycle integration |
| RTE-7: content transformation | implemented | OBJ-5 to guidance/code; non-truth-apt policy update | executed hook, name merge, formatting | instructions/computation, not validated theory | BAP-3 supplies solver context and executable code |
| RTE-7: check/evidence production | implemented | hook/library source; no content change | syntax/blocklist/interface/timeout domain | local eligibility only, not isolation or algorithm correctness | malformed pieces can be skipped |
| RTE-7: operational admission/selection/consumption | implemented | OBJ-5; no additional content change | accepted hook output/helper stage | no additional epistemic license | BAP-3 changes current solver context/runtime |
| RTE-8: operational admission/selection/consumption | implemented | OBJ-5; no content change | source-visible mapper/name/importability/staging | available helper/guidance, not execution proof | BAP-3 hands material to external backend |
| RTE-8: operational admission/selection/consumption | doctrine only | staged code; no content change | documented caller import/read interface | no observed dependence established | explicit pull afforded; SDK execution excluded |
| RTE-9: content transformation | implemented | OBJ-5; indeterminate corrective proposal | Omega receives rejected injection and failures | candidate code repair, diagnostic theory unverified | alternate layer proposed |
| RTE-9: disposition/acceptance | implemented | replacement chain; no content change | re-gate clears; later matched-subset score flag separate | gate-domain admission; no broad explanation license | new version retained without mutating rejected candidate |
| RTE-10: content transformation | implemented | OBJ-5; indeterminate intermediate-layer replacement | Omega receives full-chain evidence and compatibility guidance | proposed correction with confounded chain feedback | new chain evaluated |
| RTE-10: retention | implemented | new candidate/repair event; no content change | unconditional post-evaluation archive | record of attempted revision; score accepted flag not archive veto | later ranking decides use |
| RTE-11: content transformation | implemented | OBJ-7; indeterminate history summary | summarizer prompt, no content-preservation test | requested continuation fidelity, not guaranteed | replaces old message span |
| RTE-11: retention | implemented | OBJ-7; no additional content change | active message-list replacement | provenance to selected old messages | next model turn receives it, not post-acceptance integration |
| RTE-12: lineage/freshness/recovery | implemented | OBJ-9 and reconstructed objects; non-ampliative reconstruction | schema/depth/partial-file guards and recorded run selection | reconstructable saved state, not renewed correctness | search resumes or skips broken state |
| RTE-13: content transformation | implemented | OBJ-8; non-ampliative selection/assembly | stored task-best entries | selected recorded winners for named tasks | frozen outputs inherit scores without new comparison |
| RTE-13: operational admission/selection/consumption | implemented | OBJ-8; no content change | exact task match in native MetaLayer | prior task outcome only, no new generalization | BAP-3 routes stored program to native executor |
| RTE-14: content transformation | implemented | OBJ-10; acquisition/import | selected file and loader | imported code; upstream rationale/warrant unknown | becomes seed candidate library |
| RTE-15: content transformation | implemented | task solution; indeterminate revision | model receives code/errors/outcomes | candidate repair; no accepted causal diagnosis | another task execution and possible winner retention |
| RTE-15: disposition/acceptance | implemented | OBJ-2 and OBJ-4; no content change | finite/better-score comparison | selected observed-by-system score under evaluator | winner enters archive; no analysis-observed instance |
| RTE-16: check/evidence production | implemented | Python helper entry point; no content change | real supplied checker or explicit no-check stub | check-specific result, not universal verification | pass/fail available to filter |
| RTE-16: disposition/acceptance | implemented | library and verified-name set; non-truth-apt candidate policy update | keep/drop plus dependency closure | verified status only for particular checked names | BAP-5 governs later task-best eligibility; retained dependency may be unverified |

Each row inherits source anchors, timing, consumer/channel/horizon from its canonical route and authority records. CLM-1 concerns RTE-6, RTE-7, RTE-9 and RTE-10; CLM-2 concerns archive/frozen reuse RTE-6 and RTE-13; CLM-3 concerns RTE-16 and source-call attribution; CLM-4 bounds all memory efficacy claims. The mismatch/limit is recorded beside the relevant function: available code, archive retention and matched scores license different conclusions. Actual operation is unobserved here; `implemented` is not an observed-candidate status.

#### 4. Per-object lifecycle disposition

No lifecycle record for OBJ-1: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-1. No lifecycle record for OBJ-3: no candidate truth-apt output for this procedural instruction object; relevant direct-adaptation or update routes: integrated Omega generation. OBJ-2 is indeterminate: source architecture produces task-dependent prescriptions, predictions and possible explanations. Acquisition/reshaping/derivation/ampliative interpretation cannot be assigned to all model outputs as one class. RTE-2, RTE-3 and RTE-5 wire generation/checking/operational selection, but no instance-linked task candidate was observed here.

OBJ-4: acquisition/import of task execution observations and non-ampliative trace normalization via RTE-2, RTE-3, RTE-4 and RTE-5; discovery lifecycle not applicable to imported evidence. Embedded model reasoning may contain conjectures, but no instance was observed and its semantic production is uninspected. OBJ-5: code/rationale generation and repair on RTE-6, RTE-9 and RTE-10 are indeterminate between a restated known rule, derived implementation, and ampliative strategy/explanation. Source formats retain lineage, rationale and executable content; they do not determine which semantic class a future artifact occupies. Candidate-linked code/rationale and a stated challenged claim are needed before an ampliative lifecycle can be assigned. No instance observed.

OBJ-6: scores, lineage and indexes are entailed derivations within the supplied score/selection domain; discovery lifecycle not applicable to those computations. Imported traces keep their own warrant limits. OBJ-7: RTE-11 summary is indeterminate between faithful reshaping, omission and new interpretation. Its lineage and next-turn use are wired, but preservation, testing and epistemic acceptance are not established by the call; no instance observed. OBJ-8: RTE-13 task-map assembly is non-ampliative selection of prior output; discovery lifecycle not applicable; task-specific upstream warrant is preserved only at its prior evaluation scope. OBJ-9: RTE-12 checkpoint reconstruction is non-ampliative restoration, not a newly accepted claim. OBJ-10: RTE-14 seed import has unknown upstream warrant; discovery lifecycle not applicable to importing it. OBJ-11: diagnostic evidence acquisition only, with no independent later epistemic consumer established inside this scope.

No actual ampliative candidate instance was inspected. For any potential theory in generated OBJ-2, OBJ-5 and OBJ-7, observation and proposal call paths are implemented, but candidate-linked conjecture content, derived predictions, content-directed criticism, evidence-consuming epistemic acceptance and post-acceptance integration have architectural status not determinable at the semantic level and observed candidate state no instance observed. Operational evaluator checks and archive admission retain their implemented ledger status. They must not be relabeled theory acceptance or post-acceptance integration without identifying the candidate claim, criterion, intended use and resulting reliance.

#### 5. System-claim versus route comparison

| claim | doctrine/design and implementation | observed/causal support | bounded conclusion |
|---|---|---|---|
| CLM-1 | Omega generation, retained injection and recursive chain construction wired; higher-depth prompt template supplies role guidance | README reports lineage example; no primary run capsule inspected | constructive revision route supported; emergent role and recursive improvement efficacy remain uninspected |
| CLM-2 | archive retains best scores and supports frozen per-task reuse | prototype caveat and reported code-channel benefit only | monotonic retained score can follow selection among more draws; it does not isolate a better generating procedure |
| CLM-3 | real/stub verification branches, dependency retention and syntactic adoption proxy wired | no executed matched helper intervention | check scope and proxy distinguish retained capability from validated/causally effective use |

#### 6. Bounded conclusion

Meta^n makes model-proposed changes executable and exposes them to task evaluation and later selection. It retains source code and rationale that a later generator can inspect. The operational acceptance criteria are explicit but heterogeneous: code validity, task scores, sampled relative gate, held-out helper check where supplied, or frozen winner reuse. None licenses all explanations in a candidate or universal transfer. Rationale retention and performance feedback enable a theory-criticism interpretation only when a candidate-linked claim and a criticism of what it says can be identified; that instance evidence is not supplied here.

## Reconciliation

The specialist report is complete against the unchanged input and method hashes and the same source pin. Parent integration preserved its source-native scope, evidence strengths and fourteen-axis rationale. The epistemic lens is a local sparse overlay, not an independent duplicate clearance.

| specialist proposal | canonical record | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-4 | adopted at original scope/status |
| MEM-OBJ-2 | OBJ-5 | adopted at original scope/status |
| MEM-OBJ-3 | OBJ-6 | adopted at original scope/status |
| MEM-OBJ-4 | OBJ-7 | adopted at original scope/status |
| MEM-OBJ-5 | OBJ-8 | adopted at original scope/status |
| MEM-OBJ-6 | OBJ-9 | adopted at original scope/status |
| MEM-OBJ-7 | OBJ-10 | adopted at original scope/status |
| MEM-OBJ-8 | OBJ-11 | adopted at original scope/status |
| MEM-RTE-1 | RTE-6 | adopted at original scope/status |
| MEM-RTE-2 | RTE-7 | adopted at original scope/status |
| MEM-RTE-3 | RTE-8 | adopted at original scope/status |
| MEM-RTE-4 | RTE-9 | adopted at original scope/status |
| MEM-RTE-5 | RTE-10 | adopted at original scope/status |
| MEM-RTE-6 | RTE-11 | adopted at original scope/status |
| MEM-RTE-7 | RTE-12 | adopted at original scope/status |
| MEM-RTE-8 | RTE-13 | adopted at original scope/status |
| MEM-RTE-9 | RTE-14 | adopted at original scope/status |
| MEM-RTE-10 | RTE-15 | adopted at original scope/status |
| MEM-BAP-1 | BAP-3 | adopted at original scope/status |
| MEM-BAP-2 | BAP-4 | adopted at original scope/status |
| MEM-BAP-3 | BAP-5 | adopted at original scope/status |
| MEM-ABS-1 | ABS-1 | adopted at original scope/status |
| MEM-ABS-2 | CLM-4 | evidence gap retained as uninspected claim, not absence |
| MEM-ABS-3 | ABS-2 | adopted at original scope/status |

All nine integration issues are disposed: distinct trace/code/rationale/summary/checkpoint objects retained; OBJ-11 excluded from the operative form union; ten routes registered; RTE-15 annotates RTE-2 and RTE-3 repair subpaths rather than duplicating their generic execution; BAP-3, BAP-4 and BAP-5 retain separate forces; dependency/stub exceptions, default gate bypass and unconditional downward-repair archival preserved; ABS-2 bounds frozen-map dispatch; every summary contribution retained; faithfulness remains not determinable; no source/access correction was needed.

RTE-16 registers the distinct helper-admission mechanism previously described by the specialist's authority record, using the same checked source and exceptions. No new comparison value or stronger efficacy finding follows. The parent added explicit guidance/theory-status and return/horizon fields, and distinguished `accepted` score metadata from `archived` retention. The absence proposal about uninspected faithfulness evidence is mapped to CLM-4 because a gap does not establish an absence; its comparison uncertainty is unchanged. ABS-1 retains only the bounded store finding, with provider-weight uncertainty on CMP-2 and CMP-3. Source quotation excerpts are shortened where possible without changing meaning or report provenance.

There is no claim of independent convergence between later overlays. No substantive conflict was resolved by selecting a stronger status. Known memory unions exclude SDK-internal memory and opaque diagnostic-only payloads explicitly; normalized Trace text remains included. No previous target analysis supplied evidence.

## Bounded synthesis

Meta^n is a bounded experimental improvement plane around task solvers. Its distinctive contribution is a connected route from execution evidence to model-authored preprocessing/helpers, then into later solver behavior and renewed evaluation. It can retain alternative chains, reconstruct them after restart, replace a problematic layer, or assemble frozen per-task winners. The code channel can preserve computation beyond an individual model context, while rationale read-back makes some reasons available to subsequent Omega calls.

The default benchmark path matters: consolidation changes one focus task while preserving other task outputs, and archive maxima retain good historical draws. The resulting monotonic score is a property of retention/selection within that evaluated corpus. It is not itself evidence of improved generalization or a more capable proposal process. Optional held-out verification is benchmark-specific and does not cover every helper; task score and helper-call attribution remain separate measures.

The strongest supported improvement finding is a wired, feedback-responsive revision and reuse mechanism for the system's own solver organization. Reported empirical benefits remain claimed; achieved persistent capacity improvement at this frozen boundary is uninspected. Formulated theory generation and content-directed criticism are afforded through rationale/code plus failure evidence, but whether actual theories were held open to criticism and thereby improved capacity is uninspected. The trace-learning comparison classification is narrower and does not resolve that question.

Reflection conclusion status: wired. Retained descriptions of the system's prior injections, their rationale and their execution outcomes reach Omega; changed solver organization updates those records, and generated changes affect later solvers. This establishes an operational self-representation/revision path inside the declared boundary. A reflective theory builder additionally revising a self-theory of its theory-building organization is uninspected. Dispositional self-improvement conclusion status: wired for the configured feedback-driven mechanism, relative to benchmark score and the run/resume horizon. Occurrent self-improvement and achieved favorable improvement conclusion statuses: uninspected; no actual later operation was observed to depend on an update. Neither status is an autonomy grade or a causal efficacy finding.

For a research run, the practical distinction is between a better retained portfolio and a better solver-generation process. Meta^n implements both portfolio retention and mechanisms intended to change generation, but this source-only pass cannot measure their separate effects. Candidate-linked original/changed code, exact evaluator inputs, rationale/criticism records, matched sampling budgets and unseen-task outcomes would change that assessment. The current source also makes the execution boundary material: preprocessing can run on the host, and external spending controls operate at admission rather than enforcing every run's dollar limit.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | resolving evidence |
|---|---|---|---|---|
| no actual improvement run | CLM-1, CLM-2, CLM-3 and integrated revision routes | code/docs/test fixtures only | observed adoption, criticism, improved capacity or causal component benefit | candidate-linked artifacts and matched interventions |
| upstream oracle/SDK internals excluded | CMP-3, CMP-4, RTE-4, RTE-5 | repository interfaces, classification metric | complete context/isolation and independent benchmark validity | frozen SDK/evaluator/data evidence and deployment trace |
| mutable model routing | CMP-2, CMP-3 | configured endpoint/deployment names | immutable parameters or provider update behavior | provider version/weight evidence |
| profile-dependent admission | RTE-1 and integrated candidate/helper gates | default consolidation and optional alternatives | universal gate, universal helper verification or nonregression | profile-specific run provenance and all covered predicates |
| score selection/aggregation | RTE-3, RTE-5, CLM-2 | finite scores, reuse and maxima | universal optimality or causal learning from a rising reported score | matched-budget control and explicit task-denominator reporting |
| host callback and external spend limits | CMP-4, RTE-2, RTE-4 | static validation, thread/lease/admission controls | global sandbox, killed callback or exact spend bound | deployed isolation/metering evidence |

## Verification and blockers

### Semantic verification

Checked frozen source identity, source layers, report/input/method hashes, canonical IDs and source quote support. Runtime alternatives include custom/default benchmark profiles, all selected solver families, real/stub helper checks, native-only frozen-map dispatch, resume, and gate/consolidation/repair distinctions. Core parametric routing is distinct from inaccessible parameter identity or changes.

Memory scope includes OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9 and OBJ-10; diagnostic boundary object OBJ-11 and SDK-internal memory are excluded. Qualifying trace-fed writes all survive aggregation: RTE-6 multi-task/focus generation, RTE-9 within-layer repair, RTE-10 downward replacement, RTE-11 online per-task summary, RTE-13 task-keyed frozen solution reuse, and RTE-15 online solution repair with later archival. These collectively support tool traces/trajectories/session logs, cross-task plus per-task, staged plus online, and symbolic plus natural-language distilled content. Import RTE-14 and reconstruction RTE-12 are not independently mislabeled trace learning.

Automatic push selectors name consumer and selected retained parts: Omega receives weighted-parent/failure/ancestry/task-selected evidence, native/external solvers receive chain-selected code and guidance, native frozen replay matches task identity, active summary retains selected older messages, and resumed search restores its selected run. Helper source requests remain pull affordances; no identifier value was inferred solely from a stored label. Keyword-derived failure classes justify inferred-lexical alongside coarse/identifier. External internal selection is excluded rather than guessed.

Lineage/write agency concern in-system routes; unknown seed authoring is not assumed manual/authored. Curation distinguishes version evolution and salience from deletion/dedup; an old layer omitted from Omega can remain executable. BAP-5 and RTE-16 preserve dependency and stub limits. Each admitting route records proposal/decision/veto/recovery, guidance, oracle boundary and separate theory claims. Retention and operational acceptance are not post-acceptance epistemic integration. Wired reflection/dispositional improvement remain separate from unobserved actual efficacy and criticism-driven learning. Known comparison fields have canonical support; faithfulness stays not determinable. No semantic blocker remains.

### Deterministic validation

Exact target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-meta-n-01/result.md`. Validation result: `commonplace-validate --full` passed cleanly with no errors or warnings.

### Blockers

None.
