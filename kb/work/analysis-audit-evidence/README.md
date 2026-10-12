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
| [Letta analysis and trace audit](./reports/letta-analysis-and-trace-audit.md) | `AAS-2026-10-11-letta-d460b458ddad-01` | Supported blocked boundary, complete embedded worker trace, local byte checks and bounded timing comparison | Successful early stop; recurring quotation repair and late prerequisite read, with an unresolved operator-reporting gap |
| [Letta Code analysis and trace audit](./reports/letta-code-analysis-and-trace-audit.md) | `AAS-2026-10-11-letta-code-88afa3263646-01` | Publication-byte checks, selected source claims, failure-oriented scans of all twelve analytical worker traces and bounded timing comparison | No new substantive correction in the sample; successful profile repair, recurring quotation and shell-status failures, and timely publication-prerequisite read |
| [Napkin repeat analysis and trace audit](./reports/napkin-1b60c5d21780-repeat-analysis-and-trace-audit.md) | `AAS-2026-10-11-napkin-1b60c5d21780-01` | Same-source comparison, both sets of worker traces, byte checks and timing | Explicit denominator qualification and earlier evaluator qualification; retained-consumer and documented-delivery issues remain |
| [Graphiti repeat analysis and trace audit](./reports/graphiti-4896fccada9e-repeat-analysis-and-trace-audit.md) | `AAS-2026-10-11-graphiti-4896fccada9e-01` | Comparison with both prior same-source runs, all fifteen new worker traces and byte checks | Bulk-retention correction succeeds; provenance, saga and instruction qualifications remain; masked failures and transport recovery retained |
| [Letta Code repeat analysis and trace audit](./reports/letta-code-f54d2479889e-repeat-analysis-and-trace-audit.md) | `AAS-2026-10-11-letta-code-f54d2479889e-01` | Same-source comparison, all twelve new worker traces, byte checks and timing | Supported new mod-adaptation account, some old coverage lost; profile repair, masked validators and provider recovery retained |
| [Graphiti amendment-effects audit](./reports/graphiti-72c99440b180-amendment-effects-audit.md) | `AAS-2026-10-11-graphiti-72c99440b180-01` | Same-source result comparison, all thirteen analytical traces, amendment delivery/adoption and byte checks | Direct validation and path-only quotations adopted; path reconstruction persists; result gains and regressions coexist |
| [Napkin amendment-effects audit](./reports/napkin-28752ba411ea-amendment-effects-audit.md) | `AAS-2026-10-11-napkin-28752ba411ea-01` | Same-source result comparison, all fourteen analytical traces, amendment delivery/adoption and byte checks | Two prior result issues qualified; documented delivery remains partial; absolute handouts do not ensure exact reuse |
| [Letta Code amendment-effects audit](./reports/letta-code-9d060e7dab7e-amendment-effects-audit.md) | `AAS-2026-10-11-letta-code-9d060e7dab7e-01` | Same-source result comparison, all eighteen analytical traces, amendment delivery/adoption and byte checks | Semantic repairs supported; five reconstructed validator paths and one recovered out-of-scope identity write |
| [GBrain workflow-lens pilot check](./reports/gbrain-9de8e3c225d3-workflow-pilot-check.md) | `AAS-2026-10-11-gbrain-9de8e3c225d3-01` | Independent Sol check of workflow, cross-member agreement, source transitions and publication bytes; bounded trace sample | Proceed with retention and ten sequential analyses; connected workflow supported, runtime success and semantic success kept distinct |

The first Graphiti report compares its findings with Napkin at the same method commit
and worker profile. Masked command failures occurred and semantic review repaired
a candidate in both runs. These observations do not establish a method defect,
an error rate, or an adopted change. Multiple reviewers, findings, or retries
within one run do not constitute multiple independent runs.

## Repeat-run evidence after the coverage clarification

The three October 11 repeats above used method
`0275b8abb307039d0bc975b5699e5b86fe6ca1d5`, their prior source revisions and
pi-sol/medium. All published in isolated worktrees; the audits independently
checked publication bytes. All three report verifiers exercised consequential
omission questions and retained stopping explanations. Quality is mixed rather
than uniformly improved, and all three took longer than their comparators.
Concurrent runs, changed inspection scope, repair work and service failures
prevent causal claims about the method revision.

The failure-oriented scans cover 37 new analytical workers. They found seven
masked failed shell commands across Graphiti and Letta Code; Napkin had risky
wrappers but no demonstrated new masked failure. Four embedded model transport
errors across Graphiti and Letta Code recovered inside successful workers.
Thirteen failed validation invocations across the three runs also recovered;
these categories overlap and must not be summed as distinct incidents. No
publication-byte mismatch or demonstrated unauthorized analytical mutation was
found. This is bounded trace evidence, not an exhaustive correctness certificate.

Coordinator adjudication corrected a Graphiti audit false positive: the cited
relative output paths were supplied that way by the handout. The remaining issue
is rule/handout wording consistency, not demonstrated worker misrouting. Preserve
that distinction when considering changes. The reports make local correction
recommendations separately from method hypotheses; this comparison adopts no
further method change and authorizes no integration or frozen-result edits.

## Repeat-run evidence after the three operational amendments

On October 11 the operator commissioned monitoring the remaining runs every
five minutes, followed by another result-and-trace comparison focused on the
three amendments. Graphiti and Napkin were already complete at the initial
check. Letta Code was running at 16:54 and 16:59 UTC and reported
`publication-job-completed` at the 17:04 check. The audits then independently
checked publication bytes rather than treating engine completion as an audit.

All three new runs used method
`48453a8110bd36bc51fbcad3e9b2b394b694f603`, the same source revisions as their
comparators, and pi-sol/medium. They do not include the later workflow lens.
The relevant method changes from the preceding repeat were path-only quotation
attributions (`d823ef621`), direct validator calls (`4eed3876d`), and absolute
handout paths (`b38982da2`). All three changes were delivered together; these
are observational comparisons, not isolated causal tests.

**Recommendation: retain the amendments, but do not treat absolute path delivery
as enforcement of worker behavior.** The three reports above support different
conclusions for each change:

| Amendment | Observed operation across this batch | Limit |
|---|---|---|
| Path-only quotation attributions | Adopted in all three runs; the prior revision/attribution-format failures did not recur | Four quotation failures still required ambiguity or range repair; no semantic-correctness guarantee follows |
| Direct validation | All 60 validator calls were direct; all 11 failures propagated and recovered | Seven failures were incorrect artifact arguments, not content checks; risky non-validator shell constructions persist |
| Absolute handout paths | All 45 analytical workers received absolute filesystem bindings | Workers still shortened or reconstructed paths; seven validators used an invented artifact directory; Letta Code Memory briefly wrote an empty identity file outside its assigned handout |

The 60 validator calls comprise Graphiti 16, Napkin 18 and Letta Code 26;
the 11 failures comprise 2, 2 and 7 respectively. They divide into four
quotation failures and seven artifact-path failures, not independent incidents
to add to those totals. No demonstrated masked shell failure was found in the
190 inspected Bash results, versus seven in the preceding batch's audits.
Different inspected opportunities and lingering risky wrappers prevent a claim
that all shell failures are now visible. The strongest evidence is narrower:
actual validator failures now reach the worker as failures in all eleven cases.
Quotation occurrence counts differ in sampling across the reports and are not
pooled as independent trials.

The coordinator independently checked the Letta Code identity-write recovery
against its trace (report A4, L29/R0/m89–94): successful wrong-location write,
removal, then correct assigned write. No data loss is established, but recovery
does not erase the write-scope violation. The producer supplied the correct
path. This and the seven reconstructed validator arguments are worker errors,
not evidence of a defective absolute-path generator. Mere relative spelling
that resolved to the assigned file is recorded separately from misrouting.

Accepted-result quality remains mixed. The Napkin audit finds that the distill
create-example mismatch and saved-report/current-array confusion are now
qualified; documented automatic delivery remains partly underclassified.
The Graphiti audit retains successful bulk-retention and evaluator corrections,
but reconfirms provenance and saga-reset omissions, finds a context-count
regression, and catches another false verifier typo allegation. The Letta Code
audit supports the repaired concurrency, reflection and selector claims without
establishing a new accepted-claim correction in its sample; prior hook/Workflow
coverage is not fully replaced. These are bounded source checks, not exhaustive
correctness judgments or effects attributed to the operational amendments.

| Run | Previous → new wall minutes | Previous → new summed worker minutes | Previous → new analytical workers |
|---|---:|---:|---:|
| Graphiti | 65.68 → 71.60 | 68.63 → 74.83 | 15 → 13 |
| Napkin | 49.37 → 75.53 | 53.30 → 78.36 | 10 → 14 |
| Letta Code | 64.38 → 89.67 | 68.18 → 90.51 | 12 → 18 |

Each pair uses its report's timing boundary: Graphiti preparation record to
publication, Napkin run-start result to publication, and Letta Code preparation
call to publication. Do not pool these wall times as one identically measured
benchmark. Extra repair/review work, changed exploration and four recovered
provider interruptions accompany the new batch. Less quotation-format friction
did not produce lower total elapsed time; the evidence does not isolate the
amendments' contribution to cost or quality.

All three frozen-method set validations and report validations passed; all
three publications matched their receipts and pinned members. The reports
retain exact identities, trace locators, count definitions and limitations.
This comparison recommends no additional instruction or gate. Local correction
candidates remain separate decisions. No new analysis, integration, frozen
artifact edit, method edit, commit or worktree disposal is authorized by this
comparison. Broader graph discovery, if useful later, belongs to a separately
commissioned `cp-skill-connect` task.

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
