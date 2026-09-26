---
type: types/agentic-system-analysis-result.md
description: 'Complete code-grounded analysis of jaz-evals: execution, memory, revision and evidence limits at the
  frozen repository boundary.'
run-id: AAS-2026-09-26-jaz-evals-01
system: jaz-evals
run-date: '2026-09-26'
result-disposition: complete
target-class: workflow
boundary-kind: complete artifact, partial loop
reviewed-boundary: 83dc51ebbd02c9299890b6db93ddc773f07b74b9
analysis-cutoff: '2026-09-26'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: not-determinable
      basis: null
      note: ACE is advisory knowledge; generated JAZ prompts/tools can carry instruction and executable force; external
        Letta block and compaction consumers prevent a complete union.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    curation_operations:
      assessment: not-determinable
      basis: null
      note: ACE wires synthesis and near-duplicate merging; TTSI prescribes revision and withdrawal. Letta compaction
        and maintenance cannot be exhaustively classified here.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    distilled_form:
      assessment: not-determinable
      basis: null
      note: ACE can retain prose and code snippets; TTSI prescribes prompts and executable tools; handoff state
        may be opaque. Letta summary return is text but does not expose every later retained part.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      note: Static sources and reported diagnostics do not supply inspected execution evidence testing dependence
        on recalled content. Scores and search-count code do not establish it; no global negative is inferred.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    learning_scope:
      assessment: not-determinable
      basis: null
      note: ACE and TTSI support cross-task carry within one attempt; long-horizon handoffs may occur within or
        across tasks. External compaction retains an unresolved horizon; no project learning is established.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    learning_timing:
      assessment: not-determinable
      basis: null
      note: ACE updates between tasks during the queue; freeze_after adds a frozen evaluation tail. Handoff summaries
        are produced during execution. Exact external compaction/write timing remains outside inspected implementation.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    lineage:
      assessment: not-determinable
      basis: null
      note: Trace extraction and optional seed import are established; runtime-external memory derivations prevent
        a complete union.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-10
      values: []
    read_back_direction:
      assessment: known
      basis: afforded
      note: ACE automatically supplies accumulated playbook; documented solver roles request history search. Both
        controlled alternatives are established; pull depends on model action and external runtime interfaces.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values:
      - pull
      - push
    read_back_signal:
      assessment: not-determinable
      basis: null
      note: ACE whole-playbook push is coarse; handoff summaries involve model judgment and display budgets. Letta
        automatic history/compaction selection is external. Search query semantics concern pull and cannot fill
        this push-only axis.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    representational_form:
      assessment: not-determinable
      basis: null
      note: Visible prose, executable code and structural metadata coexist with opaque handed-off Python state and
        external Letta payloads; readable display is not the whole operative object.
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      values: []
    storage_substrate:
      assessment: not-determinable
      basis: null
      note: Files and in-memory objects are visible; Letta service persistence and optional search are included
        but external implementation prevents a complete substrate set.
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      values: []
    trace_learning:
      assessment: known
      basis: wired
      note: ACE automatically derives persisted playbook guidance from completed task trajectories and supplies
        it to later task solvers. This establishes existence without implying improvement or proving other routes
        complete.
      records:
      - RTE-6
      values:
      - 'yes'
    trace_source:
      assessment: not-determinable
      basis: null
      note: ACE task trajectories and prompt-prescribed history-derived summaries qualify; exact compaction inputs
        and opaque runtime histories prevent a complete source set.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      values: []
    write_agency:
      assessment: not-determinable
      basis: null
      note: Automatic writes are wired or afforded. Seed-file import permits externally authored material but does
        not identify all producer agencies; excluded runtime memory APIs remain unknown.
      records:
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-10
      values: []
  scope: Retained and use-modified histories, handoff state/summaries, generated prompts/tools, ACE playbooks and
    Letta memory/context exposed across JAZ, CodeAct subagent/per-task, ACE, Letta and smolagents adapters at the
    frozen commit. Includes later consumers and compaction boundaries; excludes static seed doctrine as memory and
    diagnostic-only logs except when ACE consumes trajectories. External implementation opacity is retained rather
    than silently removed.
---

# jaz-evals agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-evals-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/jaz-evals.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-evals-01/memory-report.md`
**Memory analysis report SHA-256:** f487b4bac9b673e0d4d5f77c295f21431332bbc35c7ad57ba77f649f144eaf4c

Run AAS-2026-09-26-jaz-evals-01 analyses jaz-evals at `83dc51ebbd02c9299890b6db93ddc773f07b74b9`, cutoff 2026-09-26. Coordinator model: GPT-6; exact runtime model identifier unavailable. Method: `kb/instructions/analyse-agentic-system/SKILL.md` and its mandatory memory/epistemic procedures. This analysis used primary sources, not prior reviews.

## Boundary and evidence

Evidence basis: pinned source code, prompts/configurations and shipped result tables inspected on 2026-09-26; code-grounded. Classification: workflow, specifically a benchmark execution and measurement workflow with model-dependent method adapters. Boundary kind: complete artifact, partial loop. It schedules attempts, constructs environment/tool surfaces, delegates execution to agent runtimes, scores tasks and retains measurements. It also implements the ACE adaptation loop and prompts JAZ-based optimization.

Included: tracked Python adapters, selected runner/measurement paths, prompt and configuration contracts, and reported table results. Excluded: dependency implementation inside JAZ, Letta, smolagents and benchmark Git submodules; remote model internals; downloadable task data and run archives; the paper and companion framework analysis. These exclusions prevent proving external isolation, task/oracle validity, exact reconstruction of the published runs, or candidate-level learning. A Gitlink pins a dependency reference but is not inspected dependency code. The ordinary operating mode is bounded benchmark queues and repeated experiments, not unrestricted production requests.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | Git | `https://github.com/jaz-lang/jaz-evals` | `83dc51ebbd02c9299890b6db93ddc773f07b74b9` | implementation | CLI, attempt runner, JAZ/CodeAct/ACE and external-runtime adapters, memory and feedback paths, selected table generation | `src/jaz_evals/cli.py`, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/env.py`, `src/jaz_evals/envs/appworld.py`, `src/jaz_evals/envs/stulife.py`, `src/jaz_evals/hooks.py`, `src/jaz_evals/harnesses/`, `scripts/build_appworld_table.py`, specialist canonical anchors | Dependency internals, downloaded data and raw traces excluded; no observed model run |
| SRC-2 | Git | `https://github.com/jaz-lang/jaz-evals` | `83dc51ebbd02c9299890b6db93ddc773f07b74b9` | doctrine/design | Shipped prompts/configuration and README | `prompts/ttsi/jaz.md`, `prompts/long_horizon/jaz.md`, `configs/appworld_jaz.yaml`, `configs/stulife_jaz.yaml`, `configs/appworld_ace_codeact_seed42_full.yaml`, `README.md` | Instructions demonstrate intended policy, not model compliance |
| SRC-3 | Git | `https://github.com/jaz-lang/jaz-evals` | `83dc51ebbd02c9299890b6db93ddc773f07b74b9` | reported operation | Generated score tables and recorded provenance caveats | `tables/appworld_results.tex:110-172`, `tables/stulife_results.tex:89-101`, `README.md:146-154` | Summary tables are not candidate-linked traces or independent causal replication |

Access root: `/home/zby/llm/commonplace/related-systems/jaz-lang--jaz-evals`. Source reads used commit-addressed Git blobs only. Internal code comments about historical runs remain reports, not observations by this analysis.

## Shared records

### Components

CMP-1 — CLI and evaluation runner, symbolic Python. Loads a method/environment configuration, allocates run/attempt identities and independent instances, captures provenance and aggregates attempt records. Status: wired. SRC-1 `src/jaz_evals/cli.py:39-48`, `src/jaz_evals/eval_harness.py:131-247`.

CMP-2 — Agent runtimes accessed through method adapters. JAZ, Letta and smolagents own their internal model/execution loops; jaz-evals owns the bindings, configuration and measurement surrounding them. The official AppWorld baseline has a separate shell launcher. Status: wired adapter boundaries; dependency behavior uninspected. SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:275-445`, `scripts/run_appworld_official_react.sh:1-20`; memory records cover other adapters.

CMP-3 — Solver and optimizer/reflector/curator LLMs, distributed-parametric services. Shipped JAZ AppWorld configuration names dated `openai/gpt-5.4-nano-2026-03-17` solver and `openai/gpt-5.4-2026-03-05` root; ACE uses the same dated larger model for reflection. Endpoint-name pinning is wired; exact weight identity and provider-side parameter changes are uninspected. These routes request inference rather than implement weight training. SRC-2 `configs/appworld_jaz.yaml:8-26`, `configs/appworld_ace_codeact_seed42_full.yaml:31-37`.

> model: openai/gpt-5.4-2026-03-05
> --- `configs/appworld_jaz.yaml` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

CMP-4 — ACE sentence-transformer encoder for duplicate selection, distributed-parametric. Parameter updating is not part of the inspected encode route; it loads a model-name-resolved encoder and calls encode on bullet contents. Exact model revision is not pinned in that call. Provider/model-hub internals remain uninspected. Status: wired load/encode, uninspected weight provenance. SRC-1 `src/jaz_evals/harnesses/ace_dedup.py:306-315`; SRC-2 `README.md:74-77`.

> encoder = _ENCODERS[embedding_model] = SentenceTransformer(embedding_model, device="cpu")
> --- `src/jaz_evals/harnesses/ace_dedup.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

### Operative objects

OBJ-1 — EvalConfig, prompt text, task instructions and scoped tools. YAML/text and Python objects held by the runner/adapter. Static configuration is doctrine; it is not automatically memory accumulated through use. Status: wired assembly. SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:285-422`; SRC-2 `configs/appworld_jaz.yaml`, `configs/stulife_jaz.yaml`.

OBJ-2 — Task answers and environment state under evaluation. Python values and externally maintained benchmark state; the solver produces answers/actions, while the benchmark adapter controls task selection and submission. Status: wired interface, external world internals uninspected. SRC-1 `src/jaz_evals/envs/appworld.py:907-1003`, `src/jaz_evals/envs/stulife.py:823-952`.

OBJ-3 — Task feedback, attempt records and reported aggregate tables. Structured pass/fail, partial scores, failures and costs; JSON/JSONL files and LaTeX reports. Their retention is measurement, and becomes agent memory only on the later-consumer routes below. Status: wired production; published numeric outcomes claimed as reported operation. SRC-1 `src/jaz_evals/eval_harness.py:174-195,238-246`, `scripts/build_appworld_table.py:284-304`; SRC-3 score tables.

OBJ-4 — Attempt isolation key. Symbolic random identifier, in memory and used for external namespaces/workspaces. It separates attempt storage identities; it is not an OS sandbox or knowledge object. SRC-1 `src/jaz_evals/isolation.py:47-63`. Status: wired.

> return cls(key=secrets.token_hex(_KEY_BYTES), root=Path(root).resolve())
> --- `src/jaz_evals/isolation.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

OBJ-5 — JAZ history and continuation state

Evidence: SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:349-422` wires one root invoke for the entire environment workload. SRC-2 `configs/stulife_jaz.yaml:17-47` prescribes concatenating `prev_history` with `__history__`, handing arbitrary `state` plus a prose progress summary and next steps to the child. Histories are raw interaction records; the summary is derived guidance; state is an opaque Python payload whose display cannot determine its representation. Storage is runtime memory; no automatic restoration from persisted run traces is shown. Retention across delegated invocations is afforded, not observed. Consumer authority is evidence for history, instruction for next steps, and unspecified for arbitrary state.

>                 prev_history=globals().get("prev_history", []) + __history__,
>                 # Hand over any state you've been tracking
>                 state=...,
>                 # Summarize what has been done and what remains (hard-coded string)
>                 prev_progress_summary="So far, ...",
>                 # Tell the subagent what the next steps are (hard-coded string)
>                 next_steps="Your next step is to ...",
> --- `configs/stulife_jaz.yaml` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

OBJ-6 — CodeAct and smolagents authored output history

Evidence: SRC-1 `src/jaz_evals/hooks.py:294-312` removes the core `__history__` binding on the first iteration. SRC-2 `prompts/long_horizon/jaz_codeact_subagents.md:1-18` and `prompts/long_horizon/smolagents.md:1-31` instruct the model to maintain string outputs. The latter's wrapper retains the full list in `_obj` while limiting its display; its arbitrary `state` remains separate and opaque. This is an agent-maintained runtime object, not a harness-enforced complete log. Model omission can lose information. SRC-2 `configs/stulife_smolagents.yaml:41-72,84-85` specifies the wrapper and 50,000-character display suffix.

>         # rather than core's. `iteration` is per-invoke, so a nested invoke re-arms at its own 0.
>         if event.iteration != 0:
>             return []
>         effects: list[Any] = [DropVariables({_REPL_HISTORY_NAME})]
>         # `allow_missing=True` for these two but NOT for `__history__`: a missing `__history__` means
>         # the REPL keeps no history and the section guard above would already have aborted, so a
>         # miss there is drift worth failing on. An input or scoped name may legitimately have been
>         # unbound by another hook first, where withholding an absent binding is a harmless no-op.
> --- `src/jaz_evals/hooks.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>       class Wrapped:
>           def __init__(self, obj):
>               self._obj = obj
> 
>           def unwrap(self):
>               return self._obj
> 
>           def __repr__(self):
>               return str(self._obj)[-{max_chars}:]
> --- `configs/stulife_smolagents.yaml` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

OBJ-7 — ACE playbook and provenance sidecars

Evidence: SRC-1 `src/jaz_evals/harnesses/ace.py:581-596,773-783,870-893` retains an in-memory playbook, per-task snapshots, final text and call records. `src/jaz_evals/harnesses/ace_playbook.py:63-80,307-322,350-366` encodes numbered section bullets with counters; new counters are zero and hidden in model-facing copies. Bullet IDs and counters are access/format metadata, not evidence of effectiveness. Prose guidance may contain code snippets; the section for code does not establish that any particular generated bullet contains executable content. The playbook is advisory knowledge at the solver, despite a section named “Strategies and Hard Rules.” Reflection/curator reasoning is retained in call sidecars, not automatically preserved in each bullet or subsequently supplied as its provenance. Raw session trajectories remain distinct from this derived artifact.

> You have a playbook of accumulated guidance from earlier tasks. It is advisory, not authoritative: \
> follow it where it applies, and ignore any bullet that does not fit the task in front of you.
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>     def _write_playbook(self, ace_dir: Path, playbook: str, index: int) -> None:
>         """Snapshot the playbook after task `index`, with its bullet counts beside it."""
>         (ace_dir / f"playbook_after_task_{index}.txt").write_text(playbook)
>         _append_jsonl(ace_dir / "playbook_stats.jsonl", {"task": index, **playbook_stats(playbook)})
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

OBJ-8 — Letta messages, core blocks, archival/search state and summaries

Evidence: SRC-1 `src/jaz_evals/harnesses/letta_harness.py:1345-1376` creates one service agent with human/persona blocks and base tools. The initial blocks are static input, excluded as accumulated memory until modified through use. Messages and modified blocks/archive entries are service memory, not the exported diagnostic JSONL. SRC-2 `prompts/long_horizon/letta.md:1-24` names the solver's `conversation_search` interface. The optional embedding-backed message index and SQL fallback are documented and configured at `src/jaz_evals/harnesses/letta_harness.py:992-1016`, but their implementations are excluded. Compaction is intercepted, not implemented in full, at `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py:18-75`. The patch returns summary text; its persistence and later context assembly remain outside the frozen source. The container database is intentionally ephemeral at teardown, while diagnostic logs survive. Remote index deletion/persistence is not determined by container teardown.

>             include_base_tools=self.agent_type == "letta_v1_agent",
>             memory_blocks=[
>                 {"label": "human", "value": self.human},
>                 {"label": "persona", "value": self.persona},
>             ],
> --- `src/jaz_evals/harnesses/letta_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>         if response.choices[0].message.content is None:
>             raise Exception("Summary failed to generate")
>         return response.choices[0].message.content.strip()
> 
> --- `src/jaz_evals/harnesses/letta_patches/instrument_compaction.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>         finally:
>             # Both of these MUST happen before teardown, on the error path as much as the happy one: the
>             # container's DB is ephemeral, so whatever is not drained here is destroyed with it.
>             # `_reconcile` settles the last turn's still-in-flight run -- usage that exists *only*
> --- `src/jaz_evals/harnesses/letta_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

OBJ-9 — TTSI generated prompt/tool package

Evidence: SRC-2 `prompts/ttsi/jaz.md:1-11,31-61,72-83` asks a meta-agent to use returned task traces and grading results to revise prompts and tools, validate on later batches, and remove ineffective changes. `prompts/ttsi/jaz_codeact_subagents.md:66-72` asks CodeAct workers to explicitly return code/output/exception history instead of relying on magic history. Generated prose instructions and executable tools can shape later task workers; their actual produced contents and persistence are not available. A declared hypothesis may stay in root context, but the prompt does not require a durable rationale field attached to each retained tool/prompt revision.

> Every change you make should be tested rigorously.
Quoted policy retained on OBJ-9; the rigorous-test requirement is doctrine only.

### Routes

RTE-1 — Attempt scheduling and measurement. Trigger: CLI configuration/run ID or direct run_attempt. Owner: deterministic runner. It allocates a new isolation key, constructs environment and harness, exposes AgentEnv, executes the selected method, closes the harness and grades the environment even after a recorded execution error. KeyboardInterrupt propagates; failure of aggregate Env.grade propagates. Per-attempt records survive before aggregate completion; the aggregate appears after all attempts finish. Immediate output: AttemptRecord and CLI status; later consumer: analysis/table generation, not automatic solver reuse. Selection: configured method/environment and attempt count. Delegated visibility: adapter-specific; no cross-attempt sharing is promised beyond named stores. No artifact expiry/rollback policy is established. Status: wired. SRC-1 `src/jaz_evals/eval_harness.py:131-247`.

> grade = env.grade()
> analysis = _write_analysis(env, artifacts)
> --- `src/jaz_evals/eval_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> _write_json(artifacts / "results.json", record.to_dict())
> --- `src/jaz_evals/eval_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-2 — Queue-level JAZ invocation and tool routing. The host adapter selects models, hooks and root/scoped tool bindings; the model selects code, delegates, sequences tasks and may revise prompts/tools. Root-only tools are ordinary local inputs; shared tools use jaz.scope. The finish validator rejects return while the environment still has work, either at root or tree scope. AppWorld uses bounded solver delegation and root finish control; StuLife uses tree-wide control for self-delegation. Immediate output: RunReport and environment effects; later history/learned-context routes below govern read-back. Root-only marking prevents automatic propagation, not deliberate passing by a root holding the binding. Guarantee: sequencing protocol at the configured entry surface, requiring JAZ's hook and scope contracts. Status: wired. SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:275-445,593-618`, `src/jaz_evals/env.py:70-84`; SRC-2 `configs/stulife_jaz.yaml:7-46`.

> stack.enter_context(jaz.scope(**scoped))
> --- `src/jaz_evals/harnesses/jaz_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> return ValidateReturn(lambda ret: _reject_early_return(env, ret), max_failures=None)
> --- `src/jaz_evals/harnesses/jaz_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-3 — AppWorld submission, outcome evidence and feedback delivery. The root submits an answer, adapter calls the external world evaluator, records the result, closes the task and advances the cursor. Feedback returned to the agent includes assertion outcomes and potentially actual/expected details, except task identifiers. Answer oracle: benchmark-authored expected outcomes and assertions supplied by AppWorld; their correctness is outside the inspected boundary. A grader crash becomes an explicit error task with success false, distinct from aggregate grade failure. Admission of improved prompts/tools is not performed here: the returned outcome is evidence for another owner to interpret. Consumer/horizon: optimizer or ACE reflector on later tasks in the same attempt. Submission is final rather than rollback. Status: wired. SRC-1 `src/jaz_evals/envs/appworld.py:942-1003,1093-1108`.

> result = {"task_index": self._index, "task_id": self._task_id, **self._evaluate()}
> --- `src/jaz_evals/envs/appworld.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> return {k: v for k, v in result.items() if k not in ("task_index", "task_id")} | {
>     "tasks_remaining": remaining,
>     "next_step": _NEXT_STEP if remaining else _SENTINEL,
> }
> --- `src/jaz_evals/envs/appworld.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-4 — StuLife grading with correctness withheld from the agent. Trigger: complete_task. Deterministic adapter checks task state, scores quizzes against supplied ground_truth or invokes task evaluators, writes result rows, then advances. Agent-facing response carries remaining work and next-step instructions; correctness remains in evaluation records. Oracle: benchmark dataset answers and expected world state, not model judgment. Immediate output to solver is sequencing feedback; later correctness consumer is offline analysis. Model error recovery can correct an invalid answer shape before submission; a valid final answer is not reopened by this route. Trigger tasks and action tasks have distinct handling; the adapter refuses unacted non-quiz work in agent mode. Status: wired at adapter boundary, underlying data/evaluators uninspected. SRC-1 `src/jaz_evals/envs/stulife.py:823-952`.

> if submitted == correct:
>     return 1.0, f"correct answer: {correct}"
> return 0.0, f"wrong answer: submitted {submitted!r}, correct {correct!r}"
> --- `src/jaz_evals/envs/stulife.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> response: dict[str, Any] = {"tasks_remaining": tasks_remaining}
> --- `src/jaz_evals/envs/stulife.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-5 — Measurement derivation and report publication. Trigger: analysis/table script over retained run artifacts. Owner: deterministic Python plus human-selected manifests. Task-goal completion counts success rows; scenario completion requires every variant; cost reads recorded accounting. Table generation refuses missing ordinary arm data rather than inventing it; official-baseline fallback is separately documented by the source. Immediate output: report bytes; consumer: researcher/reader. No automatic deployment, memory admission or learned successor selection follows from a higher score. Selection: manifest globs; expiry: none established. Recovery: fix unavailable artifacts and regenerate. Status: wired computation, claimed published outputs. SRC-1 `scripts/build_appworld_table.py:182-200,284-304,720-764`; SRC-3 table/provenance reports.

> return 100 * sum(1 for r in results if r["success"]) / len(results)
> --- `scripts/build_appworld_table.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-6 — ACE trace extraction, maintenance and automatic next-task delivery

Implementation conclusion status: wired. Producer is the reflector then curator; input is one finished or failed task's recorded trajectory, task text, environment feedback, exception and current playbook. Trigger is after `complete_task`, while adaptation is enabled. SRC-1 `src/jaz_evals/harnesses/ace.py:486-550,611-698` wires a fresh session, adaptation and snapshot before advancing. The trace is capped at 400,000 characters from its head; task text caps are 2,000 for reflection and 1,000 for curation (`src/jaz_evals/harnesses/ace.py:74-79,870-879`). Missing traces become a literal marker, not a blocked adaptation. Output is parsed JSON ADD operations, validated by section and shape, appended as bullets and optionally deduplicated. A malformed reply preserves the preceding playbook; an unknown section drops only that operation; thrown adaptation failures also preserve its last good state. These checks establish structural admissibility, not truth. The complete inspected admission boundary is SRC-1 `src/jaz_evals/harnesses/ace_playbook.py:470-518` and `src/jaz_evals/harnesses/ace.py:677-699`; it checks JSON fields, operation kind and section membership before applying content.

>         if typed["type"] != "ADD":
>             raise ValueError(f"curator operation {index} has type {typed['type']!r}; only 'ADD' is supported")
>         missing = {"type", "section", "content"} - set(typed)
>         if missing:
>             raise ValueError(f"curator ADD operation {index} is missing {sorted(missing)}")
>         section = str(typed["section"])
>         if normalize_section(section) not in ALLOWED_SECTIONS:
>             if on_unknown_section is not None:
>                 on_unknown_section(section)
>             continue
>         kept.append(typed)
>     return kept
> --- `src/jaz_evals/harnesses/ace_playbook.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`


>         reflection, _cost = reflect(
>             _render(
>                 _REFLECTOR_PROMPT,
>                 question=task[:_REFLECTOR_QUESTION_CHARS],
>                 environment_feedback=feedback,
>                 execution_error=execution_error,
>                 playbook=strip_counts(playbook),
>                 trajectory=trajectory,
>                 spec_or_interface=spec_or_interface,
>             ),
>             "reflector",
>             index,
>         )
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> 
>         playbook, next_id = apply_add_operations(playbook, operations, next_id)
>         if deduplicate is not None:
>             playbook = deduplicate(playbook, index)
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>         prompt = _render(_SUBAGENT_PROMPT, instructions=instructions, playbook=strip_counts(playbook))
>         inputs: dict[str, Any] = {"instructions": prompt, _TASK_INPUT: task}
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

The consumer is each later fresh solver; a task-start automatic selector supplies the whole current count-stripped playbook in its instructions. This is coarse push, with no per-task relevance retrieval. The reflector and curator also receive the whole stripped playbook. IDs in the document do not create identifier-targeted push. `freeze_after` stops writes but leaves read-back active; the shipped AppWorld arm uses 42 adapting tasks and a frozen tail, with a 200,000-character invoke input limit (SRC-2 `configs/appworld_ace_codeact_seed42_full.yaml:20-22,33-42`). The cap is passed to external JAZ rendering; exact overflow behavior is uninspected. Cross-task adaptation within an attempt is wired; there is no demonstrated improvement.

Optional dedup embeds every bullet, greedily groups by cosine similarity and asks a model to combine each group (SRC-1 `src/jaz_evals/harnesses/ace_dedup.py:154-162,216-260`). This is dedup plus consolidation of retained advice, while initial reflection/curation affords synthesis of new claims. No semantic correctness test protects a parseable merge. An unparseable merge keeps its group. Groups can overlap because visited status excludes leaders but not later members, so the implementation can duplicate content into multiple survivors. The complete document is re-embedded; there is no persistent retrieval vector index here. Quadratic pairwise comparison and one model call per similar group can become the maintenance cost. Reflector/curator/dedup calls bypass the session BudgetPool; their spend is logged but not bounded by that session budget (`src/jaz_evals/harnesses/ace.py:730-755`).

>             # "Outside any agent loop" is also the budget caveat, and it is a big one: this is a direct
>             # backend call, so it passes through no hook dispatcher and `BudgetPool` -- which books cost
>             # off `LLMQueryExit` inside an invoke -- neither counts nor caps it. A config's `cost_budget`
>             # therefore bounds the sessions only, while ACE's own ledger runs uncapped beside it. That
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>             response = client.complete_with_retry(
>                 self._reflector_model, [{"role": "user", "content": prompt}], **kwargs
>             )
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

The direct backend call confirms the nearby budget explanation at the implementation boundary. Dedup admission similarly parses a formatted bullet and accepts its content without a semantic test in the inspected `src/jaz_evals/harnesses/ace_dedup.py:198-211,246-253` path:

>     # as a successful merge. Keeping the group is the real pre-dedup state.
>     match = _MERGED_BULLET.match(text.strip())
>     if match is None:
>         return None
> --- `src/jaz_evals/harnesses/ace_dedup.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`


>     for i in range(len(embeddings)):
>         if i in visited:
>             continue
>         similar = [j for j in range(i + 1, len(embeddings)) if similarity(i, j) >= threshold]
>         if similar:
>             group = [i, *similar]
>             groups.append(group)
>             visited.update(group)
>     return groups
> --- `src/jaz_evals/harnesses/ace_dedup.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>             merged = parse_merged(merge(merge_prompt(members)))
>             if merged is None:
>                 # The group survives intact. A merge the model would not write is not evidence that
>                 # the bullets are redundant, and the dedup pass runs again after the next task.
>                 failed += 1
>                 continue
>             replacement[group[0]] = merged
> --- `src/jaz_evals/harnesses/ace_dedup.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-7 — Long-horizon handoff and requested recall

Implementation conclusion status: afforded. SRC-2 `configs/stulife_jaz.yaml:17-47`, `configs/stulife_jaz_codeact_subagents.yaml:21-49` and `configs/stulife_smolagents.yaml:20-75` prescribe warning-triggered child delegation with accumulated histories, state, a progress summary and next steps. SRC-1 `src/jaz_evals/harnesses/smolagents_harness.py:1278-1292,1560-1624` wires the warning from measured input-token usage into observations and constructs managed children. At the configured 0.7 window fraction the automatic action is cue delivery, not guaranteed summary creation or delegation. The JAZ ContextWindowWarning implementation is external, though its configuration and hook construction are local.

At handoff the manager selects retained material and supplies summary/state/history to the next consumer: an afforded push route. The prescribed display truncation is a budget filter, not targeted retrieval. The child can then ask through Python history search for concrete terms and receive a context window around a hit: pull, performed by the named solver role through its REPL. Search result printing is fulfillment of the request, not a separate push. The prompt forbids recording search results back into output history to reduce recursive pollution. SRC-2 `prompts/long_horizon/jaz.md:14-35`, `prompts/long_horizon/jaz_codeact_subagents.md:33-51` and `prompts/long_horizon/smolagents.md:43-63` specify this route. Trace-fed summaries retained as child inputs would qualify as learning, independent of novelty, but production/compliance is not observed. They can bridge context windows within a task and retain prior-task material across the episode; a session ID alone is not the scope argument.

>         if pos >= 0:
>             # Display a window around the search target
>             start = max(0, pos - 1000)
>             end = min(len(repl_output), pos + 2000)
>             print(f"--- entry[{i}] (pos {pos}) ---")
>             print(repl_output[start:end])
>             print()
>     # STOP HERE: do NOT write any code after `prev_history` search — WAIT for the next turn to act on the search results
> --- `prompts/long_horizon/jaz.md` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-8 — TTSI batch revision and later worker use

Implementation conclusion status: afforded. The whole-queue root receives the TTSI prompt and single-task text; nested runtime calls can receive root-authored prompts/tools. SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:349-422` supplies those surfaces, and SRC-2 `prompts/ttsi/jaz.md:1-11,63-83` instructs the root to request histories, diagnose failures, derive general changes and validate on subsequent task batches. The CodeAct version substitutes manually returned histories. This is an afforded automatic trace-fed transformation into behavior-shaping prose and code, with cross-task scope inside one run. Later delivery is manager-selected push. Root inspection of returned worker history is also requested evidence delivery. Consolidation, synthesis, revision and withdrawal are prescribed rather than guaranteed. No code gate forces the proposed evidence standard, and no inspected run establishes that a hypothesis or its reasons survived into the next revision.

RTE-9 — Letta task delivery, search and external compaction

Implementation conclusion status: afforded. Task delivery itself is wired: SRC-1 `src/jaz_evals/harnesses/letta_harness.py:1458-1476` repeatedly sends task text as user messages to the same agent. With `deliver_task_tool`, task fetch is withheld from the model and the driver injects tasks into searchable conversation, addressing the documented claim that tool-return messages are excluded from search (`src/jaz_evals/harnesses/letta_harness.py:1114-1125`). That exclusion is a local source claim about external Letta, not independently inspected implementation. SRC-2 `prompts/long_horizon/letta.md:1-24` identifies the consuming solver and requested search interface, supporting pull affordance. Archival memory and core-block mutation are named service capabilities but their exact calls and maintenance are not reconstructed from generic base-tool inclusion.

Compaction must not disappear from the account: the mounted patch intercepts summarizer input and returns stripped summary text, while logging cost. The adapter never shows the summary's storage, replacement policy, preserved rationale, automatic history selector or later context consumer. Thus a likely trace-fed continuation route is explicitly unresolved, not classified as “no learning.” Letta's same-agent queue establishes cross-task message accumulation, not the scope of each compaction or archival derivation. Optional semantic message indexing affects requested retrieval, not this report's push-signal axis.

>                 response = client.agents.messages.create(
>                     agent_id=agent_id, messages=[{"role": "user", "content": message}], timeout=3600.0
>                 )
> --- `src/jaz_evals/harnesses/letta_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> Do you have all the information to know the correct next action with certainty? If not, then
> *search for it*. Your conversation history contains everything said earlier in this session, which
> scrolls out of your context window as the run goes on. To recall information from earlier in the
> session, *search for this information with `conversation_search`*.
> --- `prompts/long_horizon/letta.md` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

RTE-10 — ACE configured seed import across attempts

Implementation conclusion status: wired. SRC-1 `src/jaz_evals/harnesses/ace.py:881-888` reads the configured seed path or starts from empty sections. A prior run's final playbook or an edited file can therefore be explicitly imported into a new attempt, but no automatic discovery or cross-run learning service is shown. The file's authorship/trust is not validated; a missing path fails loudly. This is an operator-controlled adoption surface, not evidence that a human edited or approved any generated bullet. The seed then follows RTE-6.

>     def _load_initial_playbook(self) -> str:
>         """The playbook to start from: a seed file if configured, else empty sections."""
>         if self._initial_playbook:
>             seed = Path(self._initial_playbook)
>             if seed.is_file():
>                 return seed.read_text()
>             raise ValueError(f"initial_playbook {self._initial_playbook!r} does not exist")
>         return empty_playbook()
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

### Claims

CLM-1 — Reproduction package for ten arms across two benchmarks. Status: claimed, with runner/adapter wiring supporting the package role. Exact historical reproducibility is bounded: source reports four development commits, mostly dirty worktrees, and unavailable commits; the installable release is a closest approximation. SRC-2 `README.md:3-16`; SRC-3 `README.md:146-154`.

> `0.2.0a4` is the earliest published release that contains the
> code those runs ran, so it is the closest version anyone can actually install, not the literal one.
> --- `README.md` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

CLM-2 — Reported improvement-capable JAZ configuration outcomes: AppWorld task completion 74.2 ± 2.1 versus CodeAct+subagents 71.1 ± 1.3 and ACE 69.9 ± 1.4; StuLife far-recall pass 69.9 ± 1.8 versus Letta 61.8 ± 2.3. These are claimed summary outcomes, not observed candidate histories in this analysis. The AppWorld table explicitly reports insufficient repetitions to separate the top two arms. Comparisons concern bundled methods, including different adaptation schedules; they do not isolate a criticism step, memory representation or history exposure alone. SRC-3 `tables/appworld_results.tex:140-172`, `tables/stulife_results.tex:94-101`.

> %   - n=6 per arm is too few to separate the top arms: JAZ invoke vs CodeAct+subagents is t = 1.26
> %     (df=10) on TGC, not significant.
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> CodeAct+subagents\textsubscript{\oursimpl{}} & \checkmark & \underline{71.1} $\pm$ 1.3 & \underline{47.6} $\pm$ 2.1 & 21.6 $\pm$ 1.8 & \textbf{7.3} $\pm$ 1.7 & 14.3 $\pm$ 0.9 \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> ACE \citep{zhang2025ace} on CodeAct\textsubscript{\oursimpl{}} & \xmark & 69.9 $\pm$ 1.4 & 47.1 $\pm$ 1.3 & 30.6 $\pm$ 0.5 & 17.1 $\pm$ 0.3 & 13.5 $\pm$ 0.3 \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> \oursimpl{} \lstinline|invoke| & \checkmark & \textbf{74.2} $\pm$ 2.1 & \textbf{51.1} $\pm$ 3.7 & 20.9 $\pm$ 3.7 & \underline{9.9} $\pm$ 3.8 & \underline{10.9} $\pm$ 0.6 \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>  & mean & 71.1$^{\pm1.3}$ & 47.6$^{\pm2.1}$ & 21.6$^{\pm1.8}$ & 7.3$^{\pm1.7}$ & 14.3$^{\pm0.9}$ \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>  & mean & 69.9$^{\pm1.4}$ & 47.1$^{\pm1.3}$ & 30.6$^{\pm0.5}$ & 17.1$^{\pm0.3}$ & 13.5$^{\pm0.3}$ \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>  & mean & 74.2$^{\pm2.1}$ & 51.1$^{\pm3.7}$ & 20.9$^{\pm3.7}$ & 9.9$^{\pm3.8}$ & 10.9$^{\pm0.6}$ \\
> --- `tables/appworld_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> Letta Agent \citep{packer2023memgpt} & \xmark & \underline{70.9} $\pm$ 0.5 & \underline{81.0} $\pm$ 0.5 & \underline{61.8} $\pm$ 2.3 & \underline{67.0} $\pm$ 2.4 & 42.1 $\pm$ 1.6 \\
> --- `tables/stulife_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> \oursimpl{} \lstinline|invoke| & \checkmark & \textbf{72.6} $\pm$ 0.1 & \textbf{81.6} $\pm$ 0.1 & \textbf{69.9} $\pm$ 1.8 & \textbf{73.6} $\pm$ 1.5 & 18.3 $\pm$ 0.3 \\
> --- `tables/stulife_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>  & mean & 70.9$^{\pm0.5}$ & 81.0$^{\pm0.5}$ & 61.8$^{\pm2.3}$ & 67.0$^{\pm2.4}$ & 42.1$^{\pm1.6}$ \\
> --- `tables/stulife_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>  & mean & 72.6$^{\pm0.1}$ & 81.6$^{\pm0.1}$ & 69.9$^{\pm1.8}$ & 73.6$^{\pm1.5}$ & 18.3$^{\pm0.3}$ \\
> --- `tables/stulife_results.tex` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

CLM-3 — Prompt-directed rigorous hypothesis testing in JAZ task-sequence optimization. Status: claimed policy; implementation affords prompt/tool changes and feedback, but does not enforce the prose's causal testing or discard rule. SRC-2 `prompts/ttsi/jaz.md:34-81`.

Quoted policy retained on OBJ-9; the rigorous-test requirement is doctrine only.

### Evidenced absences

No broad absence finding is inferred from excluded dependency code or missing traces. 

ABS-1 — Per-task branch lacks a local cross-task memory feed

Conclusion status: absent. Within SRC-1 `src/jaz_evals/harnesses/jaz_per_task.py:187-243,276-277,316-353,357-379`, each task receives a fresh invocation and fresh hooks; combined traces are produced afterward for diagnostics, not supplied to the next task solver. This bounds the negative to the harness's agent memory feed; environment state is separate and dependencies remain excluded. SRC-1 `src/jaz_evals/eval_harness.py:145-161` constructs a fresh isolation, environment and harness per attempt. Ordinary attempts therefore do not rehydrate prior runtime state; explicit ACE seed import is the identified exception at the adapter level.

The exact negative search boundary was the full frozen `src/jaz_evals/harnesses/jaz_per_task.py` blob, queried with `git --no-replace-objects -C related-systems/jaz-lang--jaz-evals grep -n -E 'invoke|_inputs|history|memory|trace|read_text|load|resume|checkpoint' 83dc51ebbd02c9299890b6db93ddc773f07b74b9 -- src/jaz_evals/harnesses/jaz_per_task.py`. Each invocation/input and trace-read match was followed: the loop uses fresh task hooks and `_inputs`; `_inputs` enumerates only instructions, current task and optional domain guidance; trace reads occur in post-loop combination. This combination of positive call/input enumeration and bounded search supports the absence of a local cross-task agent-memory feed, not an absence inside external dependencies or environment state.

>         inputs: dict[str, Any] = {
>             "instructions": env.get_single_task_instructions() or env.get_instructions(),
>             _TASK_INPUT: task,
>         }
>         guidance = self.domain_prompt()
>         if guidance is not None:
>             inputs["guidance"] = guidance
>         return inputs
> --- `src/jaz_evals/harnesses/jaz_per_task.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`


>                     try:
>                         with ExitStack() as task_stack:
>                             for hook in task_hooks:
>                                 task_stack.enter_context(hook)
>                             answer = jaz.invoke(**self._inputs(env, task))
> --- `src/jaz_evals/harnesses/jaz_per_task.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

>     isolation = Isolation.new(root)
>     artifacts = attempt_dir(root, config, run_id, attempt)
> 
>     env = _build_env(config)
>     # Before `setup()`, which is where an env names its results sink and any external state it scopes
> --- `src/jaz_evals/eval_harness.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

### Behavioral-authority paths

BAP-1 — Root agent and solver consume OBJ-1 as prompt inputs, callable bindings and scoped tools. Instructions advise; bindings permit effects; finish validation enforces queue completion at the chosen scope. Horizon: attempt/invoke tree. RTE-2, SRC-1 `src/jaz_evals/harnesses/jaz_harness.py:307-422`.

BAP-2 — AppWorld feedback reaches the optimizer/reflector through complete_task return values; it informs adaptation but does not itself enforce a particular revision. Benchmark evaluator grants only task-outcome authority over its tests. Horizon: following tasks in that attempt. RTE-3, SRC-1 `src/jaz_evals/envs/appworld.py:942-1003`.

BAP-3 — Evaluation records and tables inform the researcher through files; StuLife correctness is not delivered through its completion response to the solver. Reporting carries evidential, not executable, authority. RTE-4, RTE-5, SRC-1 `src/jaz_evals/envs/stulife.py:914-951`, `scripts/build_appworld_table.py:284-304`.

BAP-4 — Later ACE solvers consume the whole playbook as advisory guidance during an attempt; structural admission supplies no truth warrant. JAZ handoff summaries/prompts instruct later delegates, and generated tools can execute actions. Letta search supplies requested evidence while its internal compaction consumer remains uninspected. RTE-6, RTE-7, RTE-8, RTE-9; their anchored canonical records establish the consumer, channel and horizon.

## Runtime account

The operator selects an environment/method config and attempt count. The runner creates unique namespace keys and artifact directories, records configuration/provenance, then builds the environment and harness. The JAZ harness binds shared tools into scope, leaves root-only tools as root inputs, installs method hooks and runs the queue-level agent. Other methods use their own adapters; the official AppWorld baseline runs outside the main Python runner through a separate launcher. Grade production and method execution remain separate responsibilities.

Attempt concurrency uses threads where the environment permits them; a single attempt runs in the calling thread, and environments declaring concurrent attempts unsafe force sequential execution (SRC-1 `src/jaz_evals/eval_harness.py:291-320`). Fresh keys isolate named state, not all process-global dependency behavior. Error handling records method failures and grades completed work; it cannot recover process termination. Provenance is written by run_evaluation, whereas direct run_attempt does not write that run-level record. These distinctions matter when comparing interrupted, directly invoked or concurrently executed runs.

Three forcing cases were traced. A root-only tool can still be deliberately passed to a delegate; its default binding is a sequencing control, not confinement. An early Return meets a validator whose scope must match delegation: tree for StuLife continuation, root for bounded AppWorld solvers. A task grader exception in AppWorld creates an explicit failed/error task, while aggregate Env.grade failure aborts measurement; an execution failure is a third case, graded on work completed. Treating all three as ordinary task failure would hide different evidence limits.

The CodeAct comparison changes several affordances together. Its hook removes runtime __history__ and string-valued input/scope bindings while leaving their prompt text readable; it aborts if the expected template structure is missing. It therefore measures an implemented bundle of removals, not an isolated effect of one retained variable. SRC-1 `src/jaz_evals/hooks.py:82-140,188-250`.

> - **`__history__`** — the system-prompt section and the REPL binding.
> - **String invoke inputs** — the REPL binding, and the user prompt's naming sentence re-rendered
>   over whatever still survives.
> - **String scoped values** (`jaz.scope`) — the REPL binding, and the system prompt's
>   "The scoped variables ... are available in your REPL" sentence re-rendered over the survivors.
> --- `src/jaz_evals/hooks.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

There is no dynamic check planned. Live reproduction would require external task data, submodule implementations, model/service access and substantial runs; none was attempted. Mock runner/grade checks were considered but would add no model-behavior evidence to the explicit branches inspected here. Raw archived runs were not frozen into this source boundary, so reported scores remain reported rather than re-observed.

Revision roles differ. In JAZ AppWorld, the root model proposes, diagnoses, selects and can discard prompt/tool edits under CLM-3; benchmark code supplies outcome feedback, and the operator selects the initial method. In ACE, a fixed loop asks a reflector to diagnose traces, a curator proposes additions, symbolic checks admit valid operations, and optional embedding/model dedup merges entries. Parse/adaptation failures preserve the incumbent playbook; no independent truth test gates each new bullet. Shipped ACE freezes after 42 tasks; JAZ's prompt directs continued batched optimization. This changes both exposure and adaptation cost in the method comparison.

> freeze_after: 42
> --- `configs/appworld_ace_codeact_seed42_full.yaml` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

> adapting = self._freeze_after is None or index < self._freeze_after
> --- `src/jaz_evals/harnesses/ace.py` @ `83dc51ebbd02c9299890b6db93ddc773f07b74b9`

## Lens scoping

### Memory/context scope

Full depth. SRC-1 method adapters and SRC-2 long-horizon/optimization prompts trigger inspection of OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10. Included alternatives: JAZ history handoff, CodeAct variants, per-task resets, ACE playbooks, Letta service memory and smolagents handoff/compaction interfaces. External runtime payloads and maintenance are explicitly uninspected rather than silently dropped from aggregate classifications.

### Epistemic scope

Full depth. Trigger: CLM-1, CLM-2, CLM-3, RTE-3 feedback, RTE-4 withheld correctness and memory-derived adaptation. The lens asks how outcomes become criticism or new rules, which owner accepts a change, and what comparative measurements warrant. Benchmark authors' task correctness, provider internals and actual candidate-linked run histories remain outside the boundary.

## Lens outputs

### Memory/context lens

#### Accumulation and later consumers

The adapters vary where retained experience reaches later work. A whole-queue JAZ invocation can carry context and agent-created objects across tasks. Long-horizon JAZ/CodeAct/smolagents prompts prescribe handing full historical objects and short continuation instructions to a fresh child, then searching older history on demand. The CodeAct hook deliberately removes runtime history access, so its model must record output itself. ACE instead controls the cross-task write/read loop in ordinary Python: a fresh task solver gets an accumulated playbook, and a reflector/curator transforms that task's trace and grading feedback into additions for later solvers. Letta delegates memory construction and retrieval to an external service but adapts task delivery to make task text searchable.

These are different evidence strengths. ACE's route is wired in inspected implementation. The handoff and TTSI transformation policies are delivered instructions with an afforded runtime path; source-only analysis cannot establish compliance, faithful retention, or benefit. Letta's adapter wiring is visible while the search/compaction consumers are partly external. Raw diagnostic traces are not themselves learning; ACE's explicit trace-to-playbook chain is.

#### Writes and retained rationale

RTE-6 is the strongest trace-learning finding: raw task trajectory → reflector diagnosis → curator ADD → optional dedup → retained playbook → later fresh solver. Automatic acquisition of traces alone is insufficient; the later behavior-shaping consumer completes this chain. Per-task snapshots retain history even when active dedup absorbs bullets, but no runtime rollback or invalidation index is wired. A freeze prevents new writes without deleting existing guidance. Reflection prompts ask why errors occurred, yet the retained bullet schema requires only content; later solvers receive reasons only if the model chose to put them in content. Reasoning sidecars establish auditable provenance for a human, not an automatic diagnosis path for later solvers.

RTE-7 retains both raw histories and derived progress/next-step text if the agent obeys. A display suffix can be small while the underlying history list grows without that bound. No semantic faithfulness check relates summaries to full histories. RTE-8 asks for hypotheses and measured validation, but does not require every surviving revision to retain its rationale. RTE-9 exposes summary production at an interception boundary without showing retained rationale or its later use. These gaps should remain on any integrated theory routes.

Manual authoring of static prompts is not itself learning memory. RTE-10 permits reuse or manual editing of a generated seed between runs; no approval/review stage is mandatory. Across all adapters, diagnostic file retention does not imply restoration into an agent. Letta's container is removed after logs are drained; smolagents starts `manager.run(... reset=True ...)` (`src/jaz_evals/harnesses/smolagents_harness.py:1497-1499`). External remote retention remains unknown.

#### Selection and replay limits

ACE's task-start selector supplies every current bullet after removing stored counters; the later solver is explicit. Its selection has no query, relevance rank or budget-driven subset in inspected code. Reflector/curator read the same current playbook alongside the latest task evidence. Dedup embedding similarity selects material for maintenance, not material for the solver's recall prompt. Treating those embeddings as a retrieval index would conflate two consumers.

History-search prompts name the delegated solver and a concrete REPL loop, which supports pull affordance. JAZ history entries expose printed output; CodeAct and smolagents lists expose only what the model recorded. Their summary and next-step text are automatically composed only if the model follows the handoff instruction. Full state objects remain available behind partial display. Long-horizon handoffs are context migration, not evidence of lossless transfer.

Letta's named `conversation_search` consumer supports requested read-back, while the adapter's task-as-user-message change addresses which raw material can be found. The actual external service's current-context assembly and compaction summary insertion are not visible. No route in this report upgrades availability or delivery into activation or demonstrated benefit.

#### Comparison boundary

The profile uses the full commissioned boundary across all adapter branches. Unknown fields deliberately retain external Letta compaction, arbitrary handoff payloads and prompt-governed generation rather than narrowing to the most inspectable ACE path. Visible storage includes files and memory objects; service objects and optional remote indexing are exposed, but the complete backing-substrate set is not established. Natural language and symbolic code/metadata are visible; a textual wrapper does not prove opaque state has only those forms.

The direction set is complete because both controlled alternatives are supported: wired coarse ACE push and afforded solver pull. Its weakest common basis is afforded. Trace learning is a Boolean existence claim established by RTE-6; another opaque route cannot undo that existence. Its source/scope/timing/form axes require complete unions across all qualifying routes, so remain not-determinable. For ACE alone, task trajectories, cross-task scope and between-task online adaptation are established; `freeze_after` creates a training/evaluation stage boundary, not offline corpus training. TTSI and continuation summaries must be included when integrating the remaining trace routes. No learning quality is inferred.

Authority is consumer-relative. ACE's explicit advisory text outweighs the “hard rules” section label. Generated TTSI prompts are intended instructions and generated tools can become executable behavior, but the inspected prompt is not proof those objects were produced. Provenance metadata, zero counters, usage ledgers, and raw retained scores do not supply learning/ranking authority. Unknown faithfulness is required because no qualifying retained execution evidence was inspected.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1, SRC-2, SRC-3 and CLM-1, CLM-2, CLM-3. Assessed families: task submission/evaluation, report derivation, JAZ prompt/tool adaptation and ACE critique/curation. External service internals and unretained raw runs prevent candidate-level or whole-system causal findings. Scores measure the benchmark task domain, not general truthfulness or transferable procedural correctness.

#### 2. Epistemic-object inventory

OBJ-1 supplies task/method instructions, with external or author-provided warrant. OBJ-2 contains answers and action outcomes. OBJ-3 contains outcome assertions and derived aggregates. OBJ-4 is non-truth-apt bookkeeping. The memory records distinguish raw trajectories, proposed rationales/lessons, operative playbooks and programmatic improvements, rather than treating all files as accepted knowledge.

#### 3. Authority-route ledger

| route/function | architectural status | object/update | evaluator and timing | epistemic authority | operational authority | observed state/limit |
| --- | --- | --- | --- | --- | --- | --- |
| RTE-2 operational admission | implemented | OBJ-1, OBJ-2; no content change | Finish predicate at Return | Queue complete only | Continue or finish via BAP-1 | No instance observed; not correctness acceptance |
| RTE-3 check/evidence production | implemented | OBJ-2 → OBJ-3; outcome measurement | AppWorld grader after submission | Specified benchmark assertions | Feedback via BAP-2 | Dependency oracle validity uninspected |
| RTE-3 disposition/acceptance | implemented | OBJ-3; no content change | All assertion outcomes determine recorded success; exceptions produce error | Task result within benchmark | Record, close and advance irrespective of successful solution | No observed task candidate |
| RTE-4 check/evidence production | implemented | OBJ-2 → OBJ-3 | StuLife answer/world checks at submission | Dataset-dependent answer/action correctness | Record score; no correctness delivery to solver | No observed task candidate |
| RTE-4 retention | implemented | OBJ-3; no content change | Append result row | Preserves reported measurement lineage | BAP-3 offline consumer | Retention is not learning |
| RTE-5 content transformation | implemented | OBJ-3; entailed derivation conditional on input records | Counting/aggregation script | Arithmetic consequences of supplied records | Report output | Does not validate input measurements |
| JAZ adaptation on RTE-8 | implemented | Learned prompt/tool memory; indeterminate transformation | Root model interprets trace/feedback and chooses edits | Proposed strategies; generality remains untested here | Later solver context/tools | No instance observed |
| ACE adaptation on RTE-6 | implemented | Playbook lessons; indeterminate transformation | Reflector then curator, followed by structural operation checks | Diagnosis and lessons are model assertions | Valid additions used on later tasks | No instance observed; shape acceptance is not truth acceptance |

The latter routes also implement retention and subsequent operational consumption as separate functions specified on their canonical records. No entry is upgraded to post-acceptance epistemic lifecycle integration merely because a solver receives it.

#### 4. Per-object lifecycle disposition

OBJ-1: acquisition/import; discovery lifecycle not applicable to transport, warrant remains source-dependent. OBJ-2: transformation indeterminate without candidate content; factual derivation, conjecture and non-truth-apt action plans are all possible. RTE-3 and RTE-4 implement checking, but observed candidate state is no instance observed for every candidate-linked phase. OBJ-3's aggregate arithmetic is non-ampliative/entailed given its records; no independent truth warrant for benchmark data follows. No lifecycle record for OBJ-4: no candidate truth-apt output for this object; relevant update route RTE-1 only.

Memory-derived lessons and tools are indeterminate without actual candidates: extraction, reshaping, derivation or new conjecture may occur. The implementation wires feedback→reflection→curation→later use for ACE and affords it through JAZ's root agent, but the observed candidate states for anomaly, conjecture, consequence, test, acceptance and integration are all no instance observed. In particular, retaining a curator addition establishes operational admission, not an evidence-consuming decision that its proposition is warranted. A future candidate trace could establish formulated criticism even without retained historical rationale; its absence here leaves the issue uninspected.

#### 5. System-claim versus route comparison

CLM-1: implemented reproduction machinery, with an explicit mismatch between installable release and original development checkout provenance. CLM-2: reported benchmark outcomes, with code-supported mechanisms but no raw-run or causal replication in this analysis. Within-arm task dependence makes repetitions the comparison unit. The CodeAct treatment bundles removals, and ACE's shorter adaptation horizon prevents attributing a score difference solely to a general memory or criticism mechanism. CLM-3: clear criticism/test/discard policy in prose; the model controls compliance, so the requirement is not a deterministic gate.

#### 6. Bounded conclusion

The strongest contribution is a concrete route from task evidence to revised future solver context. ACE wires diagnostic and curation calls into later playbook use; JAZ's task-sequence prompt explicitly asks for hypotheses, trace diagnosis, minimal edits and subsequent tests. AppWorld supplies a real benchmark answer/outcome oracle, whereas StuLife deliberately keeps correctness outside the agent-facing channel. These are distinct evidential settings.

Under the [theory-builder definition](../../../../notes/definitions/theory-builder.md), assess conditions 1–4 separately. Condition 1, localized content: afforded as identifiable JAZ prompts/tools and ACE bullets, with wired containers; no produced candidate instance inspected. Condition 2, consumption through content: afforded by later solver and executable tool paths, with wired delivery; actual model uptake remains uninspected. Condition 3, content-directed criticism: claimed by JAZ's hypothesis-testing prompt and afforded by ACE's trace/strategy diagnosis prompts; a working formulated criticism is uninspected without trace evidence. Condition 4, iteration: wired feedback/updated-material delivery and afforded criticism uptake across tasks; actual retention of a formulated criticism or revised theory into the next decision remains uninspected. Theory-builder membership is consequently uninspected, not refuted.

Addressability: prompts, functions and individual playbook entries afford local revision; explicit scope assumptions and historical rationale depend on generated content. Persistence: cross-task within an attempt is wired for the relevant methods; ACE seed import affords reuse beyond it, but the fresh attempt design does not itself establish a cumulative cross-run learner. Learning is claimed at the reported bundled-method outcome level; improved future capacity attributable specifically to criticism of consumed theories remains uninspected. No causal decomposition is licensed by the summary tables.

[Reflection](../../../../notes/definitions/reflective-system.md) is afforded over the solver's prompt/tool strategy and runtime traces in JAZ optimization, and over playbook/solver behavior in ACE. Reflective theory-builder membership remains uninspected. Computational proposing/diagnosing/curating/selection roles are wired or afforded as described, but an autonomous theory-builder qualifier cannot be established without its missing conditions. [Self-improvement](../../../../notes/definitions/self-improving-system.md) is supported dispositionally by these evidence-responsive organizational-update routes; exercised causal dependence on a particular update is uninspected. The fixed optimizer/critic method itself is not shown undergoing criticism and replacement.

## Reconciliation

Proposal mapping: MEM-OBJ-1 → OBJ-5; MEM-OBJ-2 → OBJ-6; MEM-OBJ-3 → OBJ-7; MEM-OBJ-4 → OBJ-8; MEM-OBJ-5 → OBJ-9; MEM-RTE-1 → RTE-6; MEM-RTE-2 → RTE-7; MEM-RTE-3 → RTE-8; MEM-RTE-4 → RTE-9; MEM-RTE-5 → RTE-10; MEM-ABS-2 → ABS-1.

1. Register proposed object records OBJ-5, OBJ-6, OBJ-7, OBJ-8 and OBJ-9; route records RTE-6, RTE-7, RTE-8, RTE-9 and RTE-10; and bounded absence record ABS-1. Recall-dependence uncertainty is retained under Limitations and checks rather than allocated an absence ID. Preserve their different evidence strengths and do not merge the opaque state payload into the readable summary.
2. Retain Letta compaction as unresolved included behavior. Its local patch shows text production but not persistence/consumer assembly; resolving this requires an expanded dependency boundary. Current uncertainty is nonblocking and prevents complete aggregate sets.
3. Distinguish JAZ magic history, CodeAct model-maintained history, and smolagents wrapped history. The wrapper budgets display rather than retained bytes; CodeAct removes automatic history access rather than proving equivalent self-recording.
4. Preserve ACE's explicit advisory authority, structural-only rejection, uncapped adaptation cost, optional seed reuse, 42-task shipped freeze, and overlapping dedup groups. No source correction is proposed, but comments mentioning 10 frozen-training tasks are stale relative to the shipped 42-task config; use executable configuration for that value.
5. Rationale is requested during reflection/TTSI, but is not guaranteed to accompany retained playbook bullets or generated tools. Separate archived reasoning from rationale that the later solver actually receives.
6. Integration revision: removed the former uninspected absence proposal, moved its limitation into the report, expanded the bounded per-task absence with the exact query and input enumeration, corrected citation ranges against frozen blobs, and added admission/budget quotations.
7. Do not classify task scores, plot artifacts or search-shape metrics as faithfulness evidence. Full memory-axis unknowns are intentional, not missing work. Publication may adopt them without fetching excluded sources; strengthening requires new evidence and review.

Parent records RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 describe execution, grading and measurement; specialist routes describe retained memory and adaptation. This keeps a task score separate from its later interpretation. Known memory aggregates include all declared adapter alternatives or explicitly retain uncertainty. No independent convergence or observed learning is claimed merely from both lenses finding the same call chain. No unresolved substantive integration conflict remains.

## Bounded synthesis

jaz-evals makes the paper's method claims inspectable as executable configurations, prompts, feedback policies and comparison interventions. The operational distinction is between an agent choosing how to use its history and improve a solver, and a fixed adaptation controller that calls a reflector/curator and carries a playbook into the next task. Both depend on external model and benchmark contracts.

The package also exposes important limits to interpretation. AppWorld provides grader feedback for improvement; StuLife hides per-task correctness. CodeAct removes multiple programmatic-context features together. ACE stops adaptation after 42 tasks while the JAZ method is prompted to continue. The reported AppWorld means favour JAZ, but the source explicitly says six repetitions do not separate it from CodeAct plus subagents. The retained release cannot reproduce the original code bytes exactly from the install pin alone.

The result therefore supports implemented experimental and adaptation routes, with reported outcome evidence at the method-bundle level. It does not independently demonstrate a completed criticism-driven learning episode or a causal benefit from one component. Exact archived traces, dependency/data captures and matched controlled runs would strengthen those findings. No recommendation about another system follows automatically from this analysis.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | resolving evidence |
| --- | --- | --- | --- | --- |
| Historical run code differs from released version | CLM-1, SRC-3 | README provenance disclosure | Byte-exact reproduction from current install pin | Full original trees/diffs and immutable dependencies |
| Raw runs not inspected | CLM-2, CLM-3, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10 | Source and summary tables | Candidate criticism, activation, learning and causal attribution | Frozen traces linking theory, criticism, update and later use |
| Dependencies and data excluded | CMP-2, RTE-3, RTE-4 | Adapter boundary | Oracle correctness, full service memory and deployed isolation | Pinned dependency/data analysis |
| Bundled interventions and unequal adaptation schedules | RTE-2, CLM-2 | CodeAct and ACE configs | Isolated history/criticism component effect | Matched ablation and schedule controls |
| Finite repetitions and task dependence | CLM-2, RTE-5 | Reported AppWorld tables | Reliable separation of top methods or task-IID confidence | More independent repetitions and appropriate inference |
| Parametric internals opaque | CMP-3, CMP-4 | Dated API names and model-name encoder loading | Weight identity or training attribution | Provider/model artifact provenance |

## Verification and blockers

### Semantic verification

Checked source pins/quotes, canonical IDs, status strength, ordinary/alternate/forcing paths and answer-oracle ownership. Memory aggregation covers OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10 and preserves opaque external branches. Reviewed trace-fed ACE writes, JAZ/smolagents handoffs and compaction, Letta service boundaries, automatic selectors and their consumers; trace-learning scope/timing/form stay attached to qualifying routes rather than all recorded logs. Outcome records and table reports remain distinct from observed candidate histories. Criticism, content uptake, persistence and improved capacity are assessed separately.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-evals-01/result.md`, using `commonplace-validate --full`. Full validation passed with no warnings or failures.

### Blockers

none
