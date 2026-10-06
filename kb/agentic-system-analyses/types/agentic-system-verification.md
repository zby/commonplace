---
type: types/type-spec.md
name: agentic-system-verification
description: "Independent verification of one stage of an analysis run — records, memory profile or synthesis — with the blockers that send work back and the limits the publication declares"
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

## Blockers and limits

Every finding the verifier does not dismiss is either a blocker or a limit.
`## Blockers` and `## Limits` are each exactly `none`, or a Markdown list with
one `- ` entry per finding; a continuation line is indented. Anything else is
refused. Code continues only when Blockers is `none`.

A **blocker** is a defect that must be repaired before publication: it
undermines a central conclusion, leaves the analysis materially misleading, or
is a known false assertion with a supported correction. It names the full IDs
it concerns, the passage holding the defective text, what is wrong and the
evidence. In a record verification each blocker starts with the one report
whose text must change, `runtime:`, `memory:`, `epistemic:` or
`reconciliation:`; code routes the correction by that word and refuses a
blocker without it. A defect that needs changes in two reports is two blockers.
Profile and synthesis blockers go to the one author of that stage and need no
addressee.

A **limit** is a local unresolved issue the analysis can be published with:
its consequences can be stated, and the remaining conclusions hold. It names
the full IDs it concerns, the issue, and which conclusions readers should
withhold. The synthesis carries every limit into the overview's Limitations
with those IDs; a limit on a profile value is admissible only where the value
itself already expresses the uncertainty (`partial`, `not-determinable` or
`uninspected`), because an overview caveat does not travel with an extracted
value. A disagreement between reports that the sources do not settle is a
limit naming both positions.

Faithfully scoped uncertainty is neither a blocker nor a limit. A review
objection is evidence to assess, not an established defect.

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

## Limits

none
```
