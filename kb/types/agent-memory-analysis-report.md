---
type: types/type-spec.md
name: agent-memory-analysis-report
description: "Memory specialist's source-grounded findings, classifications and integration questions for one agentic-system analysis run"
schema: ./agent-memory-analysis-report.schema.yaml
---

# Agent memory analysis report

The memory specialist's complete analytical handoff to the orchestrator. It
describes memory mechanisms and proposes their normalized classifications.
It is not a published system review or independent approval of the main result.

## Identity and retention

The report is `memory-report.md` inside the parent's
`kb/reports/state/agentic-system-analysis/<run-id>/` directory, beside the
frozen `memory-input.md` it answers. It is local provenance for the main
result, which carries every adopted finding without requiring it.

Required frontmatter:

| Field | Meaning |
|---|---|
| `type` | `types/agent-memory-analysis-report.md` |
| `description` | Subject and discriminating memory boundary |
| `analysis-run` | Parent `AAS-*` run ID |
| `source-identity` | Exact parent repository or capture identity |
| `reviewed-boundary` | Parent full Git commit or capture label |
| `report-status` | `complete` or `blocked` |
| `canonical-register-sha256` | SHA-256 of the exact commissioned `memory-input.md` |
| `worker-model` | Actual worker model identifier, or `unknown` |
| `method-sha256` | SHA-256 of the specialist instruction `kb/instructions/analyse-agent-memory.md` used |
| `memory-comparison` | Proposed scope and all fourteen axes using the main-result comparison contract |

A blocked report names missing access, changed input, or an unresolved scope
decision that prevents completing the assigned analysis. It still keeps all
sections; unreached axes use explicit uninspected assessments rather than
guessed values.

## Report sections

### Boundary and evidence

Name the subject, frozen source boundary, included and excluded memory
surfaces, inspected paths and evidence layers, access gaps, and conclusion
limits. The input digest identifies the exact register supplied by the parent.
Keep enough source identity and scope here to understand the report alone.

### Core ideas

Describe the few mechanisms that distinguish how retained material affects
later work, including context selection and budget, source trust, and material
editing/adoption surfaces. Findings carry primary-source anchors and evidence
status. Load-bearing findings retain minimal verbatim source code or prose in
quote blocks under the main result's
[Source register](./agentic-system-analysis-result.md#source-register)
contract, which fixes the attribution grammar and the occurrence rule. A
complete report contains at least one quote anchor; that minimum does not
certify every claim's support.

### Shared records

Use relevant parent canonical IDs with short source-native descriptions,
evidence anchors and memory-specific fields. Do not copy the entire runtime
inventory. New records use local IDs such as `MEM-OBJ-1` or `MEM-RTE-1`;
these are proposals and never reassign a canonical ID. IDs follow the main
result's [Canonical identity](./agentic-system-analysis-result.md#canonical-identity)
rules, written in full in every list. Records distinguish operative parts,
raw traces from derived memory, content from access metadata, opaque payloads
from their readable display summaries, and give storage, representational
form, lineage, consumers, authority at the actual consumer, and limits. A
route identifies trigger, producer or selector, retained input, persistence,
delivery, later consumer and status.

Declare each proposed record with a heading such as `### MEM-OBJ-1 — Label`.
Use only `MEM-CMP-*`, `MEM-OBJ-*`, `MEM-RTE-*`, `MEM-CLM-*`, `MEM-ABS-*` or
`MEM-BAP-*`; evidence does not create a separate `MEM-EVD-*` kind. Put source
support on the appropriate record. For prose references, use `The object
MEM-OBJ-1 ...` and `Evidence: SRC-1 ...`, keeping ID-leading lines for declarations.

### Write side

Trace acquisition, authoring, automatic transformation, maintenance,
rejection and withdrawal, separating manual authoring, automatic acquisition,
and automatic operations over already retained material. For trace-fed
transformations, including compaction, show the raw-to-derived-to-later-consumer
chain, including alternative checkpoint forms. Give task/project horizons and timing
only when established by that route. State whether derived behavior-shaping
material retains its reasons and whether a later route reads them. Link to the
shared records rather than repeating their full artifact classifications.

### Read-back

Identify the later consumer, selection operation and delivery channel for each
route. Distinguish requested reads from automatic supply, API affordance from
wiring, and availability, delivery, activation and demonstrated benefit. A
storage method or an API with an unspecified hypothetical caller establishes
only a storage capability, not a consumer route; a documented external
consumer role may establish an afforded route without deployed wiring. A push
route names its automatic selector's trigger, inputs, selected parts, budget
and consumption channel. Record targeting inputs, budgets and authority
where they affect a conclusion.

### Comparison rationale

Explain non-obvious mappings and unions in `memory-comparison`. The vocabulary,
assessment and evidence-basis rules are those of the main result's Memory
comparison fields; use local proposal IDs until the parent registers them.
Every known value references supporting records; limitations prevent
unsupported complete sets. The same memory boundary applies across the report
and profile. No legacy token-line encoding or matrix fallback is permitted.

### Integration issues

List every proposed record, correction to a supplied fact, and unresolved
question with its evidence and analytical consequence. Identify the proposed
record kind and referenced IDs so the parent can assign canonical IDs without
rediscovering its meaning. State `none` when no issues remain. A complete
report may contain supported correction proposals and justified unknown
classifications; an unresolved question that prevents integration sets
`report-status: blocked`. Side-channel messages never substitute for this section.

### Limitations and checks

Name prevented conclusions, source and method identity rechecks, and the
deterministic validation result. A self-check does not attest independence or
correctness of the final integrated analysis. Do not omit weaknesses to make
the report appear ready for integration.
