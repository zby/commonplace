---
type: reference/types/design-proposal.md
description: "Proposal (adopted): permit analysis publication with explicit local unresolved issues, while blocking misleading conclusions and preserving uncertainty for comparison consumers"
---

# Publishing analyses with unresolved issues

Adopted on 2026-10-06 by ADR 109, *Publish analyses with declared limits*:
verifiers classify each unresolved finding as a blocker or a limit, limits
travel into the overview's Limitations, and a limit on a profile value is
admissible only where the value expresses the uncertainty. What follows is the
proposal as it stood when selected on 2026-10-05, kept as the dated record of
the design space; the ADR carries the decision and its alternatives.

## Current state (as of 2026-10-05)

The motivating analysis run stopped when a second synthesis verification
found an overstatement after the single permitted correction had been used.
The subsequent synthesis-distinction pilot did not establish that additional
writer and reviewer instructions prevent the defect. Its retained record is
`kb/reports/retained/synthesis-distinction-pilot-20261005/README.md`;
`scores.md` in that directory records missed defects, omissions and false
objections. These observations motivate a publication-policy change but do
not establish its reliability.

[ADR 107](../../adr/107-classify-memory-by-scoped-findings.md) delivered the
revised classification contracts. Profiles at revision 2 of
`memory-comparison` keep each finding on a scoped unit and can mark a unit
or axis `partial`, `not-determinable` or `uninspected`; the
[profile type](../../../agentic-system-analyses/types/agentic-system-memory-profile.md)
defines that representation. This proposal must build on those contracts
rather than redesign them.

## Proposed publication policy

Verification continues to report findings candidly. The coordinator decides
whether each unresolved finding prevents publication:

- Block when an issue undermines a central conclusion or leaves the analysis
  materially misleading.
- Permit publication when an issue is local, its consequences can be stated
  explicitly, and the remaining conclusions still hold.

A known overstatement with a supported correction should be corrected. A
generic disclaimer does not justify leaving a known false assertion in place.
For a genuinely unresolved disagreement, the published account must identify
what is disputed and which conclusions readers should withhold. A review
objection is evidence to assess, not automatically an established defect.

### Placement of limitations

Use one overview section, **Limitations and unresolved issues**, linking to
the affected records and explaining the consequences of each issue. Extend
the existing limitations surface where possible rather than duplicate it.

Qualify an individual record only where necessary for that record to be
interpreted correctly on its own. Do not require a limitations section on
every record or duplicate uncertainty already expressed there.

For structured profile values consumed by comparisons, represent uncertainty
in the value itself under the revised classification contract, or exclude
the disputed value from comparisons. An overview caveat alone is insufficient
because it does not travel with an extracted value.

## Options and tradeoffs

The operator's preferred option is coordinator disposition of review
findings, with explicit published limitations. The analysis workflow and
publication checks would consume that disposition with authority to permit
publication; overview readers would consume the limitations; comparison
consumers would honor uncertainty in profile values. Those paths must agree
before this policy can operate. Structural validity and publication integrity
requirements remain prerequisites.

Requiring resolution of every finding retains a simpler acceptance rule but
can stop useful work on a local issue. An analyst-callable verifier could
provide earlier correction opportunities, but adds a feedback loop and must
handle false objections. The operator preferred the publication-policy option
to that added complexity; this proposal does not introduce such a loop.

The preferred option shifts judgment to whether a finding materially limits
publication. It does not strengthen the semantic verifier or make coordinator
judgment a correctness guarantee. Its review warrants remain source evidence
and the analysis contracts, with the observed possibility of missed defects
and false objections.

## Adoption criteria and free choices

Before implementation, reconcile this proposal with the revision-2 profile
contracts. Implementation must show that a local unresolved issue
can be published with specific consequences, a misleading central conclusion
still blocks publication, and disputed profile values cannot silently enter
comparisons as settled findings. Records read independently must remain
truthful without relying on the overview caveat.

The disposition format, precise contract changes and verification examples
remain implementation choices. Adopt the policy coherently across review,
coordinator decisions, publication and comparison consumers. Recording this
proposal neither resumes a stopped run nor authorizes publication of an
existing candidate.
