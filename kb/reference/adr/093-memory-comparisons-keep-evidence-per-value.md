---
description: Separate memory-axis coverage from each value's evidence so mixed-strength routes remain countable without upgrading their neighbours
type: reference/types/adr.md
status: accepted
---

# 093 — Memory comparisons keep evidence per value

**Status:** accepted
**Date:** 2026-09-26

## Context

An axis can contain an implemented automatic route and a merely afforded manual
route. Giving the whole set its weakest evidence basis correctly limits claims
about the complete profile, but loses the implemented route in membership
counts. A comparison corpus needs both questions: which mechanisms have
support, and which complete profiles can be compared.

## Decision

Adopt option 2 of “Evidence granularity for memory-comparison counts”. Each
controlled value carries its own evidence basis, canonical supporting records,
and rationale. Axis coverage remains separate. `known` means complete coverage;
`partial` preserves positive findings while naming unresolved included parts.
Absence, inapplicability, uninspected and indeterminate cases stay explicit.

A value's strongest supported witness establishes its existence within the
scope; weaker alternatives remain described in its records. It does not
establish the same strength for every route. Count a system once per question.
Implementation counts use code-grounded wired, observed or causally supported
values. Complete-profile distributions require complete coverage and that
strength for every member. Neither an omitted value nor weak evidence is an
observed negative. Route-specific questions still require the full records.

## Considered alternatives

Keeping only complete-profile statistics preserves a smaller contract but
cannot answer supported mechanism-membership questions. Keeping those
statistics alongside per-value counts preserves their useful meaning.

Narrowing every comparison boundary can isolate stronger routes, but multiplies
profiles and risks counting a source twice. Scope remains an evidential boundary,
not a means to discard inconvenient alternatives.

The chosen form uses a value list plus an evidence map whose keys must match
exactly. It preserves direct set operations while making evidence explicit.
Canonical records carry route distinctions; a second route taxonomy is not
introduced. Structural checks cannot decide whether a quoted source warrants
the authored classification.

## Consequences

Analysis coordinators and profile classifiers consume the type and producing
instructions as binding authoring rules. Schemas and validators enforce shape,
controlled values and declared references. Matrix and table emitters preserve
per-value evidence; statistics and synthesis consumers apply separate positive
and complete-profile counting rules. Per-value evidence adds authoring and validation work. Historical retained bytes are immutable;
new analyses are required for admission under the current contract.

This decision governs the declared memory boundary of one analysis. It does
not establish corpus representativeness, semantic correctness, observed benefit,
or comparability between different scopes. Partial positives support lower-bound
counts, not whole-population prevalence estimates.

The [memory profile type](../../agentic-system-analyses/types/agent-memory-profile.md#memory-comparison-fields)
owns the authoring and counting contract; at the time of this decision the
fields lived in the since-retired single-file analysis result type.

Carrier amendment, 2026-10-04: the profile classifier authors a separate pinned
`memory-profile.md` after record verification; independent profile verification
checks support before synthesis. Axis definitions, evidence bases and counting
rules remain unchanged.
