# Agentic system analysis overview (draft type)

The entry member of one `analyse-agentic-system` run's retained set. It
holds the run's identity, the manifest that defines the set, the evidence
boundary and source register, lens scoping, reconciliation, synthesis,
limitations and verification. It holds no canonical records and no lens
findings; those live in the members its manifest names. A reader that
wants the analysis starts here and verifies the manifest before opening
any member.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-analysis-overview.md` |
| `description` | Yes | Retrieval description naming the system, selected boundary, and disposition |
| `run-id` | Yes | Canonical `AAS-YYYY-MM-DD-system-slug-nn` identity allocated by the producing skill |
| `system` | Yes | Source-native system name or the caller's unambiguous identifier |
| `run-date` | Yes | Date the run opened |
| `result-disposition` | Yes | `complete`, `blocked`, or `out-of-scope` |
| `target-class` | Yes | `enclosing runtime`, `embedded inner runtime`, `runtime client`, `returning computation`, `workflow`, `extension or tool mechanism`, `builder or improvement plane`, `host integration`, `memory/knowledge/context-engineering system`, or another defined class; `null` when the run stopped before classification |
| `boundary-kind` | Yes | `whole-system`, `subsystem-only`, `complete artifact, partial loop`, or `null` before a boundary could be established |
| `reviewed-boundary` | Yes | Immutable revision or capture identity shared by the run, or `null` before one could be established |
| `analysis-cutoff` | Yes | Applicability cutoff for the frozen evidence, or `null` before one could be established |
| `evidence-tier` | Yes | `code-grounded`, `doc-grounded`, or `null` before the runtime baseline could support a tier |
| `members` | Yes | The manifest: a list of `{path, sha256, type}` entries, one per other member of the set, paths relative to the overview's directory; empty for a `blocked` or `out-of-scope` run |

For a `complete` run, the five boundary fields are non-null and `members`
names exactly one runtime report, one memory report and one epistemic
report. `blocked` and `out-of-scope` are dispositions, not a second output
shape: the overview retains every required section and states what was not
reached, why, and which conclusion that prevents, with an empty manifest.

## The set

### Identity and completion

The set is the overview plus the members its manifest names, all in
`kb/reports/state/agentic-system-analysis/<run-id>/` while the run is open
and retained together under
`kb/reports/retained/agentic-system-analysis/<run-id>/` on publication.
Completion is a chain of pins: the run state pins the overview's path and
SHA-256; the overview's manifest pins every other member; the compact
review pins the overview. Correct a retained set through a new run, never
by editing a retained member.

A reader rejects the set, naming the failed check, when a manifest member
is missing or its bytes do not hash to the manifest; when a member's
`run-id` or `reviewed-boundary` differs from the overview's; when the
overview's disposition is not `complete` or the memory report's
`report-status` is not `complete`; when a canonical ID is declared in two
members or referenced without a declaration anywhere in the set; or when
any member fails its own validation.

### Canonical identity across members

The run has one namespace: `SRC-*` sources, `CMP-*` components, `OBJ-*`
operative objects, `RTE-*` routes, `CLM-*` claims, `ABS-*` evidenced
absences, and `BAP-*` behavioral-authority paths. IDs are unique across
the set and resolve within it. Write each ID in full, including lists;
abbreviated suffixes and ranges are invalid. Use commas or words between
referenced IDs, not a dash that can be read as a range. Source quotations
and fenced excerpts are excluded from identifier checks.

`SRC-*` records are declared only in this overview's Source register.
Every other record is declared exactly once, in the member that
established it: the runtime report for records the coordinator's runtime
pass registered, the memory report for records registered from specialist
proposals. A cross-member reference is the bare ID.

Canonical identity applies from allocation and sharing, not only final
acceptance. A split gives the new parts fresh IDs and marks the combined
record superseded; its ID does not change referent. Provisional labels
are local tags.

### Declaration, annotation and amendment grammar

Within a member's `## Shared records`, records are grouped under the six
level-three kind headings and declared once each as a level-four heading,
`#### OBJ-1 — Short label`. Later prose refers to a record as `The object
OBJ-1 ...` or `Evidence: SRC-1 ...`. A level-four heading of the form
`#### On OBJ-1 — Short label` is an **annotation**: another member's
lens-specific fields on a record it does not declare. It never redefines
generic identity, and a member never annotates a record it declares.

An **amendment** corrects a declared fact and lives under the declaring
record, as a paragraph opening `Amendment:` that gives the superseded
value, replacement value, evidence anchor, and affected findings. An
anchored conflict is an amendment carrying both values. Finalization of a
member appends deltas, never a second version of a record; a relabelling
from proposal to registered is carried by the overview's Reconciliation
mapping and is not an amendment.

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
source, one code span containing the full commit-relative path, optionally
followed by line ranges, such as `packages/runtime/src/agent-run.ts` or
`packages/runtime/src/agent-run.ts:595-641,944-1012`; supplied ranges
resolve in the reviewed commit, and a basename denotes a repository-root
file. Commonplace ontology may annotate a source-native mechanism, but it
never replaces the operational account.

## Required sections

### Run identity

`## Run identity` projects the frontmatter identity for readers and
states the intended run-state path and the generated review path, or `not
applicable` for a blocked or out-of-scope run. These name intended
destinations; only the run state declares that publication completed.

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
comparison classifications and assessments. Each passage occurs once
across the set, in the member whose finding it supports; a record in
another member cites that record instead of repeating the passage. At
least one quote anchor is required in a complete set. A quotation block
carries the excerpt, range and attribution that
[`commonplace-quote`](../../../reference/commands.md#commonplace-quote)
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

### Lens scoping

`## Lens scoping` contains `### Memory/context scope` and `### Epistemic
scope`. Each record gives trigger-evidence IDs, inspected boundary,
pointed-to routes and objects, warranted depth, and rationale. Both
records exist even when their evidence warrants only a brief lens pass.

### Reconciliation

`## Reconciliation` records merged proposals, amendments, anchored
conflicts, independent convergence, cross-lens ownership checks, and
integration-issue dispositions. It names affected IDs and states how each
discrepancy was disposed without selecting the strongest-sounding status.
The specialist proposal mapping is one table:

`specialist proposal | canonical record | disposition`

It also names the local specialist report the memory member was finalized
from, by path and SHA-256, and every mechanical edit finalization made.

### Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary,
architectural characterization and claimed work, runtime map, only the
discriminating mechanisms this target needs, scenario-relative assessment,
and concrete evidence or system changes that would alter the assessment.
Where the runtime report supports it, the synthesis states separately
whether the system meets theory-builder conditions 1–4, whether criticism
of a consumed theory improved the system's capacity for future action,
whether the system is reflective or autonomous, and whether it is
self-improving at the declared boundary, each at its own evidence status;
these are independent properties, not a grade or a ladder. It is organized
around the system's operational progression, not as concatenated lens
reports, and cites member records rather than restating them. It gives no
product ranking, generic adoption advice, system-wide epistemic grade,
Commonplace delta, or transfer recommendation. For learning and
self-improvement findings it leads with the strongest supported
contribution, including partial results, then states the unresolved
question, at the level of the comparison actually performed.

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
description: "Complete analysis of {system} at {boundary}, with {disposition} disposition"
run-id: AAS-YYYY-MM-DD-system-slug-nn
system: "{source-native system name}"
run-date: "YYYY-MM-DD"
result-disposition: complete
target-class: "{selected target class}"
boundary-kind: whole-system
reviewed-boundary: "{immutable revision or capture identity}"
analysis-cutoff: "YYYY-MM-DD"
evidence-tier: code-grounded
members:
  - path: runtime.md
    sha256: "{sha256}"
    type: types/agentic-system-runtime-report.md
  - path: memory.md
    sha256: "{sha256}"
    type: types/agent-memory-analysis-report.md
  - path: epistemic.md
    sha256: "{sha256}"
    type: types/agentic-system-epistemic-report.md
---

# {System} agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/{run-id}/run-state.md`

**Generated review:** {`kb/agentic-systems/reviews/<system-slug>.md` | not applicable}

## Boundary and evidence

## Source register

## Lens scoping

### Memory/context scope

### Epistemic scope

## Reconciliation

## Bounded synthesis

## Limitations

## Verification and blockers

### Semantic verification

### Deterministic validation

### Blockers
```
