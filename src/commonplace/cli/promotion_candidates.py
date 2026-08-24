"""Generate a promotion candidates report for kb/notes/."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from commonplace.lib.promotion import write_promotion_candidates_report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
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
