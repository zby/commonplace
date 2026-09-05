---
type: kb/types/type-spec.md
name: agent-memory-analysis-report
description: "Memory specialist's source-grounded findings, classifications and integration questions for one agentic-system analysis run"
schema: ./agent-memory-analysis-report.schema.yaml
---

# Agent memory analysis report

The memory specialist's complete analytical handoff to the orchestrator. It
describes memory mechanisms and proposes their normalized classifications.
It is not a published system review or independent approval of the main result.

## Identity and retention

Write `memory-report.md` inside the parent's
`kb/reports/state/agentic-system-analysis/<run-id>/` directory. The parent
consumes this file before writing the integrated result. Retain it with
`memory-input.md` for local completion verification; do not delete either at
publication cleanup. The workflow owner may remove the whole local run when
its operational verification is no longer needed. Public consumers read the
retained main result, which must contain every adopted finding, limitation and
integration decision without requiring these local files.

Required frontmatter:

| Field | Meaning |
|---|---|
| `type` | `kb/reports/types/agent-memory-analysis-report.md` |
| `description` | Subject and discriminating memory boundary |
| `analysis-run` | Parent `AAS-*` run ID |
| `source-identity` | Exact parent repository or capture identity |
| `reviewed-boundary` | Parent full Git commit or capture label |
| `report-status` | `complete` or `blocked` |
| `canonical-register-sha256` | SHA-256 of the exact commissioned `memory-input.md` |
| `worker-model` | Actual worker model identifier, or `unknown` |
| `method-sha256` | SHA-256 of the specialist `analyse-agent-memory/SKILL.md` used |
| `memory-comparison` | Proposed scope and all fourteen axes using the main-result comparison contract |

A complete report can contain explicit unknown classifications. A blocked
report names missing access, changed input, or an unresolved scope decision
that prevents completing the assigned analysis. It still keeps all sections;
unreached axes use explicit uninspected assessments rather than guessed values.

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
quote blocks with full-commit path/URL attribution (or frozen capture identity).
The source text, not a line number, is matched at publication; the parent
retains it once on the corresponding canonical record. A complete report must
contain quote anchors; that minimum does not certify every claim's support. Do not turn source claims into implemented or observed behavior.

### Shared records

Use relevant parent canonical IDs with short source-native descriptions,
evidence anchors and memory-specific fields. Do not copy the entire runtime
inventory. New records use local IDs such as `MEM-OBJ-1` or `MEM-RTE-1`;
these are proposals and never reassign a canonical ID. Write every ID in full in lists; no abbreviated suffixes or ranges. Records distinguish
operative parts, raw and derived forms, their storage, lineage, consumers,
authority, and limits. A route identifies trigger, producer or selector,
retained input, persistence, delivery, later consumer and status.

### Write side

Trace acquisition, authoring, automatic transformation and maintenance. For
trace-fed transformations, show the raw-to-derived-to-later-consumer chain,
including alternative checkpoint forms. Give task/project horizons and timing
only when established by that route. Link to the shared records rather than
repeating their full artifact classifications.

### Read-back

Identify the later consumer, selection operation and delivery channel for each
route. Distinguish requested reads from automatic supply, API affordance from
wiring, and delivery from activation or benefit. A storage method alone does
not establish a consumer route. Record targeting inputs, budgets and authority
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
report may contain supported correction proposals; a required unresolved
decision is blocking. Side-channel messages never substitute for this section.

### Limitations and checks

Name prevented conclusions, source and method identity rechecks, and the
deterministic validation result. A self-check does not attest independence or
correctness of the final integrated analysis. Do not omit weaknesses to make
the report appear ready for integration.

## Integration contract

The orchestrator verifies run/source/input identity and report bytes, reads
the report, registers proposals, and records the ID mapping and issue
dispositions in the main result. Adopted classifications retain their evidence
and uncertainty. A substantive disagreement goes back to the specialist with
the conflicting evidence or is retained as explicit uncertainty; the parent
does not silently strengthen it. Any changed input is a fresh handoff. After
integration the main result is authoritative for downstream consumers.
