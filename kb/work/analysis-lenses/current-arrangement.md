# Current arrangement

What the live method already decides about layers, lens inputs, depth, stopping
and coverage. Read this before the open questions: several of them already have
an answer in the plan, and the workshop compares options against that answer
rather than against a blank page. Observed on 2026-10-11 from the plan and role
instructions under
`kb/agentic-system-analyses/instructions/analyse-agentic-system/`. Re-check the
files before relying on a detail; the method may have moved.

## Roles and their order

The plan (`plan.yaml`) runs: opening, acquire, boundary, runtime, memory,
epistemic, reconciliation, report-verification, memory-profile,
profile-verification, synthesis, synthesis-verification, overview, publish.
Each analytical role gets a derived check job. Verification is one role that
judges boundary, runtime, memory, epistemic and reconciliation together; there
is no per-role semantic verifier.

## The general layer exists: it is the runtime role

`trace-runtime.md` asks for the consequential claimed work, shipped entry paths,
one ordinary invocation end to end, material routes, load-bearing guarantees
with their enforcement points, and change-admission mechanisms. It says the
report "is not a product inventory" and restricts inspection of permissions,
providers, packaging and the like to where they change claimed work or a
result later analysts rely on. This is the general architectural layer the
operator described, under the name runtime.

The runtime record contract
(`kb/agentic-system-analyses/types/agentic-system-runtime-report.md`) carries
shared records with source anchors: Components, Operative objects, Routes,
Claims, Evidenced absences and Behavioral-authority paths. The union of those
anchors is the set of source paths the general layer located. No separate
"located paths" surface exists or is needed to name that set.

## Lenses exist and receive the map

Memory and epistemic are question-driven investigations with authority to
search the frozen source. In the plan both read `boundary: required` and
`runtime: order-only`. In this engine an order-only input is handed to the
job and the job waits for it, but a change to it does not trigger a rerun
(`src/commonplace/artifactrun/plan.py`, class `Input`). So lenses receive the
general map today, and runtime corrections do not automatically re-run them.

`analyse-memory.md` depends on this: "Choose the memory scope from runtime
routes and state inclusions and exclusions." It also asks the memory analyst
to "cover every included part along the record contract's coverage
dimensions, not only a primary store or the best-understood route", and to
check CLI dispatch, hooks, registered tools and exposed operations against the
routes.

## Stopping rules that already exist

The runtime instruction has an explicit depth and stopping rule for
guarantees: "Inspect the smallest warranted set of forcing cases, ordinarily
two to four for a full code-grounded analysis, and state what remains
unobserved." Both analyst instructions require looking for a source-supported
case that would falsify a consequential claim before settling it.

Worker rules distinguish an uncertainty that only limits a conclusion, which
stays beside the claim, from a scope decision the instruction did not
authorize, which requires a `problem` record (`follow-worker-rules.md`).

## The coverage rule the verifier carries

`verify-reports.md` tells the verifier to "judge coverage against the frozen
repository tree, not just listed anchors", to apply the verification type's
materiality threshold, and not to weaken supported findings to produce uniform
coverage. The verification type sets the threshold at findings that undermine
a central conclusion or leave the analysis materially misleading.

So the method does bound coverage, by materiality and by the declared
boundary, and the type says completeness is "not exhaustive inspection of
repository contents". What it does not state is how the verifier selects
where to search for omissions and when to stop; the instruction's "against
the frozen repository tree" leans exhaustive without saying how far. That
missing selection and stopping rule applies equally to the general layer and
to the lenses, and it is the concrete locus of the
[verification coverage bounds proposal](./proposals/verification-coverage-bounds.md).

## What this means for the open questions

- "How much of the general layer does the runtime role provide?" Nearly all
  of it by intent; whether its depth and declared untraced components suffice
  is an evidence question.
- "Should lenses receive the general map?" They do, order-only. The open part
  is whether that anchors discovery, and whether a runtime correction should
  trigger lens reruns.
- "What is a defensible stopping point?" Runtime has one for guarantees;
  memory has a coverage-dimensions rule; the verifier has a materiality
  threshold but no selection or stopping rule for omission searches.
