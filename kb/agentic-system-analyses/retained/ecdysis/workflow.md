---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Ecdysis workflow: synthetic harness training through collaborative review, score admission and later batch inference."
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
---

# Ecdysis workflow report

## Workflow account

### Selected workflow and evidence

The selected workflow is the shipped `examples/quickstart.py`: a Python caller requests two harness-training rounds, receives the retained harness and runs two later tasks through it. It is representative because it joins collection, review, editing, admission and delivery in one shipped consumer, rather than joining unrelated APIs. Its review client and task evaluation are synthetic. Its editor ignores the review specification. It demonstrates the intended orchestration in source, not successful model-guided repair or an observed execution (SRC-1, `examples/quickstart.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

All findings use SRC-1 at the revision fixed in [boundary](boundary.md). Direct inspection for this member covered `examples/quickstart.py`, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`, `src/ecdysis/inference.py` and `tests/test_training.py`. These supply implementation and shipped instruction evidence; no target code or test was executed. The runtime baseline supplies the failure-extraction account and existing route identities. No new source or workflow record is needed.

### Request, collection and diagnosis

The caller supplies revision-zero dictionary state, collector, editor and review client, with two training rounds and two review passes. The trainer owns the sequence once `train` begins. It recollects the current harness at each round and applies the scorer before deciding whether review is needed. The quickstart collector gives both task IDs reward zero until revision reaches one, then reward one. Its reference outcome is that fixed revision predicate, not an expected task answer or model correctness test (SRC-1, `examples/quickstart.py`, `src/ecdysis/training.py`).

> reward = float(harness["revision"] >= 1)
> --- `examples/quickstart.py`

Failures below the configured threshold are extracted and grouped by termination reason and low reward components. As detailed in [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), missing rewards are not selected as failures, and recurrence affects priority rather than imposing a hard eligibility gate. The trainer delegates review only when failures exist. The review model receives cluster summaries and at most twelve failure metadata samples, not the extracted trajectory messages or harness implementation. Consequently this workflow's model diagnosis can concern the supplied signatures, but source wiring does not establish inspection of the actions that caused them (SRC-1, `src/ecdysis/fdcr/review.py`; the cited runtime record supplies extraction evidence).

### Review handoffs and editor delegation

The review code, not a model planner, schedules Analyst, Critic and Engineer serially for each pass, then Moderator. Each role uses the same client, receives its shipped system prompt and a reconstructed user message with failure context and the last twelve transcript turns. Replies become stripped text in the shared transcript. These are role-conditioned calls, not independently launched agents with separate tools or permissions. The ordinary two-pass nonempty review makes six text calls and one JSON call; even the final Engineer receives a call despite being told “No action — moderator follows.” Critic is instructed to challenge proposal risks, the next Analyst to revise against objections, and Moderator to resolve disputes conservatively. These requests do not establish that meaningful criticism occurred (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`; [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)).

Moderator returns a specification whose four normalized fields describe failure patterns, proposed changes, skills and implementation notes. That specification is advisory input to the caller's editor; the trainer does not implement its prose or check compliance. The editor receives more evidence than the review model: current harness, normalized specification, extracted failures and groups. Engineer's title does not make it the editor; its shipped instruction says not to write code yet. Actual candidate construction belongs to the supplied Python callback (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/roles.py`; [RT-BAP-review-editor](runtime.md#rt-bap-review-editor)).

In the selected consumer, the callback always increments the revision and returns a new dictionary:

> def edit(harness, _specification, _failures, _groups):
>     return {"revision": harness["revision"] + 1}
> --- `examples/quickstart.py`

This is the consequential evidence limit: a score increase here cannot establish that review content caused the change. No per-candidate human approval appears in the trainer; human intervention inside real callbacks remains outside the inspected example (SRC-1, `src/ecdysis/training.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

### Verification, rejection and recovery

The trainer delegates execution of the candidate to the same collector and applies the configured scorer. The computational acceptance gate compares the candidate score with that round's baseline; Critic and Moderator do not hold a programmatic veto. Only strict improvement replaces the retained reference. This is a training-score gate, not a shipped held-out evaluation or semantic specification check (SRC-1, `src/ecdysis/training.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

> accepted = candidate_score > baseline_score
> if accepted:
>     current_harness = candidate
>     current_score = candidate_score
> --- `src/ecdysis/training.py`

The rejection test constructs a baseline score of 0.5 and a candidate score of 0.0 and asserts that the original harness and score remain. It provides a concrete source-supported counterpath, not an observed test result. Equal scores also fail the comparison. After rejection the trainer records `rejected` and proceeds if configured rounds remain; it does not ask the editor to repair that rejected candidate within the same round. Because live references are passed to callbacks, rejection cannot undo an editor or collector's in-place mutation. The selected dictionary-returning editor avoids that mutation, but external isolation and comparable evaluation remain adapter obligations (SRC-1, `tests/test_training.py`, `src/ecdysis/training.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

> assert result.frozen_harness == 0
> assert result.final_score == 0.5
> assert result.rounds[0].status == "rejected"
> --- `tests/test_training.py`

A second counterpath is an empty failure set: the trainer records `no_failures` and continues without review or editing, rather than ending training early. In quickstart source this occurs in round two after the accepted revision-one candidate (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

Optional recovery has a narrower owner and scope. With `checkpoint_dir`, the trainer names a review checkpoint per training round; review code saves successful transcript progress, records interruption and rethrows. A caller reentering review with matching formatted-context hash and model string can resume the unfinished turn, or reuse a completed specification without calls. Mismatch raises. The hash does not cover omitted trajectory messages, role-prompt versions or provider endpoint. This protects the implemented equality condition, not complete semantic freshness or exactly-once provider execution. Quickstart does not configure this recovery path. The trainer has no persisted harness-round restart or mutation rollback mechanism, and callback exceptions propagate (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`; [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)).

Malformed/non-dictionary moderator output can normalize to empty specification fields rather than reject the workflow. With nonempty failures the trainer still delegates editing. Therefore normalization is not verification that a valid repair was proposed; the scalar gate remains the final implemented candidate decision (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`; [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)).

### Delivery and later use

Training delivery is the return of `TrainingResult`: retained harness reference, final score and tuple of round decisions. It does not automatically save harness state or reusable skills. In the selected source path, revision one is retained and later passed to `infer_many` with two new task dictionaries. The executor formats each task ID and retained revision; the caller prints the final score and record outputs. Those are the intended delivered results, not evidence of real task-solving success (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`; [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness), [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness)).

> print(f"final_score={result.final_score:.1f}")
> for record in inference.records:
>     print(record.output)
> --- `examples/quickstart.py`

Batch inference executes tasks sequentially without scheduling further review. It returns output/error/timing records, captures executor exceptions by default and continues; `fail_fast` rethrows. Its success flag means no caught executor exception, not a correct answer. Direct single-task inference instead propagates executor exceptions. The harness remains a live argument, not deeply immutable state. Hence the end-to-end delivery contract is orchestrated retention and task-result return, with real editing, task semantics and successful recovery unresolved without external adapter or run evidence (SRC-1, `src/ecdysis/inference.py`, `src/ecdysis/training.py`; [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference)).

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

#### On [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)

Workflow role: Supplies the diagnosis-to-editor handoff in the selected training consumer. Review roles are serial textual contributors, not the callback that edits the harness. This handoff is content-insensitive in quickstart because its editor disregards the specification; that consumer cannot demonstrate repair quality attributable to collaborative review.

#### On [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

Workflow role: Owns the accept/reject branch and training delivery. Rejection retains the prior reference without a same-round repair loop; `no_failures` skips editing but consumes a configured round. The result is delivered after the configured round loop, not when Moderator declares agreement.

#### On [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)

Workflow role: Optional review-local restart, not end-to-end training recovery. The selected quickstart does not enable it; a caller must reenter after interruption, while retained harness and round state have no corresponding persisted restart in the trainer.

#### On [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference)

Workflow role: Turns the returned harness into later task output records and, in quickstart, printed outputs. Returning a record completes delivery at the library boundary; correctness and provider/executor behavior are not verified by that return.
