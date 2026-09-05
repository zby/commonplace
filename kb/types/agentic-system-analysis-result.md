---
type: kb/types/type-spec.md
name: agentic-system-analysis-result
description: "Exact state result of one evidence-bounded external agentic-system analysis run"
schema: kb/types/agentic-system-analysis-result.schema.yaml
---

# Agentic system analysis result

A complete result of one `analyse-agentic-system` run. It holds the run's evidence boundary, registers, lens findings, reconciliation, synthesis, limitations, and verification record. Do not use it for the compact generated review, an agent-memory-system review, a Commonplace transfer scan, or an operator report.

## One entry artifact

Every result is one typed Markdown file at
`kb/reports/state/agentic-system-analysis/<run-id>/result.md`. Its frontmatter
and eleven level-two sections are the canonical structure. Successful publication
also retains the identical bytes at
`kb/reports/retained/agentic-system-analysis/<run-id>/result.md`. This copy keeps
the same result identity. The public review pins its path and SHA-256 so later
consumers can read the exact analysis from a clean checkout. Correct it through
a new analysis run, never by editing the retained copy.

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

### Memory comparison fields

Every newly published complete result includes `memory-comparison` in its
frontmatter. This normalizes findings already established by the main analysis;
it is not another memory review. A historical result without it cannot enter
the new matrix. Publication requires the field; validation checks it whenever
present.

The mapping has exactly `scope` and `axes`. `scope` names the memory boundary:
retained objects accumulated or changed through use, their access structures,
and their write, maintenance, and later-consumer routes. Do not substitute the
whole runtime's storage, permissions, or shipped static instructions for that
memory boundary. Every axis below occurs exactly once in `axes`:

| Axis | Controlled values |
|---|---|
| `storage_substrate` | `files`, `graph`, `in-memory`, `kv`, `model-weights`, `prompt-registry`, `rdbms`, `repo`, `service-object`, `sqlite`, `vector` |
| `representational_form` | `natural-language`, `parametric`, `symbolic` |
| `lineage` | `authored`, `imported`, `other-compiled`, `trace-extracted` |
| `behavioral_authority` | `enforcement`, `instruction`, `knowledge`, `learning`, `ranking`, `routing`, `validation` |
| `write_agency` | `automatic`, `manual` |
| `curation_operations` | `consolidate`, `decay`, `dedup`, `evolve`, `invalidate`, `promote`, `synthesize` |
| `read_back_direction` | `pull`, `push` |
| `read_back_signal` | `coarse`, `identifier`, `inferred-embedding`, `inferred-judgment`, `inferred-lexical` |
| `trace_learning` | `no`, `yes` |
| `trace_source` | `event-streams`, `session-logs`, `tool-traces`, `trajectories` |
| `learning_scope` | `cross-task`, `per-project`, `per-task` |
| `learning_timing` | `offline`, `online`, `staged` |
| `distilled_form` | `natural-language`, `parametric`, `symbolic` |
| `faithfulness_tested` | `no`, `yes` |

Each axis has exactly these fields:

```yaml
assessment: known
basis: wired
values: [pull, push]
records: [RTE-2, RTE-3]
note: "Both read-back routes are wired within the named memory boundary."
```

`assessment` is `known`, `absent`, `inapplicable`, `uninspected`, or
`not-determinable`. The last value means inspected evidence cannot determine
the classification. These are comparison assessments, distinct from the
result's conclusion-status vocabulary.

For `known`, give a nonempty set of controlled values, existing canonical
records declared at the start of a table row, paragraph, list item, or
subheading under Shared records, and one evidence `basis`: `claimed`,
`afforded`, `wired`, `observed`, or `causally supported`. Union values across the declared scoped parts; use the
weakest basis supporting that union and retain per-route differences in the
records. A known set is complete for this axis within that scope. If an
uninspected part prevents that assertion, record the uncertainty rather than
silently omitting the part.

The scope must agree across the profile, canonical objects/routes and lens
account. If a route combines included and excluded alternatives, identify the
parts on each branch. An inspected container or display summary does not decide
the representational form of an opaque payload consumed alongside it.

Other assessments require `values: []` and `basis: null`. An `absent`
assessment references an `ABS-*` record establishing the bounded absence.
Every assessment has a `note` explaining its mapping, aggregation, or conclusion
prevented. A term outside the vocabulary requires an explicit partial mapping
or a not-determinable assessment, not an invented token.

Storage and representational form cover the scoped operative parts, not one
chosen primary store. `parametric` abbreviates distributed-parametric form.
Lineage covers their derivation paths. Behavioral authority names the force
in actual memory consumer paths; `knowledge` abbreviates advisory/evidential
consumption. A human-triggered automatic extraction remains automatic write
agency. Curation operates over retained memory; acquisition and primary-key
collision checks alone are not memory consolidation or deduplication.

Read-back concerns accumulated memory, not static routing instructions. Use
both `pull` and `push` when both routes exist. Read-back signal characterizes
push selection and is inapplicable for a known pull-only boundary.

Name the memory consumer and selection operation when assigning direction.
Fulfilling that consumer's request for retained material is pull. An automatic
selector supplying retained material without that request is push; an upstream
operator choice can supply its selection input. Distinguish these operations
within a chain rather than counting a requested return as another push merely
because code delivers it. For each push signal, name trigger, selector input
and selected retained part. Identifier-based push requires an actual identity
match that selects delivered parts, such as branch/entry selection during
automatic history assembly. An identifier on a requested file or a catalog
entry alone is insufficient; coarse availability and budget filtering remain
separate from targeted selection.

Trace learning requires automatic trace-fed writes producing durable
behavior-shaping artifacts or learned parameters; storing raw logs alone does
not qualify. Its source, scope, timing, and distilled form describe that
learning route and are explicitly inapplicable when trace learning is known
not to occur. Ordinary retention and retrieval fields still apply.

A generated continuation summary qualifies when traces feed its automatic
production, it is retained, and a later consumer receives it as context or
guidance. Calling the transformation reshaping does not exclude it. Neither
new knowledge nor observed improvement is required for a wired classification.
Assess every qualifying scoped route's source, scope, timing and distilled
form before aggregating. Establish the task horizon from that route; a session
identifier alone does not decide `per-task` versus `cross-task`.

Boolean axes have one value only; quote `"yes"` and `"no"` in YAML so they
remain strings. Faithfulness tested means retained execution
evidence tests dependence on recalled content; test code or a proposed
experiment alone cannot support yes. A yes requires observed or causally
supported basis, with the result's probe or retained evidence records.

CSV readers preserve value sets, assessment, basis, and record references
separately. The original result retains the rationale and full evidence account.
No reader recovers missing classifications from a previous CSV, absent tag,
legacy review, or compact prose.

### Canonical identity

Use the run's canonical namespaces: `SRC-*` sources, `CMP-*` components, `OBJ-*` operative objects, `RTE-*` routes, `CLM-*` claims, `ABS-*` evidenced absences, and `BAP-*` behavioral-authority paths. IDs are unique across the whole result and resolve within this file. A lens may extend a canonical record only where the producing instruction assigns that field to it; it never silently redefines generic identity.

Canonical identity applies from allocation and sharing, not only final
acceptance. A split gives the new parts fresh IDs and marks the combined record
superseded; its ID does not change referent. Provisional labels are local tags.

Each amendment stays attached to its canonical record and gives the superseded value, replacement value, evidence anchor, and affected findings. Do not create a second inventory for amended or lens-specific views.

### Status fields

A conclusion-status field contains exactly one of these values:

`absent` · `inapplicable` · `uninspected` · `claimed` · `afforded` · `wired` · `observed` · `causally supported`

Put simultaneous claims at different layers in separately labelled fields or rows. For example, a route can carry `implementation conclusion status: wired` and `operation conclusion status: observed`; it cannot carry one value such as `wired; observed`. Keep guarantee strength in its own field.

The epistemic lens preserves its own two independent fields. **Architectural status** contains one value from the invoked epistemic procedure (`implemented`, `observed, implementation uninspected`, `doctrine only`, `no route found within boundary`, or `not determinable`). **Observed candidate state** contains one value from that procedure. Neither field is a conclusion-status field, and they are never concatenated with one another or translated into this type's conclusion vocabulary. In particular, `implemented and observed` is not a value in any field.

Every negative, thin, conflicting, or uncertain finding names its inspected boundary and the exact conclusion it prevents. Every source-dependent record cites a `SRC-*` ID plus a local anchor. For a Git source, write the local anchor as one code span containing the full commit-relative path and one or more line ranges, for example `packages/runtime/src/agent-run.ts:595-641,944-1012`. A basename denotes a repository-root file, not an arbitrary matching file. Commit-pinned GitHub blob links use the same full path and the result's reviewed revision. Commonplace ontology may annotate a source-native mechanism, but it never replaces the operational account.

## Required sections

### Run identity

`## Run identity` projects the canonical frontmatter identity for readers and states:

- the intended run-state path;
- the generated whole-system review path, or `not applicable` for a blocked or
  out-of-scope result; and
- `**Memory analysis report:**` with its local run path, and
  `**Memory analysis report SHA-256:**` with its exact byte digest (both
  `not applicable` when no report was produced for an incomplete result).

The local report is operational provenance; the retained result must remain
self-contained after local run cleanup. These fields make the relationship between the exact result and its public
projections legible without reproducing workflow bookkeeping. They name
intended destinations; only the run state declares that publication completed.

### Boundary and evidence

`## Boundary and evidence` states the intended use, target classification, functional inclusions and exclusions, external dependencies, boundary kind, frozen revision or capture, analysis cutoff, and overall evidence tier. Each excluded participant is paired with the conclusion its exclusion prevents.

### Source register

`## Source register` contains one row per `SRC-*` record:

`source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented`

Put each stable source identity in a code span so direct consumers can match it
exactly, including non-URL capture identities. A source with several evidence
layers uses separate rows or clearly separated scopes. The register does not flatten implementation, doctrine/design, reported operation, observed run, and causal experiment into one layer.

For a Git repository, the row identifies the canonical repository, full reviewed commit, inspected commit-relative paths, and commit-pinned citation anchors. Every cited path and line range must resolve from the reviewed commit. A local `related-systems/<owner>--<repo>/` checkout may be recorded as the operational access root, but its worktree and current HEAD are not evidence and are never the sole durable source identity.

A quote-anchored blockquote in this result or one of its generated review
projections ends with a `> ---` attribution. For Git, the attribution contains
either a full-commit GitHub blob URL matching the registered repository or
`` `commit-relative/path` @ `full-commit` ``. For a capture, it names the
captured source. Publication normalizes whitespace and requires the quote to
occur in the Git blob at the recorded commit or in the immutable capture. This
is a structural occurrence check. Semantic support remains part of semantic
verification.

For a focused test or probe, the row's citation anchor resolves to one **probe evidence capsule** in this result. The capsule contains:

`source ID | check ID | UTC execution time | evidence layer | intervention and comparison, or none for an observational run | fixture or input identity | exact command, test node, or reusable-script identity | relevant environment | execution outcome and exit status | raw output inline, or resolvable exact-output location plus byte length and SHA-256 | design and confounding limits | exact conclusion supported and affected canonical IDs`

The check ID joins this capsule to its execution-preflight record. Fixture or input identity uses an immutable revision or byte length and SHA-256 when content is not already canonical. Record a command verbatim; identify a reusable script by path plus immutable revision or SHA-256. The relevant environment names the runtime, tool, package, and service versions and non-secret configuration needed to interpret the result. It records only credential availability, never credential values. A `causal experiment` capsule includes an actual intervention and comparison; otherwise the capsule is `observed run` evidence. A digest without resolvable retained bytes may identify missing output, but by itself it cannot support an `observed` or `causally supported` conclusion. Keep the capsule inline in this result.

### Shared records

`## Shared records` contains the six required subheadings `### Components`, `### Operative objects`, `### Routes`, `### Claims`, `### Evidenced absences`, and `### Behavioral-authority paths`. Each subsection contains its canonical records. State `none found within <boundary>` when an inventory is empty; never make heading omission carry that meaning.

Component and operative-object records preserve source-native identity, representational form, storage substrate, and evidence. Route records preserve endpoints, progression, owner, context/state/action effects, applicable status fields, and evidence. Claim records preserve claimed operation and source. An evidenced absence carries an `absent` conclusion status, searched boundary, evidence, and the conclusion it supports or prevents. A behavioral-authority path records consumer, channel, force, and horizon.

### Runtime account

`## Runtime account` traces the ordinary shipped invocation and every material alternate or forcing route selected by the producing skill. For each material loop it identifies the trigger and principal, identities, next-step owner, decision policy and representational form, context, state, executor and effect boundary, runtime-client controls, persistence, coordination and return, recovery, and terminal output. A load-bearing guarantee also names its owner, enforcement point, guarantee strength, covered and alternate paths, required external contract, and separate conclusion-status fields.

For every focused test or probe selected by the producing skill, the runtime account contains one execution-preflight record:

`check ID | intended conclusion | command, test, or script identity | required dependencies and authority | availability evidence | execution disposition: ran or not run | execution outcome or non-execution reason | conclusion prevented`

Each check ID is unique inside the run. An executed check reuses it in the probe evidence capsule. Execution disposition is separate from conclusion status. `not run` does not mean a failed check or absent system behavior. A command attempt that stops before the target check executes leaves the target check `not run`. When no dynamic check was selected, state `no dynamic check planned`.

### Lens scoping

`## Lens scoping` contains `### Memory/context scope` and `### Epistemic scope`. Each record gives trigger-evidence IDs, inspected boundary, pointed-to routes and objects, warranted depth, and rationale. Both records exist even when their evidence warrants only a brief lens pass.

### Lens outputs

`## Lens outputs` contains `### Memory/context lens` and `### Epistemic lens`. Each output says what it inventoried, what it found, and which conclusions its evidence prevents. The memory/context output integrates the specialist report with canonical IDs and retains the evidence necessary to understand its findings without opening that local report. The epistemic output preserves the invoked procedure's distinct architectural-status and observed-candidate-state fields, route-level warrant, and separate epistemic, operational, and behavioral authorities.

The lens sections annotate canonical IDs. They do not reproduce the shared inventory under lens-local IDs.

### Reconciliation

`## Reconciliation` records merged proposals, amendments, anchored conflicts, independent convergence, cross-lens ownership checks, and specialist proposal-ID mappings and integration-issue dispositions. It names affected IDs and states how each discrepancy was disposed without selecting the strongest-sounding status.

### Bounded synthesis

`## Bounded synthesis` gives the evidence basis and boundary, architectural characterization and claimed work, runtime map, only the discriminating mechanisms this target needs, scenario-relative assessment, and concrete evidence or system changes that would alter the assessment. It is organized around the system's operational progression, not as concatenated lens reports. It gives no product ranking, generic adoption advice, system-wide epistemic grade, Commonplace delta, or transfer recommendation.

### Limitations

`## Limitations` contains one row per limitation:

`limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it`

Use `none` only after checking the full result. A blocker is also represented in `## Verification and blockers`; this section still states its analytical consequence.

### Verification and blockers

`## Verification and blockers` contains `### Semantic verification`, `### Deterministic validation`, and `### Blockers`. Record checks of the analysis content, the exact deterministic validation target and result, and every unresolved blocker. Do not record projection review jobs, publication attempts, or cleanup here. A complete result says `none` under blockers. A blocked or out-of-scope result states the stopping condition and marks unreached sections explicitly; it does not omit or fabricate analysis records.

A transfer-scan disposition belongs in the operator report unless an owning workflow requires it in a separate state artifact. The result's digest never appears inside the bytes it identifies.

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

**Run state:** `kb/reports/state/agentic-system-analysis/{run-id}/run-state.md`

**Generated review:** {`kb/agentic-systems/reviews/<system-slug>.md` | not applicable}

**Memory analysis report:** {path | not applicable}
**Memory analysis report SHA-256:** {sha256 | not applicable}

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

{Integrated specialist findings and canonical annotations.}

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
