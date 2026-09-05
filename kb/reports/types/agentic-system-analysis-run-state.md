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
- which frozen source boundary it used;
- which exact result and published review bytes completed the run; and
- which typed memory specialist report the exact result integrated.

It is not a recovery log. A run is `running`, `complete`, or `failed`. Do not
resume a failed run or preserve phase, packet, correction, validation-receipt,
or retry state. Start another run with a new run ID. Temporary candidate files
inside the run directory are disposable and never appear in this record.
Keep the destination inspection's expected incumbent digest (or `absent`) in
`## Run` prose. Publication requires it again at prepare and publish. Recovery
copies `incumbent-review.md` and `incumbent-result.md` are retained with the new
run when a review is replaced; they are not disposable candidate files.

The exact result always lives at
`kb/reports/state/agentic-system-analysis/<run-id>/result.md`. A substantive
`complete` result also publishes one generated review under
`kb/agentic-systems/reviews/`. A blocked or out-of-scope result has no
generated review. Publication also retains the exact result bytes at
`kb/reports/retained/agentic-system-analysis/<run-id>/result.md`. Its identity is
derived from the run ID and the existing `result.sha256`; no duplicate output
mapping is needed. Completion verification checks this copy and the public
review's `analysis-result` path and `analysis-result-sha256`. Durable comparison
readers follow those public fields without requiring ignored run state or a
local source checkout. Every substantive complete analysis requires the typed
`memory-report.md` and frozen `memory-input.md` in its run directory. The exact
result names the report and its SHA-256 in Run identity. Completion checks the
report's run, source, reviewed boundary, complete status, and input hash, and
validates its type and source anchors. These checks establish identity and
structure; they do not certify the specialist's semantic judgments.

`source` is either a Git commit or an immutable capture. A Git source records
the stable repository identity, full commit ID, and absolute checkout path. A
capture records its stable identity, version or capture label, absolute file
path, and SHA-256. The validator checks the commit or capture while the run
state exists.

For a Git source, replace `source: null` with this mapping, substituting the
repository identity, full commit and absolute checkout path:

```yaml
source:
  kind: git
  identity: https://github.com/owner/repository
  revision: "0123456789abcdef0123456789abcdef01234567"
  path: /absolute/path/to/checkout
  sha256: null
```

Use `path`, not `root`. Git sources require `sha256: null`; immutable captures
use their content digest instead. Validate the running state again immediately
after setting the source, before source analysis or delegation.

Each output mapping contains a normalized repository-relative `kb/` path and
the SHA-256 of its current bytes. Validate candidate bytes as their intended
destination before publication. The run-state validator rechecks byte,
workflow, and specialist handoff identity; it does not retain a
validation receipt.

A publication candidate is validated before it replaces a same-source review.
A correctable failure before publication leaves the incumbent unchanged and
the run `running`. Mark a run `failed` only when abandoning it or when a
publication failure leaves public state uncertain. Git history is the history
of successfully published tracked reviews; this workflow does not stage or
commit.

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
failure: null
---

# Agentic-system analysis run — AAS-YYYY-MM-DD-system-slug-nn

## Run

<Target and frozen source boundary once known.>

## Outcome

<Current status, completed outputs, or concise failure reason.>
```
