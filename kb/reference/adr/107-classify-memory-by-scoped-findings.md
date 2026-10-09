---
description: "Keep memory classifications and uncertainty on their natural units, deriving comparison unions without reclassifying immutable historical profiles"
type: reference/types/adr.md
status: accepted
---

# 107-Classify memory by scoped findings

**Status:** accepted
**Date:** 2026-10-05
**Amends:** [ADR 093](./093-memory-comparisons-keep-evidence-per-value.md) for classification representation and complete-profile counting, and [ADR 103](./103-classify-memory-profiles-after-record-verification.md) for the profile contract revision, not classifier ownership or scheduling.

## Context

A supported memory mechanism can coexist with opaque initialization or another
unclassified part. A system-wide value list hides which parts were classified
and makes complete coverage easy to assert from one positive witness. Keeping
only unresolved outcomes instead loses the supported mechanism. Comparisons
need both the existence finding and the boundary it does not resolve.

Admission control also differs from content authorship and physical I/O. Calling
an API does not establish a human decision about the content admitted. A
comparison of human versus automatic control needs that distinction explicitly.

## Decision

New profiles use revision 2 of the
[memory profile contract](../../agentic-system-analyses/types/agentic-system-memory-profile.md).
Classify natural units: objects and derivation paths, transformations, admission
mechanisms, original inputs, and actual consumers or selectors, as appropriate
to each axis. Each finding carries its value, evidence basis, canonical records
and rationale once. Units retain their own coverage and missing facts. Axis
coverage requires a warranted inventory; a positive witness establishes existence,
not exhaustive enumeration. Faithful uncertainty is publishable. Unsupported
values, completeness or absence claims and hidden included parts remain defects.

`write_agency` measures per-write admission control. Manual admission requires
an explicit human decision supplying, editing, approving or replacing the
retained content. Software/model admission without that decision is automatic.
Generic callers remain unresolved unless their control is established. Reads
alone establish no write. This metric does not classify authorship or the force
of retained content at its consumer.

Derive system-level unions from findings. Strong existence evidence on one
finding does not upgrade another finding of the same value. Complete-profile
statistics require resolved coverage and strong evidence for every finding.
Bounded absence, inapplicability and unresolved classification remain distinct.
A local trace-learning negative does not negate a qualifying alternative.

Keep immutable unversioned profiles readable as revision 1 without changing
their bytes or semantics. New scheduled profiles require revision 2. Carry
revision identity into comparisons and separate statistics by revision rather
than silently pooling changed semantics. The source-first records,
reconciliation, profile classifier and independent verifier retain their
roles under ADR 103; profiles supply no new source evidence.

## Considered alternatives

**Retain the aggregate value list and evidence map.** It supports direct set
operations but duplicates authored facts and leaves local unknowns in prose.
Deriving those views from scoped findings preserves comparison operations
without a second authored classification.

**Use write-route lists for every axis.** Admission routes fit write agency,
but stores, forms, derivation paths and consumer effects describe different
units. A universal route shape would force unrelated properties together.

**Require complete classification before publication.** It avoids partial
comparisons but discards supported findings whenever another included part is
opaque. Explicit limitations are preferable to manufactured completeness.

**Rewrite historical profiles into the new shape.** Their evidence may not
establish the new metric, and their bytes are frozen. A bounded revision-aware
reader preserves historical interpretation; refresh requires a new analysis.

## Consequences

Profile authors and independent verifiers consume the type and shared record
contract through declared workflow packets. Runtime validators check shape,
references and incompatible coverage combinations. New-job acceptance enforces
the current revision while retained-set readers permit the historical one.
Matrix emitters retain unit evidence and limitations; statistics and public
comparison instructions distinguish partial positives, complete profiles and
contract revisions. Independent semantic verification still judges source
support and inventory coverage; deterministic checks do not classify prose.

This decision applies to the declared memory boundary of one analysis. It does
not establish improved model reliability, successful learning or improvement,
corpus representativeness, or comparability across unlike boundaries. Synthetic
acceptance cases establish expressibility and enforcement of selected structural
invariants, not better outcomes in a fresh external analysis run.
