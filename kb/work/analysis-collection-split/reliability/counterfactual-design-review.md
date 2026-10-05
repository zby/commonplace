# Counterfactual design review

Retained discussion at the operator's request, following analysis of why
repeated range-error diagnosis did not initially suggest named IDs. The
reusable procedure is now
[Review design pressure behind recurring errors](../../../instructions/review-design-pressure-behind-recurring-errors.md).
This file retains the episode and reasoning, not a separate operational rule.

## Purpose

When a violation recurs, examine whether a design choice makes the forbidden
behavior attractive. Find interventions that preserve the intended outcome
while changing the conditions that produce the error. Do not stop at stronger
instructions, more checks or cheaper recovery merely because those are useful.

A counterfactual design question asks: if one design choice were different,
would the worker still face the same pressure to deviate? Its answer generates
a hypothesis to evaluate, not proof that the alternative will work.

## The missed question in the range audits

The [first Dynamic Cheatsheet audit](../../analyse-agentic-system-amendments/history/fresh-run-audit.md)
identified range compression in verification summaries, despite workers
having read the full-ID rule. It also identified late checking and a checker
false positive. The
[second audit](../../analyse-agentic-system-amendments/history/second-run-audit.md)
found no verification range retries after local guidance, but still found
ranges in reconciliation, synthesis and epistemic work.

These were useful diagnoses. Their remedies largely held numbered IDs
constant: improve guidance, reject ranges and make repair cheaper. The missing
question was why interval notation suited the writer's immediate task.

The preserved outputs support this causal hypothesis:

1. The writer needs to report coverage or support one claim with several
   records.
2. Numbered IDs repeat long prefixes and convey little about the referents.
3. Sequential suffixes make interval notation a familiar compression.
4. The writer compresses the group for human readability, but the contract
   requires explicit machine-resolvable membership.
5. Changing the identifier design could reduce that pressure without changing
   the requirement for exact references.

One verifier used ranges in its opening inventory but named routes
individually when explaining their mechanisms. The writing situation matters:
group summaries invite a compression that individual analysis does not.
This is an inference from observed writing, not evidence of private reasoning.

The [named-ID plan](./short-named-record-ids-plan.md) changes the upstream
design choice. The audits already contained enough observations to propose
that alternative. They did not establish its reliability benefit, and neither
does its subsequent adoption.

## Development of the procedure

The following records how the procedure was developed; use the library
instruction above for execution.

The intended result is an explanation that connects evidence to a repair,
plus meaningful alternatives where the design itself can change. The
following questions are a supported route, not a requirement to perform a
large brainstorming exercise for every isolated typo.

1. **What was the worker trying to accomplish at the point of deviation?**
   Identify the local task: summarize coverage, distinguish objects, quote a
   passage, or something else. “Follow the instructions” is not an adequate
   account of that task.
2. **What makes the forbidden behavior convenient?** Look for less repetition,
   familiar notation, fewer lookups or easier expression. Distinguish observed
   behavior from hypotheses about motivation.
3. **Which of our design choices creates that convenience?** Examine the
   output contract, identifiers, supplied inputs, tool interface and division
   of work. Do not assume that a clear rule implies a good interface.
4. **What outcome must survive a design change?** State the invariant apart
   from its current implementation. Here it is stable identity and explicit
   reference membership, not numeric suffixes.
5. **What alternative removes or reduces the pressure?** Change one relevant
   choice in the hypothetical design. Explain why the error should become
   less attractive, unnecessary or impossible in its demonstrated form.
6. **What new errors and costs would it introduce?** Specify an observation
   that would weaken the hypothesis. For named IDs, spelling variants,
   collisions, unstable names and vague group references remain concerns.

When consequential alternatives exist, compare intervention levels before
settling: help the worker comply with the current design; change the design
that creates the pressure; or deliberately support the behavior under a
revised contract. Not all three need to be viable. Record why an unavailable
or unjustified option is excluded.

## Boundaries and stopping conditions

Repeated violations are a trigger to inspect design, not proof that design is
the cause. An isolated violation can also justify inspection when its cost is
high or the mechanism is clear. Do not invent a numerical recurrence threshold
from these two runs.

Keep evidence, explanation and intervention separate. A successful check shows
that a defect is caught. A successful retry shows recovery. Neither establishes
that the upstream pressure has been removed. A plausible redesign also does
not establish an observed improvement.

Stop when the available evidence supports a bounded intervention or a
meaningful discriminating question. If the local writing situation cannot be
reconstructed, identify the missing evidence rather than substituting a
general claim about model habits. If no practical alternative emerges, retain
the current enforcement and record that limit; do not force a redesign.

For consequential changes, return the hypothesis, preserved invariant,
trade-offs and unresolved evidence to the operator. This diagnosis method does
not expand implementation authority.

## What to retain from this episode

The gap was not only insufficient depth. The earlier reasoning repeatedly
searched for repairs within the existing design. A deeper explanation could
still have stopped at “models compress lists.” Counterfactual questions make
the upstream design choice available for reconsideration.

This episode supports a specific correction to diagnosis practice. It does
not establish that all prior brainstorming was shallow, or that named IDs
are always preferable to numbers. The useful lesson is to inspect the fit
between the task and the chosen interface when enforcing a clear rule keeps
requiring repairs.
