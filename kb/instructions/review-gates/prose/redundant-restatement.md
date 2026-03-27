---
gate_id: prose/redundant-restatement
name: Redundant restatement
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

A section's opening paragraph re-explains what the previous section already established before reaching its own contribution.

## Test

Read the first paragraph of each section. If it can be deleted and the section still works from the second paragraph onward, it is restating rather than advancing. Report all instances.

**Severity:** WARN when the restatement fills the same argumentative role as the original (e.g., both are thesis statements, or both introduce the same framework). INFO when one is setup and the other is summary — intentional reinforcement at different structural positions is a weaker signal.

A one-sentence transition is fine. A full re-explanation is not.
