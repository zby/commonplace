---
gate_id: prose/redundant-restatement
name: Redundant restatement
description: 'The same content is given twice at a section boundary: an opening paragraph re-explains the previous section, or a closing paragraph previews what the next section then develops.'
type: types/review-gate.md
lens: prose
watches: [body]
staleness: changed
depth: 4
---

## Failure mode

The same content is given twice at a section boundary. A section's opening paragraph re-explains what the previous section already established before reaching its own contribution, or a closing paragraph previews exactly what the next section then develops.

## Test

Read the first paragraph of each section. If it can be deleted and the section still works from the second paragraph onward, it is restating rather than advancing. Report all instances.

**Severity:** WARN when the restatement fills the same argumentative role as the original (e.g., both are thesis statements, or both introduce the same framework). INFO when one is setup and the other is summary — intentional reinforcement at different structural positions is a weaker signal.

Then check the last paragraph before each section heading. If it summarizes or previews what the following section covers, and the section's own content covers the same ground, the preview is redundant. Report all instances.

A one-sentence transition is fine. A full re-explanation, or a full paragraph that duplicates the next section's enumeration, is not.

## Example (fail)

A paragraph says "The conflation arises when higher-level interfaces package bounded calls as chat sessions or framework-managed tool loops" — then the next section enumerates chat sessions, framework-owned tool loops, and continuing agent sessions as the three problem sources. The paragraph and the section cover the same ground.
