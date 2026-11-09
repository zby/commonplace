# Methods & Data

These analyses explain architectures at **frozen source boundaries**, not the
latest release of every project. Start with a system's overview, then its
boundary and synthesis. Follow the numbered records in its lens reports for
the evidence behind a conclusion.

## How the research is produced

The [analysis method](../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md)
coordinates source inspection, separate runtime, memory, knowledge and workflow
accounts, reconciliation and verification. The
[analysis-set contract](../agentic-system-analyses/types/agentic-system-analysis-set.md)
explains the accepted members and manifest. The
[Systems Directory](../agentic-system-analyses/current-analyses.md) is generated
from current accepted sets at each website build; their contents are not
rewritten for the site.

## Interpreting evidence

Documentation can **claim** a mechanism. Inspected code can show it is
**wired**; an exposed capability may only be **afforded** to a caller.
**Observed** execution, **measured** outcomes and evidence of **causal**
contribution answer different questions. A route through code alone does not
establish that a deployed agent used it or benefited from it.

Read the [record contract](../agentic-system-analyses/instructions/agentic-analysis-records.md)
for evidence classifications and the
[memory profile contract](../agentic-system-analyses/types/agentic-system-memory-profile.md#memory-comparison-fields)
for scoped comparison findings and coverage. Uninspected operation is not a
claim that a system has never been tested. Partial coverage is not absence.
The retained verification reports expose disagreements and remaining limits.

## What the evidence can settle

Design-space exploration asks more than whether a feature exists. It asks
which choices can vary, which combinations can work, what conditions limit
them, and what would justify choosing one over another.

- **Choices:** use inspected mechanisms to identify candidate dimensions.
  The current categories are a way to compare sources, not a claim that every
  relevant dimension has been found or that the dimensions are independent.
- **Combinations:** source inspection can establish that mechanisms are wired
  together within a stated boundary. Execution evidence is needed to show
  that the combination works under particular conditions. Separate features
  found in different systems do not establish their compatibility.
- **Constraints:** distinguish an operator requirement, an implementation
  limit, an observed failure and a hypothesized incompatibility. Keep each
  constraint's basis and scope beside it. Neither prevalence nor an empty
  comparison-table cell establishes necessity or impossibility.
- **Commitment:** state the decision, competing alternatives and evidence
  that could change the choice. A claim of benefit needs outcome evidence
  under relevant conditions, including cost and failure behavior; static
  wiring alone cannot supply it.

The [future-work agenda](./topics/README.md#future-work) turns these distinctions
into candidate comparisons and tests. It does not change the analysis
contracts or authorize experiments. Commonplace adoption judgments remain
separate from source-system accounts.

## Memory datasets and synthesis

- [Comparison table](./comparisons/memory/memory-systems-table.md) — inspect
  mechanisms and follow rows to their accepted analyses.
- [CSV download](./comparisons/memory/memory-systems.csv) — machine-readable
  findings, evidence bases, scope, profile revisions and artifact hashes.
- [Agent-memory landscape](./comparisons/memory/agent-memory-landscape.md) —
  a frozen synthesis of 191 analyses at inputs commit `5f92f75e5`, dated
  2026-10-22. Its counts describe that selected corpus, not the field.
- [Current memory accounts and profiles](./comparisons/memory/systems.md) —
  build-time listing; it can include analyses newer than the table or synthesis.
- [Population selection, interpretation and regeneration](./comparisons/builds.md) —
  the single operational reference for these datasets.
- [Landscape synthesis procedure](./instructions/synthesize-agent-memory-landscape/SKILL.md) —
  how a separately commissioned synthesis binds its population to a commit.
- [Taxonomy maintenance](./instructions/refresh-agent-memory-review-taxonomy.md) —
  maintenance of shared comparison terms.
- [Layout migration evidence](./reports/retained/layout-migration-2026-10-01/README.md) —
  historical path/hash mapping and acceptance checks.

The table and CSV are committed snapshots, not live queries. Their
[dataset landing](./comparisons/memory/README.md) identifies their generation
boundary. Profile revisions are not silently interchangeable. Neither the
selected population nor its counts are a representative sample of agentic
systems. There are no equivalent structured datasets for the other three
topics yet.

## Research scope

The primary research program charts the design space and seeks solutions
useful to Commonplace; this public resource makes the resulting evidence
reusable. Source-system findings stay separate from Commonplace adoption
judgments, as the [research design brief](../reference/agentic-system-analysis-design-brief.md)
requires. The [historical Agent Memory Systems collection](../agent-memory-systems/README.md)
remains available; its reviews and statistics are not the current population.
