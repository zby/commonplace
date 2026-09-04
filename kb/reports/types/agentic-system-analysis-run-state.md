---
type: kb/types/type-spec.md
name: agentic-system-analysis-run-state
description: Minimal completion state for one rerunnable agentic-system analysis
schema: kb/reports/types/agentic-system-analysis-run-state.schema.yaml
---

# Agentic system analysis run state

## Authoring Instructions

Use this type only for
`kb/reports/state/agentic-system-analysis/<run-id>/run-state.md`. The owning
workflow is `kb/instructions/analyse-agentic-system/SKILL.md`.

This record proves only what later consumers need:

- which run produced the outputs;
- which frozen source boundary it used; and
- which exact result and published review bytes completed the run.

It is not a recovery log. A run is `running`, `complete`, or `failed`. Do not
resume a failed run or preserve phase, packet, correction, validation-receipt,
or retry state. Start another run with a new run ID. Temporary candidate files
inside the run directory are disposable and never appear in this record.

The exact result always lives at
`kb/reports/state/agentic-system-analysis/<run-id>/result.md`. A substantive
`complete` result also publishes one generated review under
`kb/agentic-systems/`. A blocked or out-of-scope result has no generated
review. Set `memory-review-required: true` only when the target is itself a
memory, knowledge, or context-engineering system; that requires one published
legacy review.

`source` is either a Git commit or an immutable capture. A Git source records
the stable repository identity, full commit ID, and absolute checkout path. A
capture records its stable identity, version or capture label, absolute file
path, and SHA-256. The validator checks the commit or capture while the run
state exists.

Each output mapping contains a normalized repository-relative `kb/` path and
the SHA-256 of its current bytes. `commonplace-validate` must pass directly on
each output before it is recorded. The run-state validator rechecks byte and
workflow identity; it does not retain a validation receipt.

A publication candidate is validated before it replaces a same-source
generated review. A failed candidate leaves the incumbent unchanged, sets the
run to `failed`, and is handled by a later rerun. Git history is the history of
successfully published tracked reviews; this workflow does not stage or commit.

## Template

```markdown
---
type: kb/reports/types/agentic-system-analysis-run-state.md
description: "Minimal completion state for AAS-YYYY-MM-DD-system-slug-nn"
run-id: AAS-YYYY-MM-DD-system-slug-nn
system: "Source-native system name"
run-status: running
result-disposition: null
source: null
result: null
generated-review: null
memory-review-required: null
legacy-review: null
failure: null
---

# Agentic-system analysis run — AAS-YYYY-MM-DD-system-slug-nn

## Run

<Target and frozen source boundary once known.>

## Outcome

<Current status, completed outputs, or concise failure reason.>
```
