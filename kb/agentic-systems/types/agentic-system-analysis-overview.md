---
type: types/type-spec.md
name: agentic-system-analysis-overview
description: "Entry member of one agentic-system analysis run's retained set: identity, boundary, source register, amendment index, synthesis, limitations and both verifications"
schema: ./agentic-system-analysis-overview.schema.yaml
---

# Agentic system analysis overview

The reading entry point of one `analyse-agentic-system` run's retained set.
It holds identity, evidence boundary, source register, an amendment index,
synthesis, limitations and both verifications. Runtime, memory, epistemic
and reconciliation findings live in their respective members. The sibling
`ARTIFACT.yaml` selects the [analysis set type](./agentic-system-analysis-set.md)
and pins every member, including this overview.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-systems/types/agentic-system-analysis-overview.md` |
| `description` | Yes | For a `complete` run, the synthesizer's one-sentence retrieval description of the system's mechanism and limits, which the public review also carries; otherwise a code-written description naming the system, selected boundary, and disposition |
| `run-id` | Yes | Canonical `AAS-YYYY-MM-DD-system-slug-nn` identity allocated by the producing skill |
| `system` | Yes | Source-native system name or the caller's unambiguous identifier |
| `run-date` | Yes | Date the run opened |
| `result-disposition` | Yes | `complete`, `blocked`, or `out-of-scope` |
| `target-class` | Yes | Target role under the boundary contract; `null` before classification |
| `boundary-kind` | Yes | Extent of the selected target under the boundary contract; `null` before establishment |
| `reviewed-boundary` | Yes | Immutable revision or capture identity shared by the run, or `null` before one could be established |
| `analysis-cutoff` | Yes | Applicability cutoff for the frozen evidence, or `null` before one could be established |
| `evidence-tier` | Yes | `code-grounded`, `doc-grounded`, or `null` before the runtime baseline could support a tier |
| `inputs-commit` | Yes | Full repository commit supplying the instructions, contracts, schemas and package code; publication requires the method unchanged |

For a `complete` run, the five boundary fields are non-null. A `blocked`
or `out-of-scope` overview retains every required section and states what
was not reached, why, and which conclusion that prevents.

## Shared contracts

The [boundary contract](../instructions/agentic-analysis-boundary.md) defines
boundary classifications and source declarations. The
[source contract](../instructions/agentic-analysis-sources.md) defines
evidence layers, anchors and quotations. The [record contract](../instructions/agentic-analysis-records.md)
defines the namespace, declarations, annotations, amendments, fields and
status meanings for all members.

### Identity and completion

Working output lives under
`kb/agentic-systems/reports/state/<run-id>/output/`; publication
retains it under `kb/agentic-systems/reports/retained/<run-id>/`.
Run state and compact reviews pin `ARTIFACT.yaml`. The manifest pins the
reports, and `inputs-commit` identifies the method's committed inputs.
The [set type](./agentic-system-analysis-set.md) owns membership
and set checks. File validation checks this overview independently;
directory validation checks the whole set. Only complete sets may publish
or supply comparison rows. Correct retained output through a new run.

## Required sections

### Boundary and evidence

`## Boundary and evidence` contains the boundary account defined by the
boundary contract, copied from the boundary job.

### Source register

`## Source register` contains that job's `SRC-*` rows under the boundary
contract. Source identity and evidence scopes remain stable across members.
For Git, the identity is the repository at the reviewed commit; listed
paths record initial coverage and do not prevent later members from
inspecting and citing other files at that commit for the selected target.
For a complete run, code appends `Amended or superseded records: <IDs or none>`
and a link to `reconciliation.md`. Resolve these IDs through that member
before relying on an analyst's original wording.

### Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary, architectural
characterization and claimed work, runtime map, only the discriminating
mechanisms this target needs, scenario-relative assessment, and concrete
evidence or system changes that would alter the assessment. Where the
runtime report supports it, the synthesis states separately whether the
system meets theory-builder conditions 1–4, whether criticism of a consumed
theory improved the system's capacity for future action, whether the system
is reflective or autonomous, and whether it is
[self-improving](../../notes/definitions/self-improving-system.md) at the
declared boundary, each at its own evidence status; these are independent
properties, not a grade or a ladder. It is organized around the system's
operational progression, not as concatenated analyst reports, and cites
member records rather than restating them. It gives no product ranking,
generic adoption advice, system-wide epistemic grade, Commonplace delta, or
transfer recommendation. For learning and self-improvement findings it leads
with the strongest supported contribution, including partial results, then
states the unresolved question, at the level of the comparison actually
performed.

The Bounded synthesis has a second reader. Code publishes it, after an
evidence-basis line and before the Limitations, as the body of the public
[generated review](./generated-review.md). It must
therefore read without the members' context: a public reader has the IDs
it cites and its links, which code rewrites to point into the retained
set, but not the members' prose.

### Limitations

`## Limitations` contains one row per limitation:

`limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it`

Carry every `Unresolved conflict:` in the reconciliation into this section.
A record fault found during synthesis verification is stated here with its
prevented conclusion; it does not reopen reconciliation. If representing it
as a limitation would make the synthesis misleading, stop the run.
Use `none` only after checking the whole set. A blocker is also
represented under Verification and blockers; this section still states
its analytical consequence.

### Verification and blockers

`## Verification and blockers` contains `### Record verification`,
`### Synthesis verification`, `### Deterministic validation`, and
`### Blockers`. The two independent checks remain separate: record
verification covers the memory profile, amendments, supersessions and scope;
synthesis verification covers support for public statements, readability
without the members' context, and unresolved conflicts in Limitations.
Record the exact deterministic validation
targets and results for every member, and every unresolved blocker. Do
not record projection review jobs, publication attempts, or cleanup here.
A complete run says `none` under blockers; a blocked or out-of-scope run
states its stopping condition here. The overview's digest never appears
inside its own bytes.

## Template

```markdown
---
type: agentic-systems/types/agentic-system-analysis-overview.md
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

## Bounded synthesis

## Limitations

## Verification and blockers

### Record verification

### Synthesis verification

### Deterministic validation

### Blockers
```
