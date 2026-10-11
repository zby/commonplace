# Evidence base

What evidence exists for the governing question, what each kind can show, and
what it cannot. Use audit findings with their run and coverage limits intact.
Separate incorrect claims, missing necessary conditions and material scope
omissions from optional additional coverage. More findings or more reviewers
alone do not show an improvement. The audit workshop's multi-report standard
governs general claims about recurring method weaknesses.

## Frozen source worktrees

The frozen checkouts under each run's `related-systems/<owner>--<repo>/` are
the primary evidence for coverage. Audits of traces and records show what
workers did; only the source shows what they did not reach. Every coverage
claim in this workshop must name the run, its `source-revision`, and the
paths read.

A coverage audit reads the source, not the analysis, within a bounded module
set, and reports mechanisms the records miss with anchors, plus whether the
record declared the gap as untraced. It is a different commission from the
correctness and trace audits retained so far, and it is requested through the
[audit evidence workshop](../analysis-audit-evidence/README.md) under its
standard. Its own reading cost is part of what this workshop weighs.

## Retained audits

The audit workshop holds five reports: Napkin, two Graphiti runs, Letta and
Letta Code. They are correctness, publication-byte and trace audits. None was
commissioned as a coverage audit, so none supplies a coverage denominator or
an estimate of completeness. Both Graphiti reports do contain source-backed
findings of omitted mechanisms, such as server-wired MCP instructions and a
bulk-ingest index consumed by provenance retrieval. That is selected omission
evidence: it shows the kind of mechanism the method can miss and what the
omission cost, without showing how much was missed. The audits also supply
evidence on recovery cost, masked command failures, quotation repair and
timing, which bear on the production side of resource allocation.

## Trace measurements

The retained
[code navigation trace audit](../../reports/retained/analysis-worker-code-navigation-trace-audit-2026-10-11.md)
of 2026-10-11 counts source reads across 36 worker invocations in four runs,
all on `gpt-6.1-sol` at medium. Its finding: workers already search and use
bounded reads; the observed need is better target selection and cross-file
navigation, not replacing whole-repository reading. Its per-run read counts
are the available measure of how the current method spends investigation
effort, and the first deliverable should use them rather than reason from
contracts alone. Counts are calls, not unique files, tokens or cost.

## Deterministic measurements this workshop may add

Within scope, writing only under this workshop:

- For each retained run, the set of source paths anchored by the runtime
  record's shared records, and the share of memory and epistemic anchors
  outside that set. This tests whether runtime-located paths are a tight
  enough bound for lens verification.
- For each retained run, verification findings addressed to runtime coverage,
  by materiality. This tests how often the general map is found incomplete
  after lenses have scoped from it.
- Read counts per role from the navigation audit, as the baseline allocation.

Record run id, method commit and source revision with every measurement. Do
not pool runs across method revisions to estimate a rate.
