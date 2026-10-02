---
description: Verify reconciled analysis records before independently authoring and checking the public synthesis
type: reference/types/adr.md
status: accepted
---

# 098 — Separate analysis reconciliation from synthesis

**Status:** accepted
**Date:** 2026-10-01

## Context

Record repair and public writing have different dependencies. A public author
needs settled records; a reconciliation author must still resolve disagreement
and may return findings to the memory analyst. Combining these tasks writes
public text before the records that support it have passed independent review.
In one local Instinctual Memory run, reconciliation grew from 3,314 to 6,406
bytes across three rounds while synthesis stayed between 4,695 and 4,775 bytes.
That observation motivates the split; it does not establish its frequency or
net cost.

## Decision

Reconciliation is a separate retained member. It authors amendments,
supersessions and explicitly marked unresolved conflicts. An independent
record judge checks the three analyst members and reconciliation before a
separate author writes the public synthesis. A second independent judge checks
that synthesis against its supporting records. The overview remains the entry
point, with a code-written index of amended records and both judgments.

Keep the record loop's two correction rounds and the memory return route.
Allow one synthesis correction. A record fault found during synthesis checking
is a limitation; if it cannot be stated faithfully without making the synthesis
misleading, stop rather than reopen reconciliation.

The synthesis author and judge load the overview type plus the shared source
and record contracts. Reconciliation and record verification load the analyst
and reconciliation types. Synthesis reads the reports as evidence without
loading their authoring contracts.

## Considered alternatives

**Keep reconciliation in the overview.** Delaying synthesis could preserve four
members, but would keep a type shared by two authors and require a provisional
overview or an extraction boundary. A separate member gives reconciliation one
output contract and permits direct record checks.

**Reopen records from synthesis checking.** This permits deeper repair, but
makes the correction budget and the meaning of settled records harder to
follow. Bounded limitations or stopping preserve the phase boundary.

**Append verification to reconciliation.** Readers would find amendments and
their judgment together. It gives that member two author roles and makes the
overview's completion account less direct. Keep both judgments at the entry
point.

The unresolved-conflict marker and separate record check are execution choices.
Cited-record extracts and removing overlap between reconciliation and its
judge are deferred until trial evidence supports another change.

## Consequences

Record corrections no longer rewrite public text. A complete set has five
members, and every synthesis is checked independently. Extra synthesis and
verification jobs cost calls even when records need no correction. Separating
contracts reduces what public-writing workers must load, while retaining the
whole reports as evidence.

The workflow consumes judge blockers as scheduling authority. Validators and
publication consume the five-member contract and amendment index with binding
force. Analysis workers consume their role-specific contracts as authoring
instructions. Review rendering, handoff and comparison loaders consume the
accepted members and manifest; transfer and landscape workers resolve amended
records through reconciliation. Published reviews remain projections of the
overview.

This decision applies to new frozen-source analysis runs. Structural checks
establish shape, identity and reference resolution; both semantic judgments
remain model assessments, not an independent experimental oracle. Tests cover
both bounded loops and failure before publication. Both fresh Luna trials stopped at final record verification, before synthesis,
on source-traceability judgments, an altered quotation and lost reconciliation
markers. They exercise the bounded stop path; they do not test the synthesis
contract selection or establish reduced total work. Subsequent Sol medium
runs reached verified synthesis, and one published on 2026-10-01. Separate
Luna medium and Sol medium runs both published on 2026-10-02. These establish
the bounded publication path, without a matched estimate of reduced work or
improved analytical quality.

This ADR adopts the design proposal *Separate analysis reconciliation from
synthesis* and amends ADR 096's reconciliation location and public-writing role.
