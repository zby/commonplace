# Memory landscape query ledger

The executable queries behind the counts in the
[agent-memory landscape](../../kb/agentic-systems/comparisons/memory/agent-memory-landscape.md)
synthesis of 2026-10-22 (inputs commit `5f92f75e5`, matrix SHA-256
`d68ae228…`). Each script reads the memory matrix and prints the query
results the synthesis cites.

```bash
uv run python scripts/memory_landscape_queries/ledger.py [matrix.csv]
```

The matrix defaults to the public
`kb/agentic-systems/comparisons/memory/memory-systems.csv`. That file matched
the synthesis matrix's hash when the synthesis was written; after the tables
are regenerated, the counts describe the new population, not the synthesis.
`common.py` holds the loading, tier splits and the strong-basis rule (`wired`,
`observed`, `causally supported`); `ledger*.py` hold the queries;
`outputs-2026-10-22/` holds their output at that matrix. `axis.py` and
`rec.py` print one set's profile units and canonical records, for checking
examples.

These are working queries, not a stable interface. A later synthesis may
reuse or replace them.
