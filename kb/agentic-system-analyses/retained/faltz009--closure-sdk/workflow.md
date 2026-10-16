---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Closure-SDK workflow account of the current Rust Closure EA bounded neuromodulation experiment, from supplied carriers through corrective feedback to comparison assertions."
run-id: AAS-2026-10-13-closure-sdk-294e6865ca51-01
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
---

# Closure-SDK workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped neuromodulation experiment in SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`. It was selected because one caller connects initialization, repeated perception, prediction commitment, target feedback, final maintenance, comparison and assertions. It is a bounded numerical experiment, **not an established multi-agent workflow**. Within this inspected caller and its correction methods, progression is synchronous Rust control flow; there is no worker delegation or model-mediated task assignment. The supplied runtime records establish the underlying numerical operations. Nothing here constructs an agent workflow by joining unrelated APIs.

The account is implementation-grounded at the frozen boundary, not an execution report. No target example or test was run. The experiment's comments and printed claims of successful measurement are design/reporting text, not observed results. Added inspection covers the complete experiment file and the correction and final-consolidation bodies in SRC-1, `closure_ea/src/three_cell.rs`; these supply implementation evidence and attributed comments only. Other shipped workflows were not audited exhaustively, so this account cannot establish a system-wide absence of agent coordination.

### From supplied problem to repeated correction

1. **The example fixes the task.** `main` constructs a pattern and a true-label carrier with `domain_embed`, plus familiar and disruptive contexts. It creates independent brains with the same `make_brain` configuration and schedules two episodes of 20 rounds, each with eight context inputs before a pattern. The expected answer is the example's literal `true_label`, not a separate judge's determination. Human participation in choosing these constants is not established by caller identity. The outer controller and result consumer are the example itself (SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`; [WF-RTE-regime-comparison](#wf-rte-regime-comparison)).

2. **Each round supplies context, then a pattern.** `run_learning_episode` invokes `brain.ingest(context)` repeatedly, then `ingest_sequence` with the single pattern. The context calls' returns are ignored, but their state effects remain available to the pattern ingestion. The pattern's last `Step` supplies the prediction carrier and hit index. The runtime's channel selection, live-buffer participation, verification, expiry admission and consolidation are described by [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest), not repeated as a new workflow record. There is no child context or return-message boundary: the same mutable brain is used throughout (SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`).

3. **The prediction handoff is one pending slot.** A field hit supplies its carrier; no hit selects `IDENTITY`. The caller maps any hit index to `PredictionSource::GenomeSlot` and commits before evaluating with `true_label`. [RT-OBJ-pending-prediction](runtime.md#rt-obj-pending-prediction) captures the delayed-feedback state, while [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback) supplies its correction evidence. This is an internal state handoff, not delegation. As the runtime report warns, the caller does not preserve the hit's population when naming a genome slot. Buffer-sourced hits therefore do not establish correct source-slot attribution. The separate context/target association write remains supported (SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`, `closure_ea/src/three_cell.rs`).

4. **Target comparison changes memory; it is not an admission review.** Evaluation consumes the pending prediction and compares its geometric gap with `cell_a_threshold`. It credits eligible Response entries, writes the context/target association and updates sequential edges. If the prediction is incorrect, it can weaken the edge to the predicted result. This does not veto the supplied target or roll back the round. Both correct and incorrect feedback proceed through association writing. The caller cannot infer independent target validity from the resulting `correct` flag (SRC-1, `closure_ea/src/three_cell.rs`; [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)).

> if !correct {
>     if let Some(src) = source_idx {
>         let predicted_idx = genome.nearest_index(&pending.predicted);
>         if let Some(pred) = predicted_idx {
>             genome.weaken_edge(src, pred, 1);
>         }
>     }
> }
> --- `closure_ea/src/three_cell.rs`

### Verification, failure and delivery

The caller collects promotion counts only when evaluation returns `Some`. With no pending prediction, the runtime returns `None`; the example's `if let` skips report accumulation without retry or an explicit error result. Its normal sequence commits immediately before evaluation, but source inspection alone does not establish successful execution. This branch is not a semantic rejection of the target. The pending-state consumption and missing-state outcome are supported by [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback). The wrapper increments its cycle counter before that optional feedback result (SRC-1, `closure_ea/src/three_cell.rs`).

At the end of each episode, the caller captures arousal and coherence **before** calling `force_consolidate`; it then adds the final consolidation's promoted-category count. The delivered tuple thus combines pre-final-maintenance tones with a promotion total including final maintenance. It is not a snapshot of every metric after the same final operation. The caller chooses the end-of-episode maintenance time; [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance) supplies the forcing mechanism (SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`, `closure_ea/src/three_cell.rs`).

`main` prints both tuples and their differences. Two assertions check disrupted arousal greater than stable arousal and disrupted coherence less than stable coherence. Only after both assertions does the program print its final verified message. A failed assertion takes Rust's assertion-failure path; the inspected caller has no catch, retry, rollback or replacement procedure. Earlier comparison and success-sounding explanatory text is printed before the assertions, so that text alone is not evidence that the checks passed. The checks address directional tone differences, not prediction accuracy, promotion correctness or successful learning. Their implemented acceptance/rejection boundary is [WF-RTE-regime-comparison](#wf-rte-regime-comparison) (SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`).

Delivery here means an episode tuple returned to the local caller, followed by stdout comparison and, on the passing path, the final verification message. No artifact persistence or later reload is invoked by this example. The separate persistence API in [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration) cannot be appended to this workflow merely because it exists. Recovery from assertion failure is not assigned to an internal worker: any rerun or use of an earlier snapshot would require an additional caller action. Neither successful completion nor measured learning benefit is established by the available static evidence.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-regime-comparison
Label: Bounded regime comparison and assertion delivery

Endpoints and owner: the example's `main` supplies embedded carriers and configured brains to two `run_learning_episode` calls, receives numerical tuples, prints comparisons and asserts two directional inequalities. The controller is compiled Rust code. Context/state effects are repeated mutations of two independent `ThreeCell` instances; the terminal effect is stdout or assertion failure. Operands and tones are numerical, while loop bounds, branches, returned tuple structure and assertion policy are symbolic. SRC-1, `closure_ea/examples/exp_neuromodulated_learning.rs`.

Distinct identity: this route is the outer two-regime scheduling and terminal evaluator, not the ingestion, feedback or maintenance method. It spans [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest), [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback) and [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance), which describe its constituent operations but do not own its two-brain comparison or final assertions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: each episode returns arousal, coherence and total promotions; main prints comparisons and reaches the final verification message only after both assertions pass.
- Later read-back: changed numerical memory participates in later rounds of the same brain through the cited ingestion and feedback routes; this example does not save or reload its result.
- Delegated visibility: inapplicable — no delegated executor; tuples return directly to main and reporting uses stdout.
- Selection predicate: main fixes stable/disrupted contexts, eight context repetitions and 20 rounds; terminal assertions require disrupted arousal greater than stable and disrupted coherence less than stable.
- Invalidation or expiry: constituent ingestion and maintenance can expire or reorganize memory; main constructs separate brains and does not retain them beyond this process's workflow.
- Activation or effect: static wiring makes later rounds consume changed state and makes assertion outcomes control final-message reachability; no supplied execution establishes those effects were exercised.
- Evidence limits: the complete example and selected ThreeCell bodies are implementation evidence only; printed claims do not establish passing assertions, learning efficacy or causal attribution to an individual internal mechanism.

Admission/comparison roles: the example proposes and fixes both regimes, the literal target and the expected directional ordering. Software computes outcomes and can reject terminal verification through assertions. No separate model or per-result human approval is present in this caller. The target is the prediction oracle; the final tone inequalities are a different evaluator, not an oracle for target correctness. Mode is a bounded experiment. Update triggers are repeated inputs and target feedback under compiled geometric guidance; numerical associations and statistics persist between rounds. The assertions do not admit a revised method or reject earlier memory writes. No automatic rollback or retry appears in this caller.

Minimum controller and delivery evidence:

> const CONTEXT_REPS: usize = 8;
> const ROUNDS: usize = 20;
> --- `closure_ea/examples/exp_neuromodulated_learning.rs`

> (final_arousal, final_coherence, total_promoted)
> --- `closure_ea/examples/exp_neuromodulated_learning.rs`

> assert!(
>     arousal_b > arousal_a,
>     "disrupted regime must produce higher arousal_tone: {:.4} vs {:.4}",
>     arousal_b, arousal_a
> );
> assert!(
>     coherence_b < coherence_a,
>     "disrupted regime must produce lower coherence_tone: {:.4} vs {:.4}",
>     coherence_b, coherence_a
> );
> println!();
> println!("  Verified: arousal_b > arousal_a ✓   coherence_b < coherence_a ✓");
> --- `closure_ea/examples/exp_neuromodulated_learning.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)

Workflow role: the episode commits and supplies its fixed true label immediately after pattern ingestion. The caller's `if let Some(eval)` accumulates promotions but supplies no missing-feedback retry. An incorrect prediction is corrective input, not a rejected round. The outer terminal assertions inspect regime tone ordering rather than the prediction's correctness; their failure cannot undo feedback already written.

#### On [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance)

Workflow role: forced level-0 consolidation closes each bounded episode after the two body tones have been copied. Its promotion count is added to the episode total before return. Thus downstream comparison receives pre-force tones and an including-force promotion count, not uniformly post-force state.
