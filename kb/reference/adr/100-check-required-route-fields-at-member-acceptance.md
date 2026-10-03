---
description: Reject missing unconditional route answers during analyst acceptance using exact labels, while retaining semantic verification of their meaning and evidence
type: reference/types/adr.md
status: accepted
---

# 100 — Check required route fields at member acceptance

**Status:** accepted
**Date:** 2026-10-02

## Context

The shared analysis contract requires seven answers for every route, regardless
of which analyst declares it. Unstructured paragraphs can omit an answer while
passing deterministic validation. Detecting an omission only during semantic
verification spends a reconciliation round on a mechanical defect.

## Decision

Require one unindented bullet with an exact label and a non-empty same-line
answer for immediate return, later read-back, delegated visibility, selection
predicate, invalidation or expiry, activation or effect, and evidence limits.
An inapplicable or uninspected answer uses the corresponding exact value,
an em dash, and a non-empty reason. The
[shared record contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md)
owns the authoring syntax.

Check each route declaration under Shared records in every analyst member,
including all analyst prefixes. Another record, an annotation, a source
quotation or a fenced excerpt cannot satisfy the declaration's fields.
Supporting prose and evidence remain free text.

Apply the rule through local member validation, set validation and publication.
The existing worker refusal and amendment path repairs missing fields before
reconciliation. Keep semantic verification responsible for adequacy and source
support. Add no independent adequacy assay.

Retire obsolete live analysis sets and their generated reviews rather than
reformatting or reanalysing them. Historical archives and completed local run
states remain evidence of their original methods; they do not receive a
compatibility path through current publication.

## Considered alternatives

**Leave presence to model verification.** This permits flexible prose but makes
an unconditional, mechanically decidable omission consume analytical review.
The exact labels trade limited format flexibility for earlier refusal.

**Add structured tables or YAML records.** These would change the representation
read by downstream consumers without a demonstrated need beyond presence
checking. Labelled bullets preserve Markdown records and stable identifiers.

**Add an adequacy assay as well.** The existing semantic judge already checks
meaning and evidence. Another assay adds cost and variance without an
established independent benefit. This narrows the earlier operator selection
of combined presence and adequacy checks to presence plus existing verification.

**Migrate old retained analyses.** Reformatting complete answers would require
repinning evidence, while missing answers would require new inspection. The
operator judged these old sets insufficiently useful for current comparisons
to justify that work. They are retired rather than made to appear newly valid.

Component fixity, separate status vocabularies and conditional theory fields
remain outside the new check. Their existing substantive requirements remain.

## Consequences

Analyst workers receive the syntax through their declared shared-contract
input. Member validators consume the exact labels as binding shape checks;
set validation and publication reject a member with an omission. The workflow
delivers those diagnostics through its existing bounded amendment retry.
Reconciliation, semantic judges, synthesis and comparison readers continue to
consume Markdown findings and stable IDs. A test compares the validator's label
vocabulary with the delivered contract.

The rule establishes presence, uniqueness and reason syntax. It does not
establish truth, complete source coverage, valid conditional applicability or
behavioral benefit. Those remain analytical judgments. This decision adopts
the presence-check portion of *Required route fields as labelled record lines*;
its old-record migration and separate adequacy assay are declined.
