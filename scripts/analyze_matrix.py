"""Analyze memory comparison values directly from retained main-review results.

Only code-grounded rows with wired, observed, or causally supported values
enter value statistics. Other assessments and weaker bases are reported apart.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path

from commonplace.lib.systems_matrix import AXES, load_results

REPO_ROOT = Path(__file__).resolve().parent.parent
# Below this fill share a column can't carry the human table yet.
FILL_FLOOR = 0.60
# Above this modal share a column is near-constant -> footnote, not a column.
MODE_CEIL = 0.85
# Above this normalised MI a column pair is near-redundant.
REDUNDANCY_FLOOR = 0.85


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", action="append", type=Path)
    args = parser.parse_args(argv)
    try:
        inputs = load_results(REPO_ROOT, args.review)
        inputs.recheck(REPO_ROOT)
    except (OSError, ValueError, KeyError, UnicodeError) as exc:
        print(f"analysis not produced: {exc}", file=sys.stderr)
        return 1
    selected = [r for r in inputs.rows if r["source_tier"] == "code-grounded"]
    print(
        f"selected: {len(inputs.rows)}; doc-grounded excluded from statistics: {len(inputs.rows) - len(selected)}"
    )
    for path, digest in sorted(inputs.hashes.items()):
        print(f"input: {path} sha256={digest}")
    rows = []
    for row in selected:
        values = {}
        for axis in AXES:
            assessed = row[axis + "_assessment"]
            basis = row[axis + "_basis"]
            values[axis] = (
                json.dumps(json.loads(row[axis]), separators=(",", ":"))
                if assessed == "known"
                and basis in {"wired", "observed", "causally supported"}
                else "none"
                if assessed == "absent"
                else ""
            )
        rows.append(values)
    for axis in AXES:
        dispositions = Counter(
            row[axis + "_assessment"] + ":" + row[axis + "_basis"] for row in selected
        )
        print(f"assessment {axis}: {dict(sorted(dispositions.items()))}")
    n = len(rows)
    analytic = list(AXES)

    print(f"rows: {n}  (code-grounded main-review results only)\n")
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
        top, topn = counts.most_common(1)[0] if counts else ("", 0)
        topshare = (topn / len(nonempty)) if nonempty else 0.0
        print(
            f"{c:24} {fill:6.0%} {ndist:5d} {ent:8.2f}  {top or '-'} ({topshare:.0%})"
        )
        if fill < FILL_FLOOR:
            low_fill.append(c)
        elif topshare > MODE_CEIL:
            low_var.append(c)
        else:
            keep.append(c)

    print("\n=== column verdicts (heuristic) ===")
    print(f"candidate human columns ({len(keep)}): {', '.join(keep) or '-'}")
    print(
        f"too sparse to use yet  (<{FILL_FLOOR:.0%} fill): {', '.join(low_fill) or '-'}"
    )
    print(
        f"near-constant -> footnote (>{MODE_CEIL:.0%} one value): {', '.join(low_var) or '-'}"
    )

    print("\n=== near-redundant column pairs (normalised MI) ===")
    found = False
    for i, x in enumerate(keep):
        for y in keep[i + 1 :]:
            mi = mutual_info_norm([r[x] for r in rows], [r[y] for r in rows])
            if mi >= REDUNDANCY_FLOOR:
                print(f"  {x} ~ {y}   MI={mi:.2f}  (keep the more legible one)")
                found = True
    if not found:
        print("  (none above threshold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
