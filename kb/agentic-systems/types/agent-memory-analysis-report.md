---
type: types/type-spec.md
name: agent-memory-analysis-report
description: "Memory analyst's source-grounded findings, comparison profile and integration questions for one analysis run; the report is the set's memory member unchanged"
schema: ./agent-memory-analysis-report.schema.yaml
---

# Agent memory analysis report

The memory analyst's source-grounded findings, their comparison
classifications, and their integration questions for one run, at the run's
frozen boundary. The last report the run accepts is the set's memory member
byte for byte: it declares its records under their `MEM-` IDs, and no step
rewrites it. Corrections to its records are amendments in the reconciliation
member. Its comparison profile is authoritative for downstream consumers.
The [source contract](../instructions/agentic-analysis-sources.md) governs
evidence; the [record contract](../instructions/agentic-analysis-records.md)
governs identity, common fields and statuses.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agent-memory-analysis-report.md` |
| `description` | Yes | Subject and discriminating memory boundary |
| `run-id` | Yes | The set's run ID |
| `source-identity` | Yes | Exact repository or capture identity |
| `reviewed-boundary` | Yes | Full Git commit or capture label |
| `report-status` | Yes | `complete` or `blocked` |
| `memory-comparison` | Yes | Scope and all ten axes, under the contract below |

A blocked report names missing access or an unresolved scope decision
that prevents completing the assigned analysis. It keeps all sections;
unreached axes use explicit uninspected assessments rather than guessed
values. A blocked report never becomes a set member. A justified unknown that
only limits a conclusion may remain in a complete report.

## Memory comparison fields

The mapping has exactly `scope` and `axes`. `scope` names the memory
boundary: retained objects accumulated or changed through use, their
access structures, and their write, maintenance, and later-consumer
routes. Do not substitute the whole runtime's storage, permissions, or
shipped static instructions for that memory boundary. Every axis below
occurs exactly once in `axes`:

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

Each axis has exactly the fields `assessment`, `values`, `evidence`,
`records` and `note`. `assessment` is `known`, `partial`, `absent`,
`inapplicable`, `uninspected`, or `not-determinable`; these describe
coverage, separately from evidence strength. `known` asserts that the
value set is complete for this axis within the scope. `partial` retains
supported positive values while its note identifies the unresolved
included parts and the conclusion they prevent. `not-determinable` means
inspected evidence cannot establish any controlled classification.

For `known` or `partial`, give nonempty `values` and exactly one
`evidence` entry per value, each with `basis`, `records`, and `note`. The
basis is `claimed`, `afforded`, `wired`, `observed`, or `causally
supported`, warranted by its named route or object: the strongest
supported witness for that value's existence, with weaker alternatives and
their limits retained in the records. A wired witness does not upgrade
another route or value. A value counts once per system even if several
routes support it. Axis-level `records` support the coverage assessment.
Every record the profile references is declared or annotated
(`#### On <ID>`) in this report itself; the memory analyst annotates any
seeded record its profile cites, so the profile validates without the
other members. Other
assessments require `values: []` and `evidence: {}`. `absent` requires an
evidenced-absence record, `MEM-ABS-*` or a seeded `ABS-*`, establishing
bounded absence. Every assessment and value
has a nonempty explanatory note. An opaque included branch prevents
complete coverage, not independently supported positive findings. A
partial trace-learning assessment cannot assert `"no"`. Trace learning has one
value only; quote `"yes"` and `"no"` in YAML so they remain strings.

The scope agrees across the profile, the declared and annotated records
and the report's prose. Every value the prose supports appears in the
profile; a value the profile asserts is supported by the records it
cites. Identify included and excluded alternatives on each branch. An
inspected display summary does not classify an opaque consumed payload.

Storage and representational form cover the scoped operative parts, not
one chosen primary store; `parametric` abbreviates distributed-parametric
form. Lineage covers their derivation paths. A human-triggered automatic
extraction remains automatic write agency.

### Behavioral authority

[Behavioral authority](../../notes/definitions/behavioral-authority.md) names
the force a retained part has at its actual consumer. The profile names
the consumed part, consumer and effect supporting each value:

| Value | Consumption that establishes the value |
|---|---|
| `knowledge` | Content supplies evidence, reference, context or advice, such as facts returned to an answering agent. |
| `instruction` | Content supplies standing directions, such as retained preferences delivered as host guidance. |
| `enforcement` | Retained controls permit or refuse an action, read or write, such as suppression IDs excluding facts from delivery. |
| `learning` | Retained examples, experience or feedback feed an update to parameters or durable behavior-shaping artifacts, such as session records used to revise standing guidance. |
| `ranking` | Retained content, features or scores influence relative priority, such as fact text and aliases determining retrieval scores. |
| `routing` | Retained state selects an operation, destination, scope or input window, such as a checkpoint selecting the next events to extract. |
| `validation` | Retained criteria determine whether a candidate conforms or is admissible, such as a schema or blocked-ID set checked before admission. |

These forces can coexist. A blocked-ID set used to reject a candidate
supplies a validation criterion and an enforced veto. Ranking influence
does not require retained ranking policy or a learned scoring algorithm;
retained text scored by fixed code is a ranking input. Unconsumed metadata
has no authority. Delivery wiring and actual host compliance retain their
separate evidence bases.

### Curation operations

Curation operates over retained memory. `consolidate` selects, compresses
or combines retained content into a reduced representation of its existing
claims. Extracting standing facts from retained session messages is
consolidation, including when the raw messages remain available. `dedup`
merges or removes near duplicates; `evolve` revises an existing entry;
`synthesize` creates a claim absent from the inputs; `invalidate` withdraws
current reliance while retaining history; `decay` forgets or downweights;
`promote` raises tier or salience.

The operation follows the route's implemented transformation, not its
command name. Index rebuilds, acquisition and primary-key collision checks
alone establish none of these. A faithfulness defect, such as extraction
dropping a negation, does not turn consolidation into synthesis. Opaque
branches retain their uncertainty without excluding an operation supported
by an inspected branch.

### Read-back

Read-back uses the shared record contract's definition of accumulated
memory and later consumption. Use both `pull` and `push` when both routes
exist. Read-back signal characterizes push selection and is inapplicable for a known pull-only
boundary. Fulfilling a consumer's request for retained material is pull;
an automatic selector supplying retained material without that request is
push, and an upstream operator choice can supply its selection input.
Distinguish these operations within a chain rather than counting a
requested return as another push merely because code delivers it. For
each push signal, name trigger, selector input and selected retained part.
Identifier-based push requires an actual identity match that selects
delivered parts; an identifier on a requested file or a catalog entry
alone is insufficient, and coarse availability and budget filtering remain
separate from targeted selection.

### Trace learning and source

Traces record activity or experience, including agent sessions, tool use
and environmental events. Trace learning requires automatic trace-fed writes
producing durable behavior-shaping artifacts or learned parameters; storing
raw logs alone does not qualify. Its source describes that learning route and is
explicitly inapplicable when trace learning is known not to occur.
A generated continuation summary qualifies when traces
feed its automatic production, it is retained, and a later consumer
receives it as context or guidance; calling the transformation reshaping
does not exclude it. Neither new knowledge nor observed improvement is
required for a wired classification. Assess every qualifying scoped route's
trace source before aggregating.

`trace_source` classifies the original input to that qualifying write:

| Value | Source content |
|---|---|
| `session-logs` | Recorded conversational turns from agent work sessions, including user messages used for extraction. |
| `tool-traces` | Recorded tool requests, results or execution feedback used by the update. |
| `event-streams` | Records of discrete runtime or environmental events, such as hook callbacks, calendar entries or timestamped voice cues. |
| `trajectories` | Linked sequences of states, actions and outcomes used as multi-step experience. |

Classification follows source content and origin, not an adapter's role
label or serialization. Wrapping session messages or imported project
files as journal events does not add `event-streams`. Calendar entries and
timestamped voice cues remain event-stream sources when imported as notes
and used to produce durable facts for later consumption. A retained input
may support several source values; each value names the qualifying content
the write actually consumes. Imported static instructions alone establish
imported lineage, not a trace source.

## Report sections

### Boundary and evidence

Name the subject, frozen source boundary, included and excluded memory
surfaces, inspected paths and evidence layers, access gaps, and conclusion
limits. The set's source declarations are the overview's.

Retain a compact coverage table: entry point or memory operation, source
path, covering supplied or new IDs, or exclusion/uninspected reason and
conclusion prevented. Distinguish direct source reads from supplied
runtime findings.

### Core ideas

Describe the few mechanisms that distinguish how retained material
affects later work, including context selection and budget, source trust,
and material editing/adoption surfaces. Findings follow the shared source and status contracts.

### Shared records

`## Shared records` contains declarations under the six kind headings in
the template, following the shared record contract with `MEM-` IDs.
An empty kind says `none declared in this member`. Records declared elsewhere
are annotated under Annotations rather than re-declared. Records
distinguish operative parts, raw traces from derived memory, content from
access metadata, opaque payloads from their readable display summaries,
and give storage, representational form, lineage, consumers, authority at
the actual consumer, and limits. A route identifies trigger, producer or
selector, retained input, persistence, delivery, later consumer and
status. Evidence does not create a separate record kind.

### Annotations

`## Annotations` holds only `#### On <ID> — Label` entries on records declared
elsewhere, including every such record the comparison profile cites.
An entry carries only memory-specific fields and their supporting passages:
storage substrate, representational form, lineage, memory consumers and their
behavioral authority; raw versus derived material; write agency, curation,
trace learning and source;
and read-back trigger, selector inputs, selected retained parts, budget,
persistence, delivery, later consumer, status and limits. It does not copy the
record's generic identity or route progression. Omit the section when there
are no annotations.

### Write side

Trace acquisition, authoring, automatic transformation, maintenance,
rejection and withdrawal, separating manual authoring, automatic
acquisition, and automatic operations over already retained material. For
trace-fed transformations, including compaction, show the
raw-to-derived-to-later-consumer chain, including alternative checkpoint
forms. State whether derived behavior-shaping material retains its reasons
and whether a later route reads them. Link to the records rather than
repeating their full artifact classifications.

### Read-back

Identify the later consumer, selection operation and delivery channel for
each route. Distinguish requested reads from automatic supply, API
affordance from wiring, and availability, delivery, activation and
demonstrated benefit. A storage method or an API with an unspecified
hypothetical caller establishes only a storage capability, not a consumer
route; a documented external consumer role may establish an afforded route
without deployed wiring. A push route names its automatic selector's
trigger, inputs, selected parts, budget and consumption channel. Record
targeting inputs, budgets and authority where they affect a conclusion.

### Comparison rationale

Explain non-obvious mappings and unions in `memory-comparison`. The field
contract above governs scope and support; do not repeat record
classifications here.

### Integration issues

List every correction to a supplied fact, every record of this report that
may duplicate a seeded record, and every unresolved question, with its
evidence, analytical consequence and the full IDs it concerns, so the
reconciliation can amend or supersede without rediscovering its meaning.
State `none` when no issues remain. Supported corrections and justified
unknowns can remain in a complete report; side-channel messages do not
substitute for this section.

### Limitations and checks

Name prevented conclusions, source and method identity rechecks, and the
deterministic validation result. A self-check does not attest independence
or correctness of the final integrated analysis. Do not omit weaknesses to
make the report appear ready for integration.

A complete report retains no `Validation: pending` line. Code's acceptance
record is authoritative for structural acceptance; the report does not
independently attest acceptance.


## Template

```markdown
---
type: types/agent-memory-analysis-report.md
description: "Memory mechanisms of {system} within {memory boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
source-identity: "{repository or capture identity}"
reviewed-boundary: "{immutable revision or capture identity}"
report-status: complete
memory-comparison:
  scope: "{included and excluded memory surfaces}"
  axes:
    # Fill all ten axes under Memory comparison fields.
---

# {System} memory report

## Boundary and evidence

## Core ideas

## Shared records

### Components

### Operative objects

### Routes

### Claims

### Evidenced absences

### Behavioral-authority paths

## Annotations

## Write side

## Read-back

## Comparison rationale

## Integration issues

## Limitations and checks
```

Omit Annotations when empty; otherwise use only annotation headings there.
