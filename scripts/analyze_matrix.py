"""Summarize memory comparison evidence directly from retained analysis sets.

Per axis: assessment counts, evidence bases, values with strong positive
evidence (wired, observed or causally supported) in code-grounded rows, and
the distribution of complete strong profiles. Doc-grounded rows are excluded
from the counts; weaker bases and non-positive assessments are reported
apart and never read as absence. Revisions are reported separately; revision 2
basis counts describe unit findings, not the strongest union witness.
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
    versions = sorted({row["comparison_version"] for row in selected})
    for version in versions:
        cohort = [row for row in selected if row["comparison_version"] == version]
        print(f"comparison version {version}: {len(cohort)} code-grounded rows (not pooled across revisions)")
        for axis in AXES:
            dispositions = Counter(row[axis + "_assessment"] for row in cohort)
            bases = Counter()
            for row in cohort:
                if version == 2:
                    # Count actual unit findings, including weaker alternative routes.
                    for unit in row[axis + "_units"]:
                        for finding in unit["findings"]:
                            bases[unit["assessment"] + ":" + finding["basis"]] += 1
                else:
                    for support in row[axis + "_evidence"].values():
                        bases[row[axis + "_assessment"] + ":" + support["basis"]] += 1
            positives = Counter(
                value for row in cohort for value in supported_values(row, axis)
            )
            profiles = Counter(
                profile
                for row in cohort
                if (profile := complete_values(row, axis)) is not None
            )
            complete = sum(profiles.values())
            shown = {",".join(p) or "none": n for p, n in sorted(profiles.items())}
            print(
                f"assessment {axis}: {dict(sorted(dispositions.items()))}; finding bases: {dict(sorted(bases.items()))}"
            )
            print(
                f"supported {axis}: {dict(sorted(positives.items()))} / {len(cohort)} selected code-grounded systems (positive evidence only; remainder is not absence)"
            )
            print(
                f"complete {axis}: {complete} of {len(cohort)} rows have a complete strong profile; profiles: {shown}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
