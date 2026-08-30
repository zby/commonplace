---
type: kb/types/type-spec.md
name: agentic-system-analysis-result
description: "Complete stable result of one evidence-bounded external agentic-system analysis run, independent of its response, file, package, or retention lifecycle"
schema: kb/types/agentic-system-analysis-result.schema.yaml
---

# Agentic system analysis result

A complete stable result of one `analyse-agentic-system` run. Choose this type for the run's canonical evidence boundary, registers, lens findings, reconciliation, synthesis, limitations, and verification record. Do not use it for a compact library analysis distilled from the run, an agent-memory-system review, a Commonplace transfer scan, or an operator report.

The type fixes content shape, not lifecycle. A response-only result, a working result under an authorized workshop, a workflow-owned report, and a retained result may all use this type when their owner selects that lifecycle. The applicable collection or workflow still decides whether the artifact may be written, where it belongs, how long it remains, and what later operation consumes it.

## One entry artifact

Every result has one typed Markdown entry artifact. Its frontmatter and eleven level-two sections are the canonical structure regardless of physical carrier:

- In a response, the exact artifact is the stable block between the response fingerprint delimiters.
- In a one-file result, that file is the entry artifact.
- In a package, one file is the entry artifact. A section may contain its records directly or point to one canonical package part. Every pointer names the run ID, resolves as a local link, and states which logical record the target carries. Package parts do not establish another result identity or redefine records owned elsewhere.

The package form distributes weight; it does not create a second structure. The entry artifact retains every required heading in order, including the required shared-record and lens subheadings. A pointer sits beneath the heading it satisfies.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `kb/types/agentic-system-analysis-result.md` |
| `description` | Yes | Retrieval description naming the system, selected boundary, and result disposition |
| `run-id` | Yes | Canonical `AAS-YYYY-MM-DD-system-slug-nn` identity allocated by the producing skill |
| `system` | Yes | Source-native system name or the caller's unambiguous identifier |
| `run-date` | Yes | Date the run opened |
| `result-disposition` | Yes | `complete`, `blocked`, or `out-of-scope` |
| `target-class` | Yes | Selected target class, or `null` when the run stopped before classification |
| `boundary-kind` | Yes | `whole-system`, `subsystem-only`, `complete artifact, partial loop`, or `null` before a boundary could be established |
| `reviewed-boundary` | Yes | Immutable revision or capture identity shared by the run, or `null` before one could be established |
| `analysis-cutoff` | Yes | Applicability cutoff for the frozen evidence, or `null` before one could be established |
| `evidence-tier` | Yes | `code-grounded`, `doc-grounded`, or `null` before the runtime baseline could support a tier |

For a `complete` result, `target-class`, `boundary-kind`, `reviewed-boundary`, `analysis-cutoff`, and `evidence-tier` are non-null. `blocked` and `out-of-scope` are result dispositions, not excuses for a second output shape: retain every required section and state what was not reached, why, and which conclusion that prevents.

## Record conventions

### Canonical identity

Use the run's canonical namespaces: `SRC-*` sources, `CMP-*` components, `OBJ-*` operative objects, `RTE-*` routes, `CLM-*` claims, `ABS-*` evidenced absences, and `BAP-*` behavioral-authority paths. IDs are unique across the whole result and resolve from every physical part. A package part may extend a canonical record only where the producing instruction assigns that field to its lens; it never silently redefines generic identity.

Each amendment stays attached to its canonical record and gives the superseded value, replacement value, evidence anchor, and affected findings. Do not create a second inventory for amended or lens-specific views.

### Status fields

A conclusion-status field contains exactly one of these values:

`absent` · `inapplicable` · `uninspected` · `claimed` · `afforded` · `wired` · `observed` · `causally supported`

Put simultaneous claims at different layers in separately labelled fields or rows. For example, a route can carry `implementation conclusion status: wired` and `operation conclusion status: observed`; it cannot carry one value such as `wired; observed`. Keep guarantee strength in its own field.

The epistemic lens preserves its own two independent fields. **Architectural status** contains one value from the invoked epistemic procedure (`implemented`, `observed, implementation uninspected`, `doctrine only`, `no route found within boundary`, or `not determinable`). **Observed candidate state** contains one value from that procedure. Neither field is a conclusion-status field, and they are never concatenated with one another or translated into this type's conclusion vocabulary. In particular, `implemented and observed` is not a value in any field.

Every negative, thin, conflicting, or uncertain finding names its inspected boundary and the exact conclusion it prevents. Every source-dependent record cites a `SRC-*` ID plus a local anchor. Commonplace ontology may annotate a source-native mechanism, but it never replaces the operational account.

## Required sections

### Run identity

`## Run identity` projects the canonical frontmatter identity for readers and states the physical form: response, one file, or package. A package lists the entry artifact and every canonical part. Do not mint another run ID in a part.

### Boundary and evidence

`## Boundary and evidence` states the intended use, target classification, functional inclusions and exclusions, external dependencies, boundary kind, frozen revision or capture, analysis cutoff, and overall evidence tier. Each excluded participant is paired with the conclusion its exclusion prevents.

### Source register

`## Source register` contains one row per `SRC-*` record:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

A source with several evidence layers uses separate rows or clearly separated scopes. The register does not flatten implementation, doctrine/design, reported operation, observed run, and causal experiment into one layer.

For a focused test or probe, the row's citation anchor resolves to one **probe evidence capsule** in this result. The capsule contains:

`source ID | check ID | UTC execution time | evidence layer | intervention and comparison, or none for an observational run | fixture or input identity | exact command, test node, or reusable-script identity | relevant environment | execution outcome and exit status | raw output inline, or resolvable exact-output location plus byte length and SHA-256 | design and confounding limits | exact conclusion supported and affected canonical IDs`

The check ID joins this capsule to its execution-preflight record. Fixture or input identity uses an immutable revision or byte length and SHA-256 when content is not already canonical. Record a command verbatim; identify a reusable script by path plus immutable revision or SHA-256. The relevant environment names the runtime, tool, package, and service versions and non-secret configuration needed to interpret the result. It records only credential availability, never credential values. A `causal experiment` capsule includes an actual intervention and comparison; otherwise the capsule is `observed run` evidence. A digest without resolvable retained bytes may identify missing output, but by itself it cannot support an `observed` or `causally supported` conclusion. The capsule may be inline or reached through a canonical package pointer. This type requires the evidence to resolve inside the selected carrier; it does not authorize or choose that carrier's lifecycle.

### Shared records

`## Shared records` contains the six required subheadings `### Components`, `### Operative objects`, `### Routes`, `### Claims`, `### Evidenced absences`, and `### Behavioral-authority paths`. Each subsection contains its canonical records or one resolvable package pointer. State `none found within <boundary>` when an inventory is empty; never make heading omission carry that meaning.

Component and operative-object records preserve source-native identity, representational form, storage substrate, and evidence. Route records preserve endpoints, progression, owner, context/state/action effects, applicable status fields, and evidence. Claim records preserve claimed operation and source. An evidenced absence carries an `absent` conclusion status, searched boundary, evidence, and the conclusion it supports or prevents. A behavioral-authority path records consumer, channel, force, and horizon.

### Runtime account

`## Runtime account` traces the ordinary shipped invocation and every material alternate or forcing route selected by the producing skill. For each material loop it identifies the trigger and principal, identities, next-step owner, decision policy and representational form, context, state, executor and effect boundary, runtime-client controls, persistence, coordination and return, recovery, and terminal output. A load-bearing guarantee also names its owner, enforcement point, guarantee strength, covered and alternate paths, required external contract, and separate conclusion-status fields.

For every focused test or probe selected by the producing skill, the runtime account contains one execution-preflight record:

`check ID | intended conclusion | command, test, or script identity | required dependencies and authority | availability evidence | execution disposition: ran or not run | execution outcome or non-execution reason | conclusion prevented`

Each check ID is unique inside the run. An executed check reuses it in the probe evidence capsule. Execution disposition is separate from conclusion status. `not run` does not mean a failed check or absent system behavior. A command attempt that stops before the target check executes leaves the target check `not run`. When no dynamic check was selected, state `no dynamic check planned`.

### Lens scoping

`## Lens scoping` contains `### Memory/context scope` and `### Epistemic scope`. Each record gives trigger-evidence IDs, inspected boundary, pointed-to routes and objects, warranted depth, and rationale. Both records exist even when their evidence warrants only a brief lens pass.

### Lens outputs

`## Lens outputs` contains `### Memory/context lens` and `### Epistemic lens`. Each output says what it inventoried, what it found, and which conclusions its evidence prevents. The memory/context output includes the legacy agent-memory-review detection and invocation disposition. The epistemic output preserves the invoked procedure's distinct architectural-status and observed-candidate-state fields, route-level warrant, and separate epistemic, operational, and behavioral authorities.

The lens sections annotate canonical IDs. They do not reproduce the shared inventory under lens-local IDs.

### Reconciliation

`## Reconciliation` records merged proposals, amendments, anchored conflicts, independent convergence, cross-lens ownership checks, and any legacy review projection check. It names affected IDs and states how each discrepancy was disposed without selecting the strongest-sounding status.

### Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary, architectural characterization and claimed work, runtime map, only the discriminating mechanisms this target needs, scenario-relative assessment, and concrete evidence or system changes that would alter the assessment. It is organized around the system's operational progression, not as concatenated lens reports. It gives no product ranking, generic adoption advice, system-wide epistemic grade, Commonplace delta, or transfer recommendation.

### Limitations

`## Limitations` contains one row per limitation:

`limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it`

Use `none` only after checking the full result. A blocker is also represented in `## Verification and blockers`; this section still states its analytical consequence.

### Verification and blockers

`## Verification and blockers` contains `### Semantic verification`, `### Deterministic validation`, and `### Blockers`. Record the producing skill's semantic checks, the exact deterministic validation target and result, and every unresolved blocker. A complete result says `none` under blockers. A blocked or out-of-scope result states the stopping condition and marks unreached sections explicitly; it does not omit or fabricate analysis records.

Fingerprint and transfer-scan dispositions belong in the operator report outside a response's stable block unless an owning workflow requires them in the typed artifact. The digest never appears inside the bytes it identifies.

## Template

```markdown
---
type: kb/types/agentic-system-analysis-result.md
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
---

# {System} agentic-system analysis

## Run identity

**Physical form:** {response | one file | package}

{Canonical identity and locations.}

## Boundary and evidence

{Boundary, revision, tier, inclusions, exclusions, and prevented conclusions.}

## Source register

{`SRC-*` register.}

## Shared records

### Components

{`CMP-*` records or `none found within ...`.}

### Operative objects

{`OBJ-*` records or `none found within ...`.}

### Routes

{`RTE-*` records or `none found within ...`.}

### Claims

{`CLM-*` records or `none found within ...`.}

### Evidenced absences

{`ABS-*` records or `none found within ...`.}

### Behavioral-authority paths

{`BAP-*` records or `none found within ...`.}

## Runtime account

{Ordinary, alternate, and warranted forcing routes.}

## Lens scoping

### Memory/context scope

{Scoping record.}

### Epistemic scope

{Scoping record.}

## Lens outputs

### Memory/context lens

{Canonical annotations and legacy-review disposition.}

### Epistemic lens

{Canonical annotations, separate epistemic status fields, and route-level conclusion.}

## Reconciliation

{Proposal mappings, amendments, conflicts, convergence, and ownership checks.}

## Bounded synthesis

{System-organized, evidence-bounded synthesis.}

## Limitations

{Limitation-to-prevented-conclusion rows, or `none`.}

## Verification and blockers

### Semantic verification

{Checklist result.}

### Deterministic validation

{Validated entry artifact and result.}

### Blockers

{Blockers, or `none`.}
```

---

Relevant Notes:

- [Analyse an agentic system](../instructions/analyse-agentic-system/SKILL.md) — procedure: owns production, source handling, lens execution, verification, and lifecycle routing for this result type
- [Collections and types](../reference/collections-and-types.md) — rests-on: collections select purpose and lifecycle while this type supplies the reusable structural and semantic contract
- [Representational form](../notes/definitions/representational-form.md) — rests-on: the schema and validator are the symbolic half of this type, while this document carries its natural-language semantic half
