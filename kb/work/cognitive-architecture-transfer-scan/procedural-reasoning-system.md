# Procedural Reasoning System: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

The Procedural Reasoning System (PRS) is an influential architecture for situated, goal-directed agents and a precursor or close relative of BDI systems. The agent maintains beliefs about the world, goals or events requiring response, a library of procedural knowledge or plans, and intentions representing selected plan instances under execution. Plans are indexed by triggering events or goals and guarded by context conditions. Several intentions can be active, and meta-level reasoning can choose, suspend, or reconsider them as circumstances change.

The central transfer is a separation that ordinary "agent loop" descriptions blur: having a goal, knowing an applicable procedure, committing to one procedure, and completing its effects are different states.

## Provisional ontology

- **Belief:** current information the agent uses about itself or the world.
- **Goal/event:** a desired condition or occurrence requiring handling.
- **Plan/procedure:** reusable knowledge about how to respond under stated conditions.
- **Trigger:** the event or goal for which a plan becomes a candidate.
- **Context condition:** a test of current applicability.
- **Intention:** a selected, instantiated plan to which the agent has committed resources.
- **Intention structure/stack:** current execution state, including subgoals.
- **Meta-level control:** selection, scheduling, suspension, failure recovery, or reconsideration across intentions.

## Transfer candidates

- **`PRS-1` — give skills trigger, applicability, and completion contracts.** A description saying what a skill does is insufficient. It should expose when it becomes relevant, preconditions, observable completion, and failure/abort handling.
- **`PRS-2` — reify commitment.** Plans found during deliberation should not silently become the active plan. Recording the chosen intention makes scope, abandonment, and user revision inspectable.
- **`PRS-3` — distinguish goal revision from plan progress.** New user information may satisfy a tool dependency, change the method, or replace the goal itself. The control loop must classify the update before continuing; this bears directly on the [chatbot goal-state workshop](../chatbot-goal-state/README.md).
- **`PRS-4` — specify reconsideration conditions.** Persistence avoids thrashing, but blind persistence continues obsolete work. An intention should state what new evidence, failure, or authority can reopen selection.
- **`PRS-5` — treat the plan library as operational memory.** Procedures are memory when accumulated experience shapes future action through them, so their provenance, scope, lifecycle, and effectiveness belong in memory-system governance.

## Method worth borrowing

Evaluate an agent with event traces that distinguish goal adoption, plan retrieval, applicability check, intention selection, step execution, subgoal creation, suspension, success, and failure. Inject changes at each point. A robust system should persist through irrelevant noise, reconsider on invalidated assumptions, and recognize genuine goal replacement.

## Non-transfer and failure modes

- Plan libraries are brittle in open domains when context conditions cannot anticipate important cases.
- Explicit belief stores can diverge from information latent in model context or tools.
- Intention persistence can turn a stale initial interpretation into systematic misalignment.
- Mapping every conversational move into formal BDI state may add bookkeeping without improving behavior.
- A procedure's availability does not establish its authority to act.

## Grounding questions

1. What are the canonical PRS data structures and execution-cycle transitions?
2. How does PRS distinguish goals, events, desires, and intentions?
3. What meta-level mechanisms govern scheduling and reconsideration?
4. Which PRS descendants materially change the plan/intention model?
