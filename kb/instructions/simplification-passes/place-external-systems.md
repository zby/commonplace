---
description: "Use when an artifact should position named external systems against its own criteria or obligations, so readers can locate their systems on it, and the placements must survive the systems' authors reading them"
type: types/edit-operation.md
effort: simple
decision: none
---

# Place external systems

Give the artifact a map of named systems against its criteria, with every
placement supported by a code-grounded main-review output or an explicitly
identified source ingest the KB already holds.

Effort: simple. Lookup and summary from generated main-review files; the
operator checks the contestable list.

## Steps

The caller supplies the evidence as inputs: each generated main review from
`kb/agentic-systems/reviews/` under a role beginning with `review`, such as
`review-mem0`; each tracked `kb/sources/` ingest under a role beginning with
`ingest`; and, where a compact review is not enough, the output of
`commonplace-agentic-analysis-handoff <run-state-path>` for that review's
exact result under a role beginning with `handoff`. Use only these files.

1. Admit a supplied main review only when it has
   `generated-by: analyse-agentic-system`, `analysis-run`, `source-identity`,
   and `reviewed-revision`. Read the evidence basis and admit only findings
   supported by inspected code at the named revision. Record each input's
   origin path, run ID and source revision in the report. An ingest may
   independently supply code-grounded findings; identify it as an ingest, not
   a main review. Do not use a legacy memory review or use it to fill gaps in
   a main review.
2. For each proposed placement, identify the supporting section and sentence
   before drafting. Use a handoff input only when it reports exit status zero,
   substantive result disposition `complete`, and the run, source revision
   and generated-review path of the review it supports; record its canonical
   record IDs. If the required support is missing from the inputs, omit that
   placement and report the gap. Do not acquire new sources or infer a
   mechanism from the system's claims or from omission.
3. For each supported placement, state in one or two sentences what the system
   retains, what admits a change, and which criteria the evidence supports or
   rules out within its inspected boundary. Mark uninspected criteria as
   uninspected. Say what a gate judges and keep wiring, observed operation, and
   causal effect separate.
4. Close with what the selected placements show together and which criteria
   their evidence does not test. Do not generalize that limit into a claim
   about every system.
5. Link each placement to the tracked main-review file or ingest that supports
   it. A tracked artifact must not depend on an ignored exact result being
   present. If the needed support exists only in local state, return the
   proposed placement and its retention or regeneration requirement in the
   report; do not insert it into the artifact or point to an insufficient
   compact review as though that file carried the evidence.

## Report

The paragraph; input identities; withheld placements and their missing
support; and placements a system's author would contest, each with the
supporting section and sentence for the operator to check. The route records
each input's hash in its observation.

## Preserve

The artifact's criteria as stated. A system that does not fit them
is evidence about the criteria for the operator, not a reason to adjust them
in this pass.
