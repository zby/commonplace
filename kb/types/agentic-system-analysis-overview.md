---
type: types/type-spec.md
name: agentic-system-analysis-overview
description: "Entry member of one agentic-system analysis run's retained set: identity, boundary, source register, reconciliation, synthesis, limitations and verification"
schema: ./agentic-system-analysis-overview.schema.yaml
---

# Agentic system analysis overview

The reading entry point of one `analyse-agentic-system` run's retained set.
It holds identity, evidence boundary, source register, reconciliation,
synthesis, limitations and verification. Runtime, memory
and epistemic findings live in their respective members. The sibling
`ARTIFACT.yaml` selects the [analysis set type](../reports/types/agentic-system-analysis-set.md)
and pins every member, including this overview.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-analysis-overview.md` |
| `description` | Yes | For a `complete` run, the reconciliation's one-sentence retrieval description of the system's mechanism and limits, which the public review also carries; otherwise a code-written description naming the system, selected boundary, and disposition |
| `run-id` | Yes | Canonical `AAS-YYYY-MM-DD-system-slug-nn` identity allocated by the producing skill |
| `system` | Yes | Source-native system name or the caller's unambiguous identifier |
| `run-date` | Yes | Date the run opened |
| `result-disposition` | Yes | `complete`, `blocked`, or `out-of-scope` |
| `target-class` | Yes | `enclosing runtime`, `embedded inner runtime`, `runtime client`, `returning computation`, `workflow`, `extension or tool mechanism`, `builder or improvement plane`, `host integration`, `memory/knowledge/context-engineering system`, or another defined class; `null` when the run stopped before classification |
| `boundary-kind` | Yes | `whole-system`, `subsystem-only`, `complete artifact, partial loop`, or `null` before a boundary could be established |
| `reviewed-boundary` | Yes | Immutable revision or capture identity shared by the run, or `null` before one could be established |
| `analysis-cutoff` | Yes | Applicability cutoff for the frozen evidence, or `null` before one could be established |
| `evidence-tier` | Yes | `code-grounded`, `doc-grounded`, or `null` before the runtime baseline could support a tier |
| `inputs-commit` | Yes | The full commit of this repository whose tree supplied the run's method: the analysis instructions, the set's type specs and schemas, and the package code. The coordinator writes HEAD here when the run opens; publication requires HEAD to descend from it with the method paths, the `METHOD_PATHS` constant in `src/commonplace/lib/agentic_publication.py`, unchanged |

For a `complete` run, the five boundary fields are non-null. A `blocked`
or `out-of-scope` overview retains every required section and states what
was not reached, why, and which conclusion that prevents.

## The set

### Identity and completion

Working output lives under
`kb/reports/state/agentic-system-analysis/<run-id>/output/`; publication
retains it under `kb/reports/retained/agentic-system-analysis/<run-id>/`.
Run state and compact reviews pin `ARTIFACT.yaml`. The manifest pins the
reports, and `inputs-commit` identifies the method's committed inputs.
The [set type](../reports/types/agentic-system-analysis-set.md) owns membership
and set checks. File validation checks this overview independently;
directory validation checks the whole set. Only complete sets may publish
or supply comparison rows. Correct retained output through a new run.

### Canonical identity across members

The run has one namespace: `SRC-*` sources, `CMP-*` components, `OBJ-*`
operative objects, `RTE-*` routes, `CLM-*` claims, `ABS-*` evidenced
absences, and `BAP-*` behavioral-authority paths. The run's three
**analysts** are the jobs that inspect the source and each write one
member: the runtime analyst, the memory analyst and the epistemic analyst.
A record ID other than `SRC-*` carries the prefix of the analyst that
established it: none for the runtime analyst (`OBJ-1`), `MEM-` for the
memory analyst (`MEM-OBJ-1`), `EPI-` for the epistemic analyst
(`EPI-OBJ-1`). The prefix is part of the ID for
the life of the set; no step renames a record. IDs are unique across the
set and resolve within it. Write each ID in full, including lists,
using commas or words between referenced IDs. The validator resolves
complete IDs; it does not infer references from abbreviated suffixes or
ranges. Source quotations and fenced excerpts are excluded from identifier
checks.

`SRC-*` records are declared only in the first cell of a table row in this
overview's Source register, as `| SRC-1 | ... |`.
Every other record is declared exactly once, in the member of the analyst
that established it: unprefixed IDs in the runtime report, `MEM-` IDs in
the memory report, `EPI-` IDs in the epistemic report. A cross-member
reference is the full ID.

Canonical identity applies from declaration, not only final acceptance.
When two analysts established the same thing, both records stay declared,
and the Reconciliation supersedes one with an amendment. A split gives the
new parts fresh IDs and marks the combined record superseded; its ID does
not change referent. A superseded ID stays declared, so references to it
still resolve. Provisional labels are local tags.

### Declaration, annotation and amendment grammar

Within a member's `## Shared records`, records are grouped under the six
level-three kind headings and declared once each as a level-four heading,
`#### OBJ-1 — Short label`. The ID precedes the em dash; the rest is the
title. Prose, lists and table rows never declare these records. The same
grammar and duplicate checks apply to every prefix. A level-four heading of the form
`#### On OBJ-1 — Short label` is an **annotation**: another member's
analyst-specific fields on a record it does not declare. It never redefines
generic identity, and a member never annotates a record it declares.
Annotations sit in the section the member's type names: `## Annotations`
in the runtime report, under `## Shared records` in the memory report.

An **amendment** corrects a declared fact of any analyst's record. Amendments
live in one place: this overview's `## Reconciliation`, as paragraphs
that open `Amendment:` followed by the amended record's full ID and give
the superseded value, replacement value, evidence anchor, and affected
findings. An anchored conflict is an amendment carrying both values. A
supersession is an amendment of the form `Amendment: MEM-RTE-3 is
superseded by RTE-7`, with the evidence for the identity. No member is
rewritten after the job that wrote it; a member never carries a second
version of a record or an amendment section.

### Status fields

A conclusion-status field contains exactly one of `absent`,
`inapplicable`, `uninspected`, `claimed`, `afforded`, `wired`, `observed`,
or `causally supported`. Simultaneous claims at different layers go in
separately labelled fields; a route can carry `implementation conclusion
status: wired` and `operation conclusion status: observed`, never one
value such as `wired; observed`. Guarantee strength is its own field,
separate from evidence status: `invariant`, `protocol`, `policy`, `best
effort`, `deployment guarantee`, or `no claimed guarantee`. The epistemic
report's architectural status and observed candidate state are its own
fields and are never translated into this vocabulary.

Every negative, thin, conflicting, or uncertain finding names its
inspected boundary and the exact conclusion it prevents. Every
source-dependent record cites a `SRC-*` ID plus a local anchor: for a Git
source, one code span containing the full commit-relative path, such as
`packages/runtime/src/agent-run.ts`, or a GitHub blob link at the reviewed
commit; a basename denotes a repository-root file. A cited path must exist
at the reviewed commit and may be a binary file. Only quote attributions
carry line ranges. A ranged anchor or ranged GitHub link in prose fails
validation: cite the path without a range, or quote the passage. Commonplace ontology may annotate a source-native mechanism, but it
never replaces the operational account.

## Required sections

### Boundary and evidence

`## Boundary and evidence` states the intended use, target classification,
functional inclusions and exclusions, external dependencies, boundary
kind, frozen revision or capture, analysis cutoff, and overall evidence
tier. Each excluded participant is paired with the conclusion its
exclusion prevents.

### Source register

`## Source register` contains one row per `SRC-*` record:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

Put each stable source identity in a code span so direct consumers can
match it exactly, including non-URL capture identities. The evidence layer
is one of `implementation` (inspected executable behavior),
`doctrine/design` (declared intent or contract), `reported operation` (an
attributed report without inspectable run evidence), `observed run` (an
inspectable execution trace or artifact), or `causal experiment` (an
observed interventional comparison plus evidence about its design; a
contrast is necessary but not sufficient for causal identification, and
the record states design and confounding limits and attributes no more
finely than the actual treatment and comparison). A source with several
evidence layers uses separate rows or clearly separated scopes.

For a Git repository, the row identifies the canonical repository, full
reviewed commit, inspected commit-relative paths, and commit-pinned
citation anchors. A local `related-systems/<owner>--<repo>/` checkout may
be recorded as the operational access root, but its worktree and current
HEAD are not evidence and never the sole durable source identity. For a
focused test or probe, the row's citation anchor resolves to one probe
evidence capsule in the runtime report.

Quotations across the set follow one contract. Members retain minimum
verbatim source excerpts for load-bearing findings: disputed mechanisms,
comparison classifications and assessments. When a supplied input member
already retains the needed passage, cite its record instead of repeating it.
Analysts writing in parallel may independently retain the same passage;
they do not read each other's reports to deduplicate it. The reconciliation
identifies overlapping support through the records; it does not rewrite the
members to remove passages. A
quotation block carries the excerpt, range and attribution that
[`commonplace-quote`](../reference/commands.md#commonplace-quote)
emits for the run's frozen source, ending with a `> ---` attribution: for
Git, a full-commit GitHub blob URL matching the registered repository or
`` `commit-relative/path` @ `full-commit` ``; for a capture,
`` `capture/path[:start-end]` @ `sha256:<checksum>` `` with the registered
checksum, or the exact registered source URL. Under whitespace
normalization each quote occurs exactly once in the Git blob at the
recorded commit or in the immutable capture, or exactly once within a
supplied line range that contains the entire quote. Display line numbers,
invented ellipses and formatting fences are not part of the quoted text;
discontiguous passages use separate blocks. Semantic support remains part
of semantic verification.

### Reconciliation

`## Reconciliation` records supersessions of duplicate records, the set's
amendments, anchored conflicts, independent convergence, ownership checks
across the analysts, and integration-issue dispositions. It names affected
IDs in full and states how each discrepancy was disposed without
selecting the strongest-sounding status. Every ID it cites, amendments
included, resolves in the set. A record of the memory or epistemic analyst
found to duplicate another analyst's record is superseded here, never removed from its member.

Every member's relative links stay inside the set directory, because the
set moves when it is retained; member validation rejects a link that
leaves it.

### Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary,
architectural characterization and claimed work, runtime map, only the
discriminating mechanisms this target needs, scenario-relative assessment,
and concrete evidence or system changes that would alter the assessment.
Where the runtime report supports it, the synthesis states separately
whether the system meets theory-builder conditions 1–4, whether criticism
of a consumed theory improved the system's capacity for future action,
whether the system is reflective or autonomous, and whether it is
[self-improving](../notes/definitions/self-improving-system.md) at the declared boundary, each at its own evidence status;
these are independent properties, not a grade or a ladder. It is organized
around the system's operational progression, not as concatenated analyst
reports, and cites member records rather than restating them. It gives no
product ranking, generic adoption advice, system-wide epistemic grade,
Commonplace delta, or transfer recommendation. For learning and
self-improvement findings it leads with the strongest supported
contribution, including partial results, then states the unresolved
question, at the level of the comparison actually performed.

The Bounded synthesis has a second reader. Code publishes it, after an
evidence-basis line and before the Limitations, as the body of the public
[generated review](../agentic-systems/types/generated-review.md). It must
therefore read without the members' context: a public reader has the IDs
it cites and its links, which code rewrites to point into the retained
set, but not the members' prose.

### Limitations

`## Limitations` contains one row per limitation:

`limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it`

Use `none` only after checking the whole set. A blocker is also
represented under Verification and blockers; this section still states
its analytical consequence.

### Verification and blockers

`## Verification and blockers` contains `### Semantic verification`,
`### Deterministic validation`, and `### Blockers`. Record checks of the
analysis content across the set, including the profile-against-records
check of every known comparison value, the exact deterministic validation
targets and results for every member, and every unresolved blocker. Do
not record projection review jobs, publication attempts, or cleanup here.
A complete run says `none` under blockers; a blocked or out-of-scope run
states its stopping condition here. The overview's digest never appears
inside its own bytes.

## Template

```markdown
---
type: types/agentic-system-analysis-overview.md
description: "{one sentence on the system's mechanism and limits}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
system: "{source-native system name}"
run-date: "YYYY-MM-DD"
result-disposition: complete
target-class: "{selected target class}"
boundary-kind: whole-system
reviewed-boundary: "{immutable revision or capture identity}"
analysis-cutoff: "YYYY-MM-DD"
evidence-tier: code-grounded
inputs-commit: "{full commit of this repository at run start}"
---

# {System} agentic-system analysis

## Boundary and evidence

## Source register

## Reconciliation

## Bounded synthesis

## Limitations

## Verification and blockers

### Semantic verification

### Deterministic validation

### Blockers
```
