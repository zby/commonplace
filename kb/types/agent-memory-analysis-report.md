---
type: types/type-spec.md
name: agent-memory-analysis-report
description: "Memory specialist's source-grounded findings, comparison profile and integration questions for one analysis run; the report is the set's memory member unchanged"
schema: ./agent-memory-analysis-report.schema.yaml
---

# Agent memory analysis report

The memory specialist's source-grounded findings, their comparison
classifications, and their integration questions for one run, bound to
the frozen commission it answers. The last report the run accepts is the
set's memory member byte for byte: it declares its records under their
`MEM-` IDs, and no step rewrites it. Corrections to its records are
amendments in the overview's Reconciliation. Its comparison profile is
authoritative for downstream consumers. Set-wide conventions are those of
the [overview](./agentic-system-analysis-overview.md#the-set).

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agent-memory-analysis-report.md` |
| `description` | Yes | Subject and discriminating memory boundary |
| `run-id` | Yes | The set's run ID |
| `source-identity` | Yes | Exact repository or capture identity |
| `reviewed-boundary` | Yes | Full Git commit or capture label |
| `report-status` | Yes | `complete` or `blocked` |
| `canonical-register-sha256` | Yes | SHA-256 of the exact commissioned `memory-input.md` |
| `worker-model` | Yes | Actual worker model identifier, or `unknown` |
| `method-sha256` | Yes | SHA-256 of the specialist instruction used |
| `memory-comparison` | Yes | Scope and all fourteen axes, under the contract below |

A blocked report names missing access, changed input, or an unresolved
scope decision that prevents completing the assigned analysis. It keeps
all sections; unreached axes use explicit uninspected assessments rather
than guessed values. A blocked report never becomes a set member.

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
| `learning_scope` | `cross-task`, `per-project`, `per-task` |
| `learning_timing` | `offline`, `online`, `staged` |
| `distilled_form` | `natural-language`, `parametric`, `symbolic` |
| `faithfulness_tested` | `no`, `yes` |

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
(`#### On <ID>`) in this report itself; the specialist annotates any
seeded record its profile cites, so the profile validates without the
other members. Other
assessments require `values: []` and `evidence: {}`. `absent` requires an
evidenced-absence record, `MEM-ABS-*` or a seeded `ABS-*`, establishing
bounded absence. Every assessment and value
has a nonempty explanatory note. An opaque included branch prevents
complete coverage, not independently supported positive findings. A
partial boolean assessment cannot assert `"no"`. Boolean axes have one
value only; quote `"yes"` and `"no"` in YAML so they remain strings.

The scope agrees across the profile, the declared and annotated records
and the report's prose. Every value the prose supports appears in the
profile; a value the profile asserts is supported by the records it
cites. Identify included and excluded alternatives on each branch. An
inspected display summary does not classify an opaque consumed payload.

Storage and representational form cover the scoped operative parts, not
one chosen primary store; `parametric` abbreviates distributed-parametric
form. Lineage covers their derivation paths. Behavioral authority names
the force in actual memory consumer paths; `knowledge` abbreviates
advisory/evidential consumption. A human-triggered automatic extraction
remains automatic write agency. Curation operates over retained memory:
`consolidate` reduces retained content without new claims; `dedup` merges
near duplicates; `evolve` revises an existing entry; `synthesize` creates
a claim absent from the inputs; `invalidate` withdraws current reliance
while retaining history; `decay` forgets or downweights; `promote` raises
tier or salience. Index rebuilds, acquisition and primary-key collision
checks alone establish none of these.

Read-back concerns accumulated memory, not static routing instructions.
Use both `pull` and `push` when both routes exist. Read-back signal
characterizes push selection and is inapplicable for a known pull-only
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

Trace learning requires automatic trace-fed writes producing durable
behavior-shaping artifacts or learned parameters; storing raw logs alone
does not qualify. Its source, scope, timing, and distilled form describe
that learning route and are explicitly inapplicable when trace learning is
known not to occur. A generated continuation summary qualifies when traces
feed its automatic production, it is retained, and a later consumer
receives it as context or guidance; calling the transformation reshaping
does not exclude it. Neither new knowledge nor observed improvement is
required for a wired classification. Every qualifying scoped route's
source, scope, timing and distilled form is assessed before aggregating,
and the task horizon comes from that route; a session identifier alone
does not decide `per-task` versus `cross-task`. Faithfulness tested means
retained execution evidence tests dependence on recalled content; test
code or a proposed experiment alone cannot support yes, which requires an
observed or causally supported basis with the set's probe or retained
evidence records.

## Report sections

### Boundary and evidence

Name the subject, frozen source boundary, included and excluded memory
surfaces, inspected paths and evidence layers, access gaps, and conclusion
limits. The commissioned register the input supplied is reproduced here
as provenance; the set's source declarations are the overview's.

### Core ideas

Describe the few mechanisms that distinguish how retained material
affects later work, including context selection and budget, source trust,
and material editing/adoption surfaces. Findings carry primary-source
anchors and evidence status. Load-bearing findings retain minimal verbatim
source code or prose in quote blocks under the set's quotation contract.

### Shared records

Records this report establishes are declared under the six kind headings
under their `MEM-` IDs, as `#### MEM-OBJ-1 — Label`; the report never
declares an unprefixed ID. Records the commission supplied as seeds are not re-declared: the report's
memory-specific fields on them are annotations, `#### On OBJ-1 — Label`,
carrying only those fields and the passages that support them. Records
distinguish operative parts, raw traces from derived memory, content from
access metadata, opaque payloads from their readable display summaries,
and give storage, representational form, lineage, consumers, authority at
the actual consumer, and limits. A route identifies trigger, producer or
selector, retained input, persistence, delivery, later consumer and
status. Only `MEM-CMP-*`, `MEM-OBJ-*`, `MEM-RTE-*`, `MEM-CLM-*`,
`MEM-ABS-*` or `MEM-BAP-*` are record kinds; evidence does not create a
separate kind.

### Write side

Trace acquisition, authoring, automatic transformation, maintenance,
rejection and withdrawal, separating manual authoring, automatic
acquisition, and automatic operations over already retained material. For
trace-fed transformations, including compaction, show the
raw-to-derived-to-later-consumer chain, including alternative checkpoint
forms. Give task/project horizons and timing only when established by that
route. State whether derived behavior-shaping material retains its reasons
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

Explain non-obvious mappings and unions in `memory-comparison`. Every
known value references supporting records; limitations prevent
unsupported complete sets. The same memory boundary applies across the
report and profile. No legacy token-line encoding or matrix fallback is
permitted.

### Integration issues

List every correction to a supplied fact, every record of this report
that may duplicate a seeded record, and every unresolved question, with
its evidence, analytical consequence and the full IDs it concerns, so the
reconciliation can amend or supersede without rediscovering its meaning.
State `none` when no issues remain. A complete report may contain
supported corrections and justified unknown classifications; an unresolved question
that prevents integration sets `report-status: blocked`. Side-channel
messages never substitute for this section.

### Limitations and checks

Name prevented conclusions, source and method identity rechecks, and the
deterministic validation result. A self-check does not attest independence
or correctness of the final integrated analysis. Do not omit weaknesses to
make the report appear ready for integration.
