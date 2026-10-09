---
type: types/note.md
description: "Boundary contract for agentic analyses: the meaning of the boundary fields, what Boundary and evidence states, and the form of the Source register"
---

# Agentic analysis boundary

This contract gives the meaning of a run's boundary: the fields, what
Boundary and evidence states, and the form of the Source register. The
[boundary type](../types/agentic-system-boundary.md) fixes the document the
boundary job writes; the overview links to this member without copying its
sections. The [source contract](./agentic-analysis-sources.md), which every
worker reads, supplies the evidence layers and their limits. The boundary job and the record
verifier read this contract.

## Boundary and classification

Boundary and evidence states intended use, functional inclusions and
exclusions, external dependencies, target class, boundary kind, frozen
revision or capture, analysis cutoff and overall evidence tier. Each
exclusion or access gap names the conclusion it prevents.

| Field | Meaning and values |
|---|---|
| `target-class` | `enclosing runtime`, `embedded inner runtime`, `runtime client`, `returning computation`, `workflow`, `extension or tool mechanism`, `builder or improvement plane`, `host integration`, `memory/knowledge/context-engineering system`, or another explicitly defined class |
| `boundary-kind` | `whole-system`, `subsystem-only`, or `complete artifact, partial loop` |
| `reviewed-boundary` | Immutable revision or capture identity shared by the run |
| `analysis-cutoff` | Applicability cutoff for the frozen evidence |
| `evidence-tier` | `code-grounded` or `doc-grounded` |

These five boundary fields are non-null for a complete run. A field
remains null when the work stopped before establishing it. A blocked or
out-of-scope boundary names what was not reached, why, and the conclusion
that prevents.

A caller in the same repository is not an excluded enclosing application
merely because it calls a library API; whether it belongs to the selected
target follows from the shipped usage and the responsibilities it performs.

A `whole-system` boundary includes a coverage table under Boundary and
evidence that classifies every top-level tracked file or directory as
included or excluded, with its role and the conclusion any exclusion
prevents. Directory rows name material paths within them; a top-level label
alone does not show coverage of the system's loop. For a memory or knowledge
system, the table accounts for shipped prompts and maintenance instructions,
callers that persist, reload or later consume retained content, and
evaluators. Unavailable evidence, a deliberate exclusion and material not yet
inspected are distinguished.

`whole-system` requires coverage of the material shipped paths that produce,
maintain, admit and consume the selected system's state. If the requested
target is only a library API or another subsystem, name that narrower target
and use the corresponding boundary kind. If a material shipped path cannot
be inspected, state the prevented conclusion and choose a boundary kind
that describes the partial loop; do not retain `whole-system` solely because
the repository was cloned. Coverage is judged semantically, not by the
presence of a table alone.

## Source register

One row declares each `SRC-*` ID in its first cell, as `| SRC-1 | ... |`:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

Each stable source identity is in a code span, including a non-URL capture
identity. A Git row identifies the canonical repository, full reviewed
commit, initially inspected commit-relative paths and commit-pinned anchors.
For the frozen source row, copy `kind`, `identity` and `revision` from the
frontmatter's `source` object into their respective cells unchanged. Put an
access root such as `related-systems/<owner>--<repo>/` in inspected scope, not
the identity cell. Its mutable worktree or current HEAD is not the durable
evidence identity.

The registered Git source is the repository at that commit. Listed paths
record the boundary job's initial inspection, not an allowlist: the source
contract gives what later jobs may inspect and cite. Captures remain limited
to their frozen contents; another repository, revision or capture requires a
new evidence boundary.

Each source ID is declared once. A source with several evidence layers
keeps one row: list the layers from the source contract and label each
layer's inspected scope, anchors and limits within that row. Do not repeat
the ID or create another ID only to distinguish layers.
