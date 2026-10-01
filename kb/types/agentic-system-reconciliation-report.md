---
type: types/type-spec.md
name: agentic-system-reconciliation-report
description: "Reconciliation member of an analysis set: record amendments, duplicate supersessions, anchored conflicts and integration dispositions"
schema: ./agentic-system-reconciliation-report.schema.yaml
---

# Agentic system reconciliation report

The retained reconciliation of the runtime, memory and epistemic members.
It settles records before public synthesis. Code writes its identity and
copies the accepted job's Reconciliation section; returned memory findings
remain working inputs and never enter this member. The [record
contract](../reference/agentic-analysis-records.md) governs amendments and
supersessions; the [source contract](../reference/agentic-analysis-sources.md)
governs evidence. The member declares no analyst records of its own.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/agentic-system-reconciliation-report.md` |
| `description` | Yes | Subject and frozen reconciliation boundary |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's immutable revision or capture identity |

## Reconciliation

The body contains `## Reconciliation`: amendments, duplicate supersessions,
anchored conflicts, independent convergence, analyst ownership checks and
integration-issue dispositions. Name full IDs and resolve discrepancies
without selecting the strongest-sounding status. An amendment paragraph
starts `Amendment: <full record ID>` and gives its superseded value,
replacement, evidence anchor and affected findings. Both supersession IDs
stay declared in their original members.

Mark every conflict left unresolved with a paragraph starting
`Unresolved conflict:`, followed by the affected IDs, conflicting findings,
evidence and conclusion prevented. Record verification checks these markers;
synthesis must carry every unresolved conflict into its Limitations.
Properly scoped uncertainty is not itself a completion blocker.

All references resolve in the set. Member-relative links stay inside the
set directory, because publication moves it. This member contains neither
public synthesis nor verification text, and does not rewrite analyst reports.

## Template

```markdown
---
type: types/agentic-system-reconciliation-report.md
description: "Reconciliation of {system} records at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} reconciliation

## Reconciliation
```
