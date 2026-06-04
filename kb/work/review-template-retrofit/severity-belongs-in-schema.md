# Analysis: should the schema define FAIL vs WARNING?
Scratch analysis prompted by the Phase 0 finding that an un-retrofitted review reports `Overall: PASS (N warnings)` even though it violates the new layout. The question: where should the FAIL/WARN line live? Updated after researching how established validation ecosystems solve this — so we adopt the standard pattern rather than invent one.
## How severity is decided today
`src/commonplace/lib/validation.py`:

```python
_FAIL_PATHS = frozenset({
    ("frontmatter", "description"),
    ("frontmatter", "tags"),
    ("frontmatter", "type"),
})
...
severity = "fail" if effective_path in _FAIL_PATHS else "warn"
```

Severity is keyed on the **instance path where the error landed** (`error.absolute_path`), hardcoded in validator code. Three frontmatter fields fail; everything else — every body pattern, every required heading — warns. `Overall` is FAIL iff there is ≥1 fail (`validate_notes.py:153`).
## Why path-keying is the wrong axis
1. **Path collisions erase the distinction.** Every body constraint in the review schema reports at the same path `("body",)`: the `**Write agency:**` requirement, the `mixed` representational-form ban, the dead `**Read-back timing:**` token, the old-heading ban. `_FAIL_PATHS` literally _cannot_ tell them apart — they share one key. Same for the five `## ...` heading `contains` checks, all at `("headings",)`. So "make the missing Write-agency verdict a FAIL" is not expressible in the current model at all, regardless of how we edit `_FAIL_PATHS`.
  
2. **Blast radius.** `_FAIL_PATHS` is global across every note type. Promoting a path to fail flips severity for that path in _all_ schemas at once. Local intent, global effect.
  
3. **Severity is per-constraint author knowledge.** Whether a violated rule should block depends on what the rule _means_ — which the schema author knows when they write the constraint. The validator re-deriving it from a field-location proxy is lossy by construction. This is the core of the user's intuition, and it's right.
  
## What the established ecosystems actually do (research)
Surveyed JSON Schema/ajv, Spectral, vacuum, Redocly, ESLint, SARIF, and Schematron. 25/25 claims verified 3-0 against primary vendor/standard docs. The convergent pattern is narrower and more specific than "put severity in the schema":

> **Severity is keyed to a stable rule identifier, separate from the rule's matching logic.** Whether the severity value sits inline or in an external file is a secondary, ecosystem-by-ecosystem choice — but a _stable ID for the rule_ is universal.

- **JSON Schema: no native severity at all.** ajv's criticality-levels request (issue #766) was closed wontfix; `ajv-errors` only customizes message _text_, no error/warn/info. A pure inline severity with no rule ID and no override layer is the one shape **no** surveyed ecosystem relies on.
  
- **ESLint — fully external.** `off|warn|error` lives in config keyed by rule ID; rule code _cannot read or modify its own severity_ ("the error level cannot be known or modified from inside a rule"). A proposal to let one rule emit both warn and error (#11089) was never adopted — one severity per rule entry.
  
- **SARIF — external baseline + per-result override, both keyed by** `ruleId`**.** A rule (`reportingDescriptor`) carries `defaultConfiguration.level`; each result's `level` (`error|warning|note|none`) defaults from it and `configurationOverrides` can re-level at runtime — all tied to the stable `ruleId`.
  
- **Redocly — fully external.** `operation-operationId: warn` in `redocly.yaml`: rule ID as key, severity as value.
  
- **Spectral / vacuum — hybrid (inline default, external override).** A `severity:` sits _inline_ inside a named kebab-case rule block, but an extending ruleset can override it by the same rule name. vacuum explicitly added an `id` field "to allow… the freedom to rename" — i.e. stable identity is the load-bearing part.
  
- **Schematron — inline on an identified rule.** `assert`/`report` carry an inline `role` (severity, conventionally `error`/`warning`, free-text) plus an `id`.
  

Takeaway for us: inline severity is _not_ the mistake (Spectral and Schematron author it inline). The mistake my first proposal made is omitting the part every ecosystem shares — **a stable per-constraint rule ID** that severity attaches to and that lets a constraint be renamed or re-leveled without touching its matching logic. A raw JSON Schema subschema has no such ID; that absence is the real gap.
## Revised proposal: give each constraint a stable rule ID, then attach severity
Two coupled changes, mirroring the Spectral/Schematron hybrid (the closest fit for a small single-validator KB — full ESLint/SARIF externalization is more machinery than we need yet):

1. **Stable rule ID per constraint.** Add an explicit `ruleId` (e.g. `review-write-agency-required`) to each constraint subschema we want to govern. `error.schema` already gives the validator the failing leaf subschema, so the ID is readable with no extra plumbing. Don't key off JSON Pointer / `absolute_path` — that's the path-collision trap again and it's refactor-fragile.
  
2. **Severity attached to that ID.** Author a default `severity: fail | warn` inline on the same subschema (Spectral-style), read off `error.schema`, default `warn`:
  

```yaml
- ruleId: review-write-agency-required
  severity: fail            # missing verdict blocks
  properties:
    body:
      pattern: "\\*\\*Write agency:\\*\\*"
- ruleId: review-legacy-trace-heading-absent
  severity: warn            # legacy heading only warns
  properties:
    body:
      not:
        pattern: "## Trace-derived learning placement"
```

```python
schema = error.schema if isinstance(error.schema, dict) else None
severity = "warn"
if isinstance(schema, dict) and schema.get("severity") in ("fail", "warn"):
    severity = schema["severity"]
# rule_id = schema.get("ruleId") if isinstance(schema, dict) else None  → surface in message
```

`ruleId`/`severity` are unknown keywords → JSON Schema 2020-12 ignores them for validation, so they're inert and survive into `error.schema`. Each `allOf` branch is its own subschema, so granularity is per-constraint — exactly what the colliding `("body",)` cases need.

**Why the ID, concretely (YAGNI-aware):** we don't need an external override file _today_, so we don't build one (YAGNI). But authoring the `ruleId` now is nearly free and is the one thing the research says you regret omitting — it keeps the door open to (a) a per-collection severity override map later, (b) stable references in messages and acks, and (c) renaming a constraint without breaking either. Inline-default-only without an ID is the precise anti-pattern flagged.

Naming note: prefer `severity` over my earlier `x-severity` — it's the term Spectral, vacuum, and SARIF (`level`) converged on; the `x-` prefix buys nothing here since the keyword is already non-standard and inert.
## The remaining policy decision: what is the default?
The mechanism is settled by the research; this is the substance left to choose.

- **(A) Default warn, annotate fails.** Replaces `_FAIL_PATHS` with `severity: fail` on the frontmatter required block (+ its `ruleId`). Severity becomes fully schema-driven, the hardcoded set disappears. Smallest behavior change.
  
- **(B) Default fail, annotate warns (invert).** "Violating the schema fails unless marked soft." Most principled — a schema _is_ the spec — but flips today's warnings to failures across every type and needs a constraint audit first. Bigger, riskier.
  

(A) is the recommended next step; (B) a possible end state once constraints are audited.
## Wrinkles
- `required` **granularity.** `required` errors report at the parent object with the field name in the message, so `error.schema` is the whole object — one `severity` / `ruleId` covers all its required fields uniformly. Fine for the frontmatter case (all three fail together); per-field severity would need the fields split into separate subschemas.
  
- **No propagation.** Read severity/ID only from the failing leaf `error.schema`; don't inherit from enclosing `allOf`/`if-then`. Matches how `description`/`title` are already read and keeps the rule obvious: annotate the clause that should bite.
  
- **Unannotated constraints.** Default `warn`, and (optionally) `log`/surface that a fired constraint had no `ruleId` so coverage gaps are visible rather than silent.
  
## Recommendation
1. Adopt the **stable-**`ruleId` **+ inline-**`severity` model in `_schema_error_message` (default `warn`), and delete `_FAIL_PATHS`. This matches the Spectral/Schematron convergent pattern; it is not a bespoke invention.
  
2. Annotate the three frontmatter required fields `severity: fail` (policy A) and the `**Write agency:**` constraint `severity: fail` — the latter is the retrofit done-condition plan.md wanted but declared unreachable. Zero blast radius on other types.
  
3. Defer the external override layer and fail-by-default (B) until a second consumer needs them (YAGNI) — the `ruleId`s make both cheap to add later.
  
4. If this generalizes beyond the review schema, promote the principle ("severity is keyed to a stable rule ID, authored with the constraint") to a `kb/notes/` note.
