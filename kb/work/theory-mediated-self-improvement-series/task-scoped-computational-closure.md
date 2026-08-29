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

Task selection need not be performed by the system. A client or benchmark may
supply tasks as an explicitly exported input. The selection rule must still be
declared because it determines which decision paths the closure claim covers.

## Scope of a closure claim

Declare the following before observing the evaluated outcomes:

- **Task selection:** a finite task set or a rule for sampling tasks from a
  declared challenge distribution. State who applies the rule, whether the
  system may refuse tasks, and how refusals are counted.
- **Objective and acceptance:** the externally fixed result criterion for each
  task and any aggregate threshold used for the selected set.
- **System boundary:** the models, retained artifacts, code, schedulers,
  evaluators, state, tools, and evidence interfaces counted as internal.
- **Exogenous inputs:** observations, client choices, permissions, services, or
  feedback allowed to cross the boundary without being counted as internal
  decisions.
- **Horizon:** the part of execution covered, including repair, recovery, and
  later revision episodes when recurrence is claimed.
- **Resources:** the relevant time, compute, money, tool, and interaction
  limits.
- **Coverage rule:** which selected tasks must reach a terminal result and how
  failures, timeouts, and abstentions affect the claim.

A compact notation is:

    Closed(M | S, A, B, E, H, R, Q)

where `M` is the system, `S` task selection, `A` acceptance, `B` the system
boundary, `E` permitted exogenous inputs, `H` the horizon, `R` resources, and
`Q` the coverage rule. The notation is bookkeeping, not a theorem.

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

The path is computationally closed when every consequential decision on that
path is either:

1. made by machinery inside `B`; or
2. supplied through an input explicitly declared in `E`.

No indispensable human judgment may be hidden in task admission, decomposition,
acceptance, evaluator design, repair, continuation, or the choice to omit a
failed case. A human action that merely transmits an already determined value
does not open the path; a human judgment that selects or settles the value does.

The path may terminate in success, failure, or abstention without a human cut.
Structural closure therefore does not imply competence.

## Capability and warrant remain separate

A no-op policy can be structurally closed. A non-degenerate milestone must add,
over the same selected tasks:

- a predeclared capability or success threshold;
- an evaluator capable of rejecting plausible harmful or inadequate outputs
  on grounds not authored solely by the candidate;
- a coverage threshold that prevents easy cases from standing for the whole
  selection; and
- evidence that the closed path reaches commitments consequential to the
  measured capability.

Failure and abstention remain in the selected set and count against capability
or coverage. They do not retroactively falsify structural closure if the system
reached them without a hidden human decision.

This preserves two coordinates:

- **closure:** where the required decisions are made; and
- **capability and warrant:** whether those decisions produce acceptable,
  independently checked outcomes.

## Strength of the supported claim

The evidence determines how broadly closure may be stated.

- A fixed finite suite supports a claim about the attempted paths on that
  suite.
- Tasks sampled by a declared protocol support a statistical claim about that
  challenge distribution, subject to the sampling evidence.
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
decision moved inside the automatic system.

## Relation to the remote-programmer benchmark

For the remote-programmer comparison, `S` selects the same briefs and
repositories for both sides. Client demand choice and final acceptance may
remain declared exogenous inputs. The comparison asks whether the automatic
system carries the programming decisions between those inputs at least as well
as a competent remote programmer under the same tools, permissions, feedback,
resources, and acceptance criteria.

This is a strong capability condition added to task-scoped structural closure.
It is not the definition of all useful progress.
