---
type: types/type-spec.md
name: agentic-system-reconciliation-report
description: "Reconciliation member of an analysis set: connections between the analyst reports, duplicate supersessions, anchored conflicts and integration dispositions"
schema: ./agentic-system-reconciliation-report.schema.yaml
---

# Agentic system reconciliation report

The retained reconciliation of the runtime, memory and epistemic members.
It states how their records connect and where the reports disagree. It does
not judge one report's support and does not correct a report: the record
verifier judges, and the declaring analyst corrects its own report. The
reconciler writes the whole member, and the accepted report enters the set
unchanged. The [record contract](../instructions/agentic-analysis-records.md) governs
supersessions; the [source contract](../instructions/agentic-analysis-sources.md)
governs evidence. The member declares no analyst records of its own.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-reconciliation-report.md` |
| `description` | Yes | Subject and frozen reconciliation boundary |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's immutable revision or capture identity |

## Reconciliation

The body contains `## Reconciliation`: duplicate supersessions, anchored
conflicts, independent convergence, analyst ownership checks and
integration-issue dispositions. Name full IDs and describe discrepancies
without selecting the strongest-sounding status. A supersession paragraph
starts `Amendment: <full record ID> is superseded by <full record IDs>` and
gives its identity evidence and affected findings. Both supersession IDs
stay declared in their original members. An `Amendment:` paragraph that
replaces a record's value is not accepted in a new set; sets published before
report correction can contain them.

A split supersedes a combined record only by parts already declared in the
analyst members. Reconciliation never allocates IDs or declares parts. A
valid container stays alongside its declared `Part of:` records; containment
alone is no reason to supersede it. If a required part is missing, retain an
`Unresolved conflict:` naming the combined ID, the missing part in prose,
evidence and prevented conclusion; the verifier addresses it to the analyst
who should declare the part.

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
type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
description: "Reconciliation of {system} records at {boundary}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} reconciliation

## Reconciliation
```
