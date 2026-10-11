# Analysis audit evidence

## Purpose and commission

Collect and compare audits of agentic-system analyses so that changes to the
analysis method respond to accumulated evidence, not the latest report.
The operator commissioned this workshop on 2026-10-11 after the Napkin audit.

The operator's working premise is that the process is stable enough to mostly
work. Remaining errors may be variable model behavior rather than defects in
the method. Treat that as the reason to gather evidence, not as a conclusion
that all remaining errors are random. More than one report is required before
using audit findings to justify general method changes.

The workshop should help a maintainer distinguish a local output error, a
recurring method weakness, an audit false positive, and a successful recovery.
It collects evidence and develops recommendations. It does not itself authorize
method edits, new analysis runs, integration, changes to frozen analyses, or
worktree disposal.

## Start an audit

Use [Audit an analysis](./audit-an-analysis.md) with the completed run and its
available session traces. It is a short audit commission, not a new analysis
workflow.

## Current evidence

| Report | Run | Contribution | Disposition |
|---|---|---|---|
| [Napkin analysis and trace audit](./reports/napkin-analysis-and-trace-audit.md) | `AAS-2026-10-10-napkin-b831630d0978-01` | Static correctness review and all 13 original worker traces | First case; findings and proposed improvements are not cross-run conclusions |
| [Graphiti analysis and trace audit](./reports/graphiti-analysis-and-trace-audit.md) | `AAS-2026-10-10-graphiti-5833fd846841-01` | Static correctness, publication-byte checks, all 12 analytical worker traces, and comparison with other Graphiti analyses | Second system; masked command failures and successful semantic repair have cross-run observations, not established method causes |
| [Graphiti 85a21a06d35c analysis and trace audit](./reports/graphiti-85a21a06d35c-analysis-and-trace-audit.md) | `AAS-2026-10-10-graphiti-85a21a06d35c-01` | Static correctness, same-revision comparison, all ten original worker traces and publication-byte check | Separate Graphiti run; local correction recommendation and bounded comparison with Napkin, no adopted method change |

The first Graphiti report compares its findings with Napkin at the same method commit
and worker profile. Masked command failures occurred and semantic review repaired
a candidate in both runs. These observations do not establish a method defect,
an error rate, or an adopted change. Multiple reviewers, findings, or retries
within one run do not constitute multiple independent runs.

## Working approach

The goal is a defensible decision about whether to retain or change the method.
Use a lightweight comparison rather than building a new reporting framework.
The particulars can evolve as reports arrive; the following evidence boundaries
must remain intact.

### Retain reports without turning recommendations into decisions

Save each supplied audit under `reports/` and add it to the table above. Record
`run-id`, `method-commit`, and `source-revision` under those exact keys. Also
retain the audit date, worker profile when known, audit scope, evidence locations,
and limitations. A local worktree path is a locator, not the run identity.

Separate what the audit observed from its interpretation and suggested changes.
Keep source and trace anchors for consequential findings. Preserve recovered
failures and successful checks as well as unresolved errors. Missing traces or
unaudited surfaces mean unknown, not successful or failed execution.

These are working copies of audit evidence, retained here at the operator's
request. They are not new authoritative characterizations of external systems
and must not become inputs to analysis workers. At closure, extract evidence
that needs durable retention to the appropriate reports collection.

### Compare mechanisms, not just labels

When another report arrives, compare findings by the operation that failed and
its conditions. For each proposed recurring issue, keep a small record of:

- Supporting report and finding IDs, distinct runs, method revisions, systems,
  and worker profiles.
- The claimed failure mechanism and plausible alternatives, including auditor
  error, ambiguous contracts, source-specific complexity, and model variability.
- Whether the existing process caught and repaired it, and at what cost.
- Relevant opportunities where the same mechanism worked or the error did not
  occur; say when those opportunities were not inspected.
- Impact on the accepted result, not merely the number of failed commands.
- Current disposition: accumulating evidence, needs adjudication, candidate for
  a bounded comparison, recommend no change, or ready for an operator decision.

Do not pool materially different method revisions without explaining why the
comparison remains valid. Several reviewers agreeing on one run strengthens a
local finding but does not demonstrate recurrence. Repeated reports alone do not
establish causation or an error rate; the inspected opportunities matter too.

### Return to decisions when evidence discriminates

Reassess after additional reports supply comparable cases. More than one report
is necessary, not sufficient, for a general method recommendation. Look for a
repeated mechanism, counterexamples, and a reason a proposed change would help
without damaging successful behavior. If variation and method weakness remain
indistinguishable, retain the uncertainty and propose a bounded comparison for
separate authorization rather than adding another instruction immediately.

A directly established defect in one retained analysis can be reported for a
separate correction decision without claiming a general method defect. Urgent
safety, integrity, or deterministic correctness concerns should be escalated
with their evidence; this workshop does not silently waive the operator's
multi-report requirement for method changes.

For any proposed change, state the expected benefit, added cost, what result
would count against it, and which evidence supports the recommendation. The
Napkin report's improvement list is a set of candidates for this process, not
an implementation backlog or an approved rerun.

## Relationship to existing work

The [analysis amendments workshop](../analyse-agentic-system-amendments/README.md)
contains existing correction designs and historical investigations. This
workshop owns the accumulation and comparison of audit reports, not those
implementation plans. Relevant historical reports may be considered when their
run identity, method boundary, and evidence are available; they do not count as
independent support merely because a previous workshop mentions them.

Before separately authorized method work, follow
[method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md).
The [analysis collection contract](../../agentic-system-analyses/COLLECTION.md)
governs frozen analyses and run-evidence identity.

## Closure

Close when the accumulated evidence has supported explicit dispositions of the
candidate issues—change, retain, or unresolved with an agreed disposition—and
the useful evidence and any adopted procedure have been extracted to durable
locations. An operator may instead end the investigation with no method change.
A fixed number of reports or an empty repair backlog is not the closure test.
Remove this workshop and its Active Workshops entry only after that extraction
or explicit disposition. Preserving a report here does not authorize deleting
its source worktree or session traces.
