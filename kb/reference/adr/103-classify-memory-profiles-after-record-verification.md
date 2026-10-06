---
description: Separate source-native memory tracing from comparison classification, with a pinned profile member and independent verification after records close
type: reference/types/adr.md
status: accepted
---

# 103-Classify memory profiles after record verification

**Status:** accepted

**Amended 2026-10-06:** the profile loop permits two corrections, matching the record loop (commit on this date). Two runs stopped after one correction on a second-look finding of the same kind the first had named; the one-correction rule below records the prior decision.
**Date:** 2026-10-04
**Amends:** [ADR 093](./093-memory-comparisons-keep-evidence-per-value.md) for the profile carrier and author role.
**Amended by:** [ADR 107](./107-classify-memory-by-scoped-findings.md) for the profile representation and semantics. Classifier ownership, evidence boundaries and independent verification below remain in force.

## Context

Memory analysis combines source tracing with classification into ten comparison
axes. Classification adds fourteen output obligations and about 9.2 KB of type
definitions to memory, reconciliation and record verification. Profile faults
then consume memory correction and reconciliation rounds, even when the
source-native account is sound. Separating these tasks reduces what each
analyst must hold without weakening evidence or independent review.

## Decision

After reconciliation and independent record verification close without blockers,
run a profile classifier and independent profile verifier before synthesis.
Allow one profile correction. Persistent blockers stop the run before publication;
they never reopen the analysts or reconciliation.

The classifier writes `memory-profile.md` as the sixth manifest-pinned member
of a complete analysis set. It owns the unchanged `memory-comparison` mapping
and Comparison rationale under the [profile type](../../agentic-system-analyses/types/agent-memory-profile.md).
It cites existing canonical records, applying reconciliation amendments and
supersessions. It declares or annotates no records and adds no evidence.
Optional frozen-source reading resolves a named ambiguity in a record's cited
paths; it cannot substitute for a missing supporting record. Missing facts
retain warranted bounded assessments and prevented conclusions.

Memory analysis keeps the descriptive facts, records, annotations, write-side
and read-back accounts, in source-native terms. Reconciliation and record
verification check those records independently. The overview records separate
record, profile and synthesis verification. Blocked and out-of-scope sets remain
overview-only. Axis definitions, values, per-value evidence and counting rules
from ADR 093 remain unchanged.

## Considered alternatives

**Keep classification in memory analysis.** Avoids two jobs but retains the
combined task and profile-driven analyst correction rounds.

**Merge the classifier's mapping into the memory member.** Saves a file but
rewrites the analyst's accepted bytes. A separate pinned member preserves exact
provenance and ownership.

**Let the classifier declare evidence or return work to memory.** Could recover
missing facts, but creates another analyst and return loop. Two Luna replays of
retained Dynamic Cheatsheet records reproduced all twenty axes' values,
coverage and per-value strengths after one bounded correction, without source
reads. No axis weakened because a needed fact was missing. This supports keeping
the narrower classifier for now; those records were authored with the axes in
view, so future sufficiency remains untested.

## Consequences

The workflow supplies the profile type and job instructions by absolute
read-first paths as binding worker inputs, and schedules independent verification
before synthesis. Validators enforce the sixth member, identity, controlled
shape and references against canonical set declarations. Publication pins its
bytes with the record members. Matrix, landscape and taxonomy consumers read
the profile member directly; there is no legacy-location fallback. The site
publishes the current retained profile alongside its supporting records.

Memory loses fourteen output obligations; reconciliation and record verification
lose their axis checks. Mandatory input falls by about 10 KB for each. Existing
unrelated concerns and residual instruction conflicts do not fall further in
this phase. The classifier and verifier add jobs and their own contracts; this
redistributes work and does not establish better analytical outcomes. The first
separately commissioned regenerated analysis is the outcome check. Historical
sets and stopped runs remain unchanged and outside the current population.
