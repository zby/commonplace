# Refresh the agent-memory analysis corpus

## Commission and scope

The operator commissioned this workshop on 2026-09-26 to rerun all existing
agent-memory-system analyses through
[`analyse-agentic-system`](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md),
refreshing their sources and checking that the resulting corpus still supports
statistics and summaries. The first execution is a small pilot; expansion
returns to planning after its analysis and downstream checks are recorded.

The initial inventory contains 162 current legacy review artifacts: 155 under
`kb/agent-memory-systems/reviews/` and seven under `lightweight/`. Four files
whose names contain `.replaced.` are historical predecessors, not four extra
systems to analyse. These are artifact counts, not a claim of 162 distinct
source identities. [Inventory](./inventory.csv) retains all 166 entries so
every exclusion and subsequent disposition is visible.

New analyses publish generated reviews under `kb/agentic-systems/reviews/`
and exact results under `kb/reports/retained/agentic-system-analysis/`.
Legacy reviews and their old CSV, table, and syntheses remain historical.
Refreshing coverage means supplying new source-grounded evidence, not editing
old findings or substituting paths in existing evidential citations.

## Authority and coordination

This commission authorizes the workshop and its navigation entry, analysis
runs and their skill-owned publication paths, and bounded comparison and
synthesis trials. The operator subsequently authorized adopting per-value evidence and committing
the completed adoption and pilot work. No source
worktree is changed. Fetch current upstream objects and freeze a full commit
or immutable document capture for each run.

The workshop coordinator owns the inventory, scheduling, downstream checks,
and recovery. Each analysis receives a fresh coordinator context containing
only source identity, output ownership, and method instructions. Do not pass
legacy descriptions, findings, matrix values, or previous results to that
coordinator or its mandatory fresh memory specialist. Source identifiers
extracted from old records are discovery hints; verify them before freezing.
Prior-analysis exposure requires a new coordinator and run, as the skill says.
Do not use agent-status listings, including filtered listings: they may include
complete earlier reports. Use completion events and owned report paths instead.

One coordinator owns one run, one public destination, and one retained result.
Workers may delegate the mandatory memory lens, but do not share publication
destinations. Reserve capacity for that specialist before launching another
coordinator. In this pilot two active coordinators prevented a fresh specialist
launch (`agent thread limit reached`). Making one coordinator idle allowed a
fresh specialist launched by the parent to run; source isolation was retained.
Use one active coordinator plus its specialist until capacity is demonstrated.
The parent reconciles workshop status from validated completion,
not from an agent's statement that a draft is finished.

The existing [consumer migration workshop](../agentic-analysis-consumer-migration/README.md)
owns migration of downstream procedures. The
[analysis-method workshop](../analyse-agentic-system/README.md) owns method
construction. This workshop owns corpus refresh and acceptance observations;
record a discovered shared-method or consumer defect here and coordinate its
repair with that owner. Do not repair missing evidence by patching a generated
review or retained result independently.

## Inventory and execution

The inventory records legacy path, legacy tier/date/revision, source hint and extraction
basis, candidate existing generated review, status, new run/review/result,
and disposition. Legacy tier is scheduling metadata, not a classification for
the new analysis. A same-source generated review is only a candidate until its
boundary, current method, source freshness, and complete publication are checked.
Several artifacts can refer to one repository while covering different systems
or subsystems; resolve this before combining rows or counting systems.

Statuses are `pending`, `running`, `complete`, `blocked`, and
`historical-predecessor`. A blocked row names what would unblock it. A complete
row names the validated new run and outputs. Out-of-scope and unreachable
targets receive explicit skill dispositions rather than disappearing.

The initial pilot selects Napkin, Mem0, and Dynamic Cheatsheet from the current
legacy population. This is a bounded workflow trial, not a representative
sample. Their source identities are known; their classification and findings
must be established afresh. Newly inspected evidence may justify a narrower
boundary, a different evidence tier, or an out-of-scope result. Such an outcome
is itself a pilot observation and may require another eligible target before
testing all downstream paths.

## Pilot acceptance and next decision

The [three-pilot citation-generation rerun](./citation-generation-rerun-20260927.md)
completed at commit `5057c874` and the fixed pins in its
[execution handoff](./next-pilot-test.md). All six authors used the generator;
121 requests succeeded, and all 186 final quote blocks match returned citations
unchanged. No quotation or range failures were observed. One prepare failure
on workflow identity formatting was corrected. Independent handoffs and the
bounded matrix, table and statistics checks passed. The report records the
reasoning-effort mismatch in four workers and the remaining trace gaps; this
is bounded evidence of reduced authoring friction, not a general zero-error
claim. Inventory pointers name the three new results.

All three pilot analyses have now been regenerated under the adopted per-value
evidence contract. The pilot passes: matrix, table, numerical analysis and
reproducible membership queries all read the same retained evidence. Wired
automatic writing and push are countable without upgrading weaker manual/pull
values; partial coverage preserves positives without asserting a complete set.
See the [per-value pilot acceptance record](./per-value-acceptance.md),
[query ledger](./per-value-query-ledger.md), and
[synthesis trial](./per-value-synthesis-trial.md).

[ADR 093](../../reference/adr/093-memory-comparisons-keep-evidence-per-value.md)
records the adoption. The first pilot's acceptance, query ledger and synthesis
remain historical. There are still 159 current legacy artifacts pending. Bulk
execution has not started; the next bounded batch should cover document-only
sources, duplicate legacy boundaries and a larger eligible statistical sample.

The reliability repairs commissioned after the [trace audit](./trace-audit.md)
completed on 2026-09-27. The [retained acceptance record](../../reports/retained/agentic-analysis-reliability-20260927/README.md)
contains the eight repair dispositions, fresh Napkin publication, verified
three-system comparison and synthesis, exact query replay, and trace recoveries.
The repair workshop is closed. That trial published Napkin run
`AAS-2026-09-27-napkin-01`; subsequent runs supersede it in the inventory. This is bounded
acceptance for expanding the refresh, not full-corpus completion. Scheduling,
Pond regeneration and the remaining 159 artifacts remain owned here.

After commit `2d5a9d9a`, the operator commissioned another
[three-system rerun and trace audit](./reliability-rerun-20260927.md) at the same
source pins. All three new runs completed; handoff, matrix, table and statistics
checks passed. The six-session audit records recovered citation errors and
remaining read truncation. The inventory points to these latest results;
earlier comparison and synthesis snapshots remain historical.

The operator then commissioned a [fresh three-pilot quote-verification
rerun](./quote-rerun-20260927.md) after the quote-matching migration and the
parser/source-identity fixes in `4a97ad71`. It holds the same source revisions
fixed and audits first-check failures as well as final publication. All three
pilots completed: 199 result/specialist quote blocks and two compact-review
quote blocks pass the stronger checks. Five failed source-check attempts were
repaired before publication; authoring is not error-free. The audit records
two remaining instruction/validator inconsistencies. The bounded matrix,
table and statistics checks pass, and the inventory points to these new runs.
The follow-up [root-cause analysis](./source-check-root-causes.md) traces the
failures to specialist contract delivery, citation construction and conflicting
validation rules; it records repair priorities without changing the producer.

After the 2026-09-27 cleanup regression showed every worker wrapping the
generator in a per-quote loop, `commonplace-quote` gained a `--selections`
batch mode (`e984a460`). The [quote-batch trial](./quote-batch-trial.md)
prepares three specialist-only reruns on the same frozen inputs to test
whether fresh specialists adopt it unprompted and make no quotation errors. The
[completed trial](./quote-batch-trial-20260928.md) audited failed attempts and
recovery: no quote-tool misuse failure was observed, but five oversized reads
were truncated and followed by narrower reads. Two quote batches returned
ambiguity responses, handled without parsing failures. All 66 final citations
resolved; that final check is separate from the execution-failure audit.

The [validator investigation](./validator-disagreements.md) reproduces the
competing citation grammars and source-context errors. It also confirms that
workers used the source checker: the shipped tools detect invalid citations
after drafting but do not construct them. The subsequent instruction fix
delivers the citation contract to specialists and aligns range optionality;
validator implementation remains unchanged.

The subsequent [citation-generation change](./citation-generation-change.md)
implements the clarified workflow, repairs the validator disagreements, and
removes the separate source-check operation. It records implementation acceptance
and the command-count/simplification audit; the completed authoring trial is
recorded separately in the citation-generation rerun above.

The pilot is accepted only when:

1. Each selected analysis completes the current workflow, including both
   lenses, fresh memory report, source-checked quotations, canonical comparison
   fields, publication, and verified handoff; or records an explicit blocker
   or out-of-scope disposition.
2. An explicit list of completed pilot reviews produces a CSV and rendered
   table through the existing scripts. Every selected row retains source,
   boundary, tier, result identity, and comparison assessments. No legacy
   fallback or denominator substitution is permitted.
3. The statistics command runs against the same list. Mechanical spot checks
   recover the normalized fields from the retained results, separate evidence
   tiers and uncertain assessments, and reproduce selected counts.
4. A frozen synthesis bundle yields a short, bounded summary. Its quantitative
   claims have executable queries and its qualitative examples cite canonical
   result records. Bundle verification checks current input bytes. Public
   full-corpus outputs are not replaced by a three-system trial.
5. A missing/ineligible input is rejected without partial replacement. Record
   what was tested, defects encountered, and what remains untested, including
   historical-statistic equivalence and document-only coverage if applicable.

“The same stats and summaries” means retaining the ability to produce the
comparison matrix, human-readable table, axis distributions, coverage,
entropy/redundancy diagnostics, and evidence-grounded synthesis. It does not
mean reproducing old numerical values: sources, population, scope, and evidence
contracts have changed. Record unsupported former outputs explicitly instead
of inventing replacement values.

With the per-value evidence limitation resolved, choose
the next bounded batch from uncovered cases and observed
cost or failures. Before broad execution, resolve any defect that would corrupt
published evidence or comparison counts. If the pilot passes, schedule the
remaining inventory under the same source-only and output-ownership rules;
document-only targets and multiple legacy boundaries sharing one repository
need explicit coverage. The workshop schedules the remaining artifacts in bounded batches.

## Closure

Close when every current inventory entry has a completed new analysis or an
explicit accepted exclusion/blocker, duplicate source boundaries are resolved,
and the agreed refreshed corpus produces validated comparisons and synthesis
with disclosed coverage. Retain independently useful acceptance evidence and
publish the final library outputs, then delete this workshop and remove its
Active Workshops entry. Do not retire historical evidence merely to close it.

The retained corpus and its generated reviews were archived on 2026-09-28
(`kb/reports/retained/agentic-system-analysis-archive/`,
`kb/agentic-systems/reviews-archive/`) so that current data holds only sets
produced under the member-set method. The first refresh batch under that
producer is prepared in [batch-01-handoff.md](./batch-01-handoff.md):
Agent-S, MemoryOS and basic-memory, run in parallel where capacity allows.
Its preflight stops until the member-set producer lands.

The first run of batch 01 (branch `refresh-batch-01`, commit `a39ba9be`)
published all three sets in the layout that preceded the directory-artifact
output. Its friction record led to the method fixes landed on 2026-09-28;
its sets are superseded, not migrated, and the branch is not merged. The
operator chose to rerun the batch: [batch-01-rerun-handoff.md](./batch-01-rerun-handoff.md)
reruns Agent-S, MemoryOS and Basic Memory two at a time, and
[batch-02-handoff.md](./batch-02-handoff.md) follows with OS-Copilot,
A-mem and HippoRAG after the rerun is merged.
