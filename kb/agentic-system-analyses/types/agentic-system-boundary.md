---
type: types/type-spec.md
name: agentic-system-boundary
description: "The frozen evidence boundary of one analysis run: target classification, boundary fields, the frozen source and the Source register that every later job reads"
schema: ./agentic-system-boundary.schema.yaml
---

# Agentic system boundary

The first member of an analysis set. It fixes what the run analyses and from
which frozen evidence; every other member works within it. The overview
repeats its boundary fields in its frontmatter and links to it without
copying its sections.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-boundary.md` |
| `description` | Yes | The target and its frozen boundary in one sentence |
| `run-id` | Yes | The run's ID |
| `result-disposition` | Yes | `complete`, `blocked` or `out-of-scope` |
| `target-class` | Yes | `enclosing runtime`, `embedded inner runtime`, `runtime client`, `returning computation`, `workflow`, `extension or tool mechanism`, `builder or improvement plane`, `host integration`, `memory/knowledge/context-engineering system`, or another explicitly defined class |
| `boundary-kind` | Yes | `whole-system`, `subsystem-only`, or `complete artifact, partial loop` |
| `reviewed-boundary` | Yes | The immutable revision or capture identity shared by the run |
| `analysis-cutoff` | Yes | The applicability cutoff for the frozen evidence |
| `evidence-tier` | Yes | `code-grounded` or `doc-grounded` |
| `source` | Yes | `null` when no source was frozen; otherwise a mapping of `kind` (`git` or `capture`), `identity`, `revision` (a full commit, or a capture label), `path` (the absolute frozen checkout or capture file) and `sha256` (`null` for Git, the capture's digest otherwise) |

The five fields from `target-class` to `evidence-tier` are non-null for a
`complete` disposition, which also has a source. A field is `null` when the
work stopped before establishing it. `reviewed-boundary` is the source's
`revision`, and `source.identity` is the run's source identity.

## Boundary and evidence

`## Boundary and evidence` states the intended use, functional inclusions and
exclusions, external dependencies, target class, boundary kind, frozen
revision or capture, analysis cutoff and overall evidence tier. Each
exclusion or access gap names the conclusion it prevents. An available file
that was not inspected is not an access gap.

A caller in the same repository is not an excluded enclosing application
merely because it calls a library API, and a shipped driver is not external
merely because it supplies state to an API; whether either belongs to the
target follows from its shipped usage and responsibilities. An excluded
host's responsibilities are not attributed to the target.

A `whole-system` boundary covers the material shipped paths that produce,
maintain, admit and consume the system's state, and carries a coverage table
classifying every top-level tracked file or directory as included or
excluded, with its role and the conclusion any exclusion prevents. Directory
rows name the material paths within them; a top-level label alone does not
show coverage of the system's loop. For a memory or knowledge system, the
table accounts for shipped prompts and maintenance instructions, callers that
persist, reload or later consume retained content, and evaluators. The table
distinguishes unavailable evidence, a deliberate exclusion and material not
yet inspected. Coverage is judged on substance, not by the table's presence.

A target that is only a library API or another subsystem is named as that
narrower target with the matching boundary kind. A material shipped path that
could not be inspected gives a boundary kind describing the partial loop,
never `whole-system` merely because the repository was cloned.

## Source register

`## Source register` declares each source once, in a row whose first cell is
its `SRC-*` ID, as `| SRC-1 | ... |`:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

A frozen source has a row. That row's `kind`, `identity` and `revision`
cells hold the frontmatter `source` values unchanged. Each stable source
identity is in a code span, including a non-URL capture identity. A Git row
gives the canonical repository, the full reviewed commit, the initially
inspected commit-relative paths and commit-pinned anchors; an access root
such as `related-systems/<owner>--<repo>/` belongs in inspected scope, not
the identity cell, because a mutable worktree is not the evidence identity.

Source IDs belong to this register alone. A source's durable evidence
identity is its registered repository and reviewed commit, or its capture;
a worktree path is only the access root. The registered Git source is the
repository at that commit: listed paths record initial inspection, not an
allowlist. A capture is limited to its frozen contents. Supplied execution
traces and experimental results are registered like any other source, and
their scope and conditions bound what they support.

Each row names the evidence layers its source supplies:

| Evidence layer | What it supports |
|---|---|
| `implementation` | Inspected executable behavior |
| `doctrine/design` | Declared intent or contract |
| `reported operation` | Attributed operation without inspectable run evidence |
| `observed run` | An inspectable execution trace or artifact |
| `causal experiment` | An observed intervention and comparison with evidence about the design; design and confounding limits bound attribution |

A source with several evidence layers keeps one row, listing its layers and
labelling each layer's inspected scope, anchors and limits within that row,
never a second ID for a layer.

## Not reached

A `blocked` or `out-of-scope` disposition adds `## Not reached`: what was not
reached, why, and which conclusion that prevents. A `complete` disposition
has no such section.

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
