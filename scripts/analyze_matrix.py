"""Summarize memory comparison evidence directly from retained analysis sets.

Per axis: assessment counts, evidence bases, values with strong positive
evidence (wired, observed or causally supported) in code-grounded rows, and
the distribution of complete strong profiles. Doc-grounded rows are excluded
from the counts; weaker bases and non-positive assessments are reported
apart and never read as absence.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from commonplace.lib.systems_matrix import (
    AXES,
    complete_values,
    load_results,
    supported_values,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", action="append", type=Path)
    args = parser.parse_args(argv)
    try:
        inputs = load_results(REPO_ROOT, args.review)
    except (OSError, ValueError, KeyError, UnicodeError) as exc:
        print(f"analysis not produced: {exc}", file=sys.stderr)
        return 1
    selected = [r for r in inputs.rows if r["source_tier"] == "code-grounded"]
    print(
        f"selected: {len(inputs.rows)}; doc-grounded excluded from statistics: {len(inputs.rows) - len(selected)}"
    )
    for path, digest in sorted(inputs.hashes.items()):
        print(f"input: {path} sha256={digest}")
    print(f"code-grounded rows: {len(selected)}")
    for axis in AXES:
        dispositions = Counter(row[axis + "_assessment"] for row in selected)
        bases = Counter(
            row[axis + "_assessment"] + ":" + support["basis"]
            for row in selected
            for support in row[axis + "_evidence"].values()
        )
        positives = Counter(
            value for row in selected for value in supported_values(row, axis)
        )
        profiles = Counter(
            profile
            for row in selected
            if (profile := complete_values(row, axis)) is not None
        )
        complete = sum(profiles.values())
        shown = {",".join(p) or "none": n for p, n in sorted(profiles.items())}
        print(
            f"assessment {axis}: {dict(sorted(dispositions.items()))}; value bases: {dict(sorted(bases.items()))}"
        )
        print(
            f"supported {axis}: {dict(sorted(positives.items()))} / {len(selected)} selected code-grounded systems (positive evidence only; remainder is not absence)"
        )
        print(
            f"complete {axis}: {complete} of {len(selected)} rows have a complete strong profile; profiles: {shown}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
