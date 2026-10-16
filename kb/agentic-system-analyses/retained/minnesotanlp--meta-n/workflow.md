---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Meta-n workflow: native task-chain improvement from CLI request through sampled rejection, optional repair and saved results."
run-id: AAS-2026-10-14-meta-n-18c23b6f8bb4-01
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
---

# Meta-n workflow report

## Workflow account

### Selected workflow and evidence

This account follows a fresh native `meta-n --tasks <json> --use-archive` search, with a non-focus child and an enabled quality gate. It examines the optional within-layer repair branch when the gate rejects a proposal. This workflow was selected because it joins the system's defining responsibilities: evaluated baseline, trace-fed improvement proposal, executable composition, rejection, bounded recovery and delivery. Gate and repair activation depend on configuration; this is a supported configured path, not a claim that every invocation takes it. External SDK solving, consolidation and downstream repropagation are different paths, not additional steps inserted into this workflow ([RT-RTE-native-solve](runtime.md#rt-rte-native-solve), [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-RTE-within-refine](runtime.md#rt-rte-within-refine); SRC-1, `meta_n/main.py`, `meta_n/core/evolutionary_orchestrator.py`).

The evidence is implementation and declared design at the boundary's frozen commit. No model request, target test or search was executed or supplied as observed run evidence. Thus the account establishes coordination and rejection capacity, not an actual repaired strategy, successful completion or measured improvement. Additional inspection in SRC-1 covered the native seed, gate/full-evaluation junction, gate predicate, within-layer repair and terminal result assembly in `meta_n/core/evolutionary_orchestrator.py`; generation/refinement request construction in `meta_n/core/omega.py`; the CLI result and budget-exception branches in `meta_n/main.py`; and final artifact writing in `meta_n/core/run_persistence.py`. These extend the initial inspection, not the frozen source boundary.

### Request and evaluated baseline

The operator supplies tasks, optional verification scripts, provider/model settings and search controls. Archive mode must be enabled before the request can reach baseline evaluation. The selected bare custom-task invocation supplies `--use-archive` explicitly; without it, the startup guard returns status 1 before model-client construction or task loading. Bundled benchmark configuration can enable archive mode by default, but gate/refinement settings do not satisfy this separate startup condition ([RT-RTE-native-solve](runtime.md#rt-rte-native-solve); SRC-1, `meta_n/main.py`).

> if not getattr(args, "use_archive", False):
>     console.print(
>         "[red]Error: --use-archive is required (the linear orchestrator has "
>         "been retired). The bundled benchmark config enables it by default; "
>         "pass --use-archive explicitly if you also pass --benchmark-config "
>         "none or run with bare --tasks.[/red]"
>     )
>     return 1
> --- `meta_n/main.py`

After this startup condition is satisfied, the CLI chooses the executor and solver language, constructs the model client, Ω engine and orchestrator, then calls `run` with tasks, resume choice and run configuration. Software owns scheduling; starting the run is not human approval of each generated injection ([RT-RTE-native-solve](runtime.md#rt-rte-native-solve); SRC-1, `meta_n/main.py`).

For the selected fresh, unseeded native case, `gen0_seed` has depth 1 and no injected chain. The orchestrator passes tasks to the base solver, obtains model-written source, delegates execution to the selected executor and collects scored traces. For custom tasks the executor is host-side `LocalExecutor`; its verification script, when supplied, provides an exit-status reference outcome. Without a verification script, execution success is not an independent correctness oracle. Benchmark task families have their own evaluators. The baseline candidate is archived and written before breeding. This supplies both a scored parent and an initial recovery point ([RT-RTE-native-solve](runtime.md#rt-rte-native-solve), [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary); SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/base_executor.py`).

> seed = await self._evaluate_candidate(seed, seed_solver, tasks)
> self.archive.add(seed)
> result.absorb_candidate_tokens(seed)
> --- `meta_n/core/evolutionary_orchestrator.py`

### Improvement handoff and executable child

Archive policy selects eligible parents using elite reservation and fitness/exploration sampling. The chosen parent's traces and injected chain are passed to Ω with task descriptions, depth, temperature and score comparisons. Ω's request is not a complete copy of all retained state: code samples traces and truncates the context stack before rendering it. Helper-use information scans the original traces but is scoped to the rendered stack. Ω receives a natural-language/source-text request, not access to the archive or authority to schedule candidate admission. It returns parsed preprocessing, helper source and rationale. Empty proposals can be skipped ([RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance); SRC-1, `meta_n/core/omega.py`, `meta_n/core/evolutionary_orchestrator.py`).

> sampled = self.context_manager.sample_traces(traces)
> truncated_stack = self.context_manager.truncate_context_stack(context_stack)
> --- `meta_n/core/omega.py`

Code appends the proposal to the parent's full chain and gives the child a new identity with the archived parent as lineage. Optional helper verification can filter Python helpers before chain construction, but does not value-verify all preprocessing or bash helpers. The actual native solver consumes the full live chain, which can include layers omitted from Ω's request. Preprocessing emits additional context; merged helpers are advertised to the solver and prepended to the outer executable source. Nested layers normally return source to the outer layer rather than each executing an independent task. This is delegation among model generation, code composition and execution responsibilities, not a group of separately autonomous worker agents ([RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection); SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/evolutionary_orchestrator.py`).

### What the gate can reject

For a non-focus child with `gate_tasks > 0`, the orchestrator invokes sampled task execution before full evaluation. Code, not Ω, compares the resulting success/score to the parent baseline. A clearing task must succeed and satisfy the configured relative threshold when a baseline exists. Missing baseline or disabled margin leaves a liveness check. With the protection floor off, the first clearing sample admits the child to full evaluation; with it on, a sampled hard regression vetoes and the gate continues scanning for such a veto. Exceptions on samples are skipped, and no clearing sample yields rejection. This gate is a sampled policy, not all-task non-regression or a universal correctness guarantee (SRC-1, `meta_n/core/evolutionary_orchestrator.py`; [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)).

> cleared = trace.success and (
>     baseline is None or trace.score >= baseline - margin
> )
> --- `meta_n/core/evolutionary_orchestrator.py`

A passing child's gate traces are supplied to full evaluation as precomputed results, rather than automatically re-solving every sampled task. Remaining task evaluation yields the candidate's aggregate and task scores. The orchestrator archives and incrementally saves the evaluated child even if its mean is below the parent's; optional helper non-adoption bars affect per-task-best promotion, not the child's history or mean. Future archive selection and patience, rather than a strict improvement-only archive, govern continuation ([RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

### Rejection and bounded recovery

A gate failure prevents ordinary full evaluation and archive admission of that child. If within-layer refinement is enabled, the proposal is nonempty, the child is non-focus and depth is at least 2, code can make one additional Ω call. If neither gate traces nor child traces exist, the repair helper returns without calling the model. The repair request supplies failing traces, the buggy newest injection, the lower parent chain, task descriptions and score comparisons. Ω samples/truncates this view and adds a fixed directive to preserve the approach and helper names while correcting the code ([RT-RTE-within-refine](runtime.md#rt-rte-within-refine); SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/omega.py`).

The directive presumes that the approach is right and the code is buggy; it is not an independently established diagnosis of why the gate failed. Evaluator feedback motivates the request, but no supplied model output demonstrates correct blame localization. A passing repair therefore would establish neither the directive's causal account nor generalization beyond tested tasks (SRC-1, `meta_n/core/omega.py`; [RT-RTE-within-refine](runtime.md#rt-rte-within-refine)).

> "Emit a CORRECTED version of THAT SAME injection. FIX THE BUG — do NOT "
> "change the approach, do NOT switch algorithms, do NOT start over. Keep "
> "the same helper names and the same overall strategy; make the SMALLEST "
> "edit that makes it run correctly (guard the failing op, fix the "
> "indexing/format/numeric error, handle the edge case the traces show). "
> --- `meta_n/core/omega.py`

The repaired proposal is filtered and built as a new `_refine` candidate attached to the archived parent. It does not mutate or archive the rejected child. Empty repair or another gate failure returns no recovered candidate, with spend counted. A passing repair is fully evaluated, archived and saved. Its repair event separately reports whether its score on the original failure-task subset improved. That event's `accepted` comparison is not the archive veto: archive admission follows gate clearance, while the comparison classifies the outcome (SRC-1, `meta_n/core/evolutionary_orchestrator.py`; [RT-RTE-within-refine](runtime.md#rt-rte-within-refine)).

> accepted = mean_after >= mean_before
> --- `meta_n/core/evolutionary_orchestrator.py`

Earlier archived chains remain available after either failure. Search continues after accounting for the attempt and updating the parent's child count. Native task execution also has its separate optional bounded debug retry loop, retaining the best score. Neither recovery mechanism reverses filesystem, network or other effects already incurred by generated execution; host process limits are not a transaction or a whole-system sandbox ([RT-RTE-within-refine](runtime.md#rt-rte-within-refine), [RT-RTE-native-solve](runtime.md#rt-rte-native-solve), [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary); SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/meta_layer.py`).

### Termination and delivery

Iterations, depth eligibility and patience bound the search. The terminal result distinguishes the best single-chain score from the per-task-best aggregate across potentially different lineages. Optional frozen assembly can further change the reported best candidate without a fresh model proposal or evaluation; that alternate result must not be mistaken for a newly exercised single chain. Adapter-supported test evaluation distinguishes stored per-task-winner execution from reconstructed best-chain evaluation; custom-task delivery does not require an available held-out split ([RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing), [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

Delivery to this workflow's operator means the CLI receives the result, prints its summary and calls final artifact writing, followed by the cost-summary writer. There is no additional deployment handoff or human product-acceptance step established here. Final artifacts expose scores, executable per-task winners, source-chain provenance, archive index and best-chain ancestry. Delivery is distinct from successful search completion: a returned soft budget halt can carry an aborted status, while a hard client budget exception exits without final result writing. The latter leaves a resumable mid-run product rather than a final deliverable ([WF-CLM-delivery-boundary](#wf-clm-delivery-boundary); SRC-1, `meta_n/main.py`, `meta_n/core/run_persistence.py`, `meta_n/core/evolutionary_orchestrator.py`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-delivery-boundary
Label: Final artifact delivery boundary

Claimed operation: a returned search result reaches the operator through CLI reporting and final artifact writing; a hard budget exception deliberately skips that finalization. Distinct identity from [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) and [RT-RTE-native-solve](runtime.md#rt-rte-native-solve): this claim concerns the CLI's completion boundary and final output contract, not candidate admission or solver invocation. It complements their runtime account without declaring another route for those same referents (SRC-1, `meta_n/main.py`, `meta_n/core/run_persistence.py`).

> orchestrator.save_results(result, run_config=run_config)
> _save_cost_summary(output_dir, llm_client)
> --- `meta_n/main.py`

The final writer overwrites the mid-run summary with `result.to_dict()`, atomically writes summary/convergence files and the archive index, and separately writes per-task traces/scripts, oracle provenance and best-chain lineage. Atomic replacement of individual files does not establish an atomic multi-file delivery transaction. The cost-summary writer catches filesystem failure and reports it, so the call sequence is not an invariant that every artifact exists (SRC-1, `meta_n/core/run_persistence.py`, `meta_n/main.py`).

> atomic_json_dump(out_dir / "summary.json", summary_payload)
> --- `meta_n/core/run_persistence.py`

> with open(best_dir / f"{task_id}{ext}", "w") as f:
>     f.write(trace.script)
> --- `meta_n/core/run_persistence.py`

Hard budget exhaustion propagates to the top-level handler, which states why final writing is withheld and exits with status 2. The operator, not an autonomous recovery worker, is told to resume after daily reset. Resume reuses saved archive/checkpoint state; it is not proof of exact replay or complete recovery from a crash between writes ([RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission); SRC-1, `meta_n/main.py`, `meta_n/core/run_persistence.py`).

> # DELIBERATE (F029/F038): save_results is NOT called on the hard-kill
> # path, so summary.json keeps the MID-RUN shape (no total_iterations /
> # run_status).
> --- `meta_n/main.py`

A soft external-spine budget halt is a distinct return path: result assembly sets `run_status` to `aborted_mid` or `aborted_pre_iteration`. Thus neither a saved final-shaped summary nor the printed “Final Summary” alone establishes completed search (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/main.py`).

> if budget_halted:
>     result.run_status = (
>         "aborted_mid" if completed_iterations >= 1 else "aborted_pre_iteration"
>     )
> --- `meta_n/core/evolutionary_orchestrator.py`

This CLI finalization boundary does not establish correct completion detection by every shipped launcher. The Stage 2 CO-Bench launcher skips on summary-file existence, although hard budget exhaustion can leave a mid-run summary. Such an artifact can therefore prevent this launcher's rerun; uniform launcher completion detection and automatic recovery are not established. Operator-directed resume remains the supported recovery described above (SRC-1, `scripts/run_agentic_stage2_cobench.sh`, `meta_n/main.py`, `meta_n/core/run_persistence.py`). Additional inspection of the launcher's skip guard supplies implementation evidence, not observed launcher behavior.

> if [ -f "${OUTPUT_DIR}/${EXP_NAME}/summary.json" ]; then
>   echo "[SKIP] $EXP_NAME — already completed"
>   exit 0
> fi
> --- `scripts/run_agentic_stage2_cobench.sh`

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)

Workflow role: joins baseline evaluation to successor proposal, sampled rejection, full evaluation and future parent selection. Handoff completion differs by recipient: Ω returns a proposal; the executor returns scored traces; the archive accepts an evaluated candidate. None alone is operator delivery. Gate clearance permits more evaluation, not a declaration that every task improved. Reusing gate traces makes earlier execution part of the full candidate's evidence, rather than a separate independent confirmation.

#### On [RT-RTE-within-refine](runtime.md#rt-rte-within-refine)

Workflow role: one bounded recovery opportunity after proposal rejection. Code owns invocation and re-gating; Ω owns proposed repair content. The original archived parent is the repaired candidate's lineage parent, while the repair event names the rejected attempt as the repaired source. `archived=True` denotes gate-based retention; `accepted` denotes matched-subset score comparison. These answer different questions and must not be collapsed into one success verdict. The model's own-approach-preserving directive limits the requested diagnosis; successful diagnosis and repair remain unobserved.

#### On [RT-RTE-native-solve](runtime.md#rt-rte-native-solve)

Workflow role: produces the baseline, gate samples and full-evaluation traces that let the enclosing search compare proposals. Task-local debug retry is separate from injection-level repair: the former revises a task solution using execution feedback, while the latter replaces the newest chain injection under a new candidate identity. Returning executable source or a trace does not itself finalize the CLI's artifact set.
