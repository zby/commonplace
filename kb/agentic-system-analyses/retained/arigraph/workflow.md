---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AriGraph workflow account: the shipped Ariadne game episode, synchronous model handoffs, action recovery and logged delivery."
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
---

# AriGraph workflow report

## Workflow account

### Selection and evidence

The representative workflow is one Ariadne game attempt in `pipeline_arigraph.py`, from operator configuration and environment reset through repeated memory, planning and action decisions to termination and logs. It was selected because it exercises the memory system's production, maintenance and later consumption in one shipped caller. QA and baseline consumers are not joined into this episode. The canonical route is [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle); this member adds workflow-specific handoff and recovery analysis rather than declaring the same route again.

Evidence is SRC-1 at the frozen commit, within the [boundary](boundary.md#boundary-and-evidence). This member fully inspected `pipeline_arigraph.py`, `agents/parent_agent.py`, `graphs/contriever_graph.py` and `graphs/parent_graph.py`, supplying implementation evidence. These paths were already in the boundary's inspected scope; no new source was introduced. Runtime records supply prompt and retained-log evidence where cited. No target execution or failure injection was performed. The runtime's attributed step-one observation supports a bounded recorded sequence, not successful completion of this entire workflow or reproduction under current defaults.

### Request, owner and handoffs

The operator supplies an API key and selects the goal indirectly through module-level environment configuration. The default is `hunt_hard`, one attempt and 150 outer iterations. The Python driver owns ordering, reset, context construction and environment dispatch. Separate synchronous model wrappers perform entity selection, exploration, planning and action selection; the graph makes extraction and replacement requests. This is role-specialized computation, not delegation to independently scheduled workers. Each request returns text to its caller; no worker mailbox, acceptance protocol or autonomous continuation is implicated by these handoffs (SRC-1, `pipeline_arigraph.py`, `agents/parent_agent.py`; [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle), [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent)).

1. **Reset and seed.** The driver resets TextWorld, initializes the previous action to `start`, seeds a plan with the task goal, clears recent history and known locations, and creates a fresh graph. This bounds retained state to the attempt rather than providing restart recovery. The task plan's identity and replacement mechanism are [RT-OBJ-plan](runtime.md#rt-obj-plan) (SRC-1, `pipeline_arigraph.py`).
2. **Observation to memory.** The driver normalizes the observation, adds first-step task instructions, obtains inventory and records the current location. The entity role receives the observation and previous plan; its parsed entity dictionary becomes lowercased retrieval queries with depths. Graph update receives the observation, recent observations, previous plan/subgraph, locations and previous action. It extracts facts, proposes removal of associated outdated facts, applies guarded deletion, adds facts/spatial links, selects older facts and episodes, and stores the current observation. Inventory is appended only after this call. The later planner therefore receives inventory that was not explicitly appended to this memory-admission request (SRC-1, `pipeline_arigraph.py`, `graphs/contriever_graph.py`; [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)).
3. **Memory to new plan.** The exploration role receives the previous plan. Any response containing `True` enables graph-derived unexplored-exit context. The planner receives the goal, bounded recent observation/action history, current observation plus inventory, selected facts, selected episodes and previous plan, with exit context when enabled. Its entire returned text replaces the plan; the driver does not parse or semantically approve the plan. This is immediate admission under authored model guidance, not a verified planning result (SRC-1, `pipeline_arigraph.py`; [RT-OBJ-plan](runtime.md#rt-obj-plan), [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)).
4. **New plan to action.** The action role receives the same current decision context, the new plan and possible actions, including synthetic `go to` commands for known locations. A JSON parse/key lookup extracts `action_to_take`. The driver stores the current observation/action in history, slices the two recent-history lists to five default entries and records the pre-execution location. Parsed action text then crosses the effect boundary into TextWorld, directly or through graph navigation (SRC-1, `pipeline_arigraph.py`; [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch)).
5. **Effect to next round.** Environment feedback supplies observation, reward, completion and info. Direct actions issue one command; navigation can issue several directional commands before another planner invocation. Only navigation's final returned observation reaches the next outer memory update; intermediate observations are logged. The next round's retrieval and planning also consume the retained plan/history and selected graph memory. These are wired feedback paths, not evidence that any particular memory changed an action or improved success (SRC-1, `pipeline_arigraph.py`, `graphs/parent_graph.py`; [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation), [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions), [RT-BAP-plan-decisions](runtime.md#rt-bap-plan-decisions)).

### Verification, rejection and recovery

The driver has narrow checks, not a general verifier that certifies an episode's product. Memory deletion rejects a proposed triplet when both endpoints are caller-supplied locations, and ignores proposals not in the graph. These checks protect selected state mechanically; they do not establish fact truth, successful contradiction resolution or validity of replacement facts. There is no transaction restoring removed facts after a later failure (SRC-1, `graphs/contriever_graph.py`; [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)).

The action parser supplies a concrete rejection path: malformed JSON or missing-key failure logs an error and substitutes `look`. It does not ask the action model to repair its output. The driver then executes the fallback through the ordinary dispatcher, so a returned observation can support another round. Conversely, a well-formed off-list action is not rejected locally; the action-list restriction remains prompt policy and the environment owns the command's actual effect. Nonstring values can survive the lookup and fail later at substring dispatch. The fallback therefore does not validate the whole action schema (SRC-1, `pipeline_arigraph.py`; [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)).

> except:
>         log("!!!INCORRECT ACTION CHOICE!!!")
>         action = "look"
> --- `pipeline_arigraph.py`

Navigation supplies a second source-supported recovery path. `find_path` returns diagnostic text for already-current, unknown or disconnected destinations and catches path-computation exceptions. The dispatcher treats a non-list result as the returned observation, without stepping the environment. In a subsequent outer iteration this becomes input to memory and replanning. The driver supplies no dedicated failure flag or semantic rejection of these diagnostics before memory admission. Thus recovery is another context-driven round, not route repair or rollback; its success is unobserved (SRC-1, `graphs/parent_graph.py`, `pipeline_arigraph.py`; [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation)).

> if not isinstance(path, list):
>             observation = path
> --- `pipeline_arigraph.py`

> return "You can't navigate now through 'go to', please, use actions like north or west"
> --- `graphs/parent_graph.py`

Entity parsing and provider calls occur outside the action fallback. The inspected wrappers and caller add no retry/recovery around those requests; provider-internal retry behavior remains outside this source evidence. There is no human per-action approval. Environment rewards and `done` supply outcome feedback, not an expected plan/action answer used to approve a candidate (SRC-1, `agents/parent_agent.py`, `graphs/parent_graph.py`, `pipeline_arigraph.py`; [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)).

### Termination and delivered result

Delivery here is an environment trajectory and its logged artifacts, not a returned final answer or accepted report. After dispatch the driver accumulates reward and logs rewards, estimated costs and timing. If the environment returned completion, the next outer iteration logs the final observation and breaks; otherwise exhaustion of the outer loop ends the attempt. There is no explicit final success object returned by `run()`. Budget exhaustion is not proof that the task goal was met, and the 150-iteration bound is not a bound on environment commands because navigation expands an action into several commands (SRC-1, `pipeline_arigraph.py`; [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle), [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation)).

> if done:
>                 log("Game itog: " + observation)
>                 log("\n" * 10)
>                 break
> --- `pipeline_arigraph.py`

The account establishes the shipped coordination and bounded recovery mechanisms. The supplied step-one log evidence cited by the runtime does not establish termination, reliable model compliance, exercised rejection recovery or causal benefit over the full episode.

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

#### On [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)

Workflow handoff acceptance: entity output is parsed and consumed as a dictionary; planner text is directly accepted; action output alone has the local JSON/key-error fallback. These are different acceptance points, not one shared verification gate. Ordering is driver-owned and synchronous. Recovery after action parsing substitutes `look`; it does not retry generation or restore the previous plan/memory. Completion is owned by the external environment and checked on the following outer iteration; logged artifacts constitute delivery, without a returned final-answer contract. Evidence: SRC-1, `pipeline_arigraph.py`, `agents/parent_agent.py`, and the action/termination passages above. Failure recovery is implementation-supported, not observed in an exercised failure trace.

#### On [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation)

Workflow rejection handoff: a non-list path result becomes the next observation without an environment command. The driver neither labels it as a separate failure object nor branches to a repair agent; the ordinary memory/planner round receives it. This permits model-driven reconsideration but also exposes diagnostic text to ordinary fact extraction. There is no evidence here that reconsideration succeeds. Evidence: SRC-1, `graphs/parent_graph.py`, `pipeline_arigraph.py`, and the navigation passages above.
