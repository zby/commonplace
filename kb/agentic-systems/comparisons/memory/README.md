# Agent memory comparisons and data

Investigate how retained information reaches later work, changes over time
and affects behavior. The [Agent Memory topic](../../topics/memory.md) introduces
the questions; this directory holds comparative research and dataset snapshots,
not copies of the individual analyses.

## Comparative research

[Agent-memory landscape](./agent-memory-landscape.md) compares admission,
read-back, curation and trace learning across 191 analyses. This is a frozen
synthesis dated 2026-10-22 at inputs commit `5f92f75e5`, not a continuously
updated survey or a representative sample of the field.

## Datasets and individual systems

- [Memory comparison table](./memory-systems-table.md)
- [CSV download](./memory-systems.csv)
- [Current memory accounts and profiles](./systems.md) — generated during each
  site build, linking the accepted memory members without copying them.

The table and CSV were generated on 2026-10-22 from all 191 analyses current at
commit `5f92f75e5`. Their population can differ from the build-time listing.
A row records a scoped finding, not a blanket property of the whole system.
Read evidence and coverage alongside the value.

## Method

[Methods & Data](../../methods.md) explains evidence interpretation.
[Comparison inputs and regeneration](../builds.md) owns population selection,
profile revision semantics and rebuild commands. Cross-system syntheses follow
the separately commissioned
[landscape synthesis procedure](../../instructions/synthesize-agent-memory-landscape/SKILL.md).

The [memory analyst job](../../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/analyse-memory.md)
traces retained objects and their later consumers in each frozen analysis.

[All comparisons](../README.md) · [Research Topics](../../topics/README.md)
