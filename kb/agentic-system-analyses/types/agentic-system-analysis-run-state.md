---
type: types/type-spec.md
name: agentic-system-analysis-run-state
description: Minimal completion state for one rerunnable agentic-system analysis
schema: ./agentic-system-analysis-run-state.schema.yaml
---

# Agentic system analysis run state

## Authoring Instructions

Use this type only for
`kb/agentic-system-analyses/state/<run-id>/run-state.md`. The owning
workflow is `kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md`.

This record proves only what later consumers need:

- which run produced the outputs;
- which frozen source boundary it used;
- the last recorded workflow outcome; and
- which exact manifest and published review bytes completed the run; the
  manifest pins every member of the set.

It is not a recovery log. `run-status` reports the last completed workflow step:
`running` while jobs are pending, `blocked` when repair is permitted,
`stopped` when the workflow permits only stopping, and `uncertain` when an
effect's completion is unknown. The workflow block or effect record gives
the repair detail. `complete` means the run finished; `failed` means it was
abandoned or left public state uncertain. A coordinator's `report stop` is an
observation, not a status transition. Do not resume a failed run or preserve
phase, packet, correction, validation-receipt, or retry state. Start another
run with a new run ID. Temporary candidate files inside the run directory
are disposable and never appear in this record.
The `## Run` prose records the destination inspection's expected incumbent
digest (or `absent`). The accepted manifest lives at
`kb/agentic-system-analyses/state/<run-id>/output/ARTIFACT.yaml`.
Its [set type](./agentic-system-analysis-set.md) selects membership from the
overview's disposition. The overview's `inputs-commit` names the method commit.
A complete set publishes its accepted overview; a blocked or out-of-scope set
has only its working overview and no public output. The `generated-review`
output identity records the published overview's path and SHA-256; it does not
name a separate projection.

Publication preserves the manifest and members unchanged under
`kb/agentic-system-analyses/retained/<system-slug>/`. Completion checks those
copies against the accepted working set. When replaced, the incumbent set moves
unchanged to `retained-archive/<its-run-id>/`; its producing run's public-output
pin is historical after replacement. Comparison readers enumerate current sets
directly, validate each manifest and every member, and need no run state.

The set's `memory.md` is the memory analyst's last accepted report, unchanged.
Its separately accepted `memory-profile.md` classifies the verified records and
is pinned in the same manifest.
Completion verification checks the manifest, run and boundary identity
across members, the memory member's complete status and source identity,
and applies the shared set checks, including cross-member record
resolution.
It also checks every member's source and quote anchors.
These checks establish identity and structure; they do not impose a quote
minimum, and they do not certify the memory analyst's semantic judgments.

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
destination before publication. The run-state validator rechecks byte and
workflow identity; it does not retain a validation receipt.

A `failed` run was abandoned or left public state uncertain; it is never
resumed. Git history is the history
of successfully published tracked reviews; this workflow does not stage or
commit.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-analysis-run-state.md
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
