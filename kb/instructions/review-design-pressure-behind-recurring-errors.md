---
type: types/instruction.md
description: "Use when an agent repeatedly violates a clear rule, or repairs keep adding reminders and checks; examine whether the task or interface makes the forbidden behavior convenient."
---

# Review design pressure behind recurring errors

Enable the operator to choose a repair that preserves the intended outcome
and addresses what makes a recurring deviation attractive, rather than merely
strengthening enforcement.

The investigation is complete when the evidence supports that choice or
identifies the unresolved question that prevents it. Choose the investigative
route from the available evidence; the questions below are aids, not a required
sequence.

## When to use

Use during diagnosis of agent-operated KB workflows when a clear-rule
violation recurs, or when successive repairs strengthen enforcement without
explaining why the same behavior keeps appearing. An isolated costly error
also qualifies when its local mechanism is inspectable.

Do not substitute this review for urgent containment or a required acceptance
check. Do not assume that recurrence proves a design defect.

For now the operator invokes this instruction explicitly. No procedure
triggers it yet, and it is not an automatic gate on every repair.

## Inputs and authority

Use the observed deviation, the intended outcome, the applicable contract and
available artifacts or traces. Identify which instructions and interfaces the
worker actually received; report delivery as unknown when it is not visible.

The result is a diagnosis and a repair recommendation. This instruction grants
no authority to change contracts, implement a redesign, launch workers or run
experiments. Keep any comparison, evidence boundary or resource limit the
commission fixes. Return to the task owner when a choice would change
acceptance or affect other work, or when further evidence needs new authority
or resources.

## Investigative discretion

Choose which artifacts to inspect, which hypotheses to pursue and how to
compare alternatives within the task's evidence and resource bounds. Reorder,
combine or skip questions when they add no decision value. Follow newly
exposed evidence even when it contradicts the initial design-pressure
hypothesis; keeping the current design is an acceptable conclusion.

## Questions that may help

- What concrete task was the worker performing at the point of deviation?
  Where does the behavior appear, and where does it not?
- What must remain true after repair, independently of the current format,
  identifiers, tools or division of work? Which choices can be reconsidered?
- What does the forbidden behavior save or simplify: repetition, lookups,
  tool calls or expression?
- Which design choice might create that pressure? If it were different,
  would the worker still have the same reason to deviate?
- What alternative preserves the intended outcome while reducing that
  pressure? How does it compare with helping the worker comply or deliberately
  supporting the behavior under a revised contract?
- What new errors, maintenance or worker burden would the alternative create?
  What observation would weaken the explanation or reverse the recommendation?

Do not infer private reasoning from an output alone, assume a clear rule is
a good interface, or force every intervention category into the comparison.
Keep observations, causal hypotheses and expected benefits distinguishable.

## Result

Report the decision the evidence supports, its basis and limits, and the
trade-off that matters. Use whatever concise structure makes those clear;
there is no required report template.

For a proposed redesign, identify the outcome it preserves, the contributing
design choice, why changing it should help, and its replacement risks and
cost. If no design contribution is supported, say so and recommend current
enforcement or another supported repair.

Accept partial findings when evidence is missing. Name the unresolved
question and the smallest authorized observation that could change the
choice. Stop when further inspection
would not change the recommendation; do not turn every formatting error into
a broad redesign exercise.

## Verify

- The diagnosis explains a concrete writing or execution situation, not just
  that models sometimes ignore rules.
- The intended outcome is distinct from its current implementation.
- At least one consequential design choice was examined, even if retained.
- Observations, causal hypotheses and expected benefits are distinguishable.
- A successful check is treated as detection, and a successful retry as
  recovery; neither is presented as proof of prevention.
- The recommendation preserves required acceptance checks and does not expand
  implementation authority.
