# Task-scoped computational closure

This is a working formulation for the workshop, not yet a promoted claim. It
refines the shorthand used in the [shared model](./shared-model.md) and the
[closure-capability map](./closure-capability-map.md): a "declared path" is
always a path instantiated by selected tasks.

## Why task selection belongs in the claim

The decisions required from a system depend on the task. A system can appear
closed by choosing only trivial tasks, dropping failed cases, or ending the
horizon before a difficult decision arises. Computational closure is therefore
not a context-free property of a system. It is a relation among a system, a
task-selection rule, a boundary, and a horizon.

Task selection may be external or part of the system. A client or benchmark may
supply tasks as an explicitly exported input. A system may instead choose its
own tasks, in which case selection is one of the decisions inside the automatic
path and the claim covers only the resulting self-selected workload. The
selection rule must be declared because it determines which paths the closure
claim covers.

## Scope of a closure claim

Declare the following before observing the evaluated outcomes:

- **Task selection:** a finite task set or a rule for sampling or generating
  tasks from a declared domain. State who controls the rule, what system state
  it may depend on, whether the system may refuse tasks, and how refusals are
  counted. Fix the rule before observing the evaluated outcomes.
- **Objective and acceptance:** the result criterion, who controls it, whether
  the system may revise it inside the claimed path, and how any revision is
  evaluated. An externally anchored capability claim requires a criterion not
  controlled solely by the candidate.
- **System boundary:** the models, retained artifacts, code, schedulers,
  evaluators, state, tools, and evidence interfaces counted as internal.
- **Exogenous inputs and interactions:** observations, client choices,
  permissions, services, or feedback allowed to cross the boundary without
  being counted as internal decisions or execution.
- **Horizon:** the part of execution covered, including repair, recovery, and
  later revision episodes when recurrence is claimed.
- **Resources:** the relevant time, compute, money, tool, and interaction
  limits.
- **Coverage rule:** which selected tasks must reach a terminal result and how
  failures, timeouts, and abstentions affect the claim.

A compact notation is:

    Closed(M | S, A, B, E, H, R, Q)

where `M` is the system, `S` task selection, `A` objective and acceptance, `B`
the system boundary, `E` permitted exogenous inputs and interactions, `H` the
horizon, `R` resources, and `Q` the coverage rule. The notation is bookkeeping,
not a theorem.

## Structural closure

For each task selected by `S`, reconstruct the actual path from task
presentation through any required:

- interpretation and decomposition;
- premise or theory retrieval;
- proposal and action;
- tool use and coordination;
- evaluation and admission;
- repair, rollback, or escalation; and
- later episode included in `H`.

Conditional on the contributions listed in `E`, the path is computationally
closed when:

1. every required decision not declared as an exogenous choice is determined
   by machinery inside `B`; and
2. every required transition not assigned to a declared environmental service
   is executable by machinery inside `B`.

No indispensable human judgment or manual execution may be hidden in task
admission, decomposition, acceptance, evaluator design, repair, continuation,
or the choice to omit a failed case. A human action that transmits an already
determined exogenous value may be listed in `E`. A human judgment that selects
an undeclared value, or a human action that performs a required transition not
assigned to a declared environmental service, opens the path.

The path may terminate in success, failure, or abstention without a human cut.
Structural closure therefore does not imply competence.

## Capability and warrant remain separate

A no-op policy can be structurally closed. A non-degenerate milestone must add,
over the same selected tasks:

- a predeclared capability or success threshold;
- an evaluator capable of rejecting plausible harmful or inadequate outputs
  on grounds not authored solely by the candidate;
- an externally anchored workload or a coverage threshold that prevents
  self-selected easy cases from standing for a broader target domain; and
- evidence that the closed path reaches commitments consequential to the
  measured capability.

Failure and abstention remain in the selected set and count against capability
or coverage. They do not retroactively falsify structural closure if the system
reached them without a hidden human decision.

This preserves two coordinates:

- **closure:** where the required decisions are made and transitions executed;
  and
- **capability and warrant:** whether those decisions and transitions produce
  acceptable, independently checked outcomes.

## Strength of the supported claim

The evidence determines how broadly closure may be stated.

- A fixed finite suite supports a claim about the attempted paths on that
  suite.
- Tasks sampled by a declared external protocol support a statistical claim
  about that challenge distribution, subject to the sampling evidence.
- An internal task generator supports a claim only about the workload it
  generates under the declared policy. It does not establish coverage of an
  externally defined challenge distribution.
- A task class stated intensionally supports a universal claim only when an
  argument covers every task admitted by the definition. A successful sample
  does not establish this.
- A new task-selection rule creates a new closure claim, even when the system
  and boundary are unchanged.

## Degenerate task scoping

Reject or explicitly label a closure claim when its apparent scope is obtained
by:

- selecting tasks after seeing system performance;
- letting the candidate choose only tasks it expects to solve while calling
  the result closure over the broader class;
- removing failures, timeouts, repairs, or abstentions from the denominator;
- defining the task set by what the system already does;
- using a human to decide acceptance or recovery without naming that export;
- shortening the horizon immediately before the next required human decision;
  or
- changing the objective, evaluator, or boundary after observing an
  inconvenient result.

These are task-selection, boundary, or horizon exports. They do not show that a
decision or transition moved inside the automatic system.

## Relation to the remote-programmer benchmark

For the remote-programmer comparison, `S` selects the same briefs and
repositories for both sides. Client demand choice and final acceptance may
remain declared exogenous inputs. The comparison asks whether the automatic
system carries the programming decisions and execution between those inputs at
least as well as a competent remote programmer under the same tools,
permissions, feedback, resources, and acceptance criteria.

This is a strong capability condition added to task-scoped structural closure.
It is not the definition of all useful progress.
