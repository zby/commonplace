---
type: types/type-spec.md
name: agentic-system-runtime-report
description: "Runtime member of an analysis set: runtime account, probe evidence, the canonical records the runtime analyst declares, and its annotations on other members' records"
schema: ./agentic-system-runtime-report.schema.yaml
---

# Agentic system runtime report

The runtime baseline: traced invocations and alternate/forcing routes,
execution preflight and probes, and records under unprefixed IDs. It is
written before the two specialist members and remains unchanged afterward.
The [source contract](../reference/agentic-analysis-sources.md) governs
evidence; the [record contract](../reference/agentic-analysis-records.md)
governs identity, fields, statuses and theory assessments.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-runtime-report.md` |
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

For every focused test or probe the runtime analyst selects, the
account contains one execution-preflight record:

`check ID | intended conclusion | command, test, or script identity | required dependencies and authority | availability evidence | execution disposition: ran or not run | execution outcome or non-execution reason | conclusion prevented`

Each check ID is unique inside the run. Execution disposition is separate
from conclusion status. `not run` does not mean a failed check or absent
system behavior, and supports no negative finding; a command attempt that
stops before the target check executes leaves the target check `not run`.
When no dynamic check was selected, state `no dynamic check planned` and
list the checks considered and why static evidence was sufficient.

### Probe evidence

`## Probe evidence` contains one capsule per executed check, or `none`:

`source ID | check ID | UTC execution time | evidence layer | intervention and comparison, or none for an observational run | fixture or input identity | exact command, test node, or reusable-script identity | relevant environment | execution outcome and exit status | raw output inline, or resolvable exact-output location plus byte length and SHA-256 | design and confounding limits | exact conclusion supported and affected canonical IDs`

The check ID joins the capsule to its preflight record. Fixture or input
identity uses an immutable revision or byte length and SHA-256 when
content is not already canonical. Record a command verbatim; identify a
reusable script by path plus immutable revision or SHA-256. The relevant
environment names the runtime, tool, package, and service versions and
non-secret configuration needed to interpret the result, and records only
credential availability, never credential values. A `causal experiment`
capsule includes an actual intervention and comparison; otherwise the
capsule is `observed run` evidence. A digest without resolvable retained
bytes may identify missing output but cannot by itself support an
`observed` or `causally supported` conclusion. The capsule stays inline.

### Shared records

`## Shared records` contains this member's declarations under all six kind
headings in the template. An empty kind says `none declared in this member`.
Every record follows the shared record contract, including its conditional
admission and theory fields.

### Annotations

`## Annotations` holds only runtime-specific fields on records declared
elsewhere, as `#### On MEM-RTE-10 — Short label`: admission and theory
fields, decision roles, operating mode, answer oracle and links to
runtime-declared records. It repeats no generic identity, evidence passage
or memory finding. Ordinarily this section says `none`: the runtime is
written before the other analysts declare records. Reconciliation attaches
any later-needed runtime fields and amends this member's findings.

## Template

```markdown
---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} runtime report

## Runtime account

## Probe evidence

## Shared records

### Components

### Operative objects

### Routes

### Claims

### Evidenced absences

### Behavioral-authority paths

## Annotations
```
