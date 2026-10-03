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

For a Git source, establish functional scope after inspecting the repository
tree and tracing the shipped entry points and their consumers. A caller in
the same repository is not an excluded enclosing application merely because
it calls a library API. Determine whether it belongs to the selected target
from the shipped usage and the responsibilities it performs.

Before declaring `whole-system`, include a coverage table under Boundary and
evidence. Classify every top-level tracked file or directory as included or
excluded, with its role and the conclusion any exclusion prevents. Directory
rows name material paths within them; a top-level label alone does not show
coverage of the system's loop. For a memory or knowledge system, explicitly
identify shipped prompts and maintenance instructions, callers that persist,
reload or later consume retained content, and evaluators. Trace their wiring
before deciding whether they are material. Distinguish unavailable evidence
from a deliberate exclusion and from material not yet inspected.

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
An access root such as `related-systems/<owner>--<repo>/` may also appear; its mutable
worktree or current HEAD is not the durable evidence identity.

The registered Git source is the repository at that commit. Listed paths
record the boundary job's initial inspection; they are not an allowlist for
later analysts. Later jobs may inspect and cite other files at the same
commit for the selected target and record their additional coverage in their
own members. Functional target exclusions remain explicit, but neither a
path omitted from the register nor a coverage-table exclusion forbids
inspection to determine a file's relevance. Do not write a path-only
allowlist that changes this rule. Captures remain limited to their frozen
contents; another repository, revision or capture requires a new evidence
boundary.

Each row names one evidence layer from the source contract; a source with
several layers uses separate rows or clearly separated scopes.
