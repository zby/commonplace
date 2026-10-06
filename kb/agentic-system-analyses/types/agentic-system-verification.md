---
type: types/type-spec.md
name: agentic-system-verification
description: "Independent verification of one stage of an analysis run — records, memory profile or synthesis — with the blockers that send work back"
schema: ./agentic-system-verification.schema.yaml
---

# Agentic system verification

The judgment of an independent verifier on one stage of an analysis run. A
run has three: the record verification judges the analyst reports and the
reconciliation; the profile verification judges the memory profile against
the accepted records; the synthesis verification judges the public synthesis
against the records it cites. Each is a document in the run directory. Code
reads its blockers to decide what happens next and copies its verification
text into the overview's `## Verification and blockers`.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-verification.md` |
| `description` | Yes | What was verified and at which boundary |
| `run-id` | Yes | The run's ID |
| `reviewed-boundary` | Yes | The run's immutable revision or capture identity |
| `verifies` | Yes | `records`, `profile` or `synthesis` |

## Verification

`## Verification` records what was checked and found: the routes, records,
axes or statements examined, the dispositions, the conflicts checked, and the
consequential limits. It is the verifier's account for the overview's readers.
It contains no corrected text: the verifier marks and explains defects, and the
owner of the defective text corrects it.

## Blockers

`## Blockers` is exactly `none`, or a Markdown list with one `- ` entry per
blocker; a continuation line is indented. Anything else is refused. Code
continues only on `none`.

A blocker is a defect that a change to one document can repair. It names the
full IDs it concerns, the passage holding the defective text, what is wrong and
the evidence. In a record verification each blocker starts with the one report
whose text must change, `runtime:`, `memory:`, `epistemic:` or
`reconciliation:`; code routes the correction by that word and refuses a
blocker without it. A defect that needs changes in two reports is two blockers.
Profile and synthesis blockers go to the one author of that stage and need no
addressee.

An unsupported finding, value or statement is a blocker. Faithfully scoped
uncertainty is not.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Record verification of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
verifies: records
---

# {System} record verification

## Verification

## Blockers

none
```
