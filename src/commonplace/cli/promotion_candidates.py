#!/usr/bin/env python3
"""Generate a promotion candidates report for kb/notes/."""

from __future__ import annotations

import sys
from pathlib import Path

from commonplace.lib.promotion import write_promotion_candidates_report


def main() -> int:
    root = Path.cwd().resolve()
    try:
        result = write_promotion_candidates_report(root)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(
        f"Wrote {result.output} ({result.text_count} unstructured text files, "
        f"{result.invalid_count} invalid frontmatter files)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
