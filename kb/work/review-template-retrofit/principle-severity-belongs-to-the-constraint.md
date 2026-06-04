# Principle: severity belongs to the constraint; the schema fails by default

Distilled from `severity-belongs-in-schema.md` (the analysis + research) and its
implementation (`3bdd9661`). Candidate for promotion to a `kb/notes/` note.

## The principle

**A validation constraint's severity is a property of that constraint, authored
with it and keyed to a stable identifier — and the schema fails by default.**

Two claims, one corollary:

1. **Severity is per-constraint author knowledge, not a property of where the error
   lands.** Whether breaking a rule should block depends on what the rule *means*,
   which its author knows when writing it. Inferring severity from the error's
   *location* (field path, JSON Pointer) is a lossy proxy: many distinct constraints
   report at the same path and collide, so per-constraint severity becomes
   inexpressible. Author severity *on the constraint*, keyed to a stable rule ID so it
   can be re-leveled, referenced, or overridden without touching the matching logic.

2. **A schema is a contract, so violating it fails by default.** The default severity
   is FAIL; a constraint opts *down* to a warning explicitly. Softness is the marked
   case, not the unmarked one — an author who wants a nudge says so.

   *Corollary:* this only stays cheap if the corpus is kept clean. Fail-by-default
   has zero blast radius precisely because existing artifacts already conform; it
   bites *future* violations, which is the point. Audit before flipping the default —
   the cost of (2) is measured, not assumed.

## Why (the convergent evidence)

Surveyed JSON Schema/ajv, Spectral, vacuum, Redocly, ESLint, SARIF, Schematron
(25/25 claims verified against primary docs). The universal invariant is **severity
keyed to a stable rule identifier, separate from matching logic** — whether the value
sits inline (Spectral, Schematron) or in an external config layer (ESLint, SARIF,
Redocly) is secondary. Raw JSON Schema has *no* native severity; a bare inline
severity with no stable ID and no override path is the one shape no ecosystem relies
on. So this is adopting a standard, not inventing one.

## How it landed here

`_FAIL_PATHS` (severity keyed on instance path, collided on `("body",)`) → replaced
by `_DEFAULT_SCHEMA_SEVERITY = "fail"` plus a `severity: warn` opt-down read off
`error.schema`, keyed by an optional stable `ruleId`. The corpus audit found 3
schema-derived warnings total (all one index `minItems` rule), so the default flip
broke nothing; that constraint was removed rather than softened. See
`severity-belongs-in-schema.md` for the full reasoning and the deferred follow-ons
(external override map; folding hand-coded checks into the same model).

## Transfer test

The claim generalizes beyond this validator: any rule-based checker (linter,
schema validator, policy engine) that centralizes severity away from the rule, or
infers it from error location, will hit the same collision and blast-radius problems.
The fix is the same — severity on the identified rule, fail by default.
