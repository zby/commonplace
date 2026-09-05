---
name: scan-agentic-system-transfer
description: Use when asked what a completed analyse-agentic-system result currently suggests for Commonplace under a named design question or priority. Produces selective living state, never system characterization or matrix data.
type: kb/types/instruction.md
user-invocable: true
argument-hint: "<main-review result.md path> plus <current Commonplace question or priority> and optional state output path"
context: fork
---

# Scan an Agentic System for Current Transfer

Produce a selective current account of the external mechanisms that matter to a Commonplace question without changing the source-faithful external analysis or treating omitted differences as absent.

## Prerequisites

- Use the main-review result and interest brief supplied in `$ARGUMENTS`, the user request, or an invoking worker packet. If either cannot be identified unambiguously, stop and ask for the missing input.
- One exact `analyse-agentic-system` result at
  `kb/reports/state/agentic-system-analysis/<run-id>/result.md`, with its sibling
  `run-state.md`. Both `run-status` and `result-disposition` must be `complete`.
  The result is the authority for what the external system does; do not
  reacquire or refresh its sources during this scan.
- An explicit current question, design problem, or priority. A generic request to find every difference is not a valid brief. If the user asks broadly what is interesting, state the bounded standing concern you will use before selecting findings.
- Read access to the Commonplace artifacts needed to establish the current local analogue.
- Explicit file-output authority when the result should be written. Without it, return the scan in the response.
- A legacy memory review, compact public review, response, summary, or run ID
  alone is insufficient input, including for a response-only scan. Report the
  missing exact result or completion evidence; do not fall back to another
  analysis or produce transfer findings from the insufficient input.

## Boundaries

This is an interest-conditioned transfer scan, not a complete delta. Omission means only `not selected under this brief`; it never means that the systems are identical on that point or that no other difference exists.

Do not edit the external analysis, its matrix fields, `systems.csv`, a public landscape analysis, or any Commonplace note, proposal, instruction, reference artifact, or implementation. Return promotion candidates to the caller; a later authorized operation decides their disposition.

Use Commonplace ontology to name mechanisms when the external analysis supports the mapping. Preserve the external system's native mechanism, the mapping rationale, and any qualification. Do not turn a partial analogy into identity.

## Steps

0. **Verify the main-review input.** From the repository root, run
   `commonplace-agentic-analysis-handoff <run-state-path>` on the sibling state.
   Require exit status zero and substantive result disposition `complete`;
   a completed blocked or out-of-scope run is not a transfer input. Require the
   supplied result path to match `run-state.result.path`. If the caller supplied
   a result SHA-256, require it to match `run-state.result.sha256` and the file's
   bytes. Read the full exact result, including its evidence boundary, relevant
   shared records, lens findings, and limitations. Any validation, identity,
   or completion failure stops the scan without findings; report the failure
   to the caller for correction through the main review workflow.
1. **Fix the three substantive inputs and production provenance.** Copy the
   current interest brief exactly. Record the run ID, run-state path, source
   identity and reviewed boundary, and exact result's path, byte length, and
   SHA-256. Identify only the Commonplace artifacts actually
   consulted and record each path and SHA-256. Also record
   `scan-agentic-system-transfer` as the producing instruction and record model
   or runner provenance only when the harness supplies it; never infer missing
   provenance.
2. **Establish the current analogue.** Read the minimum Commonplace system-definition and knowledge artifacts needed to answer the brief. Distinguish shipped behavior from proposals, notes, and work in progress. Do not use a proposal or note as evidence that Commonplace already implements a mechanism.
3. **Select, do not enumerate.** Choose zero to five differences, tensions, confirmations, or implementation variants that could change the current decision. Prefer mechanisms with a named consequence over attractive features. A similarity belongs only when it confirms or challenges a live choice. If nothing clears that threshold, return a valid zero-finding scan.
4. **Write each finding as a transfer candidate.** Include:
   - the external mechanism and its evidence-bearing section and canonical
     record IDs in the exact result, preserving its conclusion status and
     inspected boundary;
   - the Commonplace ontology mapping and why it fits, including `partial` or `uncertain` when needed;
   - the current Commonplace analogue, with the consulted artifact path;
   - the selected difference or confirmation;
   - why it matters under this interest brief now;
   - the smallest consequence worth considering; and
   - a disposition: `promote candidate`, `proposal candidate`, `experiment candidate`, `watch under this brief`, or `no action`.
5. **Recheck the inputs.** Immediately before returning findings or writing
   state, repeat step 0 and recompute the result and consulted-Commonplace
   fingerprints. If validation fails, withhold the findings and report the
   blocker. If any fingerprint or the interest brief changed, discard the
   draft and restart from step 0 against the newly identified inputs.
6. **Route the living result.** Return response-only unless the caller authorized a state output. Written scans live under `kb/reports/state/agentic-system-transfer/` because their LLM judgments and unresolved candidate dispositions are not reproducible cache. Use a filename that combines the system and an interest-brief slug. A scan becomes stale when the exact-result digest changes, any consulted Commonplace artifact changes, or the interest brief changes. Do not overwrite or delete an open scan merely because it is stale: first record `no action`, promote each accepted consequence through a separately authorized operation, or receive explicit discard authority. Until then, write the new scan to a collision-safe sibling and mark the prior path as superseded when authorized. After every candidate has a durable disposition elsewhere or `no action`, the owning workflow may replace or delete the state report.

## Output

Open with:

`subject | analysis run ID and run-state path | source identity and reviewed boundary | exact result path, byte length, and SHA-256 | interest brief | consulted Commonplace paths and hashes | producing instruction | harness-supplied model/runner or not supplied | generated date | selective/non-exhaustive: yes`

Then give the selected findings and finish with:

- promotion candidates, if any;
- unresolved evidence limits; and
- the three invalidation conditions above; and
- whether every candidate is disposed and the state is therefore safe to replace or delete.

Do not add a difference count, coverage percentage, or claim that the scan exhausts the external analysis.

## Verify

- Initial and final completion/identity checks passed for the same exact result.
- Every external-system claim resolves to the exact result's findings and
  canonical records. No legacy review or compact summary supplied a finding,
  and no conclusion status or absence claim was inferred from omission.
- Every statement about current Commonplace resolves to a consulted artifact and distinguishes implemented behavior from proposed or explanatory material.
- Every ontology mapping includes a reason and preserves partial or uncertain fit.
- Every selected finding states why it matters under the recorded brief; generic admiration is absent.
- Omission carries no negative meaning, the result feeds no matrix or public corpus statistic, and no candidate was promoted automatically.
- A response or written result records the exact-result fingerprint, all three
  freshness inputs, run and production provenance, and the successful final
  input recheck. A written result also records the cleanup condition.
