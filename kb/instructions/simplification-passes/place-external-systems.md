---
description: "Use when an artifact should position named external systems against its own criteria or obligations, so readers can locate their systems on it, and the placements must survive the systems' authors reading them"
type: kb/types/instruction.md
effort: simple
---

# Place external systems

Give the artifact a map of named systems against its criteria, with every
placement supported by a code-grounded main-review output or an explicitly
identified source ingest the KB already holds.

Effort: simple. Lookup and summary from generated main-review files; the
operator checks the contestable list.

1. Select generated reviews directly under `kb/agentic-systems/reviews/` with
   `generated-by: analyse-agentic-system`, `analysis-run`, `source-identity`,
   and `reviewed-revision`. Read the evidence basis and admit only findings
   supported by inspected code at the named revision. Record each input path,
   SHA-256, run ID, and source revision in the report. A `kb/sources/` ingest
   may independently supply code-grounded findings; identify it as an ingest,
   not a main review. Do not select a legacy memory review or use it to fill
   gaps in a main review.
2. Read the selected file directly. For each proposed placement, identify the
   supporting section and sentence before drafting. If the compact review is
   insufficient and its exact `result.md` is available, run
   `commonplace-agentic-analysis-handoff <sibling-run-state-path>` from the
   repository root. Require exit status zero, substantive result disposition
   `complete`, and matching run, source revision, and generated-review path.
   Read the exact result's relevant records and limitations and record its
   SHA-256 and canonical record IDs. If the required support is still missing
   or validation fails, omit that placement and report the gap. Do not acquire
   new sources or infer a mechanism from the system's claims or from omission.
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
6. Before returning or applying the paragraph, recheck the input hashes and
   any completion check used in step 2. If an input changed or validation
   fails, withhold the affected placement and report the changed input.

Report: the paragraph; input identities and hashes; withheld placements and
their missing support; and placements a system's author would contest, each
with the supporting section and sentence for the operator to check.

Preserve: the artifact's criteria as stated. A system that does not fit them
is evidence about the criteria for the operator, not a reason to adjust them
in this pass.
