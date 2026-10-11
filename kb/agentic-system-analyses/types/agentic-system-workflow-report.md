---
type: types/type-spec.md
name: agentic-system-workflow-report
description: "Workflow member of an analysis set: one source-grounded multi-step agent workflow, its delegation, verification, recovery and delivery mechanisms"
schema: ./agentic-system-workflow-report.schema.yaml
record-prefix: WF-
---

# Agentic system workflow report

This lens explains how a multi-step agent workflow reaches delivery, rather
than cataloguing runtime capabilities. The [record contract](../instructions/agentic-analysis-records.md)
governs its records and evidence. It characterizes the source system, not its
fit for Commonplace.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-workflow-report.md` |
| `description` | Yes | System and workflow boundary traced |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's frozen revision or capture identity |

## Workflow account

The account traces one representative source-supported workflow from request
to delivered result, naming why it was selected. It explains who delegates
what to whom, what each handoff supplies, what verification can accept or
reject, who recovers from failure, and what makes the result delivered.
These mechanisms need not all exist: distinguish unsupported or uninspected
steps from evidenced absence. Keep evidence limits beside the affected claims;
shipped instructions or code do not establish successful execution.

When no multi-step workflow can be established, state the inspected boundary,
what is missing and which conclusions cannot be drawn. Do not invent a
workflow by joining unrelated capabilities. The account is selective, not an
exhaustive workflow inventory or a reliability score.

## Records and annotations

Declare only newly established records under `WF-`; cite supplied runtime
records and put workflow-specific fields on them in Annotations without
repeating their identity or evidence. Empty record kinds say
`none declared in this member`; empty Annotations says `none`.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of {system} at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} workflow report

## Workflow account

## Shared records

### Components

### Operative objects

### Routes

### Claims

### Evidenced absences

### Behavioral-authority paths

## Annotations
```
