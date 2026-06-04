#!/usr/bin/env python3
"""Render the human-readable comparison table from systems.csv.

Emits kb/agent-memory-systems/systems-table.md: a sortable (in the MkDocs HTML
build) GFM table over the code-reviewed systems, plus a short summary of the
dimensions. Generated, not hand-maintained -- rebuild after systems.csv changes:

    python3 scripts/build_systems_matrix.py    # refresh the matrix first
    python3 scripts/render_systems_table.py    # then re-render this table

Only the columns the matrix fills reliably enough to compare across the whole
population earn a place (see scripts/analyze_matrix.py). Representational-form
component columns stay in the raw matrix while the lead-token retrofit proceeds.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COLLECTION = REPO_ROOT / "kb" / "agent-memory-systems"
SYSTEMS_CSV = COLLECTION / "systems.csv"
OUT = COLLECTION / "systems-table.md"

# Display columns: (header, csv field). System name is handled separately (linked).
COLUMNS = [
    ("Storage substrate", "storage_substrate"),
    ("Read-back", "read_back_direction"),
    ("Push engineered", "push_engineered"),
    ("Trace-derived", "trace_derived"),
]

FRONTMATTER = """\
---
description: "Auto-generated sortable comparison table of the code-reviewed agent memory systems across the matrix fields filled reliably enough to compare — storage substrate, read-back direction, engineered push, and trace-derived learning. Rebuild with scripts/render_systems_table.py."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---
"""

SUMMARY = """\
# Agent memory systems comparison table

A sortable view of the code-reviewed systems in this collection, generated from
[`systems.csv`](./systems.csv). Lightweight (doc-only) reviews are excluded — a
comparison table is for *choosing* a system, and that calls for code-grounded
evidence. Click any column header to sort (in the rendered HTML site; on GitHub
the [raw matrix](./systems.csv) is itself a sortable, searchable viewer).

For the architectural deep dive behind these axes, see the
[comparative review](./agentic-memory-systems-comparative-review.md).

## How to read the columns

- **Storage substrate** — where memory physically lives: plain files, a git repo,
  SQLite, an RDBMS, a vector or graph store, key-value, in-memory, or model
  weights. It sets the operational floor — inspectability and diffability at one
  end, scale and query power at the other. Files-family still leads, but a third
  of systems are database-backed, and the most common database is plain SQLite,
  not a vector or graph store.
- **Read-back** — how remembered material reaches the next action: the agent
  *pulls* it with an explicit lookup, the system *pushes* it in unasked, or
  *both*. This is the first question to ask, because it decides whether the agent
  has to remember to look or whether context arrives on its own.
- **Push engineered** — whether the system has actually built a relevance-gated
  path that injects memory *before* the agent acts. Pull-only systems never have
  one by definition; about half of all systems do.
- **Trace-derived** — whether memory is mined automatically from the agent's own
  execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems are trace-derived — and they overwhelmingly push or
  do both, so automatic learning and automatic activation tend to ship together.

Representational form is omitted from this compact view while the component
one-hot retrofit proceeds. The raw matrix carries `form_prose`, `form_symbolic`,
and `form_parametric` columns.
"""


def rel_link(review_file: str) -> str:
    """Path of a review relative to the collection root (where this page lives)."""
    prefix = "kb/agent-memory-systems/"
    rel = review_file[len(prefix):] if review_file.startswith(prefix) else review_file
    return "./" + rel


def main() -> int:
    with SYSTEMS_CSV.open(encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if r.get("source_tier") == "code-grounded"]
    rows.sort(key=lambda r: r["system_name"].lower())

    headers = ["System"] + [h for h, _ in COLUMNS]
    lines = [FRONTMATTER, SUMMARY, "", f"## The systems ({len(rows)} code-reviewed)", ""]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for r in rows:
        name = r["system_name"].strip() or Path(r["review_file"]).stem
        cells = [f"[{name}]({rel_link(r['review_file'])})"]
        cells += [(r[field].strip() or "—") for _, field in COLUMNS]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
