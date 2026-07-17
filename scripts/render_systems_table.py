#!/usr/bin/env python3
"""Render the human-readable comparison table from systems.csv.

Emits kb/agent-memory-systems/systems-table.md: a sortable (in the ProperDocs HTML
build) GFM table over the code-reviewed systems, plus a short summary of the
dimensions. Generated, not hand-maintained -- rebuild after systems.csv changes:

    python3 scripts/build_systems_matrix.py    # refresh the matrix first
    python3 scripts/render_systems_table.py    # then re-render this table

This is the *human* view: scannable, one decision per cell. It deliberately
diverges from the raw matrix (systems.csv), which keeps the full one-hot flag
sets for authority, curation, and read-back signal. Here those collapse to a
single discriminating value each, and a plain-English "What it is" column is
pulled to the front — the thing a person surveying the landscape most wants and
the matrix buries. The full flag sets stay one click away in systems.csv.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COLLECTION = REPO_ROOT / "kb" / "agent-memory-systems"
SYSTEMS_CSV = COLLECTION / "systems.csv"
OUT = COLLECTION / "systems-table.md"

# Read-back targeting collapses the signal one-hots to one human value. The
# question a reader asks is "does a push select for *this* instance?" so any
# `instance` signal (identifier / inferred-*) reads as `targeted`; `coarse`-only
# is generic always-load; pull-only systems push nothing (`—`).
INSTANCE_SIGNALS = [
    "sig_identifier",
    "sig_inferred_lexical",
    "sig_inferred_embedding",
    "sig_inferred_judgment",
]


def field(name: str):
    """Accessor for a plain CSV field, blank -> em dash."""
    return lambda r: (r[name].strip() or "—")


def targeting(r) -> str:
    """Collapse the read-back signal one-hots to —/coarse/targeted."""
    if any(r.get(s, "").strip() == "1" for s in INSTANCE_SIGNALS):
        return "targeted"
    if r.get("sig_coarse", "").strip() == "1":
        return "coarse"
    return "—"


def yes_dash(name: str):
    """Accessor for a one-hot flag rendered as yes / em dash."""
    return lambda r: "yes" if r.get(name, "").strip() == "1" else "—"


# Display columns: (header, accessor). System name is handled separately (linked).
# Curation, the full authority set, and the raw signal one-hots stay in systems.csv;
# here `Enforces` is the one authority mode that actually discriminates (validate /
# rank / learn are near-universal), and `Targeting` collapses the signal.
COLUMNS = [
    ("What it is", field("one_line")),
    ("Storage", field("storage_substrate")),
    ("Read-back", field("read_back_direction")),
    ("Targeting", targeting),
    ("Learns from traces", field("trace_learning")),
    ("Enforces", yes_dash("auth_enforcement")),
]

FRONTMATTER = """\
---
description: "Generated comparison table for code-reviewed agent memory systems: one-line summaries plus storage, read-back, targeting, trace-learning, and enforcement."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
---
"""

SUMMARY = """\
# Agent memory systems comparison table

A scannable view of the code-reviewed systems in this collection, generated from
[`systems.csv`](./systems.csv). Lightweight (doc-only) reviews are excluded — a
comparison table is for *choosing* a system, and that calls for code-grounded
evidence. Click any column header to sort (in the rendered HTML site; on GitHub
the [raw matrix](./systems.csv) is itself a sortable, searchable viewer).

This is the human view: one decision per cell. The raw [`systems.csv`](./systems.csv)
keeps the full one-hot flag sets (every authority mode, every curation operation,
every read-back signal); here each collapses to its single discriminating value,
and a plain-English description leads.

For the findings across the whole population, see the
[comparison](./agentic-memory-systems-comparative-review.md).

## How to read the columns

- **What it is** — a one-line description of the system, lifted from its review.
  Scan this first; the rest of the row tells you *how* it works.
- **Storage** — where memory physically lives: plain `files`, a git `repo`,
  `sqlite`, an `rdbms`, a `vector` or `graph` store, `kv`, `in-memory`, or
  `model-weights`. It sets the operational floor — inspectability and diffability
  at one end, scale and query power at the other. Files-family still leads, but
  roughly a third are database-backed, and the most common database is plain
  SQLite, not a vector or graph store.
- **Read-back** — how remembered material reaches the next action: the agent
  *pulls* it with an explicit lookup, the system *pushes* it in unasked, or
  *both*. The first question to ask, because it decides whether the agent has to
  remember to look or whether context arrives on its own.
- **Targeting** — for systems that push, *how* the push selects what to inject:
  `coarse` (always-load / session-start, generic recall) versus `targeted` (the
  push selects for *this* instance — an identifier match, or relevance inferred
  from content by keyword, embedding, or LLM judgment). Pull-only systems push
  nothing (`—`). The raw signal one-hots behind this live in the matrix.
- **Learns from traces** — whether memory is mined automatically from the agent's
  own execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems do — and they overwhelmingly push or do both, so
  automatic learning and automatic activation tend to ship together.
- **Enforces** — whether the stored memory ever acts as a **hard gate** (a check
  the agent can't bypass — a validation that must pass, a blocking rule, a
  required proof) rather than advisory context it can override. This is the
  *enforcement* mode of behavioral authority — nothing to do with authentication.
  The other authority modes (instruction, routing, validation, ranking, learning)
  are near-universal and so don't discriminate; they stay in the matrix.

Curation operations and the full authority and signal flag sets are dropped from
this compact view; they live in [`systems.csv`](./systems.csv).
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
        cells += [accessor(r) for _, accessor in COLUMNS]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
