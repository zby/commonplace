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
workflow is `kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md`,
which writes the record; no worker edits it.

The record states what later consumers need and nothing else:

- which run produced the outputs (`run-id`, `system`);
- which frozen source boundary it used (`source`);
- the last recorded workflow outcome (`run-status`, `failure`); and
- which exact manifest and published overview bytes completed the run
  (`artifact`, `generated-review`); the manifest pins every member of the set.

It is not a recovery log and retains no phase, packet, correction, validation
receipt or retry state; the workflow's own records hold those.

`run-status` is one of `running` (jobs pending), `blocked` (repair permitted),
`stopped` (only stopping permitted), `uncertain` (an effect's completion is
unknown), `complete` (the run finished) or `failed` (abandoned, or public state
left uncertain). `result-disposition` is the overview's disposition once the
boundary is accepted, else `null`.

`source` is `null` until a source is frozen; then a mapping of `kind` (`git`
or `capture`), `identity` (the stable repository or capture identity),
`revision` (a full commit, or a version or capture label), `path` (the absolute
checkout or capture file; `path`, not `root`) and `sha256` (`null` for Git, the
capture's content digest otherwise). The validator checks that the commit or
capture exists at that path while the record exists.

`artifact` and `generated-review` are `null` until the run completes; then each
is a mapping of a normalized repository-relative `kb/` path and the SHA-256 of
the bytes there. `artifact` names the accepted manifest,
`kb/agentic-system-analyses/state/<run-id>/output/ARTIFACT.yaml`, whose
[set type](./agentic-system-analysis-set.md) selects membership from the
overview's disposition. `generated-review` names the published overview under
`kb/agentic-system-analyses/retained/<system-slug>/`; a blocked or
out-of-scope run has no public output and leaves it `null`.

The `## Run` prose records the destination inspection's expected incumbent
digest, or `absent`. The `## Outcome` prose records the last workflow outcome.

Validation of a complete record checks the manifest, run and boundary identity
across members, the memory member's source identity, the shared set checks
including cross-member record resolution, and every member's source and quote
anchors. These checks establish identity and structure; they impose no quote
minimum and do not certify any analyst's semantic judgments.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-analysis-run-state.md
description: "Minimal completion state for AAS-YYYY-MM-DD-system-slug-token-nn"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
system: "Source-native system name"
run-status: running
result-disposition: null
source: null
artifact: null
generated-review: null
failure: null
---

# Agentic-system analysis run — AAS-YYYY-MM-DD-system-slug-token-nn

## Run

<Target and frozen source boundary once known.>

## Outcome

<Current status, completed outputs, or concise failure reason.>
```
