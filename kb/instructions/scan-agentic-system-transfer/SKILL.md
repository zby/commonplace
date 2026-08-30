---
name: scan-agentic-system-transfer
description: Use when asked what an existing external-system analysis currently suggests for Commonplace under a named design question or priority. Produces selective living state, never system characterization or matrix data.
type: kb/types/instruction.md
user-invocable: true
argument-hint: "<external analysis path or result> plus <current Commonplace question or priority> and optional state output path"
context: fork
---

# Scan an Agentic System for Current Transfer

Produce a selective current account of the external mechanisms that matter to a Commonplace question without changing the source-faithful external analysis or treating omitted differences as absent.

## Prerequisites

- Use the external analysis and interest brief supplied in `$ARGUMENTS`, the user request, or an invoking worker packet. If either cannot be identified unambiguously, stop and ask for the missing input.
- One completed, inspectable external-system analysis or agent-memory-system review. It is the authority for what the external system does; do not reacquire or refresh its sources during this scan.
- An explicit current question, design problem, or priority. A generic request to find every difference is not a valid brief. If the user asks broadly what is interesting, state the bounded standing concern you will use before selecting findings.
- Read access to the Commonplace artifacts needed to establish the current local analogue.
- Explicit file-output authority when the result should be written. Without it, return the scan in the response.

## Boundaries

This is an interest-conditioned transfer scan, not a complete delta. Omission means only `not selected under this brief`; it never means that the systems are identical on that point or that no other difference exists.

Do not edit the external analysis, its matrix fields, `systems.csv`, a public landscape analysis, or any Commonplace note, proposal, instruction, reference artifact, or implementation. Return promotion candidates to the caller; a later authorized operation decides their disposition.

Use Commonplace ontology to name mechanisms when the external analysis supports the mapping. Preserve the external system's native mechanism, the mapping rationale, and any qualification. Do not turn a partial analogy into identity.

## Steps

1. **Fix the three substantive inputs and production provenance.** Record the external analysis identity and SHA-256 when it is a file; copy the current interest brief exactly; identify only the Commonplace artifacts actually consulted and record each path and SHA-256. If the external input is a response or package rather than one file, record its run/result identity and resolvable parts. Also record `scan-agentic-system-transfer` as the producing instruction and record model or runner provenance only when the harness supplies it; never infer missing provenance.
2. **Establish the current analogue.** Read the minimum Commonplace system-definition and knowledge artifacts needed to answer the brief. Distinguish shipped behavior from proposals, notes, and work in progress. Do not use a proposal or note as evidence that Commonplace already implements a mechanism.
3. **Select, do not enumerate.** Choose zero to five differences, tensions, confirmations, or implementation variants that could change the current decision. Prefer mechanisms with a named consequence over attractive features. A similarity belongs only when it confirms or challenges a live choice. If nothing clears that threshold, return a valid zero-finding scan.
4. **Write each finding as a transfer candidate.** Include:
   - the external mechanism and its evidence-bearing location in the completed analysis;
   - the Commonplace ontology mapping and why it fits, including `partial` or `uncertain` when needed;
   - the current Commonplace analogue, with the consulted artifact path;
   - the selected difference or confirmation;
   - why it matters under this interest brief now;
   - the smallest consequence worth considering; and
   - a disposition: `promote candidate`, `proposal candidate`, `experiment candidate`, `watch under this brief`, or `no action`.
5. **Route the living result.** Return response-only unless the caller authorized a state output. Written scans live under `kb/reports/state/agentic-system-transfer/` because their LLM judgments and unresolved candidate dispositions are not reproducible cache. Use a filename that combines the system and an interest-brief slug. A scan becomes stale when the external analysis changes, any consulted Commonplace artifact changes, or the interest brief changes. Do not overwrite or delete an open scan merely because it is stale: first record `no action`, promote each accepted consequence through a separately authorized operation, or receive explicit discard authority. Until then, write the new scan to a collision-safe sibling and mark the prior path as superseded when authorized. After every candidate has a durable disposition elsewhere or `no action`, the owning workflow may replace or delete the state report.

## Output

Open with:

`subject | external analysis identity and hash | interest brief | consulted Commonplace paths and hashes | producing instruction | harness-supplied model/runner or not supplied | generated date | selective/non-exhaustive: yes`

Then give the selected findings and finish with:

- promotion candidates, if any;
- unresolved evidence limits; and
- the three invalidation conditions above; and
- whether every candidate is disposed and the state is therefore safe to replace or delete.

Do not add a difference count, coverage percentage, or claim that the scan exhausts the external analysis.

## Verify

- Every external-system claim resolves to the completed analysis rather than recollection or newly acquired sources.
- Every statement about current Commonplace resolves to a consulted artifact and distinguishes implemented behavior from proposed or explanatory material.
- Every ontology mapping includes a reason and preserves partial or uncertain fit.
- Every selected finding states why it matters under the recorded brief; generic admiration is absent.
- Omission carries no negative meaning, the result feeds no matrix or public corpus statistic, and no candidate was promoted automatically.
- A written result is response-only or authorized operational state with all three freshness inputs, production provenance, and the cleanup condition recorded.
