"""Build a memory comparison matrix directly from retained main-review results.

Run: uv run python scripts/build_systems_matrix.py [--review kb/agentic-systems/reviews/name.md]
Default: every generated main review. Missing evidence or fields fail the build.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.agentic_publication import _atomic_write
from commonplace.lib.systems_matrix import csv_text, load_results

REPO_ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_CSV = REPO_ROOT / "kb/agentic-systems/comparisons/memory-systems.csv"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", action="append", type=Path)
    parser.add_argument("--output", type=Path, default=SYSTEMS_CSV)
    args = parser.parse_args(argv)
    try:
        inputs = load_results(REPO_ROOT, args.review)
        content = csv_text(inputs)
        inputs.recheck(REPO_ROOT)
        _atomic_write(args.output, content.encode("utf-8"))
    except (OSError, ValueError, KeyError, UnicodeError) as exc:
        print(f"matrix not written: {exc}", file=sys.stderr)
        return 1
    print(
        f"rows written: {len(inputs.rows)}; code-grounded: {sum(r['source_tier'] == 'code-grounded' for r in inputs.rows)}; doc-grounded: {sum(r['source_tier'] == 'doc-grounded' for r in inputs.rows)}"
    )
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
