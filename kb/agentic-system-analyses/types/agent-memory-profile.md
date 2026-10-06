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

New profiles use revision 2: the mapping has `version: 2`, `scope` and
`axes`. Unversioned revision-1 profiles remain interpretable only as frozen
historical outputs under their producing method; do not rewrite them or infer
human admission control from their caller-based write classifications. Revision
identity must accompany derived comparisons; do not silently pool changed
write-agency semantics across revisions. `scope` names the memory
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

Each axis has `assessment`, `units`, `records` and `note`. Each unit has
`scope`, `assessment`, `findings`, `records` and `note`. Each finding has one
`value`, `basis`, `records` and `note`. Findings are authored once; no parallel
value list or evidence map is authored. A basis is `claimed`, `afforded`,
`wired`, `observed`, or `causally supported`, attached to the actual supporting
part or mechanism. Distinct bases remain distinct findings even for the same
value. One wired witness never upgrades an opaque or claimed alternative.

Assessment is `known`, `partial`, `absent`, `inapplicable`, `uninspected`, or
`not-determinable`, describing coverage independently of evidence strength.
At unit level, `known` means complete classification within its named scope;
`partial` retains positive findings and names unresolved included parts,
missing facts and prevented conclusions. Several findings share a unit only
when their scope and coverage agree. `not-determinable` means inspection
established no controlled value; `uninspected` names an included part not
inspected. Neither means absence. These two states, `absent` and
`inapplicable` have no positive findings. `absent` needs bounded absence
records; `inapplicable` needs the relevant boundary and reason.

Axis assessment covers the explicitly named inventory, not a separately
authored complete-value assertion. `known` needs all included units resolved
and accepted records supporting inventory coverage of the scoped boundary.
A positive witness proves existence, never complete enumeration. `partial`
needs positives plus unresolved coverage; without positives, unresolved
inspection remains `uninspected` or `not-determinable`. Axis `absent` and
`inapplicable` need their own bounded warrants. An inventory containing only
inapplicable units uses axis `inapplicable`, not `known`; it is not evidenced
absence. Every assessment and finding
has an explanatory note and references canonical accepted records, resolved
through reconciliation. Unresolved included units cannot be dropped to obtain
`known`; scope excludes no opaque alternative merely because another is known.

Derived system unions retain every supported positive finding and its local
warrant. Compatibility projections may derive strongest existence evidence
per value but must retain unit data, revision and coverage. Complete-value
statistics need complete coverage and strong evidence for every positive unit
finding, not merely a strong witness per value. A local trace-learning `"no"`
is bounded absence in that unit, not a system-wide negative in a partial axis.
A positive `"yes"` suppresses `"no"` only in the derived system union, never
in local evidence. Quote both in YAML. Deterministic checks establish shape,
references and compatible combinations; semantic verification judges support
and inventory completeness.

The scope agrees across the profile, the declared and annotated records
and the members' prose. Every value the prose supports appears in the
profile; a value the profile asserts is supported by the records it
cites. Identify included and excluded alternatives on each branch. An
inspected display summary does not classify an opaque consumed payload.

These are authoring requirements. Publication review uses the supplied
[verification type](./agentic-system-verification.md)'s materiality threshold,
not exhaustive conformity as a stop condition. A partial inventory can retain
a declared local omission when its emitted findings remain valid and the
omission does not change a central conclusion or system-level comparison
value. Unsupported emitted findings and unjustified absence or complete
coverage remain blockers.

### Classification units

| Axis | Natural unit and boundary |
|---|---|
| `storage_substrate` | Each operative retained object/part, including opaque provider state; encoding is not substrate. |
| `representational_form` | Operative part and consumption path; split mixed natural-language, symbolic and numerical material. `parametric` abbreviates distributed-parametric form. |
| `lineage` | Object/part and derivation path; a known path does not resolve initial or embedding provenance. |
| `behavioral_authority` | Retained part, actual consumer and effect; distinct consumers/effects keep distinct findings. |
| `write_agency` | Each write/admission mechanism, not authorship or physical I/O. |
| `curation_operations` | Implemented transformation with its own evidence layer, not a route name or requested behavior. |
| `read_back_direction` | Request, selection and delivery operations within a chain. |
| `read_back_signal` | Actual selector and selected retained part on each push operation. |
| `trace_learning` | Each qualifying automatic trace-fed write and later consumer. |
| `trace_source` | Original input to each qualifying trace-fed write, including mixed or opaque inputs. |

### Write agency

`manual` requires an explicit human operator decision supplying, editing,
approving or replacing that retained content. Software/model admission without
that decision is `automatic`. Starting a workflow does not make subsequent
admission manual. Generic caller identity alone leaves control unresolved.
Content authorship, physical I/O and behavioral authority are independent.
Selecting or reading an existing checkpoint does not establish a write;
classify any separately evidenced replacement at its own admission mechanism.

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

These forces can coexist. Trace-fed artifact updates may establish learning
authority at their update consumer; downstream knowledge consumption is a
separate path. Check both on the actual routes, without inferring improved
capacity or imposing a blanket implication between authority and trace learning. A blocked-ID set used to reject a candidate
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
exist. Read-back signal characterizes push selection and is inapplicable only
for a completely assessed pull-only boundary or bounded evidenced absence of
read-back, with evidence covering every included direction unit. A known pull
route cannot make an unresolved alternative inapplicable. Fulfilling a consumer's request for retained material is pull;
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
inapplicable only for a bounded, completely assessed absence of qualifying
trace learning. One unresolved write cannot be made inapplicable by another
route's negative. Improved capacity remains an independent epistemic claim.
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
which supersessions affect a value, and which missing recorded facts prevent a
stronger assessment. Source inspection may disambiguate a cited record but
cannot supply replacement evidence. Each classification keeps its warrant
in the cited records.

## Template

```markdown
---
type: agentic-system-analyses/types/agent-memory-profile.md
description: "Memory profile of {system} at {memory boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
source-identity: "{repository or capture identity}"
reviewed-boundary: "{frozen revision or capture label}"
memory-comparison:
  version: 2
  scope: "{included and excluded memory surfaces}"
  axes:
    # Repeat for all ten axes using their natural units and controlled values.
    write_agency:
      assessment: partial
      units:
        - scope: "{inspected admission mechanism}"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [MEM-RTE-update-path]
              note: "{recorded software admission without per-content operator decision}"
          records: [MEM-RTE-update-path]
          note: "{unit coverage warrant}"
        - scope: "{included initial-content admission mechanism}"
          assessment: not-determinable
          findings: []
          records: [MEM-OBJ-initial-content]
          note: "{missing control fact and conclusion prevented}"
      records: [MEM-RTE-update-path, MEM-OBJ-initial-content]
      note: "{inventory coverage and unresolved included part}"
    # Placeholder IDs illustrate shape only; replace with accepted canonical IDs.
---

# {System} memory profile

## Comparison rationale
```
