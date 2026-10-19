---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ACE workflow account: sequential offline Finance adaptation from configured invocation through reflection, curation, validation and saved delivery."
run-id: AAS-2026-10-18-ace-007571102a54-01
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
---

# ACE workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped Finance caller in offline mode with batch size one, nonempty training and validation sets, supplied test samples, positive scheduling intervals and the optional bulletpoint analyzer disabled. It is representative because one invocation connects task answering, corrective feedback, retained-playbook admission, validation selection and saved output. It is a bounded labelled-data workflow, not an interactive financial agent or an AppWorld environment run. The missing AppWorld implementation and other evidence limits remain those of the [boundary](boundary.md#boundary-and-evidence).

The account uses SRC-1 at the frozen revision. Direct implementation inspection covers `eval/finance/run.py`'s loader and main invocation, `ace/ace.py`'s run dispatch, single-sample adaptation and offline training tail, and `ace/core/curator.py`'s sequential curation and failure handling. This adds workflow-focused inspection of these paths to the supplied baseline; no new source or evidence layer is admitted. Other transformations below cite the supplied runtime records. No model request, target execution or execution trace establishes successful completion or improvement.

### Request becomes a scheduled run

The operator supplies dataset/task selection, provider and role-model configuration, output directory, scheduling limits and optionally an initial-playbook path. The Finance caller prepares samples and processor, reads initial text if the named file exists, and chooses the sequential orchestrator. These are caller-level decisions, not delegations made by a model (SRC-1, `eval/finance/run.py`; [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)).

> AceCls = ACEBatch if args.batch_size > 1 else ACE
> --- `eval/finance/run.py`

The caller hands `run` the training, validation and test lists, the processor and configuration. `run` rejects an unsupported mode or missing required lists before setting up output paths and saving `run_config.json`. It evaluates the initial playbook on the test set, calls offline training, then evaluates the selected best playbook and saves consolidated results. Python owns each transition. Generator, reflector and curator are model-call roles, not independently scheduling agents (SRC-1, `ace/ace.py`; [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select)).

### Per-sample handoffs and corrective work

For every epoch/sample, `_offline_train` supplies `_train_single_sample` the sample, processor, configuration, epoch/step identifiers and log paths. The initial generator receives question, context, the full current playbook and an empty reflection. It returns response text, reported bullet IDs and call metadata. Code extracts the answer and asks the processor to compare it with the target; neither the generator nor the reflector decides correctness ([RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); SRC-1, `ace/ace.py`).

An incorrect answer causes at most `max_num_rounds` reflection/regeneration rounds. The reflector gets the current response trace, predicted answer, target unless locally withheld, target-derived mismatch feedback and only playbook lines selected by the reported IDs. It does not receive an independently verified account of which bullets caused the answer. Its returned tags update bullet counters; its reflection enters the next generator call. Code re-extracts the answer and stops these rounds on processor correctness. Exhausting the limit still permits curation; it is not a run-level rejection. An initially correct answer also receives one reflection and counter update ([RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); SRC-1, `ace/ace.py`).

The `no_ground_truth` option changes reflector/curator prompt inputs, not the correctness oracle or branch feedback. Thus this workflow remains supervised by dataset targets even in that configuration. Reflection rounds are current-sample state; they are not all appended to the curator's input. Only the last reflection is passed onward ([RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); SRC-1, `ace/ace.py`).

### Curation admits content, not proven improvement

At the step-modulo curation gate, the orchestrator hands the curator current playbook text, last reflection, the sample's context, progress, statistics, token budget and next global ID. In this call `question_context` is the sample's `context`, not a concatenation of its question and context. The model proposes operations; Python parses and applies them. No human reviews each addition. The prompt's request for new insights and the deterministic ADD consumer do not constitute a task-accuracy veto or a hard token-budget guarantee ([RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); SRC-1, `ace/ace.py`, `ace/core/curator.py`).

> recent_reflection=reflection_content,
>                 question_context=context,
> --- `ace/ace.py`

The resulting playbook is immediately supplied to a fresh generator call with an empty reflection. This separates the post-curator answer from the explicit reflection slot, but is not a controlled causal experiment. The method returns initial and post-curator answers plus tracking data; it does not require the latter answer to be correct before retaining the update. The current playbook then carries into later samples ([RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation); SRC-1, `ace/ace.py`).

### Rejection and recovery branch

A malformed curator response can be rejected locally. Within `curate`, parsing/application failures enter handlers that log the failure and return the input playbook, input ID and an empty operation list. The empty-response sentinel has a separate skip branch. This lets the orchestrator continue to post-curator generation without installing those additions, provided failure logging succeeds. It does not undo the reflector's earlier counter changes. The model transport call precedes the parsing/application `try`, so these handlers are not a universal model-transport recovery mechanism (SRC-1, `ace/core/curator.py`; [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation)).

> print("⏭️  Skipping curator operation due to invalid JSON format")
>             return current_playbook, next_global_id, [], call_info
> --- `ace/core/curator.py`

A correctly structured but unhelpful addition is different: this workflow has no per-addition accuracy rejection. Later validation can decline to select its containing snapshot as best, but training continues from the current playbook. Recovery ownership is therefore split: the curator wrapper handles certain response/application failures; offline training handles best-snapshot selection, not transactional rollback. Disabling the analyzer here avoids its distinct merge/removal admission and fallback behavior, which must not be inferred from the curator branch ([RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge); SRC-1, `ace/ace.py`, `ace/core/curator.py`).

### Verification, selection and delivery

At scheduled validation steps, evaluation workers receive the current playbook and individual question/context with empty reflection. The processor scores extracted answers against validation targets. Strictly greater validation accuracy replaces `best_playbook`; a tie or lower score keeps the earlier best. This selects a final-testing artifact rather than accepting or rejecting each ongoing training mutation. If no scheduled score improves on the initial zero threshold, the initial text remains best. Evaluation exceptions can be skipped, and an all-failed evaluation can fail in the result-return path, so this is neither guaranteed complete coverage nor a guaranteed route to delivery ([RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select); SRC-1, `ace/ace.py`).

On normal completion, offline training writes separate current and best playbook text files, epoch/intermediate snapshots, training/validation metrics and pre/post-sample tracking. `run` tests the best snapshot, writes `final_results.json` and returns the results dictionary to the caller. The Finance main function binds that return; it does not add a further approval stage. Delivery here means files saved and a programmatic return, not human acceptance or proven benchmark benefit (SRC-1, `ace/ace.py`, `eval/finance/run.py`; [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)).

> best_playbook_path = os.path.join(save_path, f"best_playbook.txt")
>         with open(best_playbook_path, "w") as f:
>             f.write(self.best_playbook)
> --- `ace/ace.py`

> final_results_path = os.path.join(save_path, "final_results.json")
>         with open(final_results_path, "w") as f:
>             json.dump(results, f, indent=2)
> --- `ace/ace.py`

A later invocation may explicitly load a saved file and deliver its text to new generator calls. That is cross-run reuse, not automatic discovery or full-state resume: ID allocation history and scheduling state are not restored by text loading. Even within this run, installed guidance reaching prompts establishes a behavior-capable channel, not actual model reliance or successful learning ([RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload), [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation)

Workflow role: sample-level corrective subworkflow. Its return supplies epoch answer arrays and pre/post tracking; it is not the workflow's delivery boundary. Round-limit exhaustion and failed curator admission still permit post-curator generation. A correct post-curator answer is measured but does not gate continued retention.

#### On [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select)

Workflow role: scheduled snapshot selection and final scoring, not an admission veto on live training state. Final testing consumes the selected best snapshot, while subsequent training steps consume the current snapshot. Normal delivery remains contingent on evaluation and file operations returning successfully.

#### On [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)

Workflow role: saved-text delivery and explicit future-invocation handoff. The operator/caller chooses whether to reuse current or best text; completing the present run does not itself start another one.
