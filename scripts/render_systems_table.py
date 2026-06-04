#!/usr/bin/env python3
"""Render the human-readable comparison table from systems.csv.

Emits kb/agent-memory-systems/systems-table.md: a sortable (in the MkDocs HTML
build) GFM table over the code-reviewed systems, plus a short summary of the
dimensions. Generated, not hand-maintained -- rebuild after systems.csv changes:

    python3 scripts/build_systems_matrix.py    # refresh the matrix first
    python3 scripts/render_systems_table.py    # then re-render this table

Only the columns the matrix fills reliably enough to compare across the whole
population earn a place (see scripts/analyze_matrix.py). Authority and curation
are rendered as collapsed flag-set profiles (discriminating modes only);
representational-form component columns stay in the raw matrix.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COLLECTION = REPO_ROOT / "kb" / "agent-memory-systems"
SYSTEMS_CSV = COLLECTION / "systems.csv"
OUT = COLLECTION / "systems-table.md"

# Authority and curation are sets of one-hot flags, not single fields. Each column
# below collapses to the *discriminating* flags only — the near-universal authority
# modes (knowledge 100%, instruction 95%, routing 91%) and near-constant curation
# ops (synthesize/promote 88%) are dropped so the cell shows signal, not noise.
AUTH_MODES = [
    ("enforce", "auth_enforcement"),
    ("validate", "auth_validation"),
    ("rank", "auth_ranking"),
    ("learn", "auth_learning"),
]
CURATION_OPS = [
    ("consolidate", "op_consolidate"),
    ("dedup", "op_dedup"),
    ("evolve", "op_evolve"),
    ("invalidate", "op_invalidate"),
    ("decay", "op_decay"),
]
# Read-back targeting lives in the signal one-hots: `coarse` (generic recall) vs an
# `instance` signal (identifier / inferred). An instance signal *is* a targeted push;
# there is no separate "engineered push" flag.
SIGNAL_MODES = [
    ("coarse", "sig_coarse"),
    ("identifier", "sig_identifier"),
    ("inferred-lexical", "sig_inferred_lexical"),
    ("inferred-embedding", "sig_inferred_embedding"),
    ("inferred-judgment", "sig_inferred_judgment"),
]


def field(name: str):
    """Accessor for a plain CSV field, blank -> em dash."""
    return lambda r: (r[name].strip() or "—")


def flag_profile(flags: list[tuple[str, str]]):
    """Accessor collapsing a one-hot flag set to a '+'-joined list of active modes."""
    return lambda r: "+".join(lab for lab, f in flags if r.get(f, "").strip() == "1") or "—"


# Display columns: (header, accessor). System name is handled separately (linked).
COLUMNS = [
    ("Storage substrate", field("storage_substrate")),
    ("Read-back", field("read_back_direction")),
    ("Read-back signal", flag_profile(SIGNAL_MODES)),
    ("Trace-derived", field("trace_derived")),
    ("Authority", flag_profile(AUTH_MODES)),
    ("Curation", flag_profile(CURATION_OPS)),
]

FRONTMATTER = """\
---
description: "Auto-generated sortable comparison table of the code-reviewed agent memory systems across the matrix fields filled reliably enough to compare — storage substrate, read-back direction, read-back signal (coarse vs instance targeting), trace-derived learning, behavioral authority, and curation operations. Rebuild with scripts/render_systems_table.py."
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
- **Read-back signal** — *how* a push selects what to inject: `coarse` (always-load /
  session-start, generic recall) versus an `instance` signal — an `identifier` match
  or `inferred` relevance (lexical / embedding / judgment). An instance signal *is* a
  targeted push; coarse is not; pull-only shows none. Targeting lives here, in one
  place — there is no separate "engineered push" flag.
- **Trace-derived** — whether memory is mined automatically from the agent's own
  execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems are trace-derived — and they overwhelmingly push or
  do both, so automatic learning and automatic activation tend to ship together.
- **Authority** — with what force the stored memory acts on the agent, beyond the
  baseline. Every system carries *knowledge* authority and nearly all add
  *instruction* and *routing*, so those are assumed and omitted; the cell shows
  only the discriminating modes: *enforce* (a hard gate the agent can't ignore),
  *validate* (checks writes against rules), *rank* (influences retrieval order),
  and *learn* (feeds back into the system's own behavior). A dash means
  advisory-only — knowledge and instruction, nothing stronger.
- **Curation** — which upkeep operations the system runs over stored memory.
  *Synthesize* and *promote* are near-universal and omitted; the cell shows the
  discriminating ops: *consolidate* (merge related entries), *dedup* (drop
  duplicates), *evolve* (rewrite entries in place), *invalidate* (mark stale),
  and *decay* (age out by time or use). A dash means write-once memory with no
  active upkeep.

Representational form is omitted from this compact view while the component
one-hot retrofit proceeds. The raw matrix carries `form_prose`, `form_symbolic`,
and `form_parametric` columns. The full agency and curation flag sets — including
the near-universal modes assumed away above — also live in the raw matrix.
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
