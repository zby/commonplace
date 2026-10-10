---
type: types/type-spec.md
name: agentic-system-memory-report
description: "Memory analyst's source-grounded findings and integration questions for one analysis run; the report is the set's memory member unchanged"
schema: ./agentic-system-memory-report.schema.yaml
record-prefix: MEM-
---

# Agent memory analysis report

The memory analyst's source-grounded findings and integration questions for one run, at the run's
frozen boundary. The last report the run accepts is the set's memory member
byte for byte: it declares its records under their `MEM-` IDs, and only the
memory analyst revises it, in a correction round.
The [record contract](../instructions/agentic-analysis-records.md) governs
identity, common fields, statuses and evidence interpretation.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-memory-report.md` |
| `description` | Yes | Subject and discriminating memory boundary |
| `run-id` | Yes | The set's run ID |
| `source-identity` | Yes | Exact repository or capture identity |
| `reviewed-boundary` | Yes | Full Git commit or capture label |

## Report sections

### Boundary and evidence

Name the subject, frozen source boundary, included and excluded memory
surfaces, inspected paths and evidence layers, access gaps, and conclusion
limits. The set's source declarations are the Source register of `boundary`.

Retain a compact coverage table: entry point or memory operation, source
path, citations of the supplied or new records covering it, or exclusion/uninspected reason and
conclusion prevented. Distinguish direct source reads from supplied
runtime findings. The inventory includes unresolved operative parts and
alternative admission/read-back paths, with missing facts and prevented
conclusions beside them, under the record contract's coverage rules.

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

`## Annotations` holds only `#### On [<ID>](<member>.md#<anchor>)` entries on
records declared elsewhere.
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
rejection and withdrawal. Separate content authorship, physical I/O and
admission control for each mechanism: explicit human decisions supplying,
editing, approving or replacing that content versus software/model admission.
Generic caller identity does not establish human control. Starting an automatic
workflow is not approval of each later write; reading or selecting an existing
checkpoint does not establish a write. Retain unknown initialization control
without suppressing known subsequent transformations. For
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
Request, selection and delivery in one chain retain separate operation findings;
automatic delivery fulfilling a request is not independent unsolicited supply.
A file identifier does not by itself establish a targeting selector. Known
requested read-back does not resolve an opaque alternative.

### Integration issues

List every correction to a supplied fact, every record of this report that
may duplicate a supplied record, and every unresolved question, with its
evidence, analytical consequence and citations of the records it concerns, so the
reconciliation can connect or supersede without rediscovering its meaning.
State `none` when no issues remain. Supported corrections and justified
unknowns can remain in a complete report; side-channel messages do not
substitute for this section.

### Limitations and checks

Name prevented conclusions, source and method identity rechecks, and the
deterministic validation result. Do not omit weaknesses to make the report
appear ready for integration. A complete report retains no
`Validation: pending` line.


## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of {system} within {memory boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
source-identity: "{repository or capture identity}"
reviewed-boundary: "{immutable revision or capture identity}"
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

## Integration issues

## Limitations and checks
```

Omit Annotations when empty; otherwise use only annotation headings there.
