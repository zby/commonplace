"""Report ``verbatim``-quote verification over a corpus.

``commonplace-validate`` fails a note whose ``verbatim`` claim is false. This
command is the corpus-wide view: it reports match / mismatch / unresolved
counts across many files, which is what an audit or a before/after sweep needs.

Exits nonzero when any mismatch is found.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from commonplace.lib.quote_verification import (
    display_path,
    markdown_files,
    verify_note,
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="+", type=Path, help="Markdown files or directories"
    )
    parser.add_argument(
        "--show-matches", action="store_true", help="print successful checks too"
    )
    args = parser.parse_args(argv)

    files = markdown_files(args.paths)
    results = [result for note in files for result in verify_note(note)]

    visible = results if args.show_matches else [r for r in results if r.status != "match"]
    for result in visible:
        source = f" -> {display_path(result.source)}" if result.source else ""
        quote = f": {result.quote!r}" if result.quote else ""
        print(
            f"{result.status.upper()} {display_path(result.note)}:{result.line}{source}{quote}"
        )
        if result.detail:
            print(f"  {result.detail}")

    counts = {
        status: sum(r.status == status for r in results)
        for status in ("match", "mismatch", "unresolved")
    }
    print(
        f"Checked {len(files)} Markdown files: "
        f"{counts['match']} match, {counts['mismatch']} mismatch, "
        f"{counts['unresolved']} unresolved."
    )
    return 1 if counts["mismatch"] else 0


if __name__ == "__main__":
    sys.exit(main())
