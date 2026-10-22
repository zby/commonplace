# Memory lens

Cross-system pages for the memory member of each current
[agentic-system analysis](../../../agentic-system-analyses/README.md). The
member traces the memory and context mechanisms each system retains, the results they keep and the later consumers that read them back. Each analysis is frozen at its own source boundary;
the per-system accounts stay in their analysis sets, and this directory links
to them.

The analyst job that writes the member: [memory and context](../../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/analyse-memory.md).

Memory also has structured comparison fields in each set's memory profile.
The [comparison builds](../README.md) turn them into `memory-systems.csv` and
`memory-systems-table.md` in this directory; regenerate them after analyses
land, and read each table's selected population before relying on it.

Current tables: [memory-systems-table.md](./memory-systems-table.md) and
[memory-systems.csv](./memory-systems.csv), generated 2026-10-22 from all 191
current analyses at commit `5f92f75e5`.
Cross-system syntheses come from the
[landscape synthesis](../../instructions/synthesize-agent-memory-landscape/SKILL.md),
commissioned separately. Current synthesis:
[agent-memory landscape](./agent-memory-landscape.md), 2026-10-22, all 191
current analyses at inputs commit `5f92f75e5`.
