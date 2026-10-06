---
type: types/type-spec.md
name: agentic-system-runtime-report
description: "Runtime member of an analysis set: source-grounded runtime account, the canonical records the runtime analyst declares, and its annotations on other members' records"
schema: ./agentic-system-runtime-report.schema.yaml
---

# Agentic system runtime report

The runtime baseline gives source-grounded invocations, alternate/forcing
routes and `RT-` records. It precedes both specialists and stays unchanged.
The [source contract](../instructions/agentic-analysis-sources.md) governs
evidence; the [record contract](../instructions/agentic-analysis-records.md)
governs identity, fields, statuses and theory assessments.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-runtime-report.md` |
| `description` | Yes | Retrieval description naming the system and the runtime boundary traced |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's frozen revision or capture identity |

## Required sections

### Runtime account

`## Runtime account` traces the ordinary shipped invocation and every
material alternate or forcing route the runtime analyst selects. For
each material loop it identifies the trigger and principal, identities,
next-step owner, decision policy and representational form, context,
state, executor and effect boundary, runtime-client controls, persistence,
coordination and return, recovery, and terminal output. A load-bearing
guarantee also names its owner, enforcement point, guarantee strength,
covered and alternate paths, required external contract, and separate
conclusion-status fields.

The account links to the route records for decision roles, answer oracles,
operating modes and admission mechanisms, and to component records for
model mutability. Those fields follow the shared record contract.

The account distinguishes inspected implementation from supplied execution
evidence. Without supplied traces or experimental results, operation,
activation and benefit remain unobserved. Missing execution evidence does
not establish absent behavior.

### Shared records

`## Shared records` contains this member's declarations under all six kind
headings in the template. An empty kind says `none declared in this member`.
Every record follows the shared record contract, including its conditional
admission and theory fields.

### Annotations

`## Annotations` holds only runtime-specific fields on records declared
elsewhere, as `#### On MEM-RTE-memory-read — Short label`: admission and theory
fields, decision roles, operating mode, answer oracle and links to
runtime-declared records. It repeats no generic identity, evidence passage
or memory finding. Ordinarily this section says `none`: the runtime is
written before the other analysts declare records. A correction round can
add later-needed runtime fields and correct this member's findings.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} runtime report

## Runtime account

## Shared records

### Components

### Operative objects

### Routes

### Claims

### Evidenced absences

### Behavioral-authority paths

## Annotations
```
