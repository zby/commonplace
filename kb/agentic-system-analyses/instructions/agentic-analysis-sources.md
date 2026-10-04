---
type: types/note.md
description: "Shared evidence contract for agentic analyses: evidence layers, reading the Source register, citation anchors and retained quotations"
---

# Agentic analysis sources

This contract defines the frozen evidence used by every worker of an
`analyse-agentic-system` run. The boundary job writes Boundary and evidence
and the Source register under the
[boundary contract](./agentic-analysis-boundary.md); code copies them into
the overview. Job invocations declare this file as a required read.

An excluded host's responsibilities are not attributed to the selected
target.

## Source register

The register declares each `SRC-*` ID in one row. Source IDs belong to this
register alone. A source's durable evidence identity is its registered
repository and reviewed commit, or its capture; a worktree path is only the
access root. Supplied execution traces and experimental results use frozen
source identities and anchors like other evidence; their scope and
conditions bound the findings.

For Git, registration permits inspection of the repository at the reviewed
commit. The register's inspected paths and citation anchors describe the
boundary job's initial coverage, not the files later analysts may read.
Inspect and cite newly discovered material files at that same commit,
recording the additional coverage in your member and retaining the required
anchors and quotations. Use the registered repository's source ID, and
state the evidence layer appropriate to the passage; discovering a file
does not establish observed operation or causal support. Do not add a source
ID or rewrite the boundary. A different repository, commit or capture is a
change to the frozen evidence boundary, not additional file coverage.

The selected target's functional scope remains binding. Inspection of an
excluded path to establish relevance is permitted; if it reveals that a
material shipped responsibility was excluded or that the boundary kind is
wrong, identify the path, responsibility and prevented conclusion. Follow
the job's problem or verification rules rather than silently treating the
file as unavailable or broadening the selected target. Captures permit only
their frozen contents.

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

Write each passage as a blockquote ending in a `> ---` attribution:

- Git: `` `commit-relative/path` ``.
- Capture: `` `registered/capture/path` ``.

The run fixes the revision or checksum. For ambiguity, paste a checked range
or lengthen the passage; never calculate a range. Existing pinned GitHub
URLs and ranged, versioned attributions remain valid.

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
