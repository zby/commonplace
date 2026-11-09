# Memory landscape query ledger

Executable queries and retained outputs behind the
[agent-memory landscape](../../kb/agentic-systems/comparisons/memory/agent-memory-landscape.md).
Use each dated output with its own evidence identity. Do not treat the mutable
public matrix as an older synthesis's input.

## Current snapshot: 2026-11-09

- Inputs commit: `bf2da04db03fb4cb60be52d1bb04e638a79eda79`.
- Selection: all 243 current accepted sets, no review filter; 225 code-grounded
  and 18 doc-grounded, all comparison revision 2.
- Builder-recorded matrix SHA-256:
  `19da70a6ca54b9c659dd9d1bf734e5f46885325d48f58b40685eccea083ce0bc`.
- `refresh.py` retains counts and membership/exclusions by revision and tier.
  It reuses `common.py`'s unit decoding and strong-basis rule: `wired`,
  `observed`, `causally supported`. Existence needs any strong witness;
  complete-value eligibility requires known axis coverage and every positive
  unit finding strong. Local trace-learning negatives remain distinct from
  system unions. All assessment categories are retained separately.
- `evidence.py` extracts selected members, canonical records, reconciliations
  and relevant profile units **from the inputs commit**. Identity comes from
  the query output, including matrix manifest hashes. Validate the selected
  directories before running it. It acquires no source and hashes nothing.
- `smoke.py` checks retained ledger structure and membership consistency,
  without rereading the matrix or independently recomputing its counts.

Pass the frozen matrix explicitly:

```bash
uv run python scripts/memory_landscape_queries/refresh.py \
  .commonplace/worktrees/gist-live-tests/cross-analysis-refresh-2026-11-09/memory-systems.csv
uv run python scripts/memory_landscape_queries/evidence.py
uv run python scripts/memory_landscape_queries/smoke.py
uv run ruff check scripts/memory_landscape_queries/refresh.py \
  scripts/memory_landscape_queries/evidence.py scripts/memory_landscape_queries/smoke.py
```

`outputs-2026-11-09/snapshot.json` retains the quantitative output, including
membership and exclusions. `evidence.py` reproduces the selected committed
excerpts when needed; duplicated excerpts and routine validation/lint logs are
not research inputs and remain local. Selected validation reported unavailable
source checkouts for some quotation checks; this snapshot does not authenticate
those upstream bytes.

To reconstruct later, use the inputs commit and its comparison reader to
produce the all-current matrix in a separate authorized workspace, then pass
that matrix explicitly. The ignored production path is not required to audit
published claims: the commit holds the retained members and reader, while
this directory retains selection, query logic, identities and outputs. Never
overwrite a dated output to represent a different population.

## Historical snapshot: 2026-10-22

`outputs-2026-10-22/` is preserved byte-for-byte. It belongs to inputs commit
`5f92f75e502f8cd11ec318d8e69d3e17cbe53df3`, matrix SHA-256
`d68ae22877ff7b34ae598ce423b0a0d8f325ca180aef29880b09226403ec07a5`.
The older `ledger.py` through `ledger5.py` remain historical working queries.
They default to the public matrix when no explicit path is supplied; rerunning
them after regeneration does not reproduce the historical output. They are
not the current snapshot's query ledger.

`axis.py` and `rec.py` inspect one set's profile units and canonical records.
These scripts are working research queries, not a stable public interface.
No change-over-time claim follows from the two dated outputs.
