---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "WikiSkill workflow: a host-native numeric learning round, including role handoffs, scorer recovery, candidate rejection and retained-result delivery."
run-id: AAS-2026-10-15-wikiskill-baafad05d35e-01
reviewed-boundary: da6984caca09d5f81b2336cf3067b59c0c18bb1e
---

# WikiSkill workflow report

## Workflow account

### Selected path and evidence

The representative workflow is one numeric product round using native host children: baseline validation → training → Maintainer → Proposer → candidate validation → retained result. It was selected because it connects the ordinary user-facing skill-improvement request to both persistent learning and a separately evaluated successor. It combines the existing [RT-RTE-product-round](runtime.md#rt-rte-product-round) and [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff), rather than declaring another identity for their composition. Feedback-first comparison and research execution are different routes, not implied steps in this workflow.

All findings concern SRC-1 at the frozen revision. This is implementation and doctrine inspection, not observed execution. Focused inspection covered `src/wikiskill/product.py` (`_load`, task progression, context construction, submissions, retry, export and status), `src/wikiskill/native_agents.py` (learning-context transformation, dispatch, bind, fail and collect), `skills/wikiskill/SKILL.md`, and both learning-role instructions under `src/wikiskill/resources/product/roles/`. The main skill adds source-native orchestration and delivery doctrine beyond the runtime baseline. No tests, providers or target commands were run. Actual host freshness, task success and improvement remain unobserved.

### Request, preparation and baseline

The foreground host agent interprets the user's improvement request, prepares examples and agrees on the evaluation criterion, current skill and budget. Shipped guidance defaults to one round unless the user requests more; adding feedback alone must not initiate an improvement run. It also directs the coordinator to check scorer readiness and obtain authorization for the exact external scorer, not infer trust from an imported workspace (SRC-1, `skills/wikiskill/SKILL.md`).

> - **Remember feedback:** save it with `wikiskill feedback`; do not start an improvement run merely because a note was added.
> --- `skills/wikiskill/SKILL.md`

`start` fixes workspace conditions; the controller, not the child agent, issues stable task requests and selects phase and skill. Initial validation measures the incumbent, then training runs with the retained skill. The user supplies the task boundary and evaluation criterion; the coordinator controls scheduling and normal host tools; WikiSkill controls request issuance and recorded progression. Setup, task hashing and scorer authorization are established in [RT-RTE-product-round](runtime.md#rt-rte-product-round).

For each request, `dispatch` stages role instructions, payload and a request-specific output directory. Executor payloads contain the filtered task and skill pointer, not the learning Wiki, scores or saved baseline answers. The native dispatcher tells the coordinator to use the host's native subagent tool, bind its actual returned ID, wait, then collect. Fresh child creation is performed by the host, not by WikiSkill (SRC-1, `src/wikiskill/native_agents.py`; [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)).

The coordinator must not substitute its own accumulated conversation for the role context. This is an explicit workflow rule, not verified context isolation:

> The main agent coordinates and submits; it does not execute tasks or act as Maintainer/Proposer in its own conversation.
> --- `skills/wikiskill/SKILL.md`

Binding checks runtime, fresh-context metadata and host-ID nonreuse. These are host reports, not attestation. A privileged child can still reach files outside its payload. The result crossing back is intended to be a result-file pointer and brief status, rather than the whole child conversation. The controller preserves output artifacts separately; fresh contexts do not make those files inaccessible (SRC-1, `src/wikiskill/native_agents.py`; [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)).

### Collection, verification and learning handoffs

`collect` requires a dispatched, bound request. It checks that result.json and referenced output/trace files resolve inside that request's output directory, then calls `record`, `learn` or `propose`. Already completed collection returns status without applying changed scratch output. These checks establish file containment and sealed submission behavior for collection, not semantic correctness or a boundary covering every direct product API (SRC-1, `src/wikiskill/native_agents.py`; [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)).

Task recording copies actual output into controller-owned records. A configured scorer receives the full task, including its reference, and the saved output path/text. Otherwise the caller supplies a finite score. The controller validates score structure, not the validity of the criterion or honesty of a manual evaluation. All tasks in the current phase must finish before progression; pending or failed requests block advancement. `count` permits concurrent task requests, but it does not permit learning to overtake unfinished task work (SRC-1, `src/wikiskill/product.py`; [RT-RTE-product-round](runtime.md#rt-rte-product-round)).

After training, the Maintainer receives current-round training results with full task evidence, existing Wiki patterns, human feedback, current skill and gate history. Native staging converts artifact paths to absolute paths and restricts numeric gate history to round, verdict and aggregate scores/improvement. Thus it does not simply pass every recorded validation artifact to the learning child (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/product.py`). The Maintainer is instructed to distinguish observations from hypotheses and review successes, failures and counterexamples. It returns sourced patterns, not an edited deployed skill:

> An empty patterns list is permitted when nothing useful is supported.
> --- `src/wikiskill/resources/product/roles/maintainer.md`

`learn` requires nonempty names/content and source IDs drawn from the supplied training, feedback or existing-pattern context. It commits patterns and changes phase to proposer. Source-ID membership is not semantic entailment; an empty list can legitimately advance without adding knowledge. The Proposer therefore receives the committed Wiki after this submission, not an independently raced proposal context (SRC-1, `src/wikiskill/product.py`; [RT-RTE-product-round](runtime.md#rt-rte-product-round)).

The separate Proposer is instructed to produce one complete procedural revision with applicability, exclusions and concrete actions, or `no_action`. It must not grade itself or alter the criterion. Controller admission only requires a nonempty UTF-8 skill or the exclusive no-action choice; the stronger content rules are model-facing doctrine, not a semantic validator (SRC-1, `src/wikiskill/resources/product/roles/proposer.md`, `src/wikiskill/product.py`).

> Do not inspect validation answers, alter the scoring criterion, evaluate your own proposal, edit the committed Wiki, delegate another agent or modify controller records.
> --- `src/wikiskill/resources/product/roles/proposer.md`

### Candidate decision and rejection

Fresh executor requests evaluate the candidate on the same validation cases used for baseline. Software compares mean score against the retained best with the configured direction and strict minimum improvement; no-action skips task evaluation and records NO_ACTION. The proposer authors the candidate, the evaluator supplies scores, and the controller selects the successor. There is no obligatory human approval of each pattern or candidate. The host can withhold further work but cannot make a rejected candidate retained through the ordinary gate (SRC-1, `src/wikiskill/product.py`; [RT-RTE-product-round](runtime.md#rt-rte-product-round)).

Rejection is selective rollback: the current skill stays unchanged, but committed Wiki patterns and gate history remain. Replay increments the round and either ends or returns to training. A rejected candidate is not installed merely because its file exists. The decisive retained-pointer update is conditional:

> if value['accepted']: s.update(best_score=value['candidate_score'],current_skill=value['skill'])
> --- `src/wikiskill/product.py`

Consequently, a later learning round can see lessons and a rejection without using the rejected skill for training. Reusing validation cases supports this configured comparison, not an independent held-out demonstration of generalization (SRC-1, `src/wikiskill/product.py`; [RT-RTE-product-round](runtime.md#rt-rte-product-round)).

### Failure recovery and delivered result

A scorer failure is not converted into task failure accuracy. `record` preserves output, records a failed request and raises; `next_work` returns needs_attention. The coordinator must diagnose the cause and explicitly retry. A changed scorer after recorded results requires a new consistent comparison rather than silently mixing scores (SRC-1, `src/wikiskill/product.py`).

> raise RuntimeError('Scoring failed; output retained, resolve the failure before retry') from exc
> --- `src/wikiskill/product.py`

Retry supersedes the failed request. When saved execution and prior delegation exist, native dispatch carries forward that delegation and saved output; collection retries scoring without another child. This is a deliberate exception to one fresh child per new execution, preserving the same execution rather than spending another model call. Execution/delegation failures can instead be explicitly failed and retried. The controller does not itself repair the host or scorer (SRC-1, `src/wikiskill/native_agents.py`, `src/wikiskill/product.py`; [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)).

Completion is a controller phase after the configured rounds, not proof of improvement. Status exposes retained skill, Wiki and gate history. The entry skill instructs the coordinator to explain the journal-derived result, link the Wiki and retained skill, and treat rejection/no-action as valid outcomes. If there is no retained skill, delivery is the Wiki and report rather than the rejected candidate (SRC-1, `skills/wikiskill/SKILL.md`, `src/wikiskill/product.py`).

> When no skill was retained, deliver the Wiki and report instead of installing a rejected candidate.
> --- `skills/wikiskill/SKILL.md`

Export copies the retained text and provenance to an empty external destination; authorized installation is a separate downstream route with replacement and restoration checks ([RT-RTE-skill-install](runtime.md#rt-rte-skill-install)). Exported or installed bytes do not establish that a later host loaded them, obeyed them or improved. Later instruction delivery is established by [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption); exercised content-dependent behavior remains outside this source-only workflow evidence.

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

#### On [RT-RTE-product-round](runtime.md#rt-rte-product-round)

Workflow dependency: task-phase completion precedes maintenance; committed maintenance precedes proposal; proposal precedes validation and successor selection. Candidate rejection preserves Wiki learning while leaving the incumbent active. Delivery has two levels: complete controller status, then coordinator explanation/export if appropriate. Neither level establishes later behavioral benefit.

#### On [RT-RTE-native-handoff](runtime.md#rt-rte-native-handoff)

Workflow recovery ownership: the coordinator diagnoses failed execution/scoring and invokes explicit retry; dispatch can reuse saved execution and its original binding after scorer failure. A handoff with an existing delegation calls for waiting/resuming that child, not spawning a duplicate. Result-file collection is a narrow return boundary, not host filesystem isolation.
