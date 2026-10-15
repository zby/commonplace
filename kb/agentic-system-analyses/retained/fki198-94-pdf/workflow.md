---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Incremental self-improvement's variable-writing workflow, from sampled actions through task payoff, probability-change rejection and continued interaction."
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
---

# Incremental self-improvement workflow report

## Workflow account

### Selection and evidence limit

The representative workflow is the variable-sequence task in SRC-1, captured text §5.1. It connects a concrete external result to the interpreter and its retention evaluator, rather than joining unrelated capabilities. There is no user request or delegated worker: a programmer supplies the task, primitives and payoff rule; a single interpreter repeatedly acts during one life. The workflow delivers changes to an external array, not an answer document. The capture supplies design and author-reported operation, not executable code or a trace of one sampled solution. The following is therefore a source-supported workflow specification, not a reconstructed successful execution ([boundary.md](boundary.md); [WF-RTE-variable-cycle](#wf-rte-variable-cycle)).

### From task setup to external result

1. **Setup.** The task initializes 30 external variables to zero. The runtime initializes storage and program-cell distributions at birth, then starts each run at ProgramStart. The programmer specifies the objective independently of any learned policy: maximize cumulative counts of variables whose values equal their addresses. Task inputs include the periodic count and changing IP, stack pointer and time-derived value. This is bounded experimental operation, not an open natural-language request ([WF-RTE-variable-cycle](#wf-rte-variable-cycle); [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)).
2. **Select and execute.** IP identifies a program cell; the interpreter samples a primitive and its arguments from the current distributions and checks syntax. Valid arithmetic, moves and branches can prepare work cells. Write transfers an indirectly addressed storage value into an indirectly addressed external variable. The handoff supplies concrete integer operands, not a subtask brief or isolated worker context. No specific sequence of preparatory instructions is supplied in the capture. Exact Read operand placement remains unresolved because the prose and table disagree; this workflow does not rely on resolving it ([WF-RTE-variable-cycle](#wf-rte-variable-cycle); [RT-OBJ-work-area](runtime.md#rt-obj-work-area); [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)).
3. **Deliver and score.** A valid Write immediately changes the external variable; no evaluator approves it beforehand. Every 1,000 measured steps the task counts exact address/value matches, supplies that count as payoff/input, then resets all external variables. This event is the task's observable result boundary. The count is a programmer-defined reference outcome, not a model's verdict. A count of 30 is maximal for that event, but is not a terminal acceptance state: the next interval starts and the lifetime objective remains cumulative payoff. Internal work cells are not reset with the external array ([WF-RTE-variable-cycle](#wf-rte-variable-cycle)).

### Policy-change handoff and rejection

Task actions and policy changes are interleaved within the same sampled computation. An effective IncP or DecP starts a self-modification program after birth or EndSelfMod. The primitive supplies the changed live distribution and saves its previous value, address, time, payoff and program-start bookkeeping on the stack. Primitive constraints can veto an illegal factor or a change violating MinP. This is not advance approval based on task success: valid changes already influence subsequent sampling while top-level checking is suspended ([RT-RTE-self-modification](runtime.md#rt-rte-self-modification); [RT-OBJ-stack](runtime.md#rt-obj-stack)).

EndSelfMod enables the fixed top-level evaluator. After completed instruction cycles outside an unfinished self-modification program, that evaluator compares the payoff/time rate since the newest program's beginning with the preceding retained program's rate, or the lifetime rate when there is no predecessor. A non-exceeding rate triggers popping and restoration. Recovery belongs to the fixed evaluator, not a worker asked to revise a rejected answer. Restoration itself consumes measured time and can force restoration of older changes as well. The next interpreter selection consumes the retained or restored probabilities ([RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment); [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection)).

This rejection restores direct probability changes only. It does not undo prior external writes or work-cell changes. An unfinished self-modification program can postpone evaluation; the documented positive minimum probability is not a hard completion deadline. The capture does not resolve exact implementation handling of a run halt during an unfinished self-modification program. Historical reward-rate acceptance does not prove that the accepted program caused the payoff, nor guarantee the next interval's score ([RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant); [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment); [RT-RTE-self-modification](runtime.md#rt-rte-self-modification)).

### Failure, continuation and reported delivery

An invalid external Read or Write halts the current run. Syntax failure also halts it. The enclosing life loop starts another run at ProgramStart without resetting storage or the environment merely because of the halt; the task's periodic external-array reset is a separate event. Thus failure recovery restarts instruction selection with surviving state, rather than restoring a clean task snapshot. The source does not supply a particular failed instruction trace ([WF-RTE-variable-cycle](#wf-rte-variable-cycle); [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)).

SRC-1 §5.1.2 reports that the system first wrote all 30 variables correctly after 286,918 payoff events. Remaining nondeterminism meant this did not establish stable perfect delivery. The enabled/disabled comparison is author-reported evidence at the whole-capability level, not independent causal evidence for any particular accepted program ([WF-RTE-variable-cycle](#wf-rte-variable-cycle); [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison)). At system death, the terminal result is cumulative payoff and final state; there is no further documented packaging, human acceptance or cross-process installation step.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-variable-cycle
Label: External variable-writing and payoff cycle

Distinct identity: this route is the task driver's external-array write, scoring and reset cycle. It overlaps [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle) at primitive execution and [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) at payoff consumption. Neither is the same referent: instruction dispatch is general, and credit assignment decides probability retention rather than scoring or resetting the array. This route spans those interfaces and is not a part of exactly one supplied route.

Endpoints and progression: programmer-defined array/task setup → sampled Write with indirect operands → external variable change → periodic exact-match count → payoff/input delivery → external-array reset → further sampled actions. Owners: interpreter for sampled actions and documented task driver for scoring/reset. Context/state: work cells supply values and addresses; external variables hold results within each interval. The payoff count reaches both the input interface and cumulative reward used in retention. SRC-1, captured text §5.1 and §5.1.2, supplies doctrine/design and reported operation respectively.

Operating mode: bounded lifetime experiment. Proposer: the sampled computation chooses writes. Decider and veto: fixed primitive validity rules reject out-of-range accesses; the task driver scores outcomes, not proposals. Human contribution: programmer-specified primitive and reward semantics, not per-write approval. Answer oracle: exact equality of each variable's value to its address, supplied by the task driver. The trigger is ongoing task interaction, not a separate improvement request; probability improvement is assessed on the supplied runtime routes rather than declared again here.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: Valid Write changes an external variable; out-of-range Read or Write halts the current run. Every 1,000 measured steps the driver supplies the count as payoff/input and resets the external array.
- Later read-back: Modified external values remain available to task reads and scoring until reset or overwritten; the score enters cumulative reward used by later credit-assignment checks. Internal work-cell changes can survive run halts and subsequent payoff events.
- Delegated visibility: inapplicable — there is no delegated worker in this documented serial task loop.
- Selection predicate: Indirect operands select the external variable and stored value; the scorer counts all variables whose values equal their own addresses.
- Invalidation or expiry: External variables reset to zero after each payoff event; subsequent writes can overwrite them earlier. Run halt does not itself reset internal storage or the environment.
- Activation or effect: Fixed Write semantics directly alter external state. The author reports a first maximal payoff event, but no raw trace establishes its exact sampled action sequence or any individual policy update's contribution.
- Evidence limits: Only the frozen report is available. The Read destination differs between prose and Table 2, so its exact operand formula is not asserted. Scoring establishes task outcome, not causal usefulness of a particular self-modification or future reliability.

> Every 1000 time steps, the
> number of variables whose values equal their addresses is written into a special input cell. This
> number is the current payo . Then, all variables are re-initialized with zeros.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Write(a1; a2) writes
> the contents of the storage cell indirectly addressed by the rst argument into the variable indirectly
> addressed by the second argument.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Write and read operations outside the valid ranges halt the current run.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> After 286,918 payo events, the system correctly had written all 30 variables
> for the rst time, and received maximal payo 30.0.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
