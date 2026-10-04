---
type: types/type-spec.md
name: agent-memory-profile
description: Comparison classifications derived from independently verified memory records at one frozen source boundary
schema: ./agent-memory-profile.schema.yaml
---

# Agent memory profile

A profile classifies the accepted set's memory records after reconciliation and
record verification. It declares no records and adds no evidence. Values cite
canonical records of the set, resolved through reconciliation. A source fact
absent from those records cannot establish a value; the assessment and note
retain that limitation. The profile is a separate member from the source-native
memory account.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agent-memory-profile.md` |
| `description` | Yes | System and compared memory boundary |
| `run-id` | Yes | Supplied set identity |
| `source-identity` | Yes | Frozen repository or capture identity |
| `reviewed-boundary` | Yes | Frozen revision or capture label |
| `memory-comparison` | Yes | Scope and all ten axes |

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
Every record the profile references is declared in the supplied set and
resolved through its reconciliation amendments and supersessions. Other
assessments require `values: []` and `evidence: {}`. `absent` requires an
evidenced-absence record, `MEM-ABS-*` or a seeded `ABS-*`, establishing
bounded absence. Every assessment and value
has a nonempty explanatory note. An opaque included branch prevents
complete coverage, not independently supported positive findings. A
partial trace-learning assessment cannot assert `"no"`. Trace learning has one
value only; quote `"yes"` and `"no"` in YAML so they remain strings.

The scope agrees across the profile, the declared and annotated records
and the members' prose. Every value the prose supports appears in the
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

## Comparison rationale

Explain non-obvious mappings and unions without repeating the records. State
which amendments affect a value, and which missing recorded facts prevent a
stronger assessment. Source inspection may disambiguate a cited record but
cannot supply replacement evidence. Each classification keeps its warrant
in the cited records.

## Template

```markdown
---
type: agentic-system-analyses/types/agent-memory-profile.md
description: "Memory profile of {system} at {memory boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
source-identity: "{repository or capture identity}"
reviewed-boundary: "{frozen revision or capture label}"
memory-comparison:
  scope: "{included and excluded memory surfaces}"
  axes:
    # Fill all ten axes under Memory comparison fields.
---

# {System} memory profile

## Comparison rationale
```
