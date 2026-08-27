---
description: Workshop baseline for analysing how an external agent runtime schedules work, assembles bounded calls, acts on external state, coordinates agents, and exposes control surfaces.
type: kb/types/instruction.md
---

# Analyse an Agent Runtime

Use this procedure as the always-on whole-system lens in an external agentic-system analysis. It locates the machinery that determines what happens next, what each bounded model call receives, and what persists or acts outside the call. It also records coordination, authority, recovery, and governance surfaces.

This is a workshop baseline. It does not yet define publication layout or source-checkout handling. Receive a pinned source/evidence register from the parent analysis and return records keyed to its source IDs.

## Definitions

- **Scheduling** owns control progression: whether, why, and when another model call or action occurs, and how run state advances.
- **Context assembly** selects and frames the instructions, state, evidence, history, tools, and constraints supplied to a bounded model call.
- **External state and action services** retain exact state, execute operations, and enforce environmental boundaries outside the model.
- **Behavioral authority** records the consumer, channel, force, and horizon through which an artifact or result changes behavior.

These are analytical responsibilities, not required module boundaries. One implementation may own several responsibilities, and one facility may span them. Split by the decision being made, not by directory or class name.

## Scope and evidence

Before analysis, receive or establish:

- the system, reviewed revision/version, declared boundary, and excluded components;
- source IDs with identities, revisions, evidence layers, and local anchors;
- the system's declared purpose and ordinary execution entry points;
- whether the inspected subject is a complete deployed loop, a library/SDK capability surface, a plugin, or one component inside a host runtime; and
- missing evidence and the conclusions each gap prevents.

Keep separate: documented intent, inspected implementation, reported operation, observed execution, and causal experiment. For a library or SDK, describe afforded capabilities unless host wiring is inspected. Do not turn an exposed API into deployed behavior.

## Required output

Produce these six blocks in order.

### 1. Runtime boundary

`system | revision/version | analysed boundary | excluded components | deployment kind | declared purpose | entry points | source IDs | missing evidence -> conclusion prevented`

### 2. Responsibility map

Use one row per operative responsibility. Split a component when it makes materially different decisions.

`responsibility id | scheduling/context assembly/external state/external action/boundary enforcement | implementing component or actor | trigger and inputs | state consulted | decision or operation | output/effect | behavioral-authority path | evidence source ID/anchor | gap/limit`

Always cover or explicitly dispose:

- turn and episode progression;
- model/provider invocation;
- tool-call dispatch and result return;
- prompt, instruction, history, retrieved-material, and tool-schema assembly;
- durable and session state;
- permission, sandbox, capability, or policy boundaries; and
- cancellation, retry, timeout, halt, resume, rollback, or recovery.

### 3. Execution and coordination routes

Use one row per material route across model, runtime, tool, human, agent, or environment boundaries.

`route id | initiating event | controller/scheduler | ordered stages | state transition | boundary crossed | capability/permission change | concurrency or serialization | failure/recovery behavior | returned artifact or effect | evidence source ID/anchor | gap/limit`

For delegation or multi-agent coordination, also record:

- scheduler placement: conversational, symbolic runtime, model-authored external program, hybrid, or not determinable;
- persistence horizon: step, episode/session, cross-session, or mixed;
- coordination form: prompt assembly, conversation, prompt refinement, shared state, cloning/forking, task graph, or other described form;
- coordination guarantee: isolation/scoping, consistency/ownership/visibility, adjudication/verification/voting, none found, or not determinable; and
- boundary-return artifact: raw output, structured result, compressed summary, state mutation, executable artifact, or other described form.

Do not infer a guarantee from the existence of a coordination channel.

### 4. Context and capability assembly

Describe each materially different bounded-call path.

`call path id | objective/role | instruction sources | task and environment state | retained-material sources | selection/scoping/ordering/compaction | tool and capability surface | provider/model selection | provenance visible to call or operator | budget/limit | evidence source ID/anchor`

State whether selection is explicit and inspectable or inherited implicitly through transcript, framework defaults, or host behavior. Context volume and complexity are separate concerns. Presence in context is not evidence that material affected action.

### 5. Control, observability, and governance surfaces

`surface id | target responsibility/route | observer or governor | signal/artifact | when available | advisory/permissive/ranking/enforcing force | prevention/detection/recovery role | wired consumer | evidence source ID/anchor | effectiveness evidence or not tested`

Cover only evidenced surfaces. Tests, ledgers, reports, warnings, and policies have no implemented force unless a consumer uses them. Distinguish preventing a decision, detecting a result, and repairing or recovering after failure.

### 6. Bounded runtime conclusion and lens signals

State:

- where progression control actually lives;
- how calls receive context and capabilities;
- what exact state and actions remain outside the model;
- how boundaries, failure, and recovery are governed;
- which coordination guarantees are implemented and which are merely declared;
- what the evidence establishes about operation versus capability; and
- which lens signals were found.

End with these explicit dispositions:

`Memory/context lens: applies | does not apply within boundary | uncertain — evidence and reason`

The memory/context lens applies when system-, user-, project-, or run-specific material persists across invocation boundaries and a later consumer can use it to shape behavior. Static shipped instructions or documentation alone do not establish memory applicability.

`Epistemic lens: applies | does not apply within boundary | uncertain — evidence and reason`

The epistemic lens applies when a material route acquires, produces, transforms, checks, disposes, accepts, integrates, or authorizes truth-apt content, or when the system makes a consequential knowledge-production or warrant claim. Do not require proof that the route succeeds before applying the lens.

If the only signal is evaluation-driven behavior or policy adaptation with no evidenced truth-apt object and no knowledge or warrant claim, retain it as a runtime route and do not let it independently trigger the epistemic lens. If another epistemic trigger applies, pass the adaptation route's IDs so the epistemic analysis can distinguish it from truth-apt production.

List candidate object and route IDs for every applicable or uncertain handoff. These are routing signals, not completed lens findings.

## Steps

1. Fix the boundary and evidence register before reading architecture claims as facts.
2. Trace one ordinary execution from entry to termination or suspension. Record the responsibilities actually exercised.
3. Trace exceptional routes that materially change authority, state, recovery, or continuation.
4. Build the responsibility map by decisions, splitting components that span roles and merging files that implement one role.
5. Record bounded-call context and capability assembly separately from scheduling and tool execution.
6. Trace delegation and coordination across boundaries, including the artifact that returns and the guarantee the route actually implements.
7. Trace permissions, validation, observability, and recovery to their consumers. Mark inert artifacts and unwired reports.
8. Apply the two lens dispositions from evidence, preserving uncertain cases.
9. Conclude only at the inspected deployment boundary and evidence layer.

## Misuse guards

- Do not call a filesystem, database, tool runner, or TUI the scheduler merely because the loop uses it.
- Do not treat stored history as context assembly until a route selects or supplies it to a call.
- Do not treat context presence as behavioral activation.
- Do not infer deployed behavior from an SDK callback or extension point without host wiring.
- Do not infer safety, governance, or recovery from a policy, test, report, or log with no operative consumer.
- Do not treat a git branch, session branch, sub-agent, task node, and prompt fork as interchangeable; record the actual boundary and return artifact.
- Do not turn an absent feature into a defect without reference to the system's declared purpose.
- Do not use the runtime conclusion to pre-judge memory quality or epistemic warrant.

## Verify

- Every material runtime responsibility is present or explicitly out of scope.
- Scheduling, context assembly, and external state/action decisions are not conflated.
- Capability and deployed wiring, and doctrine and observed operation, remain separate.
- Each coordination claim names its boundary, return artifact, persistence horizon, and implemented guarantee.
- Each authority or governance claim names a consumer, channel, force, and evidence.
- Lens dispositions cite positive, negative, or uncertain evidence and pass stable IDs rather than prose-only hints.
