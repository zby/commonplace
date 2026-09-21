# First experiment: a retained procedure for later improvement

## Question

Does a natural-language improvement procedure developed from earlier failures
help an agent make better subsequent improvements under a matched budget?
The procedure must change how improvement work proceeds, rather than merely
provide the answer to a later task. This sketch combines imports 1 and 2 from
the [agenda](./imports.md); imports 3–5 inform controls and accounting.

## Candidate comparison

Use earlier development episodes to formulate a scoped procedure for one
recurring kind of diagnosis or revision. Freeze the procedure before testing
it on separate later episodes. Select the workflow from available evidence:
it must have repeatable starting states, enough comparable cases, and an
outcome that can be assessed separately from the proposing agent's approval.

Compare the retained-procedure condition with a baseline that receives the
same model, tools, task requirements, relevant facts, and budget, but lacks the
learned procedure. Specify exactly what prior records the baseline receives.
Withholding both the procedure and information needed to solve the task would
confound procedural benefit with an information advantage.

If the initial comparison supports benefit, a content control can ask whether
the specific advice matters: replace it with plausible generic or mismatched
advice of comparable form. This is a proposed follow-up, not a mandatory
third arm before the available cases and costs are understood.

## Evidence to collect

- The versioned procedure and development evidence used to construct it.
- Which later diagnosis, candidate, or test choice consumed its content;
  record alternatives actually considered, not an invented search history.
- Quality of the resulting change on a separate assessment of its operation,
  alongside regressions and unsuccessful attempts.
- Total model work, elapsed time, and human contributions, including procedure
  construction and review. Report upfront costs and the horizon over which
  later savings might repay them.
- Cases where the procedure did not apply, supplied no useful direction, or
  made the result worse. These can support rescoping or withdrawal as well as
  revision.

Semantic judgments are permitted where task quality requires them. Fix their
criteria independently of the candidate's self-assessment, document judge
roles and uncertainty, and use executable or observable outcomes where the
task supplies them. Model identity alone does not establish judge independence.

## What results could establish

Changed branch choices support a claim about search behavior. Better assessed
results under matched conditions support bounded benefit. Connecting the two
requires evidence that the retained content caused the consequential choice;
an agent's citation is a trace, not causal proof. One successful later episode
does not establish sustained compounding or autonomous self-improvement.

## Decisions before any run

Select the target workflow and cases, define improvement and regression,
freeze development versus assessment evidence, and specify model, conditions,
budgets, repetitions, judging, and stopping rules. Check the
[component-comparison workshop](../explanatory-theories-deployment-time-learning/README.md)
and [compounding protocol](../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
for reusable controls. Replan if comparable episodes or a credible outcome
assessment are unavailable; do not replace them with internal review scores
and claim the same experiment was run.

This file commissions no execution. Its next deliverable is a concrete,
reviewable protocol or a reasoned decision that the proposed comparison is
not yet feasible.

## Separate question: when to codify a learned operation

When an operation's intended meaning and behavior become sufficiently clear,
compare continued interpretation with a codified version of that operation.
Keep the surrounding methodology and outcome criteria fixed. Specify which
judgments the symbolic consumer replaces and which remain interpreted; do not
assume the whole procedure is ready for codification.

Assess preservation of useful behavior on separate cases, interpretation
errors, and total cost, including implementation, checking, and maintenance.
A faster operation that changes the intended decision fails the preservation
claim. Agreement with the interpreter alone does not establish correctness;
both versions must face the outcome assessment. Continued interpretation or
revision of the proposed encoding are valid outcomes.

This comparison tests the selective-codification part of the
[development path](./README.md#start-with-underspecified-methodology-codify-what-becomes-clear).
It supplies no requirement that a learned method eventually become code.
