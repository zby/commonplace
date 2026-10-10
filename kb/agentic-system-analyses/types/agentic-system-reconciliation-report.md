---
type: types/type-spec.md
name: agentic-system-reconciliation-report
description: "Reconciliation member of an analysis set: connections between the analyst reports, duplicate supersessions, anchored conflicts and integration dispositions"
schema: ./agentic-system-reconciliation-report.schema.yaml
---

# Agentic system reconciliation report

The retained reconciliation of the runtime, memory and epistemic members.
It states how their records connect and where the reports disagree. It does
not judge one report's support and does not correct a report: the report
verifier judges, and the declaring analyst corrects its own report. The
reconciler writes the whole member, and the accepted report enters the set
unchanged. The [record contract](../instructions/agentic-analysis-records.md) governs
supersessions and what its connections may claim from evidence. The member declares no analyst records of its own.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-reconciliation-report.md` |
| `description` | Yes | Subject and frozen reconciliation boundary |
| `run-id` | Yes | The set's run ID |
| `reviewed-boundary` | Yes | The set's immutable revision or capture identity |

## Reconciliation

The body contains `## Reconciliation`: duplicate supersessions, anchored
conflicts, independent convergence and integration-issue dispositions. Cite the records concerned and describe discrepancies
without selecting the strongest-sounding status. Each supersession is an
`Amendment:` paragraph in the record contract's grammar, which also says what
it must show and what a split or a missing part requires.

Mark every disagreement between reports with a paragraph starting
`Unresolved conflict:`, followed by citations of the affected records, conflicting findings,
evidence and conclusion prevented. The reconciler settles none of them: the
verifier addresses a blocker to the report that must change, and a conflict
the sources cannot settle becomes a limitation of the synthesis.

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
