# ASISAS-2026 Experiment Scripts

Scripts in this directory operate only on the frozen ASISAS-2026 experiment snapshot.

- `build_systems_matrix.py` reads `../reviews/`, `../karpathy-gist-agent-memory-reproducible-core.md`, and the prior `../systems.csv`; it writes only `../systems.csv`.
- `systems_matrix_frozen.py` is the experiment-local parser snapshot. Do not replace it with an import from `commonplace.lib.systems_matrix`; the point of this copy is to keep the experiment reproducible when the living parser changes.
- `render_systems_table.py` reads only `../systems.csv` and writes only `../systems-table.md`.

Run from the repository root:

```bash
python3 kb/agent-memory-systems/asisas-2026-experiment/scripts/build_systems_matrix.py
python3 kb/agent-memory-systems/asisas-2026-experiment/scripts/render_systems_table.py
```

Use the root `scripts/build_systems_matrix.py` for the living `kb/agent-memory-systems/` matrix.
