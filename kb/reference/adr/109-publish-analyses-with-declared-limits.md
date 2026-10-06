---
description: "Verifiers classify each unresolved finding as a blocker that must be repaired or a limit the analysis is published with; limits travel into the overview's Limitations and, for profile values, into the value itself"
type: reference/types/adr.md
status: accepted
---

# 109 — Publish analyses with declared limits

**Status:** accepted
**Date:** 2026-10-06
**Amends:** [ADR 098](./098-separate-analysis-reconciliation-from-synthesis.md) for what a verification may contain and how synthesis consumes it; [ADR 108](./108-declaring-analysts-correct-their-reports.md) for what a record-verification finding can be. Round budgets and the stop at the limit are unchanged.

## Context

A verification could only block or pass. Every unresolved finding, however
local, was a blocker, and a run whose last permitted correction left any
finding open stopped without publishing. Two October 2026 runs ended this
way: one at the third record verification on stale dependents, one at the
second profile verification on three findings the verifier raised only on
its second look. The published alternative was a run that had never raised
the issue, which the Sol/Luna audit showed is not the more correct one.
Publication status was standing in for correctness.

The operator selected a publication policy in which the deciding question
is whether a finding materially limits the analysis, not whether anything is
left unresolved: publish useful analyses with declared limits, block
misleading conclusions, and never let a disputed profile value enter
comparisons as settled. The revision-2 profile contract (ADR 107) already
lets a value express its own uncertainty, which that last requirement needs.

## Decision

Every finding a verifier does not dismiss is a **blocker** or a **limit**,
in two sections of the typed verification.

A blocker must be repaired before publication: it undermines a central
conclusion, leaves the analysis materially misleading, or is a known false
assertion with a supported correction. Blockers keep their routing and
budgets: record blockers go to the declaring analyst, profile and synthesis
blockers to their author, and blockers remaining at the last permitted
correction stop the run.

A limit is a local unresolved issue the analysis is published with. It names
the records it concerns and the conclusions readers should withhold. The
synthesizer carries every limit from the record and profile verifications,
and every unresolved conflict in the reconciliation, into the overview's
Limitations; code refuses a synthesis whose Limitations names none of a
declared limit's records, and the synthesis verifier judges that the
consequence is stated. A limit on a profile value is admissible only where
the value already expresses the uncertainty (`partial`, `not-determinable`,
`uninspected`), because an overview caveat does not travel with an extracted
value; otherwise the finding is a blocker.

Faithfully scoped uncertainty is neither. A review objection is evidence to
assess, not an established defect; the verifier, not the author, decides
which of the two a finding is.

Operativity: the verification type carries the two sections and their
meaning; the three verifier instructions consume it as their authoring
contract; the scheduler reads Blockers as before and hands the final record
and profile verifications to the synthesizer and its verifier; the
synthesis acceptance check consumes limits with binding force; the overview
shows each verification's limits beside its account.

Warrant: code establishes that each limit's records are named in
Limitations and that the two sections are well formed. Whether a finding is
local or central, and whether the stated consequence is right, remain the
verifiers' judgments, with the known possibility of missed defects and
false objections.

## Considered alternatives

**Coordinator disposition.** The proposal's wording had the coordinator decide
each finding's disposition. In a code-scheduled run the coordinator is code
and a driver session that makes no content judgments, so the decision was
placed with the verifier that found the finding. A separate disposition
step would add a role without adding evidence.

**Raise the profile and synthesis budgets.** Cheaper, and it would have let
the stopped run continue. It moves the same cliff one round out and leaves
publication status as the correctness proxy.

**Require resolution of every finding.** The prior rule. Simplest acceptance
condition; it stops useful work on local issues and never publishes a run
whose verifier keeps finding small things.

**A separate "Limitations and unresolved issues" overview section.** The
proposal suggested one; the existing Limitations section already carries
unresolved conflicts with affected IDs and prevented conclusions, so limits
join it rather than duplicate it.

**An analyst-callable verifier** for earlier correction. Rejected by the
operator in the proposal as added complexity with a false-objection problem.

## Consequences

Runs finish with limits they would previously have stopped on, and the
published overview says what is unresolved and what readers should withhold.
Comparison consumers see uncertainty in profile values, not in a caveat.
Verifiers carry a new judgment, local versus central, that the budget used to
make for them.

The policy has not been exercised by a model run. The one run that would
have benefited stopped at the profile stage; whether its three findings
would have been limits or blockers under this rule is the first thing a
rerun will show. The rule applies to new runs; retained sets predate it and
have no Limits sections in their verifications. This decision adopts the
proposal *Publishing analyses with unresolved issues*, which is archived.
