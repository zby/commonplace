---
type: types/type-spec.md
name: agentic-system-analysis-run-state
description: Minimal completion state for one rerunnable agentic-system analysis
schema: ./agentic-system-analysis-run-state.schema.yaml
---

# Agentic system analysis run state

## Authoring Instructions

Use this type only for
`kb/reports/state/agentic-system-analysis/<run-id>/run-state.md`. The owning
workflow is `kb/instructions/analyse-agentic-system/SKILL.md`.

This record proves only what later consumers need:

- which run produced the outputs;
- which frozen source boundary it used;
- which exact manifest and published review bytes completed the run; the
  manifest pins every member of the set; and
- which typed memory specialist report the set's memory member was finalized
  from.

It is not a recovery log. A run is `running`, `complete`, or `failed`. Do not
resume a failed run or preserve phase, packet, correction, validation-receipt,
or retry state. Start another run with a new run ID. Temporary candidate files
inside the run directory are disposable and never appear in this record.
The `## Run` prose records the destination inspection's expected incumbent
digest (or `absent`). Recovery copies `incumbent-review.md` and
`incumbent-<member>.md` for each replaced member are retained with the new
run when a review is replaced; they are not disposable candidate files.

The artifact manifest lives at
`kb/reports/state/agentic-system-analysis/<run-id>/output/ARTIFACT.yaml`.
Its [set type](../reports/types/agentic-system-analysis-set.md) selects
membership from the overview's disposition. The overview's `inputs-commit`
names the method commit. A complete set publishes a generated review;
a blocked or out-of-scope set has only the overview and no generated review.
Publication retains the manifest and members byte for byte under
`kb/reports/retained/agentic-system-analysis/<run-id>/`. Completion checks
those copies and the public review's `analysis-artifact` and
`analysis-artifact-sha256` against `artifact.sha256`. Comparison readers
follow those public fields without ignored state or a source checkout.

Every complete analysis requires the typed `memory-report.md` and frozen
`memory-input.md` in its run directory. The coordinator finalizes that report
as `memory.md`: proposal IDs mapped to canonical IDs by exact token, seeded
records the specialist re-declared and proposals merged into another member's
record turned into `On <ID>` annotations, rejected proposals removed, and an
`## Amendments` section appended; the member's `finalized-from` is the local
report's SHA-256. Completion verification checks the manifest, run and
boundary identity across members, the memory member's complete status and
its `finalized-from` and `canonical-register-sha256` pins against the local
files, and applies the shared set checks, including cross-member record resolution.
It also checks every member's source and quote anchors.
These checks establish identity and structure; they do not check the
derivation of the memory member or impose a quote minimum, and they do not certify the specialist's semantic judgments.

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

A `failed` run was abandoned or left public state uncertain; it is never
resumed. Git history is the history
of successfully published tracked reviews; this workflow does not stage or
commit.

## Template

```markdown
---
type: types/agentic-system-analysis-run-state.md
description: "Minimal completion state for AAS-YYYY-MM-DD-system-slug-nn"
run-id: AAS-YYYY-MM-DD-system-slug-nn
system: "Source-native system name"
run-status: running
result-disposition: null
source: null
artifact: null
generated-review: null
failure: null
---

# Agentic-system analysis run — AAS-YYYY-MM-DD-system-slug-nn

## Run

<Target and frozen source boundary once known.>

## Outcome

<Current status, completed outputs, or concise failure reason.>
```
