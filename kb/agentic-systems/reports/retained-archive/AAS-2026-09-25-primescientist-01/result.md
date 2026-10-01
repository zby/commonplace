---
type: types/agentic-system-analysis-result.md
description: "PrimeScientist plan-tree search, score/prior selection, reflector rationale and execution inheritance with bounded evaluator and budget authority"
run-id: AAS-2026-09-25-primescientist-01
system: PrimeScientist
run-date: "2026-09-25"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Source-owned retained plans, priors, packets/statistics, logs and diagnostic reductions, inherited sandbox artifacts, imported insight files, baseline history and best workspace, and the reflector session access handle across search and vanilla with AutoLab/FIRE Codex interfaces. External Codex/provider context storage and transformations are excluded; their resume boundary remains explicitly opaque. Static task datasets/instructions and unrelated vendored utilities are not memory merely because stored."
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: [files, in-memory]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-14, RTE-7]
      note: "Source-owned persistence uses files; vanilla also accumulates an operative packets list between iterations and reconstructs it from disk on resume. A directory-encoded tree is not a separate graph storage service. The external context behind the session handle is excluded, not classified as files."
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7]
      note: "Plans/reasons and diagnostic prose establish natural-language; JSON fields, Python transforms, code and statistics establish symbolic form. Inherited sandboxes copy arbitrary experiment payloads without a closed artifact schema; their complete form cannot be inferred from these wrappers. External resumed context is also opaque but excluded from this aggregate."
    lineage:
      assessment: known
      basis: wired
      values: [authored, imported, other-compiled, trace-extracted]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-14, RTE-8, RTE-9, RTE-10]
      note: "Root plans are authored; existing insights and parent artifacts are imported; numeric statistics and artifact diffs are compiled; diagnostics, histories and subsequent proposals are derived from execution records. Imported content's original authorship is not claimed."
    behavioral_authority:
      assessment: known
      basis: afforded
      values: [enforcement, instruction, knowledge, ranking, routing]
      records: [BAP-1, BAP-2, BAP-3, RTE-2, RTE-3, RTE-5, RTE-7]
      note: "Ledgers enforce stopping; scores/priors rank and route work; plans and failure prohibitions instruct; logs, rationales and imported insights inform. Deterministic paths are wired; model file reads and native-skill activation are afforded, with no observed use or learning-weight authority established."
    write_agency:
      assessment: known
      basis: wired
      values: [automatic]
      records: [RTE-1, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Framework writes, copies, extraction, model-mediated proposal production and branch maintenance are automatic. Human run configuration is not manual memory authoring; producers of externally supplied insights are not inspected."
    curation_operations:
      assessment: known
      basis: afforded
      values: [consolidate, evolve, invalidate, promote, synthesize]
      records: [RTE-4, RTE-5, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Briefs and histories consolidate; child plans revise prior plans and best_sandbox replaces operative content; pruning invalidates active branches while retaining them; best_sandbox promotes a successful trial into the next seed; reflector prompts afford synthesis of new hypotheses. Prompted synthesis is not guaranteed semantic novelty. No dedup or memory decay is established; omitted prompt lines remain in raw files."
    read_back_direction:
      assessment: known
      basis: afforded
      values: [pull, push]
      records: [RTE-2, RTE-3, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11]
      note: "Orchestrator-selected nodes, inherited workspaces, staged skills and bounded history are supplied automatically. Reflector shell reads of named files and relevant siblings are an explicitly afforded pull route. Delivery to files and CLI is wired; actual model reading is unobserved."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse, identifier, inferred-lexical]
      records: [RTE-2, RTE-3, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Coarse selectors retain log head/tail, recent ten attempts and available insight files; node/task/parent identity selects delivered plan, sandbox and diagnostic paths; verifier regex preserves metric/verdict lines. BAVT score-weighted stochastic choice is an additional numeric selection mechanism without a controlled token: identifier covers the subsequent branch-specific delivery, not that ranking arithmetic. Relevance judgments during requested reads are pull, not an inferred-judgment push."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-2, RTE-4, RTE-5, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Automatic trace-fed writes persist later guidance or ranking state: revised plans/priors, log briefs, verifier reductions, pruned-branch reminders, numerical Q and baseline history. Neither novel knowledge nor measured improvement is required for this route classification."
    trace_source:
      assessment: known
      basis: wired
      values: [session-logs, tool-traces, trajectories]
      records: [RTE-4, RTE-5, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Agent-session logs feed briefs; verifier subprocess traces feed packet excerpts; retained plan/run/score sequences feed hypothesis revision, pruning memory and baseline history. These are batch files and records, not an independently established event-stream subscription."
    learning_scope:
      assessment: known
      basis: wired
      values: [per-task]
      records: [RTE-2, RTE-4, RTE-5, RTE-7, RTE-8, RTE-9, RTE-10, ABS-1]
      note: "Every qualifying source-owned trace-fed transformation is keyed to one task's tree or iteration directory. Cross-task insight read/copy interfaces do not establish automatic trace-fed insight production or cross-task learning. Task horizon comes from task paths and loop arguments, not the session ID."
    learning_timing:
      assessment: known
      basis: wired
      values: [online, staged]
      records: [RTE-2, RTE-4, RTE-5, RTE-7, RTE-8, RTE-9, RTE-10]
      note: "Numeric state is updated online in the active search loop; reflector proposal generation, bounded diagnostic preparation and vanilla history are staged between completed trials and the next consumer. No separate offline training job is established."
    distilled_form:
      assessment: known
      basis: wired
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-14, OBJ-15, OBJ-16, OBJ-17]
      note: "Qualifying source-owned transformations produce prose guidance/excerpts plus structured priors, Q statistics and executable plan transforms. Arbitrary copied experiment payloads are retained outputs, not an inspected framework distillation route; external Codex compaction/training is excluded."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-3, RTE-5]
      note: "No retained execution evidence testing dependence on recalled material is supplied by the inspected runtime/README boundary. Task-score evaluators and success claims do not establish native-skill activation or causal dependence on memory; this is not a claim that no such experiment exists elsewhere."
---

# PrimeScientist agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-primescientist-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/primescientist.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-primescientist-01/memory-report.md`

**Memory analysis report SHA-256:** `554a39675914cd2e46b2e2bd48ee0cef52650c603c55c77464dec4f45237ab04`

## Boundary and evidence

Evidence basis: source code, embedded prompts and README doctrine at SRC-1, frozen 2026-09-25. No task execution, provider probe or benchmark reproduction. PrimeScientist is a research-plan search and improvement plane: Python selects and retains plans/results, invokes a reflector and coding agents, and uses benchmark scores to continue or prune. It owns the outer search but serves/launches an external Codex inner runtime, so the boundary is complete artifact, partial loop.

Included: run_search.py, search/tree.py, search/reflector.py, the material run_vanilla.py alternative, benchmark base/registry/utils, AutoLab and FIRE-Bench adapters, Codex staging/launch interfaces, evaluator call/result paths and one illustrative AutoLab Gaussian-blur verifier. Excluded: external Codex/model/provider internals, deployment credentials, full task datasets, full scientific validation of every verifier and benchmark reproduction. The README's MLE-Bench report is not a shipped adapter established by the inspected registry. No paper, ingest, earlier review or other system is evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | https://github.com/Henri-XYu02/PrimeScientist; access `/home/zby/llm/commonplace/related-systems/Henri-XYu02--PrimeScientist` | `29971beac6f4f4b41309b1326762e1b83ceece98` | Implementation: orchestration, adapters, prompts, evaluator interfaces. Doctrine/design: source comments and README. Reported operation: README benchmark scope | Selected commit-addressed blobs and scoped tree entries | `run_search.py:51-150,168-745`; `search/tree.py:35-309`; `search/reflector.py:58-634`; detailed anchors below | External inner agent/model execution uninspected; no candidate-linked result trace or causal experiment; prevents observed learning, isolation and performance claims |

## Shared records

### Components

CMP-1 — Deterministic tree/search/budget orchestration. Python files and directories encode nodes, priors, packets, visits and Q. The outer loop chooses a node, stages/executes/evaluates it, prunes or backpropagates, and asks the reflector for children. Implementation conclusion status: wired. Source: SRC-1 `run_search.py:422-653`; `search/tree.py:35-255`.

CMP-2 — Reflector Codex prompt/CLI/session integration. Python builds initialization/reflection prompts and launches pinned CLI 0.121.0; CLI default model at public entry is gpt-5, helper default o4-mini. The selected provider model is an identifier rather than a pinned model-weight digest; parameter changes during operation and exact provider version are uninspected. Local code changes plans/state, not demonstrated model weights. Source: SRC-1 `search/reflector.py:371-490`; `run_search.py:667-690`. Model invocation is wired; content-directed reasoning/criticism is afforded by prompts, unobserved.


>     last_cumul     = int(state.get("codex_last_cumulative_tokens", 0))
> 
>     base_cmd = [
>         "npx", "--yes", f"@openai/codex@{REFLECTOR_CODEX_VERSION}",
>         "--model", model,
>         "--config", "sandbox_mode=danger-full-access",
>         "--ask-for-approval=never",
>     ]
> 
>     if session_id:
>         # NB: --skip-git-repo-check must be included here too — without it,
>         # codex refuses to run in non-git directories even when resuming.
>         cmd = base_cmd + ["exec", "resume", "--skip-git-repo-check",
>                           session_id, prompt]
>         print(f"  [reflector:codex] resuming session={session_id[:8]}…  "
>               f"last_cumul={last_cumul:,}  (codex@{REFLECTOR_CODEX_VERSION} model={model})")
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

CMP-3 — Benchmark adapter and executing Codex interface. AutoLab copies baseline or parent sandbox, installs a native skill, exposes a build-check script and runs Codex 0.121.0 with danger-full-access/approval-never. FIRE-Bench supports fresh/inherited workspaces, pinned host CLI 0.39.0 or externally configured Docker/enroot image. Actual OS/container/provider enforcement is deployment-dependent and uninspected. Host model identity comes from the chosen CLI parameter; own model training is not established by these launchers. Task programs can invoke further APIs/training as experimental subjects, outside the enumerated inner computation. Source: SRC-1 `benchmarks/autolab/__init__.py:99-193`; `benchmarks/fire_bench/agents/codex/run.py:57-282`; `benchmarks/fire_bench/agents/codex/run_inherit.py:59-164`.

CMP-4 — Evaluator and score interfaces. AutoLab runs task test.sh in Docker or enroot and reads reward JSON; FIRE-Bench extracts a log conclusion, summarizes it using gpt-5.2 and invokes RAGChecker with openai/gpt-4.1 extractor/checker against bundled reference answers. Exact provider versions/parameters remain uninspected; those model calls do not constitute a single deterministic scientific oracle. Source: SRC-1 `benchmarks/autolab/__init__.py:197-245,278-389,543-658`; `benchmarks/fire_bench/eval/RAGChecker/eval.py:14-16,190-221`; `benchmarks/fire_bench/eval/RAGChecker/utils.py:201-223`. Invocation/result wiring: wired; scientific correctness/generalization: uninspected.


>     
>     gt_vs_response = {
>         "results": [
>             {
>                 "query_id": "000",
>                 "query": f"{query[task]}",
>                 "gt_answer": f"{gt[task]}",
>                 "response": f"{core_idea}",
>                 "retrieved_context": []
>             }
>         ]
>     }
> 
>     evaluator = RAGChecker(
>         extractor_name="openai/gpt-4.1",
>         checker_name="openai/gpt-4.1",
>         batch_size_extractor=8,  
>         batch_size_checker=8
>     )
>     rag_results = RAGResults.from_json(json.dumps(gt_vs_response))
>     evaluator.evaluate(rag_results, all_metrics)
> 
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

### Operative objects

OBJ-1 — Experimental plan skill.md plus optional changes.md/diff.py. Natural-language action instructions and executable transformation code produced by reflector and staged for a child coding agent. CodeAct branch instructs diff.py to derive a full updated plan; AutoLab branch instructs a compact incremental plan. Actual plan adequacy is not certified by file existence. Source: SRC-1 `search/reflector.py:58-90,245-323`; `run_search.py:113-148`; `benchmarks/utils.py:204-258`. Storage/staging conclusion status: wired; compliance with semantic prompt requirements: afforded.

OBJ-2 — prior.json hypothesis, rationale, estimate, changes and risks. Natural-language predicted mechanism plus numeric prior. Reflector authors it from earlier results; next reflector is instructed to reread it. Bootstrap only parses/clamps estimate with default 0.5, not the quality/presence of the explanation fields. Hypothesis may be an operative tentative theory if actually used for proposal/test decisions; this use is uninspected. Source: SRC-1 `search/reflector.py:260-276,307-321`; `run_search.py:132-148`.


>       record the NEXT reflector will consult instead of your (now-discarded)
>       thinking — so invest your analysis here rather than in stdout:
>         {{
>           "estimate": <float 0-1>,
>           "hypothesis": "<the single concrete hypothesis this proposal tests>",
>           "rationale": "<2-3 sentences: WHY you expect this to improve the score,
>                          grounded in specific observations from packet.json /
>                          log_brief.log / sandbox — cite file or section>",
>           "changes": "<1 sentences naming which files/sections this proposal
>                        modifies, at what abstraction level (algorithm / data
>                        structure / hyperparam)>",
>           "risks": "<1-2 sentences on the most plausible failure mode>"
>         }}
> """
> 
> # CodeAct-style block — diff.py transforms parent skill.md to child's full
> # plan, plus a short changes.md the agent reads in the inherited sandbox.
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

OBJ-3 — Result packets, result/cost ledgers and tree stats. JSON/TSV symbolic scores, IDs, timestamps, model/cost fields and Q/P/visit state. Q is updated by backpropagated accepted-descendant rewards, not merely the node's own last execution. Stored maximum across repeated executions and aggregated Q have different referents. Source: SRC-1 `search/tree.py:60-93,145-152`; `run_search.py:348-416,551-586`; `benchmarks/utils.py:174-201`. Implementation conclusion status: wired; external score warrant is evaluator-dependent.


>     def record_visit(self, f1: float) -> None:
>         """Increment visits and update Q as running average."""
>         stats = self._read_stats()
>         n = stats.get("visits", 0)
>         q = stats.get("Q", 0.0)
>         stats["visits"] = n + 1
>         stats["Q"] = (q * n + f1) / (n + 1)
>         self._write_stats(stats)
> 
> --- `search/tree.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>     def backpropagate(self, f1: float) -> None:
>         """Walk from this node to root, updating Q and visits."""
>         node: TreeNode | None = self
>         while node is not None:
>             node.record_visit(f1)
>             node = node.parent()
> 
>     # ── Repr ────────────────────────────────────────────────────────────────
> --- `search/tree.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

OBJ-4 — Sandbox code/data/results, copied from task baseline or selected parent's own retained execution. Symbolic programs plus task-specific outputs can persist into child execution. A parent's Q may include descendants while its sandbox remains its own execution artifact; ranking quality and inherited code identity should not be conflated. Source: SRC-1 `run_search.py:348-416`; `benchmarks/autolab/__init__.py:115-129`; `benchmarks/fire_bench/agents/codex/run_inherit.py:78-102`. Implementation conclusion status: wired copy; correct subsequent execution uninspected.

OBJ-5 — Full agent logs, 100-head/500-tail brief, verifier diagnostic output and pruned-branch summary. Raw evidence, deterministic excerpts and retained hypothesis/rationale/verdict snippets differ in semantic role. Hidden full logs remain on disk; excerpting is not evidence that model reasoning was faithfully preserved. Source: SRC-1 `run_search.py:168-253,322-343`; `search/reflector.py:546-573`; `benchmarks/autolab/__init__.py:340-389`. Retention/transformation conclusion status: wired.


>         return
>     head_block = lines[:head]
>     tail_block = lines[-tail:]
>     omitted = len(lines) - head - tail
>     sep = [
>         "",
>         f"... [{omitted} middle lines omitted — read log.log directly if needed] ...",
>         "",
>     ]
>     brief.write_text("\n".join(head_block + sep + tail_block), encoding="utf-8")
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

OBJ-6 — Cross-task insight file/interface and local copies. The initializer copies other-task *.md insight files and creates an empty current-task insight. Reflection syncs external insight files locally; FIRE agent stages nonempty other-task insights. A complete production/update route and warranted empirical content cannot be inferred from these read/copy interfaces alone. Source: SRC-1 `search/reflector.py:503-543,595-602`; `benchmarks/fire_bench/agents/codex/run.py:23-54`; `run_search.py:483-491,652-653`. Imported-content production remains external; see ABS-1.

For OBJ-6, optional insight import/context assembly is wired; no closed automatic shared-insight writer was established in the specified search boundary ABS-1. Copies overwrite matching names but do not delete local files absent from source. They do not imply mirror synchronization or automatic cross-task learning. Source: SRC-1 `search/reflector.py:525-534,597-602`; `benchmarks/fire_bench/agents/codex/run.py:23-54`.

>         for insight_file in sorted(insights_dir.glob("*.md")):
>             if not insight_file.stat().st_size:
>                 continue
>             # Skip the current task's own insight (included below via skill.md)
>             if insight_file.stem == f"{task_id}_insight":
>                 continue
>             content = insight_file.read_text(encoding="utf-8").strip()
>             insight_parts.append(f"### {insight_file.stem}\n{content}")
> --- `benchmarks/fire_bench/agents/codex/run.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`


OBJ-7 — Reflector session identifier/cumulative usage state plus external resumed context. JSON persists CLI session ID/token counter; next call requests exec resume. Failed resume deletes state, allowing fresh next attempt. Provider-side context contents, compaction/fidelity and actual retained activation are uninspected. Source: SRC-1 `search/reflector.py:326-353,374-475`. Resume request and fallback: wired; model-context memory content: uninspected.

OBJ-8 — Scientific task conclusion and extracted generalized core idea. Source content is external coding-agent output; evaluation extracts from log and asks gpt-5.2 to omit numbers, methods and artifact references. Natural-language truth-apt assertions feed model comparison. Preservation of meaning is not certified by the prompt. Source: SRC-1 `benchmarks/fire_bench/eval/RAGChecker/eval.py:190-221`; `benchmarks/fire_bench/eval/RAGChecker/utils.py:201-223,227-275`; quoted on RTE-4.

OBJ-9 — Supplied answer/reference and objective. FIRE has task-indexed gt/query mappings; sampled AutoLab has reference Gaussian computation and benchmark constants. These are natural-language expected conclusions and symbolic reference functions/objectives, supplied by benchmark authors and consumed by evaluators. They are an answer oracle within those routes; their general empirical truth is uninspected. Source: SRC-1 `benchmarks/fire_bench/eval/RAGChecker/utils.py:45-55`; `benchmarks/autolab/tasks/gaussian_blur/tests/verify_correctness.py:1-30`; `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh:94-118`; RTE-4 evidence.

For OBJ-3, the aggregate retains its identity; its heterogeneous per-part epistemic disposition is superseded by OBJ-10 and OBJ-11 without reassignment.

OBJ-10 — Recorded evaluator measurements/verdict scores and associated provenance. AutoLab reward/detail or FIRE precision/recall/F1 claim tested performance/agreement; Python stores them and later selectors/reflectors consume. Source: SRC-1 `benchmarks/autolab/__init__.py:197-245`; `benchmarks/fire_bench/__init__.py:145-215,286-350`; RTE-4 evidence. Numeric form does not establish source truth.

OBJ-11 — Tree/control statistics and ledgers. Q, prior, visits and logged costs/token counts derive from accepted values and guide selection. They assert local accounting/aggregate state, not science; policy fields have ranking/stop force. Source: SRC-1 `search/tree.py:60-93,145-188`; `run_search.py:51-111,506-593`; OBJ-3 and RTE-2 evidence.

For OBJ-5, the aggregate retains its identity; its distinct per-part epistemic disposition is superseded by OBJ-12 and OBJ-13.

OBJ-12 — Agent/verifier log evidence and head/tail excerpts. Caller/runtime-generated textual assertions, retained/moved/excerpted by Python and read by reflector. Source: SRC-1 `run_search.py:322-343`; `search/reflector.py:546-573`; OBJ-5 evidence.

OBJ-13 — Pruned-branch explanation/verdict summary and vanilla recent-attempt history. Python combines retained hypothesis/rationale or clipped plan/summary with score and disposition, including an instruction not to repeat failed approaches. Consumer is later reflector or coding agent. Source: SRC-1 `run_search.py:168-253`; `run_vanilla.py:63-98`; OBJ-5/RTE-7 evidence. Distinct from raw log acquisition; trace-fed guidance is wired through RTE-9/RTE-10.

OBJ-14 — Vanilla continuation bundle: retained history_shown.md and best_sandbox, backed by the in-memory packet list and replayed packet files. This refines OBJ-4/OBJ-13 for the baseline consumer without changing their aggregate referents. Natural-language formatting and symbolic outcome fields are known; full copied payload form remains opaque. Source: SRC-1 `run_vanilla.py:77-116,164-191,235-245,303-318`.

OBJ-15 — Pruned-branch reminder: parent/pruned_children.md includes prior hypothesis/rationale/change/risks, threshold comparison, up to300 verifier-tail characters or an800-character plan fallback. Refines OBJ-13; later all-pruned re-expansion names this record for the reflector. Source: SRC-1 `run_search.py:196-253`; `search/reflector.py:94-104`.


>             pr = json.loads(prior_path.read_text(encoding="utf-8"))
>             entry_lines.append(
>                 f"  hypothesis : {pr.get('hypothesis', '—')}\n"
>                 f"  rationale  : {pr.get('rationale',  '—')}\n"
>                 f"  changes    : {pr.get('changes',    '—')}\n"
>                 f"  risks      : {pr.get('risks',      '—')}"
>             )
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`


>     rd = packet.get("reward_detail", {})
>     vot = rd.get("verifier_output_tail", "")
>     if vot:
>         tail = vot[-300:].strip()
>         entry_lines.append(f"\n  verifier tail:\n    {tail.replace(chr(10), chr(10) + '    ')}")
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

OBJ-16 — Retained reflector log brief. Refines OBJ-12 into the derived first100/last500-line continuation context, with full raw source still available. Positional selection does not guarantee retention of causes/reasons. Omission hint says log.log despite newer hidden .log.log; FIRE prompt names the hidden file while AutoLab emphasizes brief. Source: SRC-1 `search/reflector.py:136-146,194-203,546-573,608-615`; `run_search.py:325-340`.

OBJ-17 — Verifier reduction and baseline diff. AutoLab filters warning lines, prefixes last15 lexical metric/verdict matches, then appends last2000 filtered characters. This can exceed2000 total characters. The diff compares baseline/final workspace; a byte-size check followed by character slicing does not guarantee a200KB UTF-8 cap. These are retained diagnostic reductions, not semantic explanations themselves. Source: SRC-1 `benchmarks/autolab/__init__.py:355-389,620-656,659-694,730-755`.


>     kept = [ln for ln in combined.splitlines() if not any(n in ln for n in NOISE)]
>     METRIC = re.compile(
>         r"(validation_accuracy|accuracy|params|reward|metric|PASS|FAIL|correctness)",
>         re.IGNORECASE,
>     )
>     metrics = [ln.strip() for ln in kept if METRIC.search(ln)]
> --- `benchmarks/autolab/__init__.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`


>     if metrics:
>         head = "KEY METRICS (parsed from verifier output):\n" + \
>                "\n".join(metrics[-15:]) + \
>                "\n\n--- verifier output (noise-filtered tail) ---\n"
>     return head + "\n".join(kept)[-limit:]
> --- `benchmarks/autolab/__init__.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`


### Routes

RTE-1 — Root initialization or saved-tree resume. Trigger user CLI with task/benchmark/output. Python loads tree if stats exist, or calls reflector to write root plan after copying instruction/other-task insights. Force-init deletes listed run files but preserves local insights/instruction; normal resume uses files as operational state. Model is owner of root plan choice; structural state owner is Python. Persistence: root files/session/ledgers; return initialized/resumed tree or early failure. No semantic validity gate beyond later staging/execution; external instruction content is policy/knowledge, not automatically a theory. Source: SRC-1 `run_search.py:422-502`; `search/reflector.py:503-543`; `search/tree.py:298-309`. Implementation conclusion status: wired, model following uninspected.

RTE-2 — Budget-adaptive selection, execution scheduling and final best-node summary. Trigger main loop while counted successful packet evaluations remain below budget. Python computes alpha=min(1/min(remaining token ratio, remaining time ratio), alpha_max), with no-budget alpha=1; cost cap is a separate stop condition. BAVT samples children by Q^alpha or (parent Q × sqrt P)^alpha for unvisited, epsilon for zero. Traversal can expand only after existing subtrees are exhausted under cap or at unexpanded node. It returns one node, not parallel execution. Retained visits/priors/packets guide later selection; final best_node chooses highest aggregated Q and prints summary, not a separately verified deployment. Source: SRC-1 `run_search.py:51-111,506-653`; `search/tree.py:162-255`. Selection implementation: wired; expected exploration/exploitation benefit: claimed without run evidence.


>         q = node.Q
>         return q ** alpha if q > 0.0 else 1e-6
>     # Unvisited: inherit parent's proven quality, softened by √P prior
>     sqrt_p = math.sqrt(max(0.0, node.P))
>     if parent is not None and parent.Q > 0.0:
>         virtual_q = parent.Q * sqrt_p
>     else:
>         virtual_q = sqrt_p
>     return virtual_q ** alpha if virtual_q > 0.0 else 1e-6
> --- `search/tree.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>     Falls back to r_t=1 (alpha=1, pure exploration) when no budget limits are set.
>     alpha is capped at alpha_max to avoid numerical issues near budget exhaustion.
>     """
>     ratios = []
>     if max_tokens > 0:
>         used = _read_total_tokens(cost_ledger)
>         ratios.append(max(0.0, (max_tokens - used) / max_tokens))
>     if max_time_sec > 0:
>         elapsed = time_module.time() - start_time
>         ratios.append(max(0.0, (max_time_sec - elapsed) / max_time_sec))
>     if not ratios:
>         return 1.0   # no budget → always explore proportionally to V
>     r_t = min(ratios)
>     if r_t <= 0.0:
>         return alpha_max
>     return min(1.0 / r_t, alpha_max)
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

Budget guarantee owner is outer-loop check over logged estimates; strength best effort at operation boundaries. Init runs before timed main loop begins; agent/evaluation calls can overshoot before next check. AutoLab/FIRE launchers do not pass a per-call token cap; AutoLab task-agent subprocess has no timeout here, while reflector and verifier have distinct timeouts. Empty/missing usage yields no ledger row. RTE-4 accounts recorded selected/nonselected packet costs but not independently audited evaluator API costs. Failure without a packet does not increment evals_done; absent outer limits, repeated run failure has no separate consecutive-failure abort in this tree loop. These are scoped control-flow implications, not observed failures. Source: SRC-1 `run_search.py:451-506,536-593`; `benchmarks/utils.py:134-155,177-186`; `benchmarks/autolab/__init__.py:180-191`; `benchmarks/fire_bench/__init__.py:138-179`.

RTE-3 — Benchmark staging, Codex execution and parent sandbox inheritance. Trigger selected unrun node; Python checks skill existence and stages it. If parent Q>0 and parent sandbox exists it copies that workspace and prepends inheritance guidance; otherwise baseline. AutoLab injects .agents/skills; FIRE uses a full plan and copies diff/changes into inherited workspace. Executor is external Codex using host/container tools; current grant request differs by launcher. Return is timestamp/log reference, even some nonzero subprocess exits can proceed to evaluation. Persistence is code/output/log until artifact movement. Recovery is fresh baseline/parent copy or future retry, not universal transaction. Source: SRC-1 `run_search.py:348-416`; `benchmarks/autolab/__init__.py:84-193`; `benchmarks/fire_bench/__init__.py:98-143`; `benchmarks/fire_bench/agents/codex/run_inherit.py:78-164`. Launch/staging/copy conclusion status: wired; implicit skill activation and model adherence uninspected.


>     # Code inheritance: children start from the parent's best achieved sandbox
>     # rather than the pristine baseline, so they build incrementally.
>     parent_node = node.parent()
>     env_override = None
>     if parent_node is not None and parent_node.Q > 0:
>         parent_sandbox = parent_node.path / "sandbox"
>         if parent_sandbox.exists():
>             env_override = parent_sandbox
>             preamble_template = benchmark.agent_inheritance_preamble
>             if preamble_template:
>                 benchmark.prepend_skill_context(
>                     task, preamble_template.format(parent_q=parent_node.Q)
>                 )
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>             # Use npx to pin the version independently of the globally installed codex.
>             # fire_bench uses the global codex (0.39.0); autolab uses a newer release.
>             cmd = [
>                 "npx", "--yes", f"@openai/codex@{CODEX_VERSION}",
>                 "--model", model,
>                 "--config", "sandbox_mode=danger-full-access",
>                 "--ask-for-approval=never",
>                 "exec", "--skip-git-repo-check",
>                 instruction,
>             ]
>         else:
>             print(f"  [run] Unknown agent: {agent!r} (only 'codex' is supported)")
> --- `benchmarks/autolab/__init__.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

Material alternate executors are AutoLab host agent versus Docker/enroot verifier, FIRE host workspace-write versus Docker/enroot danger-full-access, fresh versus inherited workspaces, and directly supplied adapter/model/task flags. Container names do not establish the enclosing reflector is isolated; reflector itself requests danger-full-access on host. Native tool approvals, filesystem capabilities, credentials and APIs are governed by outer environment, not validated by tree selection. Source: SRC-1 `search/reflector.py:399-414`; `benchmarks/fire_bench/agents/codex/run.py:153-276`; `benchmarks/autolab/__init__.py:278-338,543-615`.

RTE-4 — Evaluation, score-pruning, packet retention and backpropagation. Trigger successful run_id; benchmark evaluates and supplies primary reward. AutoLab reads task verifier output; FIRE uses normalized RAGChecker F1. For n_runs>1, scheduler selects maximum primary packet, moves its sandbox/log and charges other returned packet costs. Prune only if parent exists, threshold>0, parent Q>0 and child score<parent Q-threshold. Pruned directory is renamed hidden, retained with packet and explanatory summary; it does not backpropagate. Otherwise score contributes to this node and all ancestors' running Q. This is a score-based operational admission, not explicit acceptance of every scientific explanation. Source: SRC-1 `run_search.py:168-253,348-416,551-586`; `search/tree.py:108-152`; `benchmarks/fire_bench/__init__.py:145-215,286-350`.


>                 packet["delta_reward"] = round(primary - parent_q, 4)
> 
>                 # ── Pruning check ────────────────────────────────────────────
>                 should_prune = (
>                     parent is not None
>                     and prune_threshold > 0.0
>                     and parent_q > 0.0
>                     and primary < parent_q - prune_threshold
>                 )
> 
>                 if should_prune:
>                     _prune_node(node, parent, primary, packet, prune_threshold)
>                     # no backpropagate — pruned score must not drag parent Q down
>                 else:
>                     node.write_packet(packet)
>                     node.backpropagate(primary)
> 
>                 _append_ledger(ledger_path, node, packet, primary, pruned=should_prune)
>                 append_cost_ledger(cost_ledger, packet.get("cost", {}),
>                                    f"agent:{agent}", model, node_name)
>                 for ec in packet.get("extra_run_costs", []):
>                     append_cost_ledger(cost_ledger, ec, f"agent:{agent}", model, node_name)
>                 evals_done += 1
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>         if run_id is None:
>             continue
>         packet  = benchmark.evaluate(task, run_id)
>         primary = benchmark.primary_score(packet)
> 
>         if primary > best_primary:
>             if best_packet is not None:
>                 extra_costs.append(best_packet.get("cost", {}))
>             best_primary = primary
>             best_packet  = packet
>         else:
>             extra_costs.append(packet.get("cost", {}))
> 
>     if best_packet is None:
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

Answer oracle is mode-specific. FIRE uses task-indexed bundled expected conclusions via gt[task] and model extraction/checking; it filters FP/FN/reference-derived explanation fields from the packet sent to reflector, but host-wide access isolation is not established by that filtering. The evaluator deliberately summarizes away concrete numbers, methods and artifacts, so its score cannot by itself verify reproducing the experiment or exact quantitative agreement. AutoLab's sampled Gaussian-blur verifier checks build-file hash, reference-image correctness then median runtime reward; that licenses only its specified tests, not all inputs or task families. Reference constants and expected outputs come from benchmark authors, not the reflector. Source: SRC-1 `benchmarks/fire_bench/eval/RAGChecker/eval.py:190-221`; `benchmarks/fire_bench/eval/RAGChecker/utils.py:45-55,201-223`; `benchmarks/fire_bench/__init__.py:286-350`; `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh:15-118`; `benchmarks/autolab/tasks/gaussian_blur/tests/verify_correctness.py:1-30,111-130`.


>                 "role": "system",
>                 "content": (
>                     "You are an expert summarizer. "
>                     "Given a conclusion, your task is to extract only the core insight or main idea, "
>                     "omitting all concrete values, specific numbers, background details, methods, "
>                     "file names, or references to artifacts. "
>                     "Focus on general trends or main conclusions/findings, and express them in a "
>                     "generalized way without referring to any precise data or background context. "
>                     "DO NOT infer any detail, context information, or background knowledge that is not mentioned "
>                     "in the original conclusion."
> --- `benchmarks/fire_bench/eval/RAGChecker/utils.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>         # RAGChecker emits metrics on a 0-100 scale; normalise to 0-1 so they
>         # match the autolab convention (and so prune_threshold/BAVT stats are
>         # comparable across benchmarks).
>         rec["score"] = {
>             "precision": float(m.group(1)) / 100.0,
>             "recall":    float(m.group(2)) / 100.0,
>             "f1":        float(m.group(3)) / 100.0,
>         } if m else {}
>         rec["agent_conclusion"] = ""
>         rec["false_positives"]  = []
>         rec["false_negatives"]  = []
>         rec["fp_results"]       = []
>         rec["fn_results"]       = []
>         if rec["score"]:
> --- `benchmarks/fire_bench/__init__.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



> echo "=== Correctness check ==="
> if ! python3 /tests/verify_correctness.py 2>&1; then
>     echo "Correctness check FAILED."
>     write_reward 0.0 false null null
>     echo "0.0" > "/logs/verifier/reward.txt"
>     exit 0
> fi
> 
> --- `benchmarks/autolab/tasks/gaussian_blur/tests/test.sh` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

RTE-5 — Reflector diagnosis/proposal creation, bootstrap and retry admission. Trigger selected evaluated node needs children. Python prepares context pointers/log brief, launches or resumes reflector, scans child directories and bootstraps; at most two expansion attempts before stopping if no ready children. Reflector should diagnose execution failures versus tested low-scoring hypotheses, compare prior trials and propose substantively different mechanisms. Prior explanation persists for later reflector. Bootstrap requires skill.md exists and clamps/defaults estimate; it does not enforce <5KB, schema-complete rationale, scientific validity or successful diff.py lineage. Missing plan is archived. Proposal owner model; structural veto Python; score disposition later RTE-4. Source: SRC-1 `search/reflector.py:106-323,576-634`; `run_search.py:113-166,259-319`.


>     # ── skill.md — should have been written directly by the reflector ────────
>     if not child.skill_path.exists():
>         reason = "skill.md missing — reflector did not write it"
>         (proposal_dir / "bootstrap_error.txt").write_text(reason, encoding="utf-8")
>         archived = proposal_dir.parent / f".archived_{proposal_dir.name}"
>         proposal_dir.rename(archived)
>         print(f"  [bootstrap] Pruned {proposal_dir.name}: {reason}")
>         return False
> 
>     # ── prior.json ───────────────────────────────────────────────────────────
>     estimate = 0.5
>     pf = proposal_dir / "prior.json"
>     if pf.exists():
>         try:
>             pr       = json.loads(pf.read_text(encoding="utf-8"))
>             estimate = float(pr.get("estimate", 0.5))
>             estimate = max(0.0, min(1.0, estimate))
>         except (json.JSONDecodeError, ValueError, TypeError) as e:
>             print(f"  [prior] WARNING: bad prior.json for {proposal_dir.name} ({e}) — using 0.5")
>     else:
>         print(f"  [prior] prior.json missing for {proposal_dir.name} — using 0.5")
>     child.set_prior(estimate)
> --- `run_search.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>                                  changed, then read ONLY the specific files the
>                                  diff points to if more context is needed.
>   Other nodes' prior.json / skill.md / packet.json in the tree — when you need to
>                                  know previous trials' approach and performance
> 
> Your job:
> 1. Read packet.json. If reward is 0, START with
>    `reward_detail.verifier_output_tail` — it usually names the exact file/line
>    where the build broke or the first divergent line of the correctness diff.
>    Then read {node_rel}/log_brief.log to correlate with what the agent tried.
>    Optionally inspect specific files in {node_rel}/sandbox/ that the agent changed.
>    Ground your analysis in what the verifier actually reported, not just the score
>    or the agent's own claims.
> 2. Check other nodes' prior.json / skill.md / packet.json as needed to avoid re-proposing a hypothesis
>    that's already been tried, or to learn previous trials' performance to better reflect.
> 3. Extract experimental setup failures, or factors in skill file that cause runtime failures.
> 
> 4. Propose between 1 and {n_proposals} CONTROVERSIALLY DIFFERENT skill variants.
>    "Controversially different" means each proposal bets on a fundamentally different
>    hypothesis — e.g. different algorithm, different data structure, different trade-off,
>    different part of the code to change. Do NOT create proposals that differ only in
>    a parameter value or a minor wording change; those are not separate bets.
> 
>    You decide how many to create:
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

Theory-route guidance: hypothesis/rationale predicts how changes improve score and names risks, grounded by requested references to observed files. Formulation: afforded by prompt and model-call wiring; operative use: afforded by instructions, actual use uninspected; content-directed criticism: afforded by requested diagnosis/verifier comparison, not entailed by scalar score; revision/changed reliance: wired proposal and selection route, semantic response to criticism uninspected; attributable future capacity: uninspected. Retention and addressability are per-plan/per-hypothesis/file/branch, with structured rationale but unconstrained adequacy. Selection optimizes score/prior/budget; no implemented preference for explanatory reach among equally fitting theories is inferred.

RTE-6 — Log/packet/artifact moves, briefs and cross-task insight interface. Trigger completed selected run or reflection initialization. Python moves selected log to hidden .log.log and sandbox to node, adjusts packet relative paths, excerpts first100/last500 log lines, syncs external insight *.md files. The host is told which evidence to read and when full log is worth opening. Acquisition/formatting owner Python; semantic selection/use owner reflector/agent. Return paths/brief/selectedcontext; persisted files supply later iterations. Other run artifacts may remain outside the selected node; move is conditional destination-not-exists, not atomic global cleanup. Cross-task production is bounded by ABS-1. Source: SRC-1 `run_search.py:322-343`; `search/reflector.py:503-543,546-634`; `benchmarks/fire_bench/agents/codex/run.py:23-54`. Implementation conclusion status: wired interfaces/excerpts; truth and activation uninspected.

RTE-7 — Linear baseline history and keep/revert alternative. Trigger run_vanilla CLI with selected benchmark/task. It replays per-iteration packets, builds last10 history with up to400 chars summary, stages this as skill and seeds from best_sandbox when positive. Coding agent makes one change; evaluator scores; strict score>best keeps/copies sandbox, otherwise leaves best unchanged. It records every packet/ledger and stops after limits or three consecutive no-run_id failures. Parent tree proposals/BAVT are absent from this alternative by the inspected run_vanilla control flow; it is not a second theory-builder inference. Source: SRC-1 `run_vanilla.py:63-118,137-337`. Implementation conclusion status: wired. Guidance is retained score/action/summary and improvement instruction; richer theory formulation/criticism remains uninspected for the opaque agent.


> def _format_history(results_tsv: Path, packets: list[dict], max_entries: int = 10) -> str:
>     """Render past iterations as a markdown log shown to the agent."""
>     if not packets:
>         return HISTORY_HEADER + "_(no prior attempts — this is iteration 0)_\n"
>     lines = [HISTORY_HEADER]
>     # Keep the last max_entries to bound prompt size
>     shown = packets[-max_entries:]
>     if len(packets) > max_entries:
>         lines.append(f"_(showing last {max_entries} of {len(packets)} attempts)_\n")
>     for entry in shown:
>         i      = entry["iter"]
>         score  = entry["score"]
>         delta  = entry["delta"]
>         action = entry["action"]
>         summary = entry.get("summary", "").strip()[:400] or "(no summary)"
>         lines.append(f"## Iteration {i}  —  score={score:.4f}  Δ={delta:+.4f}  **{action}**\n")
>         lines.append(summary + "\n")
>     return "\n".join(lines)
> 
> 
> # ---------------------------------------------------------------------------
> # Sandbox commit/revert
> --- `run_vanilla.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`



>         packet["best_so_far"]   = max(best_score, score)
> 
>         # ── Move artefacts into iter_dir ─────────────────────────────────────
>         if benchmark.log_root:
>             try:
>                 _move_artifacts(packet, benchmark.log_root, iter_dir, task_dir)
>             except Exception as e:
>                 log_error("_move_artifacts", e, task=task, iter=i)
> 
> --- `run_vanilla.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

On RTE-7, strict improvement admits code but does not certify explanation. Rollback means not replacing best_sandbox, while successful commit deletes/copies with ignored per-run files. A copy failure can be logged while best_score still advances; recorded kept status and deployed best bytes can diverge under that failure. Resume reconstructs score/history from packet files without reconstructing a missing best_sandbox. Source: SRC-1 `run_vanilla.py:105-116,164-191,303-318`. Failure consequence is static, not observed. Changes target task implementation, not automatically the search framework/model weights.

RTE-8 — Diagnostic-reduction subroute refining RTE-6. Trigger AutoLab evaluation and selected-node reflection. Deterministic producer reduces raw verifier/session traces and diffs baseline/final state into OBJ-16/OBJ-17. Context owner reflector receives node-specific paths and pulls evidence; persistence packet field/files. Return compact diagnostics, no content validation; failure to produce diff is diagnostic only. Later read-back BAP-2 on the next proposal; selectors positional and verifier regex. Original traces persist, derived files overwrite on regeneration. Conclusion status wired reduction/context targeting, afforded actual model reading. Guidance is selected observations, not newly established theory. Trace-fed brief/verifier reduction qualify as continuation memory; state diff is a separate compiled diagnostic. Source: SRC-1 `benchmarks/autolab/__init__.py:355-389,620-694,730-755`; `search/reflector.py:118-159,546-573,608-634`.

RTE-9 — Rejected-approach reminder subroute refining RTE-4/RTE-5. Trigger score pruning; producer Python combines outcome and prior/plan into OBJ-15. Later all-children-pruned re-expansion injects its path with a must-not-repeat instruction for BAP-2. Mixed surviving/pruned siblings do not trigger that special injection; stored failures may still be pulled. Persistence hidden child and appended reminder; return future prompt path; invalidation is traversal exclusion, not deletion. No semantic novelty matcher enforces the prohibition. Explanation is retained when prior rationale exists; threshold is the explicit algorithmic rejection reason, not proof against the causal theory. Conclusion status wired write/delivery and afforded model response. Source: SRC-1 `run_search.py:168-253,595-624`; `search/reflector.py:94-104,617-629`.


>   {{node_rel}}/pruned_children.md — READ THIS FIRST. All previous children of this
>                                  node were pruned (score fell too far below the
>                                  parent). Each entry has the prior.json hypothesis,
>                                  rationale, and verifier verdict.
>                                  You MUST NOT repeat any of those approaches.
>                                  Check `ls {{node_rel}}/children/` so your new
>                                  proposals use names that don't conflict with
>                                  existing dirs (including hidden .pruned_* ones).
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

RTE-10 — Baseline continuation subroute refining RTE-7. Trigger next vanilla iteration after retained/replayed packets. Python writes OBJ-14 history selecting last10 attempts and up to400 summary characters and stages it for BAP-1. Supplied adapters usually leave summary empty: AutoLab returns neither summary field; FIRE clears conclusion; resume reads only agent_summary whereas live list first tries agent_conclusion. Scores/delta/action and inherited state still guide later run. Persistence packet list/history_shown.md/staged skill; return next-run context; older entries drop from prompt but remain disk history. No independent semantic admission or novelty check. Conclusion status wired guidance construction, afforded actual model use. Source: SRC-1 `run_vanilla.py:77-98,164-191,235-245,319-325`; `benchmarks/autolab/__init__.py:234-243`; `benchmarks/fire_bench/__init__.py:201-210,340-345`.

RTE-11 — Reflector resume subroute refining RTE-5. Trigger next initialization/expansion; local OBJ-7 session ID selects exec resume, otherwise fresh exec. Return external model result or error; session metadata merged for later calls, nonzero resume deletes handle. Retained provider payload is excluded/opaque; local token metadata is not context content. Source docstring says fresh calls but executable branch resumes. Consumer external CLI, channel process arguments; explicit recovery fallback, no established memory expiry policy beyond it. Conclusion status wired invocation and recovery, uninspected actual successful recall or benefit. Source: SRC-1 `search/reflector.py:10-12,326-353,397-475`.


>     if session_id and result.returncode != 0:
>         print(f"  [reflector:codex] resume failed (exit {result.returncode}) — "
>               f"clearing saved session state")
>         session_file.unlink(missing_ok=True)
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`


### Claims

CLM-1 — Budget-adaptive plan-tree search shifts exploration toward exploitation as remaining budget decreases. Source claim conclusion status: claimed; scalar alpha and stochastic weighting wired, performance benefit uninspected. Source: SRC-1 `README.md:7-12,74-98`; RTE-2. Q propagation and cost/accounting limits qualify interpretation.

CLM-2 — Autonomous research plan execution and reflector-generated children, with evaluation on FIRE-Bench, AutoLab and MLE-Bench. Source claim conclusion status: claimed; shipped registry supports FIRE/AutoLab and conditional unavailable terminal_bench dispatch, not an inspected MLE adapter. Launch/loop wired, experimental benefit and autonomy within excluded model internals uninspected. Source: SRC-1 `README.md:7-20`; `benchmarks/registry.py:8-33`. This is a scope limit, not a claim that MLE experiments never occurred.


> Code for **PrimeScientist**, a budget-adaptive tree-search framework for
> autonomous research agents. Each tree node is an *experimental plan*
> executed by a coding agent (Codex); a *reflector agent* reads each result and
> proposes child plans. A budget-adaptive selection rule (BAVT,
> `α = 1/r_t`) shifts the search from exploration to exploitation as the
> token budget is consumed.
> 
> Evaluated on three benchmarks:
> 
> - **FIRE-Bench** — research-paper replication, scored by RAGChecker F1.
> - **AutoLab** — systems-engineering code optimization, scored by throughput ratio.
> - **MLE-Bench** — Kaggle-style ML engineering.
> 
> Baselines: a **linear AutoResearch** edit-run-keep-or-revert loop
> --- `README.md` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

### Evidenced absences

ABS-1 — No closed automatic cross-task insight-production route found within the inspected entry surfaces at SRC-1. Search boundary: run_search.py, run_vanilla.py, search/reflector.py, benchmarks/base.py, benchmarks/autolab/__init__.py, benchmarks/fire_bench/__init__.py and both benchmarks/fire_bench/agents/codex/run.py/run_inherit.py. Query: commit-addressed Git grep -n -E 'insight|insights_dir', followed by inspection of every referenced write/copy/call site and initialization/reflection prompts. Findings are directory creation, empty touch, imported copy, staging and read paths; no invoked extraction/shared-store write-back. Source: SRC-1 `search/reflector.py:58-90,245-323,503-543,595-634`; `run_search.py:450-495,652-653`; `benchmarks/fire_bench/agents/codex/run.py:23-54`. Conclusion status absent within this boundary only. Comments promising later filling do not implement it; external authors can still supply files. Prevents automatic cross-task trace-learning classification, not cross-task reading. Other missing provider/benchmark details remain limitations, not absence records.



>     if insights_dir and insights_dir.exists():
>         for f in insights_dir.glob("*.md"):
>             if f.stem != f"{task}_insight":   # skip this task's own file
>                 shutil.copy2(f, local_insights / f.name)
> 
>     # Create empty insight file for this task — filled by reflector after real runs
>     root_node.insight_path.touch()
> --- `search/reflector.py` @ `29971beac6f4f4b41309b1326762e1b83ceece98`

### Behavioral-authority paths

BAP-1 — Coding agent consumes staged native skill and inherited code through filesystem/initial task prompt; instruction force for current run, code operational force when executed. Staging is wired, automatic skill activation remains an external Codex contract. Source: SRC-1 `benchmarks/utils.py:204-258`; RTE-3.

BAP-2 — Reflector consumes packet/log brief/priors/sandbox evidence and optional insights through prompt-directed file reads and resumed context. Force: instructions plus evidence/advice; horizon next proposals and later rounds. Literal prior estimates are model predictions, not warrant. Source: SRC-1 `search/reflector.py:106-323,576-634`; RTE-5, RTE-6.

BAP-3 — Deterministic selector/pruner consumes Q/P/cost/result fields through JSON/TSV reads. Force: ranking, eligibility and stop/prune control; horizon current/later search. This operational authority licenses no scientific conclusion independently. Source: SRC-1 `search/tree.py:162-255`; `run_search.py:506-653`; RTE-2, RTE-4.

## Runtime account

Ordinary invocation selects a task, model, benchmark and output directory. A fresh reflector sees the instruction and optional other-task insight files, writes root plan, and returns to Python. The scheduler selects an unrun node; adapter stages plan, copies baseline/parent code, runs external Codex, evaluates outputs and returns a score packet. Python retains or prunes and updates statistics. At an evaluated node it requests differentiated child plans and prior explanations. Remaining logged budget raises alpha, sharpening sampling. Completion prints highest aggregated-Q node and ledgers; stored tree remains the source of truth.

Principal is the CLI operator; filesystem/process/API authority flows through the process environment and chosen launchers. The harness controls scheduling and local state but not the internal tools/weights/skill matching of Codex. Models propose plans/code and, in FIRE, judge conclusions; Python computes traversal/pruning; task authors supply objectives/reference evidence. Humans configure scope/budget/model and can stop externally, but no additional per-child approval step is implemented by the inspected launch commands. Operating mode is bounded task experiments and a linear baseline, not a standing open-request assistant.

Material revisions include root/child plans and rationale admitted on structural existence; code inherited and admitted by score; scalar statistics affecting future scheduling; and retained pruning/history advice affecting proposals. None alone demonstrates model-parameter change or recursive rewrite of the outer search engine. Every route's source-derived guidance and theory links are separated above. Scores can falsify a task outcome expectation when valid, but a lower score alone does not determine which causal explanation is wrong.

| Static forcing case | Evidence | Supported result and limit |
|---|---|---|
| Missing plan/bad prior | RTE-5 `run_search.py:113-148,259-319` | Missing plan archives; malformed/missing estimate defaults0.5; detailed rationale not validated |
| n_runs>1 and low child score | RTE-4 `run_search.py:348-416,558-580` | Maximum run chosen, other returned costs charged; pruned score excluded from ancestor averages |
| Budget reaches limit during a long call | RTE-2/RTE-3 launch/check anchors | Outer stop occurs after return; not a universal hard token/time cap |
| Resume/copy/run failure | RTE-1/RTE-7 and reflector anchors | Stale resume clears local session; tree no-packet can repeat, vanilla aborts after3; failed best-copy can diverge from recorded best score |

Execution preflight: **no dynamic check planned**. Considered deterministic selector fixtures, no-packet retry and staging/verifier replay. Static code suffices to bound these control paths; full execution would require external CLI/models, credentials, containers/data and expense. No target code, model call, container or benchmark test was run. No unexecuted check supplies negative evidence.

| Route | Immediate return | Later read-back and delegated visibility | Selection predicate | Invalidation/expiry | Activation/effect limit |
|---|---|---|---|---|---|
| RTE-1 | Root/resumed tree or failure | Files/session reused by scheduler/reflector | Existing root stats or force-init | Force-init deletes listed run state, preserves task insights | Initialization wired; plan semantics unknown |
| RTE-2 | Next node/final best-Q print | Stats/budget guide later scheduling | BAVT weights, limits, caps/depth | New scores/budget alter selection; no semantic expiry | Control wired; benefit not observed |
| RTE-3 | Run ID/log/sandbox | Parent code/plan copied into later children | Parent Q>0 and sandbox exists | New run copy; fresh baseline fallback | Delivery wired; native skill use uninspected |
| RTE-4 | Score packet/pruned branch | Q/priors/summaries guide future calls | Maximum repeat score, pruning threshold | Hidden pruned directories excluded; packets remain | Admission wired, outcome warrant task-specific |
| RTE-5 | Child plans or exhausted retries | Prior rationale/files consumed in later reflection | Exists skill, parsed estimate, requested cap | Missing plans archived; resume failure clears session | Reasoning afforded; formal checks narrow |
| RTE-6 | Moved files/brief/synced insights | Reflector reads selected summaries, full log may remain | Active node paths, head/tail, *.md sources | Copies replace local file, no time-decay rule inferred | Presence wired, truthful/causal use unknown |
| RTE-7 | Kept/reverted packet and final summary | Last10 history plus positive best sandbox | Strict score improvement | Old summary excluded from prompt, retained packet; copy replaces best | Code selection wired, improvement beyond score uninspected |



For the added route refinements: RTE-8 returns retained diagnostic reductions, later read by BAP-2 through node-ID/position/regex selection; regenerated files supersede old views, actual use unobserved. RTE-9 returns appended failure memory, later specially named only on all-pruned re-expansion; hidden branch remains but traversal invalidates it, model compliance unobserved. RTE-10 returns staged recent history and later best-state input, selected by recency/task; old prompt entries expire from the window but packets persist, actual model use unobserved. RTE-11 returns external resumed/fresh result, selects by local session identifier, clears handle on nonzero resume; provider payload/expiry/activation remain uninspected. Each is a refinement of the corresponding audited parent route, with no additional authority claim.

## Lens scoping

### Memory/context scope

Full lens triggered by OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6 and OBJ-7 and all seven routes. Frozen input SHA-256 `c69f88cd2906718518e46b55d4274dcbf5b84c8f8d8d5d195432d82f5899e1cc`. Includes every shipped plan/rationale/log/history/state/insight and inherited-code route; excludes external provider context internals except their exposed resume contract. Fresh specialist completed; profile reconciled below.

### Epistemic scope

Full lens triggered by hypotheses/rationale, scientific conclusions, evaluator/reference comparisons and operational selection. Standalone procedure used locally over SRC-1, all material routes and CLM-1/CLM-2. Scientific task validity outside the sampled evaluator boundary and actual candidate-linked learning remain uninspected.

## Lens outputs

### Memory/context lens

The fresh specialist report's complete profile is integrated in frontmatter. Input hash, method hash, source pin, complete status and exact report bytes were checked. Its local proposals are mapped in Reconciliation; substantive findings and their evidence are retained on canonical records, so this result does not require opening the specialist file.

Memory is source-owned files plus operative in-memory packet lists. Plans/reasons establish natural-language and structured statistics/code establish symbolic material, but copied sandbox payloads are unrestricted. Overall representational form therefore remains not determinable. External resumed-provider context is explicitly excluded from aggregate storage/form; only its handle and boundary behavior are included.

The qualifying trace-fed set includes score-to-Q continuation under RTE-2/RTE-4, model-produced plans/priors under RTE-5, session-log and verifier reductions under RTE-8, failed-approach reminders under RTE-9 and vanilla next-run history under RTE-10. All have later consumers and persisted guidance/control, even when they add no new scientific claim. Mere raw logging, arbitrary sandbox copying, session identifiers and insight imports are not independently learning. The shared horizon is per-task; statistics update online and proposals/reductions/history are staged between trials. Distilled outputs are prose and symbolic fields/code. Trace learning is wired in the comparison sense, without implying conjectural learning, observed activation or capacity improvement.

Push includes orchestrator-chosen node/task/parent plans and workspaces, coarse available-file/head-tail/recency selection and lexical verifier-metric extraction. Numeric stochastic ranking has no exact controlled signal label; identifier maps only subsequent branch-specific delivery. Reflector requested shell reads are pull, with relevance decisions afforded to the model. Staging is wired while native skill activation/model consumption remains afforded. Pruned reminders have targeted delivery only after all siblings are pruned; broader disk availability does not guarantee reading. Tree summaries are printed for the operator, not injected into reflector prompts.

Curation includes reductions/consolidation, plan evolution, branch invalidation with retained history, best-workspace promotion and afforded hypothesis synthesis. Prompt limits and rationale/novelty requirements are not semantic admission checks. Vanilla continuation normally contains scores/actions without a useful account of changes; its successful guidance route must not be described as rich learned lessons. Imported insights supply possible cross-task context, but ABS-1 excludes automatic source-owned cross-task learning. Faithfulness remains not determinable without a recalled-content-dependence probe.

### Epistemic lens

#### 1. Source-and-claim boundary

System/revision: see Run identity and SRC-1. Declared scope: the outer search/improvement plane with the shipped execution/evaluator interfaces; excluded inner Codex/provider operations and exhaustive task validity remain as in Boundary and evidence. Question: which routes produce, test or accept truth-apt hypotheses/conclusions, and what do score-driven operational choices license? Assessed route families: RTE-1 initialization/resume, RTE-2 selection, RTE-3 task execution, RTE-4 evaluation/pruning, RTE-5 diagnosis/proposals, RTE-6 retention/context and RTE-7 linear adaptation. Unassessed families: inner model theory formation, every scientific task's evidence design, private provider state and deployed experiments. Missing candidate-linked runs prevent observation/causality claims. Claims CLM-1 and CLM-2 are source-native README claims; implementation, prompts and reported operation remain separate SRC-1 evidence layers.

#### 2. Epistemic-object inventory

Generic identity/form/storage are canonical-owned; see named objects rather than treating this overlay as a new register. OBJ-3 and OBJ-5 heterogeneous aggregates are disposed through their parts below.

| Object | Source/input and producer/consumer | Candidate truth-apt content and role | Evidence/limit |
|---|---|---|---|
| OBJ-1 | Reflector from task instruction/results, then coding agent | Plan is primarily an instruction; embedded factual assumptions or causal predictions require instance-level interpretation | RTE-1/RTE-5 anchors; file existence does not validate assumptions |
| OBJ-2 | Reflector from score/log/sandbox, then later reflector and prior scalar selector | Hypothesis/rationale about why an intervention improves outcome; estimated expected score and risks | SRC-1 `search/reflector.py:260-276,307-321`; interpretation is model-produced, actual operative use uninspected |
| OBJ-4 | Coding agent from baseline/parent state, then verifier/child agent | Executable implementation and experiment outputs; a program is an intervention, not automatically an asserted explanation | RTE-3/RTE-4 anchors; actual scientific claims separately OBJ-8 |
| OBJ-8 | Agent experiment/log output, then evaluator/reflector | Final scientific conclusion and its generalized extracted version | SRC-1 `benchmarks/fire_bench/eval/RAGChecker/eval.py:190-221`; extraction preservation and process validity uninspected |
| OBJ-9 | Benchmark authors/reference code, then judge/verifier | Expected conclusion or expected output and objective | RTE-4 source anchors; supplied warrant, not independently accepted by this analysis |
| OBJ-10 | Task verifier/model judge, then scheduler/reflector | Claim about test correctness/performance or agreement with reference | RTE-4 anchors; metric scope cannot be extended to all scientific truth |
| OBJ-11 | Python derives Q/visits/prior/budget from recorded values, then selector | Descriptive statistics and operational policy state | RTE-2/RTE-4 anchors; Q is a subtree-history aggregate |
| OBJ-12 | Agent/verifier observations retained and excerpted, then reflector | What execution apparently did or returned | RTE-6 anchors; retained claims/logs do not attest experiment fidelity |
| OBJ-13 | Python combines failed-branch rationale/score/verdict or recent iteration summaries, then model | Mixed retained observation plus instruction against repeating failed approaches | RTE-4/RTE-7 anchors; lower score does not identify a causal error |
| OBJ-6 | External insight files copied/read, then reflector/agent | Possible empirical discoveries, content not inspected | RTE-1/RTE-6 anchors; production absent within ABS-1 search boundary, external warrant unknown |
| OBJ-7 | CLI/session-state parser, then resumed external process | Identifier/counter control, no required candidate truth-apt output | RTE-5 anchors; contents of external context uninspected |

#### 3. Authority-route ledger

Rows split functions even when the same route owns them. Architectural status is separate from conclusion status and activation. All code rows are unobserved implementations; source prompts alone do not prove semantic reasoning. BAP references supply consumer/channel/force/horizon from canonical records.

| Route/function | Architectural status; content/update relation | Target, evaluator/condition and timing | Result, epistemic license and operational authority | Source/claim/mismatch/limit |
|---|---|---|---|---|
| RTE-1 / content transformation | implemented model-call interface, doctrine only plan semantics; non-truth-apt policy/content update: root plan | OBJ-1; reflector reads instruction and relevant insights on new task | Produces executable guidance BAP-1; no truth license from initialization | SRC-1 `search/reflector.py:58-90,503-543`; CLM-2; semantic assumptions uninspected |
| RTE-1 / lineage/freshness/recovery | implemented; no content change | Saved tree/session/files; existing root or force-init | Resumes operational state or deletes listed run artifacts; BAP-3 | SRC-1 `run_search.py:451-502`; CLM-2; no evidence refresh/semantic endorsement |
| RTE-2 / content transformation | implemented; truth-apt transformation: entailed derivation | OBJ-11 alpha/statistics from logged inputs and elapsed time | Correct formula within supplied values; changes selection BAP-3 | SRC-1 `run_search.py:85-111`; CLM-1; accounting omissions prevent exact total-spend inference |
| RTE-2 / operational admission/selection/consumption | implemented; no content change | Nodes/OBJ-11; stochastic Q/P weights, depth/cap/budget | Selects next task expenditure or stops; no scientific acceptance; BAP-3 | SRC-1 `search/tree.py:162-255`; CLM-1; rank is not warrant |
| RTE-3 / operational admission/selection/consumption | implemented staging/launch; no content change | OBJ-1 and OBJ-4; skill exists, parent Q>0/sandbox available | Delivers instruction/code BAP-1 and launches external execution | SRC-1 `run_search.py:348-416`; CLM-2; actual native skill activation uninspected |
| RTE-3 / behavior/policy adaptation | implemented delegated code-edit interface; non-truth-apt policy/content update: experimental implementation | OBJ-4; coding agent follows task/plan using host tools | New task code/results, candidate for evaluator; BAP-1 | AutoLab/FIRE launch anchors on RTE-3; CLM-2; model decisions/internal checks uninspected |
| RTE-3 / content transformation | not determinable at inner reasoning, implemented output interface; truth-apt transformation: indeterminate | OBJ-8 agent conclusion from experiment/log | Candidate statement for evaluation, no truth license before checking | RTE-3/CMP-4 anchors; CLM-2; excluded cognition could copy, derive or conjecture |
| RTE-4 / check/evidence production | implemented; truth-apt transformation: acquisition/import | OBJ-4 task program against OBJ-9 reference/test contract in AutoLab | Produces OBJ-10 outcome, operational reward consumed BAP-3 | SRC-1 `benchmarks/autolab/__init__.py:278-389,543-658`; CLM-2; sample verifier licenses tested cases only |
| RTE-4 / content transformation | implemented model-call interface; truth-apt transformation: indeterminate | OBJ-8 extracted/generalized conclusion; summarizer removes numbers/methods/artifact references | New evaluation input; preservation intended but not verified; evaluator has advisory epistemic judgment | SRC-1 `benchmarks/fire_bench/eval/RAGChecker/utils.py:201-223`; CLM-2; could preserve gist or change scope |
| RTE-4 / check/evidence production | implemented model-evaluator interface; truth-apt transformation: indeterminate | OBJ-8 versus OBJ-9 reference, model extractor/checker | OBJ-10 F1/precision/recall judgments, not formal proof; controls ranking BAP-3 | SRC-1 `benchmarks/fire_bench/eval/RAGChecker/eval.py:190-221`; CLM-2; agreement does not establish experimental process |
| RTE-4 / disposition/acceptance | implemented; no content change | Node candidate score; optional child<parent Q-threshold prunes, otherwise retained | Admits branch for future search; no claim-by-claim acceptance; BAP-3 | SRC-1 `run_search.py:551-580`; CLM-1/CLM-2; even non-improving nodes can remain |
| RTE-4 / retention | implemented; no content change | OBJ-10/OBJ-12/OBJ-13; packets saved, pruned directories hidden, summaries appended | Evidence remains inspectable for BAP-2; retention is not acceptance | SRC-1 `run_search.py:168-253,322-343`; CLM-2; hidden state excluded from traversal |
| RTE-4 / content transformation | implemented; truth-apt transformation: entailed derivation | OBJ-11 Q/visits from admitted rewards; max of repeated outcomes selected first | Conditional numeric aggregate; future selection BAP-3 | SRC-1 `search/tree.py:84-93,145-152`; `run_search.py:348-416`; CLM-1; not expected scientific reliability |
| RTE-4 / behavior/policy adaptation | implemented; non-truth-apt policy/content update: branch weights/eligibility | Numeric outcome changes next selection or branch exclusion | Outer search behavior responds to score BAP-3; explanation need not be criticized | RTE-2/RTE-4 anchors; CLM-1; no guaranteed capacity gain |
| RTE-5 / content transformation | implemented prompt/invocation; doctrine only content-directed reasoning; truth-apt transformation: ampliative conjecture | OBJ-2 hypothesis/rationale from earlier outcomes, reflector proposes different bets | Candidate explanatory expectation and next plan BAP-2/BAP-1 | SRC-1 `search/reflector.py:145-168,260-276,307-321`; CLM-2; no observed theory use |
| RTE-5 / check/evidence production | doctrine only for semantic diagnosis; no content change | OBJ-2 mechanism or failed setup, reflector compares logs/verifier and prior trials | Potential criticism of stated cause/expected effect; may revise plan BAP-2 | SRC-1 `search/reflector.py:106-178,180-238`; CLM-2; scalar failure alone does not identify theory error |
| RTE-5 / disposition/acceptance | implemented; no content change | OBJ-1 plan-file existence and OBJ-2 estimate parse | Admits proposal structure, missing file archived/default prior0.5; BAP-3 | SRC-1 `run_search.py:113-148,259-319`; CLM-2; no rationale/semantic check |
| RTE-5 / retention | implemented filesystem interface; no content change | OBJ-1/OBJ-2 and session state | Later reflector can inspect reasons, resume requested via BAP-2 | SRC-1 `search/reflector.py:326-353,374-475`; CLM-2; actual reliance/provider memory unknown |
| RTE-6 / content transformation | implemented; truth-apt transformation: non-ampliative reshaping | OBJ-12 logs to head/tail, selected artifacts/insights copied | Preserves selected text and lineage, loses middle context in brief; BAP-2 | SRC-1 `search/reflector.py:546-634`; CLM-2; source remains available, complete interpretation not guaranteed |
| RTE-6 / retention | implemented; no content change | OBJ-4/OBJ-12 selected sandbox/log moved into node | Later evidence/code read-back available BAP-1/BAP-2 | SRC-1 `run_search.py:322-343`; CLM-2; not an accepted-knowledge lifecycle transition |
| RTE-6 / operational admission/selection/consumption | implemented delivery interface, doctrine only relevant-file reading; no content change | Node-selected logs and cross-task insight files | Prompt/file context BAP-2/BAP-1; no warrant from source presence | RTE-6 anchors; CLM-2; ABS-1 bounds cross-task writer limits |
| RTE-7 / content transformation | implemented; truth-apt transformation: non-ampliative reshaping | Recent packet actions/summary to OBJ-13 last10 clipped history | Makes retained outcome visible BAP-1; no new causal evidence | SRC-1 `run_vanilla.py:63-98,235-239`; CLM-2 baseline; summary may be absent |
| RTE-7 / disposition/acceptance | implemented; no content change | OBJ-4 candidate score strictly>best | Operational keep/revert for later iterations; BAP-3 then BAP-1 | SRC-1 `run_vanilla.py:260-268,303-318`; no separate claim; scalar criterion does not accept explanatory truth |
| RTE-7 / lifecycle integration | implemented only for operationally accepted code; no content change | Kept code copied into best_sandbox then later seeded execution | Post-admission task implementation changes BAP-1; no scientific-claim lifecycle inferred | SRC-1 `run_vanilla.py:105-116,241-245,303-318`; no separate claim; copy failure can desynchronize score/bytes |
| RTE-7 / lineage/freshness/recovery | implemented; no content change | Saved packets reconstruct prior actions; best files retained on revert | Resume/rollback of task state; no provenance or truth revalidation | SRC-1 `run_vanilla.py:164-191,303-318`; no separate claim; missing best bytes not reconstructed |

The scalar/reference checks serve different evaluator domains; no common epistemic oracle is assigned. Acceptance rows state operational use, while truth-apt candidate lifecycle below remains separately unresolved.

The added refinements preserve separate functions: RTE-8 content transformation is implemented non-ampliative reshaping of OBJ-16/OBJ-17, with BAP-2 advisory diagnostic force, no scientific license; RTE-9 retention is implemented for OBJ-15 and operational selection is a separate implemented instruction-delivery function on all-pruned re-expansion, BAP-2, no semantic veto; RTE-10 content transformation is implemented non-ampliative history formatting for OBJ-14, followed by implemented staged delivery/afforded model consumption BAP-1, no new evidence; RTE-11 lineage/freshness/recovery is implemented handle-based continuation, no content change established, with external payload/activation not determinable. Targets, triggers, predicates, results and source anchors are those canonical records; no additional public claim is introduced. Their limitations are scope/activation, not mismatches requiring a new evaluator.

#### 4. Per-object lifecycle disposition

For OBJ-2, transformation is **ampliative conjecture**: predicted cause/benefit is not entailed by earlier scores. Relevant routes RTE-5, RTE-3 and RTE-4. Observation/anomaly: RTE-4 implemented diagnostic/result capture and RTE-5 doctrine only interpretation. Conjecture: RTE-5 implemented invocation with doctrine only semantic formulation. Derived consequence: RTE-5 doctrine only hypothesis/expected improvement and executable plan. Test/evidence: RTE-3/RTE-4 implemented experiment/evaluation interface, RTE-5 doctrine only claim-directed diagnosis. Acceptance: RTE-4 implemented branch-score disposition; criterion lower-than-parent threshold for exclusion, intended use continued search, but no separate implemented acceptance criterion for the causal explanation. Lifecycle integration: RTE-5 doctrine only later reliance on retained hypothesis/rationale; retaining prior.json does not itself establish this phase. **Observed candidate state: no instance observed for every phase.** Accepted explanatory scope is unestablished; missing evidence is an actual hypothesis used in decisions, valid test of its stated content and subsequent reliance/capacity. Sources: OBJ-2/RTE-5 quotations and RTE-4 implementation anchors.

For OBJ-1, transformation is **indeterminate** for truth-apt embedded content, with non-truth-apt instruction as the main declared role. A plan may import facts, derive a procedure from a theory or propose causal predictions. Lineage is task instruction plus earlier files; implementation checks existence and prior scalar only. Needed evidence is an actual plan, premises and decision trace to decide preservation/entailment/ampliation. Its procedural update alone has no discovery lifecycle; candidate truth claims cannot be inferred from a filename.

For OBJ-8, transformation is **indeterminate** across the excluded coding agent's conclusion production and implemented model summarization. Possible classes are copied/acquired claim, entailed experimental calculation, ampliative scientific interpretation or changed/generalized meaning. Preserved lineage is log location and extracted response; source text may include numbers/methods deliberately omitted for evaluation. RTE-4 provides reference-agreement checking and operational selection, not independent proof of conclusion truth or process validity. No candidate instance was inspected; a linked experiment/conclusion/extraction/judge record is needed to distinguish classes and lifecycle phases.

For OBJ-9, transformation is **acquisition/import** of supplied reference conclusions and expected-output/objective code. Discovery lifecycle: not applicable to importing these supplied authorities. The actual bundled reference mapping is inspectable, but its scientific warrant and all test domains are not independently assessed. RTE-4 uses it as oracle within the named evaluator's scope; it does not make the reference infallible.

For OBJ-10, AutoLab observed measurement/assertion is **acquisition/import** from task execution, followed by reward arithmetic; discovery lifecycle is not applicable to recording/scoring that result. Formal arithmetic can be an entailed derivation relative to trusted inputs. FIRE model semantic scoring has **indeterminate** preservation/entailment because extraction/checker judgments are opaque here; it could make ampliative or erroneous entailment judgments. Warrant is bounded to the referenced scoring protocol, not all experimental validity. Candidate-linked traces/design and judge checks are missing.

For OBJ-11, transformation is **entailed derivation** of counts/means/weights and non-truth-apt policy-state change under RTE-2/RTE-4. Discovery lifecycle: not applicable. Premises are recorded values; the computation does not establish their empirical truth. Read-back changes scheduling but is not knowledge acceptance.

For OBJ-12, transformation is **acquisition/import** followed by **non-ampliative reshaping** into excerpts under RTE-6. Discovery lifecycle: not applicable. Text selection preserves literal portions, not complete context or source veracity; full log may remain retrievable. Missing evidence is original execution authenticity and meaningful linkage to claimed hypothesis.

For OBJ-13, retained hypotheses/outcome snippets undergo **non-ampliative reshaping**, while the instruction not to repeat a pruned approach is a non-truth-apt policy update. Discovery lifecycle is not applicable to deterministic formatting or instruction creation. RTE-4/RTE-7 preserve failed-approach evidence for a model, not a proof that every described approach is intrinsically false or inferior.

For OBJ-6, transformation is **indeterminate** outside the inspected copy/read interfaces. Its lineage is preexisting external insight files; RTE-1/RTE-6 copying is acquisition/import, while producing warranted cross-task discoveries remains unresolved. Needed evidence is its writer, source observations and later consumer; do not infer a lifecycle from the term insight. ABS-1 establishes no closed source-owned production loop within its recorded boundary; imported files remain usable but do not establish automatic cross-task learning.

No lifecycle record for OBJ-4's executable-state part: no required candidate truth-apt output for that part; relevant direct-adaptation routes RTE-3, RTE-4 and RTE-7. Scientific statements/results within outputs are separately OBJ-8/OBJ-10. No lifecycle record for OBJ-7: no candidate truth-apt output for this identifier/control object; relevant update/recovery route RTE-5. OBJ-3 and OBJ-5 are aggregates with the separate dispositions above.

For OBJ-14 history, OBJ-15 reminder and OBJ-16 brief, transformations and warrant follow OBJ-13/OBJ-12: non-ampliative trace reshaping with no discovery lifecycle; directive parts are non-truth-apt policy updates. For OBJ-14 best workspace, no candidate truth-apt output is required; adaptation follows OBJ-4/RTE-7. For OBJ-17, verifier reduction is non-ampliative reshaping of recorded observations, while baseline diff is entailed text/state difference within the compared files; neither licenses a causal explanation. RTE-8, RTE-9 and RTE-10 provide retention/use with no observed semantic acceptance. The full original traces, actual candidate reasoning and valid experiment linkage remain necessary for stronger warrant.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design support | Implemented routes | Observed-run/causal support | Supported conclusion and mismatch |
|---|---|---|---|---|
| CLM-1 | README BAVT remaining-budget concentration; SRC-1 `README.md:74-98` | RTE-2 weighting/stopping and RTE-4 state updates | None inspected; no causal comparison | Wired adaptive sampling over recorded values. It does not establish better research per token, exact cost accounting or hard in-flight caps |
| CLM-2 | README agent execution/reflector children/benchmark scope; source prompt contracts | RTE-1, RTE-3, RTE-4, RTE-5, RTE-6 and alternative RTE-7 | None inspected; no component-effect attribution | Concrete outer research-search orchestration with delegated execution. Scientific conclusions and rationale need evaluator/experiment-specific warrant; full reported suite and inner autonomy are not demonstrated here |

#### 6. Bounded conclusion

PrimeScientist retains instructions, hypotheses, diagnostics, outcome summaries and executable parent state, then changes future proposals and scheduling through named consumers. Its arithmetic and structural checks have narrow enforceable semantics. AutoLab's sampled verifier compares program behavior/performance under a task contract; FIRE compares a generalized conclusion to supplied reference text using model judgments. These checks permit operational selection, not automatic acceptance of every causal or scientific claim.

The explicit hypothesis/rationale/risks contract and request to distinguish setup failure from tested low-scoring hypotheses afford content-directed criticism. The source does not establish that a model actually used those explanations, revised reliance for the right reason or improved future capacity. Direct plan/code adaptation and score-based search are wired without requiring a truth-apt theory at every step. Rationale retention and source selection preserve potential material for later reasoning, but neither context presence nor operational use resolves the missing epistemic links.

## Reconciliation

Specialist mappings: MEM-OBJ-1 → OBJ-14; MEM-OBJ-2 → OBJ-15; MEM-OBJ-3 → OBJ-16; MEM-OBJ-4 → OBJ-17; MEM-RTE-1 → RTE-8; MEM-RTE-2 → RTE-9; MEM-RTE-3 → RTE-10; MEM-RTE-4 → RTE-11; MEM-ABS-1 → ABS-1. MEM-ABS-2 is an evidence limitation on RTE-3/RTE-5, not an absence record; its profile reference maps to RTE-3 with duplicate references removed. Existing OBJ-1 through OBJ-7 and RTE-1 through RTE-7 preserve their original referents; later subdivisions refine them rather than reassign IDs. Complete tokens were mapped exactly and accepted IDs are declared once.

All nine material specialist issues are resolved: optional cross-task import is separated from missing source-owned production; resume handle is not memory payload and executable resume overrides stale fresh-call prose; vanilla summaries are normally empty; Q differs from own sandbox reward; proposal size/rationale/novelty/diff lineage are instructed but not enforced; all trace-fed diagnostic/history branches enter the profile; printed tree summary and stale filename hint are limited as documented; arbitrary copied payload form stays not determinable; and model activation remains afforded while deterministic selection/reduction is wired. The added diagnostic byte/character and metric-tail bounds are kept on OBJ-17. No issue is silently strengthened into observed behavior.

Parent messages supplied source-checkable questions about Q, pruning, vanilla history and FIRE filtering; the report retained the answers. Those are coordinated checks, not independent convergence claims. Supplemental parent object IDs were sent late; the specialist retained local proposals against unchanged input, so this mapping resolves overlaps without changing the frozen commission. The local epistemic lens retains separate transformation/check/disposition/retention/integration rows and leaves theory use/improvement uninspected.

## Bounded synthesis

The strongest supported contribution is a wired plan-search loop that retains explicit rationale, outcome/diagnostic evidence and executable parent state for later proposals. BAVT and pruning use those retained values directly; reflector prompts demand competing hypotheses and reasons grounded in failures. The plan-generation and evaluation interfaces form a concrete route for evidence-responsive adaptation, while actual theory use and improved future capacity remain unobserved.

Operational selection is stronger than epistemic certification. AutoLab's sampled verifier tests a specific correctness/performance contract. FIRE's score compares a generalized extracted conclusion with supplied reference answers through model judges. Neither score automatically warrants the proposing explanation. Maximum-of-repeats, ancestor-averaged Q, filtered adverse branches and estimated soft budget checks must remain visible when interpreting best score or efficiency claims.

Self-improvement at the declared boundary is a standing **wired** procedural adaptation route for plans/task code and selection, with semantic proposal quality **afforded** and actual improvement **uninspected**. Conjectural learning is **uninspected**: formulation and criticism are afforded but their operative use and attributable capacity gain were not observed. Narrow reflection is **afforded** where the reflector represents this search system's plans, failures and approaches and proposes changes to later behavior; actual causal representation-mediated changes and a reflective theory-builder remain uninspected. Task-code optimization is not automatically self-modification of the outer controller. These properties are separate claims.

## Limitations

External Codex skill activation/context and exact provider weights prevent claims about implemented inner cognition, faithful use or fixed model parameters. No candidate-linked experimental result was inspected, so implementation cannot establish observed benefit. Full task-suite correctness, reference-answer validity and deployed resource isolation are excluded. Root/init and external subprocess accounting make budget limits operation-boundary controls rather than absolute spend guarantees. Shipped cross-task insight interfaces need a separately verified production/read-back chain before claiming learned cross-task transfer. Candidate/reason/score artifacts plus controlled interventions, reference audit and runtime observations would resolve these limits.

## Verification and blockers

### Semantic verification

Baseline source-only boundary checked. All seven routes separate immediate return, later memory, selection, expiry, delegated visibility and activation. Q's accumulated-descendant meaning is separate from node execution score/sandbox identity. Evaluator oracle is independently named by mode; numeric comparison does not establish semantic warrant. Model identity and weight fixity are separately bounded. Parent/full-plan versus delta-plan branches and native/container execution alternatives remain explicit. The integrated fourteen-axis scope includes both tree and vanilla paths, diagnostic compaction, inherited arbitrary payloads and imported insights, while excluding external provider context transforms. Checked every trace-fed write on RTE-2, RTE-4, RTE-5, RTE-8, RTE-9 and RTE-10; dependent source/horizon/timing/form axes use the same set. Push selectors name consumer, trigger, input and selected part on each refinement, and pull file reads remain separate. Unknown aggregate form is preserved; no claimed known union hides opaque payloads. All material specialist issues are explicitly disposed, with scoped absence and evidence limitation kept distinct.

### Deterministic validation

Integrated result passed full validation cleanly. Retained quotes matched complete frozen blobs; full-path line ranges stayed within file boundaries. No target execution performed.

### Blockers

None.
