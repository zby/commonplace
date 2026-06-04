---
description: Schema-violation severity is a property of the constraint (read off error.schema, keyed by an optional stable ruleId), and the schema fails by default — a constraint opts down to a warning explicitly; replaces the instance-path _FAIL_PATHS proxy that collided on shared paths and under-enforced required structure
type: ../types/adr.md
tags: []
status: accepted
---

# 024-Schema severity is per-constraint, fail by default

**Status:** accepted
**Date:** 2026-06-04

## Context

The validator (`commonplace.lib.validation`) decided schema-violation severity from the **instance path** where the error landed: a hardcoded `_FAIL_PATHS` set (`("frontmatter","description"|"tags"|"type")`) failed; everything else — every body pattern, every required heading — warned. Two problems:

- **Path collisions make per-constraint severity inexpressible.** Many distinct constraints report at the same path. Every body rule in the review schema lands at `("body",)` — the `**Write agency:**` requirement, the `mixed`-form ban, the dead `**Read-back timing:**` ban — and all heading `contains` checks land at `("headings",)`. `_FAIL_PATHS` cannot tell them apart, so "make *this* rule fail" is unrepresentable regardless of how the set is edited.
- **It is operationally misleading.** A review missing required structure (no `## Write-side placement`, missing `source-tier`, a legacy `mixed` value) still reported `Overall: PASS (N warnings)`, even though the spec says required sections are enforced. A clean `PASS` did not mean conformance.

Severity is really **per-constraint author knowledge**: whether breaking a rule should block depends on what the rule *means*, which its author knows when writing it. Inferring it from error location is a lossy proxy. A survey of rule-based checkers (JSON Schema/ajv, Spectral, vacuum, Redocly, ESLint, SARIF, Schematron) converges on one invariant — **severity keyed to a stable rule identifier, separate from matching logic** — whether inline or in an external config layer. Raw JSON Schema has no native severity, so adding one is adopting a standard, not inventing one.

## Decision

**A constraint's severity is authored on the constraint, and the schema fails by default.**

- Default schema-violation severity is **`fail`**; a constraint opts *down* to `warn` explicitly (`_DEFAULT_SCHEMA_SEVERITY = "fail"`, with a `severity: warn` annotation read off `error.schema`). Softness is the marked case.
- The opt-down is keyed by an optional stable `ruleId` on the constraint, so a rule can be re-levelled, referenced, or overridden without touching the matching logic.
- `_FAIL_PATHS` (instance-path severity) is removed.

## Consequences

- All note types now **hard-fail** schema violations unless the constraint marks itself `warn`. A clean `Overall: PASS` again means structural conformance.
- **Zero blast radius on flip.** The corpus audit found 3 schema-derived warnings total (one index `minItems` rule), so fail-by-default broke nothing existing — it bites *future* violations, which is the point. The one rule was removed rather than softened. Fail-by-default stays cheap only while the corpus is kept clean; audit before flipping, don't assume.
- The required-section / token contract for `agent-memory-system-review` (write-side placement, `**Read-back:**` verdict, `source-tier`, no legacy `mixed`) is now genuinely enforced, not advisory.
- **Deferred follow-ons:** an external override map for severity, and folding the hand-coded (non-schema) checks into the same per-rule severity model.
- The principle generalises: any rule-based checker that centralises severity away from the rule, or infers it from error location, hits the same collision and blast-radius problems; the fix is severity on the identified rule, fail by default.
