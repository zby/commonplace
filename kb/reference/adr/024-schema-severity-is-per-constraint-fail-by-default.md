---
description: "Moves schema finding severity from instance-path inference to each constraint, failing by default with explicit warn opt-downs and optional stable rule identifiers"
type: ../types/adr.md
tags: []
status: accepted
---

# 024-Schema severity is per-constraint, fail by default

**Status:** accepted
**Date:** 2026-06-04

## Context

The validator decided schema-violation severity from the **instance path** where the error landed: a hardcoded set of frontmatter paths failed; everything else — every body pattern, every required heading — warned. Two problems:

- **Path collisions make per-constraint severity inexpressible.** Many distinct constraints report at the same path. Every body rule in the review schema lands at `("body",)` — the `**Write agency:**` requirement, the `mixed`-form ban, the dead `**Read-back timing:**` ban — and all heading `contains` checks land at `("headings",)`. A path set cannot tell them apart, so "make *this* rule fail" is unrepresentable regardless of how the set is edited.
- **It is operationally misleading.** A review missing required structure (no `## Write-side placement`, missing `source-tier`, a legacy `mixed` value) still reported `Overall: PASS (N warnings)`, even though the spec says required sections are enforced. A clean `PASS` did not mean conformance.

Severity is really **per-constraint author knowledge**: whether breaking a rule should block depends on what the rule *means*, which its author knows when writing it. Inferring it from error location is a lossy proxy. A survey of rule-based checkers (JSON Schema/ajv, Spectral, vacuum, Redocly, ESLint, SARIF, Schematron) converges on one invariant — **severity keyed to a stable rule identifier, separate from matching logic** — whether inline or in an external config layer. Raw JSON Schema has no native severity, so adding one is adopting a standard, not inventing one.

## Decision

**A constraint's severity is authored on the constraint, and the schema fails by default.**

- Default schema-violation severity is **`fail`**; a constraint opts *down* to `warn` explicitly with a `severity: warn` annotation on the constraint. Softness is the marked case.
- The opt-down is keyed by an optional stable `ruleId` on the constraint, so a rule can be re-levelled, referenced, or overridden without touching the matching logic.
- Instance-path severity is removed.

## Consequences

- All note types now **hard-fail** schema violations unless the constraint marks itself `warn`. A clean `Overall: PASS` again means structural conformance.
- **Zero blast radius on flip.** The corpus audit found 3 schema-derived warnings total, so fail-by-default broke nothing existing — it bites *future* violations, which is the point. Fail-by-default stays cheap only while the corpus is kept clean; audit before flipping, don't assume.
- The required-section / token contract for `agent-memory-system-review` is now genuinely enforced, not advisory.
- **Deferred follow-ons:** an external override map for severity, and folding the hand-coded (non-schema) checks into the same per-rule severity model.
- The principle generalises: any rule-based checker that centralises severity away from the rule, or infers it from error location, hits the same collision and blast-radius problems; the fix is severity on the identified rule, fail by default.
