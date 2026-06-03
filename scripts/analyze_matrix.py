#!/usr/bin/env python3
"""Preliminary analysis of the wide comparison matrix (systems.csv).

Informs which columns earn a place in the human-readable comparison table.
Reports, per column:

  - fill   : share of rows with a non-empty value (low fill -> CSV-only, not a column)
  - values : distinct value count
  - top    : modal value and its share (high share = low variance -> footnote, not a column)
  - entropy: normalised Shannon entropy over non-empty values (0 = all-same, 1 = uniform)

Then flags redundancy: column pairs whose values are near-perfectly predictable
from each other (normalised mutual information), where keeping one would do.

Reads kb/agent-memory-systems/systems.csv. Run:  python3 scripts/analyze_matrix.py
"""
from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_CSV = REPO_ROOT / "kb" / "agent-memory-systems" / "systems.csv"

# Identity/free-text columns are not analytic axes; skip them in the variance pass.
SKIP = {"system_name", "review_file", "public_repo", "clone_path", "one_line",
        "representational_form", "read_back_notes", "source_tier"}

# Below this fill share a column can't carry the human table yet.
FILL_FLOOR = 0.60
# Above this modal share a column is near-constant -> footnote, not a column.
MODE_CEIL = 0.85
# Above this normalised MI a column pair is near-redundant.
REDUNDANCY_FLOOR = 0.85


def load() -> tuple[list[str], list[dict[str, str]]]:
    with SYSTEMS_CSV.open(encoding="utf-8") as fh:
        r = csv.DictReader(fh)
        return r.fieldnames or [], list(r)


def entropy(counts: list[int]) -> float:
    n = sum(counts)
    if n <= 1 or len(counts) <= 1:
        return 0.0
    h = -sum((c / n) * math.log2(c / n) for c in counts if c)
    return h / math.log2(len(counts))


def mutual_info_norm(a: list[str], b: list[str]) -> float:
    """Normalised MI over rows where BOTH columns are non-empty."""
    pairs = [(x, y) for x, y in zip(a, b) if x and y]
    n = len(pairs)
    if n < 5:
        return 0.0
    ca, cb, cab = Counter(), Counter(), Counter()
    for x, y in pairs:
        ca[x] += 1
        cb[y] += 1
        cab[(x, y)] += 1
    mi = 0.0
    for (x, y), nxy in cab.items():
        pxy = nxy / n
        mi += pxy * math.log2(pxy / ((ca[x] / n) * (cb[y] / n)))
    hx = -sum((c / n) * math.log2(c / n) for c in ca.values())
    hy = -sum((c / n) * math.log2(c / n) for c in cb.values())
    denom = min(hx, hy)
    return mi / denom if denom > 0 else 0.0


def main() -> int:
    cols, all_rows = load()
    rows = [r for r in all_rows if r.get("source_tier") == "repo-reviewed"]
    n = len(rows)
    analytic = [c for c in cols if c not in SKIP]

    print(f"rows: {n}  (code-backed reviews only)\n")
    print(f"{'column':24} {'fill':>6} {'vals':>5} {'entropy':>8}  top-value (share)")
    print("-" * 72)
    keep, low_fill, low_var = [], [], []
    for c in analytic:
        vals = [r[c].strip() for r in rows]
        nonempty = [v for v in vals if v]
        fill = len(nonempty) / n if n else 0.0
        counts = Counter(nonempty)
        ndist = len(counts)
        ent = entropy(list(counts.values()))
        top, topn = (counts.most_common(1)[0] if counts else ("", 0))
        topshare = (topn / len(nonempty)) if nonempty else 0.0
        print(f"{c:24} {fill:6.0%} {ndist:5d} {ent:8.2f}  {top or '-'} ({topshare:.0%})")
        if fill < FILL_FLOOR:
            low_fill.append(c)
        elif topshare > MODE_CEIL:
            low_var.append(c)
        else:
            keep.append(c)

    print("\n=== column verdicts (heuristic) ===")
    print(f"candidate human columns ({len(keep)}): {', '.join(keep) or '-'}")
    print(f"too sparse to use yet  (<{FILL_FLOOR:.0%} fill): {', '.join(low_fill) or '-'}")
    print(f"near-constant -> footnote (>{MODE_CEIL:.0%} one value): {', '.join(low_var) or '-'}")

    print("\n=== near-redundant column pairs (normalised MI) ===")
    found = False
    for i, x in enumerate(keep):
        for y in keep[i + 1:]:
            mi = mutual_info_norm([r[x] for r in rows], [r[y] for r in rows])
            if mi >= REDUNDANCY_FLOOR:
                print(f"  {x} ~ {y}   MI={mi:.2f}  (keep the more legible one)")
                found = True
    if not found:
        print("  (none above threshold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
