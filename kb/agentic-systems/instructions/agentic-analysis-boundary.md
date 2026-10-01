---
type: types/note.md
description: "Boundary contract for agentic analyses: target classification, boundary fields and construction of the Source register; read by the boundary job only"
---

# Agentic analysis boundary

This contract defines what the boundary job of an `analyse-agentic-system`
run writes: Boundary and evidence and the Source register. Only that job's
invocation declares this file. The
[source contract](./agentic-analysis-sources.md), which every worker reads,
supplies the evidence layers and their limits.

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

## Source register

One row declares each `SRC-*` ID in its first cell, as `| SRC-1 | ... |`:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

Each stable source identity is in a code span, including a non-URL capture
identity. A Git row identifies the canonical repository, full reviewed
commit, inspected commit-relative paths and commit-pinned anchors. An access
root such as `related-systems/<owner>--<repo>/` may also appear; its mutable
worktree or current HEAD is not the durable evidence identity.

Each row names one evidence layer from the source contract; a source with
several layers uses separate rows or clearly separated scopes.
