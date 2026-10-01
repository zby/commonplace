---
type: types/note.md
description: "Shared evidence contract for agentic analyses: target and source boundaries, evidence layers, Source register, citation anchors and retained quotations"
---

# Agentic analysis sources

This contract defines the frozen evidence used by every worker of an
`analyse-agentic-system` run. The boundary job writes Boundary and evidence
and the Source register; code copies them into the overview. Job invocations
declare this file as a required read.

## Boundary and classification

Boundary and evidence states intended use, functional inclusions and
exclusions, external dependencies, target class, boundary kind, frozen
revision or capture, analysis cutoff and overall evidence tier. Each
exclusion or access gap names the conclusion it prevents. An excluded
host's responsibilities are not attributed to the selected target.

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
identity. Source IDs belong to this register alone. A Git row identifies
the canonical repository, full reviewed commit, inspected commit-relative
paths and commit-pinned anchors. An access root such as
`related-systems/<owner>--<repo>/` may also appear; its mutable worktree or
current HEAD is not the durable evidence identity. Supplied execution
traces and experimental results use frozen source identities and anchors
like other evidence; their scope and conditions bound the findings.

| Evidence layer | What it supports |
|---|---|
| `implementation` | Inspected executable behavior |
| `doctrine/design` | Declared intent or contract |
| `reported operation` | Attributed operation without inspectable run evidence |
| `observed run` | An inspectable execution trace or artifact |
| `causal experiment` | An observed intervention and comparison with evidence about the design; design and confounding limits bound attribution |

A source with several layers uses separate rows or clearly separated
scopes. A contrast is necessary but not sufficient for causal
identification; attribution is no finer than the treatment and comparison
actually performed. A component effect requires independent variation of
that component.

## Anchors and quotations

Every source-dependent finding cites a `SRC-*` ID and a local anchor. For
Git, the anchor is one code span containing the full commit-relative path,
such as `packages/runtime/src/agent-run.ts`, or a GitHub blob link at the
reviewed commit. A basename denotes a repository-root file. The path must
exist at that commit and may be binary. Only quotation attributions carry
line ranges; prose paths and GitHub links carry no ranges.

Load-bearing findings, including disputed mechanisms, comparison
classifications and assessments, retain minimum verbatim passages. A
supplied member's record can supply the passage: cite it rather than
repeat it. Parallel analysts may independently retain the same passage;
reconciliation identifies overlapping support without rewriting members.

Each block preserves the excerpt, range and attribution emitted by
`commonplace-quote`, ending in a `> ---` attribution:

- Git: a full-commit GitHub blob URL matching the registered repository,
  or `` `commit-relative/path` @ `full-commit` ``.
- Capture: `` `capture/path[:start-end]` @ `sha256:<checksum>` `` with the
  registered checksum, or the exact registered source URL.

Under whitespace normalization, the quote occurs exactly once in the
frozen blob or capture, or exactly once within a supplied line range that
contains the whole quote. Display line numbers, invented ellipses and
formatting fences are not quote text; discontiguous passages use separate
blocks. Occurrence establishes neither semantic support nor coverage.

## Evidence interpretation

Presence, delivery, activation and demonstrated benefit are distinct.
Claim, affordance, wiring, observation and causal support are distinct.
Curation alone establishes no warrant. Every negative, thin, conflicting
or uncertain finding names its inspected boundary and the conclusion it
prevents. A casual search miss or uninspected branch supports a limitation,
not an evidenced absence.

Source-native operation precedes a Commonplace interpretation. The fit and
any partial or unresolved mapping are stated; ontology never replaces the
operational account. Omission from an open-ended mechanism list is not
evidence of absence.
