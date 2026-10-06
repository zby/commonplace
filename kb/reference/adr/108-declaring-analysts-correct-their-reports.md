---
description: "Record-verifier blockers go to the declaring analyst, who writes a corrected report; reconciliation states relations between reports and no longer replaces values or returns findings"
type: reference/types/adr.md
status: accepted
---

# 108 — Declaring analysts correct their reports

**Status:** accepted
**Date:** 2026-10-05
**Amends:** [ADR 096](./096-analysis-passes-declare-their-own-records-under-lens-prefixes.md) for the rule that analyst members are not rewritten, and [ADR 098](./098-separate-analysis-reconciliation-from-synthesis.md) for who corrects records and the memory return route. Lens-prefixed identities, declaration ownership, the separate reconciliation member and the three independent checks remain in force.

## Context

Folding three analyst reports into one account produces three kinds of
statement. A connection relates records in different reports, and no single
report owns it. A correction changes a claim one report made, and that
report also holds the fields, ledger rows and conclusions that depend on the
claim. A standing disagreement is one the evidence cannot settle.

Writing corrections in the reconciliation member made it an overlay. The
report kept the superseded text, and the verifier, the profile and synthesis
jobs and readers of the published set each had to apply the correction and
work out what else it affected. Two of the three runs that entered the record
loop on the method of ADR 107 stopped at the third verification for this
reason: each verification found report text that still asserted a value an
amendment had replaced. Neither run used the memory return, the one path on
which a declaring analyst could revise its own text.

The reconciler also judged single reports and corrected what it judged
faulty, before an independent verifier judged the same records again. The
verifier could not correct; its blockers could only start another
reconciliation.

## Decision

Each role has one function. The reconciler connects, the record verifier
judges, and the declaring analyst corrects.

A record-verification blocker names the one report whose text must change:
`runtime`, `memory`, `epistemic` or `reconciliation`. Code reads that word to
schedule work and refuses a blocker without it. For each analyst report
named, code runs that analyst again with its previous report and the
verification. The analyst returns a complete report and one answer per
blocker addressed to it: a correction, or a reason for declining. A runtime
correction finishes before memory and epistemic corrections start, because
both read the runtime report; they then read the corrected version. A new
reconciliation and verification follow each correction step. The loop keeps
three verifications, and blockers at the third stop the run.

Every version of a report stays in the run directory. Later jobs and
publication receive one current version of each report; the published set
carries no predecessor. A corrected report keeps every record ID its
predecessor declared.

Reconciliation states identity between declared records, including
supersessions in the existing `Amendment: <ID> is superseded by <IDs>` form,
and describes disagreements between reports as unresolved conflicts for the
verifier. It does not replace a record's value, judge one report's support
or return findings to an analyst.

Operativity: the workflow consumes blocker addressees as scheduling
authority. Analyst, reconciliation and verification jobs consume their
revised instructions as authoring contracts. Acceptance checks consume the
answer count, the retained record IDs and the supersession form with binding
force. Profile, synthesis and publication consume the current reports as
authoritative text.

Warrant: deterministic checks establish that each addressed blocker has an
answer, that declared IDs survive, that an answer claiming a correction comes
with changed text, and which versions were verified together. A
code-computed text difference shows the verifier which lines changed. None of
these establishes that a correction is right or that unchanged dependent
text is still supported; that remains the verifier's model-dependent
judgment.

## Considered alternatives

**Keep amendment overlays with stronger instructions.** No report is
rewritten and no job is added. Every consumer still applies corrections and
finds their dependents by reading, which is where the stopped runs failed.

**Let the reconciler write corrected reports.** One job could correct several
reports together without using a round. It gives a worker authority over
findings it did not declare and does not re-derive them from the sources. It
remains available if analyst jobs prove too costly for small corrections.

**Let the reconciler also request corrections.** Cross-report disagreements
would be repaired a verification earlier. It adds a second request authority
and a second correction cycle; the verifier reads the described conflict and
addresses it.

**Mark changes inside reports with tracked-change notation.** It would add a
notation with its own escaping and checking rules for information that
record IDs and a computed difference already give.

**Produce corrected reports only at publication.** Public readers would get
coherent text, but the record loop would still verify against an overlay.

**Declare dependencies between findings so code routes dependents.** This
would remove the reading step that finds stale dependents. It was left out so
that a trial can attribute its outcome to report correction alone.

## Consequences

Consumers read reports as written, and the rule to judge records as amended
is gone. A correction cycle costs one job per addressed analyst plus a
reconciliation and a verification. A dependent passage that neither the
verifier nor the analyst notices waits for the next verification, and the
third verification still ends the run.

A defect the reconciler would have caught before verification now waits for
the verifier. A record cannot be removed by a correction; a wrong record
keeps its declaration and states the corrected finding.

Sets published before this decision can carry value amendments in their
reconciliation member, and their readers still resolve those. The acceptance
rules apply to new runs only.

The decision rests on two stopped runs and scripted workflow tests. It has
not been exercised by a model run. Whether three verifications suffice, how
often analysts decline, and whether reconcilers stay within the narrower
role are open until a trial. The publication policy for unresolved issues is
a separate decision and may change what happens to blockers at the limit.
