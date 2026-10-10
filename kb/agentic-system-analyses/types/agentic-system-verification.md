---
type: types/type-spec.md
name: agentic-system-verification
description: "Independent verification of one stage of an analysis run — analyst reports, memory profile or synthesis — with the blockers that send work back and the limits the publication declares"
schema: ./agentic-system-verification.schema.yaml
---

# Agentic system verification

The judgment of an independent verifier on one stage of an analysis run. A
run has three: the report verification judges the analyst reports and the
reconciliation; the profile verification judges the memory profile against
the accepted records; the synthesis verification judges the public synthesis
against the records it cites. They are the set's `report-verification.md`,
`profile-verification.md` and `synthesis-verification.md` members. Code reads
their blockers to decide what happens next; the overview links each judgment
without copying it. The [record contract](../instructions/agentic-analysis-records.md)
governs the records a verification cites and judges.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-verification.md` |
| `description` | Yes | What was verified and at which boundary |
| `run-id` | Yes | The run's ID |
| `reviewed-boundary` | Yes | The run's immutable revision or capture identity |

## What code checks and what the verifier judges

Code checks form and agreement between members: each citation's destination
and scope, the fields a role must equal, the set's deterministic
cross-member constraints, relation coverage, and quotations against the
frozen source. A verifier does not repeat these checks. The verifier judges
meaning: whether the cited content supports each claim, and whether
qualifications, disagreements between reports and required limitations are
preserved. Each member's type still determines its required content. Code
does not match quotations between members.

## Verification

`## Verification` records what was checked and found: the routes, records,
axes or statements examined, the dispositions, the conflicts checked, and the
consequential limits. It is the verifier's retained account, linked from the overview.
It contains no corrected text: the verifier marks and explains defects, and the
owner of the defective text corrects it.

## Blockers and limits

Every finding the verifier does not dismiss is either a blocker or a limit.
`## Blockers` and `## Limits` are each exactly `none`, or a Markdown list with
one `- ` entry per finding; a continuation line is indented. Anything else is
refused. Code continues only when Blockers is `none`.

A **blocker** is a defect that must be repaired before publication: it
undermines a central conclusion, leaves the analysis materially misleading, or
asserts an unsupported comparison value, evidence strength, absence or complete
coverage. A repairable defect is not automatically a blocker. Explain what
readers or comparison consumers would infer incorrectly and why a stated limit
cannot preserve the bounded account. It cites the records
it concerns, the passage holding the defective text, what is wrong and the
evidence. When the verifying role verifies more than one member (the
layout's `verifies`, which the prompt binds to `verifies`), each blocker starts
with the one member whose text must change, `- <member>: `; code routes the
correction by that name and refuses a blocker without it. A defect that needs
changes in two members is two blockers, and a passage relying on a defective
value is addressed to its own author. A verifier of one member writes no
addressee.

A **limit** is a local unresolved issue the analysis can be published with:
its consequences can be stated, and the remaining conclusions hold. It cites
the records it concerns, the issue, and which conclusions readers should
withhold. The synthesis carries every limit into its Limitations
with those citations; a limit on a profile value is admissible only where the value
itself already expresses the uncertainty (`partial`, `not-determinable` or
`uninspected`), because a synthesis caveat does not travel with an extracted
value. A disagreement between reports that the sources do not settle is a
limit naming both positions.

Local omissions, coarse units and overly cautious assessments can be limits
when they leave the supported conclusions and emitted comparison findings
valid and do not imply absence or complete coverage. A supported mechanism
missing from a partial inventory need not stop publication merely because a
more complete inventory could be written. State the omitted mechanism and
which inventory or route comparisons remain incomplete. If the omission
changes a central conclusion or a system-level comparison value, it is a
blocker. Do not use a limit to excuse an unsupported emitted value or a false
`known`, `absent` or `inapplicable` assessment.

A request for additional inspection or correction names the material conclusion
it could change and why it is needed to support, qualify or withdraw that
conclusion. Completeness is relative to the required analysis questions and
declared evidence boundary, not exhaustive inspection of repository contents.
The presence of additional artifacts alone creates no coverage obligation;
this does not excuse missing evidence needed for a required finding or an
emitted claim.

Faithfully scoped uncertainty is neither a blocker nor a limit. A review
objection is evidence to assess, not an established defect.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Report verification of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} report verification

## Verification

## Blockers

none

## Limits

none
```
