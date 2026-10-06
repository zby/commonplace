---
type: types/type-spec.md
name: agentic-system-boundary
description: "The frozen evidence boundary of one analysis run: target classification, boundary fields, the frozen source and the Source register that every later job reads"
schema: ./agentic-system-boundary.schema.yaml
---

# Agentic system boundary

The first result of an analysis run, written by the boundary job and read by
every later job. It fixes what the run analyses and from which frozen evidence.
Code copies its boundary fields into the overview's frontmatter and its two
sections into the overview unchanged. The
[boundary contract](../instructions/agentic-analysis-boundary.md) gives the
meaning of the fields, what Boundary and evidence must state and how the
Source register is built; the
[source contract](../instructions/agentic-analysis-sources.md) gives the
evidence layers.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-boundary.md` |
| `description` | Yes | The target and its frozen boundary in one sentence |
| `run-id` | Yes | The run's ID |
| `result-disposition` | Yes | `complete`, `blocked` or `out-of-scope` |
| `target-class`, `boundary-kind`, `reviewed-boundary`, `analysis-cutoff`, `evidence-tier` | Yes | The boundary fields of the boundary contract, with the overview's values; `null` when the work stopped before establishing one. All five are non-null for a `complete` disposition. |
| `source` | Yes | `null` when no source was frozen; otherwise a mapping of `kind` (`git` or `capture`), `identity`, `revision` (a full commit, or a capture label), `path` (the absolute frozen checkout or capture file) and `sha256` (`null` for Git, the capture's digest otherwise). A `complete` disposition has a source. |

For a run whose source code froze before this job, `source` is exactly that
frozen checkout and `reviewed-boundary` is its commit; `source.identity` is
the run's source identity.

## Sections

`## Boundary and evidence` and `## Source register`, with the content the
boundary contract requires; the register declares the frozen source in an
`SRC-*` row. A `blocked` or `out-of-scope` disposition adds `## Not reached`,
saying what was not reached, why, and which conclusion that prevents; a
`complete` disposition has no such section.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "{target} at {frozen boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
result-disposition: complete
target-class: "{value}"
boundary-kind: whole-system
reviewed-boundary: "{full commit or capture identity}"
analysis-cutoff: "YYYY-MM-DD"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/owner/repository
  revision: "{full commit}"
  path: /absolute/path/to/checkout
  sha256: null
---

# {System} boundary

## Boundary and evidence

## Source register
```
