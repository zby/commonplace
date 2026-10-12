# Audit a rerun before integration

Help the batch coordinator decide whether a newly published analysis is ready
to integrate. Catch consequential omissions, contradictions and hidden
operational problems cheaply. Compare with legacy accounts to detect coverage
regressions, not to preserve every old detail or treat the old account as truth.
This is a bounded independent audit, not a second analysis.

## Commission and boundaries

The coordinator supplies the target and run, prepared worktree and command
environment, frozen source boundary, new publication, relevant historical
accounts, available run/trace evidence, and an owned report path under this
workshop's `audits/`. Use the fresh Sol auditor specified by the
[workshop plan](./README.md).

You may read those materials and investigate discrepancies against the frozen
sources. Historical accounts are leads; differences in revision, scope or
accuracy may explain apparent losses. This access belongs only to the audit
and must not feed legacy findings back into the source-first analysis.

Write only your audit report. Do not edit analysis content, sources, engine
state or the checklist; advance runs; integrate; commit; or delegate. The batch
coordinator owns recovery and integration.

## Judgment sought

Choose the inspection method. Concentrate on differences that change a reader's
understanding of the system, and whether the public overview and synthesis
carry necessary qualifications. Check operational evidence sufficiently to
avoid presenting publication success as proof that every worker obligation
was fulfilled. Investigate sources or traces where a consequential question
requires them, not as a routine exhaustive pass.

Return one disposition:

- **integrate** — no consequential problem established within the inspected scope;
- **integrate with recorded limits** — useful result with necessary qualifications
  already visible in the published analysis;
- **hold** — a specific suspected defect or missing qualification needs resolution.
  State what would unblock integration.

A qualification written only in your audit cannot repair its absence from the
published analysis. Missing evidence is a stated limit, not an invented pass.
If further investigation would become substantial, return the bounded finding
and what follow-up would decide it rather than silently undertaking a reanalysis.

Retain a concise, validated report with run/method/source identity, auditor
profile, historical comparison boundaries, consequential findings and evidence
locators, coverage limits, and the disposition. Return its path and any blocker.
The coordinator chooses a supported recovery route or asks the operator; the
auditor does not patch accepted outputs.

## Optional shortcuts from earlier audits

The [report statistics script](../../../scripts/agentic_system_rerun_stats.py)
is ready to use for a cheap report inventory; point it at this run's new output,
not an older origin copy. It does not inspect sources or runtime evidence.

Stored attempts and judgments can narrow trace work to reported problems and
refusals. Distinguish semantic objections from deterministic validation failures.
For an apparent preflight/engine disagreement, compare candidate and input
versions before concluding that the checks disagree. When using nested traces,
pair exact call/result identifiers within the same worker; an unexecuted tool
proposal is not an action. These are useful shortcuts, not required audit steps.
